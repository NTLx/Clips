---
type: entity
title: Model Manager
definition: "分配经济中的人的核心角色，负责分配 AI 工作资源、评估质量、迭代改进"
created: 2026-04-10
updated: 2026-04-15
tags:
  - AI-Agent
  - management
  - skills
related_entities:
  - "[[Allocation-Economy]]"
  - "[[Agentic-Engineering]]"
  - "[[Taste]]"
source_raw:
  - "[[The Knowledge Economy Is Over. Welcome to the Allocation Economy.]]"
  - "[[Management as AI superpower]]"
---

# Model Manager（模型管理者）

> **角色转变**：从 doer 到 delegator，从 maker to manager

## 定义

**Model Manager** 是分配经济中的核心角色。当 AI 能完成大部分执行工作时，人类的核心价值转向：

1. **分配工作** - 决定哪些任务交给 AI
2. **评估质量** - 判断 AI 输出是否达标
3. **迭代改进** - 提供反馈让 AI 改进

## 核心能力

### 1. Coherent Vision（连贯愿景）

清晰、具体、有目的的愿景表达能力：

- 提示越具体简洁，工作成果越好
- 语言模型可以帮助提炼愿景

### 2. Clear Taste（清晰品味）

知道想要什么，能表达为什么不对：

> 最差的管理者说"不对"，但无法解释问题。
> 最好的管理者有清晰品味，AI 能更好地创造连贯内容。

### 3. Talent Evaluation（人才评估）

评估 AI 模型能力：

- 哪个模型适合什么任务
- 如何拆分复杂任务给不同模型
- 快速测试新模型是否足够好

### 4. Detail Management（细节管理）

知道何时深入、何时放手：

- 不像 micromanager 亲力亲为
- 不像 hands-off manager 完全放任
- 知道问什么问题、何时检查

## Delegation Equation

Ethan Mollick 提出的委托决策公式：

```
是否委托 AI = f(Human Baseline Time, Probability of Success, AI Process Time)
```

- **Human Baseline Time**: 你自己做需要多久
- **Probability of Success**: AI 一次成功的概率
- **AI Process Time**: 请求、等待、评估的时间

## 与传统管理的区别

| 维度 | 传统管理 | Model Manager |
|------|---------|---------------|
| 资源稀缺性 | 人才稀缺 | "人才"充裕廉价 |
| 委托原因 | 不能自己做 | AI 更快更便宜 |
| 核心挑战 | 找到好人才 | 知道要什么 |

---

## 关键数据点

- GPT-5.2 Thinking 和 Pro 模型在 GDPval 任务中平均 72% 的时间打平或击败人类专家
- 人类专家完成 GDPval 任务平均需要 7 小时，AI 只需几分钟但检查需要 1 小时
- 如果任务需要 1 小时，AI 只需几分钟但检查需要 30 分钟，只有高成功率才值得委托
- 如果一个任务需要 10 小时，值得花数小时与 AI 合作
- 委托决策公式：是否委托 AI = f(Human Baseline Time, Probability of Success, AI Process Time)

## 前提与局限性

- 依赖前提：AI 速度足够快且成本足够低，使得委托的 overhead 值得
- 适用边界：适用于 Human Baseline Time > AI Process Time × (1/Probability of Success) 的场景
- 局限性：对于看似 plausible 但实际失败的任务，检查和纠正可能比自己做更耗时
- 领域专业知识是关键：专家知道给什么指令、能更快发现错误、更擅长纠正
- 不是所有任务都适合委托：需要明确输出标准的任务比开放性任务更适合

## 关联概念

- [[Allocation-Economy]] - Model Manager 是分配经济中的核心角色
- [[Agentic-Engineering]] - Model Manager 管理 coding agents 的工程范式
- [[Taste]] - Clear Taste 是 Model Manager 的核心能力之一
- Delegation to AI - 委托决策公式的具体应用（详见 raw: *Management as AI superpower*）

> **来源**：Dan Shipper (Every), Ethan Mollick (Wharton)