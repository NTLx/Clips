---
type: log
layer: wiki
scope: wiki
created: 2026-04-09
---

# Wiki 层操作日志

记录所有 Wiki 层的操作：Ingest 编译、Entity 创建、Topic 更新等。

---

## 操作记录

### [2026-04-09] Ingest 执行

**已编译文章**：

| Raw Source | 生成的 Entity | 生成的 Topic |
|-----------|--------------|-------------|
| Good Taste the Only Real Moat Left.md | Taste, Judgment, Specificity | AI-Era-Taste-and-Judgment |

**Ingest 流程**：
1. 读取文章内容
2. 分析主题：AI 时代的人类竞争优势
3. 提取 3 个核心概念：Taste, Judgment, Specificity
4. 创建 Entity 页面（3 个）
5. 创建 Topic 页面（1 个）
6. 更新 index.md

**待编译**：剩余 14 篇文章

---

*日志更新: 2026-04-09*

---

### [2026-04-09] Ingest 执行 - AI-Agent 分类

**已编译文章**：

| Raw Source | 生成的 Entity | 生成的 Topic |
|-----------|--------------|-------------|
| Enabling agent-first process redesign.md | Agent-First-Enterprise, Human-Governor-Agent-Operator, Machine-Readable-Processes | Agent-First-Process-Redesign |
| The Conscious 1% Leading a new renaissance in the era of AI.md | Conscious-Creators, Inner-World-Mastery, Decision-Quality, Taste, Resonance | Conscious-Creation-in-AI-Era |
| Using Git with coding agents - Agentic Engineering Patterns.md | Git-Fluent-Agents, History-Rewriting, Agentic-Engineering | Git-with-Coding-Agents |

**Ingest 流程**：
1. 读取三篇 AI-Agent 分类文章
2. 分析主题：企业转型、人类潜能、软件工程
3. 提取 11 个核心概念
4. 创建 Entity 页面（11 个）
5. 创建 Topic 页面（3 个）
6. 更新 Entity 间关联关系

**Entity 关联矩阵**：
- Agent-First Enterprise ← Human-Governor-Agent-Operator, Machine-Readable-Processes
- Conscious-Creators ← Inner-World-Mastery, Decision-Quality, Taste, Resonance
- Git-Fluent-Agents ← History-Rewriting, Agentic-Engineering

---

*日志更新: 2026-04-09*

---

### [2026-04-09] Ingest 执行 - Claude-Code 分类

**已编译文章**：

| Raw Source | 生成的 Entity | 生成的 Topic |
|-----------|--------------|-------------|
| Claude code最小闭环核心文档 openclaw agent skill.md | Claude-Code-CLI, PTY-Mode, Headless-Mode | Claude-Code-Automation |
| OpenClaw + 6 个 Agent 运转半个月，从聊天到干活的完整工程实践.md | Context-Engineering, Multi-Layer-Memory, Three-State-Protocol | OpenClaw-Agent-System |
| OpenClaw + CodexClaudeCode Agent Swarm The One-Person Dev Team Full Setup.md | Agent-Orchestration, Agent-Swarm | OpenClaw-Agent-System |
| Openclaw自己操作Claude code完整开发了TikTok爆款分析系统.md | PTY-Mode (补充), Agent-Orchestration (补充) | Claude-Code-Automation |

**Ingest 流程**：
1. 读取四篇 Claude-Code 分类文章
2. 分析主题：Claude Code 自动化、OpenClaw Agent 系统
3. 提取 8 个核心概念
4. 创建 Entity 页面（8 个）
5. 创建 Topic 页面（2 个）
6. 建立 Entity 间关联关系

**Entity 关联矩阵**：
- Claude-Code-CLI ← PTY-Mode, Headless-Mode, Agent-Orchestration
- Agent-Orchestration ← Context-Engineering, Agent-Swarm, Three-State-Protocol
- Context-Engineering ← Multi-Layer-Memory, Claude-Code-CLI
- Agent-Swarm ← Agent-Orchestration, PTY-Mode

**Wiki 统计**：
- Entity 页面：13 个（新增 8 个）
- Topic 页面：6 个（新增 2 个）
- 总 Markdown 文件：17 个

---

*日志更新: 2026-04-09*

---

### [2026-04-09] Ingest 执行 - 其他分类

**已编译文章**：

