---
type: entity
title: Accessibility-Complexity-Evaluation
aliases:
  - Accessibility Complexity Evaluation
  - 无障碍代码复杂度评估
definition: "用启发式脚本评估前端代码复杂度，评分超过阈值时禁止 Agent 自动修改，转而建议联系无障碍团队人工介入"
created: 2026-05-18
updated: 2026-05-18
tags:
  - accessibility
  - AI-Agent
  - code-quality
related_entities:
  - "[[Accessibility-Agent]]"
  - "[[Accessibility-High-Risk-Patterns]]"
source_raw:
  - "[[Building a general-purpose accessibility agent—and what we learned in the process]]"
---

# Accessibility-Complexity-Evaluation

> [!definition] 定义
> **无障碍代码复杂度评估** 是 Accessibility Agent 中的一项机制：用一个小型 shell 脚本，基于一组基本启发式规则分析目标代码的相对复杂度，生成评分。评分超过阈值时，Agent 不执行代码变更，而是通知使用者联系无障碍团队咨询。

## 设计动机

避免高成本返工：如果 Agent 对一个复杂代码块生成了"自以为无障碍但实际上不可用"的方案，后续需要大量时间重新审查和修复。复杂度评估是一种前置保护机制。

## 工作流程

1. 脚本分析目标代码 → 生成复杂度评分
2. 评分 < 阈值 → Agent 正常执行修改
3. 评分 ≥ 阈值 → Agent 切换到"仅指导"模式，建议人工介入

## 关键数据点

- 使用 shell 脚本 + 启发式规则（非 LLM 自身判断），避免循环依赖
- 复杂度评估与高风险模式检测配合使用，形成两层保护

## 前提与局限性

- 启发式规则的质量决定了评估的准确性——过于简单可能误判，过于复杂本身也需要维护
- 复杂度评分是二元的（通过/不通过），实际复杂度是连续谱，边界情况可能被误判
- 需要与高风险模式检测配合使用，单独使用不足以覆盖所有 Agent 不该碰的场景

## 关联概念

- [[Accessibility-Agent]] — 复杂度评估是无障碍 Agent 的核心约束机制
- [[Accessibility-High-Risk-Patterns]] — 与复杂度评估配合，形成两层保护
