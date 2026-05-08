---
type: entity
title: Product Overhang
aliases:
  - Product Overhang
  - 产品能力溢出
definition: "Boris Cherny 提出的概念：AI 模型已经具备的能力超出了现有产品所能释放的边界——大量模型潜力未被产品化，等待被\"追赶\""
created: 2026-05-08
updated: 2026-05-08
tags:
  - AI
  - product-strategy
  - claude-code
related_entities:
  - "[[Boris-Cherny]]"
  - "[[Claude-Code-CLI]]"
  - "[[Agent-Loops]]"
  - "[[Agentic-Engineering]]"
source_raw:
  - "[[Anthropic's Boris Cherny: Why Coding Is Solved, and What Comes Next]]"
---

# Product Overhang（产品能力溢出）

> [!definition] 定义
> **Product Overhang** 由 Boris Cherny 提出，描述一种 AI 时代特有的不对称现象：底层模型已经具备的能力，远远超出了现有产品界面和交互范式所能释放的边界。就像模型能飞但产品还在地上走。Boris 用这个词解释 Claude Code 的构建策略——不是为当前模型构建，而是为"下一代模型"构建。

## 关键数据点

- **Claude Code 起源**：2024 年底，编程交互主流仍是 typeahead（Tab 补全一行），但模型（Sonnet 3.5）实际已能做到的远不止于此。Boris 团队判断"不需要补全了，直接让 Agent 写全部代码"
- **Pre-PMF 策略**：Claude Code 前 6 个月没有 PMF——Boris 自己只用它写 10% 代码。团队的 deliberate 选择是"等模型赶上产品"
- **Opus 4 拐点**（2025 年 5 月）：Claude Code 开始指数增长，此后每一代新模型（4.5 → 4.6 → 4.7）都是另一个 inflection point
- **反向逻辑**：传统产品构建路径是"识别需求 → 用现有技术满足"；Product Overhang 的逻辑是"识别模型隐藏能力 → 为能力构建产品界面"

## 前提与局限性

- Product Overhang 的前提是模型能力持续进步——如果模型进展停滞，overhang 会消失
- 判断哪些模型能力是"可持续的"而非"偶然的"本身就是巨大的不确定性
- Pre-PMF 策略需要组织有足够耐心和资源支撑——不适合所有公司

## 关联概念

- [[Agent-Loops]] — Product Overhang 的典型案例：模型现在就能做到，产品刚刚开始释放
- [[Claude-Code-CLI]] — Product Overhang 策略的产物
- [[Agentic-Engineering]] — 如何系统性利用 overhang 的工程实践
