---
type: entity
title: YAGNI
aliases:
  - YAGNI
  - You Aren't Gonna Need It
  - 你不需要它
definition: "敏捷软件开发原则：不要实现当前未需要的功能。避免过度设计，只实现明确需求。"
created: 2026-04-21
updated: 2026-04-21
tags:
  - agile
  - software-engineering
  - design-principle
related_entities:
  - "[[Laziness-Virtue]]"
  - "[[Martin-Fowler]]"
  - "[[Agentic-Engineering]]"
source_raw:
  - "20260414-martin-fowler-fragments"
---

# YAGNI

> [!definition] 定义
> 敏捷软件开发原则：不要实现当前未需要的功能。

## 起源

- **提出者**: Ron Jeffries (Extreme Programming)
- **推广者**: Martin Fowler (bliki 文章)
- **核心原则**: "You aren't gonna need it" — 不要为未来需求提前实现功能

## 关键数据点

- **起源**: Extreme Programming (XP) 实践
- **推广**: Martin Fowler 在 martinfowler.com/bliki/Yagni.html 详细阐述
- **AI 应用**: Martin Fowler (2026) 用 YAGNI 简化 playlist generator，避免过度复杂化

## 前提与局限性

- **前提**: 
  1. 未来需求不可预测
  2. 未实现的功能不产生维护成本
  3. 实现后可能发现不需要
- **局限性**: 
  1. 需要判断"当前需要"的边界
  2. 某些基础设施提前设计有益

## 关联概念

- [[Laziness-Virtue]] — YAGNI 是懒惰美德的具体实践
- [[Martin-Fowler]] — 推广者，2026 年文章中再次强调
- [[Agentic-Engineering]] — AI 编程需要 YAGNI 约束

## Martin Fowler 的个人体验 (2026)

Fowler 描述修改 playlist generator 的经历：
- 开始添加新功能 → 发现复杂度增加 → 气馁
- 想起 YAGNI → 删除未需要的部分 → 简化为 24 行代码
- 反思：如果用 LLM，是否会过度复杂化？是否会 LGTM 接受？

> "If I had used an LLM for this, it may well have done the task much more quickly, but would it have made a similar over-complication?"