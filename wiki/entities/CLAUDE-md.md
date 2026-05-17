---
type: entity
title: CLAUDE.md
aliases:
  - CLAUDE.md
  - 架构上下文文档
definition: "用于为 Claude Code 提供持久化上下文、架构决策和规范约束的 Markdown 文件，是 AI 原生开发中防止“架构漂移”的核心机制。"
created: 2026-05-13
updated: 2026-05-13
tags:
  - AI-Agent
  - Documentation
  - Software-Engineering
related_entities:
  - "[[Claude-Code]]"
  - "[[Agentic-Engineering]]"
  - "[[AI-Native-Startup]]"
source_raw:
  - "[[The-Founders-Playbook-05062026_v3]]"
---

# CLAUDE.md

> [!definition] 定义
> **CLAUDE.md** 是 AI Agent 的“长期记忆”，它显式记录了项目不应随对话丢失的硬性规则。

## 核心作用

1. **防止架构漂移**：确保 Agent 在不同会话中遵循一致的架构决策，而非随意推导。
2. **定义技术栈与规范**：记录使用的库、编码风格、测试要求及安全边界。
3. **沉淀决策背景**：记录“为什么”这么做的权衡（Trade-offs），而不仅仅是结果。

## 最佳实践

- **会话前同步**：开启新会话时先由 Agent 读取此文件。
- **会话后更新**：会话产生的任何新决策应及时更新回文件中。
- **模块化**：在大型项目中可以使用多个子目录下的 `.md` 文件提供局部上下文。

## 关联概念

- [[Claude-Code]] - 主要读取者
- [[Agentic-Engineering]] - 实践框架
