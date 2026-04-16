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
