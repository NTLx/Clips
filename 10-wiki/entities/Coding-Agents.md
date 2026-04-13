---
type: entity
title: Coding Agents
definition: "能够编写并执行代码的 AI Agent，具备 Code Execution 能力，是 Agentic Engineering 的核心工具"
created: 2026-04-10
updated: 2026-04-10
tags:
  - AI-Agent
  - coding-tools
  - core-concept
related_entities:
  - "[[Agentic-Engineering]]"
  - "[[Code-Execution]]"
  - "[[Claude-Code-CLI]]"
source_raw:
  - "[[20260410-what-is-agentic-engineering.md]]"
  - "[[building-effective-agents.md]]"
---

# Coding Agents（编码代理）

> **定义**：能够编写并执行代码的 AI Agent，区别于仅生成代码文本的 LLM。

## 核心能力

| 能力 | 描述 | 传统 LLM | Coding Agent |
|------|------|---------|--------------|
| **生成代码** | 输出代码文本 | ✅ | ✅ |
| **执行代码** | 直接运行生成的代码 | ❌ | ✅ |
| **迭代改进** | 基于执行结果自动修改 | ❌ | ✅ |
| **测试验证** | 运行测试并解读结果 | ❌ | ✅ |

## 代表工具

| 工具 | 开发者 | 特点 |
|------|--------|------|
| **Claude Code** | Anthropic | CLI 工具，深度 Git 集成 |
| **Codex** | OpenAI | 原型工具，IDE 集成 |
| **Gemini CLI** | Google | 命令行，Google 生态 |

## 与传统编程的区别

### 传统 LLM 编程

```
用户 → LLM → 代码文本 → 人类复制 → 人类运行 → 人类反馈
```

### Coding Agent 闭环

```
用户 → Agent → 代码 → 自动执行 → 测试结果 → 自动迭代
                    ↑                            ↓
                    ←←← 反馈循环 ←←←←←←←←←←←←←←←←
```

## 为什么重要

> [!important] 决定性差异
> Code Execution 是 Agentic Engineering 成为可能的决定性能力。
> 
> 没有 Code Execution：LLM 输出价值有限
> 有了 Code Execution：Agent 可以迭代出**可验证工作的软件**

## 相关概念

- [[Agentic-Engineering]] - 以 Coding Agents 为基础的工程范式
- [[Code-Execution]] - Coding Agents 的核心能力
- [[Claude-Code-CLI]] - Anthropic 的 Coding Agent 工具
- [[Vibe-Coding]] - 不强调验证的对比模式

---

> **来源**：Simon Willison, "What is agentic engineering?" + Anthropic, "Building Effective Agents"