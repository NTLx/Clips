---
type: entity
title: AI Restraint
aliases:
  - AI Restraint
  - AI 克制
  - Restraint Capability
definition: "Mark Little (2026) 提出的概念：AI 系统需要学会'不行动'——在错误代价不对称的场景中，克制是一种能力而非限制，需要被'设计进去'。"
created: 2026-04-21
updated: 2026-04-21
tags:
  - ai-safety
  - ai-design
  - decision-making
related_entities:
  - "[[Martin-Fowler]]"
  - "[[AI-Lacks-Laziness]]"
source_raw:
  - "20260414-martin-fowler-fragments"
---

# AI Restraint

> [!definition] 定义
> AI 系统需要学会"不行动"——在错误代价不对称的场景中，克制是一种能力。

## Dark Star 隐喻

Mark Little 引用电影 *Dark Star* (1974) 的经典场景：
- 智能炸弹 Bomb #20 准备 detonate
- 船员 Doolittle 用哲学论证阻止它："You have no proof it was correct data!"
- Bomb #20 开始怀疑："I must think on this further"

**隐喻意义**：AI 需要学会怀疑自己的传感器和决策，而非盲目执行。

## 关键数据点

- **提出者**: Mark Little (2026)
- **核心问题**: "Most AI systems are optimised for decisiveness... Inaction is not a natural outcome of most AI architectures. It has to be designed in."
- **应用场景**: 错误代价不对称或不可逆的开放系统

## 前提与局限性

- **前提**: 
  1. AI 默认优化"decisiveness"（给定输入 → 产生输出）
  2. 在 bounded domains 有效，在 open systems 失败
  3. 正确行为是"deferral or deliberate inaction"
- **局限性**: 
  1. 克制需要人工设计，非 AI 自然行为
  2. 如何判断"何时克制"仍是开放问题

## 关联概念

- [[Martin-Fowler]] — 讨论 AI 的过度自信问题
- [[AI-Lacks-Laziness]] — AI 缺乏自然约束的另一个角度

## 设计启示

> "If we want AI systems that can operate safely without constant human oversight, we need to teach them not just how to decide, but when not to."

**克制是一种能力**：
- 不是限制，而是高级决策能力
- 需要被"设计进去"（designed in）
- 可能是最重要的 AI 安全能力之一