| Raw Source | 生成的 Entity | 生成的 Topic |
|-----------|--------------|-------------|
| OpenClaw + seekdb skills：打造个人 seekdb 助手.md | OpenClaw (补充), seekdb | OpenClaw-Agent-System |
| 6 类岗位的必备 Skills 总结：用上的人正在甩开 90% 的同行.md | Wisdom-Work, Emotional-Clarity, Discernment | AI-Era-Career-Skills |
| 6 类岗位的必备 Skills 总结：用上的人正在甩开 90% 的同行（第二篇）.md | Connection, Agent-Orchestration (补充) | Wisdom-Work-Evolution |

**Ingest 流程**：
1. 读取 OpenClaw、Career-Skills 分类文章
2. 分析主题：个人工具、职业技能框架
3. 提取 5 个核心概念
4. 创建 Entity 页面（5 个）
5. 创建 Topic 页面（2 个）
6. 更新 Entity 间关联关系

**最终 Wiki 统计**：
- Entity 页面：28 个
- Topic 页面：8 个
- Raw Sources：15 篇（全部编译完成）

---

*日志更新: 2026-04-09*

---

### [2026-04-13] Ingest 执行 - Karpathy LLM Wiki

**已编译文章**：

| Raw Source | 生成的 Entity | 生成的 Topic |
|-----------|--------------|-------------|
| 20260413-llm-wiki.md | Andrej-Karpathy, Software-2.0, Memex, Knowledge-Compilation | Karpathy-AI-Thought |

**Ingest 流程**：
1. 剪藏 Karpathy 的 LLM Wiki 设计文档（GitHub Gist）
2. 联网检索验证作者身份（karpathy.ai + Tavily）
3. 分析主题：LLM Wiki 设计模式、知识管理范式
4. 提取 4 个核心概念（不含已有 Vibe-Coding）
5. 创建 Entity 页面（4 个新 entity）
6. 创建 Topic 页面（整合 Karpathy 思想体系）
7. 更新 Comparison 页面（RAG-vs-LLM-Wiki）
8. 更新 Vibe-Coding entity（添加 Karpathy 来源）

**Entity 关联矩阵**：
- Andrej-Karpathy ← Software-2.0, Vibe-Coding, LLM-Wiki, Memex
- Software-2.0 ← Vibe-Coding, Agentic-Engineering, Coding-Agents
- Knowledge-Compilation ← RAG-vs-LLM-Wiki, Context-Engineering
- Memex ← Knowledge-Work, RAG-vs-LLM-Wiki

**Karpathy 核心贡献识别**：
- OpenAI 创始团队成员、Tesla AI 前总监
- CS231n 课程创建者（"深度学习圣经"）
- Software 2.0 概念提出者（编程范式转变）
- Vibe Coding 术语创造者（2025）
- LLM Wiki 设计模式提出者（2026）
- Eureka Labs 创始人（2024，AI 教育）

**Wiki 统计更新**：
- Entity 页面：67 个（新增 4 个）
- Topic 页面：9 个（新增 1 个）
- Comparison 页面：5 个（更新 1 个）

---

*日志更新: 2026-04-13*

---

### [2026-04-13] Output 创建 - 部署教程

**创建文件**：
- `wiki/outputs/deploy-obsidian-wiki-with-quartz.md`

**Output 类型**：Tutorial

