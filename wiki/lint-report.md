---
type: lint-report
title: Clips Lint Report
date: 2026-04-21
health_score: 57
---

# Clips Lint Report (2026-04-21)

## 📊 健康度评分

| 指标 | 分数 |
|------|------|
| **健康度** | **57/100** |

## 📈 知识库统计

| 指标 | 数值 |
|------|------|
| Entity 页面 | 91 |
| Raw 文章 | 33 |

## 🔍 检查结果

### ✅ 通过项 (5/8)

| 检查项 | 结果 |
|--------|------|
| Raw backlog | ✅ 无未编译文章 |
| 一致性检查 | ✅ 无明显冲突 |
| 孤岛检测 | ✅ 无孤岛 Entity |
| Comparison 元数据 | ✅ 所有 comparison 有 updated 字段 |
| 摘要覆盖 | ✅ 所有 raw 文件已编译 |

### ❌ 问题项 (3/8)

#### 1. 失效链接 (963 处)

**扣分**: -20 分

主要问题：`source_raw` 使用了带 `.md` 后缀的完整文件名，应使用短链接格式。

| 文件 | 失效链接 |
|------|---------|
| Aaron-Levie | [[[[Dan-Shipper]]]] |
| Aaron-Levie | [[[[Ethan-Mollick]]]] |
| Aaron-Levie | [[[[(14) Jevons Paradox for Knowledge Work]]]] |
| Aaron-Levie | [[[[(14) Jevons Paradox for Knowledge Work]] |
| Multi-Layer-Memory | [[[[Context-Engineering]]]] |
| Multi-Layer-Memory | [[[[Agent-Orchestration]]]] |
| Multi-Layer-Memory | [[[[OpenClaw + 6 个 Agent 运转半个月，从聊天到干活的完整工程实践]]]] |
| Multi-Layer-Memory | [[[[Context-Engineering]]]] |
| Multi-Layer-Memory | [[[[Agent-Orchestration]]]] |
| Multi-Layer-Memory | [[[[Headless-Mode]]]] |
| Multi-Layer-Memory | [[[[Knowledge-Compilation]]]] |
| Ontology | [[[[TBox]]]] |
| Ontology | [[[[ABox]]]] |
| Ontology | [[[[RDF]]]] |
| Ontology | [[[[OWL]]]] |
| Ontology | [[[[Protégé]]]] |
| Ontology | [[[[Ontology-Agent]]]] |
| Ontology | [[[[20260420-ontology-enterprise-ai-agent]]]] |
| Ontology | [[[[20260420-build-first-business-ontology]]]] |
| Ontology | [[[[20260420-ontology-meets-agent-case-study]]]] |

#### 2. Entity 完整性 (13 个)

**扣分**: -13 分

概念 Entity 缺失标准三章节：

| Entity | 缺失章节 |
|--------|---------|
| Aaron-Levie | 关键数据点 / 前提与局限性 / 关联概念 |
| AISI | 关键数据点 / 前提与局限性 / 关联概念 |
| Barry-Zhang | 关键数据点 / 前提与局限性 / 关联概念 |
| Raj-Nandan-Sharma | 关键数据点 / 前提与局限性 / 关联概念 |
| Wes-Botman | 关键数据点 / 前提与局限性 / 关联概念 |
| Joe-Hudson | 关键数据点 / 前提与局限性 / 关联概念 |
| Paul-Graham | 关键数据点 / 前提与局限性 / 关联概念 |
| Konstantine-Buhler | 关键数据点 / 前提与局限性 / 关联概念 |
| Erik-Schluntz | 关键数据点 / 前提与局限性 / 关联概念 |
| Elvis-Sun | 关键数据点 / 前提与局限性 / 关联概念 |
| MIT-Technology-Review-Insights | 关键数据点 / 前提与局限性 / 关联概念 |
| Ben-Thompson | 关键数据点 / 前提与局限性 / 关联概念 |
| Ethan-Mollick | 关键数据点 / 前提与局限性 / 关联概念 |

#### 3. MathJax 冲突风险 (62 处)

**扣分**: -10 分

包含 `$` 符号的文本可能触发 MathJax 解析，需检查是否已包裹或转义。

## 📋 修复建议

### 优先级 P0（立即修复）

1. **失效链接**：批量移除 `source_raw` wikilinks 中的 `.md` 后缀
   - 影响文件：Ontology.md, Harness-Engineering.md, Vibe-Coding.md 等
   - 命令：`sed -i '' 's/\[\[\([^]]*\)\.md\]\]/[[]]/' wiki/entities/*.md`

### 优先级 P1（本周修复）

2. **Entity 完整性**：为 13 个概念 Entity 补充标准三章节
   - 部分 Entity 可能需要重新分类为 `person` 类型

### 优先级 P2（持续监控）

3. **MathJax 冲突**：扫描包含金额、缩写等 `$` 符号的文本
   - 修复方式：用反引号包裹 `` `$200` `` 或转义 `\$200`

---

*报告由 Claude Code 自动生成*
