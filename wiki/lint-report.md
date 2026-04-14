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

### 架构简化

> **变更**: 知识库架构从三层简化为两层
> - `00-raw/` → `raw/`（扁平化，无子目录）
> - `10-wiki/` → `wiki/`
> - `docs/` 添加到 `.gitignore`

### 新增 Entity（2 个）

| Entity | 定义 | 状态 |
|--------|------|------|
| `Knowledge-Work.md` | 以知识为核心价值的工作形态，正在被 AI 取代 | ✅ 已创建 |
| `Technical-Debt-Avoidance.md` | 通过持续改进避免技术债务累积的策略 | ✅ 已创建 |

---

## 🟡 待处理问题

### 1. Wikilink 格式不一致（P1 - 建议）

> **问题**: `related_entities` 使用空格而非连字符，如 `[[Dan-Shipper]]` 应为 `[[Dan-Shipper]]`

**影响**: Obsidian 可自动解析，但不符合命名规范，建议统一。

**示例**:
- `[[Dan-Shipper]]` → `[[Dan-Shipper]]`
- `[[Simon-Willison]]` → `[[Simon-Willison]]`
- `[[Ethan-Mollick]]` → `[[Ethan-Mollick]]`

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
| Raw Sources | 28 篇 | 28 篇 | ✅ |

---

## 统计摘要

| 分类 | 数量 |
|-----|------|
| Raw 文章 | 28 篇 |
| Entity 页面 | 65 个 |
| Topic 页面 | 11 个 |
| Comparison 页面 | 5 个 |

---

## 变化趋势

| 指标 | 上期 (04-10) | 本期 (04-13) | 变化 |
|-----|-------------|-------------|------|
| 健康度 | 95/100 | 95/100 | 持平 |
| Entity 数量 | 63 | 65 | +2 |
| Topic 数量 | 11 | 11 | 持平 |
| 失效链接 | 0 | 0 | ✅ |

---

## 建议操作

### P1（建议）
1. [ ] 统一 wikilink 格式：`[[Name With Space]]` → ``

### P2（可选）
2. [ ] 将 `Vibe-Design.md` 关联到相关 topic

---

**健康度评分**：95/100 🟢

*报告生成: 2026-04-13*