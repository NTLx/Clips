---
type: entity
title: Agentic Engineering
aliases:
  - Agentic Engineering
definition: "使用 Coding Agents 辅助开发软件的实践，核心能力是 Code Execution 使 Agent 能迭代出可验证工作的软件"
created: 2026-04-09
updated: 2026-04-16
tags:
  - AI-Agent
  - Software-Engineering
  - Development-Paradigm
related_entities:
  - "[[Code-Execution]]"
  - "[[Coding-Agents]]"
  - "[[Vibe-Coding]]"
  - "[[Harness-Engineering]]"
  - "[[Compound-Engineering]]"
  - "[[Git-Fluent-Agents]]"
source_raw:
  - "[[Using Git with coding agents - Agentic Engineering Patterns]]"
  - "[[20260410-what-is-agentic-engineering]]"
  - "[[Why Your \u201cAI-First\u201d Strategy Is Probably Wrong]]"
  - "[[20260409-ai-capability-gap-ai-psychosis]]"
---

# Agentic Engineering

> [!definition] 定义
> **Agentic Engineering** 是使用 Coding Agents 辅助开发软件的实践。

## 核心定义

> **Agents run tools in a loop to achieve a goal**

Agent 软件：
1. 调用 LLM，传入用户提示和工具定义
2. 执行 LLM 请求的工具
3. 将结果反馈给 LLM
4. 循环直到目标达成

### Code Execution：决定性能力

> [!important] 核心洞察
> **Code Execution is the defining capability that makes agentic engineering possible.**
> 
> 没有直接运行代码的能力，LLM 输出价值有限。
> 有了 Code Execution，Agent 可以迭代出**可验证工作的软件**。

## 核心原则（Simon Willison）

| 原则 | 说明 | 实践意义 |
|-----|------|---------|
| **Writing code is cheap now** | 代码成本趋近于零 | 可以更雄心勃勃地尝试 |
| **Hoard things you know how to do** | 囤积可运行代码示例 | 记录可复用的解决方案 |
| **AI should help produce better code** | AI 应帮助产出更好的代码 | 不是更快，而是更好 |
| **Anti-patterns** | 不要提交未审查的代码 | 你的工作是交付能工作的代码 |

## 与 Vibe Coding 的区别

| 维度 | Vibe Coding | Agentic Engineering |
|------|-------------|---------------------|
| **代码质量** | 原型级、未审查 | 生产级、已验证 |
| **验证方式** | 无/凭感觉 | 自动测试 + 运行验证 |
| **人类角色** | "忘记代码存在" | 验证者、迭代者 |
| **目标** | 快速原型 | 可工作软件 |

> [!warning] 保持区分
> Vibe Coding 应保持原意：**未经审查、原型质量的 LLM 生成代码**，与已提升到生产标准的代码区分开来。

## 核心实践

| 领域 | Agent 角色 | 人类角色 |
|------|-----------|---------|
| **Git 操作** | 执行复杂命令、解决冲突 | 设定目标、审核结果 |
| **测试** | Red/Green TDD、运行测试 | 定义测试策略 |
| **代码理解** | Linear walkthroughs、解释代码 | 提出问题 |
| **重构** | 后台异步重构 | PR 评估 |
| **历史管理** | History Rewriting | 编辑决策 |

## 关键数据点

- Agent 定义：**Agents run tools in a loop to achieve a goal**
- Code Execution 是决定性能力：没有直接运行代码的能力，LLM 输出价值有限
- Vibe Coding 一词由 Andrej Karpathy 在 2025 年 2 月提出（Claude Code 发布前三周）
- 四项核心原则：代码成本趋近于零、囤积可运行代码示例、AI 应帮助产出更好的代码、不提交未审查的代码

## 前提与局限性

- Agentic Engineering 依赖 coding agents 具备代码执行能力，纯文本 LLM 无法胜任
- 人类角色从"写代码"转为"验证和迭代"，需要对结果负责
- LLM 不从过去错误中学习，需要人类显式更新指令和工具 harness
- Vibe Coding 和 Agentic Engineering 应保持区分：前者是未审查原型，后者是生产级代码

## 关联概念

- [[Code-Execution]] - 决定性能力
- [[Coding-Agents]] - Claude Code, Codex, Gemini CLI
- [[Vibe-Coding]] - 对比概念
- [[Compound-Engineering]] - 持续改进模式
- [[Git-Fluent-Agents]] - Git 实践

## 来源

- [[Using Git with coding agents - Agentic Engineering Patterns]]
- [[20260410-what-is-agentic-engineering]]
- Simon Willison, [Agentic Engineering Patterns Guide](https://simonwillison.net/guides/agentic-engineering-patterns/)