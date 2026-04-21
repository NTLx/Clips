---
type: entity
title: Ontology-Agent
aliases:
  - Ontology Agent
  - 本体增强 Agent
  - Ontology-Enhanced Agent
definition: "基于本体语义层的 AI Agent，通过调用本体推理工具判断业务规则，而非依赖 LLM 概率推理。"
created: 2026-04-20
updated: 2026-04-20
tags:
  - AI-Agent
  - Enterprise-AI
  - Ontology
related_entities:
  - "[[Ontology]]"
  - "[[TBox]]"
  - "[[ABox]]"
  - "[[OWL]]"
  - "[[HermiT]]"
source_raw:
  - "[[20260420-ontology-meets-agent-case-study]]"
---

# Ontology-Agent（本体增强 Agent）

> [!definition] 定义
> 基于本体语义层的 AI Agent，通过调用本体推理工具判断业务规则，而非依赖 LLM 概率推理。

## 关键数据点

- **技术栈示例**：
  - Agent 框架：LangChain
  - 后端数据层：PostgreSQL
  - 本体存储推理：OWL 文件 + Owlready2 + HermiT
- **工具选择原则**：
  - 日常查询 → 数据库查询工具
  - 规则判定 → 本体推理工具
  - 语义概念查询 → 本体概念查询
- **核心能力**：可解释的规则推理（结论可追溯到具体规则）

## 前提与局限性

### 前提条件
- 已构建业务本体（TBox）
- Agent 能注入事实数据到本体
- 推理引擎可用

### 局限性
- 推理性能相对较慢（需注入数据 + 运行推理机）
- 本体建模需要额外工程成本
- 复杂场景可能需要定制推理逻辑

## 关联概念

- [[Ontology]]：Ontology-Agent 的核心语义层
- [[TBox]]：规则定义来源
- [[ABox]]：运行时注入的事实数据
- [[OWL]]：本体语言
- [[HermiT]]：推理引擎
- [[Owlready2]]：Python 本体操作库