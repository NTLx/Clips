---
type: entity
title: Agent Workflow Patterns
definition: "构建 Agentic 系统的模式集合，从简单组合到自主 Agent 的渐进式架构"
created: 2026-04-10
updated: 2026-04-10
tags:
  - AI-Agent
  - architecture
  - patterns
related_entities:
  - "[[Coding-Agents]]"
  - "[[ACI-Agent-Computer-Interface]]"
source_raw:
  - "[[building-effective-agents]]"
---

# Agent Workflow Patterns（Agent 工作流模式）

> **核心理念**：从简单开始，只在需要时增加复杂性

## 定义

**Agent Workflow Patterns** 是 Anthropic 总结的构建 Agentic 系统的模式集合，从最简单的构建块到完全自主的 Agent。

## 架构层级

### 基础构建块：Augmented LLM

```
LLM + 检索 + 工具 + 记忆
```

基础能力：
- 生成搜索查询
- 选择合适工具
- 决定保留什么信息

---

## Workflow 模式

### 1. Prompt Chaining（提示链）

```
输入 → LLM → 输出 → LLM → 输出 → ...
        ↑             ↑
      步骤1         步骤2
```

**适用场景**：任务可清晰分解为固定子任务

**示例**：
- 生成营销文案 → 翻译成其他语言
- 写大纲 → 验证大纲 → 写文档

### 2. Routing（路由）

```
      输入
        ↓
    分类/路由
    ↙    ↘
专用处理A  专用处理B
```

**适用场景**：不同类别需要不同处理

**示例**：
- 客服：一般问题/退款/技术支持 → 不同流程
- 简单问题给 Haiku，难题给 Sonnet

### 3. Parallelization（并行化）

```
      输入
    ↙   ↘   ↘
  LLM1 LLM2 LLM3
    ↘   ↙   ↙
     聚合结果
```

**两种形式**：
- **Sectioning**：任务拆分为独立子任务
- **Voting**：同一任务多次运行取共识

**示例**：
- Guardrails：一个处理用户查询，一个检查安全
- 代码审查：多个 prompt 审查不同方面

### 4. Orchestrator-Workers（编排者-工作者）

```
      Orchestrator（编排者）
         ↓ 分解任务
    ↙    ↓    ↘
Worker1 Worker2 Worker3
    ↘    ↙    ↙
     合成结果
```

**适用场景**：无法预测子任务的复杂任务

**示例**：
- 编码：多文件修改，每个文件改动取决于任务
- 搜索：多源信息收集与分析

### 5. Evaluator-Optimizer（评估者-优化者）

```
Generator（生成者）
    ↓ 输出
Evaluator（评估者）
    ↓ 反馈
Generator ← 改进
    ↓ 循环
```

**适用场景**：
- 有清晰评估标准
- 迭代改进有可衡量价值
- 人类能提供有用反馈

**示例**：
- 文学翻译：捕捉细微差别
- 复杂搜索：多轮搜索分析

---

## 自主 Agent

```
用户指令 → Agent 规划执行 → 循环操作 → 检查点/结果
```

**适用场景**：
- 开放性问题，无法预测步数
- 无法硬编码固定路径
- 信任其决策能力

**关键设计**：
- 工具集和文档清晰
- 停止条件（如最大迭代次数）
- 沙箱测试 + 护栏

---

## 核心原则

> [!important] 三大原则
> 1. **简单性**：保持设计简单
> 2. **透明性**：明确展示 Agent 规划步骤
> 3. **精心设计 ACI**：通过文档和测试优化工具接口

## 选择指南

| 需求 | 推荐模式 |
|------|---------|
| 固定子任务 | Prompt Chaining |
| 不同类别处理 | Routing |
| 速度/多视角 | Parallelization |
| 动态子任务 | Orchestrator-Workers |
| 迭代改进 | Evaluator-Optimizer |
| 开放任务 | Autonomous Agent |

---

> **来源**：Anthropic, "Building Effective AI Agents", 2024-12-19