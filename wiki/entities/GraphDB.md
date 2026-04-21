---
type: entity
title: GraphDB
aliases:
  - GraphDB
  - GraphDB Free
definition: "原生支持 RDF/OWL 标准与推理机的三元组数据库，用于生产环境存储本体数据并提供 SPARQL 查询能力。"
created: 2026-04-20
updated: 2026-04-20
tags:
  - Ontology
  - Database
  - RDF-Store
related_entities:
  - "[[Ontology]]"
  - "[[RDF]]"
  - "[[SPARQL]]"
source_raw:
  - "[[20260420-build-first-business-ontology]]"
---

# GraphDB

> [!definition] 定义
> 原生支持 RDF/OWL 标准与推理机的三元组数据库，用于生产环境存储本体数据并提供 SPARQL 查询能力。

## 关键数据点

- **类型**：RDF 三元组库
- **核心能力**：
  - 存储 RDF 数据与 OWL 模型
  - 内置推理机
  - 支持 SPARQL 查询
- **定位**：生产环境本体运行环境
- **替代品**：Apache Jena 等

## 前提与局限性

### 前提条件
- 本体模型已定义
- 需要生产级推理能力

### 局限性
- 部署和运维成本
- 大规模数据可能需要优化
- 与属性图数据库（Neo4j）不兼容

## 关联概念

- [[Ontology]]：GraphDB 存储的对象
- [[RDF]]：GraphDB 的数据格式
- [[SPARQL]]：GraphDB 的查询语言
- Neo4j：属性图数据库（不同类别）