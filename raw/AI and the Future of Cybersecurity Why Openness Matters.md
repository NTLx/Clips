---
title: "AI and the Future of Cybersecurity: Why Openness Matters"
source: "https://huggingface.co/blog/cybersecurity-openness"
author:
  - "[[Margaret Mitchell]]"
  - "[[Yacine Jernite]]"
  - "[[Clem 🤗]]"
published: 2026-04-21
created: 2026-05-11
description: "We’re on a journey to advance and democratize artificial intelligence through open source and open science."
tags:
  - "clippings"
---
Following the announcement of [Mythos and Project Glasswing](https://www.anthropic.com/glasswing), institutions throughout the world are grappling with the potential dawn of a new era of cybersecurity. In this post, we break down the current situation, discuss the role of openness, and situate the future of cybersecurity within the larger AI ecosystem.

## What is Mythos?

Mythos is a [“frontier AI model”](https://www-cdn.anthropic.com/08ab9158070959f88f296514c21b7facce6f52bc.pdf), a large language model (LLM) that can be used to process software code (among many other things). This follows a general trend in LLM development, where LLM performance on code-related tasks has recently skyrocketed. What’s particularly significant about Mythos is the system it’s embedded within: It's the system, not the model alone, that has enabled Mythos to rapidly find and patch software vulnerabilities. Understanding this distinction is key to understanding the current landscape of AI cybersecurity.

What Mythos demonstrates is that the following **system** recipe is powerful:

- substantial compute power
- models trained on troves of software-relevant data
- scaffolding built to handle software vulnerability probing and patching
- speed (enabled by compute power and the capital behind it)
- some degree of system **autonomy**

Together, these ingredients can uncover software vulnerabilities, find exploits, and build patches. It’s in this recipe — not in any one model — that both the benefits and the risks come in.

This matters because others can build comparable systems. Smaller models embedded in systems built with deep security expertise could potentially produce similar outcomes more cheaply, which is particularly promising for defense. [AI cybersecurity capability is **jagged**](https://aisle.com/blog/ai-cybersecurity-after-mythos-the-jagged-frontier): It doesn’t scale smoothly with model size or general benchmark performance. The system the model is embedded within matters a lot.

So what Mythos has demonstrated is that it’s possible to build an AI system that finds and addresses software vulnerabilities. We already knew this was possible and there has been increasing work on this, but we’re just beginning to explore what it means in the context of agentic AI: Systems that can rapidly and autonomously take action.

## How Openness Can Be a Structural Advantage

As autonomous systems that identify software vulnerabilities proliferate (and they will), open code and tooling can help level the playing field. Software security has become a speed race across four stages: detection, verification, coordination, and patch propagation. Open ecosystems distribute these across a community, where more closed-source projects centralize knowledge and action across all four stages inside a single vendor, representing a single point of failure where only one organization can see and fix the code. The distributed nature of open development is robust to such constraints, and can be especially powerful in communities with dedicated security professionals, like the [Linux kernel security team](https://docs.kernel.org/process/security-bugs.html), the [Open Source Security Foundation](https://openssf.org/), and [the team at Hugging Face](https://huggingface.co/docs/hub/security) working on model and supply-chain security.

A common argument for more closed systems is proprietary obscurity, where the code underlying a system is inaccessible. Unfortunately, this provides less protection than it used to. AI systems are increasingly able to assist with reverse engineering of stripped binaries, which matters because most legacy firmware and embedded code is closed, binary-only, and no longer maintained. That code represents a huge attack surface, and it’s becoming more legible and accessible as AI tools improve.

There’s also a risk created by how AI is being used *inside* closed codebases. When companies adopt AI coding tools under the wrong incentives (for instance, evaluating engineers by the volume of features shipped rather than code quality) AI-accelerated development can introduce more vulnerabilities into proprietary code than traditional development would. Those vulnerabilities then sit inside a closed codebase where only one organization can find and fix them, while AI-enabled attackers are increasingly capable of discovering them from the outside. The combination of more vulnerabilities produced more quickly, behind a single-organization firewall, is exactly the kind of imbalance that open ecosystems are positioned to avoid.

Underlying all of this is capability asymmetry between attackers and defenders. Open models and open tooling narrow that gap by giving defenders access to the same class of capabilities attackers can reach for — capabilities that would otherwise be concentrated within a small number of well-resourced entities.

## Building Defenses with Open Tools and Semi-Autonomous Agents

Cybersecurity defense is where open source and AI agents can play a key role together. Based on the [System Card](https://www-cdn.anthropic.com/08ab9158070959f88f296514c21b7facce6f52bc.pdf), it appears that Mythos is capable of operating with close to full autonomy, something we’ve [advised against](https://huggingface.co/papers/2502.02649) due to the potential loss of control. AI agents that are instead *semi-autonomous*, where the types of actions they can take are prespecified and certain steps require human approval, hit a sweet spot of benefit and risk. In semi-autonomous systems, people remain in control, and the AI agent is responsible for specific subtasks. This is possible to do with open code that organizations can run privately within their own institutions, specifying allowable tools, skills, and system access privileges. With this setup, AI agents can be deployed defensively, finding vulnerabilities and assisting with patching under an organization’s own controls.

The semi-autonomous approach depends on humans being able to actually understand what an AI agent did and why. That’s much more possible when the system is built on open components, such as open agent scaffolding, open rule engines, and auditable decision logs and traces, than when it’s a black box. The “human in the loop” is only meaningful if the human can see into the loop.

Companies don’t have to build these capabilities entirely from scratch. There’s a rich open-source ecosystem of security tooling, including vulnerability scanners, intrusion detection systems, log analyzers, and fuzzing frameworks, that AI agents can be integrated with.

## Why This Matters Especially for High-Stakes Organizations

For high-stakes organizations, starting from open, auditable foundations means security teams can actually inspect how their monitoring works, rather than trusting a single vendor’s claims. This is particularly important where sensitive data and processes are involved, and where sensitive material should generally not be flowing through external AI providers. Open systems can be rigorously analyzed by in-house security professionals, fine-tuned on an organizations’s own secure data, modified to produce organization-specific oversight mechanisms, and run entirely within an organization’s own infrastructure, keeping everything behind appropriate firewalls.

## The Path Forward

Attackers will develop models that take advantage of vulnerabilities. A significant part of the answer is leaning into transparent practices: open security reviews, published threat models, shared vulnerability databases, and open tooling that any team can adopt. The alternative of each organization trying to secure itself in isolation with proprietary tools doesn’t scale against attackers who are coordinating and sharing techniques in their own communities.

The future of AI cybersecurity will be shaped less by any single model and more by the ecosystems that surround them. Openness provides defenders with the visibility, the control, the community, and the shared infrastructure to stay ahead.

More Articles from our Blog

llmmoelong-context

## [DeepSeek-V4: a million-token context that agents can actually use](https://huggingface.co/blog/deepseekv4)

burtenshaw

43

April 24, 2026

announcementmlxllm

## [The PR you would have opened yourself](https://huggingface.co/blog/transformers-to-mlx)

pcuenq, awni

68

April 16, 2026
---

## 编译摘要

### 1. 浓缩
- **核心结论1**: Mythos 的威力不在单一模型，而在系统级配方（算力+数据+脚手架+速度+自主性），其他人可构建类似系统
  - 关键证据: 更小的模型+深度安全专业知识可能产生类似结果且更便宜；AI 安全能力呈锯齿状分布
- **核心结论2**: 开放性是网络安全的结构性优势——安全是四阶段速度赛跑（检测→验证→协调→补丁），开放社区天然分布式，闭源方案将所有环节集中在单一供应商形成单点故障
  - 关键证据: Linux kernel security team、OpenSSF 等社区安全专业力量；AI 逆向工程能力使闭源代码的"隐匿安全"保护减弱
- **核心结论3**: 半自主 Agent（非完全自主）是安全防御的最佳平衡点，开放代码使组织可在私有环境中运行和审计
  - 关键证据: Anthropic 自己也 advise against 完全自主；"人类在环"只有在人类能看懂环内发生什么时才有意义

### 2. 质疑
- **关于"开放性优势"的质疑**: 开放社区的决策速度和协调效率可能不如单一供应商——紧急漏洞响应时分布式社区能否快速统一行动？
- **关于"AI 加速漏洞生产"的质疑**: 论文假设错误激励导致 AI 引入更多漏洞，但未提供定量数据；正确激励下 AI 可能反而提升代码质量
- **关于数据可靠性的质疑**: 缺乏开放 vs 闭源安全效果的定量对比，论点更多基于逻辑推演而非实证数据

### 3. 对标
- **跨域关联1**: 此现象类似 Linux vs Windows 的安全辩论——"足够多的眼球"在有 AI 辅助后效果放大
- **跨域关联2**: 半自主 Agent 模式可迁移到其他高风险领域（医疗、金融），开放审计是建立信任的前提

### 关联概念
- [[Cybersecurity-Openness]]
- [[Mythos]]
- [[Cybersecurity-Proof-of-Work]]
