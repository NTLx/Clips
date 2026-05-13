---
type: raw
title: "How I run multiple `$10K` MRR companies on a `$20`/month tech stack"
source: "https://stevehanov.ca/blog/how-i-run-multiple-10k-mrr-companies-on-a-20month-tech-stack"
author:
  - "[[Steve-Hanov]]"
published: "2026-04-15"
created: 2026-05-08
description: "Steve Hanov 分享他如何用每月 `$20` 技术成本运营 6 个月入过万美元的产品——从 VPS、Go 语言、SQLite+WAL 到本地 AI 推理和 GitHub Copilot per-request 定价漏洞的完整技术栈。"
tags:
  - clippings
  - indie-developer
  - bootstrap
  - lean-stack
---
Last night, I was rejected from yet another pitch night. It was just the pre-interview, and the problem wasn't my product. I already have MRR. I already have users who depend on it every day.

The feedback was simply: *"What do you even need funding for?"*

I hear this time and time again when I try to grow my ideas. Running lean is in my DNA. I've built tools you might have used, like [websequencediagrams.com](https://websequencediagrams.com/), and niche products you probably haven't, like [eh-trade.ca](https://eh-trade.ca/). That obsession with efficiency leads to successful bootstrapping, and honestly, a lot of VCs *hate* that.

Keeping costs near zero gives you the exact same runway as getting a million dollars in funding with a massive burn rate. It's less stressful, it keeps your architecture incredibly simple, and it gives you adequate time to find product-market fit without the pressure of a board breathing down your neck.

If you are tired of the modern "Enterprise" boilerplate, here is the exact playbook of how I build my companies to run on nearly nothing.

## Use a lean server

The naive way to launch a web app in 2026 is to fire up AWS, provision an EKS cluster, set up an RDS instance, configure a NAT Gateway, and accidentally spend `$300` a month before a single user has even looked at your landing page.

The smart way is to rent a single Virtual Private Server (VPS).

First thing I do is get a cheap, reliable box. Forget AWS. You aren't going to need it, and their control panel is a labyrinth designed to extract billing upgrades. I use Linode or DigitalOcean. Pay no more than `$5` to `$10` a month.

1GB of RAM sounds terrifying to modern web developers, but it is plenty if you know what you are doing. If you need a little breathing room, just use a swapfile.

The goal is to serve requests, not to maintain infrastructure. When you have one server, you know exactly where the logs are, exactly why it crashed, and exactly how to restart it.

## Use a lean language

Now you have constraints. You only have a gigabyte of memory. You *could* run Python or Ruby as your main backend language—but why would you? You'll spend half your RAM just booting the interpreter and managing `gunicorn` workers.

I write my backends in Go.

Go is infinitely more performant for web tasks, it's strictly typed, and—crucially for 2026—it is incredibly easy for LLMs to reason about. But the real magic of Go is the deployment process. There is no `pip install` dependency hell. There is no virtual environment. You compile your entire application into a single, statically linked binary on your laptop, `scp` it to your `$5` server, and run it.

Here is what a complete, production-ready web server looks like in Go. No bloated frameworks required:

```
package main

import (
    "fmt"
    "net/http"
)

func main() {
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "Hello, your MRR is safe here.")
    })
    
    // This will comfortably handle 10,000s of requests per second
    // on a potato.
    http.ListenAndServe(":8080", nil) 
}
```

## Use Local AI for long-running tasks

If you have a graphics card sitting somewhere in your house, you already have *unlimited* AI credits.

When I was building eh-trade.ca, I had a specific problem: I needed to perform deep, qualitative stock market research on thousands of companies, summarizing massive quarterly reports. The naive solution is to throw all of this at the OpenAI API. I could have paid hundreds of dollars in API credits, only to find a logic bug in my prompt loop that required me to run the whole batch over again.

Instead, I'm running VLLM on a dusty `$900` graphics card (an RTX 3090 with 24GB of VRAM) I bought off Facebook Marketplace. It’s an upfront investment, sure, but I never have to pay a toll to an AI provider for batch processing again.

For local AI, you have a distinct upgrade path:

- **Start with Ollama.** It sets up in one command (`ollama run qwen3:32b`) and lets you try out dozens of models instantly. It's the perfect environment for iterating on prompts.
- **Move to VLLM for production.** Once you have a system that works, Ollama becomes a bottleneck for concurrent requests. VLLM locks your GPU to one model, but it is *drastically* faster because it uses PagedAttention. Structure your system so you send 8 or 16 async requests simultaneously. VLLM will batch them together in the GPU memory, and all 16 will finish in roughly the same time it takes to process one.
- **Use Transformer Lab for anything more advanced.** If you need to do any model pre-training or fine-tuning, [Transformer Lab](https://lab.cloud/) makes it easy on local hardware.

To manage all this, I built [laconic](https://github.com/smhanov/laconic), an agentic researcher specifically optimized for running in a constrained 8K context window. It manages the LLM context like an operating system's virtual memory manager—it "pages out" the irrelevant baggage of a conversation, keeping only the absolute most critical facts in the active LLM context window.

I also use [llmhub](https://github.com/smhanov/llmhub), which abstracts any LLM into a simple provider/endpoint/apikey combo, gracefully handling both text and image IO whether the model is running under my desk or in the cloud.

## Use OpenRouter for your Fast/Smart LLM

You can't do *everything* locally. Sometimes you need the absolute cutting-edge reasoning of Claude or ChatGPT for user-facing, low-latency chat interactions.

Instead of juggling billing accounts, API keys, and rate limits for Anthropic, Google, and OpenAI, I just use OpenRouter. You write one OpenAI-compatible integration in your code, and you instantly get access to every major frontier model.

More importantly, it allows for seamless fallback routing. If Anthropic's API goes down on a Tuesday afternoon (which happens), my app automatically falls back to an equivalent OpenAI model. My users never see an error screen, and I don't have to write complex retry logic.

## Use Copilot instead of hyped AI IDEs

New, insanely expensive models are being released every week. I constantly hear about developers dropping hundreds of dollars a month on Cursor subscriptions and Anthropic API keys just to have an AI write their boilerplate.

Meanwhile, I'm using Claude Opus 4.6 all day and my bill barely touches `$60` a month. My secret? I exploit Microsoft's pricing model.

I bought a GitHub Copilot subscription in 2023, plugged it into standard VS Code, and never left. I tried Cursor and the other fancy forks when they briefly surpassed it with agentic coding, but Copilot Chat always catches up.

Here is the trick that you might have missed: somehow, Microsoft is able to charge per request, not per token. And a "request" is simply what I type into the chat box. Even if the agent spends the next 30 minutes chewing through my entire codebase, mapping dependencies, and changing hundreds of files, I still pay roughly `$0`.04.

The optimal strategy is simple: write brutally detailed prompts with strict success criteria (which is best practice anyway), tell the agent to "keep going until all errors are fixed," hit enter, and go make a coffee while Satya Nadella subsidizes your compute costs.

## Use SQLite for everything

I always start a new venture using `sqlite3` as the main database. Hear me out, this is not as insane as you think.

The enterprise mindset dictates that you need an out-of-process database server. But the truth is, a local SQLite file communicating over the C-interface or memory is orders of magnitude faster than making a TCP network hop to a remote Postgres server.

"But what about concurrency?" you ask. Many people think SQLite locks the whole database on every write. They are wrong. You just need to turn on Write-Ahead Logging (WAL). Execute this pragma once when you open the database:

```
PRAGMA journal_mode=WAL;
PRAGMA synchronous=NORMAL;
```

Boom. Readers no longer block writers. Writers no longer block readers. You can now easily handle thousands of concurrent users off a single `.db` file on an NVMe drive.

Since implementing user authentication is usually the most annoying part of starting a new SQLite-based project, I built a library: [smhanov/auth](https://github.com/smhanov/auth). It integrates directly with whatever database you are using and manages user signups, sessions, and password resets. It even lets users sign in with Google, Facebook, X, or their own company-specific SAML provider. No bloated dependencies, just simple, auditable code.

## Conclusion

The tech industry wants you to believe that building a real business requires complex orchestration, massive monthly AWS bills, and millions in venture capital.

It doesn't.

By utilizing a single VPS, statically compiled binaries, local GPU hardware for batch AI tasks, and the raw speed of SQLite, you can bootstrap a highly scalable startup that costs less than the price of a few coffees a month. You add infinite runway to your project, giving yourself the time to actually solve your users' problems instead of sweating your burn rate.

If you are interested in running lean, check out my auth library and agent implementations on my [GitHub](https://github.com/smhanov). I’ll be hanging around the comments—let me know how you keep your server costs down, or tell me why I'm completely wrong.

---

## 编译摘要

### 1. 浓缩

- **核心结论1: 零成本跑道等价于百万美元融资** — 月支出 `$20` = 无限生存时间，VC 拒绝他的原因恰恰是他跑得太精简
  - 关键证据: "Keeping costs near zero gives you the exact same runway as getting a million dollars in funding with a massive burn rate." Steve 因"太精益"被 pitch night 拒绝
  - Runway 公式: `$10,000` ÷ `$20/月` = 500 个月 (41 年) vs VC 融 `$1M` ÷ `$50K/月` = 仅 20 个月

- **核心结论2: 技术选型由约束驱动，而非潮流** — 1GB RAM 约束 → Go 而非 Python（静态二进制 几MB vs gunicorn 500MB 基线）；单机约束 → SQLite+WAL 而非 Postgres RDS（查询走 C 函数调用纳秒级 vs TCP 往返毫秒级）；一人团队 → systemd service 而非 K8s
  - 关键证据: SQLite+WAL `SELECT 1` benchmark 0.07s vs PostgreSQL TCP 2.77s（40 倍差距）；Go 交叉编译为静态二进制，scp 上传即运行，无依赖地狱

- **核心结论3: AI 成本有三层降本策略** — (1) 本地 GPU 处理批量任务：RTX 3090 (`$900` 一次性) + VLLM PagedAttention 并发推理，(2) OpenRouter 统一 API 网关 + 故障自动回退（Anthropic → OpenAI → 本地 VLLM），(3) GitHub Copilot per-request 定价漏洞：按请求而非 token 计费，一次请求可让 agent 运行 30 分钟修改数百文件，成本 `$0.04`
  - 关键证据: "Somehow, Microsoft is able to charge per request, not per token." Copilot 订阅 `$13/月`，作者用 Opus 4.6 全天开发月账单 `$60`，Cursor 等竞品用户月支出 `$100+`

- **核心结论4: 一人运营 6 个 `$10K+` MRR 产品的商业模式组合拳** — B2B 高客单价（zwibbler `$5,999`/单 × 20 单/年）养 C 端产品矩阵；六种定价模式覆盖三种盈利逻辑（大额低频、小额高频、一次性前置）
  - 关键证据: websequencediagrams.com (2008-) 18 年 SEO 权重无法复制；每 3-5 年新增一个产品，需求永恒 > 热点时髦

### 2. 质疑

- **关于"Copilot 定价漏洞"的持久性**: Microsoft 的 per-request 而非 per-token 定价模式显然低估了 agentic coding 的 token 消耗量。这个漏洞迟早会被修补——一旦修补，Copilot 的成本优势将消失。依赖定价漏洞的策略本质上是不可持续的套利
- **关于 SQLite+WAL 的可扩展性上限**: WAL 模式下单写者限制真实存在。虽然读不阻塞写，但高并发写入场景（如实时协作编辑）确实会遇到瓶颈。Steve 的选择成立的前提是：他的 6 个产品"不需要"高并发写入。这适用于大多数独立开发者产品，但不适用于所有场景
- **关于本地 GPU 的真实经济性**: RTX 3090 的 24GB VRAM 跑 32B 模型尚可，但前沿模型（Claude Opus 等级别）无法本地运行。他的"本地 AI"解决的是批量分类/摘要任务，不是替代前沿推理。电费 + 硬件折旧 + 维护时间 vs API 成本的完整 TCO 需要更精确的计算
- **关于"一个人"模式的不可复制性**: Steve 从 2008 年就开始积累，18 年的 SEO 权重、反链和用户信任构成的时间护城河，后发者无法复制。他今天的成功是他 18 年前开始的结果

### 3. 对标

- **跨域关联1 — 反云运动（Cloud Exit）**: Steve 的实践与 DHH (David Heinemeier Hansson) 的"cloud exit"运动在哲学上同源——都质疑"云=默认正确"的行业共识。差别在于 DHH 是从云迁回自建机房（大团队操作），Steve 是从一开始就不进云（单人操作），两条路径指向同一结论：云的成本结构对大部分产品不是最优
- **跨域关联2 — 边缘计算**: 本地 AI 推理（RTX 3090 + VLLM）本质上是将计算从云端移到边缘。这不仅是成本考量，也是延迟和隐私策略。与 CDN 将静态资产推到边缘的动机一致——让计算更靠近数据产生和消费的地方
- **跨域关联3 — 早期的云计算定价套利**: Copilot per-request 定价漏洞类似于早期 AWS 的预留实例 vs 按需实例套利，以及 Google Cloud 的 sustained use discount。平台在快速增长期往往定价偏低以获取市场份额，随后修补漏洞。识别和利用这种窗口期本身就是一种技能

### 关联概念

- [[Lean-Stack]]
- [[Runway-Math]]
- [[Anti-Enterprise-Mindset]]
- [[Constraint-Driven-Engineering]]
- [[B2B-Nurture-C-Model]]
- [[Time-Moat]]
- [[Steve-Hanov]]
- [[Vibe-Coding]]
