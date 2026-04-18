---
type: entity
title: History Rewriting
aliases:
  - History Rewriting
definition: "将 Git 提交历史视为可编辑的叙事而非永久记录的理念，使历史成为帮助未来开发的工具。"
created: 2026-04-09
updated: 2026-04-15
tags:
  - AI-Agent
  - Software-Engineering
  - Git
related_entities:
  - "[[Git-Fluent-Agents]]"
  - "[[Agentic-Engineering]]"
source_raw:
  - "[[Using Git with coding agents - Agentic Engineering Patterns]]"
---

# History Rewriting

> [!definition] 定义
> History Rewriting 是将 Git 提交历史视为可编辑的叙事而非永久记录的理念。

## 核心要点

### Git 历史的本质
- Git 历史不是"实际发生什么"的永久记录
- Git 历史是"故意编辑的叙事"，描述项目进展
- 这个叙事是帮助未来开发的工具

### Agent 能执行的重写操作
- **Undo commits**: `git reset --soft HEAD~1`
- **Remove specific files**: 从提交中移除特定文件
- **Combine commits**: 合并多个提交为单个单元
- **Rewrite messages**: 重写提交信息

## 关键数据点

- Git 历史不是"实际发生了什么"的永久记录，而是"故意编辑的叙事"
- 历史是帮助未来开发的工具，作者可以做编辑决策决定保留什么
- 常用重写操作：`git reset --soft HEAD~1`（撤销提交）、从提交中移除特定文件、合并多个提交、重写提交信息
- Agent 可以从旧仓库中提取代码到新仓库，同时保留关键的提交历史（作者和日期）

## 前提与局限性

- 历史重写仅适用于未推送或局部范围的提交，共享历史改写需团队协调
- 改写历史的前提是 Git 数据结构本质是文件（`.git/` 目录），可以被修改
- 频繁改写历史可能影响团队协作，应在个人或功能分支上使用
- Agent 执行重写时需要人类确认，避免意外丢失重要历史

## 关联概念

- [[Git-Fluent-Agents]] - Agent 执行 History Rewriting 的工具
- [[Agentic-Engineering]] - History Rewriting 是 Agentic Engineering 的实践之一

## 来源

- Raw Source: [[Using Git with coding agents - Agentic Engineering Patterns]]