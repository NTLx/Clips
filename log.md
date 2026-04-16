---
type: log
layer: main
scope: Clips
created: 2026-04-09
---

# Clips 知识库主日志

记录 Clips 知识库的所有操作：Ingest、Query、Lint 等。

---

## 操作记录

### [2026-04-09] 初始化 LLM Wiki 架构

**Phase 0 完成**：
- OpenClaw官方文档 移出到根目录，独立为专项知识库

**Phase 1 完成**：
- 创建两层目录结构：raw/, wiki/
- raw 目录扁平化（所有文章直接存放）
- 创建 Wiki 层子目录：entities, topics, comparisons, outputs

**待执行**：
- [ ] Phase 2: 编写 CLAUDE.md Schema 文件
- [ ] Phase 3: 迁移未整理文章
- [ ] Phase 4: 执行 Ingest 编译

---

*日志创建: 2026-04-09*
## 2026-04-15: 编译 — 每月$20成本，$60000+营收：加拿大程序员的"最穷"技术栈

- **来源**: https://mp.weixin.qq.com/s/eTFOY-gtZxNJr8lRHGf6pg (微信公众号，刘小排)
- **编译方式**: 标准路径（三步编译法）
- **新增 Entity (7 个)**:
  - [[Steve-Hanov]] (person) — 加拿大 Waterloo 独立开发者
  - [[Lean-Stack]] — $20/月极简技术栈：VPS + SQLite + Go + systemd
  - [[Runway-Math]] — 生存时间 = 资金 ÷ 月支出，控制分母
  - [[Anti-Enterprise-Mindset]] — 拒绝预优化，不买"万一"的账
  - [[B2B-Nurture-C-Model]] — B2B 养 C 端的抗周期产品组合
  - [[Time-Moat]] — 多年运营积累的 SEO + 品牌 + 信任壁垒
  - [[Constraint-Driven-Engineering]] — 先设定约束，再从约束出发选技术
- **新增 Topic (1 个)**:
  - [[wiki/topics/Lean-Indie-Engineering\|精益独立开发]] — 整合 7 个相关 Entity
- **索引更新**: 58→65 entities, 12→13 topics, 24→25 raw articles
- **编译摘要**: 3 条核心结论 + 5 条质疑 + 3 条跨域对标

---

## 2026-04-16: 编译 — Karpathy AI 能力鸿沟帖

- **来源**: https://x.com/karpathy/status/2042334451611693415 (X/Twitter, Andrej Karpathy)
- **编译方式**: 标准路径（三步编译法）+ 附加思考整合
- **附加资料**: 池建强微信公众号 + 墨问笔记（人群分层、核心洞察、社区讨论）
- **新建 Entity (2 个)**:
  - [[AI-Psychosis]] — 付费前沿 agentic 模型用户对 AI 编程能力跃迁的极度震撼
  - [[AI-Capability-Gap]] — 同一技术在不同用户群体中的能力鸿沟，形成两条平行认知现实
- **更新 Entity (4 个)**:
  - [[Andrej-Karpathy]] — 新增 source_raw + AI-Psychosis/AI-Capability-Gap 关联
  - [[Vibe-Coding]] — 新增 source_raw + AI-Capability-Gap/AI-Psychosis 关联
  - [[Software-2.0]] — 新增 source_raw + AI-Capability-Gap/AI-Psychosis 关联
  - [[Claude-Code-CLI]] — 新增 source_raw
- **更新 Topic (1 个)**:
  - [[wiki/topics/Karpathy-AI-Thought\|Karpathy AI 思想体系]] — 新增 AI-Capability-Gap、AI-Psychosis 概念矩阵 + 相关实体引用
- **索引更新**: 67→69 entities，25→26 raw articles
- **编译摘要**: 3 条核心结论 + 5 条质疑 + 3 条跨域对标

---

## 2026-04-14: Lint 修复

