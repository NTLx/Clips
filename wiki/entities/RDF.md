---
type: entity
title: RDF
aliases:
  - RDF
  - Resource Description Framework
  - 资源描述框架
definition: "W3C 推荐的基础数据标准，使用三元组（主语-谓语-宾语）表达信息，更适合表达业务事实（ABox）。"
created: 2026-04-20
updated: 2026-04-20
tags:
  - Ontology
  - W3C-Standard
  - Semantic-Web
related_entities:
  - "[[Ontology]]"
  - "[[OWL]]"
  - "[[ABox]]"
source_raw:
  - "[[20260420-build-first-business-ontology.md]]"
---

# RDF（Resource Description Framework）

> [!definition] 定义
> W3C 推荐的基础数据标准，使用三元组（主语-谓语-宾语）表达信息，更适合表达业务事实（ABox）。

## 关键数据点

- **标准组织**：W3C
- **核心概念**：三元组（Subject - Predicate - Object）
- **数据形式**：多个三元组构成 RDF 图
- **适用场景**：表达业务事实（ABox），如"张三 rdf:type VIP客户"

## 前提与局限性

### 前提条件
- 数据能够用三元组形式表达
- URI 作为资源标识符

### 局限性
- 不擅长表达复杂语义结构、约束规则
- 单纯 RDF 需要扩展才能表达 TBox
- 存储和查询需要三元组库支持

## 关联概念

- [[Ontology]]：RDF 是本体的基础数据标准
- [[OWL]]：RDF 的语义增强层
- [[ABox]]：RDF 通常用于表达 ABox
- [[SPARQL]]：RDF 的查询语言