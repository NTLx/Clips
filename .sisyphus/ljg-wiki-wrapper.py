#!/usr/bin/env python3
"""
ljg-wiki-wrapper: 将 ljg 技能输出适配到 Clips LLM Wiki

功能:
  1. 读取 ~/Documents/notes/ 中的 ljg md 输出
  2. 提取元数据，注入 Wiki 标准 YAML frontmatter
  3. 搬运到 wiki/{entities|topics|outputs|comparisons}/
  4. 返回搬运清单供 log.md 记录

用法:
  python3 .sisyphus/ljg-wiki-wrapper.py --skill learn --source-raw "20260408-knowledge-work.md"
  python3 .sisyphus/ljg-wiki-wrapper.py --scan
  python3 .sisyphus/ljg-wiki-wrapper.py --all
"""

import os
import re
import sys
from datetime import datetime
from pathlib import Path

CLIPS_ROOT = Path(os.path.expanduser("~/Obsidian/Clips")).expanduser()
LJG_NOTES_DIR = Path(os.path.expanduser("~/Documents/notes")).expanduser()
TODAY = datetime.now().strftime("%Y-%m-%d")

SKILL_DEST_MAP = {
    "learn": "wiki/entities/",
    "paper": "wiki/entities/",
    "think": "wiki/topics/",
    "rank": "wiki/topics/",
    "writes": "wiki/outputs/",
    "paper-river": "wiki/comparisons/",
}

SKILL_SUFFIX_MAP = {
    "learn": "__concept.md",
    "paper": "__paper.md",
    "think": "__think.md",
    "rank": "__rank.md",
    "writes": "__write.md",
    "paper-river": "__paper_river.md",
}


def kebab_case(text):
    text = text.strip()
    text = re.sub(r"[^\w\u4e00-\u9fff\- ]", "", text)
    parts = text.split()
    kebab_parts = []
    for part in parts:
        if re.match(r"^[\u4e00-\u9fff]+$", part):
            kebab_parts.append(part)
        else:
            kebab_parts.append(part.lower().replace(" ", "-"))
    return "-".join(kebab_parts) if kebab_parts else text


def extract_title(content):
    m = re.search(r"^# (.+)", content, re.MULTILINE)
    if m:
        t = m.group(1).strip()
        t = re.sub(r"(概念解剖|论文解析|追本|降秩)[：:]?\s*", "", t).strip()
        return t if t else "untitled"
    return "untitled"


def extract_definition(content):
    m = re.search(r"^#+ 压缩\s*\n(.*?)(?=^#+|\Z)", content, re.DOTALL | re.MULTILINE)
    if m:
        block = m.group(1).strip()
        s = re.search(r"^#+ 一句话[：:]?\s*(.+)", block, re.MULTILINE)
        if s:
            return s.group(1).strip()
    m = re.search(r"^#+ 定锚\s*\n(.+?)\n", content, re.DOTALL | re.MULTILINE)
    if m:
        line = m.group(1).strip().split("\n")[0].strip()
        if line and len(line) < 200:
            return line
    return ""


def extract_key_data(content):
    points = []
    for section in ["形式", "历史"]:
        m = re.search(
            rf"^#+ {section}\s*\n(.*?)(?=^#+ |\Z)", content, re.DOTALL | re.MULTILINE
        )
        if m:
            points.append(m.group(1).strip())
    return "\n".join(points) if points else ""


def extract_limitations(content):
    parts = []
    for section in ["辩证", "元反思"]:
        m = re.search(
            rf"^#+ {section}\s*\n(.*?)(?=^#+ |\Z)", content, re.DOTALL | re.MULTILINE
        )
        if m:
            parts.append(m.group(1).strip())
    return "\n".join(parts) if parts else ""


def extract_related(content):
    m = re.search(r"^#+ 语言\s*\n(.*?)(?=^#+ |\Z)", content, re.DOTALL | re.MULTILINE)
    if m:
        return re.findall(r"\*\*([^*]+?)\*\*", m.group(1))
    return []


def fm_entity(title, source_raw, definition, related):
    rel_yaml = ""
    for r in related:
        rel_yaml += f'  - "[[{r}]]"\n'
    rel_yaml = rel_yaml.strip() if rel_yaml.strip() else "  - []"
    tags = [
        "  - concept",
    ]
    return (
        f"---\n"
        f"type: entity\n"
        f'title: "{title}"\n'
        f'definition: "{definition}"\n'
        f"created: {TODAY}\n"
        f"updated: {TODAY}\n"
        f"tags:\n"
        f"{'\n'.join(tags)}\n"
        f"related_entities:\n"
        f"{rel_yaml}\n"
        f"source_raw:\n"
        f'  - "[[{source_raw}]]"\n'
        f"---\n"
    )


def fm_topic(title, source_raw):
    return (
        f"---\n"
        f"type: topic\n"
        f'title: "{title}"\n'
        f"created: {TODAY}\n"
        f"updated: {TODAY}\n"
        f"tags:\n"
        f"  - {title}\n"
        f"source_raw:\n"
        f'  - "[[{source_raw}]]"\n'
        f"---\n"
    )


def fm_output(title):
    return (
        f"---\n"
        f"type: output\n"
        f'title: "{title}"\n'
        f"created: {TODAY}\n"
        f"updated: {TODAY}\n"
        f"tags:\n"
        f"  - essay\n"
        f"---\n"
    )


def strip_ljg_header(content):
    for marker in [
        "---\n",
        "name:",
        "description:",
        "skill:",
        "type:",
        "skill_name:",
        "triggers:",
        "examples:",
        "version:",
    ]:
        if marker in content:
            return ""
    return content


