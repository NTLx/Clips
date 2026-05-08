---
type: entity
title: Continual Learning
aliases:
  - Continual Learning
  - 持续学习
definition: "AI 系统在不遗忘已有知识的前提下，将新知识优雅融入已有知识库的能力——Demis Hassabis 认为这是 AGI 缺失的关键拼图之一"
created: 2026-05-08
updated: 2026-05-08
tags:
  - AI
  - AGI
  - machine-learning
related_entities:
  - "[[Demis-Hassabis]]"
  - "[[Jagged-Intelligence]]"
  - "[[World-Model]]"
source_raw:
  - "[[Demis Hassabis: Agents, AGI & The Next Big Scientific Breakthrough]]"
---

# Continual Learning（持续学习）

> [!definition] 定义
> **Continual Learning** 是 Demis Hassabis 明确定义的 AGI 关键缺失组件之一：AI 系统在遇到新信息时，能够优雅地整合进已有知识库，而不发生灾难性遗忘（catastrophic forgetting）。当前 LLM 是 stateless 的——"没有能力适应所在的上下文环境"——这是 agent 不能完全"fire and forget"的根本原因。

## 关键数据点

- **生物学对应物**: 海马体（hippocampus）在睡眠（尤其是 REM）期间回放重要情景（episodic replay），实现渐进式记忆整合——这正是 Hassabis 的 PhD 研究方向
- **当前做法是"胶带"**: "把一切塞进上下文窗口"——百万 token 窗口看似大，但如果处理实时视频，只有约 20 分钟
- **成本问题**: 即使能全存下来，"在需要的时候找到相关的东西"的成本是非凡的——记忆检索效率与存储容量不是同一维度
- **DQN Experience Replay (2013)**: DeepMind 最早的突破之一，从神经科学借鉴"回放成功轨迹"机制

## 前提与局限性

- 持续学习可能最终被证明只需要 scale + incremental innovation（Hassabis: 50/50）
- 也可能需要一个全新的架构突破——不只是在已有 paradigm 里优化
- 神经科学启发可能提供突破口（睡眠、海马体模型），但机器不必然需要模拟生物

## 关联概念

- [[Jagged-Intelligence]] — 缺乏持续学习是模型能力锯齿状的成因之一
- [[World-Model]] — 持续学习使得 agent 能建立对环境动态的内部模拟
- [[Multi-Layer-Memory]] — Claude Code 中的多层记忆系统是持续学习的初级实现
