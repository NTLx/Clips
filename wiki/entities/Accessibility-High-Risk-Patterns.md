---
type: entity
title: Accessibility-High-Risk-Patterns
aliases:
  - Accessibility High Risk Patterns
  - 无障碍高风险模式
definition: "被无障碍 Agent 禁止自动修改的交互模式——拖放、Toast、富文本编辑器、树形视图、数据网格等，这些模式即使通过自动检测，实际使用中仍可能无法被辅助技术正常使用"
created: 2026-05-18
updated: 2026-05-18
tags:
  - accessibility
  - AI-Agent
  - anti-patterns
related_entities:
  - "[[Accessibility-Agent]]"
  - "[[Accessibility-Complexity-Evaluation]]"
source_raw:
  - "[[Building a general-purpose accessibility agent—and what we learned in the process]]"
---

# Accessibility-High-Risk-Patterns

> [!definition] 定义
> **无障碍高风险模式** 是那些即使通过自动化无障碍检测，实际使用中仍可能无法被辅助技术正常使用的交互模式。GitHub 的无障碍 Agent 被明确禁止为这些模式生成代码，包括：拖放（drag and drop）、Toast 通知、富文本编辑器（rich text editors）、树形视图（tree views）和数据网格（data grids）。

## 已知高风险模式清单

| 模式 | 风险原因 |
|------|---------|
| 拖放 | 需要同时支持鼠标、键盘和触摸操作，状态反馈复杂 |
| Toast 通知 | 需要在不干扰当前任务的前提下让用户感知重要通知 |
| 富文本编辑器 | 涉及复杂的键盘快捷键和屏幕阅读器交互 |
| 树形视图 | 层级展开/折叠与屏幕阅读器阅读顺序的协调困难 |
| 数据网格 | 大量单元格需要支持排序、选择和键盘导航 |

## 为什么代码检测通过但实际不可用

一个微妙但关键的认识：**代码通过自动无障碍检测 ≠ 功能上可用**。自动检测器验证的是代码层面的合规性（如 ARIA 属性是否存在），但无法验证实际辅助技术使用体验。

## 关键数据点

- 这些模式需要大量专注和细致工作，当前超出 LLM 的生成能力
- 禁止 Agent 碰高风险模式避免了不必要的时间浪费和可访问性团队声誉风险

## 前提与局限性

- 清单基于当前（2026 年）无障碍团队的经验判断，会随着技术进步和 LLM 能力提升而变化
- "高风险"判断本身依赖人工经验，Agent 自己无法可靠判断某个模式是否高风险
- 不在清单上的模式不自动等于"安全"——清单是已知的，不是全部的

## 关联概念

- [[Accessibility-Agent]] — 高风险模式是无障碍 Agent 的核心约束条件
- [[Accessibility-Complexity-Evaluation]] — 与复杂度评估配合，形成两层保护
