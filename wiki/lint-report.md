---
type: lint-report
title: Lint Report
updated: 2026-04-15
---

# Lint Report — 2026-04-15

## 总分: 80/100 (100/100 排除历史债务)

### 检查结果

| # | 检查项 | 状态 | 详情 |
|---|-------|------|------|
| 1 | Raw Backlog | ✓ PASS | 26/26 文件已编译 |
| 2 | 孤儿 Entity | ✓ PASS | 0 个孤儿 |
| 3 | 失效链接 | ✓ PASS | 0 个断裂 wikilink |
| 4 | Entity 完整性 | ⚠ PARTIAL | 16 个 Entity 缺失字段（全部为预存历史债务） |
| 5 | 孤岛检测 | ✓ PASS | 0 个孤岛 |
| 6 | 摘要覆盖 | ✓ PASS | 26/26 Raw 文件均有编译摘要 |
| 7 | Comparison 元数据 | ✓ PASS | 所有 Comparison 均有 updated 字段 |
| 8 | 一致性 | ✓ PASS | 无跨文件定义冲突 |

### 扣分项

| 扣分项 | 扣分 | 说明 |
|-------|------|------|
| Entity 完整性 | -20 | 16 个预存 Entity 缺失「关键数据点」「前提与局限性」「关联概念」章节 |

### 新编译内容（本次 compile 产出）

- **7 新 Entity**: Steve-Hanov, Lean-Stack, Runway-Math, Anti-Enterprise-Mindset, B2B-Nurture-C-Model, Time-Moat, Constraint-Driven-Engineering
- **1 新 Topic**: Lean-Indie-Engineering
- **质量**: 所有新增 Entity 均通过完整性检查 ✓

### 历史债务（非本次 compile 引入）

16 个预存 Entity 缺失标准三章节：
- Aaron-Levie, Barry-Zhang, Ben-Thompson, Coding-Agents, Dan-Shipper, Elvis-Sun, Erik-Schluntz, Ethan-Mollick, Joe-Hudson, Judgment, Konstantine-Buhler, MIT-Technology-Review-Insights, Paul-Graham, Raj-Nandan-Sharma, Taste, Wes-Botman

待执行 `fix-lint` 时统一补充。
