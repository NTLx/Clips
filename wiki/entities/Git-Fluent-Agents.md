---
type: entity
title: Git-Fluent Agents
definition: "AI coding agents with deep understanding of Git terminology and operations, capable of executing both basic and advanced Git commands autonomously."
created: 2026-04-09
updated: 2026-04-09
tags:
  - AI-Agent
  - Software-Engineering
  - Git
related_entities:
  - "[[Agentic-Engineering]]"
  - "[[History-Rewriting]]"
source_raw:
  - "[[Using Git with coding agents - Agentic Engineering Patterns]]"
---

# Git-Fluent Agents

> [!definition] 定义
> Git-Fluent Agents 是深度理解 Git 术语和操作的 AI 编码 Agent，能够自主执行基础和高级 Git 命令，包括版本控制、分支管理、历史重写和冲突解决。

## 栅心要点

### Agent 能做什么

| Git 操作 | Agent 能力 | 关键命令 |
|---------|-----------|---------|
| 创建仓库 | 启动新 Git 项目 | `git init` |
| 提交更改 | 创建新提交并记录更改 | `git commit -m "message"` |
| 分支管理 | 创建、切换、合并分支 | `git branch`, `git checkout` |
| 远程操作 | 配置 GitHub 远程仓库 | `git remote add` |
| 历史查看 | 查看更改历史 | `git log`, `git diff` |
| 合并集成 | 多种合并策略 | merge, rebase, squash |
| 冲突解决 | 处理复杂合并冲突 | 自动分析并解决 |
| 历史重写 | 修改、撤销、合并提交 | `git reset`, `git rebase -i` |
| 调试追踪 | Git bisect 定位 bug | `git bisect` |
| 代码恢复 | Reflog 恢复丢失代码 | `git reflog` |

### 关键优势
- Agent 可以处理开发者难以记住的复杂命令
- Agent 能够分析冲突代码的意图，智能解决
- Agent 可以确保测试通过后才完成合并

### 常用 Agent 提示语
```
Start a new Git repo here
Commit these changes
Review changes made today
Integrate latest changes from main
Sort out this git mess for me
Find and recover my code that does...
Use git bisect to find when this bug was introduced
```

## 关联概念

- [[Agentic-Engineering]] - Git-Fluent Agents 是 Agentic Engineering 的核心工具
- [[History-Rewriting]] - Git-Fluent Agents 可以执行高级历史重写操作

## 来源

- Raw Source: [[Using Git with coding agents - Agentic Engineering Patterns]]
- Original URL: https://simonwillison.net/guides/agentic-engineering-patterns/using-git-with-coding-agents/