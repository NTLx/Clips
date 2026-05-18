---
type: entity
title: Accessibility-Agent
aliases:
  - Accessibility Agent
  - 无障碍 Agent
definition: "GitHub 正在试验的通用无障碍 Agent，通过两步子 Agent 架构（被动评审者 + 主动实现者）自动评审和修复前端代码中的可访问性问题，已评审 3535 个 PR，解决率 68%"
created: 2026-05-18
updated: 2026-05-18
tags:
  - AI-Agent
  - accessibility
  - GitHub
related_entities:
  - "[[WCAG]]"
  - "[[Sub-Agent-Architecture]]"
  - "[[Agentic-Engineering]]"
  - "[[Bias-to-Action-LLM]]"
  - "[[Social-Model-of-Disability]]"
  - "[[Accessibility-Complexity-Evaluation]]"
  - "[[Accessibility-High-Risk-Patterns]]"
  - "[[Template-Schema-Pattern]]"
  - "[[Agent-PR-Review]]"
source_raw:
  - "[[Building a general-purpose accessibility agent—and what we learned in the process]]"
---

# Accessibility-Agent

> [!definition] 定义
> **Accessibility Agent（无障碍 Agent）** 是 GitHub Copilot 团队正在试验的通用无障碍 Agent，有两个核心目标：为工程师提供即时可靠的无障碍问题解答（集成于 Copilot CLI 和 VS Code），以及自动捕获并修复进入生产环境前的简单客观无障碍问题。截至 2026 年 5 月，已评审 **3535 个 PR**，解决率 **68%**。

## 核心架构：评审者 + 实现者

不同于常见的"多子 Agent 并行执行"方案，Accessibility Agent 采用两个专用子 Agent **顺序执行**：

| 子 Agent | 角色 | 能力 |
|---------|------|------|
| **评审者（Reviewer）** | 被动评审 + 研究 | 只读，进行代码审计、WCAG 研究、检测升级触发器 |
| **实现者（Implementer）** | 主动修复 | 可读写，两种模式：默认代码变更模式 + 回退纯指导模式 |

工作流程：父 Agent → 评审者（结构化发现）→ 父 Agent 验证路由 → 实现者（变更/指导）→ 父 Agent

选择顺序执行而非并行执行的原因：
- **升级检查点**：评审者识别需要人工干预的区域
- **复杂度行为**：代码过于复杂时切换到纯指导模式
- **过滤**：评审者报告所有发现，父 Agent 决定哪些相关
- **可追溯性**：子 Agent 之间不直接通信，保留审计追踪

## 执行策略：线性阶段

Agent 强制执行**固定顺序的阶段**，每个阶段包含有序步骤：

1. **Phase 1 - Research**：查阅 WCAG 成功标准、组织内部解读、辅助技术支持、历史审计记录
2. **Phase 2 - Code Audit**：按需读取源文件、验证 URL、交叉对比发现
3. **Phase 3 - Structured Output**：生成标准化发现报告（含严重度评分：critical/warning/info）

线性执行比并行 Agent 更准确，因为无障碍工作本身需要方法论和细致态度。

## 关键数据点

- 评审 **3535 个 PR**，解决率 **68%**
- Top 5 问题类型：结构与关系不清晰、交互控件缺少名称、用户未感知重要通知、非文本内容缺替代文本、键盘焦点顺序不合理
- WCAG 2.2 级别 A 和 AA 共 55 个成功标准，仅 **35 个（64%）可通过自动代码检查器检测**，约 **36% 需人工评估**
- LLM 对无障碍反模式有偏差，因为所有主流 LLM 都训练于数十年不可访问的代码

## 前提与局限性

- **不是银弹**：Agent 不能自动解决所有无障碍场景，而是增强人工工程师的努力
- **LLM 反模式偏差**：训练数据中大量不可访问代码导致 LLM 倾向生成无障碍反模式
- **高质量历史数据是关键**：Agent 的强弱高度依赖组织积累的结构化无障碍问题库
- **复杂度限制**：通过脚本启发式评分判断是否应自动修改，高分代码需转人工
- **高风险模式排除**：拖放、Toast、富文本编辑器、树形视图、数据网格等模式禁止 Agent 自动修改
- **Token 消耗大**：无障碍是整体性和高度上下文的工作，Agent 可能消耗大量 Token

## 关联概念

- [[WCAG]] — Web Content Accessibility Guidelines，Agent 评审的核心标准
- [[Sub-Agent-Architecture]] — 评审者+实现者的两 Agent 顺序架构
- [[Agentic-Engineering]] — 更广泛的 Agent 工程实践
- [[Bias-to-Action-LLM]] — LLM 的"迫切生成内容"倾向，需反博弈指令约束
- [[Social-Model-of-Disability]] — 无障碍 Agent 的哲学基础
- [[Accessibility-Complexity-Evaluation]] — 代码复杂度评估决定 Agent 行为模式
- [[Accessibility-High-Risk-Patterns]] — 被排除在 Agent 自动化之外的高风险交互模式
- [[Template-Schema-Pattern]] — 子 Agent 间使用模板 Schema 传递信息
- [[Agent-PR-Review]] — Agent 自动评审 PR 的实践
