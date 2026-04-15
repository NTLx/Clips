---
title: "一篇文章卖了20万，开源CC+Obsidian打造的LLM Wiki 内容创作3.0系统"
source: "https://mp.weixin.qq.com/s/uSNIibUFNVnZg1JSoeqtHg"
author:
  - "饼干哥哥"
published:
created: 2026-04-14
description:
tags:
  - "clippings"
---
原创 饼干哥哥 *2026年4月13日 14:46*

前两周，我在小号「第二曲线增长」上发了一篇介绍文章，入池干到 2 万阅读，量不多，但直接带来 20 万销售额。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/UQ9fsOliarQ9icokY0wbv8LJmUEAcfSdN0tibVrQSGtTiaoVgFibwDVeNFv22A8zu4S0l60A286b1QiblGo38ibOZeHBDHib0wmfY4rHibeLLZLauxLg/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

文章从选题调研、写稿、改稿评审、排版到发布，全程 Claude Code 执行。我只做了一件事：审稿点发布。

这是我搭的一套全自动内容生产系统，管理着4 个矩阵公众号、共享一个知识库，35 个 AI 技能包覆盖完整创作链路，从选题、写稿打分重改，到生成插图、排版、发布，甚至拆成短视频脚本做一鱼多吃，全部自动化。

有时候一篇文章能被打回去 2 次，我看着很欣慰

