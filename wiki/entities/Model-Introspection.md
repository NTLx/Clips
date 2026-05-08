---
type: entity
title: Model Introspection
aliases:
  - Model Introspection
  - 模型自省
definition: "Cat Wu 提出的最被低估的 AI 技能——让模型分析自己为什么会犯某个错误，从中获得的洞察远超人类自己分析代码或逻辑缺陷"
created: 2026-05-08
updated: 2026-05-08
tags:
  - AI
  - prompting
  - debugging
related_entities:
  - "[[Cat-Wu]]"
  - "[[Jagged-Intelligence]]"
  - "[[AI-Psychosis]]"
source_raw:
  - "[[How Anthropic's product team moves faster than anyone else | Cat Wu (Head of Product, Claude Code)]]"
---

# Model Introspection（模型自省）

> [!definition] 定义
> **Model Introspection** 是 Cat Wu 提出的最被低估的 AI 使用技能：当模型犯错时，不要只修复错误——要追问模型"分析你刚才为什么犯这个错，告诉我你为什么会这样做"。Cat 发现，模型对自己错误的分析能产生远超人类独立分析的洞察，因为它能访问其"推理链路"中隐含的模式和假设，这些对人类可能不可见。

## 关键数据点

- **Cat 的实际用法**：经常让 Claude "分析你刚犯的错误，告诉我你为什么会犯"——将此视为 debugging workflow 的标准步骤
- **洞察深度**：模型的自省经常揭示其推理路径中的系统性偏差——不仅仅是"我算错了"，而是"我在做类似 X 的判断时倾向于假设 Y"
- **与其他 debugging 方法的关系**：比传统 rubber duck debugging 更强——你不是在跟一个无响应的对象说话，你是在问那个犯了错的 entity
- **隐性知识提取**：模型对自身行为的解释可能揭示其训练数据分布或 RL 回路中的规律——这构成了反馈到 fine-tuning 的闭环

## 前提与局限性

- 模型自省本质上仍是 pattern prediction——它不是真正的元认知（metacognition），而是对"什么样的解释看起来合理"的预测
- 模型对错误原因的解释可能是幻觉——"我是因为 X 犯的错"可能只是听起来合理，实际上真正原因是完全不同的模式偏差
- 过度依赖自省可能产生"自我强化偏差"——模型在自省中发现的模式可能进一步固化其偏见
- 区分真正有用的自省和 post-hoc rationalization 需要人类 Judgment

## 关联概念

- [[Jagged-Intelligence]] — 模型自省揭示了锯齿状的内部结构
- [[Taste]] — 判断模型自省的质量需要 taste——区分真洞察和合理美化
- [[Judgment]] — 辨别模型自省中的信号与噪音
