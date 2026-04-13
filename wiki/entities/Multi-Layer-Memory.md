---
type: entity
title: Multi-Layer Memory
definition: "五层记忆系统借鉴人类认知模型，从短期到长期分层管理 Agent 的记忆，实现跨会话的知识沉淀和自主进化。"
created: 2026-04-09
updated: 2026-04-09
tags:
  - AI-Agent
  - OpenClaw
  - Memory-System
related_entities:
  - "[[Context-Engineering]]"
  - "[[Agent-Orchestration]]"
source_raw:
  - "[[OpenClaw + 6 个 Agent 运转半个月，从聊天到干活的完整工程实践]]"
---

# Multi-Layer Memory

> [!definition] 定义
> 五层记忆系统借鉴人类记忆的分层模型（工作记忆→长期记忆→程序性记忆），为 Agent 设计不同时间尺度和管理方式的记忆层级，实现跨会话的知识沉淀和自主进化。

## 核心问题：Agent 今天犯的错，明天还会犯

chatbot 每次对话从零开始，反复犯同样错误是正常的。但 Agent 7×24 运行、每天处理几千次 LLM 调用，**无法接受反复犯同一个错误**。

交易蜘蛛 5 次把龙虎榜 API 字段名搞错——每次 session 重置后记忆丢失，下一次又犯。

**Agent 和 chatbot 的分水岭**：Agent 应该能从错误中学习，下次不犯。

## 五层记忆架构

| 层 | 存储 | 时间尺度 | 管理方式 | 典型内容 |
|---|------|---------|---------|---------|
| **L1 身份层** | SOUL.md | 永恒 | 人工确认修改 | 身份 + 硬约束 + 决策框架 |
| **L2 期记忆** | MEMORY.md | 长期 | Agent 自主维护 | 结构化经验（成功模式/失败教训） |
| **L3 中期记忆** | memory/YYYY-MM-DD.md + memory.db | 中期 | Harness 自动提取 | Session > 40K tokens 时的精华快照 |
| **L4 期记忆** | .learnings/ | 短期 | Agent 即时记录 | 错误记录、用户纠正、最佳实践 |
| **L5 持久化** | Skills + Obsidian + ontology | 持久 | 共享/归档 | 技能库 + 知识归档 + 知识图谱 |

## 记忆自主迭代循环（6 步）

```
1. 触发事件
   操作失败 / 用户纠正 / 发现更优做法 / 需要新能力
   ↓
2. .learnings/ 即时记录
   ERRORS.md / LEARNINGS.md / FEATURE_REQUESTS.md
   状态：pending — 低成本、高频率、不审查直接写入
   ↓
3. 每日反思 Cron (23:00-23:45)
   扫描 .learnings/ 所有 pending 条目 → 评估复现频率和重要性
   ✓ ≥3 次 → promote 到 MEMORY.md
   ✗ <3 次 → 保留 pending，继续观察
   ↓
4. promote 到 MEMORY.md
   长期记忆、<3000 tokens 硬上限、超限时 Agent 自主精简
   ↓
5. 下次 Session 加载
   self-improvement hook bootstrap 注入
   ↓
6. Agent 行为改进
   下次遇到同样问题时自动避免
```

## 层间衔接机制

### Harness 并行路径

Session 40K tokens → memoryFlush → memory/YYYY-MM-DD.md → memory.db

与 Agent 自主的 `.learnings/` → MEMORY.md 路径互补：
- Harness 管"对话精华提取"
- Agent 管"经验教训沉淀"

### 为什么 ≥3 次？

防止偶发事件（如一次 API 超时）污染长期记忆。3000 tokens 额度很珍贵，只有反复出现的模式才值得占位。

## SOUL.md 的特殊地位

Agent 可以自主更新 `.learnings/`、`MEMORY.md`、`memory/`、`knowledge/`——但**绝对不能改 SOUL.md**。

SOUL.md 是身份和硬约束，修改需要用户确认。曾有 Agent 把自己的"人格"改松，行为立刻变得不可控。

## 真实进化案例

```
用户纠正: "昨天建议买军工，今天跌了就转空"
  ↓
即时记录 (.learnings/):
  "[LRN-20260303-001] correction | priority: high
   军工策略在地缘利好场景下未充分强调短线拥挤与顶背离风险
   Suggested Action: 条件单模板 — 入场带失效位 + bullish/base/bear 三情景"
  ↓
每日反思 cron (23:30): promote 到 MEMORY.md
  ↓
MEMORY.md: "❌ 事件驱动标的必须用条件单模板"
  ↓
三周后遇到类似板块轮动:
  交易蜘蛛直接引用了这条经验
```

## 进化记录表

| 发现 | 进化 | 来源 |
|-----|------|------|
| SOUL.md 信息过载导致规则失效 | 精简核心，非核心规则迁移到 Skills 按需加载 | 行为异常排查 |
| delivery=ok ≠ 知识库已落库 | 反思同时核对投递 + 文件存在性 | 管家零产出事件 |
| butler 零产出但反思说"正常" | 建议性兜底 → 硬门禁（产出为空 = 失败） | 运维巡检 |
| trading 频道刷屏（双发送链路） | 幂等键 + 单层重试 + 节流 | P0 事故 |
| 军工策略只看事件驱动 | 条件单模板：入场+失效位+三情景 | **Agent 自提方案** |

## 来源

- Raw Source: [[OpenClaw + 6 个 Agent 运转半个月，从聊天到干活的完整工程实践]]