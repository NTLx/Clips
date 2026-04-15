---
type: raw
source: "https://www.anthropic.com/engineering/building-effective-agents"
author:
  - "[[Erik-Schluntz]]"
  - "[[Barry-Zhang]]"
published: "2024-12-19"
created: "2026-04-10"
tags:
  - clippings
  - AI-Agent
  - LLM
  - agentic-systems
  - workflows
  - tool-use
  - Claude
description: "Anthropic shares practical advice on building effective LLM agents, recommending simple, composable patterns over complex frameworks."
---

# Building Effective AI Agents

We've worked with dozens of teams building LLM agents across industries. Consistently, the most successful implementations use simple, composable patterns rather than complex frameworks.

Over the past year, we've worked with dozens of teams building large language model (LLM) agents across industries. Consistently, the most successful implementations weren't using complex frameworks or specialized libraries. Instead, they were building with simple, composable patterns.

In this post, we share what we've learned from working with our customers and building agents ourselves, and give practical advice for developers on building effective agents.

## What are agents?

"Agent" can be defined in several ways. Some customers define agents as fully autonomous systems that operate independently over extended periods, using various tools to accomplish complex tasks. Others use the term to describe more prescriptive implementations that follow predefined workflows. At Anthropic, we categorize all these variations as **agentic systems**, but draw an important architectural distinction between **workflows** and **agents**:

- **Workflows** are systems where LLMs and tools are orchestrated through predefined code paths.
- **Agents**, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks.

## When (and when not) to use agents

When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all. Agentic systems often trade latency and cost for better task performance, and you should consider when this tradeoff makes sense.

When more complexity is warranted, workflows offer predictability and consistency for well-defined tasks, whereas agents are the better option when flexibility and model-driven decision-making are needed at scale. For many applications, however, optimizing single LLM calls with retrieval and in-context examples is usually enough.

## When and how to use frameworks

There are many frameworks that make agentic systems easier to implement, including:

- The [Claude Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview);
- [Strands Agents SDK by AWS](https://strandsagents.com/latest/);
- [Rivet](https://rivet.ironcladapp.com/), a drag and drop GUI LLM workflow builder; and
- [Vellum](https://www.vellum.ai/), another GUI tool for building and testing complex workflows.

These frameworks make it easy to get started by simplifying standard low-level tasks like calling LLMs, defining and parsing tools, and chaining calls together. However, they often create extra layers of abstraction that can obscure the underlying prompts and responses, making them harder to debug. They can also make it tempting to add complexity when a simpler setup would suffice.

We suggest that developers start by using LLM APIs directly: many patterns can be implemented in a few lines of code. If you do use a framework, ensure you understand the underlying code. Incorrect assumptions about what's under the hood are a common source of customer error.

See our [cookbook](https://platform.claude.com/cookbook/patterns-agents-basic-workflows) for some sample implementations.

## Building blocks, workflows, and agents

In this section, we'll explore the common patterns for agentic systems we've seen in production. We'll start with our foundational building block—the augmented LLM—and progressively increase complexity, from simple compositional workflows to autonomous agents.

### Building block: The augmented LLM

The basic building block of agentic systems is an LLM enhanced with augmentations such as retrieval, tools, and memory.

---

## 编译摘要

### 1. 浓缩
- **核心结论1**: 最简单的方案往往最好——最成功的实现使用简单、可组合的模式，而非复杂框架
  - 关键证据: 应该先用简单的 prompt + retrieval + in-context examples，只有在明确证明能提升效果时才增加复杂度
- **核心结论2**: Workflows vs Agents 选择——预定义工作流适合可预测任务，自主决策适合需要灵活性的复杂任务
  - 关键证据: Coding agents 和 customer support 是两个最有前景的应用场景
- **核心结论3**: Agent-Computer Interface (ACI) 很重要——工具定义和文档应该和 prompt 一样精心设计
  - 关键证据: Anthropic 在 SWE-bench 上花在优化工具的时间比优化 prompt 更多

### 2. 质疑
- **关于"简单"的质疑**: 简单方案是否总是最优？复杂框架是否有存在的必要？
- **关于"自主性"的质疑**: 完全自主的 agents 是否适合生产环境？需要多少人类监督？
- **关于 ACI 的质疑**: 是否存在通用工具设计模式，还是每个工具都需要单独设计？

### 3. 对标
- **跨域关联1**: 类似软件工程中的"过度设计"反模式——YAGNI 原则在 LLM 领域的体现
- **跨域关联2**: 类似自动驾驶分级——从 rules-based 到 end-to-end，agents 是 LLM 的"完全自动驾驶"
- **可迁移场景**: 任何需要 AI 辅助决策和执行的复杂任务——研究代理、自动化运维、多步骤内容创作

### 关联概念
- [[Agentic-Engineering]] - Agent 工程范式
- [[Agent-Workflow-Patterns]] - Agent 工作流模式
- [[ACI-Agent-Computer-Interface]] - Agent 计算机接口
- [[Code-Execution]] - AI 代码执行能力
- [[Context-Engineering]] - Agent 上下文工程

current