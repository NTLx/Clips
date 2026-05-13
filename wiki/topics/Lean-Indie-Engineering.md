---
type: topic
title: Lean-Indie-Engineering
description: "独立开发者用极低技术成本运营盈利产品的工程哲学与实践，核心是控制分母、反企业思维、约束驱动决策"
created: 2026-04-15
updated: 2026-05-08
tags:
  - indie-developer
  - bootstrap
  - software-engineering
  - entrepreneurship
related_entities:
  - '[[Steve-Hanov]]'
  - '[[Lean-Stack]]'
  - '[[Runway-Math]]'
  - '[[Anti-Enterprise-Mindset]]'
  - '[[B2B-Nurture-C-Model]]'
  - '[[Time-Moat]]'
  - '[[Constraint-Driven-Engineering]]'
source_raw:
  - '[[How I run multiple `$10K` MRR companies on a `$20`month tech stack]]'
---

# Lean-Indie-Engineering（精益独立开发）

## 主题定义

**Lean-Indie-Engineering** 是独立开发者用极低成本（`$20/月`）运营多个盈利产品的工程哲学。2026 年由 Steve Hanov 的 Hacker News 帖子 (952 分) 引发广泛讨论。

核心问题：**如何在一个人都能跑月入六位数产品的前提下，把技术月支出压到 `$20`？**

---

## 核心原则

### 1. Runway-Math：分母控制论

```
生存时间 = 资金 ÷ 月支出
```

- 分子不可控（VC 不理你、市场不买账、产品没起来 → 随时归零）
- 分母 100% 可控（你可以永远选择花多少钱）
- `$20` 月支出 = 永远不会死，可以一直试

> "Keeping costs near zero gives you the exact same runway as getting a million dollars in funding."

### 2. Anti-Enterprise-Mindset：不买"万一"的账

| "万一"担忧 | 预付成本 | 实际需要 |
|-----------|---------|---------|
| 万一火了 → K8s | `$500-2000/月` | 便宜 VPS |
| 万一挂了 → Multi-AZ RDS | `$200-500/月` | 单机 + 备份 |
| 万一要 SSO → Auth0 | `$50-200/月` | 30 行 OAuth2 |

六个"万一" = `$3,000/月` = 300 个 `$10` 用户才能回本。而你还没发第一条营销推文。

### 3. Constraint-Driven-Engineering：约束决定选择

没有放之四海皆准的"最佳技术栈"。必须先设定约束（预算、人力、时间），再从约束出发选择。

Steve 的约束 = "一个人、`$20/月`、6 个产品" → Go + SQLite + 单机 VPS 是唯一最优解。

---

## Lean-Stack 配置

| 组件 | 选择 | 成本 |
|------|------|------|
| 服务器 | Linode/DigitalOcean 1GB | `$5/月` |
| 数据库 | SQLite + WAL | `$0` |
| 语言 | Go (静态二进制, `scp` 部署) | `$0` |
| 认证 | 自写 30 行 OAuth2 | `$0` |
| 部署 | systemd service | `$0` |
| AI 批量推理 | RTX 3090 (24GB) + VLLM | 一次性 `$900` |
| AI API 网关 | OpenRouter 统一接口 + 故障回退 | 按量 |
| AI 开发 | GitHub Copilot per-request | `$13/月` |

### SQLite + WAL 的 40 倍优势

跑 10 万次 `SELECT 1`:
- PostgreSQL (localhost TCP): 2.77 秒
- SQLite (内存): 0.07 秒 — **差距 40 倍**

因为 app 和数据库在同一进程，查询走 C 函数调用（纳秒级），不是 TCP 往返（毫秒级）。

### 本地 AI 三层升级路径

Steve 的 AI 策略不是"不用 API"，而是**把不同任务路由到不同成本层**：

```
Ollama (快速实验)
    ↓ 一个命令试几十个模型，调 prompt
VLLM + PagedAttention (生产并发)
    ↓ 16 个异步请求 GPU 自动批处理，同时完成
Transformer Lab (微调)
    ↓ 需要定制模型时
```

| 任务类型 | 用本地 GPU | 用云端 API |
|---------|-----------|-----------|
| 批量研究/分类/摘要（数千次） | ✅ 零边际成本 | ❌ `$100+`/次 |
| 用户交互（低延迟对话） | ❌ 模型不够强 | ✅ OpenRouter |
| Prompt 迭代实验 | ✅ 无压力试错 | ❌ 每次改 prompt 都要重新付费 |

**核心工具**: laconic — Go 写的 agentic researcher，将 LLM 上下文像 OS 虚拟内存一样管理，"swap out" 不相关对话，让 8K 上下文窗口也能做深度研究。

### Copilot per-request 定价漏洞

GitHub Copilot 按**请求**计费而非按 **token**——一次请求即使让 agent 跑 30 分钟、修改数百文件，仍然 `$0.04`。策略：

1. 写极其详细的 prompt + 严格成功标准（本身就是最佳实践）
2. 告诉 agent "一直继续直到所有错误都修复"
3. 按回车，去冲杯咖啡，Satya Nadella 补贴你的算力成本

月账单 `$60`（全天用 Opus 4.6）vs Cursor 竞品用户 `$100+`。这个套利窗口迟早被修补——但在那之前，它是已知最便宜的 agentic coding 方案。

### OpenRouter：API 网关 + 故障回退

不直接对接 Anthropic/Google/OpenAI 的 API。用 OpenRouter 做统一接口：
- 一次集成 → 所有前沿模型可用
- Anthropic API 挂了 → 自动回退到 OpenAI 等价模型
- 用户永远看不到错误页面，不需要写复杂的重试逻辑

---

## 商业模式：B2B 养 C 端

| 产品 | 类型 | 定价 | 作用 |
|------|------|------|------|
| zwibbler | B2B SDK | `$5,999/`单 | 现金流引擎 |
| websequencediagrams | C 端工具 | Freemium | SEO 引流 |
| rhymebrain | C 端工具 | 广告+API | 长尾收入 |
| rapt.ink | C 端工具 | Freemium | 用户增长 |
| xreplyextension | C 端工具 | 一次性点数 | 现金流前置 |
| eh-trade.ca | 金融工具 | 订阅 | 垂直市场 |

**抗周期**: 经济好时 B2B 好卖，经济差时 DIY 工具好卖。

---

## 时间护城河

- **websequencediagrams**: 2008 年至今，Google "sequence diagram" 第一
- **rhymebrain**: 2009 年至今，8 语种押韵数据
- **每 3-5 年加一个新产品**: 慢做、深做、长做

> "这些东西你今天从零做，永远追不上。"

---

## 我们能抄什么作业？

1. **数据库迁到 SQLite + WAL** — 体验 50ms → 2ms 的响应
2. **App 搬到 Hetzner** — `$5` 买 4GB，systemd 一个 service 就起来
3. **试试 GitHub Copilot per-request** — 省下来的钱买 RTX 3090
4. **先想清楚你的约束** — 再看别人用了什么，往自己身上套

---

## 最清醒的一段话

> "Forget about the tech stack, how do I get multiple `$10k` MRR companies?"
> — @stavros, HN 评论区

> "The tech industry wants you to believe that building a real business requires complex orchestration. It doesn't."
> — Steve Hanov

## 关联 Entity
- [[Cybersecurity-Proof-of-Work]]
- [[Security-Hardening-Phase]]
- [[YAGNI]]
