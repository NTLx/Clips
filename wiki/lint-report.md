---
type: lint-report
date: 2026-04-14
---

# Lint Report - 2026-04-14

## 健康度

| 指标 | 初检 | 修复后 | 状态 |
|-----|------|------|------|
| Raw backlog | 0 items | 0 items | 🟢 优秀 |
| 摘要覆盖 | 24/24 (100%) | 24/24 (100%) | 🟢 优秀 |
| 孤儿 entity | 18 items | 0 items | 🟢 已修复 |
| 失效链接 | 1 目标/18 处引用 | 0 items | 🟢 已修复 |
| 孤岛页面 | 1 item (Paul-Graham) | 已修复 | 🟢 已修复 |
| source_raw 缺失 | 8 entities | 0 items | 🟢 已修复 |
| Index 一致性 | 全部一致 | 全部一致 | 🟢 优秀 |
| 作者验证字段 | 1/16 | 16/16 | 🟢 已修复 |
| **总体健康度** | 72/100 | **96/100** | 🟢 |

---

## 本期修复完成

### P0: 失效链接修复 (ASCII vs Unicode 撇号)

> **问题**: wikilinks 中使用 ASCII 撇号 `'` (U+0027)，但 raw 文件名使用 Unicode 右单引号 `'` (U+2019)。**已修复：18 处 → 0 处**。

**涉及文件**:
- `wiki/entities/Connection.md` (2处), `Discernment.md` (2处), `Emotional-Clarity.md` (2处)
- `wiki/entities/Joe-Hudson.md` (3处), `Knowledge-Work.md` (2处), `Wisdom-Work.md` (2处)
- `wiki/comparisons/Knowledge-Work-vs-Wisdom-Work.md` (1处), `wiki/topics/Wisdom-Work-Evolution.md` (2处)

### P0: source_raw 补充（8 个 Entity）

| Entity | source_raw |
|--------|-----------|
| `Claude-Code-CLI` | OpenClaw + 6 个 Agent 运转半个月, OpenClaw + CodexClaudeCode Agent Swarm |
| `Headless-Mode` | OpenClaw + 6 个 Agent 运转半个月, OpenClaw + CodexClaudeCode Agent Swarm |
| `Technical-Debt-Avoidance` | 20260410-better-code |
| `Elvis-Sun` | OpenClaw + CodexClaudeCode Agent Swarm |
| `Ethan-Mollick` | Management as AI superpower |
| `Konstantine-Buhler` | The Always-On Economy AI and the Next 5-7 Years |
| `Paul-Graham` | Taste for Makers, The Brand Age |
| `Raj-Nandan-Sharma` | Good Taste the Only Real Moat Left |

### P1: 孤儿 Entity 消除（18 → 0）

7 个 topic 页面新增 `related_entities` 引用：

| Topic | 新增引用（数量） |
|-------|----------------|
| `AI-Era-Economy-Shift.md` | Aaron-Levie, Ben-Thompson, Ethan-Mollick, Konstantine-Buhler (4) |
| `Building-Effective-Agents.md` | Barry-Zhang, Erik-Schluntz, MIT-Technology-Review-Insights (3) |
| `AI-Era-Taste-and-Judgment.md` | Dan-Shipper, Paul-Graham, Refusal (3) |
| `Wisdom-Work-Evolution.md` | Dan-Shipper, Joe-Hudson, Knowledge-Work (3) |
| `OpenClaw-Agent-System.md` | Elvis-Sun (1) |
| `Agentic-Engineering-Patterns.md` | Raj-Nandan-Sharma, Simon-Willison, Technical-Debt-Avoidance (3) |
| `Claude-Code-Automation.md` | Wes-Botman, 同学都叫我-饶老师 (2) |

### P1: Paul-Graham 孤岛修复

入链=0, 出链=1 → 入链≥1, 出链=4：
- `source_raw:` 补充 `Taste for Makers`, `The Brand Age`
- `related_entities:` 新增 `Taste`, `Judgment`, `Specificity`（共4个）
- AI-Era-Taste-and-Judgment topic 已添加引用

### P2: 作者 Entity 验证字段补充（15/15）

所有 15 个作者 entity 新增 `validated_source` + `validated_at`（含 Dan-Shipper, Ethan-Mollick, Simon-Willison 等 15 人）。

---

## 数据核对

| 指标 | Index 记录 | 实际统计 | 状态 |
|-----|----------|---------|-----|
| Entity 页面 | 58 个 | 58 个 | ✅ |
| Topic 页面 | 12 个 | 12 个 | ✅ |
| Comparison 页面 | 4 个 | 4 个 | ✅ |
| Raw 文章 | 24 个 | 24 个 | ✅ |
| Output 作品 | 1 个 | 1 个 | ✅ |

---

## 变化趋势

| 指标 | 上期 (04-13) | 修复后 (04-14) | 变化 |
|-----|-------------|---------------|------|
| 健康度 | 95/100 | 96/100 | ↑ +1 |
| Entity 数量 | 65 | 58 | -7（清理冗余） |
| Topic 数量 | 11 | 12 | +1 |
| Comparison 数量 | 5 | 4 | -1 |
| Raw 文章 | 28 | 24 | -4 |

---

**健康度评分**: 96/100 🟢

*报告生成: 2026-04-14*
