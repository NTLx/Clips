---
type: entity
title: Agent-Native
aliases:
  - Agent-Native
  - Agent 原生
definition: "为 AI agent 而非人类设计的基础设施、文档、流程和交互界面——将系统分解为传感器（sensors）和执行器（actuators），让 agent 可以直接理解和操作"
created: 2026-05-08
updated: 2026-05-08
tags:
  - AI
  - agent
  - infrastructure
  - software-architecture
related_entities:
  - "[[Software-3.0]]"
  - "[[Agentic-Engineering]]"
  - "[[Agent-First-Enterprise]]"
  - "[[Andrej-Karpathy]]"
source_raw:
  - "[[Andrej Karpathy: From Vibe Coding to Agentic Engineering]]"
---

# Agent-Native（Agent 原生）

> [!definition] 定义
> **Agent-Native** 是 Andrej Karpathy 在 Sequoia AI Ascent 2026 上提出的概念：当前一切基础设施——文档、API、部署平台、DNS 配置——都是为人类阅读和操作设计的。Agent-Native 要求将这些系统重构为 agent 可直接消费和操作的形态，分解为传感器（sensors，感知世界）和执行器（actuators，作用于世界）。

## 关键数据点

- **文档痛点**：Karpathy 的"pet peeve"——为什么文档还在告诉"你"去做什么？他想要的是"我应该复制粘贴给 agent 的文本"
- **部署摩擦**：MenuGen 项目的最大痛苦不是写代码，而是去 Vercell 后台配置 DNS、连接各种服务——这些都应该被 agent 接管
- **Agent-Native 测试标准**：Karpathy 提出——"给定一句 prompt，LLM 能否从零构建一个 app 并直接部署上网，中间不需要人触碰任何东西？"
- **Sensors（传感器）+ Actuators（执行器）框架**：这是 Karpathy 提出的 agent 交互架构隐喻，如同物联网中的传感器和执行器

## 前提与局限性

- Agent-Native 的前提是模型能力足够稳定，能可靠地在非确定性环境中操作
- 安全边界是核心挑战——给 agent 自动配置 DNS 的能力意味着巨大的权限风险
- 目前仍是早期阶段，Agent-Native 的标准和最佳实践尚未形成
- 与 [[Agent-First-Enterprise]] 是同一方向的不同层面——前者是基础设施范式，后者是企业组织范式

## 关联概念

- [[Software-3.0]] — Agent-Native 是 Software 3.0 的基础设施要求
- [[Agentic-Engineering]] — Agent-Native 环境下的开发实践
- [[Agent-First-Enterprise]] — 企业层面的 Agent-Native 组织设计
- [[Machine-Readable-Processes]] — 流程层面的 Agent-Native 化
