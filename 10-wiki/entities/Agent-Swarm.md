---
type: entity
title: Agent Swarm
definition: "Agent Swarm 是多个编码 Agent 的并行调度系统，每个 Agent 拥有独立的 worktree 和 tmux session，实现并行开发和自主监控。"
created: 2026-04-09
updated: 2026-04-09
tags:
  - AI-Agent
  - OpenClaw
  - Multi-Agent-System
related_entities:
  - "[[Agent-Orchestration]]"
  - "[[PTY-Mode]]"
  - "[[Context-Engineering]]"
source_raw:
  - "[[../00-raw/web-clips/Claude-Code/OpenClaw + CodexClaudeCode Agent Swarm The One-Person Dev Team Full Setup]]"
  - "[[../00-raw/web-clips/Claude-Code/OpenClaw + 6 个 Agent 运转半个月，从聊天到干活的完整工程实践]]"
---

# Agent Swarm

> [!definition] 定义
> Agent Swarm 是多个编码 Agent 的并行调度系统，每个 Agent 拥有独立的 Git worktree 和 tmux session，由编排层统一监控和调度，实现并行开发和自主运维。

## 为什么需要 Agent Swarm

直接用 Claude Code 或 Codex 的限制：
- **一次只能盯一个事**：开发后端 API 时没法同时调前端样式
- **上下文窗口是零和的**：填代码 → 无业务上下文；填业务 → 无代码库

Agent Swarm 通过**并行调度 + 上下文分离**解决这些问题。

## 架构设计

### Worktree + tmux 模式

每个 Agent 独立的工作环境：

```bash
# Create worktree + spawn agent
git worktree add ../feat-custom-templates -b feat/custom-templates origin/main
cd ../feat-custom-templates && pnpm install

tmux new-session -d -s "codex-templates" \
  -c "/Users/elvis/Documents/GitHub/medialyst-worktrees/feat-custom-templates" \
  "$HOME/.codex-agent/run-agent.sh templates gpt-5.3-codex high"
```

### 任务注册系统

```json
// .clawdbot/active-tasks.json
{
  "id": "feat-custom-templates",
  "tmuxSession": "codex-templates",
  "agent": "codex",
  "description": "Custom email templates for agency customer",
  "repo": "medialyst",
  "worktree": "feat-custom-templates",
  "branch": "feat/custom-templates",
  "startedAt": 1740268800000,
  "status": "running",
  "notifyOnComplete": true
}
```

## Agent 选择策略

| Agent | 优势 | 适用场景 |
|-------|------|---------|
| **Codex** | 推理强、跨代码库理解 | 后端逻辑、复杂 bug、多文件 refactor |
| **Claude Code** | 快速、前端好、权限问题少 | 前端工作、Git 操作 |
| **Gemini** | 设计 sensibility | UI 设计 → Claude 实现 |

Zoe 根据任务类型选择 Agent：
- Billing system bug → Codex
- Button style fix → Claude Code
- New dashboard design → Gemini 设计 → Claude 实现

## 监控系统

### Cron 级监控脚本

每 10 分钟运行 `.clawdbot/check-agents.sh`：
- 检查 tmux sessions 是否存活
- 检查 tracked branches 的 open PRs
- 检查 CI 状态（via gh cli）
- 自动 respawn 失败 agent（max 3 attempts）
- 只在需要人工介入时 alert

### Definition of Done

Agent 完成任务的标准：

- PR created
- Branch synced to main（no merge conflicts）
- CI passing（lint, types, unit tests, E2E）
- Codex review passed
- Claude Code review passed
- Gemini review passed
- Screenshots included（if UI changes）

## 并行开发效率

Elvis 的实战数据：
- **94 commits in one day**：有 3 个 client calls，没打开编辑器
- **7 PRs in 30 minutes**：编码和验证大部分自动化
- **Commits → MRR**：实时 B2B SaaS，当天交付大部分 feature requests

## 系统瓶颈

**RAM 是天花板**：

每个 Agent 需要：
- 独立 worktree
- 独立 node_modules
- 独立 TypeScript compiler、test runner

5 个 Agent 同时运行 → 5 组并行进程 → Mac Mini 16GB 开始 swapping。

解决方案：Mac Studio M4 max 128GB RAM。

## ACP 编码专家阵型

6 种编码 Agent，最大 6 并发，120min TTL：

| Agent | 模型 | 特点 |
|-------|------|------|
| Claude Code | claude-opus-4.5 | 快速、前端强 |
| Codex | gpt-5.3-codex | 推理强、后端复杂任务 |
| Gemini | gemini-pro | 设计 sensibility |
| Pi | - | - |
| OpenCode | - | - |
| GPT-5.3-Codex | gpt-5.3-codex | 高推理 |

分析 Agent 不写代码，编码全部通过 `sessions_spawn` 委派给专家。

## 来源

- Raw Source: [[../00-raw/web-clips/Claude-Code/OpenClaw + CodexClaudeCode Agent Swarm The One-Person Dev Team Full Setup]]
- Raw Source: [[../00-raw/web-clips/Claude-Code/OpenClaw + 6 个 Agent 运转半个月，从聊天到干活的完整工程实践]]