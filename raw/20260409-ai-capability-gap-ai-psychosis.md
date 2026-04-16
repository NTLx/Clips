---
title: "AI 能力鸿沟与 AI Psychosis"
type: raw
source: "https://x.com/karpathy/status/2042334451611693415"
author:
  - "[[Andrej-Karpathy]]"
published: "2026-04-09"
created: "2026-04-16"
updated: "2026-04-16"
description: "用户对 AI 的惊叹程度与其用 AI 编程的程度完美相关。免费层/旧模型用户与付费 agentic 模型用户之间存在巨大认知鸿沟。AI 进步不是平均分布的，而是在 coding/agent 方向先长成完全不同的物种。"
tags:
  - "clippings"
  - "ai-gap"
  - "ai-psychosis"
  - "agentic-models"
engagement:
  likes: "1.1万"
  retweets: "1.9万"
---

## 附加参考

- **池建强微信公众号**: https://mp.weixin.qq.com/s/OArrjAbDpinIADQzmymsVA
- **池建强墨问笔记**: https://note.mowen.cn/detail/wVRtr2XSutpQQZTnKnX5W

---

**Andrej Karpathy** @karpathy · 2026-04-09

Judging by my tl there is a growing gap in understanding of AI capability.

The first issue I think is around recency and tier of use. I think a lot of people tried the free tier of ChatGPT somewhere last year and allowed it to inform their views on AI a little too much. This is a group of reactions laughing at various quirks of the models, hallucinations, etc. Yes I also saw the viral videos of OpenAI's Advanced Voice mode fumbling simple queries like "should I drive or walk to the carwash". The thing is that these free and old/deprecated models don't reflect the capability in the latest round of state of the art agentic models of this year, especially OpenAI Codex and Claude Code.

But that brings me to the second issue. Even if people paid `$200/month` to use the state of the art models, a lot of the capabilities are relatively "peaky" in highly technical areas. Typical queries around search, writing, advice, etc. are *not* the domain that has made the most noticeable and dramatic strides in capability. Partly, this is due to the technical details of reinforcement learning and its use of verifiable rewards. But partly, it's also because these use cases are not sufficiently prioritized by the companies in their hillclimbing because they don't lead to as much `$$$` value. The goldmines are elsewhere, and the focus comes along.

So that brings me to the second group of people, who *both* 1) pay for and use the state of the art frontier agentic models (OpenAI Codex / Claude Code) and 2) do so professionally in technical domains like programming, math and research. This group of people is subject to the highest amount of "AI Psychosis" because the recent improvements in these domains as of this year have been nothing short of staggering. When you hand a computer terminal to one of these models, you can now watch them melt programming problems that you'd normally expect to take days/weeks of work. It's this second group of people that assigns a much greater gravity to the capabilities, their slope, and various cyber-related repercussions.

TLDR the people in these two groups are speaking past each other. It really is simultaneously the case that OpenAI's free and I think slightly orphaned (?) "Advanced Voice Mode" will fumble the dumbest questions in your Instagram's reels and *at the same time*, OpenAI's highest-tier and paid Codex model will go off for 1 hour to coherently restructure an entire code base, or find and exploit vulnerabilities in computer systems. This part really works and has made dramatic strides because 2 properties: 1) these domains offer explicit reward functions that are verifiable meaning they are easily amenable to reinforcement learning training (e.g. unit tests passed yes or no, in contrast to writing, which is much harder to explicitly judge), but also 2) they are a lot more valuable in b2b settings, meaning that the biggest fraction of the team is focused on improving them. So here we are.

---

**Andrej Karpathy** @karpathy · 2026-04-09

The degree to which you are awed by AI is perfectly correlated with how much you use AI to code.

---

## X Thread 相关回复（经池建强整理）

### Karpathy 补充：OpenClaw 的体感

> 最近有人跟我说，OpenClaw 之所以会引发那么大的反响，是因为这是第一次有一大批非技术背景的人，真正体验到了最新的 agentic 模型。对他们来说，之前对 AI 的理解，基本就停留在"ChatGPT 这个网站"上。

### 数据回复：ChatGPT 使用分布

> 根据 OpenAI 自己的数据以及哈佛 NBER 的一项研究，编程类查询只占 ChatGPT 消息的大约 **4%**，而非工作类查询占比超过 **73%**。
>
> 对于非编程使用场景，即使是每月 200 美元的订阅用户，从 2025 年到现在，体验到的更多也是**停滞甚至倒退**。

### Sebastian Raschka 的补充

> 这个差距其实还要更大。在我身边很多朋友和家人的圈子里，他们接触 AI 的主要入口甚至是新款 iPhone 上的 **Apple Intelligence**。
>
> 很多人当然也听说过 ChatGPT，但并没有太大兴趣。因为就像你说的，他们曾经用过某个时间点的免费版，然后就……

---

## 池建强的思考与分析

> 我以前在墨问里写过，AI 的出现正在加速人的能力差距。聪明和勤奋的人，没有 AI 的时候也会主动学习，有了 AI 之后，在学研领域只能用突飞猛进和如虎添翼形容。懒散一点的人，之前没有 AI 的情况下因为要找工作就得去啃书本，找师傅，实践，有了 AI 反而不学了，有点作业和任务，都让 AI 搞定。一来一去，差距越来越大。
>
> 这两天看 Andrej Karpathy 在 X 上的一条长帖，比我这个观点更进一步：**人们对 AI 能力的理解也越来越不一样了。**

