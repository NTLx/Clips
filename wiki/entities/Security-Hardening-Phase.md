---
type: entity
title: Security Hardening Phase
aliases:
  - Security Hardening Phase
  - 安全硬化阶段
  - Hardening Phase
definition: "Drew Breunig (2026) 提出的 Agentic Coding 第三阶段：识别漏洞直到预算耗尽，money 是瓶颈而非 human input。"
created: 2026-04-21
updated: 2026-04-21
tags:
  - agentic-coding
  - cybersecurity
  - software-engineering
related_entities:
  - "[[Cybersecurity-Proof-of-Work]]"
  - "[[Agentic-Engineering]]"
  - "[[Drew-Breunig]]"
source_raw:
  - "20260414-cybersecurity-proof-of-work"
---

# Security Hardening Phase

> [!definition] 定义
> Agentic Coding 的第三阶段：识别漏洞直到预算耗尽。

## 三阶段模型

| 阶段 | 任务 | 瓶颈 | 特点 |
|------|------|------|------|
| **开发** | 实现功能、快速迭代 | Human input | 人类直觉主导 |
| **代码审查** | 文档、重构、PR 审查 | Human input | 应用最佳实践 |
| **安全硬化** | 识别漏洞、持续审计 | Money (tokens) | 自主运行直到预算耗尽 |

## 关键数据点

- **Anthropic Code Review**: `$15-20` per review（代码审查阶段产品）
- **Mythos Hardening**: `$12,500` per attempt (100M tokens)
- **历史对比**: 安全审计从"rare, discrete, inconsistent"变为"constant, within optimal budget"

## 前提与局限性

- **前提**: 
  1. 模型安全能力随 tokens 增加
  2. 有明确的硬化成功标准
- **局限性**: 
  1. 为什么硬化前要先完成开发？避免浪费 tokens 硬化未稳定代码
  2. 预算上限需人工决策

## 关联概念

- [[Cybersecurity-Proof-of-Work]] — 硬化阶段的核心博弈
- [[Agentic-Engineering]] — 扩展为三阶段模型
- [[Drew-Breunig]] — 提出者

## 实践意义

- 安全从"一次性审计"变为"持续投入"
- 代码便宜，除非需要安全
- 硬化成本由漏洞市场价值决定（而非模型推理成本）