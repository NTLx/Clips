---
type: entity
title: Agent Tenacity
aliases:
  - Agent Tenacity
  - 代理韧性
  - AI Stamina
definition: "Karpathy (2026) 观察到的 Agent 特性：永不疲劳、永不气馁，能持续尝试直到成功。揭示'韧性'是人类工作的隐形瓶颈。"
created: 2026-04-21
updated: 2026-04-21
tags:
  - ai-agent
  - software-engineering
  - productivity
related_entities:
  - "[[Andrej-Karpathy]]"
  - "[[Claude-Code-CLI]]"
  - "[[Agentic-Engineering]]"
source_raw:
  - "20260127-claude-coding-notes"
---

# Agent Tenacity

> [!definition] 定义
> Karpathy (2026) 观察到的 Agent 特性：永不疲劳、永不气馁，能持续尝试直到成功。

## 关键数据点

- **观察实例**: Agent 可持续工作 30+ 分钟直到解决问题，人类可能在 5 分钟后放弃
- **核心差异**: Agent 不受情绪影响（无挫败感、无气馁），人类受情绪制约
- **对比**: 人类"韧性"受体力、情绪、动机影响；Agent 韧性仅受预算（token/money）限制

## 前提与局限性

- **前提**: Agent 有明确的成功目标和验证机制（如测试通过）
- **局限性**: 无限韧性可能导致无效循环（重复尝试无解的问题）；需要人类判断何时放弃

## 关联概念

- [[Andrej-Karpathy]] — 观察者
- [[Claude-Code-CLI]] — Karpathy 使用的 coding agent
- [[Agentic-Engineering]] — Agent 编程方法论

## 跨域洞察

| 领域 | 对比 |
|------|------|
| **心理学** | 人类工作瓶颈可能是"情绪韧性"而非智力能力 |
| **经济学** | Agent 将"劳动成本"转化为"计算成本"，改变了工作的边际效用 |
| **管理学** | "Feel the AGI moment"提示：AI 的优势不在于智力，而在于"永不停止" |

## 实践应用

Karpathy 建议：
1. 不要命令 Agent"做什么"，给出"成功标准"让 Agent 循环尝试
2. 先写测试，让 Agent 循环直到测试通过
3. 用声明式指令而非命令式指令，获得更大杠杆