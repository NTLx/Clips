---
type: entity
title: Agent Orchestration
aliases:
  - Agent Orchestration
definition: "Agent 编排层是管理多个 AI Agent 协作的核心架构，OpenClaw 作为编排者负责任务拆解、进度监控、错误处理和结果汇总。"
created: 2026-04-09
updated: 2026-04-15
tags:
  - AI-Agent
  - OpenClaw
  - Multi-Agent-System
related_entities:
  - "[[Claude-Code-CLI]]"
  - "[[Context-Engineering]]"
  - "[[Agent-Swarm]]"
  - "[[Three-State-Protocol]]"
source_raw:
  - "[[OpenClaw + 6 个 Agent 运转半个月，从聊天到干活的完整工程实践]]"
  - "[[OpenClaw + CodexClaudeCode Agent Swarm The One-Person Dev Team Full Setup]]"
---

# Agent Orchestration

> [!definition] 定义
> Agent 编排层（Orchestration Layer）是管理多个 AI Agent 协作的核心架构。OpenClaw 作为编排者，负责任务拆解、进度监控、错误处理和结果汇总，将业务上下文转化为精确的编码任务指令。

## 为什么需要编排层

直接使用 Claude Code 或 Codex 的问题：

- **上下文局限**：编码 Agent 有 200K token 窗口，但无法同时容纳代码库 + 业务上下文
- **交互阻塞**：Claude Code 需要人工确认，凌晨 3 点没人回应就卡住
- **进程失控**：Agent 进程可能死掉，没人知道，第二天发现工作白费

编排层解决了这些问题——它**24 小时在线**，**有持久记忆**，**能同时管理多个任务**。

## 编排者角色

### 项目经理模式

OpenClaw 作为项目经理，Claude Code 作为开发工程师：

> "我只跟项目经理说需求，项目经理自己拆任务、盯进度、处理报错、测试验收。开发工程师闷头写代码就行。"

核心职责：
- 接收产品需求 → 写 PRD + 技术方案 → 用户确认
- 拆解功能 → 逐个委派 Claude Code 开发
- 监控进度 → 处理报错 → 自动修复或升级
- 开发完成 → 自动测试 → 发报告给用户

### Zoe 编排者（6 Agent 实战）

Zoe 是"首席编排者"，不只是管理员：

- **技术方案设计**：三态通信协议、Task Watcher、通信 Guardrail 都是 Zoe 自主设计
- **任务编排**：指派 ainews 深入调研，委派 ACP 编码专家实现
- **系统运维**：每天 3 次巡检，检查 cron 执行状态、磁盘使用、session 健康度
- **记忆系统维护**：每周分析 MEMORY.md，执行分层压缩

## 编排架构示例

### 1+5+6 阵型

```
┌─────────────────────────────────────────┐
│           Zoe（编排者）                  │
│  技术设计 / 任务编排 / 系统运维          │
└─────────────────────────────────────────┘
         ↓ 委派任务
┌─────────────────────────────────────────┐
│  5 个专业 Agent                         │
│  ainews / Trading / Macro / Content / Butler │
└─────────────────────────────────────────┘
         ↓ ACP 编码委派
┌─────────────────────────────────────────┐
│  6 个编码专家（最大 6 并发）             │
│  Claude Code / Codex / Gemini / ...     │
└─────────────────────────────────────────┘
```

### Agent Swarm 编排

Elvis 的 Agent Swarm 系统：

- Zoe spawns agents，写 prompts，选模型，监控进度
- Telegram 通知 PR ready to merge
- 94 commits/天，7 PRs/30 分钟

## 编排 vs 直接使用对比

| 维度 | 直接用 Claude Code | OpenClaw 编排 |
|-----|-------------------|--------------|
| 人工参与 | 必须坐在电脑前 | 只需确认方案和看效果 |
| 问题处理 | 遇到问题就停 | 自己先扛，修不好才问 |
| 并行能力 | 一次只能盯一个 | 多 Claude Code 进程并行 |
| 上下文 | 只有代码上下文 | 业务上下文 + 代码上下文分离 |

## 关键设计原则

1. **分离关注点**：分析 Agent 不写代码，编码通过 ACP 委派
2. **上下文专业化**：编排者持有业务上下文，编码 Agent 只有代码上下文
3. **协议级通信**：不是群聊问题，是协议问题——设计三态协议防止 ACK storm
4. **自主进化**：编排者从失败中学习，写更好的 prompts

## 关键数据点

- 1+5+6 阵型：1 个编排者（Zoe）+ 5 个专业 Agent（ainews/Trading/Macro/Content/Butler）+ 6 个 ACP 编码专家
- Zoe 每天 3 次巡检（10:00/14:00/22:00），检查 cron 执行状态、磁盘使用、session 健康度
- 52 个 cron 任务每天自动轮转，覆盖 A 股 + 美股双时区
- 编码 Agent 有 200K token 窗口，但无法同时容纳代码库 + 业务上下文
- 复杂度随 Agent 数快速上升：3 个 Agent = 3 对交互关系，6 个 = 15 对

## 前提与局限性

- 编排层解决的核心问题：编码 Agent 上下文局限、需要人工确认会卡住、进程死掉没人知道
- 分离关注点：分析 Agent 不写代码，编码通过 ACP 委派；编排者持有业务上下文，编码 Agent 只有代码上下文
- 早期设了 coding、architect、PM 三个技术角色后发现产出与 Zoe + ACP 组合高度重叠，反而增加通信复杂度，后来全砍了
- 每加一个 Agent 都需要半天到一天调试，处理通信冲突、共享资源竞争、规则兼容
- 协议级通信是必须的——不是群聊问题，是协议问题

## 关联概念

- [[Agent-Swarm]] — 编排层与 Agent 群体协作配合
- [[Three-State-Protocol]] — 协议级通信确保编排可靠性
- [[Context-Engineering]] — 编排层持有业务上下文，编码层持有代码上下文
- [[Agent-First-Enterprise]] — Agent 编排是 Agent-First 运营的核心实践

## 来源