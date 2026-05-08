---
type: entity
title: Dominator Analysis
aliases:
  - Dominator Analysis（支配者分析）
definition: "在控制流图/执行图中，节点 A 支配节点 B = 所有从起点到 B 的路径必经 A。用于从非确定性 Agent 执行中自动提取 essential states。"
created: 2026-05-07
updated: 2026-05-07
tags:
  - agent-validation
  - compiler-theory
  - graph-theory
related_entities:
  - '[[Agentic-Engineering]]'
  - '[[Ontology]]'
  - '[[Decision-Quality]]'
  - '[[Agent-Tenacity]]'
source_raw:
  - '[[Validating agentic behavior when “correct” isn’t deterministic]]'
---

> [!definition] 定义
> Dominator Analysis 是编译器优化中的经典技术，用于分析控制流图（CFG）中节点间的支配关系。Node A **dominates** node B 当且仅当从入口节点到 B 的每条路径都必须经过 A。将此技术应用于 Agentic 系统验证中，可以数学化地区分「essential states」（支配者节点，所有成功执行都必须经过）和「optional variations」（非支配者节点，如 loading spinner）。

## 关键数据点

- 编译器起源: 控制流图中的 dominator 概念是 compiler optimization 和 SSA（Static Single Assignment）形式的基础设施
- Agent 验证实验结果: GitHub Copilot Coding Agent VS Code 扩展测试中，Dominator Tree 方法达到 100% 准确率（F1=100%），Agent 自评仅 69.8% F1（+30.2 百分点）
- Agent 自评盲区: CUA（Computer-Use Agent）完全无法识别 "Not a Bug" 场景（F1=0%），Dominator-based Trust Layer 达到 52.2% F1
- 学习效率: 仅需 2-10 次成功执行 trace 即可构建 ground truth 模型，无需大规模训练数据
- 前置步骤: 将 Agent 执行建模为 Prefix Tree Acceptor (PTA)，节点 = 可观察状态（截图/代码快照），边 = 动作转换；通过三层次等价性检测（视觉哈希 → LLM 语义分析 → 保守合并）合并多 trace 为统一图

## 前提与局限性

- **前提条件**: 任务须有可定义的「essential states」（成功完成的逻辑必经节点）。Open-ended 探索型任务（如"研究 X 主题"）可能没有明确的支配者节点
- **LLM 依赖**: 三层次等价性检测中的语义判断依赖多模态 LLM，引入外部 API 依赖和延迟——本质是一个非确定性组件验证另一个非确定性系统
- **需正样本**: 算法从成功案例中学习，无法仅从失败日志推导正确性定义
- **时间盲点**: 当前实现只验证事件发生顺序（topological subsequence matching），无法检测某个状态的持续时间是否合理（如 loading 超过 5 秒）
- **State space 覆盖**: 2-10 次 trace 可能覆盖不全复杂环境中的全部 valid variation paths，需要在线学习机制持续改进

## 关联概念

- [[Agentic-Engineering|Agentic Engineering]] — Dominator Analysis 是 Agentic Engineering 从 demo 走向 production 的测试验证关键方法论
- [[Ontology|Ontology]] — 结构类比: TBox 提取概念规则骨架 vs ABox 承载实例变异，类似 dominator skeleton vs optional noise 的分离
- [[Decision-Quality|Decision Quality]] — Essential states 的概念与决策质量中「基于清晰而非路径细节」的原则一致
- [[Agent-Tenacity|Agent Tenacity]] — 测试非确定性 Agent 行为时，tenacity（持续重试）与验证框架需协同设计，避免 agent 的 adaptive retry 被误判为失败