- **失效链接**: 修复 18 处 ASCII/Unicode 撇号不匹配 (Knowledge Work Is Dying...)
- **source_raw 补充**: 8 个实体（Claude-Code-CLI, Headless-Mode, Technical-Debt-Avoidance, Elvis-Sun, Ethan-Mollick, Konstantine-Buhler, Paul-Graham, Raj-Nandan-Sharma）
- **孤儿消除**: 18 个孤儿 → 0，通过 7 个 topic 页面新增 related_entities 引用
- **孤岛修复**: Paul-Graham 补充 source_raw + 3 个相关实体 + topic 引用
- **作者验证**: 15 个作者 entity 新增 validated_source / validated_at
- **健康度**: 72/100 → 96/100

---

## 2026-04-16: 剪藏 → 编译 — Why Your "AI-First" Strategy Is Probably Wrong

- **来源**: https://x.com/intuitiveml/status/2043545596699750791 (X/Twitter, Peter Pang / @intuitiveml)
- **中文翻译**: 微信公众号 ThinkInAI社区 2026-04-15 发布
- **编译方式**: 标准路径（三步编译法） + Entity 创建
- **新建 Entity (2 个)**:
  - [[Harness-Engineering]] — 让 AI Agent 成为主要构建者的完整系统框架（OpenAI 2026.02 提出概念，CREAO 实践案例）
  - [[AI-First]] — 围绕"AI 是主要构建者"重新设计流程、架构和组织的全职能范式
- **更新 Entity (3 个)**:
  - [[Vibe-Coding]] — 追加 Harness-Engineering 关联 + 新增 source_raw
  - [[Agentic-Engineering]] — 追加 Harness-Engineering 关联 + 新增 source_raw
  - [[Machine-Readable-Processes]] — 追加 Harness-Engineering 关联 + 新增 source_raw
- **更新 Topic (1 个)**:
  - [[wiki/topics/Agentic-Engineering-Patterns\|Agentic Engineering Patterns]] — 追加 AI-First → Harness Engineering 演进展节
- **索引更新**: 65→67 entities
- **编译摘要**: 3 条核心结论 + 5 条质疑 + 3 条跨域对标（[[Constraint-Driven-Engineering]], [[Always-On-Economy]], [[Decision-Quality]]）
- **备注**: 重复的微信公众号中文翻译文件已删除，保留英文原文为唯一 Raw source

---

## 2026-04-16: 剪藏 Karpathy X 帖 → 优化 + 附加思考

- **来源**: https://x.com/karpathy/status/2042334451611693415 (X/Twitter, Andrej Karpathy / @karpathy)
- **附加资料**:
  - 池建强微信公众号文章: https://mp.weixin.qq.com/s/OArrjAbDpinIADQzmymsVA
  - 池建强墨问笔记: https://note.mowen.cn/detail/wVRtr2XSutpQQZTnKnX5W
- **操作类型**: 剪藏完善（通过 web-access 获取原文 + 附加思考）
- **优化文件**:
  - 文件名: `Thread by @karpathy.md` → `20260409-ai-capability-gap-ai-psychosis.md`
  - 提取 X Thread 相关回复（Karpathy 补充 / NBER 数据 / Raschka 评论）
  - 追加池建强分析（人群分层：完全不用 → 免费用户 → 付费专业 → 顶尖 Researcher）
  - 追加墨问社区讨论精选（普通人应对策略讨论）
- **附加元数据**: `engagement`（1.1 万 likes / 1.9 万 RTs）, `related_commentary`（池建强微信/墨问链接）
- **Tags**: clippings / ai-gap / ai-psychosis / agentic-models / chi-jianqiang
- **更新 Entity (2 个)**:
  - [[Andrej-Karpathy]] — 新增 `source_raw` 引用 + `[[AI-Psychosis]]` / `[[AI-Capability-Gap]]` 关联
  - [[AI-Psychosis]] — 新建（Karpathy 提出的 AI 狂热概念）
- **编译摘要**: 追加三步编译法（浓缩/质疑/对标）到 raw 文档
