---
type: raw
source: "https://simonwillison.net/guides/agentic-engineering-patterns/anti-patterns/"
author:
  - "[[Simon-Willison]]"
published: "2026-03-04"
updated: "2026-03-04"
created: "2026-04-10"
tags:
  - clippings
  - AI-Agent
  - coding-agents
  - agentic-engineering
  - code-review
description: "讨论 AI 编程时代需要避免的反模式，重点强调不要将未经审查的代码提交给协作者审查。"
changes_url: "https://simonwillison.net/guides/agentic-engineering-patterns/anti-patterns/changes/"
---

# Anti-patterns: things to avoid

> [!info] 文章来源
> - 作者: [[Simon-Willison]]
> - 来自《Agentic Engineering Patterns》指南系列

## 概述

在 AI 编程（agentic engineering）这个新世界中，存在一些需要避免的反模式行为。

## Inflicting unreviewed code on collaborators

这是一个常见且令人深感沮丧的反模式。

**核心原则**：不要提交你自己没有审查过的代码作为 Pull Request。

如果你打开一个包含数百（或数千）行由 agent 生成的代码的 PR，而你自己没有确保这些代码能正常工作，那么你实际上是将真正的工作推给了其他人。

> [!warning] 关键问题
> 别人自己也可以让 agent 生成代码。那你到底提供了什么价值？

如果你提交代码供审查，你需要确信它已经准备好让其他人花时间去审查。**最初的审查是你的责任**，而不是你应该外包给别人的事情。

### 一个好的 AI 编程 Pull Request 应具备的特征

1. **代码能运行**，而且你有信心它能运行。你的任务是交付能运行的代码。

2. **改动足够小**，可以在不给审查者带来过多认知负担的情况下高效审查。几个小 PR 比一个大 PR 更好，而且让 coding agent 帮你处理 Git 操作来拆分代码是很容易的。

3. **PR 包含额外上下文**，帮助解释这个改动。这个改动服务于什么更高层级的目标？链接到相关 issue 或规格说明在这里很有用。

4. **审查 agent 写的 PR 描述**。Agent 会写出看起来很有说服力的 PR 描述，你也需要审查这些内容！指望别人去读你自己都没读过和验证过的文字是不礼貌的。

### 最佳实践建议

考虑到向别人倾倒未审查代码是多么容易，我建议包含一些形式的证据来表明你已经付出了额外的努力：

- 关于你如何手动测试的笔记
- 对特定实现选择的评论
- 甚至截图和视频展示功能正常工作

这些都能**大大证明**审查者的时间不会浪费在挖掘细节上。

---

## AI 提取元数据

### 核心概念
- **Agentic Engineering**: AI 辅助编程工程模式
- **Code Review Anti-pattern**: 将未审查代码推给协作者的反模式
- **Pull Request Quality**: PR 质量标准

### 相关链接
- [[Agentic-Engineering-Patterns|Agentic Engineering Patterns 指南]] - 本文所属系列
- [Your job is to deliver code that works](https://simonwillison.net/2025/Dec/18/code-proven-to-work/) - 相关文章

### 推荐分类
- **主分类**: AI-Agent
- **子分类**: coding-agents / agentic-engineering

### 章节索引
本文是《Agentic Engineering Patterns》指南的一个章节：
- Principles → Anti-patterns: things to avoid（本文）
- Working with coding agents → Testing and QA → Understanding code → Appendix

---

> [!note] 元数据
> - Created: 4th March 2026
> - Last modified: 4th March 2026
> - Tag counts: ai (1954), llms (1701), coding-agents (190), agentic-engineering (41), code-review (14)

---

## 编译摘要

### 1. 浓缩
- **核心结论1**: AI 编程时代最大的反模式是将未经审查的代码作为 PR 提交给协作者
  - 关键证据: 别人也可以让 agent 生成代码，你需要提供真正的价值——确保代码能运行
- **核心结论2**: 好的 AI 编程 PR 应具备四个特征：代码能运行、改动足够小、提供额外上下文、审查 agent 写的 PR 描述
  - 关键证据: 几百行未审查代码的 PR 是对审查者时间的浪费
- **核心结论3**: 建议提供额外证据证明你付出了额外努力——手动测试笔记、实现选择评论、截图视频
  - 关键证据: 这些能证明审查者的时间不会浪费

### 2. 质疑
- **关于"代码能运行"的质疑**: 如何定义"能运行"？通过测试就算还是需要实际使用验证？
- **关于"改动足够小"的质疑**: 拆分 PR 是好实践，但何时拆？如何平衡拆分粒度和整体功能完整性？
- **关于证据的质疑**: 截图和视频是否可验证？审查者如何确认这些证据的真实性？

### 3. 对标
- **跨域关联1**: 类似产品发布流程——不仅仅是功能可用，还要考虑用户体验和后续支持
- **跨域关联2**: 类似学术论文审稿——作者有责任确保论文质量，而非丢给审稿人发现所有问题
- **可迁移场景**: 任何涉及 AI 生成内容需要人工审核的场景——文档、报告、设计稿

### 关联概念
- [[Agentic-Engineering]]
- [[Code-Execution]]
- [[Context-Engineering]]
- [[Refusal]]