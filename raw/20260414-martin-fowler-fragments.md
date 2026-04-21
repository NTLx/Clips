---
type: raw
source: "https://www.martinfowler.com/fragments/2026-04-14.html"
author:
  - "Martin Fowler"
published: "2026-04-14"
created: "2026-04-20"
tags:
  - clippings
  - AI
  - TDD
  - Software-Engineering
---
I attended the first Pragmatic Summit early this year, and while there host [Gergely Orosz interviewed Kent Beck and myself on stage](https://www.youtube.com/watch?v=CZs8J1ZD0CE). The video runs for about half-an-hour.

[![A photo of Gergely, Kent, and myself on the stage. We are all bedazzled by the vibrancy of Kent's trousers](https://www.martinfowler.com/img/catalog/2026-prag-summit.png)](https://www.youtube.com/watch?v=CZs8J1ZD0CE)

I always enjoy nattering with Kent like this, and Gergely pushed into some worthwhile topics. Given the timing, AI dominated the conversation - we compared it to earlier technology shifts, the experience of agile methods, the role of TDD, the danger of unhealthy performance metrics, and how to thrive in an AI-native industry.

❄ ❄ ❄ ❄ ❄

Perl is a language I used a little, but never loved. However the definitive book on it, by its designer Larry Wall, contains a wonderful gem. The three virtues of a programmer: hubris, impatience - and above all - *laziness*.

Bryan Cantrill [also loves this virtue](https://bcantrill.dtrace.org/2026/04/12/the-peril-of-laziness-lost/):

> Of these virtues, I have always found laziness to be the most profound: packed within its tongue-in-cheek self-deprecation is a commentary on not just the need for abstraction, but the aesthetics of it. Laziness drives us to make the system as simple as possible (but no simpler!) — to develop the powerful abstractions that then allow us to do much more, much more easily.
> 
> Of course, the implicit wink here is that it takes a lot of work to be lazy

Understanding how to think about a problem domain by building abstractions (models) is my favorite part of programming. I love it because I think it’s what gives me a deeper understanding of a problem domain, and because once I find a good set of abstractions, I get a buzz from the way they make difficulties melt away, allowing me to achieve much more functionality with less lines of code.

Cantrill worries that AI is so good at writing code, we risk losing that virtue, something that’s reinforced by brogrammers bragging about how they produce thirty-seven thousand lines of code a day.

> The problem is that LLMs inherently lack the virtue of laziness. Work costs nothing to an LLM. LLMs do not feel a need to optimize for their own (or anyone’s) future time, and will happily dump more and more onto a layercake of garbage. Left unchecked, LLMs will make systems larger, not better — appealing to perverse vanity metrics, perhaps, but at the cost of everything that matters. As such, LLMs highlight how essential our human laziness is: our finite time forces us to develop crisp abstractions in part because we don’t want to waste our (human!) time on the consequences of clunky ones. The best engineering is always borne of constraints, and the constraint of our time places limits on the cognitive load of the system that we’re willing to accept. This is what drives us to make the system simpler, despite its essential complexity.

This reflection particularly struck me this Sunday evening. I’d spent a bit of time making a modification of how my music playlist generator worked. I needed a new capability, spent some time adding it, got frustrated at how long it was taking, and wondered about maybe throwing a coding agent at it. More thought led to realizing that I was doing it in a more complicated way than it needed to be. I was including a facility that I didn’t need, and [by applying yagni](https://martinfowler.com/bliki/Yagni.html), I could make the whole thing much easier, doing the task in just a couple of dozen lines of code.

If I had used an LLM for this, it may well have done the task much more quickly, but would it have made a similar over-complication? If so would I just shrug and say LGTM? Would that complication cause me (or the LLM) problems in the future?

❄ ❄ ❄ ❄ ❄

Jessica Kerr (Jessitron) has a simple example of [applying the principle of Test-Driven Development to prompting agents](https://jessitron.com/2026/04/06/adding-correctness-conditions-to-code-changes/). She wants all updates to include updating the documentation.

> Instructions – We can change AGENTS.md to instruct our coding agent to look for documentation files and update them.
> 
> Verification – We can add a reviewer agent to check each PR for missed documentation updates.
> 
> This is two changes, so I can break this work into two parts. Which of these should we do first?

Of course my initial comment about TDD answers that question

❄ ❄ ❄ ❄ ❄

Mark Little prodded an old memory of mine as he wondered about to work with AIs that are over-confident of their knowledge and thus prone to make up answers to questions, or to act when they should be more hesitant. He draws inspiration from an old, low-budget, but classic SciFi movie: [Dark Star](https://en.wikipedia.org/wiki/Dark_Star_\(film\)). I saw that movie once in my 20s (ie a long time ago), but I still remember the crisis scene where a crew member has to use [philosophical argument to prevent a sentient bomb from detonating](https://www.youtube.com/watch?v=S-xUjmJkO8g).

> Doolittle: You have no absolute proof that Sergeant Pinback ordered you to detonate.  
> Bomb #20: I recall distinctly the detonation order. My memory is good on matters like these.  
> Doolittle: Of course you remember it, but all you remember is merely a series of sensory impulses which you now realize have no real, definite connection with outside reality.  
> Bomb #20: True. But since this is so, I have no real proof that you’re telling me all this.  
> Doolittle: That’s all beside the point. I mean, the concept is valid no matter where it originates.  
> Bomb #20: Hmmmm….  
> Doolittle: So, if you detonate…  
> Bomb #20: In nine seconds….  
> Doolittle: …you could be doing so on the basis of false data.  
> Bomb #20: I have no proof it was false data.  
> Doolittle: You have no proof it was correct data!  
> Bomb #20: I must think on this further.  

Doolittle has to expand the bomb’s consciousness, teaching it to doubt its sensors. [As Little puts it:](https://markclittle.blogspot.com/2026/03/dark-star-and-ai-morality.html)

> That’s a useful metaphor for where we are with AI today. Most AI systems are optimised for decisiveness. Given an input, produce an output. Given ambiguity, resolve it probabilistically. Given uncertainty, infer. This works well in bounded domains, but it breaks down in open systems where the cost of a wrong decision is asymmetric or irreversible. In those cases, the correct behaviour is often deferral, or even deliberate inaction. But inaction is not a natural outcome of most AI architectures. It has to be designed in.

In my more human interactions, I’ve always valued doubt, and distrust people who operate under undue certainty. Doubt doesn’t necessarily lead to indecisiveness, but it does suggest that we include the risk of inaccurate information or faulty reasoning into decisions with profound consequences.

> If we want AI systems that can operate safely without constant human oversight, we need to teach them not just how to decide, but when not to. In a world of increasing autonomy, restraint isn’t a limitation, it’s a capability. And in many cases, it may be the most important one we build.

---

## 编译摘要

### 1. 浓缩

- **核心结论1**: 程序员的"懒惰"美德（Larry Wall）是驱动抽象和简化设计的核心动力——AI 缺乏此美德，倾向于过度膨胀代码
  - 关键证据: "The problem is that LLMs inherently lack the virtue of laziness. Work costs nothing to an LLM... LLMs will make systems larger, not better"

- **核心结论2**: AI 系统过度优化" decisiveness"，缺乏"克制"（Restraint）——在错误代价不对称的场景中，正确的行为是"延迟行动或不行动"，但这需要被"设计进去"
  - 关键证据: "Inaction is not a natural outcome of most AI architectures. It has to be designed in"

- **核心结论3**: TDD 原则可应用于 Agent 编程——先写验证规则（Verification），再写指令（Instructions），而非反向
  - 关键证据: Jessica Kerr "This is two changes, so I can break this work into two parts. Which of these should we do first? ... my initial comment about TDD answers that question"

### 2. 质疑

- **关于"结论1"的质疑**: 懒惰美德的前提是"人类时间有限"，AI 时间（tokens）虽便宜但非无限；若 tokens 成本上升，AI 是否会"被迫懒惰"？
- **关于"结论2"的质疑**: Dark Star 隐喻是否过于悲观？AI 的过度自信可能是能力限制而非设计缺陷；随着模型能力提升，过度自信可能减少
- **关于数据可靠性的质疑**: Martin Fowler 的个人体验（playlist generator）样本量为 1；Bryan Cantrill 和 Mark Little 的观点是博客评论而非研究

### 3. 对标

- **跨域关联1**: 懒惰美德类似经济学中的"稀缺驱动效率"——人类时间稀缺 → 追求简化；AI 时间充裕 → 无需简化
- **跨域关联2**: AI Restraint 类似管理学中的"战略耐心"——不是所有决策都需要立即行动，克制是一种高级能力

### 概念更新建议

- **新增 Entity**: [[Laziness-Virtue]]（程序员三美德中的懒惰）
- **新增 Entity**: [[AI-Restraint]]（AI 克制能力）
- **新增 Entity**: [[Martin-Fowler]]（作者）
- **更新 [[Agentic-Engineering]]**: 补充 TDD-for-Agents 方法

## 关联概念

- [[Martin-Fowler]]
- [[Laziness-Virtue]]
- [[AI-Restraint]]
- [[Agentic-Engineering]]
- [[TDD]]