### 人群分层

| 层级 | 特征 | 对 AI 的认知 |
|------|------|-------------|
| **完全不用 AI** | 大多数 | 没有理解 |
| **免费 AI 助手用户** | ChatGPT 免费版、豆包、千问、元宝等 | AI 是能聊天、有幻觉、偶尔有点惊喜的玩具 |
| **付费专业用户** | Claude Code、Codex、SOLO，用于编程/科研/业务长任务 | 看到的是完全不同的 AI 物种 |
| **顶尖 AI Researcher/工程师** | 在进行模型下一个范式的研发，制作 Claude Code 这样的工具 | 看到 AI 的全貌和未来 |

### 核心洞察

> A 觉得 B 过于狂热，B 又觉得 A 没看见真正的变化。Karpathy 说，这两群人其实是在鸡同鸭讲。
>
> 这中间当然有"新旧版本"的差异，但更深一层的原因，是 **AI 的进步本来就不是平均分布的**。
>
> 对普通用户来说，AI 在很多日常体验里并没有想象中那么大的跃迁；但对程序员、研究员和一部分专业用户来说，2025 到 2026 这段时间，简直像**地壳运动一样剧烈**。
>
> **AI 并不是"整体变强"了，而是在某些方向上先长成了一个完全不同的物种。比如 Coding 和 Agent。**
>
> 技术的浪潮总是这样。最开始，它只在少数人的工作台上发生。安静，陡峭，不太好解释。等大多数人都看见的时候，世界已经完全不一样了。

---

## 墨问社区讨论精选

**问题：普通人怎么应对这种情况呢？感觉与现实离得越来越远**

| 回复者 | 观点 |
|--------|------|
| **池建强**（作者） | 和 AI 一起进步 |
| **墨西西** | 普通人只需要等，等到像手机这样技术普惠阶段再开始使用。除非你不想做普通人，试图趁早捞点什么 |
| **Mew151** | 想办法把 AI 融入到你真实的生活和工作场景中去体验和使用。有哪些枯燥、重复、需要费心费力才能保证不出错（比如文字校对，数据筛选等）的事，试着交给 AI 去做 |
| **明轩** | 一样东西特别特别好，一样东西会很便宜或者免费给普通人，这两个在资本市场没办法同时出现在同一件产品上 |
| **鲮鱼** | AI 适合把**高频、不想做的活儿**做了。如果你没想到有什么活儿可以交给它，可以先考虑工作、生活里，有什么是高频的脏活，是不是可以标准、流程化，并且让 AI 持续帮你做 |
| **何遇** | 今天用 sonnet4.6 识别 Figma 截图做系统设计，能力让人震惊——第一次把图发给它 |

---

## 相关链接

- [[Andrej-Karpathy]]
- [[Software-2.0]]
- [[Vibe-Coding]]
- [[Claude-Code-CLI]]
- [[AI-Psychosis]]
- [[Agentic-Engineering]]

---

## 编译摘要

### 1. 浓缩
- **核心结论1**: AI 理解存在两条平行现实——免费用户 vs 付费 agentic 用户——"鸡同鸭讲"
  - **关键证据**: OpenAI 数据 + 哈佛 NBER 研究 — 编程类查询仅占 ChatGPT 消息 ~4%，非工作类 >73%；非编程场景下 $200/月订阅用户自 2025 年体验"停滞甚至倒退"
- **核心结论2**: AI 进步不是"整体变强"，而是"局部先长成不同物种"（Coding/Agent）
  - **关键证据**: RL 在可验证奖励领域（单元测试 yes/no）大幅领先；B2B 商业价值高 → 资源倾斜
- **核心结论3**: 一个人对 AI 的震撼程度 ≈ 用 AI 写了多少代码
  - **关键证据**: OpenClaw 首次让大批非技术用户接触最新 agentic 模型；池建强 4 层人群分层印证

### 2. 质疑
- **关于"两条平行现实"的前提假设**: 鸿沟不仅是"使用体验差异"，信息渠道和社交圈层的放大作用可能更大
- **"4% 编程查询"的定义模糊**: 是消息条数还是 token 消耗？4% 的消息可能消耗远超 4% 的算力
- **"震撼≈编码量"的相关性未验证**: Karpathy 自身编程背景的"选择偏差"；非技术用户的"震撼"可能来自法律/医疗等不同场景
- **关于"AI 不是整体变强"的反例**: 写作/创意领域也在进步（Midjourney, Sonnet 写作），只是进步更难量化
- **边界条件**: 如果出现"日常写作/搜索"的高效低价产品，鸿沟是否收敛？

### 3. 对标
- **跨域关联1**: [[Jevons-Paradox-for-Knowledge-Work]] — 效率提升导致需求增长，AI 编程越高效，程序员用越多
- **跨域关联2**: [[Knowledge-Work]] dying — 知识工作被 AI 取代，但 AI 本身正在创造新的"智慧工作"
- **跨域关联3**: 技术采纳曲线理论 — 早期采用者 vs 大众之间的认知鸿沟是所有颠覆性技术的共性

### 关联概念
- [[AI-Psychosis]]
- [[AI-Capability-Gap]]
- [[Agentic-Engineering]]
- [[Claude-Code-CLI]]
- [[Vibe-Coding]]
- [[Software-2.0]]
- [[Knowledge-Work]]
