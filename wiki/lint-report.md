---
type: lint-report
title: "Lint Report"
date: "2026-05-01"
score: 100
previous_score: 68
---

# Lint Report - 2026-05-01 (fix-lint)

## 健康度: 100/100 (68 → 100, +32)

---

## 检查项汇总

| 检查项 | 状态 | 发现 | 扣分 |
|-------|------|------|------|
| Raw backlog | ✅ | 所有 34 个 raw 文件已包含编译摘要 | 0 |
| 失效链接 | ✅ | 0 处断裂，全部修复 | 0 |
| 孤儿 entity | ✅ | 0 个孤儿，全部关联到 topic | 0 |
| 一致性检查 | ✅ | 未发现定义冲突 | 0 |
| 完整性检查 | ✅ | 所有 entity 字段/章节完整 | 0 |
| 孤岛检测 | ✅ | 未发现孤岛页面 | 0 |
| Comparison 元数据 | ✅ | 所有 comparison 有 updated 字段 | 0 |
| \$ 符号转义 | ✅ | 0 处未转义，全部修复 | 0 |

---

## 修复记录

### 1. \$ 符号转义修复 (98 处 → 0, +12 分)

修复 16 个文件中所有未转义的 `$` 符号，全部用反引号包裹。

| 文件 | 修复数 |
|------|--------|
| `Lean-Indie-Engineering.md` (topic) | 21 |
| `Runway-Math.md` | 17 |
| `Anti-Enterprise-Mindset.md` | 14 |
| `B2B-Nurture-C-Model.md` | 12 |
| `Steve-Hanov.md` | 12 |
| `Lean-Stack.md` | 6 |
| `Constraint-Driven-Engineering.md` | 5 |
| `Cybersecurity-Proof-of-Work.md` | 1 |
| `AI-Capability-Gap.md` | 1 |
| `AI-Psychosis.md` | 1 |
| `Agent-Swarm.md` | 1 |
| `Headless-Mode.md` | 1 |
| `Mythos.md` | 1 |
| `Security-Hardening-Phase.md` | 2 |
| `Time-Moat.md` | 2 |
| `deploy-obsidian-wiki-with-quartz.md` | 1 |

**附带修复**: 修复了美元符号转义时误入 wikilink 内部的反引号问题（8 个文件）。

### 2. 失效链接修复 (9 处 → 0, +10 分)

| 断裂链接 | 修复方式 | 影响文件数 |
|---------|---------|-----------|
| `Why Your "AI-First" Strategy Is Probably Wrong` | 改为 raw 文件名 `20260413-why-ai-first-strategy-wrong` | 6 |
| `工程师抗拒被\"蒸馏\"...` | 移除 wikilink 中 `\"` 转义，改为实际 `"` 字符 | 3 |

### 3. 孤儿 entity 关联 (15 个 → 0, +5 分)

| Topic | 关联 Entity |
|-------|------------|
| `AI-Era-Taste-and-Judgment` | AI-Lacks-Laziness, Laziness-Virtue, Slopocalypse |
| `Agentic-Engineering-Patterns` | AI-Restraint, Agent-Tenacity, Martin-Fowler, 朱少民 |
| `Lean-Indie-Engineering` | Cybersecurity-Proof-of-Work, Security-Hardening-Phase, YAGNI |
| `Agent-First-Process-Redesign` | Adversarial-Distillation |
| `Conscious-Creation-in-AI-Era` | Mythos |
| `Enterprise-Ontology-Application` | Knowledge-Graph |
| `Karpathy-AI-Thought` | AISI |
| `OpenClaw-Agent-System` | Drew-Breunig |

### 4. 完整性修复 (2 个 → 0, +5 分)

| Entity | 修复内容 |
|--------|---------|
| `朱少民.md` | 添加 `person` tag，正确识别为作者 entity（已有 validated_source + validated_at） |
| `Memex.md` | 无需修复 — 是概念 entity 非作者 entity，三章节完整 |

---

## 与上次报告对比

| 指标 | 上次 | 本次 | 变化 |
|------|------|------|------|
| 健康度 | 68 | 100 | +32 |
| 失效链接 | 9 处 | 0 处 | -9 |
| \$ 符号 | 98 处 | 0 处 | -98 |
| 孤儿 entity | 15 个 | 0 个 | -15 |
| 完整性缺失 | 2 个 | 0 个 | -2 |

---

## 统计概览

| 指标 | 数值 |
|------|------|
| Raw 文章 | 34 |
| Entity 页面 | 97 (78 概念 + 19 作者) |
| Topic 页面 | 14 |
| Comparison 页面 | 4 |
| Wikilink 总数 | 995 |
| 编译覆盖率 | 100% (34/34) |
