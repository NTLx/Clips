---
type: entity
title: Constraint-Driven-Engineering
aliases:
  - Constraint Driven Engineering
definition: "先设定约束（预算、人力、时间），再从约束出发选择技术方案"
created: 2026-04-15
updated: 2026-04-15
tags:
  - software-engineering
  - decision-making
  - architecture
related_entities:
  - "[[Lean-Stack]]"
  - "[[Anti-Enterprise-Mindset]]"
  - "[[Taste]]"
source_raw:
  - "[[每月20成本，60000+营收：加拿大程序员的“最穷”技术栈]]"
---

# Constraint-Driven-Engineering（约束驱动工程）

## 定义

**Constraint-Driven-Engineering** 是一种技术决策方法论：**先设定约束，再从约束出发选技术**。核心主张：没有放之四海皆准的"最佳技术栈"，约束决定选择，而不是技术决定约束。

## 决策框架

```
1. 设定约束 (预算、团队、时间、规模预期)
2. 从约束出发推导最优技术组合
3. 执行最小可行方案
4. 约束变化时才重新评估
```

## 案例对比

| 约束集 | 技术选型 | 理由 |
|-------|---------|------|
| 一个人、`$20/月`、6 个产品 | Go + SQLite + 单机 VPS | 唯一最优解 |
| 单机、多人协作 Web app | Clojure + 全栈 | 开发效率高 |
| JVM 生态、React Native、最小客户端 | JVM 后端 + 薄客户端 | 约束决定的选择 |

## 核心引述

> "There are not universally applicable 'best tech stacks.' Constraints determine the choice, not the technology determining the constraints."
> — @andersmurphy, HN 评论区

## 与 Anti-Enterprise-Mindset 的关系

Anti-Enterprise-Mindset 是 Constraint-Driven-Engineering 在成本维度上的具体应用：
- 约束 = "一个人、`$20/月`"
- 选择 = 不用 K8s、Auth0、Multi-AZ RDS

但 Constraint-Driven-Engineering 更通用：约束可以是团队规模、技术债务、合规要求等任何维度。

## 关键数据点

- Steve Hanov 约束集: {一个人, `$20/月,` 6 个产品} → Go + SQLite + 单机 VPS（唯一最优解）
- @andersmurphy 两套完全不同的技术选型：{单机, Clojure, Web app} vs {JVM, React Native, 最小客户端}
- HN 952 分帖子引发 500+ 条评论，"约束决定选择" 被社区广泛认同


## 前提与局限性

- **前提**: 约束必须真实且明确，不是人为捏造的限制
- **局限**: 并非所有技术问题都有唯一最优解；相同约束下可能有多个可行方案
- **注意**: "约束驱动" 不等于 "不升级" — 当约束变化时（用户增长、收入增加），应重新评估技术选择


## 关联概念

- [[Lean-Stack]] — 约束驱动选择的技术输出
- [[Anti-Enterprise-Mindset]] — 成本约束下的心态
- [[Taste]] — 选择什么作为约束需要品味
