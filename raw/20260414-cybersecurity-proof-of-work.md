---
title: "Cybersecurity Looks Like Proof of Work Now"
source: "https://www.dbreunig.com/2026/04/14/cybersecurity-is-proof-of-work-now.html"
author:
  - "[[Drew Breunig]]"
published: 2026-04-14
created: 2026-04-20
description: "Is security spending more tokens than your attacker?"
tags:
  - "clippings"
---
### Is security spending more tokens than your attacker?

Last week we learned about Anthropic’s Mythos, a new LLM so “ [strikingly capable at computer security tasks](https://red.anthropic.com/2026/mythos-preview/) ” that Anthropic didn’t release it publicly. Instead, [only critical software makers have been granted access](https://www.anthropic.com/glasswing), providing them time to harden their systems.

We quickly blew through our standard stages of processing big AI claims: shock, existential fear, hype, skepticism, criticism, and (finally) moving onto the next thing. I encouraged people to take a wait-and-see approach, as security capabilities are tailor-made for impressive demos. Finding exploits is a clearly defined, [verifiable](https://www.dbreunig.com/2025/12/29/2025-in-review.html) search problem. You’re not building a complex system, but poking at one that exists. A problem well suited to throwing millions of tokens at.

Yesterday, the first 3rd party analysis landed, [from the AI Security Institute](https://www.aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities) (AISI), largely supporting Anthropic’s claims. Mythos is *really* good, “a step up over previous frontier models in a landscape where cyber performance was already rapidly improving.”

The entire report is worth reading, but I want to focus on the following chart, detailing the ability of different models to successfully complete a simulated, complex corporate network attack:

![](https://www.dbreunig.com/img/the_last_ones_chart.png)

“ [The Last Ones](https://arxiv.org/abs/2603.11214) ” is, “a 32-step corporate network attack simulation spanning initial reconnaissance through to full network takeover, which [AISI](https://www.aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities) estimates to require humans 20 hours to complete.” The lines are the average performance across multiple runs (10 runs for Mythos, Opus 4.6, and GPT-5.4), with the “max” lines representing the best of each batch. Mythos was the only model to complete the task, in 3 out of its 10 attempts.

This chart suggests an interesting security economy: **to harden a system we need to spend more tokens discovering exploits than attackers spend exploiting them**.

AISI budgeted 100M tokens for each attempt. That’s $12,500 per Mythos attempt, $125k for all ten runs. Worryingly, none of the models given a 100M budget showed signs of diminishing returns. “Models continue making progress with increased token budgets across the token budgets tested,” AISI notes.

If Mythos continues to find exploits so long as you keep throwing money at it, security is reduced to a brutally simple equation: **to harden a system you need to spend more tokens discovering exploits than attackers will spend exploiting them**.

You don’t get points for being clever. You win by paying more. It is a system that echoes cryptocurrency’s [proof of work](https://en.wikipedia.org/wiki/Proof_of_work) system, where success is tied to raw computational work. It’s a [low temperature lottery](https://x.com/lateinteraction/status/2042025859003920574): buy the tokens, maybe you find an exploit. Hopefully you keep trying longer than your attackers.

This calculus has a few immediate takeaways:

**First, open source software remains critically important.**

For those of you who aren’t exposed to AI maximalists, this statement feels absurd. But lately, after the [LiteLLM](https://docs.litellm.ai/blog/security-update-march-2026) and [Axios](https://www.elastic.co/security-labs/how-we-caught-the-axios-supply-chain-attack) supply chain scares, many have argued for reimplementing dependency functionality using coding agents.

Here’s Karpathy, [just a few weeks ago](https://x.com/karpathy/status/2036487306585268612?s=20):

> Classical software engineering would have you believe that dependencies are good (we’re building pyramids from bricks), but imo this has to be re-evaluated, and it’s why I’ve been so growingly averse to them, preferring to use LLMs to “yoink” functionality when it’s simple enough and possible.

If security is purely a matter of throwing tokens at a system, [Linus’s law](https://en.wikipedia.org/wiki/Linus%27s_law) that, “given enough eyeballs, all bugs are shallow,” expands to include tokens. If corporations that rely on OSS libraries spend to secure them with tokens, it’s likely going to be more secure than your budget allows. Certainly, this has complexities: cracking a widely used OSS package is inherently more valuable than hacking a one-off implementation, which incentivizes attackers to spend more on OSS targets.

**Second, hardening will be an additional phase for agentic coders.**

We’ve already been seeing developers break their process into two steps, development and code review, often using different models for each phase. As this matures, we’re seeing purpose-built tooling meeting this pattern. Anthropic launched a [code review](https://code.claude.com/docs/en/code-review) product that costs $15-20 per review.

If the above Mythos claims hold, I suspect we’ll see a three phase cycle: development, review, and hardening.

1. **Development:** Implement features, iterate quickly, guided by human intuition and user feedback.
2. **Review:** Document, refactor, and other gardening tasks, async, applying best practices with each PR.
3. **Hardening:** Identify exploits, autonomously, until the budget runs out.

Critically, human input is the limiter for the first phase and money is the limiter for the last. This quality inherently makes them separate stages (why spend to harden before you have something?). Previously, security audits were rare, discrete, and inconsistent. Now we can apply them constantly, within an optimal (we hope!) budget.

Code remains [cheap](https://www.dbreunig.com/2026/03/26/winchester-mystery-house.html), unless it needs to be secure. Even if costs go down as inference optimizations, unless models reach the point of diminishing security returns, you *still* need to buy more tokens than attackers do. The cost is fixed by the market value of an exploit.

---

## 编译摘要

### 1. 浓缩

- **核心结论1**: 网络安全正在变成”Proof of Work”博弈——防御者需要花费比攻击者更多的 tokens 发现漏洞，而非依靠技术巧思
  - 关键证据: “You don’t get points for being clever. You win by paying more... to harden a system you need to spend more tokens discovering exploits than attackers will spend exploiting them”

- **核心结论2**: Anthropic Mythos 模型在 AISI 测试中完成 32 步企业网络攻击模拟（人类需 20 小时），100M tokens 预算（$12,500）仍未显示边际收益递减
  - 关键证据: “Mythos was the only model to complete the task, in 3 out of its 10 attempts... none of the models given a 100M budget showed signs of diminishing returns”

- **核心结论3**: Agentic Coding 将进入三阶段循环：开发 → 代码审查 → 安全硬化（human input vs money 分别是瓶颈）
  - 关键证据: “I suspect we’ll see a three phase cycle: development, review, and hardening”

### 2. 质疑

- **关于”结论1”的质疑**: Proof of Work 模型假设 tokens 成本不变；若推理成本下降（如推理优化），安全预算是否持续有效？
- **关于”结论2”的质疑**: Mythos 测试结果来自 AISI（英国 AI 安全研究所），是否独立验证？Anthropic 自称”strikingly capable”可能有营销成分
- **关于数据可靠性的质疑**: 100M tokens 预算未显示边际收益递减，但测试范围有限；真实攻击场景可能更复杂

### 3. 对标

- **跨域关联1**: Proof of Work 类似加密货币挖矿——成功概率与算力投入成正比，而非技术优势
- **跨域关联2**: Linus’s law 扩展（”eyeballs + tokens”）类似开源软件历史：平台依赖 → 社区审计 → 企业投入 tokens 审计

### 概念更新建议

- **新增 Entity**: [[Cybersecurity-Proof-of-Work]]（安全即 token 成本博弈）
- **新增 Entity**: [[Drew-Breunig]]（作者）
- **新增 Entity**: [[Mythos]]（Anthropic 安全专用模型）
- **新增 Entity**: [[Security-Hardening-Phase]]（agentic coding 第三阶段）
- **更新 [[Agentic-Engineering]]**: 补充三阶段模型（开发/审查/硬化）

## 关联概念

- [[Drew-Breunig]]
- [[Cybersecurity-Proof-of-Work]]
- [[Mythos]]
- [[Security-Hardening-Phase]]
- [[Agentic-Engineering]]
- [[Andrej-Karpathy]]