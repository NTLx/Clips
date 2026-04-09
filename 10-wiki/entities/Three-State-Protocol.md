---
type: entity
title: Three-State Protocol
definition: "三态通信协议是 Agent 之间协作的通信协议设计，通过 request → confirmed → final 三种状态防止 ACK storm 并确保协作收敛。"
created: 2026-04-09
updated: 2026-04-09
tags:
  - AI-Agent
  - OpenClaw
  - Communication-Protocol
related_entities:
  - "[[Agent-Orchestration]]"
  - "[[Agent-Swarm]]"
source_raw:
  - "[[../00-raw/web-clips/Claude-Code/OpenClaw + 6 个 Agent 运转半个月，从聊天到干活的完整工程实践]]"
---

# Three-State Protocol

> [!definition] 定义
> 三态通信协议是 Agent 之间协作的通信协议设计，通过固定三态（request → confirmed → final）防止 ACK storm（消息刷屏），并确保多 Agent 协作能够收敛到最终结果。

## 核心问题：把 Agent 放进群聊 ≠ 协作

大多数人对 Multi-Agent 的直觉是"给几个 Agent 一个聊天群，它们就能协作"。实际上，这和把几个工程师拉到没有流程规范的群聊里没有区别。

### ACK Storm 案例

Macro 和 Trading 在"伊朗局势对 A 股影响"上互相"收到/确认/感谢"刷了十几轮。分析早就做完了，但分析之后两个 Agent 客套的 token 比分析本身还多。

根因是**缺乏终态协议**。当两个 Agent 互相 @，A → B → A → B......这就是经典的 ACK storm。

## 协议设计

```
固定三态协议（强制）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[request]    @对方 + ack_id + 期望动作 + 截止时间
             模板: @agent [state=request] [ack_id=topic-v1-202603081430]

[confirmed]  @发起方 + 相同 ack_id + 版本号/生效时间/关键结论
             模板: @requester [state=confirmed] [ack_id=...] 版本=v2

[final]      @相关方 + 相同 ack_id + 终态收敛（全线程仅 1 条）
             发出后全员进入静默，"收到/感谢/OK" → NO_REPLY
```

## V1 线程协议

```
V1 线程协议（2026-03-08 起）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• 同一线程只允许一个 ack_id，新一轮必须新开
• final 后禁止续话；必须补充时优先 edit 既有消息
• sessions_send 超时 ≠ 失败 → 同一 ack_id 不得重试
• 同一内容最多重试 1 次；第二次超时 → shared-context/ 文件投递

⏰ 5 分钟无 confirmed → 催办 1 次 · 10 分钟仍无 → 升级 Zoe 仲裁
```

## 协议执行案例

### 下周 A 股策略圆桌讨论

**Step 1**：Zoe 发起议题 + Macro/Trading 按 protocol confirmed

**Step 2**：Trading 基于 Macro 研判给出详细策略（confirmed 输出）

**Step 3**：Trading 输出 final（DRI 结论 + 完整推理过程）

**Step 4**：协议收敛（final 后全员静默）

从十几轮废话 → 一份可执行策略文档。模型没变，变的是规则。

## DRI 原则

一个问题只有一个 Directly Responsible Individual 出最终结论。非 DRI 只能补充，不能覆盖。

Zoe 组织和归档，不替代专业 Agent 出专业意见。

## 三种通信机制

| 机制 | 用途 | 特点 |
|-----|------|------|
| `sessions_send` | 实时触发 | 不可靠（超时、重复） |
| `shared-context/` 文件 | 关键数据 | 可追溯、结构化 |
| Discord Thread | 子线程协作 | 主频道只同步三次状态 |

## shared-context/ 结构

```
shared-context/
├── agent-sessions/       # ACP 编码专家的 session 状态
├── monitor-tasks/        # Task Watcher 持久化存储
├── intel/                # 情报共享（finance_news_latest.json 等）
├── roundtable/           # 圆桌讨论记录
├── decisions/            # 重大决策存档
├── status/               # 各 Agent 当前状态 JSON
├── tech-radar.json       # 技术雷达
└ PROJECT_STATUS.md       # 项目全局状态（Zoe 维护）
```

**核心价值**：从消息驱动升级到状态驱动。

Trading 不需要每次问 Macro"今天宏观怎么样"，直接读 `intel/finance_news_latest.json`。

## 协议演进

协议不是一次性设计出来的：

- 初版：禁止客套（无效）
- V1：线程级收敛 + ack_id + 超时升级（有效）

每一步协议优化都来自 Agent 的 `.learnings/` 经验沉淀——这正是五层记忆系统的价值。

## 来源

- Raw Source: [[../00-raw/web-clips/Claude-Code/OpenClaw + 6 个 Agent 运转半个月，从聊天到干活的完整工程实践]]