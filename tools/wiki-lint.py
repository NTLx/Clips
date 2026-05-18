#!/usr/bin/env python3
"""
Clips Wiki 校验与同步门禁。

本脚本保证 LLM Wiki 作为普通 Obsidian/Quartz Markdown 可正常工作：
- 校验 YAML frontmatter 与 ISO 日期字段
- 检测会触发 Obsidian MathJax 的裸露美元符号
- 用真实文件校验 wikilink 与 source_raw 目标
- 检查 index.md 统计漂移
- 检查 entity/comparison 必填元数据
- 报告仍需编译的 raw 文件

用法:
  python3 tools/wiki-lint.py
  python3 tools/wiki-lint.py --fix-index
  python3 tools/wiki-lint.py --write-report
  python3 tools/wiki-lint.py --fix-index --write-report
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Iterable

import yaml


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
RAW = ROOT / "raw"
INDEX = ROOT / "index.md"
LINT_REPORT = WIKI / "lint-report.md"

COUNT_LABELS = {
    "Entity 页面": ("entities", WIKI / "entities"),
    "Topic 页面": ("topics", WIKI / "topics"),
    "Comparison 页面": ("comparisons", WIKI / "comparisons"),
    "Raw 文章": ("raw", RAW),
    "Output 作品": ("outputs", WIKI / "outputs"),
}

STANDARD_ENTITY_SECTIONS = (
    "## 关键数据点",
    "## 前提与局限性",
    "## 关联概念",
)

DATE_FIELDS = ("published", "created", "updated", "date", "validated_at")
ZERO_WIDTH = ("\ufeff", "\u200b", "\u200c", "\u200d", "\u2060")


@dataclass(frozen=True)
class Issue:
    category: str
    path: Path
    line: int | None
    message: str
    blocking: bool = True

    def rel(self) -> str:
        return self.path.relative_to(ROOT).as_posix()


def markdown_files() -> list[Path]:
    files = [INDEX, ROOT / "README.md"]
    files.extend(sorted(RAW.glob("*.md")))
    files.extend(sorted(WIKI.rglob("*.md")))
    return [p for p in files if p.exists()]


def wiki_link_files() -> list[Path]:
    files = [INDEX]
    files.extend(sorted(WIKI.rglob("*.md")))
    return [p for p in files if p.exists()]


def wiki_targets() -> tuple[set[str], set[str]]:
    files = markdown_files()
    stems = {p.stem for p in files}
    rels = {p.relative_to(ROOT).with_suffix("").as_posix() for p in files}
    return stems, rels


def frontmatter(text: str) -> tuple[str | None, int]:
    if not text.startswith("---\n"):
        return None, 0
    end = text.find("\n---", 4)
    if end == -1:
        return None, 0
    return text[4:end], text[:end].count("\n") + 1


def load_frontmatter(path: Path) -> tuple[dict, Issue | None]:
    text = path.read_text(encoding="utf-8", errors="replace")
    raw, _ = frontmatter(text)
    if raw is None:
        return {}, None
    try:
        data = yaml.safe_load(raw) or {}
    except yaml.YAMLError as exc:
        return {}, Issue("frontmatter", path, 1, f"YAML 解析失败: {exc}")
    if not isinstance(data, dict):
        return {}, Issue("frontmatter", path, 1, "frontmatter 必须是 YAML mapping")
    return data, None


def strip_code(text: str) -> str:
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"`[^`\n]*`", "", text)
    return text


def strip_fenced_code(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.S)


def strip_code_preserve_lines(text: str) -> str:
    lines = []
    in_fence = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            lines.append("")
            continue
        if in_fence:
            lines.append("")
        else:
            lines.append(remove_inline_code(line))
    return "\n".join(lines)


def remove_inline_code(line: str) -> str:
    out: list[str] = []
    in_code = False
    code_ticks = 0
    i = 0
    while i < len(line):
        if line[i] == "`":
            j = i
            while j < len(line) and line[j] == "`":
                j += 1
            run = j - i
            if not in_code:
                in_code = True
                code_ticks = run
            elif run >= code_ticks:
                in_code = False
                code_ticks = 0
            i = j
            continue
        if not in_code:
            out.append(line[i])
        i += 1
    return "".join(out)


def has_bare_dollar(line: str) -> bool:
    in_code = False
    code_ticks = 0
    i = 0
    while i < len(line):
        if line[i] == "`":
            j = i
            while j < len(line) and line[j] == "`":
                j += 1
            run = j - i
            if not in_code:
                in_code = True
                code_ticks = run
            elif run >= code_ticks:
                in_code = False
                code_ticks = 0
            i = j
            continue
        if line[i] == "$" and not in_code and (i == 0 or line[i - 1] != "\\"):
            return True
        i += 1
    return False


def split_wikilink(raw: str) -> str:
    value = raw.replace(r"\|", "|")
    target = value.split("|", 1)[0].strip()
    target = target.split("#", 1)[0].strip()
    if target.endswith(".md"):
        target = target[:-3]
    return target.strip("/")


def target_exists(target: str, stems: set[str], rels: set[str]) -> bool:
    if not target:
        return True
    return target in stems or target in rels


def line_number(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def check_frontmatter_and_dates(paths: Iterable[Path]) -> list[Issue]:
    issues: list[Issue] = []
    iso = re.compile(r"^\d{4}-\d{2}-\d{2}$")

    for path in paths:
        text = path.read_text(encoding="utf-8", errors="replace")
        data, err = load_frontmatter(path)
        if err:
            issues.append(err)
            continue

        raw, _ = frontmatter(text)
        if raw:
            for i, line in enumerate(raw.splitlines(), 2):
                stripped = line.strip()
                if not stripped or stripped.startswith("#"):
                    continue
                if stripped.count('"') > 2 and not re.search(r'\\"', stripped):
                    issues.append(
                        Issue(
                            "frontmatter",
                            path,
                            i,
                            "双引号标量内疑似包含未转义双引号，Quartz/YAML 可能解析失败",
                        )
                    )

        for field in DATE_FIELDS:
            if field not in data:
                continue
            value = data[field]
            if value is None:
                issues.append(Issue("date", path, None, f"{field} 不能为空"))
            elif isinstance(value, (date, datetime)):
                continue
            elif not isinstance(value, str) or not iso.match(value):
                issues.append(Issue("date", path, None, f"{field} 必须为 YYYY-MM-DD: {value!r}"))

    return issues


def check_hidden_chars(paths: Iterable[Path]) -> list[Issue]:
    issues: list[Issue] = []
    for path in paths:
        text = path.read_text(encoding="utf-8", errors="replace")
        for char in ZERO_WIDTH:
            pos = text.find(char)
            if pos >= 0:
                issues.append(Issue("hidden-char", path, line_number(text, pos), f"发现隐藏字符 U+{ord(char):04X}"))
    return issues


def check_dollars(paths: Iterable[Path]) -> list[Issue]:
    issues: list[Issue] = []
    for path in paths:
        text = path.read_text(encoding="utf-8", errors="replace")
        in_fence = False
        for i, line in enumerate(text.splitlines(), 1):
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            if has_bare_dollar(line):
                issues.append(Issue("mathjax", path, i, "发现裸露 $，需用反引号包裹或反斜杠转义"))
    return issues


def check_wikilinks(paths: Iterable[Path]) -> list[Issue]:
    issues: list[Issue] = []
    stems, rels = wiki_targets()

    for path in paths:
        text = path.read_text(encoding="utf-8", errors="replace")
        stripped = strip_code_preserve_lines(text)
        for match in re.finditer(r"!?\[\[([^\]]+)\]\]", stripped):
            raw = match.group(1)
            target = split_wikilink(raw)
            if not target_exists(target, stems, rels):
                issues.append(
                    Issue(
                        "wikilink",
                        path,
                        line_number(stripped, match.start()),
                        f"链接目标不存在: [[{raw}]]",
                    )
                )
    return issues


def as_list(value) -> list:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def check_source_raw() -> list[Issue]:
    issues: list[Issue] = []
    stems, rels = wiki_targets()

    for path in sorted(WIKI.rglob("*.md")):
        data, err = load_frontmatter(path)
        if err or not data:
            continue
        for item in as_list(data.get("source_raw")):
            if not isinstance(item, str) or not item.startswith("[[") or not item.endswith("]]"):
                issues.append(Issue("source_raw", path, None, f"source_raw 必须使用 wikilink 短链接: {item!r}"))
                continue
            target = split_wikilink(item[2:-2])
            if not target_exists(target, stems, rels):
                issues.append(Issue("source_raw", path, None, f"source_raw 目标不存在: {item}"))
    return issues


def check_entities() -> list[Issue]:
    issues: list[Issue] = []
    for path in sorted((WIKI / "entities").glob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        data, err = load_frontmatter(path)
        if err:
            continue

        tags = {str(t) for t in as_list(data.get("tags"))}
        is_person = "person" in tags

        for field in ("title", "aliases", "definition", "source_raw"):
            if field not in data or data[field] in (None, "", []):
                issues.append(Issue("entity", path, None, f"Entity 缺少必填字段: {field}"))

        if is_person:
            for field in ("validated_source", "validated_at"):
                if field not in data or data[field] in (None, "", []):
                    issues.append(Issue("entity", path, None, f"作者 Entity 缺少字段: {field}"))
        else:
            for section in STANDARD_ENTITY_SECTIONS:
                if section not in text:
                    issues.append(Issue("entity", path, None, f"概念 Entity 缺少章节: {section}"))

    return issues


def check_comparisons() -> list[Issue]:
    issues: list[Issue] = []
    for path in sorted((WIKI / "comparisons").glob("*.md")):
        data, err = load_frontmatter(path)
        if err:
            continue
        if "updated" not in data or data["updated"] in (None, ""):
            issues.append(Issue("comparison", path, None, "Comparison 缺少 updated 字段"))
    return issues


def count_md(directory: Path) -> int:
    return len(list(directory.glob("*.md")))


def actual_counts() -> dict[str, int]:
    return {key: count_md(path) for _, (key, path) in COUNT_LABELS.items()}


def check_index_counts() -> list[Issue]:
    issues: list[Issue] = []
    if not INDEX.exists():
        return [Issue("index", INDEX, None, "index.md 不存在")]

    text = INDEX.read_text(encoding="utf-8", errors="replace")
    counts = actual_counts()
    for label, (key, _) in COUNT_LABELS.items():
        match = re.search(rf"\| {re.escape(label)} \| (\d+) 个 \|", text)
        if not match:
            issues.append(Issue("index", INDEX, None, f"索引概览缺少计数行: {label}"))
            continue
        current = int(match.group(1))
        if current != counts[key]:
            issues.append(Issue("index", INDEX, line_number(text, match.start()), f"{label} 计数漂移: index={current}, actual={counts[key]}"))
    return issues


def fix_index_counts() -> bool:
    text = INDEX.read_text(encoding="utf-8")
    original = text
    counts = actual_counts()

    for label, (key, _) in COUNT_LABELS.items():
        text = re.sub(rf"\| {re.escape(label)} \| \d+ 个 \|", f"| {label} | {counts[key]} 个 |", text)
    today = datetime.now().strftime("%Y-%m-%d")
    text = re.sub(r"^updated: \d{4}-\d{2}-\d{2}$", f"updated: {today}", text, count=1, flags=re.M)

    if text != original:
        INDEX.write_text(text, encoding="utf-8")
        return True
    return False


def raw_compile_status() -> tuple[list[Path], list[Path]]:
    compiled: list[Path] = []
    pending: list[Path] = []
    sources_dir = WIKI / "sources"

    for path in sorted(RAW.glob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        compiled_note = sources_dir / f"{path.stem}.md"
        if "## 编译摘要" in text or compiled_note.exists():
            compiled.append(path)
        else:
            pending.append(path)
    return compiled, pending


def collect_issues() -> tuple[list[Issue], dict[str, int], list[Path]]:
    paths = markdown_files()
    issues: list[Issue] = []
    issues.extend(check_frontmatter_and_dates(paths))
    issues.extend(check_hidden_chars(paths))
    issues.extend(check_dollars(paths))
    issues.extend(check_wikilinks(wiki_link_files()))
    issues.extend(check_source_raw())
    issues.extend(check_entities())
    issues.extend(check_comparisons())
    issues.extend(check_index_counts())

    compiled, pending = raw_compile_status()
    stats = actual_counts()
    stats["raw_compiled"] = len(compiled)
    stats["raw_pending"] = len(pending)
    return issues, stats, pending


def group_issues(issues: Iterable[Issue]) -> dict[str, list[Issue]]:
    grouped: dict[str, list[Issue]] = {}
    for issue in issues:
        grouped.setdefault(issue.category, []).append(issue)
    return grouped


def md_escape_code(value: str) -> str:
    return value.replace("`", "'")


def render_report(issues: list[Issue], stats: dict[str, int], pending: list[Path]) -> str:
    today = datetime.now().strftime("%Y-%m-%d")
    blocking = [i for i in issues if i.blocking]
    score = max(0, 100 - len(blocking))
    status = "PASS" if not blocking else "FAIL"
    grouped = group_issues(issues)

    lines = [
        "---",
        "type: lint-report",
        'title: "Clips Wiki Lint 报告"',
        f'date: "{today}"',
        f"score: {score}",
        f'status: "{status}"',
        "tags:",
        "  - lint-report",
        "  - wiki-maintenance",
        "---",
        "",
        f"# Clips Wiki Lint 报告 - {today}",
        "",
        f"> [!summary] 状态",
        f"> 门禁: **{status}**",
        f"> 分数: **{score}/100**",
        f"> 阻断问题: **{len(blocking)}**",
        "",
        "## 统计",
        "",
        "| 类别 | 数量 |",
        "|------|------|",
        f"| Raw 来源 | {stats['raw']} |",
        f"| Raw 已编译 | {stats['raw_compiled']} |",
        f"| Raw 待编译 | {stats['raw_pending']} |",
        f"| Entity | {stats['entities']} |",
        f"| Topic | {stats['topics']} |",
        f"| Comparison | {stats['comparisons']} |",
        f"| Output | {stats['outputs']} |",
        "",
    ]

    if pending:
        lines.extend(["## 待编译 Raw", ""])
        for path in pending:
            lines.append(f"- `{md_escape_code(path.relative_to(ROOT).as_posix())}`")
        lines.append("")

    lines.extend(["## 检查项", "", "| 检查项 | 问题数 |", "|--------|--------|"])
    for category in ("frontmatter", "date", "hidden-char", "mathjax", "wikilink", "source_raw", "entity", "comparison", "index"):
        lines.append(f"| `{category}` | {len(grouped.get(category, []))} |")
    lines.append("")

    if issues:
        lines.extend(["## 问题明细", ""])
        for category, items in sorted(grouped.items()):
            lines.extend([f"### {category}", ""])
            for issue in items:
                loc = f"{issue.rel()}:{issue.line}" if issue.line else issue.rel()
                lines.append(f"- `{md_escape_code(loc)}` - `{md_escape_code(issue.message)}`")
            lines.append("")
    else:
        lines.extend(["## 问题明细", "", "未发现阻断问题。", ""])

    lines.extend(
        [
            "## 运行命令",
            "",
            "```bash",
            "python3 tools/wiki-lint.py --fix-index --write-report",
            "```",
            "",
            "*本报告由 `tools/wiki-lint.py` 生成。*",
            "",
        ]
    )
    return "\n".join(lines)


def print_summary(issues: list[Issue], stats: dict[str, int], pending: list[Path]) -> None:
    blocking = [i for i in issues if i.blocking]
    print("Clips Wiki Lint")
    print("=" * 60)
    print(f"Raw: {stats['raw']}（已编译 {stats['raw_compiled']}，待编译 {stats['raw_pending']}）")
    print(f"Entity: {stats['entities']} | Topic: {stats['topics']} | Comparison: {stats['comparisons']} | Output: {stats['outputs']}")
    print(f"阻断问题: {len(blocking)}")

    grouped = group_issues(issues)
    for category in sorted(grouped):
        print(f"- {category}: {len(grouped[category])}")

    if pending:
        print("\n待编译 Raw:")
        for path in pending[:20]:
            print(f"- {path.relative_to(ROOT).as_posix()}")
        if len(pending) > 20:
            print(f"... 另有 {len(pending) - 20} 个")

    if issues:
        print("\n前几个问题:")
        for issue in issues[:30]:
            loc = f"{issue.rel()}:{issue.line}" if issue.line else issue.rel()
            print(f"- [{issue.category}] {loc}: {issue.message}")


def main() -> int:
    parser = argparse.ArgumentParser(description="检查并同步 Clips LLM Wiki")
    parser.add_argument("--fix-index", action="store_true", help="更新 index.md 计数和 updated 日期")
    parser.add_argument("--write-report", action="store_true", help="写入 wiki/lint-report.md")
    args = parser.parse_args()

    if args.fix_index:
        changed = fix_index_counts()
        if changed:
            print("已更新 index.md 计数")

    issues, stats, pending = collect_issues()
    print_summary(issues, stats, pending)

    if args.write_report:
        LINT_REPORT.write_text(render_report(issues, stats, pending), encoding="utf-8")
        print(f"\n已写入 {LINT_REPORT.relative_to(ROOT).as_posix()}")

    return 1 if any(i.blocking for i in issues) else 0


if __name__ == "__main__":
    sys.exit(main())
