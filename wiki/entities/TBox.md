---
type: entity
title: TBox
aliases:
  - TBox
  - Terminological Box
  - 术语集
definition: "本体的概念与规则部分，定义业务世界的概念框架和运行规则，类比数据库 Schema 或 OOP Class。"
created: 2026-04-20
updated: 2026-04-20
tags:
  - Ontology
  - Knowledge-Engineering
related_entities:
  - "[[Ontology]]"
  - "[[ABox]]"
  - "[[OWL]]"
source_raw:
  - "[[20260420-build-first-business-ontology.md]]"
---

# TBox（术语集）

> [!definition] 定义
> 本体的概念与规则部分，定义业务世界的概念框架和运行规则，类比数据库 Schema 或 OOP Class。

## 关键数据点

- **组成**：类（Class）、关系（Object Property）、属性（Data Property）、约束（Axiom）
- **类比**：数据库 Schema / OOP Class 定义
- **示例**：
  - "客户"是一个类，"订单"是一个类
  - "VIP 客户"是"客户"的子类
  - "VIP 客户的订单可以加急处理"（业务规则）

## 前提与局限性

### 前提条件
- 业务领域有稳定的概念结构
- 规则能够用形式化语言表达
- OWL 等语言足够表达所需语义

### 局限性
- 复杂规则可能需要 SWRL 扩展
- 领域专家需要学习本体建模概念
- 模型变更需要版本管理

## 关联概念

- [[Ontology]]：TBox 是本体的组成部分
- [[ABox]]：TBox 的对应部分（事实数据）
- [[OWL]]：建模 TBox 的主要语言
- [[Class]]：TBox 的核心元素（见本体 6 积木）