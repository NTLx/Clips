---
type: topic
title: Building Effective Agents
description: "Anthropic 的 Agent 构建指南：从简单模式到自主 Agent 的架构设计"
created: 2026-04-10
updated: 2026-04-10
tags:
  - AI-Agent
  - architecture
  - best-practices
related_entities:
  - "[[Agent-Workflow-Patterns]]"
  - "[[ACI-Agent-Computer-Interface]]"
  - "[[Coding-Agents]]"
source_raw:
  - "[[building-effective-agents]]"
---

# Building Effective Agents

> **来源**：Anthropic, "Building Effective AI Agents" (2024-12-19)
> **作者**：Erik Schluntz, Barry Zhang

## 核心原则

> [!important] 关键洞察
> 成功的实现使用**简单、可组合的模式**，而非复杂框架。

### 三大原则

1. **Simplicity** - 保持设计简单
2. **Transparency** - 明确展示规划步骤
3. **Well-crafted ACI** - 精心设计 Agent-Computer Interface

---

## 架构定义

### Workflows vs Agents

| 类型 | 定义 |
|------|------|
| **Workflows** | LLM 和工具通过预定义代码路径编排 |
| **Agents** | LLM 动态指导自己的过程和工具使用 |

---

## 何时使用 Agent

### 不需要 Agent

- 单次 LLM 调用 + 检索 + 示例足够
- 可预测的任务
- 对延迟/成本敏感

### 需要 Workflow

- 任务可清晰分解
- 需要一致性和可预测性
- 有明确的评估标准

### 需要 Agent

- 开放性问题
- 无法预测步数
- 需要灵活决策

---

## Workflow Patterns 详解

### 1. Prompt Chaining

**适用**：任务可分解为固定子任务

```
步骤1 → 步骤2 → 步骤3 → 输出
```

### 2. Routing

**适用**：不同类别需要不同处理

```
分类 → 路由到专门处理流程
```

### 3. Parallelization

**适用**：速度优化、多视角验证

```
并行执行 → 聚合结果
```

### 4. Orchestrator-Workers

**适用**：动态子任务分解

```
Orchestrator 分解 → Workers 执行 → 合成结果
```

### 5. Evaluator-Optimizer

**适用**：迭代改进有价值

```
生成 → 评估 → 反馈 → 改进 → 循环
```

---

## ACI 设计

### 核心类比

> 在 HCI 上投入多少努力，就在 ACI 上投入多少。

### 设计检查清单

1. **模型视角** - 使用方式是否明显？
2. **命名清晰** - 参数名是否让事情更明显？
3. **测试迭代** - 在 workbench 测试错误模式
4. **Poka-yoke** - 防错设计

### 格式选择

| 格式 | Agent 难度 |
|------|-----------|
| Markdown 代码块 | 低 |
| 整个文件重写 | 低 |
| Diff 格式 | 高（需计算行号） |
| JSON 内嵌代码 | 高（需转义） |

---

## 框架使用建议

### 推荐框架

- Claude Agent SDK
- Strands Agents SDK (AWS)
- Rivet (GUI workflow builder)
- Vellum (GUI workflow tool)

### 注意事项

> [!warning] 框架陷阱
> 框架增加抽象层，可能掩盖底层 prompt/response。
> 
> **建议**：
> 1. 先用 LLM API 直接实现简单模式
> 2. 使用框架时理解底层代码
> 3. 不要因框架添加不必要复杂性

---

## Agent 应用场景

### 客户支持

- 自然对话 + 工具集成
- 成功可清晰衡量
- 人类监督机制

### 编码 Agent

- 代码可通过测试验证
- Agent 可用测试结果迭代
- 问题空间结构化

---

## 相关主题

- [[Agent-Workflow-Patterns]] - 详细模式说明
- [[Agentic-Engineering-Patterns]] - Simon Willison 的工程视角
- [[ACI-Agent-Computer-Interface]] - 接口设计详解

---

> **来源**：Anthropic, "Building Effective AI Agents", 2024-12-19