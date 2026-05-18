#!/usr/bin/env python3
"""
审计 Clips LLM Wiki 的 Entity 价值。

本脚本刻意与 wiki-lint.py 分离。wiki-lint.py 处理渲染和 schema 的硬错误；
Entity 审计输出需要人工判断的复核/合并队列。

用法:
  python3 tools/entity-audit.py
  python3 tools/entity-audit.py --write-report
"""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
ENTITY_DIR = ROOT / "wiki" / "entities"

BUCKET_LABELS = {
    "keep": "保留",
    "keep-actor": "保留-人物",
    "strengthen": "增强",
    "review": "复核",
    "merge-or-demote": "合并或降级",
}

BUCKET_MEANINGS = {
    "keep": "多源、已有主题承载，或处于图谱中心",
    "keep-actor": "人物/作者类 Entity，已验证则保留",
    "strengthen": "概念有价值，但需要补来源或补链接",
    "review": "单一来源，且缺少 topic/comparison 承载",
    "merge-or-demote": "单一来源且无图谱入链，通常更适合合并或降级为来源内细节",
}


@dataclass
class Entity:
    stem: str
    path: Path
    title: str
    definition: str
    tags: list[str]
    source_count: int
    related_count: int
    body_len: int
    graph_in: int
    topic_in: int
    comparison_in: int
    entity_in: int
    reasons: list[str]
    score: int
    bucket: str


def read_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    try:
        data = yaml.safe_load(text[4:end]) or {}
    except yaml.YAMLError:
        return {}
    return data if isinstance(data, dict) else {}


def as_list(value) -> list:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def wikilink_targets(text: str) -> list[str]:
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    targets: list[str] = []
    for match in re.finditer(r"!?\[\[([^\]]+)\]\]", text):
        target = match.group(1).replace(r"\|", "|").split("|", 1)[0].split("#", 1)[0].strip()
        if target.endswith(".md"):
            target = target[:-3]
        if target.startswith("wiki/entities/"):
            target = target.split("/")[-1]
        targets.append(target)
    return targets


def inbound_maps(entity_stems: set[str]) -> tuple[dict[str, set[str]], dict[str, set[str]], dict[str, set[str]], dict[str, set[str]]]:
    graph: dict[str, set[str]] = defaultdict(set)
    topics: dict[str, set[str]] = defaultdict(set)
    comparisons: dict[str, set[str]] = defaultdict(set)
    entities: dict[str, set[str]] = defaultdict(set)

    for path in (ROOT / "wiki").rglob("*.md"):
        if path.name == "lint-report.md":
            continue
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        for target in wikilink_targets(text):
            if target not in entity_stems or path == ENTITY_DIR / f"{target}.md":
                continue
            graph[target].add(rel)
            if "/topics/" in rel:
                topics[target].add(rel)
            elif "/comparisons/" in rel:
                comparisons[target].add(rel)
            elif "/entities/" in rel:
                entities[target].add(rel)

    return graph, topics, comparisons, entities


def classify(data: dict, body_len: int, graph_in: int, topic_in: int, comparison_in: int, entity_in: int) -> tuple[int, str, list[str]]:
    tags = [str(t) for t in as_list(data.get("tags"))]
    tags_lower = {t.lower() for t in tags}
    source_count = len(as_list(data.get("source_raw")))
    related_count = len(as_list(data.get("related_entities")))
    is_person = "person" in tags_lower

    score = 35
    reasons: list[str] = []

    if is_person:
        score += 25
        reasons.append("人物/作者类 Entity")
    if source_count >= 2:
        score += 20
        reasons.append("多源支撑")
    if topic_in > 0:
        score += 25
        reasons.append("已有 topic 承载")
    if comparison_in > 0:
        score += 15
        reasons.append("已有 comparison 承载")
    if entity_in >= 3:
        score += 10
        reasons.append("Entity 图谱枢纽")
    elif entity_in >= 1:
        score += 5
        reasons.append("已有 Entity 入链")
    if related_count >= 3:
        score += 8
        reasons.append("related_entities 较丰富")
    if body_len >= 1800:
        score += 5
        reasons.append("正文内容较充分")

    if not is_person and source_count <= 1:
        score -= 10
        reasons.append("单一来源")
    if not is_person and topic_in == 0 and comparison_in == 0:
        score -= 12
        reasons.append("缺少 topic/comparison 承载")
    if not is_person and graph_in == 0:
        score -= 18
        reasons.append("无图谱入链")

    score = max(0, min(100, score))

    if is_person:
        bucket = "keep-actor"
    elif graph_in == 0 and source_count <= 1:
        bucket = "merge-or-demote"
    elif source_count <= 1 and topic_in == 0 and comparison_in == 0:
        bucket = "review"
    elif score >= 55:
        bucket = "keep"
    else:
        bucket = "strengthen"

    return score, bucket, reasons


