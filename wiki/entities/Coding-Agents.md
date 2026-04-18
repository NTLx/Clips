---
type: entity
title: Coding Agents
aliases:
  - Coding Agents
definition: "能够自主完成编程任务的 AI Agent——理解需求、编写代码、运行测试、修复 bug、提交 PR，形成完整开发循环"
created: 2026-04-10
updated: 2026-04-16
tags:
  - AI-Agent
  - coding-tools
  - core-concept
related_entities:
  - "[[Agentic-Engineering]]"
  - "[[Code-Execution]]"
  - "[[Claude-Code-CLI]]"
  - "[[Vibe-Coding]]"
  - "[[Harness-Engineering]]"
  - "[[Decision-Quality]]"
source_raw:
  - "[[20260410-what-is-agentic-engineering]]"
  - "[[building-effective-agents]]"
  - "[[Why Your “AI-First” Strategy Is Probably Wrong]]"
---

# Coding Agents（编码智能体）

> [!definition] 定义
> **Coding Agents** 是能够自主完成编程任务的 AI Agent——理解需求、编写代码、运行测试、修复 bug、提交 PR，形成完整开发循环。与代码补全工具（如 Copilot）不同，Coding Agents 具有目标导向的自主性和多步骤的执行能力。

## Coding Agents vs 代码补全

区别不在于代码质量，而在于**控制流**：

| 维度 | 代码补全（Copilot） | Coding Agent |
|------|-------------------|-------------|
| 控制流 | 人主导，AI 辅助补全 | AI 主导循环，人监督审查 |
| 自主性 | 逐行补全 | 理解需求→规划→实现→验证→迭代 |
| 人类角色 | 作者 | 编辑（审阅和修改 Agent 草稿） |

## 核心要点

### 范式转换：从"人写代码"到"人定义任务"

自动编码的梦想从 1950 年代就开始了：代码生成器 → CASE 工具 → 低代码/无代码 → Copilot 补全 → Coding Agents。

关键拐点：
- **2022**: Copilot 证明了 LLM 能写出可用代码
- **2024-2025**: Claude Code、Devin 等证明了 Agent 能**自主完成多步骤任务**

### Coding Agent Loop

```
人类: "做什么"
  ↓
需求理解 → 步骤规划 → 代码实现（Agent 自主循环）→ 测试验证 → 人类审查（关键 checkpoint）→ 完成/迭代
```

人类只在关键 checkpoint 介入，**程序员从作者变为编辑**——你不再创作原文，你审阅和修改 Agent 的草稿。

### 能力边界

Coding Agent 擅长**边界清晰、可验证、有据可查**的任务。

**不适用场景**：
- 需要创造性探索的需求（"做一个有趣的数据可视化"）
- 涉及复杂遗留代码和隐性知识（"修复那个只在生产环境出现的偶发 bug"）

## 关键数据点

- 2022 Copilot 证明 LLM 能写可用代码；2024-2025 Claude Code、Devin 证明 Agent 能自主完成多步骤任务
- Coding Agent Loop = Understand → Plan → Implement → Verify → Iterate
- 范式隐喻：程序员从作者变为编辑——"I don't write code, I edit it"
- CREAO 案例：99% 生产代码由 AI 编写，14 天内每天 3-8 次部署（Peter Pang, 2026）

## 前提与局限性

- **前提**: Code Execution 是 Coding Agent 的决定性能力——无此能力则输出价值有限
- **前提**: 任务边界清晰、可验证、有据可查时效率最高
- **局限**: 创造性探索需求（无明确成功标准）效率急剧下降
- **局限**: 复杂遗留代码和隐性知识（无文档的生产 bug）处理能力不足
- **局限**: 人类审查质量直接决定产出质量——缺乏 Taste/Judgment 的审查者无法有效把关

## 关联概念

- [[Agentic-Engineering]] — Coding Agents 是 Agentic Engineering 的核心工具
- [[Code-Execution]] — Coding Agents 的决定性能力
- [[Claude-Code-CLI]] — Coding Agent 的具体实现
- [[Vibe-Coding]] — Coding Agent 产出的原型级代码 vs 生产级代码
- [[Harness-Engineering]] — Coding Agent 作为主要构建者时，需要完整的系统框架来保证稳定、可靠、安全
- [[Decision-Quality]] — Coding Agent 时代程序员的核心价值从代码产出转向决策质量

## 来源

- [[20260410-what-is-agentic-engineering]]
- [[building-effective-agents]]
- [[Why Your “AI-First” Strategy Is Probably Wrong]] — CREAO CTO Peter Pang: "99% 的生产代码由 AI 编写"
