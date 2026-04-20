---
type: entity
title: Ontology
aliases:
  - Ontology
  - 本体
  - 本体论
definition: "对现实业务世界的数字化建模，承载企业业务的语义结构与规则（而非事实数据），为 AI Agent 提供统一的业务语义层。"
created: 2026-04-20
updated: 2026-04-20
tags:
  - Enterprise-AI
  - Knowledge-Engineering
related_entities:
  - "[[TBox]]"
  - "[[ABox]]"
  - "[[RDF]]"
  - "[[OWL]]"
  - "[[Protégé]]"
  - "[[Ontology-Agent]]"
source_raw:
  - "[[20260420-ontology-enterprise-ai-agent.md]]"
  - "[[20260420-build-first-business-ontology.md]]"
  - "[[20260420-ontology-meets-agent-case-study.md]]"
---

# Ontology（本体）

> [!definition] 定义
> 对现实业务世界的数字化建模，承载企业业务的语义结构与规则（而非事实数据），为 AI Agent 提供统一的业务语义层。

## 关键数据点

- **来源**：哲学中的"存在之学"，2000 年代语义网浪潮中被标准化（W3C RDF/OWL）
- **复兴驱动**：Palantir 等公司的实践 — 把本体当作企业的共享"语义底座"
- **核心价值**：统一业务概念、融入业务规则、支持复杂推理、提升可解释性
- **与知识图谱的区别**：本体是"语义与规则"（TBox），知识图谱是"事实与数据"（ABox）

## 前提与局限性

### 前提条件
- 企业有明确的业务规则需要表达和推理
- 业务概念能够被形式化定义
- 有足够的领域专家参与建模过程

### 局限性
- 不适合存储海量业务数据（应作为语义层而非数据源）
- 建模成本较高，需要领域专家与本体工程师协作
- 推理性能相对较慢（相比直接查询）

## 关联概念

- [[TBox]]：本体的概念与规则部分
- [[ABox]]：本体的事实数据部分
- [[RDF]]：基础数据标准（三元组）
- [[OWL]]：高级本体表示语言
- [[Protégé]]：本体建模工具
- [[Ontology-Agent]]：基于本体的 AI Agent
- [[Knowledge-Graph]]：事实数据的集合（与本体互补）