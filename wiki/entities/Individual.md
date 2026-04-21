---
type: entity
title: Individual
aliases:
  - Individual
  - 个体
  - Instance
definition: "本体论术语：ABox 的核心元素，表示具体实例（如 'Andrej Karpathy' 是 'Person' 的 Individual）。"
created: 2026-04-21
updated: 2026-04-21
tags:
  - ontology
  - knowledge-representation
related_entities:
  - "[[ABox]]"
  - "[[Ontology]]"
source_raw:
  - "20260420-build-first-business-ontology"
---

# Individual (Ontology)

> [!definition] 定义
> 本体论术语：ABox 的核心元素，表示具体实例。

## 关键数据点

- **定义**: 具体实例，是 Class 的成员
- **示例**: 'Andrej Karpathy' 是 'Person' 的 Individual
- **位置**: 在 ABox（实例层）中存储

## 前提与局限性

- **前提**: Individual 必须属于某个 Class（概念类型）
- **局限性**: Individual 是静态数据，不包含推理能力

## 关联概念

- [[ABox]] — Individual 的存储层
- [[Ontology]] — Individual 的定义框架