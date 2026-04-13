---
type: lint-report
date: 2026-04-13
---

# Lint Report - 2026-04-13

## 健康度

| 指标 | 数值 | 状态 |
|-----|------|-----|
| Raw backlog | 0 items | 🟢 优秀 |
| 孤儿 entity | 2 items | 🟡 需关注 |
| 过期 entity | 0 items | 🟢 优秀 |
| 失效链接 | 0 items | 🟢 优秀 |
| Wikilink 格式一致性 | ~35 处 | 🟡 建议改进 |
| **总体健康度** | **95/100** | 🟢 |

---

## ✅ 本期修复完成

### 新增 Entity（2 个）

| Entity | 定义 | 状态 |
|--------|------|------|
| `Knowledge-Work.md` | 以知识为核心价值的工作形态，正在被 AI 取代 | ✅ 已创建 |
| `Technical-Debt-Avoidance.md` | 通过持续改进避免技术债务累积的策略 | ✅ 已创建 |

### 路径漂移修复（19 处）

> **问题**: Entity 文件的 `source_raw` 指向 `inbox/`，但原始文章已移动至 `web-clips/{分类}/`

| 文件 | 修复内容 | 状态 |
|------|---------|------|
| `Simon-Willison.md` | 5 个 source_raw + 5 个内联链接 → web-clips/AI-Agent/ | ✅ |
| `Jevons-Paradox-for-Knowledge-Work.md` | 1 个 source_raw → web-clips/AI-Agent/ | ✅ |
| `逛逛.md` | 1 个 source_raw + 1 个内联链接 → web-clips/Claude-Code/ | ✅ |
| `Always-On-Economy.md` | 1 个 source_raw → web-clips/Knowledge-Work/ | ✅ |
| `Model-Manager.md` | 1 个 source_raw → web-clips/Knowledge-Work/ | ✅ |
| `Vibe-Design.md` | 1 个 source_raw → web-clips/Design/ | ✅ |
| `Agent-Workflow-Patterns.md` | 1 个 source_raw → web-clips/AI-Agent/ | ✅ |
| `Ben-Thompson.md` | 1 个 source_raw + 1 个内联链接 → web-clips/AI-Agent/ | ✅ |
| `Barry-Zhang.md` | 1 个 source_raw + 1 个内联链接 → web-clips/AI-Agent/ | ✅ |
| `编程进阶社.md` | 1 个 source_raw + 1 个内联链接 → web-clips/Design/ | ✅ |
| `ACI-Agent-Computer-Interface.md` | 1 个 source_raw → web-clips/AI-Agent/ | ✅ |
| `Compound-Engineering.md` | 1 个 source_raw → web-clips/AI-Agent/ | ✅ |

**验证结果**: `inbox/` 引用已全部清除 ✅

---

## 🟡 待处理问题

### 1. Wikilink 格式不一致（P1 - 建议）

> **问题**: `related_entities` 使用空格而非连字符，如 `[[Dan Shipper]]` 应为 `[[Dan-Shipper]]`

**影响**: Obsidian 可自动解析，但不符合命名规范，建议统一。

**示例**:
- `[[Dan Shipper]]` → `[[Dan-Shipper]]`
- `[[Simon Willison]]` → `[[Simon-Willison]]`
- `[[Ethan Mollick]]` → `[[Ethan-Mollick]]`

**涉及文件**: 约 20+ entity 文件，35+ 处引用

---

## 孤儿 Entity（低优先级）

| Entity | 建议 |
|--------|------|
| `Vibe-Design.md` | 可关联到 Design 相关 topic |
| `MIT-Technology-Review-Insights.md` | 作者 entity，无需强制关联 |

---

## 数据核对

| 指标 | Index 记录 | 实际统计 | 状态 |
|-----|----------|---------|-----|
| Entity 页面 | 65 个 | 65 个 | ✅ 一致 |
| Topic 页面 | 11 个 | 11 个 | ✅ 一致 |
| Comparison 页面 | 5 个 | 5 个 | ✅ 一致 |
| Raw Sources | - | 29 篇 | ✅ |

---

## 统计摘要

| 分类 | 数量 |
|-----|------|
| AI-Agent 文章 | 12 篇 |
| Claude-Code 文章 | 5 篇 |
| Career-Skills 文章 | 2 篇 |
| Knowledge-Work 文章 | 4 篇 |
| General 文章 | 4 篇 |
| Design 文章 | 1 篇 |
| OpenClaw 文章 | 1 篇 |
| **总计** | **29 篇** |

---

## 变化趋势

| 指标 | 上期 (04-10) | 本期 (04-13) | 变化 |
|-----|-------------|-------------|------|
| 健康度 | 95/100 | 95/100 | 持平 |
| Entity 数量 | 63 | 65 | +2 |
| Topic 数量 | 11 | 11 | 持平 |
| 路径漂移 | 已修复部分 | **全部修复** | ✅ |
| 失效链接 | 0 | 0 | ✅ |

---

## 建议操作

### P1（建议）
1. [ ] 统一 wikilink 格式：`[[Name With Space]]` → `[[Name-With-Space]]`

### P2（可选）
2. [ ] 将 `Vibe-Design.md` 关联到相关 topic

---

**健康度评分**：95/100 🟢

*报告生成: 2026-04-13*