---
type: entity
title: Code Execution
definition: "AI Agent 直接运行代码的能力，是 Agentic Engineering 的决定性能力"
created: 2026-04-10
updated: 2026-04-10
tags:
  - AI-Agent
  - coding-agents
  - core-capability
related_entities:
  - "[[Agentic-Engineering]]"
  - "[[Coding-Agents]]"
source_raw:
  - "[[20260410-what-is-agentic-engineering.md]]"
---

# Code Execution（代码执行）

> **核心洞察**：代码执行是使 Agentic Engineering 成为可能的决定性能力。

## 定义

**Code Execution** 是 Coding Agents 的核心能力：能够直接运行生成的代码，而非仅仅输出代码文本。

> [!important] 关键区分
> 没有 Code Execution，LLM 输出的内容价值有限。
> 有了 Code Execution，Agent 可以迭代出**可验证工作的软件**。

## 为什么重要

### 传统 LLM 编程的局限

```
User → LLM → 代码文本 → 人类复制粘贴 → 人类运行测试 → 人类反馈
```

### Coding Agent 的闭环

```
User → Agent → 代码 → 自动执行 → 测试结果 → 自动迭代
                    ↑                              ↓
                    ←←←← 反馈循环 ←←←←←←←←←←←←←←←←
```

## 能力层级

| 层级 | 描述 | 例子 |
|------|------|------|
| **Read** | 读取代码库 | 理解项目结构 |
| **Write** | 生成代码 | 创建新文件 |
| **Execute** | 运行代码 | 执行脚本、测试 |
| **Iterate** | 基于结果改进 | 测试失败 → 修复 → 再测试 |

## 与 Vibe Coding 的区别

| 维度 | Vibe Coding | Agentic Engineering |
|------|-------------|---------------------|
| 代码质量 | 原型级、未审查 | 生产级、已验证 |
| 验证方式 | 无 | 自动测试 + 运行验证 |
| 人类角色 | "忘记代码存在" | 验证者、迭代者 |

## 相关概念

- [[Agentic-Engineering]] - 以此能力为基础的工程范式
- [[Coding-Agents]] - 具备此能力的 Agent 类型
- [[Vibe-Coding]] - 不强调验证的对比模式

---

> **来源**：Simon Willison, "What is agentic engineering?" (Agentic Engineering Patterns, 2026)