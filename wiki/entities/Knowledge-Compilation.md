---
type: entity
title: Knowledge Compilation
definition: "LLM Wiki 的核心操作：将原始知识源（文档、对话、经验）通过 LLM 转化为结构化 Wiki（Entities、Topics、Comparisons），实现知识的持久累积和高效复用。"
created: 2026-04-13
updated: 2026-04-13
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
7. Log     → 记录到 log.md
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
- 记录到 log.md

## 编译产物类型

| 产物类型 | 描述 | 示例 |
|---------|------|------|
| **Entity** | 概念定义页面 | Agentic-Engineering.md |
| **Topic** | 主题整合页面 | Agentic-Engineering-Patterns.md |
| **Comparison** | 对比分析页面 | RAG-vs-LLM-Wiki.md |
| **Index** | 内容索引 | index.md |
| **Log** | 操作记录 | log.md |

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

## 相关链接

- [[RAG-vs-LLM-Wiki]] — 编译 vs 检索的对比
- [[Context-Engineering]] — 编译时的上下文优化
- [[Multi-Layer-Memory]] — 编译产物的记忆层级