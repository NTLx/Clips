---
type: entity
title: Knowledge Graph
aliases:
  - Knowledge Graph
  - 知识图谱
definition: "事实数据的集合，以图结构表示实体及其关系。与本体互补：本体定义概念和关系类型，知识图谱填充具体实例。"
created: 2026-04-21
updated: 2026-04-21
tags:
  - ontology
  - knowledge-representation
related_entities:
  - "[[Ontology]]"
  - "[[ABox]]"
  - "[[TBox]]"
source_raw:
  - "20260420-build-first-business-ontology"
---

# Knowledge Graph

> [!definition] 定义
> 事实数据的集合，以图结构表示实体及其关系。

## 关键数据点

- **与本体关系**: 本体定义概念和关系类型（TBox），知识图谱填充具体实例（ABox）
- **结构**: 节点（实体）+ 边（关系）组成的图结构
- **应用**: 搜索引擎（Google Knowledge Graph）、推荐系统、问答系统

## 前提与局限性

- **前提**: 需要本体或 schema 定义实体类型和关系类型
- **局限性**: 知识图谱是静态数据，不包含推理规则；更新和维护成本高

## 关联概念

- [[Ontology]] — 本体定义概念层
- [[ABox]] — 知识图谱的实例层
- [[TBox]] — 知识图谱的概念层