---
type: entity
title: Agentic Workflow Token Efficiency
aliases:
  - Agentic Workflow Token Efficiency
  - Token Efficiency
definition: "通过 API 代理记录、自动化审计、MCP 工具裁剪、CLI 替代等手段，系统性优化 Agentic Workflows 的 token 成本"
created: 2026-05-09
updated: 2026-05-09
tags:
  - Agentic-Engineering
  - cost-optimization
  - DevOps
related_entities:
  - "[[Agentic-Engineering]]"
  - "[[Agent-Workflow-Patterns]]"
  - "[[Agent-PR-Review]]"
source_raw:
  - "[[Improving token efficiency in GitHub Agentic Workflows]]"
---

# Agentic-Workflow-Token-Efficiency（Agentic Workflow Token 效率）

> [!definition] 定义
> **Agentic-Workflow-Token-Efficiency** 是通过 API 代理记录、自动化审计、MCP 工具裁剪、CLI 替代等手段，系统性优化 Agentic Workflows 的 token 成本的方法论。

## 核心问题

### 成本累积

- Agentic Workflows 自动调度和触发，成本可能在视野外累积
- 每个 MCP 工具调用都是一个推理步骤，消耗 token
- 未使用的工具注册也会占用上下文空间

### 效率悖论

- 工作负载变化（5 行修复 vs 200 行 PR）导致 token 使用波动
- 模型差异（Haiku vs Sonnet vs Opus）导致成本差异
- 质量影响难以直接测量

## 优化策略

### 1. API 代理记录

- 使用 API 代理捕获所有 token 使用数据
- 输出 `token-usage.jsonl` 文件，包含输入/输出/缓存读取/缓存写入 token
- 建立历史视图，识别优化机会

### 2. 自动化审计和优化

**Daily Token Usage Auditor**：
- 读取近期工作流运行的 token 使用数据
- 按工作流聚合消费
- 标记显著增加的工作流
- 发布结构化报告

**Daily Token Optimizer**：
- 分析标记的工作流源码和日志
- 创建 GitHub issue 描述具体低效问题
- 提出具体优化建议

### 3. 消除未使用的 MCP 工具

- MCP 工具函数名和 JSON Schema 每次请求都包含在上下文中
- 40 个工具的 MCP 服务器可增加 10-15 KB Schema
- 移除未使用工具可减少 8-12 KB 上下文

### 4. 用 GitHub CLI 替代 MCP 调用

**两种策略**：

1. **Pre-agentic 数据下载**：工作流开始前运行 `gh` 命令，写入工作区文件
2. **In-agent CLI 代理替换**：运行时通过轻量级 HTTP 代理路由 CLI 流量

**优势**：
- CLI 调用是确定性 HTTP 请求，无 LLM 参与
- 消除工具调用开销（工具 JSON Schema、参数块、响应）
- 利用 Agent 在 bash 脚本方面的训练

## 关键数据点

| 指标 | 数据 |
|------|------|
| 优化工作流数量 | 12 个生产工作流 |
| Auto-Triage Issues 优化效果 | -62% (109 次运行) |
| Daily Compiler Quality 优化效果 | -19% (12 次运行) |
| Community Attribution 优化效果 | -37% (8 次运行) |
| Security Guard 优化效果 | -43% |
| Smoke Claude 优化效果 | -59% |
| Auto-Triage 运行频率 | 6.8 次/天 (最高 15 次) |
| MCP 工具 Schema 大小 | 40 工具 = 10-15 KB |
| 移除未使用工具节省 | 8-12 KB 上下文 |

## 效率测量

### Effective Tokens (ET) 公式

```
ET = m × (1.0 × I + 0.1 × C + 4.0 × O)
```

其中：
- `m` = 模型成本乘数（Haiku = 0.25×, Sonnet = 1.0×, Opus = 5.0×）
- `I` = 新处理的输入 token
- `C` = 缓存读取 token（权重 0.1×）
- `O` = 输出 token（权重 4×）

### 三个混淆因素

1. **模型差异**：相同工作流在不同模型上 token 数相似但成本不同
2. **工作负载变化**：小 PR vs 大 PR 导致 token 使用波动
3. **质量影响**：轻量模型+受限工作流可能降低输出质量

### 质量信号

- 输出 token 每 LLM 调用
- 每次运行的轮次计数
- 工具调用完成率

## 初步结果

| 工作流 | 优化效果 | 运行频率 |
|--------|----------|----------|
| Auto-Triage Issues | -62% | 6.8 次/天 |
| Daily Compiler Quality | -19% | 1 次/天 |
| Community Attribution | -37% | 1 次/天 |
| Security Guard | -43% | 高频 |
| Smoke Claude | -59% | 高频 |

## 三个关键模式

### 1. 许多 Agent 轮次是确定性数据收集

- 移除不需要推理的读取操作（获取 issue 元数据、扫描标签）
- 相关性门控跳过不涉及安全敏感文件的 PR
- **最便宜的 LLM 调用是你不做的调用**

### 2. 未使用的工具携带成本高

- 一个工具在单次运行中被调用 342 次，尽管完全不必要
- 移除工具可显著减少 token 使用
- 但工具清单可能只是整体上下文的一小部分

### 3. 单个配置错误可导致失控循环

- 错误的 bash 模式配置导致 Agent 陷入 64 轮回退循环
- Agent 手动读取源代码重建编译器输出
- 一个配置修复消除循环

## 前提与局限性

- 基于 GitHub 自己的 Agentic Workflows 实践，可能不适用于所有框架
- ET 公式是近似值，不同提供商的定价差异可能未充分考虑
- 质量影响难以直接测量，依赖过程信号而非结果信号

## 关联概念

- [[Agentic-Engineering]] — Token 效率是 Agentic Engineering 实践的重要组成部分
- [[Agent-Workflow-Patterns]] — 工作流模式影响 token 使用效率
- [[Agent-PR-Review]] — PR 审查工作流是 token 优化的重要场景
