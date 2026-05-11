---
type: entity
title: Dual-Tier LLM Architecture
aliases:
  - 双层 LLM 架构
  - 分层模型路由
definition: "一种 LLM 系统架构模式，根据查询复杂度将请求路由到不同规模的模型——简单任务用小模型保证速度，复杂任务用大模型保证质量。"
created: 2026-05-10
updated: 2026-05-11
tags:
  - AI-Architecture
  - Multi-Agent
  - Model-Routing
related_entities:
  - "[[Agent-Orchestration]]"
  - "[[Agentic-Engineering]]"
  - "[[Corrective-RAG]]"
source_raw:
  - "[[OncoAgent A Dual-Tier Multi-Agent Framework for Privacy-Preserving Oncology Clinical Decision Support]]"
  - "[[MachinaCheck Building a Multi-Agent CNC Manufacturability System on AMD MI300X]]"
---

> [!definition] 定义
> 双层 LLM 架构是一种模型路由模式：通过加权复杂度评分器（如肿瘤类型、分期、突变数量等因子）量化查询复杂度，低于阈值的路由到速度优化的小模型（如 9B），高于阈值的路由到深度推理的大模型（如 27B），实现速度与质量的最优平衡。

## 关键数据点

- **复杂度评分公式**: `S = w_cancer + w_stage + w_mutations + w_treatment`
- **决策边界**: S >= 0.5 → Tier 2（27B 深度推理）；S < 0.5 → Tier 1（9B 速度分诊）
- **OncoAgent 实例**: 罕见癌 +0.40、未知原发 +0.30、IV 期 +0.25、>=2 突变 +0.30、既往治疗 +0.10
- **验证案例**: IV 期胰腺癌 + KRAS + BRCA2 突变 → S = 0.80，正确路由到 Tier 2
- **人工覆盖**: 临床医生可通过 UI 手动覆盖层级选择
- **模型选择**: Tier 1 = Qwen 3.5-9B，Tier 2 = Qwen 3.6-27B

## 前提与局限性

- **前提**: 需要明确定义的复杂度因子和权重，这依赖领域专家知识
- **前提**: 需要两个不同规模的模型，且都需要经过领域微调
- **局限性**: 加权评分是线性的，可能无法捕捉因子间的非线性交互
- **局限性**: 阈值和权重需要根据实际效果持续调优

## 关联概念

- [[Agent-Orchestration]] — 双层路由是 Agent 编排中的请求分发模式
- [[Agentic-Engineering]] — 分层架构是 Agentic 工程中优化资源利用的关键策略
- [[Corrective-RAG]] — CRAG 为两个层级的模型提供质量可控的上下文
