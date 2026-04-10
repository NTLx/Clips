---
type: raw
source: "https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering/"
author:
  - "[[Simon Willison]]"
published: "2026-03-15"
updated: "2026-03-16"
created: "2026-04-10"
tags:
  - clippings
  - AI-Agent
  - agentic-engineering
  - coding-agents
  - llms
description: "Simon Willison 定义了 agentic engineering —— 使用 coding agents 辅助开发软件的实践，解释了 agents 的核心定义（在循环中运行工具以达成目标），以及与 vibe coding 的区别。"
changes_url: "https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering/changes/"
---

# What is agentic engineering?

> [!info] 文章来源
> - 作者: [[Simon Willison]]
> - 发布日期: 2026-03-15
> - 原文链接: [What is agentic engineering?](https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering/)
> - 所属指南: [[Agentic Engineering Patterns]]

---

## 核心定义

**Agentic engineering** 是使用 coding agents 辅助开发软件的实践。

### 什么是 Coding Agents？

Coding agents 是能够**编写和执行代码**的 agents。流行示例包括：
- Claude Code
- OpenAI Codex
- Gemini CLI

### 什么是 Agent？

Agent 的定义：
> **Agents run tools in a loop to achieve a goal**

Agent 软件调用 LLM，传入用户提示和工具定义集合，然后执行 LLM 请求的任何工具，并将结果反馈给 LLM。

对于 coding agents，这些工具包括**能够执行代码的工具**。

用户提示 coding agent 定义一个目标。Agent 然后在循环中生成和执行代码，直到目标达成。

---

## 核心洞察

### Code Execution 是关键

> [!important] 核心能力
> **Code execution is the defining capability that makes agentic engineering possible.**

没有直接运行代码的能力，LLM 输出的任何内容价值有限。有了代码执行，这些 agents 可以迭代出**可验证工作的软件**。

### 人类工程师的价值

现在软件能写可工作的代码，人类还有什么用？

> **答案：so much stuff.**

写代码从来不是软件工程师的唯一活动。这个技艺一直是**弄清楚该写什么代码**。任何软件问题都有数十种潜在解决方案，各有权衡。我们的工作是导航这些选项，找到最适合独特情况和需求的方案。

### 有效使用 Coding Agents 的要点

1. **提供工具** - 给 coding agents 解决问题所需的工具
2. **正确规格化** - 以恰当的细节级别描述问题
3. **验证迭代** - 验证并迭代结果，确保稳健可信

> [!tip] 关键洞察
> LLMs 不会从过去的错误中学习，但 coding agents 可以——前提是我们有意识地更新指令和工具配置来纳入沿途所学。

---

## 与 Vibe Coding 的区别

**Vibe coding** 是 Andrej Karpathy 在 2025 年 2 月提出的术语——恰好是 Claude Code 首次发布前三周——描述"忘记代码甚至存在"的 LLM 编程方式。

> [!warning] 区分的重要性
> 不要把 vibe coding 定义扩展到覆盖任何 LLM 生成代码的情况。Vibe coding 应保持原意：**未经审查、原型质量的 LLM 生成代码**——与作者已提升到生产标准的代码区分开来。

---

## 关于本指南

Agentic Engineering Patterns 是一个**持续演进的工作**。目标是识别和描述：
- 能产生实际结果的工作模式
- 不太可能因工具进步而过时的模式

---

## 指南目录

### Principles

1. What is agentic engineering?
2. [[Writing code is cheap now]]
3. [[Hoard things you know how to do]]
4. [[AI should help us produce better code]]
5. [[Anti-patterns: things to avoid]]

### Working with coding agents

1. [[How coding agents work]]
2. [[Using Git with coding agents]]
3. [[Subagents]]

### Testing and QA

1. [[Red/green TDD]]
2. [[First run the tests]]
3. [[Agentic manual testing]]

### Understanding code

1. [[Linear walkthroughs]]
2. [[Interactive explanations]]

### Annotated prompts

1. [[GIF optimization tool using WebAssembly and Gifsicle]]

---

## AI 提取的元数据

### 核心概念

| 概念 | 定义 |
|-----|------|
| **Agentic Engineering** | 使用 coding agents 辅助开发软件的实践 |
| **Coding Agents** | 能编写和执行代码的 agents（Claude Code, Codex, Gemini CLI） |
| **Agent 定义** | 在循环中运行工具以达成目标的软件 |
| **Code Execution** | 使 agentic engineering 成为可能的决定性能力 |
| **Vibe Coding** | 未经审查、原型质量的 LLM 生成代码（Karpathy 2025） |

### 关键引用

1. "Agents run tools in a loop to achieve a goal"
2. "Code execution is the defining capability that makes agentic engineering possible"
3. "Writing code has never been the sole activity of a software engineer. The craft has always been figuring out what code to write."

### 文章定位

- 所属系列: Agentic Engineering Patterns 指南的第一章
- 系列目标: 识别能有效产出结果、且不会因工具进步而过时的模式
- 作者背景: Simon Willison，AI/LLM 领域知名博主和技术专家

---

## 相关链接

- 指南主页: [Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/)
- 作者博客: [Simon Willison's Weblog](https://simonwillison.net/)
- 下一章: [[Writing code is cheap now]]