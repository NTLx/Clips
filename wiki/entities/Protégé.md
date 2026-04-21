---
type: entity
title: Protégé
aliases:
  - Protégé
  - Protégé Desktop
definition: "斯坦福大学开发的开源本体编辑器，支持 OWL/RDF 标准，通过可视化界面创建类、属性、关系并定义约束规则。"
created: 2026-04-20
updated: 2026-04-20
tags:
  - Ontology
  - Tool
  - Open-Source
related_entities:
  - "[[Ontology]]"
  - "[[OWL]]"
  - "[[HermiT]]"
source_raw:
  - "[[20260420-build-first-business-ontology]]"
---

# Protégé

> [!definition] 定义
> 斯坦福大学开发的开源本体编辑器，支持 OWL/RDF 标准，通过可视化界面创建类、属性、关系并定义约束规则。

## 关键数据点

- **开发者**：斯坦福大学
- **类型**：开源本体编辑器
- **支持标准**：OWL/RDF
- **核心功能**：
  - Classes 面板：添加业务概念（类）
  - Object Properties 面板：定义关系
  - Data Properties 面板：定义属性
  - Individuals 面板：创建测试数据
- **定位**：语义建模实验场，适合初学者

## 前提与局限性

### 前提条件
- 需要本体建模需求
- 熟悉 OWL 基本概念

### 局限性
- 主要用于开发期验证，非生产环境
- 大规模本体管理可能需要其他工具
- 可视化界面有时不如代码灵活

## 关联概念

- [[Ontology]]：Protégé 是建模本体的主要工具
- [[OWL]]：Protégé 支持的核心标准
- [[HermiT]]：可集成到 Protégé 的推理引擎
- [[Owlready2]]：Python 本体操作库（生产替代）