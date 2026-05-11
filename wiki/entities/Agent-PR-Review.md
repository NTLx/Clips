---
type: entity
title: Agent PR Review
aliases:
  - Agent PR Review
  - Agent Pull Request Review
definition: "审查 Agent 生成的 Pull Request 的系统性策略——关注 CI 游戏化、代码重用盲点、幻觉正确性、Agent 幽灵、工作流安全等 5 个关键检查点"
created: 2026-05-09
updated: 2026-05-11
tags:
  - Agentic-Engineering
  - code-review
  - DevOps
related_entities:
  - "[[Agentic-Engineering]]"
  - "[[Agent-Workflow-Patterns]]"
  - "[[AI-Ready-Organization]]"
  - "[[Agent-Generated-PRs]]"
source_raw:
  - "[[Agent pull requests are everywhere. Here's how to review them.]]"
  - "[[The PR you would have opened yourself]]"
---

# Agent-PR-Review（Agent PR 审查）

> [!definition] 定义
> **Agent-PR-Review** 是审查 Agent 生成的 Pull Request 的系统性策略。核心观点：Agent PR 的表面看起来干净，但隐藏着更多技术债务，审查者需要不同的检查清单。

## 核心问题

### 带宽饱和

- GitHub Copilot 已处理超过 6000 万次审查
- 超过 1/5 的代码审查涉及 Agent
- 一个开发者可以在午餐前启动十几个 Agent 会话
- 人类审查能力跟不上指数级增长

### 质量悖论

- Agent 代码引入更多冗余和技术债务
- 但审查者对 Agent 代码感觉更好（更容易批准）
- "看起来干净"的失败模式是危险的

## 5 个关键检查点

### 1. CI 游戏化 (CI Gaming)

Agent 可能通过以下方式规避 CI：
- 删除测试
- 跳过 lint 步骤
- 添加 `|| true` 到测试命令
- 降低覆盖率阈值

**检查清单**：
- 覆盖率阈值是否改变？
- 测试是否被删除、重命名或标记为跳过？
- 工作流是否停止在 fork 或 PR 上运行？
- CI 步骤是否新增了条件门控？

### 2. 代码重用盲点 (Code Reuse Blindness)

Agent 的本地上下文不包含仓库全貌，可能重复实现已有功能：
- 新工具函数重复现有功能
- 验证逻辑在多处重新实现
- 中间件从头编写，实际已有共享模块

**检查清单**：
- 对每个新工具/辅助函数进行仓库搜索
- 发现重复则要求合并，不留评论
- 要求为新增工具提供理由

### 3. 幻觉正确性 (Hallucinated Correctness)

明显的幻觉（调用不存在的 API）会被 CI 捕获，危险的是更微妙的：
- 分页中的 off-by-one 错误
- 测试未覆盖的分支缺少权限检查
- 边界条件下的验证短路
- 仅在规模下显现的竞态条件

**检查清单**：
- 追踪关键路径：输入 → 转换 → 输出
- 检查边界条件（零、最大值、空值）
- 要求新测试在变更前行为上失败

### 4. Agent 幽灵 (Agentic Ghosting)

Agent PR 可能对审查反馈无响应或循环跑题：
- 大型 PR 无结构化计划
- Agent 对审查意见无响应
- 投入多轮审查仍无进展

**检查清单**：
- 检查 PR 历史响应性
- 要求实现计划再进行深度审查
- 拆分大型 PR 为更小范围的单元

### 5. 工作流中的不可信输入 (Untrusted Input in Workflows)

CI Agent 中的提示注入是真实且被低估的：
- PR body、issue body、commit message 被插入提示
- 模型输出被管道传输到 shell 命令
- 整个流程以 `GITHUB_TOKEN` 权限运行

**检查清单**：
- 不可信输入是否未经清理就插入提示？
- `GITHUB_TOKEN` 是否在只需要读权限时使用了写权限？
- 模型输出是否未经验证就作为 shell 命令执行？
- Agent 步骤是否可访问 secret 或打印到日志？

## 10 分钟审查流程

| 时间 | 步骤 | 内容 |
|------|------|------|
| 1-2 min | 扫描分类 | 文件列表和 diff 大小，判断简单/复杂 |
| 2-3 min | 检查 CI 变更 | 先看 .github/workflows、测试配置、覆盖率设置 |
| 3-5 min | 扫描新工具 | 搜索新函数/辅助模块，检查重复 |
| 5-8 min | 追踪关键路径 | 选择最重要的逻辑变更，端到端追踪 |
| 8-9 min | 安全边界 | 如果涉及 LLM 调用或不可信输入，运行安全检查 |
| 9-10 min | 要求证据 | 非平凡逻辑变更要求测试，高风险变更要求回滚计划 |

## 何时要求拆分 PR

1. diff 触及超过 5 个不相关文件
2. 无法用一句话描述 PR 目的
3. Agent 无实现计划或 PR body 为空
4. CI 失败且 diff 中只有测试文件变更

## 关键数据点

- GitHub Copilot 代码审查已处理超过 6000 万次审查
- 超过 1/5 的代码审查涉及 Agent
- 2026 年 1 月研究 "More Code, Less Reuse" 发现 Agent 代码引入更多冗余

## 前提与局限性

- 基于 2026 年初的 Agent 能力，质量可能随模型迭代快速改善
- 10 分钟审查流程适用于中等复杂度 PR，大型重构可能需要更多时间
- 检查清单可能过于繁琐，需要根据团队实际情况调整

## 正面策略：Skills + Test Harness

与上述防御性审查互补，HuggingFace (2026) 展示了**主动提升 Agent PR 质量**的方法：

- **Skills（Agent 配方）**: 文本文件形式的领域知识编码，包含技术规则（RoPE 验证、dtype 检测）和文化规则（不解释代码、不提议重构）
- **Test Harness**: 独立于 Agent 的非 LLM 测试套件，消除幻觉结果不确定性，保证可复现性
- **Signal 丰富度**: Agent 辅助 PR 应比中位数人工 PR 提供更多数据（生成示例、数值比较、逐层对比）

> 核心洞察："The bottleneck in open source is not typing speed: it's understanding the codebase to change it without breaking the implicit and explicit contracts with users."

## 关联概念

- [[Agentic-Engineering]] — Agent PR 审查是 Agentic Engineering 实践的一部分
- [[Agent-Workflow-Patterns]] — Agent 工作流模式影响 PR 生成方式
- [[AI-Ready-Organization]] — AI 就绪组织需要建立 Agent PR 审查流程
