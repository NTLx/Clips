---
type: entity
title: Laziness Virtue
aliases:
  - Laziness Virtue
  - 懒惰美德
  - Three Virtues of a Programmer
definition: "Larry Wall (Perl 设计者) 提出的程序员三美德之一：懒惰驱动抽象和简化，是高质量设计的核心动力。'It takes a lot of work to be lazy'。"
created: 2026-04-21
updated: 2026-04-21
tags:
  - software-engineering
  - philosophy
  - programming
related_entities:
  - "[[Martin-Fowler]]"
  - "[[AI-Lacks-Laziness]]"
  - "[[YAGNI]]"
source_raw:
  - "20260414-martin-fowler-fragments"
---

# Laziness Virtue

> [!definition] 定义
> Larry Wall 提出的程序员三美德之一：懒惰驱动抽象和简化。

## 三美德

Larry Wall（Perl 设计者）定义的程序员三美德：

| 美德 | 含义 | 驱动行为 |
|------|------|---------|
| **Hubris** (傲慢) | 相信自己能做得更好 | 追求卓越 |
| **Impatience** (急躁) | 不愿等待 | 追求效率 |
| **Laziness** (懒惰) | 不愿做重复工作 | 追求抽象和简化 |

> "Of these virtues, I have always found laziness to be the most profound: packed within its tongue-in-cheek self-deprecation is a commentary on not just the need for abstraction, but the aesthetics of it." — Bryan Cantrill

## 关键数据点

- **提出者**: Larry Wall (Perl 设计者，*Programming Perl* 作者)
- **核心洞察**: "It takes a lot of work to be lazy" — 懒惰是结果，不是过程
- **设计哲学**: 懒惰驱动我们建立"最简但不过简"的抽象

## 前提与局限性

- **前提**: 人类时间有限 → 懒惰成为约束 → 驱动简化
- **局限性**: 过度懒惰可能导致过度抽象（增加而非减少复杂度）

## 关联概念

- [[Martin-Fowler]] — 讨论 AI 对懒惰美德的影响
- [[AI-Lacks-Laziness]] — AI 不具备此美德的问题
- [[YAGNI]] — 懒惰美德的具体实践（不要实现未需要的功能）

## Bryan Cantrill 的扩展

> "Laziness drives us to make the system as simple as possible (but no simpler!) — to develop the powerful abstractions that then allow us to do much more, much more easily."

**核心观点**：
- 懒惰不是"不做"，而是"聪明地做"
- 懒惰驱动抽象 → 抽象带来杠杆
- 人类时间有限 → 懒惰成为约束 → 系统保持简洁