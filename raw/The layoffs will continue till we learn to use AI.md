---
title: "The layoffs will continue till we learn to use AI"
source: "https://x.com/championswimmer/status/2051807284691612099"
author:
  - "[[Arnav-Gupta]]"
published: 2026-05-06
created: 2026-05-11
description: "Somewhere in the upper echelons of my company is a list of 8000 names. There is a 10% chance I am on it. I will get to know in a few days on..."
tags:
  - "clippings"
---
![图像](https://pbs.twimg.com/media/HHl6kyyXsAAEIjS?format=jpg&name=large)

Somewhere in the upper echelons of my company is a list of 8000 names. There is a 10% chance I am on it. I will get to know in a few days on 20 May.

Seeing today's "AI layoffs" announcement by Coinbase, made me consider writing this. Especially before 20 May, because I would love to share my thoughts on this, untainted, by the knowledge of whether I am on the list myself. These thoughts do not depend on whether I am on the list, not are they about (only) my workplace - it is what I am hearing from all my friends in various companies of various mid to large sizes.

A lot of ink has been poured debating whether these new wave of layoffs (largely regarded as to have started with Jack laying off 40% of Square) are really because of AI or are they merely "AI-washing". I'll spare you the trouble of peppering my article with links to all those articles, essays, news pieces but you either have read them already or they just a Google search ChatGPT query away.

## The oft-touted 'AI productivity' and its elusive proof

Does AI make us productive. Ah that loaded question! If we flip that for a second and just say "AI didn't change anything". I think no one, not even the biggest sceptics of AI's impact will agree to that. Especially in tech companies - the skyrocketing usage of AI is something you just cannot ignore. Even the most conservative of places which are putting AI spending caps, not giving AI tools to employees or what not - even there, undeniably some amount of work is being done by AI, even if it is as sad as just using Gemini or Copilot inside their Google or Microsoft Office suite to edit their docs.

In the more forward-looking companies that dove head first into the ocean of AI tokens, the Ubers, Shopifys of the world (I am not counting Metas or Microsofts - which is making their own model, or Vercels or Cloudflares - which is actively building AI infra; just the ones who are purely "users"), the usage has been crazy. 90-100% code being AI generated, to PRs/diffs per week going up 2-5x, to hundreds of millions of dollars in AI budget for the year being eaten up within months - we have seen it all.

And yet, ofcourse the Ed Zitrons, Will Manidis, Gary Marcus and the Michael Burys of the world will also counter you with the question - why have these companies not 2-5xed their revenue then? Why are their apps still almost exactly the same as it was 6 months back? If AI is really all that productive, what are they even producing with it? If they are generating 5x the code, and the end user doesn't even notice it, then what is the point of all that code? And that's a fair question.

## Input, Output, Outcome

We have to take a little Business Administration 101 detour. When your fast growing mid sized overfunded company throwing money at everything finally starts drying out of funds, and some elder CEO who you go to for advice, asks you to get somebody from McKinsey come and have a look at your state of affairs, they start their presentation with a bland white slide with 3 words written in the default Arial font. "Input, Output, Outcome"

They explain to you, what everybody knows, but loves to forget.

Code is an input.

Features are an output.

Users spending money on your product is an outcome.

AI (or at least Claude Enterprise) is a B2B SaaS product. You'll notice that SaaS products are priced and marketed in different ways. If the product directly changes the outcome, they simply take a cut from the outcome. Imagine the sales pitch "our tool closes sales leads 36% faster. try it out for the low fee of 5% of your sales value"

This is an instant sell. Most other variables unchanged, if you were closing 100 leads in 100 days, you now close them in 63 days, freeing up 36 more days to close (if my math is right) 57 more leads! So your sales potentially goes up by 57% You'll be happy to pay 5% of your sales commission to get 57% more revenue any day. And if you don't use the product, you are paying them `$0` anyway.

As you would have predicted where I am going with this - pricing of Claude Code tokens aren't exactly like that. If your software engineers, who are addicted to Claude Code like crack cocaine (I just realised they're both abbreviated to 'cc'), generate 100M tokens a day, you are spending `$100` per day, per engineer, on it.

Even if some of the code they generated was discarded because it didn't work

Even if some more of the code was reverted later because it caused a SEV

Even if yet another share of the code was for internal tools to make dashboards look more cute for the VPs to look at

