---
type: entity
title: History Rewriting
definition: "将 Git 提交历史视为可编辑的叙事而非永久记录的理念，使历史成为帮助未来开发的工具。"
created: 2026-04-09
updated: 2026-04-09
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

## 关联概念

- [[Git-Fluent-Agents]] - Agent 执行 History Rewriting 的工具
- [[Agentic-Engineering]] - History Rewriting 是 Agentic Engineering 的实践之一

## 来源

- Raw Source: [[Using Git with coding agents - Agentic Engineering Patterns]]