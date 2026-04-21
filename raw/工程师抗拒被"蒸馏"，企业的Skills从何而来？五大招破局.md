---
title: "工程师抗拒被\"蒸馏\"，企业的Skills从何而来？五大招破局"
source: "https://mp.weixin.qq.com/s/OAQ-Vn6_ClLijT_b5KTELA"
author:
  - "[[朱少民]]"
published: "2026-04-21"
created: 2026-04-21
description: "缺的不是技术，是制度"
tags:
  - "clippings"
---
原创 朱少民 *2026年4月21日 11:26*

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/WzzWicO2aD7ql45HONE2ckib1P2TEluUQlIHkBsDonoER5EAdQ8la2ibtSNv8ljSAyu0ibOIfbicAw5CyqtGRK5iaPKsicqGz6MLTQicfLeSmPmLiaLw/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)


![图片](https://mmbiz.qpic.cn/mmbiz_png/WzzWicO2aD7r1EXE1QkX67XK6rGShJXiaMicq2nicziaErNav3C6hQSt3J3957x6cianyGRdiah2UjjvG32RSoY4RgE67OuRoQib7pr8ozLKmzddNxE/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=1)

![图片](https://mmbiz.qpic.cn/mmbiz_png/WzzWicO2aD7r8aqNEYGpVZTl3fdmHvD1gaLRTeodIGIlJDkVWqs4Pick2vGPjeNEpqoNmxSib2QNO3npRy0Ud9VVcpCKbsS3C6TvE2CUdePDmw/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=2)

![图片](https://mmbiz.qpic.cn/mmbiz_png/WzzWicO2aD7rYyO9Pu9ia4m1dMIq909icIycuib85GOsYyDNXtMicaZ8nyJAx9cu4fUiaY6H2M2a0jPEOiaTQSiaWL4sicsetf1pKoMDThIW8TicYgutY/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=3)

![图片](https://mmbiz.qpic.cn/mmbiz_png/WzzWicO2aD7rsRtN11uFPq4PkOxCPpY3YpdUur7QHMvyAHeSeHYHib9icMr014lJpb5Clq9oO6diapxEpV8JbWIj4zTkRKnmQjhjgwR4wkynyek/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=4)


[Hermes Agent、OpenCode等自主智能体框架的核心能力之一](https://mp.weixin.qq.com/s?__biz=MjM5ODczMDc1Mw==&mid=2651863456&idx=1&sn=bf940c6f9d1a81eae12e12529c084135&scene=21#wechat_redirect) ，是将工程师完成复杂任务的过程自动沉淀为可复用的Skills。这些Skills一旦形成，就像一份"数字克隆"——企业不再需要这位工程师亲自上阵，Agent调用Skill即可。

这制造了一个经典的委托-代理困境，这也是我们昨天闭门会上讨论的一个非常尖锐的问题：

企业（委托方）希望工程师（代理方）尽可能多地将知识沉淀为Skills。但工程师完全清楚，这等于亲手训练自己的替代品。

理性博弈的结果是显而易见的：

- 消极抵抗：工程师不主动创建Skills，或只创建低价值的Skills
- 质量投毒：在Skills中埋入微妙的缺陷，使其在关键场景下失效，从而证明"还是需要我"
- 上下文污染：故意在知识沉淀中遗漏关键的隐性知识（tacit knowledge），让Skills看起来完整但实际不可靠

HAL发表的一篇关于Agentic Skills全生命周期的综述论文，详细描述了Skills从发现、实践、蒸馏、存储、组合到评估和更新的完整周期——但它回避了一个根本问题：谁有动力启动这个循环？

一、问题的根源：错误的激励结构

这个困局不是技术问题，而是制度设计问题。让我们拆解当前的激励结构：

当"做正确的事"对个体的风险最高、收益最低时，没有任何道德说教能改变行为。这是制度的失败，不是人的失败。

二、破局：五种激励重构方案

（从工程师和企业“双赢”来设计激励方案更好，如方案一）

方案一：Skills版税制——让创建者持续分润

核心思想：将Skill视为"内部知识产权"，创建者在Skill每次被调用时获得持续收益。

我自己写了差不多20多本书，深有体会，现在每年有十几万稿税收入，生活就没有后顾之忧。这个方案的具体设计：

- 每个Skill在创建时自动绑定作者信息（不可篡改，基于Git签名或内部区块链）
- 企业建立Skills调用计量系统：每次Agent调用某Skill，计入该Skill的"使用量"
- 按月/季度结算Skills版税：可以是现金奖金、股权积分、晋升积分
- 版税金额与Skill的调用频次 × 成功率 × 复杂度系数挂钩

为什么有效：工程师从"创建Skill会让我被替代"变成"创建Skill会给我带来持续的被动收入"。高质量Skill被调用得越多，作者收益越大，激励方向与企业利益完全对齐。

防投毒机制：Skill的版税与成功率挂钩。投毒会导致失败率上升，版税归零甚至倒扣。

方案二：角色跃迁制——创建Skills是晋升的阶梯而非坟墓

核心思想：把"能蒸馏自己"定义为晋升到更高层级的必要条件。

制度设计：

- 晋升资深工程师的硬性条件之一：必须创建≥N个被验证的高质量Skills，且这些Skills已接管了你原来的部分职责
- 组织承诺：一旦你的Skills成功接管了当前职责，你不会被解雇，而是被赋予更复杂的新职责
- "向上蒸馏"文化：你蒸馏掉的是你今天的工作，换来的是明天更有挑战的工作

这背后的组织逻辑是：

工程师 → 创建Skills → Skills接管当前工作 → 工程师被释放去做更高阶的工作 → 再次创建Skills → 循环

关键前提：企业必须有足够的"更高阶工作"来吸纳被释放的工程师。这要求企业本身在持续创新和扩张。如果企业只是在"降本"，这个承诺就不可信，整个机制就会崩塌。

方案三：对抗性蒸馏——不依赖工程师的主动配合

核心思想：如果工程师不愿意主动创建Skills，那就通过自动化观察和提炼来绕过这个问题。

技术路径：

- Agent在观察工程师日常工作的过程中，自动识别重复模式并生成Skill草案
- Skill草案不需要工程师"主动创建"，而是由系统自动生成，工程师只需"审核确认"
- 引入多工程师交叉验证：同一个Skill草案由多位工程师独立审核，防止单点投毒

这就是Hermes Agent的Skills自动创建能力的升级版——从"工程师手动沉淀"变成"Agent自动观察+工程师验证"。

优势：降低了工程师的心理防线——"不是我主动蒸馏自己，是系统自动学习的，我只是确认一下"。

风险：工程师可能在审核环节投毒。对策：多人交叉审核 + 自动化测试验证 + 灰度发布Skill（先在低风险场景试用）。

方案四：Skills竞技场——用竞争和声望驱动创建

核心思想：将Skill创建游戏化，利用工程师的竞争心理和声望需求。

机制设计：

- 建立企业内部Skills排行榜：按使用量、好评率、覆盖场景数排名
- 定期举办Skills Hackathon：限时创建高质量Skills，优胜者获得奖金和全公司曝光
- Skills作者公开署名：在Agent执行任务时，显示"此任务由 \[张三\] 创建的Skill \[XXX\] 完成"
- 最佳Skills作者获得"内部技术合伙人"头衔，参与技术战略决策

心理学基础：顶尖工程师的核心驱动力往往不是金钱，而是技术影响力和同侪认可。当创建Skills成为彰显技术实力的方式（而非自掘坟墓），行为就会逆转。

方案五：组织保险——消除根本恐惧

上述所有方案都有一个隐含前提：工程师相信企业不会在Skills建成后抛弃自己。如果这个信任不存在，一切激励都是空中楼阁。

建立信任的制度设计：

- "Skills贡献者保护期"：贡献了高价值Skills的工程师，享有N年（如2~3年）的裁员保护期
- "蒸馏后转岗优先权"：当工程师的职责被Skills接管后，该工程师在内部转岗中享有优先权
- "Skills退休金"：离职时，如果工程师创建的Skills仍在使用，企业按约定支付一笔"知识资产买断费"

以上条款写入劳动合同，具有法律效力

三、更深层的思考：从"蒸馏工程师"到"工程师主导蒸馏"

回到问题的本质。当前的叙事是"企业蒸馏工程师"——工程师是被动的被提取方。这个叙事本身就制造了对抗。

需要翻转叙事：

不是企业在蒸馏工程师，而是工程师在用Skills构建自己的技术遗产和影响力杠杆。

最好的类比是开源软件。Linux之父Linus Torvalds创建了Linux，理论上"蒸馏"了自己的操作系统设计能力——但没有人认为他被替代了。相反，Linux成为了他影响力的永久放大器。

企业内部的Skills体系应该追求同样的效果：

- 创建者获得署名权和声望
- 创建者在Skill的演进方向上有发言权
- 创建者因为深刻理解Skill的原理，成为Skill失效时的"最终裁判"——反而更不可替代

四、防投毒的技术纵深

即使激励设计完美，仍需技术手段作为安全网：

- Skill形式化验证：对关键Skills进行属性级别的形式化证明，而非仅靠测试
- Skill血缘追踪：记录每个Skill的完整演化历史，任何修改可追溯到个人
- Skill对抗性测试：专门的红队（Red Team）尝试在Skill中发现隐藏的缺陷或后门
- Skill灰度发布：新Skill先在低风险、有人类兜底的场景运行，通过观察期后才全面启用
- 多源交叉验证：同一功能由不同工程师独立创建多个Skill，交叉比对结果，异常偏差触发告警

结语：这是一场制度创新，不是技术问题

Skills的技术基础已经成熟——Hermes Agent的四层记忆系统、OpenCode的Skills自动创建、学术界对Agentic Skills全生命周期的系统化研究，都已经铺好了路。

缺的不是技术，是制度。

工程师不是不愿意分享知识，开源社区已经证明了这一点。工程师抗拒的是"无偿交出知识后被抛弃"。只要制度设计能让"创建Skills"变成对个人有利的行为——无论是通过版税、晋升、声望还是保障——Skills就会像开源软件一样自发涌现。


---

## 编译摘要

### 1. 浓缩
- **核心结论1**: Skills 沉淀制造了委托-代理困境——企业希望工程师蒸馏知识，但工程师清楚这等于训练替代品
  - 关键证据: 理性博弈导致消极抵抗、质量投毒、上下文污染三种对抗策略
- **核心结论2**: 问题根源是错误的激励结构——做正确的事对个体风险最高、收益最低时，任何道德说教无效
  - 关键证据: HAL 的 Agentic Skills 全生命周期综述回避了"谁有动力启动循环"的根本问题
- **核心结论3**: 破局需要五种激励重构：版税制（持续分润）、角色跃迁制（晋升阶梯）、对抗性蒸馏（自动观察）、竞技场（声望驱动）、组织保险（消除恐惧）
  - 关键证据: 类比开源软件——Linus 没被替代，Linux 成为影响力放大器

### 2. 质疑
- **关于"版税制"的质疑**: 版税计算依赖调用计量系统，技术实现复杂度可能抵消激励效果；且"复杂度系数"如何量化？
- **关于"角色跃迁制"的质疑**: 前提是企业有足够高阶工作吸纳释放的工程师，如果企业只是在降本，承诺不可信
- **关于数据可靠性的质疑**: 文章未提供任何实际企业案例或实验数据，所有方案都是理论设计

### 3. 对标
- **跨域关联1**: 与开源软件贡献者激励类似——声望和署名权是核心驱动力，而非金钱
- **跨域关联2**: 与知识产权法类似——版税制本质是"内部知识产权"，需要法律保障写入劳动合同
- **跨域关联3**: 与平台经济零工困境类似——劳动者担心"训练算法替代自己"（外卖骑手轨迹数据）

### 关联概念
- [[Adversarial-Distillation]]
- [[Agentic-Engineering]]
- [[朱少民]]