Because, code is input. And while if the direction is right, more input usually tends to more output, and that tends to more outcome - all of that may or may not hold true when you overnight 5x the input. Your "direction" of input might well suddenly point to random places, and not towards the output or the outcome.

## What is blocking us!

Well, every time the CEO or the PM wanted to do 10 things, the team said they could do only the top 2. There is no time for the rest 8. The explanation? Well coding is not child's play. It takes time to code up complex, working software.

Hmmm.... but code is free now. Why are we not doing those other 8 things?

There are 2 answers, one the CEO & PM will not like, and one the middle management and seniors will not like.

1. **All those 8 ideas were not actually.... any good?** Just because the CEO or the PM had 10 brainfarts, doesn't mean they were all actually going to lead to outcomes. Even 10 new features (outputs) does not guarantee users like all 10 of them and use your app more for it (outcome). In fact the friction of not having enough bandwidth to code, made people debate a lot more and kill bad ideas much sooner before they hogged too much resources, so you filtered for the top 2 much better. Now that writing code is fast and cheap and easy, there is no point even trying to debate the ideas. Even if you decide to push back against them, do you think it will stop the CEO or the PM from spinning up Claude themselves? Yeah so don't even bother trying.
2. **It is a pain to get everyone "aligned"** We know it is. Getting stakeholders to align first "why" we are doing this, and then separately "what" exactly we are doing it, and then once all over again on "how" we are doing it is pain. The more the number of teams, the more the number of projects that get stuck in alignment hell. Writing code being the slow part was hiding this away. Now once the "what" is aligned, overnight someone builds an MVP, and schedules another meeting the very next day. In the meeting, you find out the other team also made an MVP. Yours and theirs work differently based on different assumptions. Sure you can sit together and iron that out, and discuss which of whose assumptions are correct. But let's be serious for a moment. You and your team armed with infinte Claude Code tokens are not going to do that. Nor will the other team. You will go right back into the arms of Claude and ask it to re-implement the other teams' part of the work in the way you think is best, and Claude will say "You're absolutely right" and get right to it!

## What will the layoffs solve?

Well you have been bearing with me telling you mostly obvious things so far. But I know you want me to get to the meat of the story. What will the layoffs achieve? If, as I posit, AI is **not** literally drop-in replacing 30% of the employees. (I think we can agree on this? Although it is better than an entry level white collar worker in many tasks and worse in others - it is not a drop-in replacement, definitely not 10 or 20 or 30% of your company)

The layoffs immensely help with 2 immediate short-term problems which are clear as day.

1. **They offset "AI spending"** I mean, this is just cashflow 101. Surely, you can see that if all your Claude-addicted engineers are blowing up `$100` per day on Claude (which is `$2500` per month, or `$30`k per year), that is clearly worth 1 SDE salary in India, worth 0.5 SDE in EU and worth 0.25 SDE in USA. If you just do the dumbest math possible, assuming every employee is an SDE in a flat org, then you need to remove 50%(India) or 33% (EU) or 20% (USA), to continue to meet the same wage bill, inclusive of token spends. The very fact that AI usage is growing regardless, and revenue is not yet seeing this uptick, this has to happen otherwise the balance sheet of the company goes in disarray. Your entire unit economics of the SDLC goes for a toss - if you spend 50% more in input, with no or little change in outcome. If we did learn to use AI though - and we figured out how 50% more input costs translate to 50% more revenue outcome, we would not need this to happen. But since you didn't learn to use AI, some of you need to leave to make space for Anthropic's salary.
2. **Cut the 'alignment tax'** There is no arguing that any large company, is bigger than it "needs" to be to just survive. That's the whole point. Larger organisations carry organisational fat. That is by design. It is possible for anyone to leave the company, and systems to still continue to work because someone else knew what they did. In big companies, you can go on 6 months parental leaves and things you worked on still keep running. These are good things to have! But this is also proof that if some percentage of people were removed, things will not shut down immediately. In fact, maybe with few weeks of initial system shock, for the next few months, things will get faster! Remember how the two teams above didn't agree to each other's approaches? Well if you just layoff one of those teams and asked the other one to pull a few all nighters and do their job instead - they have no one to align with. We don't know what happens long term (or as Keynes said - "in the long term we are all dead"), but in the short term, cutting off 10-20% people in a big org, only makes things faster. Large organisations, over time, invariably build up slack, build up redundancies, and build up 'org debt' just like tech debt. It is the nature of big organisations, and cutting 10% people today doesn't prevent it from happening again in 2 years time. But when you see everyone saying they are generating 5x more diffs, but unable to ship because **they are blocked** by other teams, at least the most immediate solution does look like removing people so that there is fewer people to block each other.

