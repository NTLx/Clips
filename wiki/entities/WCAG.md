---
type: entity
title: WCAG
aliases:
  - WCAG
  - Web Content Accessibility Guidelines
  - Web 内容无障碍指南
definition: "W3C 制定的 Web 内容无障碍指南，包含 55 个级别 A 和 AA 成功标准，其中仅 64% 可通过自动代码检查器检测，约 36% 需人工评估"
created: 2026-05-18
updated: 2026-05-18
tags:
  - accessibility
  - standard
  - W3C
related_entities:
  - "[[Accessibility-Agent]]"
  - "[[Accessibility-High-Risk-Patterns]]"
source_raw:
  - "[[Building a general-purpose accessibility agent—and what we learned in the process]]"
---

# WCAG

> [!definition] 定义
> **WCAG（Web Content Accessibility Guidelines，Web 内容无障碍指南）** 是 W3C 制定的 Web 内容无障碍标准。当前版本 WCAG 2.2 包含 55 个级别 A 和 AA 成功标准，其中仅 35 个（64%）可通过自动代码检查器检测，约 36% 需要人工评估。

## 自动化检测的边界

| 类型 | 数量 | 比例 |
|------|------|------|
| 可自动检测 | 35 个 | 64% |
| 需人工评估 | ~20 个 | ~36% |

LLM Agent 正在缩小这 36% 的差距，但这不是完美科学。

## 法规驱动

- **欧洲无障碍法案（EAA）**：已生效，要求数字产品符合 WCAG 标准
- **美国 ADA 第二章**：2027 年 4 月起，将 WCAG 2.1 AA 确立为法律意义上的"完成标准"

组织如果尚未投入无障碍问题识别和修复，将在未来处于劣势。

## 关键数据点

- WCAG 2.2 级别 A + AA 共 **55 个成功标准**
- 仅 **64% 可自动检测**，36% 需人工判断
- 欧洲 EAA 已生效，美国 ADA 2027 年 4 月生效

## 前提与局限性

- WCAG 是最低标准而非目标——合规不代表可用，不合规一定不可用
- 自动检测器只能验证代码层面的合规性，无法验证实际辅助技术使用体验
- 不同国家和地区对 WCAG 版本的法律引用不同（2.0/2.1/2.2），需注意适用版本

## 关联概念

- [[Accessibility-Agent]] — 无障碍 Agent 以 WCAG 成功标准为核心评审依据
- [[Accessibility-High-Risk-Patterns]] — 即使 WCAG 检测通过，某些交互模式仍可能实际不可用
