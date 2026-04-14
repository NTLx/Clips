---
title: "What is agentic engineering? - Agentic Engineering Patterns"
source: "https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering/"
author:
  - "[[Simon-Willison]]"
published:
created: 2026-04-10
description: "What is agentic engineering? - Agentic Engineering Patterns"
tags:
  - "clippings"
---
## What is agentic engineering?

I use the term **agentic engineering** to describe the practice of developing software with the assistance of coding agents.

What are **coding agents**? They're agents that can both write and execute code. Popular examples include [Claude Code](https://code.claude.com/), [OpenAI Codex](https://openai.com/codex/), and [Gemini CLI](https://geminicli.com/).

What's an **agent**? Clearly defining that term is a challenge that has frustrated AI researchers since [at least the 1990s](https://simonwillison.net/2024/Oct/12/michael-wooldridge/) but the definition I've come to accept, at least in the field of Large Language Models (LLMs) like GPT-5 and Gemini and Claude, is this one:

**Agents run tools in a loop to achieve a goal**

The "agent" is software that calls an LLM with your prompt and passes it a set of tool definitions, then calls any tools that the LLM requests and feeds the results back into the LLM.

For coding agents, those tools include one that can execute code.

You prompt the coding agent to define a goal. The agent then generates and executes code in a loop until that goal has been met.

Code execution is the defining capability that makes agentic engineering possible. Without the ability to directly run the code, anything output by an LLM is of limited value. With code execution, these agents can start iterating towards software that demonstrably works.

## Agentic engineering

Now that we have software that can write working code, what is there left for us humans to do?

The answer is *so much stuff*.

Writing code has never been the sole activity of a software engineer. The craft has always been figuring out *what* code to write. Any given software problem has dozens of potential solutions, each with their own tradeoffs. Our job is to navigate those options and find the ones that are the best fit for our unique set of circumstances and requirements.

Getting great results out of coding agents is a deep subject in its own right, especially now as the field continues to evolve at a bewildering rate.

We need to provide our coding agents with the tools they need to solve our problems, specify those problems in the right level of detail, and verify and iterate on the results until we are confident they address our problems in a robust and credible way.

LLMs don't learn from their past mistakes, but coding agents can, provided we deliberately update our instructions and tool harnesses to account for what we learn along the way.

Used effectively, coding agents can help us be much more ambitious with the projects we take on. Agentic engineering should help us produce more, better quality code that solves more impactful problems.

## Isn't this just vibe coding?

The term "vibe coding" was [coined by Andrej Karpathy](https://twitter.com/karpathy/status/1886192184808149383) in February 2025 - coincidentally just three weeks prior to the original release of Claude Code - to describe prompting LLMs to write code while you "forget that the code even exists".

Some people extend that definition to cover any time an LLM is used to produce code at all, but I think that's a mistake. Vibe coding is more useful in its original definition - we need a term to describe unreviewed, prototype-quality LLM-generated code that distinguishes it from code that the author has brought up to a production ready standard.

## About this guide

Just like the field it attempts to cover, *Agentic Engineering Patterns* is very much a work in progress. My goal is to identify and describe patterns for working with these tools that demonstrably get results, and that are unlikely to become outdated as the tools advance.

I'll continue adding more chapters as new techniques emerge. No chapter should be considered finished. I'll be updating existing chapters as our understanding of these patterns evolves.

[Writing code is cheap now](https://simonwillison.net/guides/agentic-engineering-patterns/code-is-cheap/) →

**Chapters in this guide**

1. **Principles**
	1. **What is agentic engineering?**
		2. [Writing code is cheap now](https://simonwillison.net/guides/agentic-engineering-patterns/code-is-cheap/)
		3. [Hoard things you know how to do](https://simonwillison.net/guides/agentic-engineering-patterns/hoard-things-you-know-how-to-do/)
		4. [AI should help us produce better code](https://simonwillison.net/guides/agentic-engineering-patterns/better-code/)
		5. [Anti-patterns: things to avoid](https://simonwillison.net/guides/agentic-engineering-patterns/anti-patterns/)
2. **Working with coding agents**
	1. [How coding agents work](https://simonwillison.net/guides/agentic-engineering-patterns/how-coding-agents-work/)
		2. [Using Git with coding agents](https://simonwillison.net/guides/agentic-engineering-patterns/using-git-with-coding-agents/)
		3. [Subagents](https://simonwillison.net/guides/agentic-engineering-patterns/subagents/)
3. **Testing and QA**
	1. [Red/green TDD](https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/)
		2. [First run the tests](https://simonwillison.net/guides/agentic-engineering-patterns/first-run-the-tests/)
		3. [Agentic manual testing](https://simonwillison.net/guides/agentic-engineering-patterns/agentic-manual-testing/)
4. **Understanding code**
	1. [Linear walkthroughs](https://simonwillison.net/guides/agentic-engineering-patterns/linear-walkthroughs/)
		2. [Interactive explanations](https://simonwillison.net/guides/agentic-engineering-patterns/interactive-explanations/)
5. **Annotated prompts**
	1. [GIF optimization tool using WebAssembly and Gifsicle](https://simonwillison.net/guides/agentic-engineering-patterns/gif-optimization/)
6. **Appendix**
	1. [Prompts I use](https://simonwillison.net/guides/agentic-engineering-patterns/prompts/)

Created: 15th March 2026  
Last modified: 16th March 2026  
[10 changes](https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering/changes/)

**Next:** [Writing code is cheap now](https://simonwillison.net/guides/agentic-engineering-patterns/code-is-cheap/)

## 编译摘要

### 1. 浓缩
- **核心结论1**: Agentic engineering 是"在 coding agents 协助下开发软件"的实践
  - 关键证据: Coding agents 是能写能执行代码的代理（如 Claude Code、OpenAI Codex、Gemini CLI）
- **核心结论2**: Agent 的核心定义——"循环调用工具达成目标"
  - 关键证据: Agent 调用 LLM，传递工具定义，执行 LLM 请求的工具，将结果反馈给 LLM
- **核心结论3**: 代码执行是让 agentic engineering 成为可能的关键能力
  - 关键证据: 没有直接运行代码的能力，LLM 输出的价值有限；有代码执行能力，代理可以迭代出真正可工作的软件
- **核心结论4**: Vibe coding 是特指"未审查的原型质量代码"——与生产就绪代码有本质区别
  - 关键证据: Andrej Karpathy 2025年2月提出这个词，描述"忘记代码存在"的提示方式

### 2. 质疑
- **关于"代理不学习过去错误"的质疑**: 如果 LLM 不从错误中学习，如何积累经验？是否完全依赖人类的指令更新？
- **关于"vibe coding"定义扩展的质疑**: 将任何 LLM 生成代码都叫 vibe coding 是否有害？是否模糊了质量标准？

### 3. 对标
- **跨域关联1**: 类似"软件工程"到"AI 辅助软件工程"——从完整控制到意图指导
- **跨域关联2**: 类似"自动驾驶分级"——L0 完全人到 L5 完全 AI，有渐进过渡

### 关联概念
- [[Agentic-Engineering]]
- [[Coding-Agents]]
- [[Vibe-Coding]]

current
