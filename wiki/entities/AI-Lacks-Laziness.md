---
type: entity
title: AI Lacks Laziness
aliases:
  - AI Lacks Laziness
  - AI 缺乏懒惰美德
  - AI 不懒惰
definition: "Bryan Cantrill (2026) 指出的问题：LLM 不具备程序员'懒惰美德'——Work costs nothing to an LLM，导致系统膨胀而非简化。"
created: 2026-04-21
updated: 2026-04-21
tags:
  - ai-limitation
  - software-engineering
  - design-philosophy
related_entities:
  - "[[Laziness-Virtue]]"
  - "[[AI-Restraint]]"
  - "[[Martin-Fowler]]"
source_raw:
  - "20260414-martin-fowler-fragments"
---

# AI Lacks Laziness

> [!definition] 定义
> LLM 不具备程序员"懒惰美德"——Work costs nothing to an LLM。

## 关键数据点

- **提出者**: Bryan Cantrill (2026)
- **核心问题**: "The problem is that LLMs inherently lack the virtue of laziness. Work costs nothing to an LLM."
- **后果**: "LLMs will make systems larger, not better"

## 前提与局限性

- **前提**: 懒惰美德依赖"人类时间有限"的约束；AI 无此约束
- **局限性**: 
  1. 若 tokens 成本上升，AI 可能"被迫懒惰"
  2. 通过 instruction engineering 可能改善（但效果有限）

## 关联概念

- [[Laziness-Virtue]] — AI 缺乏的美德
- [[AI-Restraint]] — AI 缺乏的另一能力（克制）
- [[Martin-Fowler]] — 讨论 AI 对懒惰美德的影响

## Cantrill 的核心论述

> "LLMs do not feel a need to optimize for their own (or anyone's) future time, and will happily dump more and more onto a layercake of garbage."

**对比**：

| 维度 | 人类 | AI |
|------|------|---|
| **时间约束** | 有限 → 追求简化 | 无限 → 追求膨胀 |
| **懒惰美德** | 有（驱动抽象） | 无（驱动复杂化） |
| **系统设计** | 简洁优先 | 功能优先 |