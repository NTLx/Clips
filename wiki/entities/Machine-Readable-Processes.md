---
type: entity
title: Machine-Readable Processes
aliases:
  - Machine Readable Processes
definition: "Process definitions that are structured and explicit, enabling AI agents to understand, execute, and optimize workflows autonomously."
created: 2026-04-09
updated: 2026-04-16
tags:
  - AI-Agent
  - Process-Design
  - Technical-Architecture
related_entities:
  - "[[Agent-First-Enterprise]]"
  - "[[Human-Governor-Agent-Operator]]"
  - "[[Harness-Engineering]]"
source_raw:
  - "[[Enabling agent-first process redesign]]"
  - "[[20260413-why-ai-first-strategy-wrong]]"
---

# Machine-Readable Processes

> [!definition] 定义
> Machine-Readable Processes 是指结构化、显式的流程定义，使 AI Agent 能够理解、执行和自主优化工作流程。这是 Agent-First Enterprise 的技术基础设施。

## 核心要点

### 三大要素

| 要素 | 说明 | 示例 |
|-----|------|-----|
| **流程定义** | 机器可理解的工作流程描述 | YAML/JSON 格式的流程配置 |
| **政策约束** | 明确的边界和规则约束 | "审批金额上限"、"数据访问权限" |
| **结构化数据流** | 标准化的数据输入输出 | API 接口定义、数据 Schema |

### 与遗留流程的区别

| 维度 | 遗留流程 | Machine-Readable 流程 |
|-----|---------|----------------------|
| 表达形式 | 文档、手册、隐性知识 | 代码、配置、显式定义 |
| 执行方式 | 人类理解后执行 | Agent 直接执行 |
| 优化能力 | 需人工分析改进 | Agent 可动态优化 |

### 为什么 Agent 需要它
- Legacy processes 不是为自主系统设计的
- Agent 需要明确的规则边界来安全运营
- 结构化数据流支持实时决策

## 关键数据点

- AI 技术预算预计未来两年增长超过 70%，agents 需要结构化流程才能发挥潜力
- Machine-Readable 流程的三大要素：流程定义（YAML/JSON）、政策约束（金额上限/权限）、结构化数据流（API/Schema）
- 遗留流程以文档、手册、隐性知识表达；Machine-Readable 流程以代码、配置、显式定义表达
- Agent 可动态优化流程，而遗留流程需人工分析改进

## 前提与局限性

- 仅适用于可被结构化和显式定义的流程——高度创意或探索性工作难以机器可读化
- 需要先有明确的 policy constraints，否则 Agent 缺乏安全运营边界
- 遗留系统的迁移成本可能很高——不是所有企业都能快速转换
- 机器可读流程假设数据流标准化，但现实中很多组织的数据流是碎片化的

## 关联概念

- [[Agent-First-Enterprise]] - Machine-Readable Processes 是其技术基础
- [[Human-Governor-Agent-Operator]] - 政策约束由人类 Governor 定义

## 来源

- Raw Source: [[Enabling agent-first process redesign]]
- Original URL: https://www.technologyreview.com/2026/04/07/1134966/enabling-agent-first-process-redesign/