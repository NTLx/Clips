---
type: entity
title: SPARQL
aliases:
  - SPARQL
  - SPARQL Query Language
definition: "查询与操作 RDF/本体数据的语言，类比 SQL，用于三元组库中查询和推理结果。"
created: 2026-04-20
updated: 2026-04-20
tags:
  - Ontology
  - Query-Language
  - W3C-Standard
related_entities:
  - "[[Ontology]]"
  - "[[RDF]]"
  - "[[GraphDB]]"
source_raw:
  - "[[20260420-build-first-business-ontology]]"
---

# SPARQL

> [!definition] 定义
> 查询与操作 RDF/本体数据的语言，类比 SQL，用于三元组库中查询和推理结果。

## 关键数据点

- **类型**：查询语言
- **标准组织**：W3C
- **类比**：本体世界的 SQL
- **用途**：
  - 查询 RDF 数据
  - 查询推理结果
  - 操作本体数据

## 前提与局限性

### 前提条件
- 三元组库（如 GraphDB）支持
- 数据以 RDF 格式存储

### 局限性
- 学习曲线（不同于 SQL）
- 复杂查询性能优化需要技巧
- 部分推理结果可能需要预处理

## 关联概念

- [[Ontology]]：SPARQL 查询的对象
- [[RDF]]：SPARQL 操作的数据格式
- [[GraphDB]]：支持 SPARQL 的数据库
- [[OWL]]：SPARQL 可查询的模型语言