之前写过一篇「 [用 OpenClaw + Obsidian 搭建内容工厂](https://mp.weixin.qq.com/s?__biz=MjM5NDI4MTY3NA==&mid=2257498975&idx=1&sn=c035ee9d79ff444ac74d6b8466ff5f1d&scene=21#wechat_redirect) 」讲的就是这套 2.0 版本。

但跑了三个月后，我发现了一个严重的问题。

200 多篇塞进知识库的研究资料，同一个问题问 AI 两次，答案不一样。37 处概念定义冲突，4 处事实矛盾，60 多篇文章从来没被引用过——收藏进来就再也没人碰。

创作链路是自动化了，但底层的知识库还是一个信息垃圾场。

2.0 的天花板在这里。

然后 4 月初，Karpathy 公开了他的 LLM Wiki 方法论。看完之后，我把知识库拆了重建——从「2.0 全自动创作」升级到「3.0 知识编译」。AI 不再只是执行写作指令，而是持续编译、维护、进化整个知识资产。

这篇文章是我从 2.0 到 3.0 的完整思考 + 开箱即用的干货。你会拿到：

一套在 Karpathy 方案基础上改进过的三步编译法，附完整提示词。以及我管理 4 个公众号的真实项目结构、CLAUDE.md 写法和健康检查提示词。

01

从 2.0 到 3.0，到底升级了什么

先讲清楚 Karpathy 说了什么，再讲我怎么改的。

Karpathy（OpenAI 联合创始人、前特斯拉 AI 负责人）4 月初公开了一份他自己用的知识管理方案，叫 LLM Wiki。核心思路一句话：别在提问时才去翻原始文档，让 LLM 提前把所有资料编译成一个持久的 Wiki。

我现在用的界面

我的 2.0 系统就是典型的「提问时才翻」——200 篇资料扔在那里，写文章时让 AI 现搜现读现拼。每次从零开始，搜到哪篇算哪篇，同一个问题换个对话窗口问就可能得到不同答案。NotebookLM、ChatGPT 的文件上传，都是这个逻辑。

Karpathy 的方案反过来：原始文档先经过 LLM「编译」，变成结构化的概念条目、方法论页面、交叉引用网络。编译完之后，知识是一个持久资产——矛盾已经标记了，交叉引用已经建好了，新资料加入时增量更新。

这就是我说的 3.0。2.0 自动化了「创作」，3.0 自动化了「知识本身的积累和进化」。

![2.0 Runtime RAG vs 3.0 Compile-time Wiki 架构对比](https://mmbiz.qpic.cn/sz_mmbiz_png/UQ9fsOliarQicZUjMeHmEwPB9iaxJlKiazt9HsCQ4kIvpC4w1v4AgTByhvoibibAGM67LlSw0cibpPnCjWPRGKuG3zRTIbHaQvia6YD1bU7OOxJ61Og/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

2.0 Runtime RAG vs 3.0 Compile-time Wiki 架构对比

但 Karpathy 的原始方案我跑了两周后发现有一个盲区——他的编译基本上就是做摘要。假设有两篇观点相反的文章，它们分别编译后，有可能两份摘要的结果是一样的。也就是说，摘要只压缩信息，不生成新知识。

我加了两个步骤解决了这个问题。下面先看目录结构，再讲编译法。

![三步编译法：浓缩 → 质疑 → 对标](https://mmbiz.qpic.cn/sz_mmbiz_png/UQ9fsOliarQ9PXdZ5J1eevibW6M2ibu6cCbmq5BtaGe7Qx0xxmSphqwCgC3GkxmTb5C9EH20Fl2KTZN2D3icESQW3xUKZPyibzM8ruMrgTjb3UOA/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

三步编译法：浓缩 → 质疑 → 对标

02

3.0 的目录结构：直接抄

我重建后的目录结构，直接复制：

`我的Obsidian仓库/   ├── 02_Research/   │   ├── raw/                    # 第一层：原始资料（只读）   │   │   ├── articles/           # Web Clipper 剪藏的文章   │   │   ├── reports/            # 行业报告   │   │   └── competitors/        # 竞品分析   │   └── wiki/                   # 第二层：编译产物（LLM 维护）   │       ├── summaries/          # 逐篇编译摘要   │       ├── concepts/           # 概念条目（核心）   │       ├── methods/            # 方法论页面   │       └── indexes/   │           ├── index.md        # 全局索引   │           └── log.md          # 操作日志   └── CLAUDE.md                   # 编译规则写在这里`

核心就两个文件夹： `raw/` 存原始资料只读不改， `wiki/` 存 LLM 编译产物。你负责往 `raw/` 塞文章，LLM 负责编译到 `wiki/` 。

在 CLAUDE.md 里加上这段编译规则（直接复制）：

markdown

`### 知识编译规则      当用户说「编译 {文件路径}」时，执行以下步骤：      1. 读取 raw/ 下的指定文件   2. 执行三步编译法（浓缩 → 质疑 → 对标）   3. 在 wiki/summaries/ 写编译摘要   4. 在 wiki/concepts/ 创建或更新相关概念条目      - 如果概念已存在，合并新信息，标注来源差异      - 如果两篇文章观点矛盾，在条目中显式标记冲突   5. 更新 wiki/indexes/index.md（追加来源 + 关联概念）   6. 更新 wiki/indexes/log.md（追加操作记录）      概念条目模板：   ---   concept: {概念名}   sources: [{来源文章1}, {来源文章2}]   last_updated: {日期}   ---   # {概念名}   ## 定义   ## 关键数据点（附来源）   ## 前提与局限性   ## 冲突标记（如有）   ## 关联概念`

03

三步编译法：附完整提示词

Karpathy 的编译流程是：读原文 → 写摘要 → 提取概念 → 更新索引。

为了解决前面说的摘要问题，我加了两个步骤：

**第一步：浓缩。** 砍到只剩核心结论（不超过 3 条）+ 关键证据。

**第二步：质疑。** 这一步是跟 Karpathy 方案的关键差异。

我编译了一篇讲「用 GPT-4 做跨境电商选品，转化率提升 40%」的文章。AI会质疑步骤里，AI 指出核心前提是「目标市场是北美」——如果你做东南亚市场，这个 40% 可能完全不成立。

否则，这个数字就会作为孤立事实躺在 Wiki 里误导你。

**第三步：对标。** 跨领域找类似现象。

我编译一篇讲「AI Agent 多步推理链在第 5 步后容易失控」的文章时，AI 对标发现这跟跨境电商里「供应链超过 4 个环节后出错率指数上升」是同一种现象——复杂链条的可靠性随环节数指数下降。

这个跨域洞察被写入了 `wiki/concepts/链条可靠性递减.md` ，同时链接到 AI Agent 和供应链两个概念页。

我第一次看到这个结果愣了五秒。在 AI 和跨境电商两个领域分别干了好几年，从没想过这两件事是同一种现象。

下面是完整的编译提示词，直接复制到 CLAUDE.md 或者对话里用：

markdown

`请对以下文章执行三步编译法：      ### 第一步：浓缩   - 用剃刀法则：删掉这条信息会影响理解吗？不会就删   - 输出：核心结论（不超过 3 条）+ 支撑每条结论的关键证据   - 格式：每条结论一行，证据缩进在下方      ### 第二步：质疑   针对每条核心结论，回答：   1. 这个结论依赖哪些前提假设？   2. 如果这些前提不成立（换行业/换市场/换规模），结论还成立吗？   3. 作者的数据来源可靠吗？样本量、时间范围、地域限制？   4. 有没有作者没提到的反例或边界条件？      ### 第三步：对标   1. 其他领域有没有类似现象？（技术↔商业↔管理↔科学）   2. 这个知识可以迁移到哪些场景？   3. 如果有跨域关联，创建或更新对应的概念条目      最后，按概念条目模板输出编译结果。`

04

实操：一篇文章编译后会产出什么

拿一个真实场景。我用 Obsidian Web Clipper 剪了一篇 TikTok Shop 选品策略的文章到 `raw/articles/` 。

对 Claude Code 说： `编译 02_Research/raw/articles/2026-04-tiktok-shop-选品策略.md`

Claude Code 做了 6 件事：

1 读取原文

2 执行三步编译法

3 在 `wiki/summaries/` 写了一篇编译摘要（浓缩 + 质疑 + 对标结果）

4 在 `wiki/concepts/` 下创建或更新了「TikTok Shop 选品」「AI 选品工具」「跨境电商利润率」3 个概念条目

5 更新 `wiki/indexes/index.md` ——追加来源和关联概念

6 在 `wiki/indexes/log.md` 追加操作记录

![一篇文章编译后的产物：1 篇原始文章 → 7 个 Wiki 文件](https://mmbiz.qpic.cn/sz_mmbiz_png/UQ9fsOliarQic74DYn62icpdicPNzPal34Y1moBd54lnZUOBSyffKZ3DLHb3HTwA9wXcRGfiaKHUZ333IIjmrmXVHqevYO213czW5LkW6NKU0yPg/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

一篇文章编译后的产物：1 篇原始文章 → 7 个 Wiki 文件

一篇文章编译后的产物：1 篇原始文章 → 7 个 Wiki 文件

关键在于：下次我再编译一篇跟 TikTok 选品相关的文章时，AI 不是从零开始。它会读取已有的概念条目，把新信息跟旧信息合并，标注异同——如果有矛盾，直接在条目里标记。

这就是 L3 和 L2 的本质区别：L2 是 runtime 的（每次运行时才检索），L3 是 compile-time 的（知识在编译时已经被处理过）。

05

每周跑一次知识库健康检查

![知识库每周健康检查四维度](https://mmbiz.qpic.cn/sz_mmbiz_png/UQ9fsOliarQibbuMia2HfficOq9P0TsiboLYrgqCuaYRvqxqQjvFibkq2RqaD81EEtRk7xjKMhX6UtusA8QeEzCTGicz0GEyW5DHNbwMiaaVtQ2yBP8/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

知识库每周健康检查四维度

参考体检提示词：

markdown

`对 wiki/ 目录执行健康检查，生成报告：      ### 1. 一致性检查   扫描所有 concepts/ 下的条目，检查：   - 同一个概念在不同条目中的定义是否一致   - 如果不一致，列出冲突位置和建议统一方向      ### 2. 完整性检查   检查每个概念条目是否包含所有必填字段：   - 定义、关键数据点、前提与局限性、关联概念   - 缺失字段标记为待补充      ### 3. 孤岛检测   找出入链和出链都少于 2 的页面——   这些页面要么需要跟其他概念建立关联，要么说明它不够重要可以考虑合并      ### 4. 跨目录一致性（多账号场景）   扫描各账号的 _style-guide.md 和 CLAUDE.md，   检查风格规则有没有遗漏或冲突      输出格式：表格 + 每个问题的建议修复方案`

上周这个检查发现我在「饼干哥哥AGI」的禁止词表里写了「不用双引号」，但在 「第二曲线增长」的 CLAUDE.md 里漏写了。这种跨文件的一致性问题，人工几乎不可能发现。

06

为什么 3.0 能持续运转

我之前用过 Notion、飞书、Obsidian 做知识管理，每次都是头两个月很勤快，然后就荒废了。原因很简单：维护知识库最繁琐的部分——更新交叉引用、保持定义一致、标注矛盾——这些活儿的成本增速超过了它带来的价值。我会忘记更新某个交叉引用，会懒得去检查两篇文章有没有冲突。

一口气改很多个文档

LLM 把这个成本打到了接近零。它可以在一次操作中同时修改 15 个文件，不会忘，不会烦。这是 3.0 能持续运转的根本原因——不是方法论多先进，是维护成本终于低到可以忽略了。

1945 年 Vannevar Bush 描述过一台叫 Memex 的机器——私人知识库，文档之间有联想式关联路径。他没解决的问题是：谁来维护？

80 年后，LLM 解决了。

07

3.0 之后，我看到的商业可能性

除了运营公众号外，我还用这套 wiki给团队新人做 onboarding 知识库、以及给客户做行业知识产品的底层数据源。

后者是最有想象空间的——LLM Wiki 做成的行业知识库是可以卖钱的。不是卖原始资料，是卖编译后的知识资产。

2.0 让我可以一个人当一个内容团队。3.0 让我可以一个人当一个知识公司。

这才刚开始。

继续滑动看下一个

饼干哥哥AGI

向上滑动看下一个

## 编译摘要

### 1. 浓缩
- **核心结论1**: 2.0 的天花板是"信息垃圾场"——200多篇资料，同一个问题问AI两次答案不一样，37处概念定义冲突
  - 关键证据: 创作链路自动化了，但底层知识库还是信息垃圾场
- **核心结论2**: 3.0 的核心是从 Runtime RAG 升级到 Compile-time Wiki——知识在编译时已经被处理过
  - 关键证据: LLM 不再只是执行写作指令，而是持续编译、维护、进化整个知识资产
- **核心结论3**: 三步编译法（浓缩→质疑→对标）解决了 Karpathy 原始方案的盲区
  - 关键证据: 摘要只压缩信息不生成新知识，质疑步骤可以指出"40%转化率"的前提是"北美市场"

### 2. 质疑
- **关于"卖20万"的质疑**: 是否可复制？是否是特定时间节点、特定平台的结果？
- **关于"自动化程度"的质疑**: AI 负责编译和维护，但初始的"选题调研"是否也需要自动化？
- **关于"知识所有权"的质疑**: LLM 编译后的知识资产，所有权归谁？

### 3. 对标
- **跨域关联1**: 类似 Vannevar Bush 的 Memex（1945）——LLM 解决了"谁维护"的问题
- **跨域关联2**: 类似卡片盒法（Zettelkasten）——从手工链接升级到 AI 自动维护
- **跨域关联3**: 类似从"人力资源"到"人才DevOps"——知识作为可组合的资产

### 关联概念
- [[Knowledge-Compilation]] - 知识编译工作流
- [[Software-2.0]] - 软件范式与 AI 创作
- [[Vibe-Coding]] - AI 驱动创作范式
- [[Agent-Swarm]] - Agent 协作工作流

currentcurrent