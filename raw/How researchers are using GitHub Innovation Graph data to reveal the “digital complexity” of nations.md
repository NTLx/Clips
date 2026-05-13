---
title: "How researchers are using GitHub Innovation Graph data to reveal the 'digital complexity' of nations"
source: "https://github.blog/news-insights/policy-news-and-insights/how-researchers-are-using-github-innovation-graph-data-to-reveal-the-digital-complexity-of-nations/"
author:
  - "[[Kevin-Xu]]"
published: 2026-05-08
created: 2026-05-09
description: "Researchers share in an interview how they used GitHub data to predict GDP, inequality, and emissions in ways that traditional economic data misses."
tags:
  - "clippings"
---
One of our goals for the GitHub Innovation Graph was to facilitate research on the economic impact of open source software and developer collaboration. In a paper recently published by [Research Policy](https://doi.org/10.1016/j.respol.2026.105422), four researchers used Innovation Graph data to do just that. I’m happy to share an interview with these researchers, along with our Q4 2025 data release.

The Research Policy paper examines whether the geography of open-source software production on GitHub can reveal the “digital complexity” of nations, and whether that complexity predicts GDP, inequality, and emissions in ways that traditional economic data misses.

Meet the four researchers:

- **Sándor Juhász** is a research fellow at the Corvinus University of Budapest. His work focuses on economic geography, knowledge networks, and how spatial structures shape innovation.
- **Johannes Wachs** is an Associate Professor at Corvinus University of Budapest, Director of the [Center for Collective Learning](https://centerforcollectivelearning.org/) at the Corvinus Institute of Advanced Study, and a researcher at the Complexity Science Hub in Vienna. His work sits at the intersection of computational social science and economic geography, with a particular focus on open-source software communities.
- **Jermain Kaminski** is an Assistant Professor at the School of Business and Economics at Maastricht University. His research specializes in entrepreneurship, strategy, and causal machine learning, with a focus on how data-driven methods can improve decision-making and innovation. He is a cofounder of the [Causal Data Science Meeting](https://causalscience.org/).
- **César A. Hidalgo** is a professor at the Toulouse School of Economics and Corvinus University of Budapest, and he is the Director of the [Center for Collective Learning.](https://centerforcollectivelearning.org/) He is also the creator of the [Observatory of Economic Complexity](https://oec.world/) and cofounder of [DataWheel](https://www.datawheel.us/).

## Research Q&A

**Kevin:** Thanks so much for chatting, everyone! Could you give a quick high-level summary of the paper for our readers here?

**Sándor:** For the last fifteen years or so, economists have been measuring the complexity of national economies by looking at what physical products countries export, what patents they file, and what research they publish. These measures turn out to be remarkably good at predicting which countries will grow, which have high inequality, amongst many other macroeconomic features. But they all have a massive blind spot: software.

**Jermain:** Code doesn’t go through customs. It crosses borders through “ `git push` ”, cloud services, and package managers. So all that productive knowledge was essentially invisible, what some colleagues have called the “digital dark matter” of the economy. We decided to fix that using the GitHub Innovation Graph, which tracks how many developers in each economy push code in each programming language, based on IP addresses. We applied the Economic Complexity Index (ECI) to this data. The bottom line is that software ECI surfaces new information that trade flows, patents, and research data partly leave on the table. In particular, software ECI helps explain variation in GDP per capita and income inequality even after you control for all the traditional measures.

**Johannes:** We also found that countries don’t jump randomly between software specializations. They diversify into technology stacks that are related to what they already do, just like countries in the physical economy tend to move into products similar to what they already export. This is considered the “principle of relatedness,” and it holds for software too.

**Kevin:** Interesting! Could you provide an overview of the methods you used in your analysis?

**Johannes:** Sure. As mentioned, the core data comes from the GitHub Innovation Graph, which gives us quarterly counts of developers pushing code by economy and programming language for 163 economies and 150 languages from 2020 to 2023. But individual programming languages aren’t really the right unit, most real software uses bundles of languages together. A web app might combine HTML, CSS, and JavaScript; a data science project uses Python and Jupyter Notebook; systems programming pairs C with Assembly.

**Sándor:** So we built a separate dataset by querying the GitHub GraphQL API for all repositories active in 2024 to find which languages co-occur within the same repos. We computed cosine similarity between languages based on weighted co-occurrence, with a normalization scheme so that polyglot repos with twenty languages don’t dominate the signal, and then applied hierarchical clustering to group the 150 languages into 59 “software bundles.” Each bundle represents a coherent technology stack.

**Jermain:** …and from there, it’s the “standard” economic complexity pipeline. We build a country-by-bundle matrix, compute revealed comparative advantage, essentially asking, “does this country have a disproportionate share of developers in this bundle relative to the global average?”, binarize it, and then apply the iterative method to compute the Economic Complexity Index. Countries that specialize in many non-ubiquitous bundles score high, and countries that only specialize in things everyone does score low. For the relatedness analysis, we define proximity between bundles using co-specialization patterns. If countries that are good at bundle A also tend to be good at bundle B, those bundles are close in the software space. Then we test whether countries are more likely to enter bundles that are close to their existing specializations.

**Kevin:** Nice! Follow-up question: could you provide an “explain it like I’m five” overview of the methods you used in your analysis?

**César:** Think of countries like kitchens. Some kitchens can cook anything, since they have an abundance of ingredients and tools, from the rarest spices to the best knives. Others are more limited. Maybe they can boil rice and do a few other simple things. Since we cannot look at the kitchens directly, we need to infer their “complexity” based on the dishes they are able to produce. This is what the economic complexity index or ECI allows you to estimate. We can infer what’s going on in the kitchen by seeing if it is a chicken and rice operation, or a place that can produce sophisticated edible foams and souffles. Originally, these methods were applied to trade data, where the dishes coming out of the kitchen were a country’s exports, but in this paper, we applied that to software. A chicken-and-rice country is a Python and JavaScript country. A Michelin-star country is one that can program certified embedded systems for aerospace and defense.

### Top 20 economies by software economic complexity

| **Ranking** | **Economy** | **Software ECI** |
| --- | --- | --- |
| 1 | Germany | 1.739 |
| 2 | Australia | 1.730 |
| 3 | Canada | 1.729 |
| 4 | Netherlands | 1.727 |
| 5 | France | 1.702 |
| 6 | United States | 1.695 |
| 7 | Poland | 1.691 |
| 8 | United Kingdom | 1.687 |
| 9 | Italy | 1.672 |
| 10 | Sweden | 1.620 |
| 11 | Switzerland | 1.620 |
| 12 | Hong Kong SAR | 1.595 |
| 13 | Norway | 1.571 |
| 14 | Japan | 1.552 |
| 15 | Spain | 1.552 |
| 16 | Russia | 1.530 |
| 17 | Singapore | 1.468 |
| 18 | Taiwan | 1.464 |
| 19 | Belgium | 1.448 |
| 20 | Finland | 1.444 |

**Kevin:** Thanks, that’s super helpful. I’d be curious about the limitations of your paper and data that you wished you had for further work. What would the ideal datasets look like for you?

**Johannes:** One major drawback is that we only see *public* GitHub activity. That means we’re missing proprietary software entirely. Hence, we can’t see closed-source enterprise work, which is huge. So our measure likely *underestimates* software complexity in countries with a weaker open source software culture.

**Sándor:** The time window is another constraint. Four years of data (2020–2023) is enough for cross-sectional analysis but too short to credibly test long-run growth predictions, which is what economic complexity measures are really designed for. Economic structures shift over decades, not quarters. We’d love to have twenty years of this data.

**Jermain:** The dream dataset would combine GitHub-like activity data with information about the *projects* themselves, not just languages, but frameworks, libraries, and what the software actually does. Considering this dimension would be a natural next step for our project, and it would shed more light into software bundles and use cases. If we knew that a repo was building a fintech application versus a game engine, we could define much finer-grained capability bundles. *GitHub Topics* gives us a taste of this, and we used it as a robustness check, but it’s still noisy and incomplete.

**Kevin:** Do you have any predictions for the future? Recommendations for policymakers? Recommendations for developers?

**César:** Software is an interesting target for industrial policy because it is an industry that depends primarily on highly movable human capital (software developers). In principle, it provides an opportunity for development that can be incentivized via talent attraction programs. In practice, however, the high mobility of software talent can be a double-edged sword, since that makes it sensitive to consumer protection regulations that make it hard to work with data or worker protection schemes that distribute the risk of innovation to small and medium size firms (e.g. laws that on paper protect workers, but that in reality pass on that responsibility to the firms). The countries that figure out how to attract software talent without suffocating it with well-intentioned but poorly designed regulation will pull ahead.

**Johannes:** For developers, understanding that places are highly specialized in the kind of software they produce is useful when they are looking to relocate. Developers can use the product space representation of software capabilities to know which countries their skillsets are a good match for.

**Jermain:** Looking ahead, the big question is what generative AI does to this picture. If AI coding assistants lower the barrier to working in new programming languages, does relatedness weaken? Do countries diversify faster? Or does it reinforce existing advantages because the countries with the best AI infrastructure benefit most? We’re working on this, and Johannes and his colleagues have a new paper in [Science](https://www.science.org/doi/10.1126/science.adz9311) on tracking the global diffusion of AI-assisted coding on GitHub. I think the answer will reshape how we think about digital complexity within the next five years. One further consideration would be how classifications of software or software bundles would be represented as [NAICS](https://www.census.gov/naics/) or [NACE](https://ec.europa.eu/competition/mergers/cases/index/nace_all.html) industry codes.

**Sándor:** I’d add a prediction: I think we’ll see economic complexity indices based on software data become a standard part of the policymaker’s toolkit within the decade, sitting right alongside the trade-based measures. The data is open, it updates quarterly, and it captures something that traditional data genuinely can’t.

## Personal Q&A

**Kevin:** I’d like to change gears a bit to chat more about your personal stories. Johannes, I understand that you have a background in computational social science and network science, which is a bit different from the traditional economics path. Tell us more about your path to research.

**Johannes:** I actually started in mathematics and then moved into computational social science during my PhD at Central European University in Budapest. I became enchanted by the opportunities that digital data traces present for studying human behavior. I like using network methods because they help us move between the micro level activity and interactions found in such traces and the macro outcomes. I stumbled into open source research in particular when I realized that GitHub data was this incredibly rich, publicly available record of valuable knowledge production that few people were using to study social science questions.

**Kevin:** Sándor, I see you have a background in economic geography, which is a more traditional route compared to computational social science. What was your path toward working with software data?

**Sandor:** I received my PhD in economic geography at Utrecht University, in a research community that was already using economic complexity to study regional development. So I was trained in thinking about places—cities, regions, industries—through the lens of networks and capability accumulation.

**Kevin:** Jermain, it looks like you developed practical technical expertise through some entrepreneurial projects in parallel with academic training.

**Jermain**: During my PhD at RWTH Aachen, I was a visiting researcher with Cèsar at MIT. In that time, I was also working with a colleague on a project called Moviegalaxies.com (open data) and later worked on analyzing text, speech and video data in Kickstarter projects. It was my first multimodal machine learning pipeline. From my network analysis projects, I somehow ended up analyzing passing networks for a larger German soccer team. These days my research is mostly concerned with causality and causal machine learning. In this capacity, I co-founded the Causal Data Science meeting with my colleague Paul Hünermund.

**Kevin:** César, do I have right that you have a background in Physics?

**César:** I started in physics, with a PhD at Notre Dame focused on complex networks. During that time, I realized that network tools could be used to describe the evolution and fate of economies. Eventually, this became a field that we know today as economic complexity, which studies the process of economic development by using tools from physics, economics, and computer science.

**Kevin:** Finding a niche that you’re passionate about is such a joy, and I’m curious about how you’ve found living in that niche. What’s the day-to-day like for you?

**Johannes:** Honestly, in research, the day-to-day is a mix of writing code, writing papers, and talking to people, then iterating. Of course, working at a university usually comes with teaching and administration, too. I like that I have a good amount of freedom in what I choose to work on. If a project or direction doesn’t spark joy, I can usually shift my focus. That is a unique thing.

**Sándor:** I’d add that one of the best parts of this niche is the interdisciplinary community. On any given week I might talk to an economic geographer, a computer scientist, and a physicist about the same research question. That’s unusual and very stimulating.

**Kevin:** Have things changed since generative AI tooling came along? Have you found generative AI tools to be helpful?

**Johannes:** Absolutely. We use LLM tools regularly now for things like debugging data pipelines, drafting boilerplate code, and even sanity-checking statistical approaches. It’s particularly useful in a project like where you have a lot of different methods and need to coordinate work in a team. That said, LLMs are much more helpful if you already have a clear idea in mind.

**Kevin:** Do you have any advice for folks who are starting out in software engineering or research? What tips might you give to a younger version of yourself, say, from 10 years ago?

**César:** The key is to invest in things that grow or compound. This is easier said than done because there are always distractions and temptations. I’ve seen many scholars spend months or years working on projects just because they don’t want to lose the work that they’ve already put into them. The cost of doing that is working on other projects that might matter more in ten or twenty years. Building tools that can generate an audience, like [The Observatory of Economic Complexity](https://oec.world/), [Data USA](https://datausa.io/), or [Pantheon](https://pantheon.world/), was challenging, but they have borne fruit for a long time. The same is true about working on a few important papers or completing a book. The question you need to ask when working on a project is whether you honestly believe that the project will be more important in a decade from now than today. If the answer is yes, that’s probably a good project. Ten years ago, I would have told myself to trust that test more and to walk away from “almost done” projects faster. Sunk costs are the most expensive thing in a research career.

**Johannes:** In can rather make suggestions for young researchers. The first is to build a broad question and research agenda to motivate what you do. You have to have a problem you care about so much that even partial or highly specific results about that problem get you excited. Once you have that, in practice I think there is a lot of value in generating your own data. I prefer applying a straightforward method to a bespoke dataset than applying a highly complex method to a dataset everyone knows.

**Jermain:** My advice echoes César’s: don’t ride a dead horse. In the years after the PhD and into assistant professorship, it’s tempting to keep milking old topics while pivoting to new ones, but this leaves you straddling two worlds and mastering neither. Pick your focus deliberately, narrow enough to build real expertise, broad enough to stay curious, and be willing to let go of past work that no longer aligns, even if it feels wasteful.

**Sándor:** I’d tell my younger self to collaborate more and earlier. This paper has four authors across five institutions in four countries. That wouldn’t have happened if any of us had stayed in our silos. Go to conferences outside your field, say yes to coffee meetings with people whose work seems tangentially related, and don’t be afraid to cold-email researchers whose work you admire.

**Kevin:** Are there any learning resources you might recommend to someone interested in learning more about this space?

**César:** The [Observatory of Economic Complexity](https://oec.world/), for a web experience, and [The Infinite Alphabet: and The Laws of Knowledge](https://www.amazon.com/Infinite-Alphabet-Laws-Knowledge/dp/0241655676), for a book that puts this in context.

**Jermain:** If you’re a developer curious about the economics angle, I’d honestly just recommend browsing the [Observatory of Economic Complexity](https://oec.world/) and looking up your own country. See what it exports, where it sits in the product space, and then think about how software fits in. It’s a very intuitive way to build the intuition before diving into the math.

**Kevin:** Thank you, Sándor, Johannes, Jermain, and César! It’s been fascinating to learn about your current work and broader career trajectories. We truly appreciate you taking the time to speak with us and will absolutely keep following your work.

---

## 编译摘要

### 1. 浓缩
- **核心结论1**: 软件生产在传统经济统计中完全隐形（"数字暗物质"），GitHub Innovation Graph 首次使这部分知识可见
  - 关键证据: 代码不经过海关，通过 git push/云服务/包管理器跨境流动，无贸易/专利/论文记录
- **核心结论2**: 将经济复杂度指数 (ECI) 应用于 GitHub 数据后，软件 ECI 能解释传统指标遗漏的 GDP 和不平等变异
  - 关键证据: 控制贸易/专利/论文指标后，Software ECI 仍能额外解释 GDP per capita 和收入不平等差异；Top 5 为德国、澳大利亚、加拿大、荷兰、法国
- **核心结论3**: 软件领域存在"相关性原则"——国家向与现有能力相关的技术栈多样化，而非随机跳跃
  - 关键证据: 基于共专业化模式定义软件束间邻近度，验证国家进入新模式的概率与现有专长的邻近度正相关

### 2. 质疑
- **关于"软件 ECI 预测 GDP"的质疑**: 仅基于公开 GitHub 活动，企业闭源软件完全缺失——这可能系统性低估美国（企业软件巨头集中）的真实复杂度
- **关于"相关性原则"的质疑**: 4 年窗口期（2020-2023）横跨疫情，远程工作爆发可能扭曲了正常的软件专业化模式
- **关于数据可靠性的质疑**: 语言聚类为 59 个"软件束"的方法依赖 2024 年活跃仓库，但主体分析用的是 2020-2023 数据，存在时间不一致

### 3. 对标
- **跨域关联1**: "数字暗物质"隐喻类似 [[Knowledge-Work|知识工作]] 的度量困境——AI 时代的知识产出同样难以用传统指标捕捉
- **跨域关联2**: ECI 方法论可迁移到 AI 模型能力评估——哪些国家/机构能组合"非泛在"的 AI 能力组合

### 关联概念
- [[Software-Economic-Complexity]]
- [[Digital-Dark-Matter]]
- [[Kevin-Xu]]
