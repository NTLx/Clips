---
type: entity
title: Compound Engineering
definition: "持续改进 Agent 指令和工具配置的模式，每个项目后记录有效做法供未来运行使用"
created: 2026-04-10
updated: 2026-04-10
tags:
  - AI-Agent
  - coding-agents
  - best-practices
related_entities:
  - "[[Agentic-Engineering]]"
  - "[[Coding-Agents]]"
source_raw:
  - "[[20260410-better-code]]"
---

# Compound Engineering（复合工程）

> **核心理念**：每个编码项目以回顾结束，记录有效内容用于未来的 Agent 运行

## 定义

**Compound Engineering** 是 Every (Dan Shipper & Kieran Klaassen) 提出的模式，描述与编码助手持续改进的工作方式：

```
项目完成 → Compound Step（回顾）→ 记录有效做法 → 未来运行使用
```

## 核心循环

### 1. 执行项目

使用编码助手完成开发任务。

### 2. Compound Step

项目结束时的回顾环节：

- 什么做法有效？
- 什么指令帮助最大？
- 遇到什么问题？
- 如何避免未来问题？

### 3. 记录沉淀

将学习内容记录到：

- CLAUDE.md 或类似配置文件
- 自定义指令
- 工具文档

### 4. 未来复用

下次运行时，Agent 可以访问这些积累的知识。

## 关键洞察

> [!tip] 复合效应
> 小改进会复合。曾经耗时的质量增强现在成本已降至没有借口不投资质量。
> 
> **编码助手意味着我们终于可以两者兼得**：新功能 + 高质量。

## 与传统开发的区别

| 维度 | 传统开发 | Compound Engineering |
|------|---------|---------------------|
| 学习沉淀 | 个人经验 | 可复用指令 |
| 知识传递 | 文档/培训 | Agent 配置 |
| 迭代速度 | 手动改进 | 自动应用 |
| 知识累积 | 线性 | 复合增长 |

## 实践建议

1. **每个 PR 后**：记录什么提示有效
2. **遇到问题时**：更新指令避免重复
3. **成功模式**：标准化为可复用模板
4. **工具文档**：持续优化 Agent-Computer Interface

## 相关概念

- [[Agentic-Engineering]] - 基础工程范式
- [[ACI-Agent-Computer-Interface]] - 工具接口设计
- [[Technical-Debt-Avoidance]] - 复合工程帮助避免技术债务

---

> **来源**：Simon Willison, "AI should help us produce better code" (Agentic Engineering Patterns, 2026)