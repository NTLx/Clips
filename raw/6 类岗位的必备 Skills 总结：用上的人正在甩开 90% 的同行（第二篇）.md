---
title: "6 类岗位的必备 Skills 总结：用上的人正在甩开 90% 的同行（第二篇）"
source: "https://mp.weixin.qq.com/s/lNdINr5yK2pT8HbW4zAtcA"
author:
  - "[[Ai大刘]]"
published:
created: 2026-03-06
description: "6 个岗位的必备 skills（下篇），用上！"
tags:
  - "clippings"
---
原创 Ai大刘 *2026年2月27日 18:02*

![头图](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J1Cdba5GUc1E4Fg0S7tEoPh2ibD15qm6S6EOaMd2nUsZIXvibPAKBx3mGVu6qqfCj3cica6eY5oSn9cYU06a0gVXbo93QEicb6OTW2FwLicG7380/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

>   
> 
> 昨天分享了文章之后，很多朋友说没有涉及到自己的岗位，所以今天又整理了 6 个岗位的必备 skills 。
> 
>   
> 
>   
> 
> 1. 新的 6 类岗位 × 每类 3 个 Skill 精选推荐（昨天的文章已经整理过 6 个了
> 
> 2\. 哪些我亲测过、哪些顶尖大学教授连续几个学期跑通的、哪些社区几万 Star 验证过的，都标了
> 
> 3\. 文末附 6 岗位 18 Skill 速查表，收藏这一张就够了建议收藏，按需取用。
> 
>   
> 
> 建议收藏，按需取用。请无私的分享给你关心且需要这些 skills 的人～

  

一个做法务的朋友，上周装了个 Claude Skill。

  

50 页的商业合同，以前审一天半。Skill 帮她把所有风险条款标成了红黄绿三色——她只花了 3 个小时做最终判断。

  

Emory 大学的经济学教授，更狠。6 套博士课程讲义，800 多张幻灯片——全部用 Claude Skills 协作完成。从文献检索到 LaTeX 编译，整个学术工作流都跑通了。

  

我自己也试了。拿一篇写了两个月的文献综述丢进去，它补出来 3 篇我漏掉的文献。

  

这不是"AI 能帮点忙"的级别了。

  

话不多说，直接开始。

  

## 岗位 1：财务/会计

  

做财务的人最怕什么？ **月底。**

  

对账、做报表、处理发票、差异分析……每一项都是精确到小数点后两位的苦力活。德勤 2025 年的调研数据： **74% 的会计事务所已经在试点或使用 AI** 。不是"计划用"，是"已经在用了"。

  

你还在 Excel 里一行行核数据，隔壁公司的财务已经在一句话出报表了。真的，这个差距已经不是效率的差距了——是装备代差。

  

1\. **Finance Plugin** 。Anthropic 官方出品（GitHub: `anthropics/knowledge-work-plugins` ，8.1k Star）。一口气 6 个会计 Skill——记账凭证、对账、利润表、差异分析、月结管理、SOX 审计。输入 `/journal-entry` 就开始记账，就这么简单。

  

最关键的是——它能直连 NetSuite、SAP、Snowflake。就像给你的 Excel 装了个自动驾驶，直接从 ERP 里拉数据出报表。不是玩具级别的，是真正打通企业级 ERP 的。

  

我自己试了一下 `/journal-entry` ，三步就出了一张凭证——确实比 Excel 手动录入快太多。

  

2\. **Financial Services Suite** 。同样 Anthropic 官方出品（GitHub: `anthropics/financial-services-plugins` ，2.9k Star）。这个套件的体量，我数了三遍才确认没看错—— **41 个 Skill + 38 个命令** 。

  

DCF 估值、LBO 建模、三表模型、投行分析、股票研究、财富管理——说人话就是：这家公司值多少钱、怎么收购、财务报表怎么做。整套工具相当于给你配了个不要工资的投行分析师实习生。还有 LSEG 和 S&P Global 的合作插件。说白了，整个金融行业的分析工作，这一个套件就包了大半。

  

3\. **Invoice Organizer** 。来自 ComposioHQ 社区（GitHub: `ComposioHQ/awesome-claude-skills` ，38k Star）。干的事很简单但很实用——读 PDF 发票和扫描件，自动提取金额、供应商、日期，按税务分类归档，最后生成 CSV。

  

每个月攒了一堆发票不想整理？丢进去，几秒搞定。

  

**月底不加班的财务，不是活少——是装备好。**

  

## 岗位 2：教师/培训师

  

以前出一套试卷要半天——翻教材、琢磨出题角度、平衡难度梯度、反复检查答案。备一堂公开课？那至少一晚上。

  

现在呢？

  

1\. **教育技能套件** 。来自 GitHub 开发者 Dan McCreary（仓库： `dmccreary/claude-skills` ）。 **19 个教育专用 Skill** ，这个数字本身就够说明问题了。

  

最硬核的是布鲁姆分类法出题——按"记住了没、理解了没、会用了没"的认知层级自动生成每章 8-12 道选择题，还附带质量评分。我拿了一章机器学习教材试了一下——8 道题里 6 道直接能用，有 2 道需要微调表述。比我自己出题快了至少三倍。另外还有课程描述分析（100 分质量评估）、学习图谱（200+ 概念依赖映射）、词汇表自动生成、FAQ 自动生成、参考文献自动整理。你以前备一堂课要花一晚上的事，它帮你做完大半。

  

2\. **learning-education** 。来自开发者 spitoglou（GitHub: `spitoglou/fabric-claude-skills` ）。这玩意桥接了 Fabric 提示库，提供 7 个教学模式。

  

最让我眼前一亮的是 `dialog_with_socrates` ——苏格拉底式问答教学。AI 不直接给答案，而是通过反问引导学生自己想出来。还有类比式术语解释、按难度出题、间隔重复闪卡、学习路径规划。

  

3\. **Office 文档套件** 。来自开发者 Thomas Friedel（GitHub: `tfriedel/claude-office-skills` ，309 Star）。PPTX、DOCX、XLSX 一站式创建编辑。内置公式、配色方案、数据校验。

  

PPT 课件、Word 教案、Excel 成绩表——教学"三件套"，一个 Skill 全搞定。不用在三个软件之间来回切了。

  

**备课的本质不是整理资料，是琢磨这节课怎么让学生眼睛亮起来。**

  

## 岗位 3：法务/律师

  

凌晨一点，你还在逐条审一份 50 页的商业合同。每一条都得看、都得标、都得想"万一对方抓住这条怎么办"。

  

律师的日常，不是法庭上的慷慨陈词——是这种一个字都不能漏的苦差事。麦肯锡做过一个研究： **生成式 AI 对法律行业的可自动化潜力约 44%** 。将近一半。

  

1\. **Legal Plugin** 。Anthropic 官方出品（GitHub: `anthropics/knowledge-work-plugins` ，同财务板块的 Finance Plugin 同一仓库）。5 个法律 Skill，其中合同审查这个做得特别细——它会按 Playbook 逐条审，然后给每一条打三色标记：GREEN（安全）、YELLOW（注意）、RED（高风险）。

  

就像给合同做了个体检报告，红黄绿一目了然，哪里有坑立刻知道。还有 NDA 分拣、合规工作流（GDPR/CCPA/DPA 全支持）、法律风险评估（严重性 x 可能性矩阵）、会议简报准备。官方出品，品质有保障。

  

说实话三色标记这个功能我看完 demo 就知道它值——做过合同审查的人都懂那种"不知道哪条有坑"的焦虑。

  

2\. **claude-legal-skill** 。来自开发者 Chris Sheehan（GitHub: `evolsb/claude-legal-skill` ，51 Star）。这个 Skill 专攻合同审查，基于 CUAD 数据集的 41 个风险类别——CUAD 相当于合同审查领域的驾考题库，41 种坑，它全见过。

  

支持 NDA、SaaS 协议、并购合同、劳动合同，还能按代表方调整审查立场。你代表买方还是卖方，审查重点完全不同，它帮你自动切换。还有一个 ContractEval 市场基准对比功能，让你知道这份合同在市场上处于什么水平。

  

3\. **Awesome Legal Skills** 。来自 lawvable 社区（GitHub: `lawvable/awesome-legal-skills` ，126 Star）。这是首个法律 Skill 开放社区，目前已经有 20+ 个独立法律 Skill，覆盖商法、隐私法、合规、劳动法、法律方法论。它不是一个单独的 Skill，是一个生态——说明法律 AI 这条路，已经有很多人在走了。

  

**律师最贵的不是审合同的时间，是判断"这条能不能签"的经验。前者 AI 做得了，后者只有你做得了。**

  

## 岗位 4：咨询顾问/分析师

  

上篇有人问我：做咨询的有什么 Skill 吗？

  

我替你翻了——还真不少。

  

1\. **stratarts** 。来自 MAIGENT 团队（GitHub: `maigent/stratarts` ）。 **27 个商业战略 Skill** ，覆盖范围大到我反复确认了好几次。

  

市场分析、竞争情报、商业模式设计、财务建模、定价策略、投资者路演 Deck——你能想到的咨询报告类型，它基本全有。最酷的是输出不是纯文字，是带图表的 HTML 报告，打开浏览器就能看到可视化的分析结果。

  

我拿一个模拟项目跑了一下市场分析模块——出来的 HTML 报告带图表带结论，说实话比我实习时候写的像样多了。

  

2\. **Deep Research Skills** 。来自开发者 Weizhena（GitHub: `Weizhena/Deep-Research-skills` ，74 Star）。两阶段深度研究法——Phase 1 生成大纲，Phase 2 逐项深挖。

  

三个命令： `/research` （快速研究）、 `/research-deep` （深度研究）、 `/research-report` （报告生成）。明确支持行研和尽调场景。而且，含中英文双版本——做跨境项目的咨询顾问可以直接用。

  

3\. **ceo-advisor / product-strategist** 。来自开发者 Alireza Rezvani（GitHub: `alirezarezvani/claude-skills` ，2k Star）。这个仓库是个 65+ Skill 的合集，战略板块特别强。

  

CEO 顾问（战略决策、财务情景建模）、CTO 顾问（技术战略、架构决策）、产品策略师（OKR、愿景对齐、路线图规划）、营销策略（多触点归因、漏斗转化分析）。一个仓库，多个角色，按需启用。

  

**80 分的报告 AI 半小时就能出。但客户买单的，从来都是那最后 20 分的洞察。**

  

## 岗位 5：合规/审核/质检

  

你可能觉得合规这种岗位跟 AI 八杆子打不着——不就是拿着标准一条条对照嘛。

  

ISO 标准、GDPR 法规、FDA 要求、SOC 2 审计……每一条都得对照、都得核实、都得出证据。但恰恰因为它足够标准化，AI 切入得反而最深—— **人家已经有 12 个 Skill 了。**

  

1\. **RA/QM Team Bundle** 。来自 Alireza Rezvani 的 Skill 合集（GitHub: `alirezarezvani/claude-skills` ，2k Star）， `ra-qm-team/` 目录。

  

**12 个合规 Skill** ，横跨四大体系——医疗器械质量（ISO 全家桶 + FDA + 欧盟法规）、信息安全、隐私保护（GDPR）、风险管理。你做医疗器械合规的话，这一套装完基本就齐了。

  

2\. **soc2-audit-helper** 。来自开发者 Jeremy Longshore（GitHub: `jeremylongshore/claude-code-plugins-plus-skills` ，1.4k Star）。SOC 2 证据自动采集、安全控制分析、合规差距识别、修复建议。就像税务稽查前帮你把所有发票账单按年份整理好——你只需要开门让检查员进来。

  

同仓库里还有 HIPAA 合规检查 + OWASP Top 10 安全检查。内置合规审计 SOP——不是简单告诉你"这条不合规"，是告诉你"这条不合规、差距在哪、怎么修"。

  

3\. **spec-to-code-compliance** 。来自 Trail of Bits（GitHub: `trailofbits/skills` ，3k Star）。如果你不认识 Trail of Bits——这是全球顶级安全审计公司，客户包括以太坊基金会、微软等。

  

他们出品的这个 Skill 做一件事： **规范与实际执行的合规性对照审计** 。证据式对齐分析，每一条结论都有置信度评分和严重性分级。我虽然不做合规，但这种"每条结论都有置信度"的输出方式——说实话应该推广到所有 AI 工具。安全审计公司做的合规 Skill，这个背书分量够重了。

  

**合规最难的不是对照标准——是标准没写到的那页。**

  

## 岗位 6：科研/学术研究

  

做科研的人，一半时间在做研究，一半时间在跟文书打架。

  

文献综述、论文排版、审稿回复、基金申请、引用格式——每一项都不难，但加起来能把人逼疯。这个板块放在最后，是因为科研领域的 Skills 生态， **成熟得超乎我的想象** 。接下来你看到的数字，可能会让你和我一样愣住。

  

1\. **claude-scientific-skills** 。来自 K-Dense-AI（GitHub: `K-Dense-AI/claude-scientific-skills` ，9.4k Star）。

  

**147+ 个科学 Skill。** 你没看错，一百四十七个。这不是瑞士军刀了，这是一整个军械库。覆盖文献综述、同行评审、假设生成、基金申请、引用管理。更猛的是——直连 6 大科学数据库：PubMed、arXiv、bioRxiv、ClinicalTrials.gov、ChEMBL、UniProt。相当于同时打开 6 个图书馆的大门，而且不用办借书证。做生物信息学、化学信息学的朋友，这就是你的装备库。

  

2\. **claude-scholar** 。来自 Galaxy-Dawn（GitHub: `Galaxy-Dawn/claude-scholar` ，843 Star）。 **32 个学术 Skill + 14 个 Agent + 50 个命令** ——这个体量是认真的。

  

`/lit-review` （文献综述）、 `/research-init` （研究启动）、 `/rebuttal` （审稿回复）——光这三个命令就解决了科研人 80% 的文书痛苦。还支持 Zotero 集成、NeurIPS / ICML / ICLR 格式指导。写论文的人都知道，格式调不对比内容写不好更崩溃。

  

我拿了一篇之前写过的综述丢进去跑 `/lit-review` ，它补出来的文献有 3 篇是我之前漏掉的。这个我是真服气。

  

3\. **claude-code-my-workflow** 。来自 Pedro H. C. Sant'Anna（GitHub: `pedrohcgs/claude-code-my-workflow` ，443 Star）。这位不是普通开发者——他是 Emory 大学的经济学家 Pedro Sant'Anna。21 个 Skill + 10 个 Agent。 `/lit-review` 、 `/research-ideation` 、 `/data-analysis` 、 `/compile-latex` 、 `/slide-excellence` 。

  

最让我服气的是他的实战数据： **6 套博士课程讲义，800+ 张幻灯片** ——全部用 Claude Skills 协作完成。

  

你想象一下那个画面：一个顶尖大学的教授，坐在办公室里，跟 Claude 一起备课。文献检索、数据分析、LaTeX 编译、幻灯片制作——每个环节他都跑通了。不是试一次就放弃，是连续几个学期，800 张 PPT。

  

说实话看到这个数字的时候，我愣了好一会儿。

  

**AI 能帮你读完一千篇论文，但那个让你凌晨三点突然坐起来的灵感，它给不了你。**

  

## 最后

  

上篇 6 个岗位，这篇又 6 个。 **12 个岗位，36 个 Skill。**

  

写完这两篇我最大的感受是——这些 Skill 的作者，很多不是程序员，是各行各业真正在用的人。法务律师、大学教授、安全审计师。他们把自己的工作流变成了 Skill，然后开源给所有人。

  

这件事本身就挺让人感慨的。

  

不要贪多，先找到你岗位最痛的那个场景，给它配一个 Skill。跑通了，你就懂了。

  

你的岗位在这两篇里找到了吗？用了哪个？效果怎么样？ **评论区聊。**

  

找到你的 Skill。

  

装上。

  

然后——腾出手来。

  

## 全岗位 Skill 速查表（下篇）

  

> 收藏这张表，按你的岗位直接找。

**财务/会计**

| Skill 名称 | 一句话说明 | 来源 |
| --- | --- | --- |
| Finance Plugin | 6 个会计 Skill，直连 NetSuite/SAP/Snowflake | Anthropic 官方 · anthropics/knowledge-work-plugins |
| Financial Services Suite | 41 个 Skill + 38 个命令，覆盖金融全链条 | Anthropic 官方 · anthropics/financial-services-plugins |
| Invoice Organizer | PDF 发票自动提取→分类归档→生成 CSV | ComposioHQ/awesome-claude-skills |

教师/培训师

| Skill 名称 | 一句话说明 | 来源 |
| --- | --- | --- |
| 教育技能套件 | 19 个教育 Skill，布鲁姆分类法出题+学习图谱 | dmccreary/claude-skills |
| learning-education | 苏格拉底式问答+闪卡+学习路径，7 个教学模式 | spitoglou/fabric-claude-skills |
| Office 文档套件 | PPT/Word/Excel 一站式创建编辑 | tfriedel/claude-office-skills |

法务/律师

| Skill 名称 | 一句话说明 | 来源 |
| --- | --- | --- |
| Legal Plugin | 三色标记合同审查+NDA 分拣+合规工作流 | Anthropic 官方 · anthropics/knowledge-work-plugins |
| claude-legal-skill | CUAD 41 个风险类别，按代表方调整审查立场 | evolsb/claude-legal-skill |
| Awesome Legal Skills | 首个法律 Skill 开放社区，20+ 独立 Skill | lawvable/awesome-legal-skills |

咨询顾问/分析师

| Skill 名称 | 一句话说明 | 来源 |
| --- | --- | --- |
| stratarts | 27 个战略 Skill，输出含图表的 HTML 报告 | maigent/stratarts |
| Deep Research Skills | 两阶段深度研究法，中英双版本，支持行研/尽调 | Weizhena/Deep-Research-skills |
| ceo-advisor 等 | 65+ Skill 合集，CEO/CTO/产品/营销多角色覆盖 | alirezarezvani/claude-skills |

合规/审核/质检

| Skill 名称 | 一句话说明 | 来源 |
| --- | --- | --- |
| RA/QM Team Bundle | 12 个合规 Skill，覆盖 ISO/GDPR/FDA/EU MDR | alirezarezvani/claude-skills |
| soc2-audit-helper | SOC 2 + HIPAA + OWASP 三合一合规审计 | jeremylongshore/claude-code-plugins-plus-skills |
| spec-to-code-compliance | 规范 vs 实际的对照审计，置信度评分 | Trail of Bits · trailofbits/skills |

科研/学术研究

| Skill 名称 | 一句话说明 | 来源 |
| --- | --- | --- |
| claude-scientific-skills | 147+ 科学 Skill，直连 PubMed/arXiv 等 6 大数据库 | K-Dense-AI/claude-scientific-skills |
| claude-scholar | 32 Skill + 14 Agent + 50 命令，Zotero 集成 | Galaxy-Dawn/claude-scholar |
| claude-code-my-workflow | Emory 教授实战验证，800+ 张幻灯片产出 | pedrohcgs/claude-code-my-workflow |

  

**去哪里找 & 怎么装：**

  

\- **Anthropic 官方仓库** ：GitHub 搜索 `anthropics/skills` 和 `anthropics/knowledge-work-plugins`

\- **SkillsMP 技能市场** ：skillsmp.com（28 万+ Skills 聚合索引，按分类浏览）

\- **GitHub 直搜** ：上表中的来源名就是仓库路径，直接搜即可

\- **Claude Code 内装** ：输入 `/plugin` 浏览和安装官方插件

  

后台回复 skill，也可以获取全套～

昨天的 6 类岗位文章在这里： [6 类岗位的必备 Skills 总结：用上的人正在甩开 90% 的同行](https://mp.weixin.qq.com/s?__biz=MzIyNzQ3MDM3Mw==&mid=2247484112&idx=1&sn=26d164b1b30ba303bab2fb578958f0fe&scene=21#wechat_redirect)

  

**请无私的分享给你关心且需要这些 skills 的人 ～** ，可能帮他省下每周 5 小时的重复劳动。

  

以上，既然看到这里了，  
如果觉得不错，随手点个赞、在看、转发三连吧，  
如果想第一时间收到推送，也可以给我个星标⭐～  
谢谢你看我的文章

  

**我是谁**

我是 AI大刘 ，北大毕业，大模型研究方向，腾讯犀牛鸟先后在腾讯、百度的大模型研发部门，现在给多家国企做AI顾问（也期待大家和我咨询交流

朋友圈会分享我的日常深度思考，欢迎链接。 还送你一份持续更新的适用于所有人的 AI 认知、工具笔记～

欢迎链接我：

![图片](https://mp.weixin.qq.com/s/www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg%20stroke='none'%20stroke-width='1'%20fill='none'%20fill-rule='evenodd'%20fill-opacity='0'%3E%3Cg%20transform='translate(-249.000000,%20-126.000000)'%20fill='%23FFFFFF'%3E%3Crect%20x='249'%20y='126'%20width='1'%20height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

同时，也欢迎加入交流群，里面有行业动态、AI 趋势、工具干货等等内容，期待您的加入 ～

![图片](https://mp.weixin.qq.com/s/www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg%20stroke='none'%20stroke-width='1'%20fill='none'%20fill-rule='evenodd'%20fill-opacity='0'%3E%3Cg%20transform='translate(-249.000000,%20-126.000000)'%20fill='%23FFFFFF'%3E%3Crect%20x='249'%20y='126'%20width='1'%20height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

往期精选

2026用上这些Skills，你就跑赢了90%的人

![图片](https://mp.weixin.qq.com/s/www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg%20stroke='none'%20stroke-width='1'%20fill='none'%20fill-rule='evenodd'%20fill-opacity='0'%3E%3Cg%20transform='translate(-249.000000,%20-126.000000)'%20fill='%23FFFFFF'%3E%3Crect%20x='249'%20y='126'%20width='1'%20height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

一文讲透 Claude Skills！大白话教程让你跑赢 90% 的人

![图片](https://mp.weixin.qq.com/s/www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg%20stroke='none'%20stroke-width='1'%20fill='none'%20fill-rule='evenodd'%20fill-opacity='0'%3E%3Cg%20transform='translate(-249.000000,%20-126.000000)'%20fill='%23FFFFFF'%3E%3Crect%20x='249'%20y='126'%20width='1'%20height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](https://mp.weixin.qq.com/s/www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg%20stroke='none'%20stroke-width='1'%20fill='none'%20fill-rule='evenodd'%20fill-opacity='0'%3E%3Cg%20transform='translate(-249.000000,%20-126.000000)'%20fill='%23FFFFFF'%3E%3Crect%20x='249'%20y='126'%20width='1'%20height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

  

  

内容含AI生成图片

继续滑动看下一个

爱AI的大刘

向上滑动看下一个