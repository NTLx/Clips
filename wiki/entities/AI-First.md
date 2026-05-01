---
type: entity
title: AI-First
aliases:
  - AI First
definition: "围绕'AI 是主要构建者'假设，重新设计流程、架构和组织的范式——不再问'AI 如何帮助人类'，而是问'如何重构一切，让 AI 负责构建，人类提供方向和判断'"
created: 2026-04-16
updated: 2026-04-16
tags:
  - AI-Agent
  - Organizational-Design
  - Development-Paradigm
related_entities:
  - "[[Harness-Engineering]]"
  - "[[Agentic-Engineering]]"
  - "[[Machine-Readable-Processes]]"
  - "[[Agent-First-Enterprise]]"
  - "[[Decision-Quality]]"
  - "[[Taste]]"
source_raw:
  - "[[20260413-why-ai-first-strategy-wrong]]"
---

# AI-First（AI 优先）

> [!definition] 定义
> **AI-First** 是围绕"AI 是主要构建者"这一假设，重新设计流程、架构和组织的工程与商业范式。核心区分：不再问"AI 如何帮助我们的工程师"，而是问"如何重构一切，让 AI 负责构建，工程师提供方向和判断"。

## AI-Assisted vs AI-First

| 维度 | AI-Assisted（AI 辅助） | AI-First（AI 优先） |
|------|----------------------|-------------------|
| **流程** | 保持现有流程不变 | 重新设计流程围绕 AI 构建 |
| **效率提升** | 10-20% | 量级级提升 |
| **人类角色** | 主要构建者，AI 辅助 | 提供方向和判断，AI 构建 |
| **工具集成** | 把 AI 加入循环 | 重新设计循环本身 |
| **典型表现** | 工程师用 Cursor，PM 用 ChatGPT | 6 阶段 CI/CD + 3 轮 AI 审查的自愈系统 |

## AI-First = 重新设计循环，而非加入循环

常见伪 AI-First 形态：
- 相同的 Sprint 周期 + 相同的 Jira 看板 + 相同的每周站会 + 相同的 QA 审批

真正 AI-First 的核心特征：
1. **Monorepo 统一架构** — 让 AI 能看到一切
2. **确定性 CI/CD 流水线** — 让 Agent 能预测结果、推断失败
3. **自愈反馈循环** — 错误被自动检测、分诊、修复、验证
4. **功能标志 + 熔断回滚** — 发布即实验，坏功能当天淘汰
5. **全职能 AI 原生** — 工程、产品、市场营销同速运转

## 实施代价

AI-First 不是免费午餐，真实成本包括：
- 员工不确定感
- CTO 每天工作 18 小时设计系统
- 高级工程师质疑自身价值
- 旧系统已去而新系统尚未经验证的煎熬期

竞争优势不在于技术栈（无专有技术），而在于**重新设计一切的决定**和**承受代价的意愿**。

## 关键原则

### 验证速度必须与实现速度匹配

```
构建时间: 2小时
测试时间: 3天  ❌ 瓶颈（旧 QA）
测试时间: 2小时  ✅ 匹配（AI 测试平台）
```

任何环节速度不匹配，就会成为整条流水线的制约。

### 从代码产出到决策质量

工程师价值从"快速写代码"转向"评估、批判和引导 AI"。产品感知（Taste）变得至关重要——能在用户开口前知道 UI 不对，能发现 Agent 遗漏的失败场景。

## 关键数据点

- AI-Assisted 效率提升 10-20%，AI-First 差距是量级上的
- CREAO 案例：25 人，10 工程师 → 14 天内每天 3-8 次生产部署
- 旧模式：两周可能零发布
- CTO 管理时间从 60% 降到 10% 以下
- 模型能力是驱动时钟：Opus 4.5 做不到 Opus 4.6 的事，下一代模型将进一步加速

## 前提与局限性

- **前提**：Agent 具备 Code Execution 和代码审查能力
- **前提**：统一的 monorepo 使 AI 能检查、验证、修改
- **局限**：基于 25 人小公司案例，大规模组织验证不足
- **局限**：转型期产生员工焦虑和团队不确定性
- **局限**：单人公司愿景（1 架构师 + Agent = 100 人工作）尚未大规模验证
- **风险**：对 AI 工具链（CloudWatch/Claude/GitHub Actions）高度依赖

## 关联概念

- [[Harness-Engineering]] - AI-First 的工程实现框架：让 Agent 能够有效工作的系统设计
- [[Agentic-Engineering]] - 使用 Coding Agents 辅助开发；AI-First 是其组织级进阶
- [[Machine-Readable-Processes]] - AI-First 的流程层：让流程可被 Agent 理解和执行
- [[Agent-First-Enterprise]] - 商业组织视角的 AI-First
- [[Decision-Quality]] - AI-First 时代人类的核心价值：从代码产出转向决策质量
- [[Taste]] - AI-First 时代人类的核心技能：在无限噪声中认出信号

## 来源

- [[20260413-why-ai-first-strategy-wrong]] - Peter Pang (CREAO CTO), 2026-04-13
