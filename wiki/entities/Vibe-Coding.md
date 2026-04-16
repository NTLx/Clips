---
type: entity
title: Vibe Coding
definition: "Andrej Karpathy 提出的概念，指未经审查、原型质量的 LLM 生成代码"
created: 2026-04-10
updated: 2026-04-16
tags:
  - AI-Agent
  - coding-agents
  - programming
related_entities:
  - "[[Agentic-Engineering]]"
  - "[[Harness-Engineering]]"
  - "[[Code-Execution]]"
  - "[[Andrej-Karpathy]]"
  - "[[Software-2.0]]"
  - "[[AI-Capability-Gap]]"
  - "[[AI-Psychosis]]"
source_raw:
  - "[[20260410-what-is-agentic-engineering]]"
  - "[[20260413-llm-wiki]]"
  - "[[Why Your \u201cAI-First\u201d Strategy Is Probably Wrong]]"
  - "[[20260409-ai-capability-gap-ai-psychosis]]"
---

# Vibe Coding（氛围编程）

> **核心特征**：忘记代码存在，专注于氛围和直觉

## 定义

**Vibe Coding** 是 Andrej Karpathy 于 2025 年 2 月提出的术语，描述一种 LLM 编程方式：

> "I just see things, say things, run things, and copy paste things, and it mostly works."

### 核心特征

1. **忘记代码存在** - 不关心代码细节
2. **原型质量** - 快速产出，不追求生产级
3. **未经审查** - 直接使用 AI 输出
4. **氛围驱动** - 凭直觉迭代

## 与 Agentic Engineering 的区别

Simon Willison 强调保持术语的原意：

| 维度 | Vibe Coding | Agentic Engineering |
|------|-------------|---------------------|
| **代码质量** | 原型级 | 生产级 |
| **审查程度** | 无 | 深度审查 |
| **验证方式** | 凭感觉 | 自动测试 |
| **目标** | 快速原型 | 可工作软件 |
| **心态** | "忘记代码" | 验证和迭代 |

## 适用场景

### 适合 Vibe Coding

- 快速原型验证
- 个人实验项目
- 学习和探索
- 一次性脚本

### 需要 Agentic Engineering

- 生产环境代码
- 团队协作项目
- 长期维护系统
- 安全敏感应用

## 不要滥用术语

> [!warning] 重要区分
> 不要把 Vibe Coding 扩展定义为"任何 LLM 生成代码的情况"。
> 
> 保持原意：**未经审查、原型质量的 LLM 生成代码**，与已提升到生产标准的代码区分开来。

## Karpathy 的完整论述

Andrej Karpathy 在 LLM Wiki 文章中进一步阐述：

> "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."

这揭示了 Vibe Coding 的深层含义：当 LLM 成为"程序员"，人类角色转变为：
- **Sourcing** — 提供知识源
- **Exploration** — 探索和验证
- **Questioning** — 提出正确的问题

---

## 关联概念

- [[Software-2.0]] - Vibe Coding 是 Software 2.0 的实践延伸
- [[Agentic-Engineering]] - 与 Vibe Coding 对比的工程范式
- [[Harness-Engineering]] - 超越 Agentic Engineering：不仅审查代码，而是构建让 Agent 有效工作的完整系统
- [[Code-Execution]] - Vibe Coding 不强调验证，Agentic Engineering 和 Harness Engineering 强调
- [[Andrej-Karpathy]] - 概念提出者

Vibe Coding 与 Software 2.0 的关系：

| Software 2.0 | Vibe Coding |
|--------------|-------------|
| 程序员写目标 | 用户说"氛围" |
| 神经网络生成程序 | LLM 生成代码 |
| 数据是源代码 | 对话是源代码 |

## 关键数据点

- Andrej Karpathy 于 2025 年 2 月提出该术语
- Karpathy 的原始描述："I just see things, say things, run things, and copy paste things, and it mostly works."
- Claude Code 于 2025 年 3 月发布（Karpathy 提出术语后仅 3 周）
- LLM Wiki 的深层含义："Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."

## 前提与局限性

- 依赖前提：人类愿意接受"忘记代码存在"的开发方式
- 适用边界：快速原型、个人实验、学习探索、一次性脚本
- 局限性：不适用于生产环境、团队协作、长期维护系统、安全敏感应用
- 质量标准：未经审查、原型质量，与生产就绪代码有本质区别
- 术语滥用风险：不应将"任何 LLM 生成代码"都定义为 Vibe Coding

---

> **来源**：Andrej Karpathy (2025-02, 2026-04), Simon Willison (Agentic Engineering Patterns, 2026)