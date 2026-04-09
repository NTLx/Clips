---
type: entity
title: Context Engineering
definition: "Context Engineering 是设计 Agent 每次推理时看到的完整信息结构，包括 SOUL.md、AGENTS.md、Skills 按需加载、上下文生命周期管理等。"
created: 2026-04-09
updated: 2026-04-09
tags:
  - AI-Agent
  - OpenClaw
  - System-Design
related_entities:
  - "[[Agent-Orchestration]]"
  - "[[Multi-Layer-Memory]]"
  - "[[Claude-Code-CLI]]"
source_raw:
  - "[[../00-raw/web-clips/Claude-Code/OpenClaw + 6 个 Agent 运转半个月，从聊天到干活的完整工程实践]]"
---

# Context Engineering

> [!definition] 定义
> Context Engineering（上下文工程）是设计 Agent 每次推理时看到的完整信息结构——系统级的信息架构设计。它决定了 Agent 能记住什么、能遵守什么规则、能做出什么决策。

## 核心问题：Agent 系统的热力学第二定律

**不加约束，entropy 只增不减。** 持续运行的 Agent 系统会**确定性地**走向崩溃。

Agent 就像一个没有操作系统的进程：
- 谁来管理它的内存（上下文）？
- 谁来做垃圾回收（Session 清理）？
- 谁来防止 OOM（膨胀保护）？

不设计就没有人管。

## 上下文层级结构

```
~/.claude/CLAUDE.md     ← 全局（所有项目通用）
~/project/CLAUDE.md     ← 项目级（当前项目专用）
~/project/src/CLAUDE.md ← 子目录级（进入该目录时加载）
```

所有层级是**叠加**的，不会覆盖。

## Agent 信息架构设计

| 层级 | 文件 | 内容 | 特点 |
|-----|------|------|------|
| **身份层** | SOUL.md | 身份定义、决策框架、绝对禁止项 | 放在 system prompt 最前面，精简核心 |
| **操作层** | AGENTS.md | 操作规范和协作协议 | 跟在 SOUL.md 后面 |
| **技能层** | Skills | 可复用知识包 | 通过 extraDirs 按需加载 |
| **冷存储** | Obsidian Vault | 归档产出 | 不参与推理 |

## LLM 上下文窗口的特性

**上下文窗口不是等价的**：
- system prompt 前面的信息权重远高于后面的
- session 膨胀到几万 tokens 后，早期消息的影响力被稀释

类比操作系统的内存管理：**热数据放缓存，冷数据放磁盘，关键数据常驻内存**。

## 按需加载策略

Trading 的 15 个 Skills（68000+ 行）：
- `stock_analysis`（技术面评分）在每日扫描时才需要
- `bilateral_analysis`（龙虎榜分析）只在异动时触发

全部常驻上下文的话，**噪声淹没了真正重要的规则**。通过 `extraDirs` 按需注入，每次推理只加载相关的 1-3 个 Skill。

## 规则措辞原则

**面向最弱的模型写规则**：

| 措辞 | GPT-5.4 | Qwen3.5+ | qwen3:8b |
|-----|---------|----------|----------|
| `"建议不要编造数据"` | 基本遵守 | 偶尔遵守 | 几乎无视 |
| `"MUST: 不编造数据"` | 高遵守 | 显著提升 | 较高遵守 |
| `"MUST + P0 + NON-NEGOTIABLE"` | 很高 | 高 | 高 |

多模型 fallback 时，所有关键规则都要按最弱模型的理解能力来写。**显式 > 隐式，硬规则 > 软建议**。

## Harness 框架自动管理

| 机制 | 触发条件 | 动作 |
|-----|---------|------|
| compaction memoryFlush | Session > 40K tokens | 提取精华到 memory/YYYY-MM-DD.md |
| contextPruning | 上下文 > 6 小时 | cache-ttl 裁剪，保留最近 3 条 |
| session reset | 每天 5:00 或空闲 30min | 自动重置 |
| session maintenance | 文件 > 7 天 | 自动清理，磁盘上限 100MB |

## 真实事故案例

### P0 — 全团队瘫痪 8 小时

ainews 的 session 因连续处理新闻累积到 **235K tokens**。Gateway 启动时对所有 session 做 compaction，这个 session 永远超时 → crash → macOS 守护进程每秒重启 → 无限循环。所有 Agent 全部离线。

修复要四层：手动清理膨胀 session → ThrottleInterval 1→10 → idleMinutes 180→30 → exec.security full→allowlist。

### P2 — 信息过载后关键规则失效

当 SOUL.md 堆满各种操作规范、session 膨胀到几万 tokens，Agent 开始"选择性遵守"规则。管家蜘蛛越界做投资分析，交易蜘蛛忽略数据验证规则。**关键信息被噪声淹没了**。

## 来源

- Raw Source: [[../00-raw/web-clips/Claude-Code/OpenClaw + 6 个 Agent 运转半个月，从聊天到干活的完整工程实践]]