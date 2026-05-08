---
type: entity
title: Tool-Use Architecture
aliases:
  - Tool-Use Architecture
  - 工具使用架构
definition: "Demis Hassabis 设想的 AGI 系统架构：通用模型作为工具使用者（orchestrator），专用系统（AlphaFold、材料模拟器等）作为可调用的工具——反对将所有能力塞入一个巨型模型"
created: 2026-05-08
updated: 2026-05-08
tags:
  - AI
  - AGI
  - system-architecture
related_entities:
  - "[[Demis-Hassabis]]"
  - "[[Scientific-Discovery-AI]]"
  - "[[Agent-Orchestration]]"
  - "[[MCP]]"
source_raw:
  - "[[Demis Hassabis: Agents, AGI & The Next Big Scientific Breakthrough]]"
---

# Tool-Use Architecture（工具使用架构）

> [!definition] 定义
> **Tool-Use Architecture** 是 Demis Hassabis 提出的 AGI 系统架构理念：不把所有的知识和能力塞进一个巨大的通用模型（"如果在 Gemini 里放入所有蛋白质数据，它的语言能力会退化"），而是让通用模型成为优秀的工具使用者和协调者，将 AlphaFold、材料模拟器等专用系统当作可调用的工具。这与 Anthropic 的 MCP 协议在架构理念上高度共振。

## 关键数据点

- **信息效率原则**：Hassabis 明确指出一个巨型全能脑会导致"regression"——信息密度并非无限，专业能力和通用能力在单个模型中存在 tradeoff
- **工具使用 vs 大统一模型**：好的通用模型"可能甚至可以训练这些专用工具"，但工具本身保持独立
- **物理世界的延伸**：不仅是软件工具——"什么样的工厂要建"、"什么类型的金融系统"——物理基础设施也适用这一逻辑
- **与 MCP 的关系**：Hassabis 的 Tool-Use Architecture 与 Anthropic MCP 协议在理念上高度一致——都是"通用 orchestrator + 标准化 tool connections"模式

## 前提与局限性

- 工具使用假设通用模型有足够智能来判断"何时调用哪个工具"——这个判断能力本身可能成为瓶颈
- 专用系统版本升级可能导致与 orchestrator 的兼容性问题
- 如果通用模型未来发展出更强的专业化能力而不损失通用性（逆 described tradeoff），这一架构可能被简化

## 关联概念

- [[Scientific-Discovery-AI]] — AlphaFold、材料模拟器等作为科学发现工具被 orchestrator 调用
- [[Agent-Orchestration]] — Agent 层面同样存在"编排 vs 单一大 Agent"的问题
- [[Cross-Disciplinary-Generalist]] — 人类组织层面存在相同模式：通才管理者 + 专家团队