## These are AI layoffs, even if AI is not replacing you

Is your employee id being replaced by a new instance of Claude running on VM? We know that is not what is happening.

That said, are there many different workflows in the company that were once done by someone hitting keyboard keys and mouse clicks on tools like VS Code, Figma, Canva, Google Docs, and today is basically someone else (who needed that work from you) just yelling a prompt into an LLM instead of bothering to ask you for it? That is true as well.

Are these layoffs "AI-washing"? By which we mean - are there fundamental problems with the company regardless of AI (overhiring, diminishing profits, competitor pressure, bad business decisions) and AI being used as an 'excuse' to lay people off? Well that's somewhat true too.

And you'll also notice that over a period if you collect all these "layoff emails" from CEOs you'll almost feel they are all in the same Whatsapp group writing these emails together. **AI-native pods**, **managers writing code, more reports for managers, flat hierarchy, managing a team of agents**, you'll read those exact same terms in all their emails. Almost as if they all gave GPT the same prompt.

But the truth is that these layoffs, even if they they are not because AI is replacing you you, and even if they are some form of AI-washing. These layoffs are still because of AI. And these layoffs will continue till we learn to use AI. Till we learn to convert AI-tokens into outcomes and not just input. Till we learn to re-align the speed of "alignment" with the new speed of coding. And till we figure out, beyond our 2 good and 8 stupid ideas, 10 more ideas that we can chase with our increased productivity.

Till we figure out how the GDP of the world actually grows because of AI, we have to offset the `$70` B (combined OAI/Ant enterprise revenue) of annual token spend by cutting some salaries. And till we figure out how to unblock each other faster, we can always be removed from the org chart itself.

I'll know more about my own fate in 15 days. But either way, I think I know why. And even if I were in the corner office making the decisions, I don't even know if I would have or could have done any better, or just did what everyone else in the CEO WhatsApp group is doing.

---

## 编译摘要

### 1. 浓缩
- **核心结论1**: AI 裁员的本质不是"AI 替代人"，而是"AI 提升输入成本但未提升结果"——企业需要裁员来抵消 AI 支出
  - 关键证据: 每位工程师每天消耗 `$100` Claude tokens（`$30`k/年），相当于印度 1 名 SDE 的薪资；代码生成量 5 倍增长但用户感知的产品几乎未变
- **核心结论2**: 大型组织的"对齐税"被 AI 暴露——代码变便宜后，跨团队协调成为真正的瓶颈
  - 关键证据: 传统模式下 CEO 想做 10 件事团队只做前 2 件（自然筛选），AI 模式下两个团队各自做出 MVP 但假设冲突，无人愿意对齐
- **核心结论3**: 裁员短期内有效——减少 AI 支出 + 减少对齐人数——但长期无法阻止组织债务重新累积
  - 关键证据: 大型组织天然积累冗余和组织债务，裁员不解决组织结构和目标清晰度的根本问题

### 2. 质疑
- **关于"AI 提升输入但不提升结果"的质疑**: 该结论以软件产品公司为前提——在某些场景（如代码本身就是可交付物的开源项目），输入提升即价值提升
- **关于"裁员减少对齐税"的质疑**: 裁员只是将对齐成本从显性（多人协调）转为隐性（单人承担全部上下文），长期可能增加单人认知负荷
- **关于数据可靠性的质疑**: `$100`/天/token 成本的数据来源未明确，且不同模型、不同使用模式的成本差异巨大

### 3. 对标
- **跨域关联1**: Input-Output-Outcome 框架类似制造业的"产量-良率-利润"模型——提升产量不等于提升利润，良率（=方向正确性）才是关键
- **跨域关联2**: 对齐税与 [[Organizational-Shape-Moat]] 关联——组织形态决定了对齐税的大小，这是 AI 时代的结构性护城河

### 关联概念
- [[Knowledge-Work]]
- [[AI-Capability-Gap]]
- [[Organizational-Shape-Moat]]
- [[Allocation-Economy]]
