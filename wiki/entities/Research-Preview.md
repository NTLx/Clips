---
type: entity
title: Research Preview
aliases:
  - Research Preview
  - 研究预览
definition: "Cat Wu 描述的 Anthropic 核心发布方法论——几乎所有新功能以\"早期实验版本，收集反馈，不保证长期支持\"的形式上线，将发布从重型承诺降维为轻量试探"
created: 2026-05-08
updated: 2026-05-08
tags:
  - product-management
  - AI
  - release-strategy
related_entities:
  - "[[Cat-Wu]]"
  - "[[AI-Native-Shipping]]"
  - "[[Product-Overhang]]"
source_raw:
  - "[[How Anthropic's product team moves faster than anyone else | Cat Wu (Head of Product, Claude Code)]]"
---

# Research Preview（研究预览）

> [!definition] 定义
> **Research Preview** 是 Anthropic（由 Cat Wu 描述）的核心发布策略：几乎每个新功能都先以"Research Preview"标签上线，明确告诉用户该功能是早期版本、正在收集反馈、可能不被长期支持。这种策略通过降低"发布"的承诺成本，将发布行为从需要市场/法务/销售多部门协同的重型事件，变为"我们有个新想法，想让你试试"的轻量沟通。

## 关键数据点

- **心理门槛效应**：Research Preview 消除了团队对"完美发布"的心理枷锁——不完美的版本也可以 ship
- **覆盖范围广泛**：Anthropic "绝大多数功能"都采用此方式——这是系统性策略而非例外
- **用户期望管理**：标签本身即沟通——不需要每次额外解释"这不是最终版本"
- **反馈闭环加速**：早发布→早反馈→早迭代，形成 compounding speed advantage
- **与 Product Overhang 协同**：当模型能力溢出（有潜力但未完全成熟），Research Preview 允许产品先"预占位置"

## 前提与局限性

- 依赖用户群对不确定性的容忍——developer tools 用户天然更能接受"不保证支持"
- 如果滥用（每个功能永远停留在预览阶段），用户信任会消退
- 安全敏感功能需要更审慎——Research Preview 不适用于可能造成实质性损害的场景

## 关联概念

- [[AI-Native-Shipping]] — Research Preview 是极速发布的引擎
- [[Product-Overhang]] — 为还没完全成熟的模型能力提前预留产品接口
