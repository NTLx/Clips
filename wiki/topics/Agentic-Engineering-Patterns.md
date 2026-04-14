---
type: topic
title: Agentic Engineering Patterns
description: "Simon Willison 的 Agentic Engineering 指南系列，定义 AI 编程代理时代的工程范式"
created: 2026-04-10
updated: 2026-04-14
tags:
  - AI-Agent
  - coding-agents
  - best-practices
related_entities:
  - "[[Agentic-Engineering]]"
  - "[[Coding-Agents]]"
  - "[[Code-Execution]]"
  - "[[Compound-Engineering]]"
  - "[[Raj-Nandan-Sharma]]"
  - "[[Simon-Willison]]"
  - "[[Technical-Debt-Avoidance]]"
  - "[[Vibe-Coding]]"
source_raw:
  - "[[20260410-what-is-agentic-engineering]]"
  - "[[20260410-code-is-cheap]]"
  - "[[20260410-hoard-things-you-know]]"
  - "[[20260410-better-code]]"
  - "[[20260410-anti-patterns]]"
---

# Agentic Engineering Patterns

> **作者**：Simon Willison
> **定位**：识别能产生实际结果、且不会因工具进步而过时的模式

## 核心定义

**Agentic Engineering** 是使用 Coding Agents 辅助开发软件的实践。

### Agent 定义

> **Agents run tools in a loop to achieve a goal**

- 调用 LLM，传入 prompt 和工具定义
- 执行 LLM 请求的工具
- 将结果反馈给 LLM
- 循环直到目标达成

### Coding Agents

能**编写和执行代码**的 agents：

- Claude Code
- OpenAI Codex
- Gemini CLI

---

## 指南章节

### Principles（原则）

| 章节 | 核心观点 |
|------|---------|
| **What is agentic engineering** | Code Execution 是决定性能力 |
| **Writing code is cheap now** | 代码成本从昂贵到几乎免费 |
| **Hoard things you know** | 囤积可运行代码示例作为资产 |
| **AI should help produce better code** | 用助手预防技术债务 |
| **Anti-patterns** | 不要提交未审查的代码 |

### Working with Coding Agents

| 章节 | 核心观点 |
|------|---------|
| **Using Git** | Agent 深度理解 Git，可处理复杂操作 |
| **Subagents** | 并行代理处理独立任务 |

### Testing and QA

- Red/green TDD
- First run the tests
- Agentic manual testing

---

## 核心洞察

### Code Execution 是关键

> [!important] 决定性能力
> 没有 Code Execution，LLM 输出价值有限。
> 有了 Code Execution，Agent 可以迭代出**可验证工作的软件**。

### 代码成本范式转变

```
传统：生产几百行代码需要一天
现在：编码代理几乎免费产出代码
```

**影响**：
- 重估所有权衡决策
- 对代码异味零容忍
- 异步代理后台重构

### 知识囤积

收集可运行代码示例的价值：

- 维护博客/TIL 记录解决方案
- GitHub repos 作为概念验证
- HTML tools 集合
- 用 prompt 指引 Agent 组合现有示例

### 复合工程

```
项目完成 → 回顾 → 记录有效做法 → 未来运行使用
```

小改进复合，编码助手意味着**可以兼得新功能 + 高质量**。

---

## 与 Vibe Coding 的区别

| 维度 | Vibe Coding | Agentic Engineering |
|------|-------------|---------------------|
| 代码质量 | 原型级 | 生产级 |
| 审查程度 | 无 | 深度审查 |
| 验证方式 | 凭感觉 | 自动测试 |
| 目标 | 快速原型 | 可工作软件 |

> [!warning] 保持区分
> 不要把 Vibe Coding 扩展为"任何 LLM 生成代码"。
> 保持原意：**未经审查、原型质量的 LLM 生成代码**。

---

## 相关主题

- [[Coding-Agents]] - 工具层面
- [[Agent-Workflow-Patterns]] - 架构模式
- [[ACI-Agent-Computer-Interface]] - 接口设计

## 参见

- [[Raj-Nandan-Sharma]] - AI Agent 实践文章作者
- [[Simon-Willison]] - Agentic Engineering 指南作者
- [[Technical-Debt-Avoidance]] - Agentic Engineering 核心模式：用助手预防技术债务

---

> **来源**：Simon Willison, [Agentic Engineering Patterns Guide](https://simonwillison.net/guides/agentic-engineering-patterns/)