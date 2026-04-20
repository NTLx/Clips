---
type: entity
title: OWL
aliases:
  - OWL
  - Web Ontology Language
  - Web本体语言
definition: "建立在 RDF 之上的高级本体表示语言，具备更强语义能力，用于定义类、属性、关系及复杂业务规则与约束（TBox）。"
created: 2026-04-20
updated: 2026-04-20
tags:
  - Ontology
  - W3C-Standard
  - Semantic-Web
related_entities:
  - "[[Ontology]]"
  - "[[RDF]]"
  - "[[TBox]]"
  - "[[Protégé]]"
source_raw:
  - "[[20260420-build-first-business-ontology.md]]"
---

# OWL（Web Ontology Language）

> [!definition] 定义
> 建立在 RDF 之上的高级本体表示语言，具备更强语义能力，用于定义类、属性、关系及复杂业务规则与约束（TBox）。

## 关键数据点

- **标准组织**：W3C
- **定位**：RDF 的"语义增强层"
- **核心能力**：
  - 定义类层级关系（rdfs:subClassOf）
  - 定义属性约束
  - 定义等价类（owl:equivalentClass）
  - 定义逻辑限制条件
- **示例**：
  - `VIP客户 rdfs:subClassOf 客户`
  - `加急订单 owl:equivalentClass（订单 AND 下单人为 VIP客户）`

## 前提与局限性

### 前提条件
- 需要表达复杂语义结构
- 规则需要形式化定义
- 推理引擎支持 OWL 标准

### 局限性
- 复杂规则可能需要 SWRL 扩展
- 学习曲线相对陡峭
- 不同 OWL profile 能力不同

## 关联概念

- [[Ontology]]：OWL 是建模本体的主要语言
- [[RDF]]：OWL 底层以 RDF 三元组形式存储
- [[TBox]]：OWL 通常用于建模 TBox
- [[Protégé]]：OWL 的主要建模工具
- [[HermiT]]：OWL 推理引擎