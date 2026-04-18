---
type: entity
title: Knowledge Compilation
aliases:
  - Knowledge Compilation
definition: "LLM Wiki 的核心操作：将原始知识源（文档、对话、经验）通过 LLM 转化为结构化 Wiki（Entities、Topics、Comparisons），实现知识的持久累积和高效复用。"
created: 2026-04-13
updated: 2026-04-15
tags:
  - knowledge-management
  - llm-wiki
  - workflow
related_entities:
  - "[[RAG-vs-LLM-Wiki]]"
  - "[[Context-Engineering]]"
  - "[[Multi-Layer-Memory]]"
  - "[[Andrej-Karpathy]]"
source_raw:
  - "[[20260413-llm-wiki]]"
  - "[[一篇文章卖了20万，开源CC+Obsidian打造的LLM Wiki 内容创作3.0系统]]"
---

# Knowledge Compilation

> **核心操作**：Raw → Wiki 的知识转化过程

## 定义

**Knowledge Compilation**（知识编译）是 LLM Wiki 的核心操作：

> 原始知识源经过 LLM 处理，转化为结构化 Wiki 层，实现一次编译、持续复用。

## 与程序编译的类比

| 程序编译 | 知识编译 |
|---------|---------|
| 源代码 | Raw Sources（原始文档） |
| 编译器 | LLM Agent |
| 目标代码 | Wiki 层（Entities、Topics） |
| 运行时 | Query（查询） |
| 调试 | Lint（健康检查） |

## 编译流程（Ingest）

### 标准流程

```
1. Read    → 读取 raw source
2. Analyze → 分析主题、确定分类
3. Extract → 提取 3-5 个核心概念
4. Create  → 创建/更新 entity 页面
5. Link    → 更新 topic 页面、建立关联
6. Index   → 更新 index.md
7. Commit  → 提交 git commit（按 Commit 规范撰写）
```

### 单源编译示例

一篇关于"Agentic Engineering"的文章：

```
Raw Source: what-is-agentic-engineering.md
    ↓ (LLM 编译)
Entities Created:
    - Agentic-Engineering.md
    - Coding-Agents.md
    - Code-Execution.md
    - Vibe-Coding.md
Topics Updated:
    - Agentic-Engineering-Patterns.md
Index Updated:
    - 添加 4 个 entity 条目
    - 添加 topic 引用
Log Entry:
    - ## [2026-04-10] ingest | what-is-agentic-engineering
```

### 触及范围

> [!important] 单源编译的影响
> **一篇 source 可能触及 10-15 个 wiki 页面**

- 新建 entities（3-5 个）
- 更新相关 entities（添加关联）
- 创建/更新 topic（整合主题）
- 更新 index.md
- 更新 comparisons（如有对比）
- 提交 git commit

## 编译产物类型

| 产物类型 | 描述 | 示例 |
|---------|------|------|
| **Entity** | 概念定义页面 | Agentic-Engineering.md |
| **Topic** | 主题整合页面 | Agentic-Engineering-Patterns.md |
| **Comparison** | 对比分析页面 | RAG-vs-LLM-Wiki.md |
| **Index** | 内容索引 | index.md |
| **History** | 操作记录 | git commit log |

## 编译 vs 检索

| 维度 | RAG（检索） | Compilation（编译） |
|-----|------------|-------------------|
| 处理时机 | Query 时 | Ingest 时 |
| 处理成本 | 每次查询都付出 | 一次编译，后续免费 |
| 结果稳定性 | 可能不同 | 固定不变 |
| 知识累积 | 无 | 持久沉淀 |
| 冗余处理 | 切片可能冗余 | 编译时已提炼 |

## 编译质量保障

### Lint 检查

定期执行 lint 操作：

```
Lint 检查项：
    - 矛盾检测（页面间矛盾）
    - 孤儿检测（无引用的 entity）
    - 过期检测（被新 source 超越的 claims）
    - 缺失检测（提及但无页面的概念）
    - 链接检测（失效的 wikilinks）
```

### 版本控制

Wiki 是 git repo，支持：

- 版本历史（追溯变更）
- 分支管理（实验性编译）
- 协作编辑（团队 Wiki）

## 编译策略

### 单源精细编译

Karpathy 推荐的方式：

> "I prefer to ingest sources one at a time and stay involved — I read the summaries, check the updates, and guide the LLM on what to emphasize."

优势：
- 深度参与知识提炼
- 确保 quality 和 relevance
- 建立个人理解

### 批量快速编译

适用于：

- 初始知识库建设
- 已有大量 raw sources
- 对质量要求较低的场景

## 编译与 Query 的循环

> [!tip] 关键洞察
> **好的查询答案可以回填为新的 Wiki 页面**

