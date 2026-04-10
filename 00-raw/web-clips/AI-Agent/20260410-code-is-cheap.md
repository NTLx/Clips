---
type: raw
source: "https://simonwillison.net/guides/agentic-engineering-patterns/code-is-cheap/"
author:
  - "[[Simon Willison]]"
published: "2026-02-23"
updated: "2026-02-24"
created: "2026-04-10"
tags:
  - clippings
  - AI-Agent
  - coding-agents
  - ai-assisted-programming
  - agentic-engineering
description: "Simon Willison 探讨 AI 编程代理时代下代码成本的变化，以及开发者需要建立的新习惯。"
changes_url: "https://simonwillison.net/guides/agentic-engineering-patterns/code-is-cheap/changes/"
---

# Writing code is cheap now

> 这是 Agentic Engineering Patterns 指南中的一章。

## 核心观点

采用 AI 代理工程实践的最大挑战是接受一个事实：**写代码现在很便宜了**。

代码一直以来都是昂贵的。生产几百行干净、经过测试的代码需要大多数软件开发者一整天甚至更长时间。我们的许多工程习惯——无论是宏观还是微观层面——都建立在这个核心约束之上。

### 宏观层面

我们花费大量时间在设计、估算和规划项目上，以确保昂贵的编码时间被尽可能高效地利用。产品功能想法的评估基于它们能提供多少价值**来换取那个时间**——一个功能需要多次赚回其开发成本才算值得！

### 微观层面

我们每天做出数百个基于可用时间和预期权衡的决策：
- 如果重构那个函数让它稍微优雅一点会增加一小时的编码时间，值得吗？
- 写文档呢？
- 为这个边缘情况添加测试值得吗？
- 我能 justify 为这个构建一个调试界面吗？

编码代理大幅降低了将代码输入计算机的成本，这颠覆了我们许多现有的个人和组织直觉——关于哪些权衡是合理的。

运行并行代理的能力使评估变得更加困难，因为一个人类工程师现在可以在多个地方同时实现、重构、测试和记录代码。

## Good code still has a cost

交付新代码的价格已经降到几乎免费……但交付**好代码**仍然比这昂贵得多。

### 什么是好代码？

- **代码能工作**。它做它该做的事，没有 bug。
- **我们知道代码能工作**。我们采取了步骤来确认自己和他人代码是适用的。
- **它解决了正确的问题**。
- **它优雅地处理错误情况**：不只考虑 happy path。错误应该提供足够的信息帮助未来的维护者理解出了什么问题。
- **它简单且最小**——它只做需要的，以一种人和机器现在和未来都能理解的方式。
- **它有测试保护**。测试显示它现在能工作，并作为回归套件避免它在未来悄悄崩溃。
- **它在适当的级别有文档**，且文档反映系统的当前状态——如果代码改变了现有行为，现有文档需要更新以匹配。
- **设计支持未来变更**。重要的是保持 YAGNI——添加复杂性以预期可能永远不会到来的未来变更的代码往往是坏代码——但也重要的是不要写出让未来变更比它们应该的更难的代码。
- **所有其他相关的"ilities"**——可访问性、可测试性、可靠性、安全性、可维护性、可观察性、可扩展性、可用性——适合正在开发的特定类别软件的非功能性质量度量。

编码代理工具可以帮助处理大部分这些，但在驱动这些工具的开发者身上仍有相当大的负担，以确保生产的代码对于当前项目所需的那部分"好"来说是好代码。

## We need to build new habits

挑战在于开发新的个人和组织习惯，响应代理工程的能力和机会。

这些最佳实践仍在我们的行业中被摸索出来。我自己也还在摸索。

目前我认为我们能做的最好是怀疑自己：任何时候我们的直觉说"不要构建那个，不值得花时间"，反正发送一个 prompt，在一个异步代理会话中，最坏的情况是你十分钟后检查发现它不值得那些 tokens。

---

> [!info] 导航
> 上一章：[[What is agentic engineering]]
> 下一章：[[Hoard things you know how to do]]

---

## AI 提取元数据

### 核心概念

1. **Code Cost Paradigm Shift** - 代码成本范式转变：从昂贵到几乎免费
2. **Good Code vs Cheap Code** - 好代码与廉价代码的区别
3. **Agentic Engineering Habits** - 代理工程需要的新习惯
4. **YAGNI** - You Aren't Gonna Need It 原则

### 相关主题

- [[Agentic Engineering]] - 代理工程方法论
- [[Coding Agents]] - 编程代理工具
- [[AI-Assisted Programming]] - AI 辅助编程

### 来源信息

- 作者：[[Simon Willison]]
- 系列：Agentic Engineering Patterns 指南
- 创建日期：2026-02-23
- 最后修改：2026-02-24
- 标签：coding-agents, ai-assisted-programming, generative-ai, agentic-engineering, yagni