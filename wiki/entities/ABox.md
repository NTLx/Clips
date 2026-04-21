---
type: entity
title: ABox
aliases:
  - ABox
  - Assertional Box
  - 断言集
definition: "本体的事实数据部分，描述真实世界发生的业务事实，类比数据库表数据或 OOP Object。"
created: 2026-04-20
updated: 2026-04-20
tags:
  - Ontology
  - Knowledge-Engineering
related_entities:
  - "[[Ontology]]"
  - "[[TBox]]"
  - "[[RDF]]"
source_raw:
  - "[[20260420-build-first-business-ontology]]"
---

# ABox（断言集）

> [!definition] 定义
> 本体的事实数据部分，描述真实世界发生的业务事实，类比数据库表数据或 OOP Object。

## 关键数据点

- **组成**：实例（Individual）及其关系
- **类比**：数据库表数据 / OOP Object 实例
- **示例**：
  - "张三"是一个"VIP 客户"
  - "Order001"是一个"订单"
  - "张三"下了一个"Order001"订单

## 前提与局限性

### 前提条件
- 有 TBox 定义的概念框架
- 业务系统数据能够映射到本体概念

### 局限性
- 不适合存储海量数据（本体不是数据库）
- 生产中通常临时注入，推理后丢弃
- 数据同步需要额外工程

## 关联概念

- [[Ontology]]：ABox 是本体的组成部分
- [[TBox]]：ABox 的对应部分（概念框架）
- [[RDF]]：表达 ABox 的主要语言
- [[Individual]]：ABox 的核心元素（见本体 6 积木）