def inject_standard_chapters(content, source_raw):
    if "## 关键数据点" not in content:
        content += "\n\n## 关键数据点\n待从 raw 源补充\n"
    if "## 前提与局限性" not in content:
        content += "\n## 前提与局限性\n待补全\n"
    return content


def process_learn(path, source_raw):
    content = path.read_text(encoding="utf-8")
    title = extract_title(content)
    definition = extract_definition(content)
    key_data = extract_key_data(content)
    limitations = extract_limitations(content)
    related = extract_related(content)

    header = fm_entity(title, source_raw, definition, related)
    content = inject_standard_chapters(content, source_raw)

    dest = CLIPS_ROOT / SKILL_DEST_MAP["learn"] / (kebab_case(title) + ".md")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(header + "\n" + content, encoding="utf-8")
    return dest


def process_paper(path, source_raw):
    content = path.read_text(encoding="utf-8")
    title = extract_title(content)
    header = fm_entity(title, source_raw, "来自论文解析", [])

    dest = CLIPS_ROOT / SKILL_DEST_MAP["paper"] / (kebab_case(title) + ".md")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(header + "\n" + content, encoding="utf-8")
    return dest


def process_think(path, source_raw):
    content = path.read_text(encoding="utf-8")
    title = extract_title(content)
    header = fm_topic(title, source_raw)

    dest = CLIPS_ROOT / SKILL_DEST_MAP["think"] / (kebab_case(title) + ".md")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(header + "\n" + content, encoding="utf-8")
    return dest


def process_rank(path, source_raw):
    content = path.read_text(encoding="utf-8")
    title = extract_title(content)
    header = fm_topic(title, source_raw)

    dest = CLIPS_ROOT / SKILL_DEST_MAP["rank"] / (kebab_case(title) + ".md")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(header + "\n" + content, encoding="utf-8")
    return dest


def process_writes(path, source_raw):
    content = path.read_text(encoding="utf-8")
    title = extract_title(content)
    header = fm_output(title)

    dest = CLIPS_ROOT / SKILL_DEST_MAP["writes"] / (kebab_case(title) + ".md")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(header + "\n" + content, encoding="utf-8")
    return dest


def process_paper_river(path, source_raw):
    content = path.read_text(encoding="utf-8")
    title = extract_title(content)
    header = fm_topic(title, source_raw)

    dest = CLIPS_ROOT / SKILL_DEST_MAP["paper-river"] / (kebab_case(title) + ".md")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(header + "\n" + content, encoding="utf-8")
    return dest


PROCESSORS = {
    "learn": process_learn,
    "paper": process_paper,
    "think": process_think,
    "rank": process_rank,
    "writes": process_writes,
    "paper-river": process_paper_river,
}


def scan_pending():
    if not LJG_NOTES_DIR.exists():
        print(f"ljg notes 目录不存在: {LJG_NOTES_DIR}")
        return []

    pending = []
    for skill, suffix in SKILL_SUFFIX_MAP.items():
        files = list(LJG_NOTES_DIR.glob(f"*{suffix}"))
        for f in files:
            title = extract_title(f.read_text(encoding="utf-8"))
            dest_filename = kebab_case(title) + ".md"
            dest_path = CLIPS_ROOT / SKILL_DEST_MAP.get(skill, "wiki/") / dest_filename
            if not dest_path.exists():
                pending.append((f, skill))
            else:
                print(f"已存在，跳过: {dest_path}")
    return pending


def main():
    import argparse

    parser = argparse.ArgumentParser(description="ljg → Clips Wiki Wrapper")
    parser.add_argument(
        "--skill", choices=list(PROCESSORS.keys()), help="要处理的技能类型"
    )
    parser.add_argument("--file", help="指定要处理的文件路径")
    parser.add_argument("--source-raw", help="关联的 raw 源文件名")
    parser.add_argument("--scan", action="store_true", help="扫描待处理文件")
    parser.add_argument("--all", action="store_true", help="处理所有待处理文件")
    args = parser.parse_args()

    if args.scan or args.all:
        pending = scan_pending()
        if not pending:
            print("没有待处理文件")
            return
        print(f"找到 {len(pending)} 个待处理文件:")
        for filepath, skill in pending:
            print(f"  [{skill}] {filepath.name}")

        if args.scan:
            return

        processed = []
        for filepath, skill in pending:
            processor = PROCESSORS.get(skill)
            if processor:
                dest = processor(filepath, filepath.stem.split("--")[0])
                processed.append(dest)
                print(f"✓ → {dest}")
        print(f"\n处理完成: {len(processed)} 个文件")
        return

    if not args.skill:
        parser.print_help()
        return

    processor = PROCESSORS.get(args.skill)
    if not processor:
        print(f"未知技能: {args.skill}")
        sys.exit(1)

    if args.file:
        filepath = Path(args.file)
    else:
        suffix = SKILL_SUFFIX_MAP[args.skill]
        files = sorted(
            LJG_NOTES_DIR.glob(f"*{suffix}"),
            key=lambda f: f.stat().st_mtime,
            reverse=True,
        )
        if not files:
            print(f"未找到 {args.skill} 的输出文件")
            sys.exit(1)
        filepath = files[0]
        print(f"使用最新文件: {filepath.name}")

    source_raw = args.source_raw or "unknown"
    dest = processor(filepath, source_raw)
    print(f"✓ 已处理 → {dest}")


if __name__ == "__main__":
    main()
