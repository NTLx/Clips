---
type: entity
title: Claude Code CLI
definition: "Anthropic 出品的终端原生 AI 编程助手，是一个代理式编码环境，可读取文件、执行命令、编辑代码、运行测试，并自主解决问题。"
created: 2026-04-09
updated: 2026-04-15
tags:
  - AI-Agent
  - Claude-Code
  - Developer-Tools
related_entities:
  - "[[Headless-Mode]]"
  - "[[Agent-Orchestration]]"
source_raw:
  - "[[OpenClaw + 6 个 Agent 运转半个月，从聊天到干活的完整工程实践]]"
  - "[[OpenClaw + CodexClaudeCode Agent Swarm The One-Person Dev Team Full Setup]]"
  - "[[20260409-ai-capability-gap-ai-psychosis]]"
---

# Claude Code CLI

> [!definition] 定义
> Claude Code 是 Anthropic 出品的**终端原生 AI 编程助手**（CLI 工具）。它不是聊天机器人——它是一个**代理式编码环境（agentic coding environment）**，可以读取文件、执行命令、编辑代码、运行测试，并在你观察或离开时自主解决问题。

## 核心特征

- **终端原生**：运行在终端中，理解整个代码库的文件结构、依赖关系和 Git 历史
- **强大推理**：使用 Claude Opus 4.6（最强推理）或 Claude Sonnet 4.6（快速高效）
- **Agentic Loop**：拥有专有的代理循环：收集上下文 → 执行操作 → 验证结果，循环进行
- **200K Context**：200K token 上下文窗口，可将整个项目保持在记忆中
- **多界面支持**：支持 VS Code、JetBrains、桌面应用、Web 界面等多种使用方式

## 核心能力

| 能力 | 说明 |
|-----|------|
| 文件操作 | Read、Write、Edit 文件内容 |
| 命令执行 | 执行 Bash shell 命令 |
| 代码搜索 | Glob 文件模式匹配、Grep 文本搜索 |
| Git 操作 | 原生理解 Git，可创建分支、提交、解决冲突 |
| 测试运行 | 可自主运行测试并修复失败 |
| 子代理 | 可启动独立的 Subagents 进行并行任务 |

## 权限模式

Claude Code 有五种权限模式，操控时需选择合适的模式：

| 模式 | 行为 | 适用场景 |
|------|------|----------|
| **Normal** | 每个危险操作都要确认 | 生产环境、敏感操作 |
| **Auto-Accept Edits** | 自动批准文件编辑，其他操作仍需确认 | 快速原型迭代 |
| **Plan Mode** | 只读模式，不做任何修改 | 代码探索、方案规划 |
| **Don't Ask** | 除了预先批准的工具外，自动拒绝所有 | 受限自动化 |
| **Bypass Permissions** | 自动批准所有操作（危险） | 仅限隔离容器/CI |

## 与 OpenClaw 的关系

当 OpenClaw 需要进行编码任务时，Claude Code 是其首选的编码执行者。OpenClaw 通过 PTY 模式调用 Claude Code 的 Headless 模式，实现自动化编程流程。

## 关键数据点

- Claude Code 使用 Claude Opus 4.6（最强推理）或 Claude Sonnet 4.6（快速高效）
- 200K token 上下文窗口，可将整个项目保持在记忆中
- 五种权限模式：Normal、Auto-Accept Edits、Plan Mode、Don't Ask、Bypass Permissions
- 在 OpenClaw 系统中，通过 ACP 协议委派，最大 6 并发实例、120min TTL
- OpenClaw 系统架构：1 个编排者 + 5 个专业 Agent + 6 类 ACP 编码专家（含 Claude Code）
- OpenClaw 每天几千次 LLM 调用、52 个 cron 定时任务、118 个 Skills

## 前提与局限性

- **前提**: Claude Code 需要 Anthropic API key 和有效的订阅
- **边界条件**: 自动批准所有操作（Bypass Permissions 模式）仅限隔离容器/CI 环境使用
- **局限性**: 200K context window 并非无限，超大代码库可能需要选择性加载
- **局限性**: 作为 agentic coding environment，其代码生成质量依赖模型能力，复杂架构设计仍需人类参与
- **局限性**: 在 OpenClaw 系统中，Claude Code 只是 6 种编码专家之一，不同任务需要选择不同的编码 Agent

## 关联概念