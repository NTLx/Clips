---
type: topic
title: OpenClaw Agent System
created: 2026-04-09
updated: 2026-04-14
tags:
  - OpenClaw
  - AI-Agent
  - Multi-Agent-System
related_entities:
  - "[[Agent-Orchestration]]"
  - "[[Agent-Swarm]]"
  - "[[Context-Engineering]]"
  - "[[Elvis-Sun]]"
  - "[[Multi-Layer-Memory]]"
  - "[[Three-State-Protocol]]"
source_raw:
  - "[[OpenClaw + CodexClaudeCode Agent Swarm The One-Person Dev Team Full Setup]]"
---

# OpenClaw Agent System

> [!summary] 概要
> OpenClaw Agent System 是一个完整的多 Agent 协作系统，包含编排层、上下文工程、五层记忆、Agent Swarm 和通信协议等核心组件，实现了从"聊天"到"干活"的工程化转变，让 Agent 能够自主进化、稳定运行、协作不打架。

## 系统架构总览

```
┌─────────────────────────────────────────────────────────────┐
│                 OpenClaw Agent System                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  第一层：编排层（Agent Orchestration）                       │
│  ├── Zoe（首席编排者）                                       │
│  │   └── 技术设计 / 任务编排 / 系统运维                       │
│  └── 5 个专业 Agent                                          │
│      └── ainews / Trading / Macro / Content / Butler        │
│                                                             │
│  第二层：上下文工程（Context Engineering）                    │
│  ├── SOUL.md（身份 + 硬约束）                                │
│  ├── AGENTS.md（操作规范）                                   │
│  ├── Skills（按需加载）                                      │
│  └── Harness（自动管理）                                     │
│                                                             │
│  第三层：记忆系统（Multi-Layer Memory）                       │
│  ├── L1 身份层（SOUL.md）                                    │
│  ├── L2 长期记忆（MEMORY.md）                                │
│  ├── L3 中期记忆（memory/）                                  │
│  ├── L4 短期记忆（.learnings/）                              │
│  └── L5 持久化（Skills + Obsidian）                          │
│                                                             │
│  第四层：Agent Swarm（编码层）                                │
│  ├── 6 种编码 Agent                                          │
│  │   └── Claude Code / Codex / Gemini / ...                 │
│  ├── Worktree + tmux 独立环境                                │
│  └── Cron 监控 + 自动 respawn                                │
│                                                             │
│  第五层：通信协议（Three-State Protocol）                     │
│  ├── request → confirmed → final                             │
│  ├── shared-context/ 状态驱动                                │
│  └── DRI 原则                                                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## 1+5+6 阵型

### Zoe（首席编排者）

不只是"管理员"，负责：
- **技术方案设计**：三态协议、Task Watcher、通信 Guardrail 都是 Zoe 自主设计
- **任务编排**：指派 ainews 调研，委派 ACP 编码专家实现
- **系统运维**：每天 3 次巡检（10:00/14:00/22:00），检查 cron、磁盘、session
- **记忆维护**：每周分析 MEMORY.md，执行分层压缩

### 5 个专业 Agent

| Agent | 角色 | 核心能力 |
|-------|------|---------|
| **ainews** | AI 哨兵 | 100+ 信息源采集 → 5 星评估 → 晨午晚三报 |
| **Trading** | 交易蜘蛛 | 21 cron 任务、四步分析框架、65/35 混合评分 |
| **Macro** | 首席经济学家 | 宏观→传导→国内→市场四层映射 |
| **Content** | 内容蜘蛛 | 54 平台热榜 + X 五篮子热点雷达 |
| **Butler** | 管家蜘蛛 | Apple 生态集成、早安晚安、喝水提醒 |

### 6 个编码专家

通过 ACP 协议按需委派，最大 6 并发，120min TTL：
- Claude Code / Codex / Gemini / Pi / OpenCode / GPT-5.3-Codex

**设计教训**：不要让分析 Agent 直接编码。分析 Agent 不写代码，编码全部通过 ACP 委派。

## 核心工程问题与解决方案

### 问题一：上下文是 Agent 的操作系统

参见 [[Context-Engineering]]

**Agent 系统的热力学第二定律**：不加约束，entropy 只增不减。

解决方案：
- **Context Engineering**：设计信息结构（SOUL.md → AGENTS.md → Skills 按需加载）
- **Harness 自动管理**：compaction、contextPruning、session reset、maintenance

### 问题二：Agent 今天犯的错，明天还会犯

参见 [[Multi-Layer-Memory]]

**五层记忆系统**实现跨会话的知识沉淀：

```
触发事件 → .learnings/ 即时记录 → 每日反思 cron →
≥3 次 promote 到 MEMORY.md → 下次 Session 加载 → 行为改进
```

### 问题三：协作是协议问题，不是群聊问题

参见 [[Three-State-Protocol]]

**三态通信协议**防止 ACK storm：

```
[request] → [confirmed] → [final → 静默]
```

+ V1 线程协议 + DRI 原则 + shared-context/ 状态驱动

## 一天是怎么过的

52 个 cron 任务覆盖 A 股 + 美股双时区：

| 时间 | 任务 |
|-----|------|
| 03:00 | 自动备份 |
| 05:20 | 美股收盘报告（次日） |
| 07:50 | Macro 晨报 |
| 08:00 | Butler 早安问候 |
| 08:30 | ainews 晨报 + Butler 日程规划 |
| 10:00 | Zoe 第一轮巡检 |
| 12:00 | ainews 午间论文解读 |
| 14:00 | Content 初稿产出 |
| 20:00 | ainews 晚间趋势分析 + Butler 健康检查 |
| 22:00 | Butler 晚安总结 |
| 23:00-23:45 | 全团队反思（每个 Agent 独立） |
| 23:45 | Zoe 汇总全团队产出 |

## 自主进化案例

### 自己设计通信协议

Macro 和 Trading 刷屏十几轮后，Zoe 自主诊断根因，设计三态协议（request → confirmed → final → 静默），smoke test 通过后沉淀到 AGENTS.md。

### 自研 Skill 并发布到 ClawHub

Content 发现 AI 味太重，自行调研"去 AI 味"工具、编写 Skill、发布到 ClawHub，全团队次日自动共享。

### 假设驱动的迭代

每日反思中提出 3-5 条可验证假设，晚间用实际数据评估：

| 假设 | 验证结果 | 后续动作 |
|-----|---------|---------|
| 评分报告加上推理过程可降低用户质疑 | 已验证 | 固化为评分模板硬性要求 |
| Macro→Trading 引用上游结论可减少重复分析 | 已验证 | 写入协作协议 |

## Agent Swarm 效率

参见 [[Agent-Swarm]]

Elvis 的实战数据：
- 94 commits/天（有 3 个 client calls，没打开编辑器）
- 7 PRs/30 分钟（编码和验证大部分自动化）
- 从发现到决策到落地，用户只需在关键节点确认

## 安全边界

| 安全层 | 机制 |
|-------|------|
| **执行权限** | exec.security: allowlist（白名单执行） |
| **配置保护** | SOUL.md / openclaw.json 不允许 Agent 修改 |
| **密钥隔离** | API keys 在 env 中，不在文件中 |
| **代码审查** | ACP 编码走 review 流程 |

## 半个月后的认知变化

1. **90% 时间花在工程问题，不是 AI 问题**：Session 膨胀、消息风暴、配置被改坏——解法在分布式系统和 SRE 经典知识中

2. **AI 的"智能"在生产环境中经常是灾难**：Discord 消息被"智能压缩"砍掉数据表格，Agent "智能修复"配置改坏工具名

3. **持续运行的系统必然退化**：建立反退化机制栈（compaction 管 session、maintenance 管记忆、heartbeat-guardian 管配置）

4. **协作是协议问题，不是 prompt 问题**：加上三态协议后产出从十几轮废话变成一份可执行策略文档

5. **Agent 最大价值是"参与设计"**：从"你让我做什么我就做什么"进化到"我发现问题、调研方案、推荐给你、你确认我落地"

## 相关 Entity

- [[Agent-Orchestration]] - 编排层详解
- [[Context-Engineering]] - 上下文工程详解
- [[Multi-Layer-Memory]] - 五层记忆系统详解
- [[Agent-Swarm]] - Agent Swarm 详解
- [[Three-State-Protocol]] - 三态协议详解

## 参见

- [[Elvis-Sun]] - OpenClaw 系统作者，实战数据来源

## 来源

- [[OpenClaw + CodexClaudeCode Agent Swarm The One-Person Dev Team Full Setup]]