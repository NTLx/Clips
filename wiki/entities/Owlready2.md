---
type: entity
title: Owlready2
aliases:
  - Owlready2
  - owlready2
definition: "Python 本体操作库，用于加载本体、创建实例数据、调用推理机，常用于开发期本体测试。"
created: 2026-04-20
updated: 2026-04-20
tags:
  - Ontology
  - Python
  - Library
related_entities:
  - "[[Ontology]]"
  - "[[OWL]]"
  - "[[HermiT]]"
source_raw:
  - "[[20260420-build-first-business-ontology.md]]"
  - "[[20260420-ontology-meets-agent-case-study.md]]"
---

# Owlready2

> [!definition] 定义
> Python 本体操作库，用于加载本体、创建实例数据、调用推理机，常用于开发期本体测试。

## 关键数据点

- **语言**：Python
- **核心功能**：
  - 加载 OWL 本体文件
  - 创建和操作实例数据
  - 调用 HermiT 推理机
  - 读取推理结果
- **典型用法**：
  ```python
  from owlready2 import get_ontology
  onto = get_ontology("demo_ontology.owx").load()
  with onto:
      sync_reasoner(infer_property_values=True)
  ```

## 前提与局限性

### 前提条件
- Python 环境
- OWL 本体文件

### 局限性
- 主要用于开发期测试
- 生产环境通常使用 GraphDB 等三元组库
- 大规模数据性能受限

## 关联概念

- [[Ontology]]：Owlready2 操作的对象
- [[OWL]]：Owlready2 支持的标准
- [[HermiT]]：Owlready2 调用的推理引擎
- [[GraphDB]]：生产环境替代方案