```
Query → Answer → File back to Wiki → Compounding
```

示例：
- 用户请求对比 → 生成 Comparison 页面
- 用户请求分析 → 生成 Topic 页面
- 用户发现关联 → 更新 Entity 关联

这样探索也能累积，不只是 source 编译累积。

---

## 三步编译法（进阶）

> 饼干哥哥在 Karpathy 方案基础上的改进，增加了"质疑"和"对标"两步

### 核心流程

```
原文 → 浓缩 → 质疑 → 对标 → 结构化 Wiki
```

### 第一步：浓缩 (Condense)

- **原则**：用剃刀法则——删掉这条信息会影响理解吗？不会就删
- **输出**：核心结论（不超过 3 条）+ 支撑每条结论的关键证据
- **格式**：每条结论一行，证据缩进在下方

### 第二步：质疑 (Question) — 关键差异

针对每条核心结论，回答：
1. **前提假设**：这个结论依赖哪些前提假设？
2. **边界条件**：如果这些前提不成立（换行业/换市场/换规模），结论还成立吗？
3. **数据可靠**：作者的数据来源可靠吗？样本量、时间范围、地域限制？
4. **反例存在**：有没有作者没提到的反例或边界条件？

> [!important] 质疑的价值
> 避免孤立事实误导——如"转化率提升40%"的前提是"目标市场是北美"

### 第三步：对标 (Cross-reference)

1. **跨域洞察**：其他领域有没有类似现象？（技术↔商业↔管理↔科学）
2. **知识迁移**：这个知识可以迁移到哪些场景？
3. **跨域关联**：如果有跨域关联，创建或更新对应的概念条目

> [!example] 跨域洞察示例
> - 领域 A："AI Agent 多步推理链在第 5 步后容易失控"
> - 领域 B："跨境电商供应链超过 4 个环节后出错率指数上升"
> - **洞察**：复杂链条的可靠性随环节数指数下降

### 与 Karpathy 原方案的对比

| 步骤 | Karpathy 原始方案 | 饼干哥哥改进版 |
|-----|------------------|---------------|
| 第一步 | 读原文 → 写摘要 | 浓缩（更精炼） |
| 第二步 | 提取概念 | **质疑（新增）** |
| 第三步 | 更新索引 | **对标（新增）** |

### 编译产物示例

一篇 TikTok Shop 选品策略文章编译后产出：
- 1 篇编译摘要（浓缩 + 质疑 + 对标结果）
- 3 个概念条目（TikTok Shop 选品、AI 选品工具、跨境电商利润率）
- 更新全局索引和操作日志

> **关键价值**：下次编译相关文章时，AI 不是从零开始，而是读取已有概念条目，把新信息跟旧信息合并，标注异同

## 与多层记忆的关系

参见 [[Multi-Layer-Memory]]

| 记忆层 | 对应 | 编译角色 |
|-------|------|---------|
| 短期记忆 | 当前对话 | 无 |
| 工作记忆 | RAG 检索 | 未编译知识 |
| 长期记忆 | Wiki 层 | **编译产物** |

## 编译成本分析

| 维度 | 首次编译 | 后续使用 |
|-----|---------|---------|
| Token 成本 | 高（深度分析） | 低（直接查询） |
| 时间成本 | 高（触及多页面） | 低（结构化呈现） |
| 人工成本 | 需参与指导 | 无需参与 |
| 累积价值 | 基础建立 | 持续增值 |

---

## 关键数据点

- 单篇 source 编译可能触及 10-15 个 wiki 页面
- Wiki 规模在 ~100 篇 sources、数百个页面时，index.md 仍可有效工作
- 一次编译，后续查询免费（相比 RAG 每次查询都需付出 token 成本）
- 三步编译法：浓缩（≤3 条核心结论）→ 质疑（4 个问题）→ 对标（3 个跨域关联）

## 前提与局限性

- **前提**: LLM 具备足够的理解和综合能力，能准确提炼源材料的核心概念
- **前提**: index.md 的方式在"中等规模"（~100 sources）有效，超大规模可能需要向量检索
- **边界条件**: 编译质量依赖 Schema 文档的质量，Schema 不完善会导致编译结果不一致
- **局限性**: "一次编译、持续复用"假设知识源之间没有根本性冲突，矛盾处理需要人工介入
- **局限性**: Karpathy 的方案是个人 Wiki 场景，团队/企业场景的协作和权限管理未深入讨论

## 关联概念

- [[RAG-vs-LLM-Wiki]] — 编译 vs 检索的对比
- [[Context-Engineering]] — 编译时的上下文优化
- [[Multi-Layer-Memory]] — 编译产物的记忆层级