def audit_entities() -> list[Entity]:
    paths = sorted(ENTITY_DIR.glob("*.md"))
    stems = {p.stem for p in paths}
    graph, topics, comparisons, entities = inbound_maps(stems)
    rows: list[Entity] = []

    for path in paths:
        data = read_frontmatter(path)
        text = path.read_text(encoding="utf-8", errors="replace")
        score, bucket, reasons = classify(
            data,
            len(text),
            len(graph[path.stem]),
            len(topics[path.stem]),
            len(comparisons[path.stem]),
            len(entities[path.stem]),
        )
        rows.append(
            Entity(
                stem=path.stem,
                path=path,
                title=str(data.get("title") or path.stem),
                definition=str(data.get("definition") or ""),
                tags=[str(t) for t in as_list(data.get("tags"))],
                source_count=len(as_list(data.get("source_raw"))),
                related_count=len(as_list(data.get("related_entities"))),
                body_len=len(text),
                graph_in=len(graph[path.stem]),
                topic_in=len(topics[path.stem]),
                comparison_in=len(comparisons[path.stem]),
                entity_in=len(entities[path.stem]),
                reasons=reasons,
                score=score,
                bucket=bucket,
            )
        )
    return rows


def render_report(rows: list[Entity]) -> str:
    today = datetime.now().strftime("%Y-%m-%d")
    buckets = defaultdict(list)
    for row in rows:
        buckets[row.bucket].append(row)

    lines = [
        "---",
        "type: audit-report",
        'title: "Entity 价值审计"',
        f'date: "{today}"',
        "tags:",
        "  - audit-report",
        "  - wiki-maintenance",
        "---",
        "",
        f"# Entity 价值审计 - {today}",
        "",
        "## 概览",
        "",
        "| 分组 | 数量 | 含义 |",
        "|--------|-------|---------|",
    ]
    for bucket in ("keep", "keep-actor", "strengthen", "review", "merge-or-demote"):
        lines.append(f"| {BUCKET_LABELS[bucket]} | {len(buckets[bucket])} | {BUCKET_MEANINGS[bucket]} |")

    lines.extend(
        [
            "",
            "## 复核队列",
            "",
            "这些页面不一定是错误条目，但需要人工/Agent 决策：补入 topic、合并到更大的页面，或降级为来源摘要中的细节。",
            "",
            "| Entity | 分数 | 来源数 | 图谱入链 | Topic 入链 | 原因 |",
            "|--------|-------|---------|----------|----------|--------|",
        ]
    )
    for row in sorted(buckets["review"], key=lambda r: (r.score, r.stem)):
        lines.append(
            f"| [[{row.stem}]] | {row.score} | {row.source_count} | {row.graph_in} | {row.topic_in} | {', '.join(row.reasons)} |"
        )

    lines.extend(
        [
            "",
            "## 合并或降级队列",
            "",
            "| Entity | 分数 | 来源数 | 定义 |",
            "|--------|-------|---------|------------|",
        ]
    )
    for row in sorted(buckets["merge-or-demote"], key=lambda r: (r.score, r.stem)):
        definition = row.definition.replace("|", "/")
        lines.append(f"| [[{row.stem}]] | {row.score} | {row.source_count} | {definition} |")

    lines.extend(
        [
            "",
            "## 管控规则",
            "",
            "- 新建 Entity 至少应满足两个正向信号：多源复用、topic/comparison 需要、跨来源冲突、稳定命名概念或高未来查询价值。",
            "- 单一来源的细节默认写入来源摘要或 topic 小节，不默认建立 Entity。",
            "- 工具、产品、组织名只有在多次复用或具有直接架构重要性时才建立 Entity。",
            "- 复核队列中的条目应在维护时补入 topic/comparison，或合并、降级。",
            "",
            "```bash",
            "python3 tools/entity-audit.py --write-report",
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def report_path() -> Path:
    today = datetime.now().strftime("%Y-%m-%d")
    return ROOT / "docs" / f"entity-audit-{today}.md"


def print_summary(rows: list[Entity]) -> None:
    buckets = defaultdict(list)
    for row in rows:
        buckets[row.bucket].append(row)
    print("Entity 价值审计")
    print("=" * 60)
    print(f"Entity 总数: {len(rows)}")
    for bucket in ("keep", "keep-actor", "strengthen", "review", "merge-or-demote"):
        print(f"{BUCKET_LABELS[bucket]}: {len(buckets[bucket])}")
    print("\n合并或降级候选:")
    for row in sorted(buckets["merge-or-demote"], key=lambda r: (r.score, r.stem))[:20]:
        print(f"- {row.stem} (分数={row.score}, 来源数={row.source_count}, 图谱入链={row.graph_in})")
    print("\n复核候选:")
    for row in sorted(buckets["review"], key=lambda r: (r.score, r.stem))[:30]:
        print(f"- {row.stem} (分数={row.score}, 来源数={row.source_count}, 图谱入链={row.graph_in}, Topic 入链={row.topic_in})")


def main() -> int:
    parser = argparse.ArgumentParser(description="审计 Clips LLM Wiki 的 Entity 价值")
    parser.add_argument("--write-report", action="store_true", help="写入 docs/entity-audit-YYYY-MM-DD.md")
    args = parser.parse_args()

    rows = audit_entities()
    print_summary(rows)
    if args.write_report:
        path = report_path()
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render_report(rows), encoding="utf-8")
        print(f"\n已写入 {path.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
