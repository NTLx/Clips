---
type: entity
title: Verifiability
aliases:
  - Verifiability
  - 可验证性
definition: "决定 LLM 自动化能力的关键维度——能客观验证输出质量的领域，即可通过 RLVR 训练使模型能力持续提升；不能验证的领域，模型进步停滞"
created: 2026-05-08
updated: 2026-05-08
tags:
  - AI
  - LLM
  - RL
  - training
related_entities:
  - "[[Jagged-Intelligence]]"
  - "[[Ghost-Intelligence]]"
  - "[[Agentic-Engineering]]"
  - "[[Andrej-Karpathy]]"
source_raw:
  - "[[Andrej Karpathy: From Vibe Coding to Agentic Engineering]]"
---

# Verifiability（可验证性）

> [!definition] 定义
> **Verifiability** 由 Andrej Karpathy 在分析 LLM 能力分布时提出，指一个任务/领域的输出能否被客观、自动地验证。这是 RLVR（基于可验证奖励的强化学习）训练的核心前提——只有可验证的领域，模型才能通过大规模 RL 持续进步。

## 关键数据点

- **RLVR 机制**：数学题的答案可自动判断对错、代码可通过测试验证——因此模型在这些领域能力爆炸性增长
- **模型能力的经济学**：代码领域创造了最大的经济价值和最多的 RL 环境，因此 labs 投入最多，能力进步最快
- **非对称分布**：传统计算机能自动化的是"你可以在代码中精确指定"的任务；LLM 能自动化的是"你可以验证"的任务——后者范围大得多
- **可验证 ≠ 自动进步**：即使一个领域客观可验证，如果 labs 不投入（没经济价值），模型也不会自动变好

## 前提与局限性

- 当前框架下，"可验证"主要指有客观自动化验证方式（测试、数学证明、eval 分数）
- 写作、设计等主观领域可通过 LLM 评审团等方式逼近可验证性，但精度下降
- Karpathy 认为长期看"几乎一切都可以被做成可验证的"，区别只是难度
- 对创业者而言，在未被 labs 覆盖的可验证领域建立 RL 环境，是结构性机会

## 关联概念

- [[Jagged-Intelligence]] — 可验证性是锯齿状分布的根本原因
- [[Ghost-Intelligence]] — LLM 没有内在动机，完全依赖外部验证信号
- [[Agentic-Engineering]] — 可验证性使 agent 能迭代出可工作的软件
- [[Taste]] — 在不可验证领域的判断力，目前仍是人类护城河