**内容概述**：
- 从 Memex 到 LLM Wiki 的理念介绍
- 本知识库三层架构设计
- Quartz 核心配置详解（quartz.config.ts + quartz.layout.ts）
- GitHub Actions 自动部署 workflow
- Markdown 文档格式规范
- 效果展示：Clips 知识库网站 (https://ntlx.github.io/Clips/)

**章节结构**（线性叙事）：
1. 第1章：缘起 —— 从 Memex 到 LLM Wiki
2. 第2章：架构 —— 本知识库的设计
3. 第3章：配置 —— Quartz 核心文件详解
4. 第4章：部署 —— GitHub Actions 自动化
5. 第5章：写作 —— Markdown 文档格式
6. 第6章：成果 —— 最终效果与进阶

**代码示例**：
- quartz.config.ts（完整配置 + 注释）
- quartz.layout.ts（完整布局 + 注释）
- deploy.yml（完整 GitHub Actions workflow）
- Markdown 格式示例（frontmatter、wikilinks、callouts）

**Wiki 统计更新**：
- Output 页面：1 个（新增）
- Entity 页面：69 个
- Topic 页面：12 个

---

*日志更新: 2026-04-13*

---

### [2026-04-13] Entity 修正 - Andrej-Karpathy 时间与排序

**修正文件**：
- `wiki/entities/Andrej-Karpathy.md`
- `wiki/outputs/deploy-obsidian-wiki-with-quartz.md`
- `index.md`

**修正内容**：

| 问题 | 原内容 | 修正后 |
|-----|--------|--------|
| 教程 LLM Wiki 提出时间 | "2024 年提出 LLM Wiki" | "2026 年提出 LLM Wiki" |
| Entity definition 缺少 LLM Wiki | "提出 Software 2.0 和 Vibe Coding 概念" | "提出 Software 2.0（2017）、Vibe Coding（2025）、LLM Wiki（2026）三大概念" |
| 职业履历排序错误 | Tesla → OpenAI → Eureka Labs → Stanford | Stanford → OpenAI → Tesla → Eureka Labs（按时间顺序） |
| OpenAI 时间段表述不清 | "2015-2017, 2023" | "2015-2017（创始），2023（返回）" |
| Software 2.0 缺少时间标注 | 无标注 | "(2017)" |
| index.md 两处定义不一致 | 分别写不同描述 | 统一包含三大概念 |

**职业履历正确排序（按时间）**：
1. Stanford (2011-2015) - PhD/CS231n
2. OpenAI (2015-2017, 2023) - 创始成员
3. Tesla (2017-2022) - Director of AI
4. Eureka Labs (2024) - Founder

**概念创新正确排序（按提出时间）**：
1. Software 2.0 (2017)
2. Vibe Coding (2025)
3. LLM Wiki (2026)

---

*日志更新: 2026-04-13*

---

### [2026-04-13] Schema 更新 - 时间与事实规范

**更新文件**：
- `CLAUDE.md`

**新增章节**："时间与事实规范"

**新增内容**：

### 时间标注
- 概念/事件必标注年份
- 时间线表格按时间排序
- 跨文件一致性要求

### 事实核查
- 年份验证必须联网确认
- 人物贡献对齐职业履历
- 时间信息优先级高于描述性信息

**新增原因**：本次会话中发现 LLM Wiki 提出年份错误（2024→2026）、职业履历排序混乱、时间标注缺失等问题，需要在 Schema 层明确规范以防止类似错误。

---

### [2026-04-14] Ingest 执行 - LLM Wiki 3.0 实战升级

**Raw Source**：一篇文章卖了20万，开源CC+Obsidian打造的LLM Wiki 内容创作3.0系统.md

**内容概述**：
- 饼干哥哥分享从 2.0（Runtime RAG）到 3.0（Compile-time Wiki）的完整升级
- 20万销售额的真实案例
- 三步编译法（浓缩 → 质疑 → 对标）的完整提示词
- 知识库健康检查四维度（一致性、完整性、孤岛检测、跨目录一致性）

**更新文件**：

| 文件 | 操作类型 | 更新内容 |
|-----|---------|---------|
| wiki/entities/Andrej-Karpathy.md | 更新 | 添加 source_raw 引用、关联饼干哥哥 |
| wiki/entities/Knowledge-Compilation.md | 更新 | 添加"三步编译法"章节、source_raw |
| wiki/topics/Karpathy-AI-Thought.md | 更新 | 添加"内容创作3.0"章节、source_raw |
| index.md | 更新 | 统计数字（30→31）、更新时间、饼干哥哥描述 |
| wiki/log.md | 更新 | 添加本日志条目 |

**核心概念提取**：

| 概念 | 类型 | 说明 |
|-----|------|------|
| 内容创作3.0 | 新概念 | 从 Runtime RAG 到 Compile-time Wiki 的升级 |
| 三步编译法 | 新方法 | 浓缩→质疑→对标，饼干哥哥的改进方案 |
| 知识质疑 | 新步骤 | 验证前提假设、边界条件、反例 |
| 跨域洞察 | 新步骤 | 对标找类似现象，如链条可靠性递减 |

**触及范围**：5 个文件

**待编译**：无

---

*日志更新: 2026-04-14*

*日志更新: 2026-04-13*