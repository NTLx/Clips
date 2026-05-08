---
type: entity
title: Scientific Discovery AI
aliases:
  - Scientific Discovery AI
  - 科学发现 AI
definition: "Demis Hassabis 定义的 AI 科学发现通用模式：巨大组合搜索空间 + 明确目标函数 + 足够数据/模拟器 → 找到 needle in a haystack 式的突破方案"
created: 2026-05-08
updated: 2026-05-08
tags:
  - AI
  - science
  - deepmind
related_entities:
  - "[[Demis-Hassabis]]"
  - "[[Einstein-Test]]"
  - "[[Continual-Learning]]"
source_raw:
  - "[[Demis Hassabis: Agents, AGI & The Next Big Scientific Breakthrough]]"
---

# Scientific Discovery AI

> [!definition] 定义
> **Scientific Discovery AI** 是 Demis Hassabis 基于 AlphaGo 和 AlphaFold 的成功总结出的 AI 科学发现通用模式。三个条件：(1) 问题可以描述为巨大的组合搜索空间（越大越好——没有任何暴力算法能解决），(2) 有清晰的目标函数可以 hill climb，(3) 有足够数据或能在分布内生成合成数据的模拟器。满足这三点，今天的 AI 方法就能走很远。

## 关键数据点

- **AlphaFold 影响力**：300 万+ 研究人员全球使用，"几乎所有新药发现都将使用 AlphaFold 的某个环节"
- **Root Node 策略**：优先攻克"解锁整个知识领域"的根本性问题（蛋白质折叠、药物分子设计），形成连锁反应
- **AlphaGo 到 AlphaFold 的过渡**：Move 37 让 Hassabis 确信"这些系统能找到 needle in a haystack"，当天他就启动了 AlphaFold
- **药物发现即搜索问题**："存在一种化合物能治愈疾病，只要物理学允许它存在——问题只是如何高效找到它"
- **虚拟细胞路线图**：约 10 年，突破口可能是硬件（无需杀死细胞的活体纳米成像→把生物学变成计算机视觉问题）或软件（学习到的动力学模拟器）

## 前提与局限性

- 清晰目标函数在某些科学领域很难定义（如"什么是好的新数学猜想"）
- 数据获取是瓶颈——活细胞实时成像目前不可能
- 当前系统在"真正原创"上仍然不够——可以解题（"只是解决黎曼猜想"），但难以提出同等重要的新猜想

## 关联概念

- [[Einstein-Test]] — 检验真正科学创造力的标准
- [[Continual-Learning]] — 持续学习将允许多个科学发现累积而非互相覆盖
- [[Tool-Use-Architecture]] — 专门化的科学 AI（如 AlphaFold）vs 通用模型的工具使用
