---
type: entity
title: Agent Loops
aliases:
  - Agent Loops
  - Agent 循环调度
definition: "Boris Cherny 提出的大规模 Agent 编排范式——通过 cron 定时任务让 Agent 在后台持续自主运行，执行 CI 维护、PR 看护、反馈聚类等重复性工作"
created: 2026-05-08
updated: 2026-05-08
tags:
  - AI-agent
  - claude-code
  - automation
related_entities:
  - "[[Boris-Cherny]]"
  - "[[Claude-Code-CLI]]"
  - "[[Product-Overhang]]"
  - "[[Agent-Swarm]]"
  - "[[Agent-Workflow-Patterns]]"
source_raw:
  - "[[Anthropic's Boris Cherny: Why Coding Is Solved, and What Comes Next]]"
---

# Agent Loops（Agent 循环调度）

> [!definition] 定义
> **Agent Loops** 由 Boris Cherny 提出并实践，是一种极简但极具爆发力的大规模 Agent 编排范式：通过 cron 调度让 Agent 在后台以固定频率（每分/每 N 分/每天）持续自主运行。Boris 称其为"最简单却最有效的东西"——"Loops 就是未来"。Anthropic 已将这一概念产品化为 Routines（服务器端 Loop，关掉电脑也继续运行）。

## 关键数据点

- **Boris 个人使用规模**：数十个 Loop 同时运行，功能涵盖 PR 看护（自动修 CI、auto rebase）、CI 健康维护（自动修 flaky test）、Twitter 反馈聚类（每 30 分钟）
- **夜间规模**：数千个 Agent 在夜间做深度工作
- **4.7 模型新行为**：模型开始自主建议启动 Loop——"嘿我注意到数据在变化，我可以启动一个 Loop 每 30 分钟给你报告"
- **产品化路径**：Loop（cron 调度）→ Routines（服务器端持久化）→ 内置为 Claude Code 一等公民功能
- **与其他范式的关系**: 区别于 Sub-agents（任务分派），Loop 是时间驱动的自主持续运行

## 前提与局限性

- Loop 的有效性假设 Agent 输出质量在无监督情况下保持稳定——错误累积是核心风险
- 大量 Agent 并行运行时的调度冲突和资源竞争仍未充分解决
- 模型需要在长时间运行中保持上下文一致性——目前仍有限制
- Routines 的服务器端运行意味着权限和安全模型需要重新设计

## 关联概念

- [[Product-Overhang]] — Loop 是 overhang 的典型案例：模型现在就能做到
- [[Agent-Swarm]] — 大规模并行 Agent 的群体协作
- [[Agent-Workflow-Patterns]] — Anthropic 的 Agent 架构设计模式
- [[Claude-Code-CLI]] — Loop 的运行平台
