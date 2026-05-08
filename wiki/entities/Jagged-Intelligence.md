---
type: entity
title: Jagged Intelligence
aliases:
  - Jagged Intelligence
  - 锯齿状智能
definition: "LLM 能力分布高度不均匀的现象——在可验证领域（数学、代码）表现超人，在简单常识问题上严重脆弱，如同锯齿板的凹凸边缘"
created: 2026-05-08
updated: 2026-05-08
tags:
  - AI
  - LLM
  - cognitive-science
related_entities:
  - "[[Verifiability]]"
  - "[[Ghost-Intelligence]]"
  - "[[AI-Capability-Gap]]"
  - "[[AI-Psychosis]]"
  - "[[Andrej-Karpathy]]"
source_raw:
  - "[[Andrej Karpathy: From Vibe Coding to Agentic Engineering]]"
---

# Jagged Intelligence（锯齿状智能）

> [!definition] 定义
> **Jagged Intelligence** 由 Andrej Karpathy 提出，描述 LLM 的能力分布不是均匀进步的，而是像锯齿板一样参差不齐——在某些领域达到超人水平，在其他领域连三岁小孩都不如。根源在于 RLVR（基于可验证奖励的强化学习）训练机制和实验室的经济投入选择。

## 关键数据点

- **洗车案例**：Opus 4.7 能重构 10 万行代码库、发现零日漏洞，却建议你"走路去 50 米外的洗车店"——忽略了车不能走路这一基本常识
- **草莓问题**：LLM 长期无法正确回答"strawberry 中有几个 r"，后被针对性修补
- **象棋跃迁**：GPT-3.5 → GPT-4 期间象棋能力大幅提升，不是因为模型全面变强，而是因为有人把大量棋谱数据加入了预训练集
- **RL 回路效应**：如果你在 RL 训练回路中，你飞；如果你在回路之外，你挣扎

## 前提与局限性

- 锯齿状的分布取决于训练数据分布和 RL 环境覆盖范围，不是模型的内在固定属性
- 随着新模型发布，旧的"锯齿缺口"可能被修补（如草莓问题），新的缺口可能产生
- 理解锯齿状的形态对具体应用场景至关重要——不能说"AI 很强"或"AI 很弱"，要看具体在哪个回路里

## 关联概念

- [[Verifiability]] — 锯齿状的根源：RLVR 只在可验证的领域有效
- [[Ghost-Intelligence]] — 幽灵比喻：LLM 不是全能的动物智能
- [[AI-Capability-Gap]] — 不同用户群体因体验不同而产生的认知鸿沟
- [[AI-Psychosis]] — 深度使用前沿 agentic 模型的用户因看到锯齿状高峰而产生的震撼感
