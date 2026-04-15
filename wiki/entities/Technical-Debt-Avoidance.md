---
type: entity
title: Technical Debt Avoidance
definition: "通过持续改进和高质量实践避免技术债务累积的策略"
created: 2026-04-13
updated: 2026-04-15
tags:
  - AI-Agent
  - best-practices
  - coding-agents
related_entities:
  - "[[Compound-Engineering]]"
  - "[[Agentic-Engineering]]"
source_raw:
  - "[[20260410-better-code]]"
---

# Technical Debt Avoidance（技术债务避免）

> **核心理念**：AI 编程助手让我们终于可以兼顾新功能与高质量

## 定义

**Technical Debt Avoidance** 是在 AI 辅助开发时代变得更容易实现的实践：通过 Compound Engineering 持续改进指令和工具配置，避免技术债务累积。

## AI 时代的变化

> [!tip] 关键洞察
> 小改进会复合。曾经耗时的质量增强现在成本已降至没有借口不投资质量。
> 
> **编码助手意味着我们终于可以两者兼得**：新功能 + 高质量。

## 传统困境

| 维度 | 传统开发 | AI 辅助开发 |
|------|---------|------------|
| 速度 vs 质量 | 需权衡 | 可同时实现 |
| 技术债务 | 容易累积 | 每次迭代可清理 |
| 代码审查 | 事后补救 | Agent 自动验证 |

## Compound Engineering 的贡献

```
每个 PR 后 → 记录有效提示 → 更新指令 → 未来自动应用高质量标准
```

### 防止债务累积的方式

1. **持续改进** - 每个项目后记录有效做法
2. **标准化** - 成功模式变为可复用模板
3. **自动验证** - Agent 配置测试护栏

## 关联概念

- [[Compound-Engineering]] - 实现技术债务避免的核心方法
- [[Agentic-Engineering]] - 基础工程范式
- [[ACI-Agent-Computer-Interface]] - 工具接口设计影响代码质量

## 关键数据点

- 常见技术债务类别：API 设计未覆盖新场景、命名选择不佳、重复功能需要合并、单文件增长到数千行
- 所有这些变更概念上简单，但需要投入时间，考虑到更紧迫的问题很难证明其合理性
- 编码助手将代码改进成本降至可以对轻微代码异味采取零容忍态度
- 最好的技术债务缓解措施是一开始就不承担它

## 前提与局限性

- 依赖前提：编码助手能够理解重构意图并正确执行
- 适用边界：适用于概念简单但耗时的重构任务
- 局限性：大规模重构的正确性需要人类验证
- 异步助手适合后台重构（如 Gemini Jules、OpenAI Codex web、Claude Code on the web）
- 风险评估：AI 做的重构需要通过 PR 评估，好的合并、接近的提示改进、不好的丢弃

---
> **关联**：Simon Willison 的 Agentic Engineering Patterns 隐含此概念