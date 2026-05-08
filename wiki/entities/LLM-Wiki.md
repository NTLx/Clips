---
type: entity
title: LLM Wiki
aliases:
  - LLM Wiki
  - LLM 知识库
definition: "用 LLM 将文档集合编译为结构化 Wiki 的知识管理范式——对固定数据进行多次重编译和重排列，每次产生新的洞察投影，人始终是最终理解者"
created: 2026-05-08
updated: 2026-05-08
tags:
  - knowledge-management
  - AI
  - wiki
related_entities:
  - "[[Knowledge-Compilation]]"
  - "[[Knowledge-Graph]]"
  - "[[Memex]]"
  - "[[Software-3.0]]"
  - "[[Andrej-Karpathy]]"
source_raw:
  - "[[Andrej Karpathy: From Vibe Coding to Agentic Engineering]]"
  - "[[20260413-llm-wiki]]"
---

# LLM Wiki

> [!definition] 定义
> **LLM Wiki** 是 Andrej Karpathy 描述的一种新型知识管理范式：用 LLM 对固定文档集合进行多次"重编译"（recompile）和"重排列"（reorder），每次产生新的信息投影（projection），让人从中获得洞察。这不同于传统的 RAG（检索增强生成）——它不是"查找+回答"，而是"重组+创造新结构"。

## 关键数据点

- **不是加速已有事物**：传统的代码加速了已有的信息处理，LLM Wiki 创造了此前不可能存在的东西——没有代码能在 LLM 之前完成"基于事实集合自动建 Wiki"这件事
- **Synthetic Data Generation 类比**：Karpathy 将 LLM Wiki 视为对固定数据的"合成数据生成"——不同的投影产生不同的理解
- **人与 LLM 的分工**：LLM 做信息的填充和重排（像 interns 填充细节），人做顶层分类、设计决策和最终理解
- **与 RAG 的区别**：RAG 是检索→回答的线性流程；LLM Wiki 是多轮编译→结构化→持续演化的循环
- **"Outsource thinking, not understanding"**：Karpathy 引用的一条推文——LLM Wiki 帮你思考，但不能替代你的理解

## 前提与局限性

- 需要高质量的源文档集合作为输入
- LLM 输出的重组结构需要人工验证和筛选——LLM 可能产生虚假关联
- 信息的"投影"质量依赖 prompt 设计和编译策略
- 不适用于需要实时更新的动态知识（更适合相对稳定的文档集合）

## 关联概念

- [[Knowledge-Compilation]] — LLM Wiki 的核心操作：编译
- [[Knowledge-Graph]] — LLM Wiki 的结构化表示
- [[Memex]] — Vannevar Bush 1945 年提出的信息关联愿景，LLM Wiki 是其 AI 增强版
- [[Software-3.0]] — LLM Wiki 是 Software 3.0 在知识管理中的应用
- [[RAG-vs-LLM-Wiki]] — 两种范式的对比
