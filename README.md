# Clips LLM Wiki Schema

本文档定义 Clips 知识库的架构、工作流和规范，指导 AI Agent 运营和维护这个 LLM Wiki。

---

## 知识库定位

Clips 是一个**大杂烩文章剪藏 Wiki**，收集各类有价值的网络文章，通过 LLM Wiki 模式实现：

- **知识编译**：将原始文章提炼为结构化知识
- **概念提取**：从文章中提取核心概念，建立 entity 页面
- **持续累积**：每次编译都沉淀到 wiki 层，避免重复处理

### 技术平台

Clips 是一个 **Obsidian 知识库**，AI Agent 应遵循以下原则：

- **使用 Obsidian 技能**：进行文档编辑、链接管理、图谱操作等工作时，优先使用 Obsidian 相关技能
- **遵循 Obsidian 规范**：文档格式使用 Wikilinks (`[[文件名]]`)、Obsidian Callouts、YAML Frontmatter 等
- **无法使用时告知用户**：如果当前环境不支持 Obsidian 技能，应及时告知用户，避免使用不兼容的操作方式

---

## 三层架构

```
┌─────────────────────────────────────────────────────────────────┐
│                    Clips LLM Wiki 架构                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Layer 0: Raw Sources (00-raw/)                                │
│  ├── inbox/          快速捕获入口，新文章先放这里               │
│  ├── web-clips/      已分类的 Web 剪藏                         │
│  │   ├── AI-Agent/   AI 与 Agent 相关文章                      │
│  │   ├── Claude-Code/ Claude Code 相关文章                     │
│  │   ├── Career-Skills/ 职业技能相关文章                       │
│  │   ├── Knowledge-Work/ 知识工作相关文章                      │
│  │   ├── General/     通用思想文章                             │
│  │   └── OpenClaw/    OpenClaw 相关文章                        │
│  └── pdf-docs/       PDF 文档                                  │
│                                                                 │
│  Layer 1: Wiki (10-wiki/) ← LLM 维护层                         │
│  ├── entities/       概念页面（从文章提取的核心概念）           │
│  ├── topics/         主题页面（整合多篇文章的主题）             │
│  ├── comparisons/    对比分析页面                              │
│  └── outputs/        输出作品（博客、笔记等）                   │
│                                                                 │
│  Layer 2: Schema (README.md) ← 当前文件                        │
│  定义工作流、规范、约定                                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 各层职责

| 层级 | 职责 | 维护者 |
|-----|------|-------|
| **Raw Sources** | 存储原始文章，不可变 | 用户 |
| **Wiki** | 结构化知识，可更新 | **AI Agent** |
| **Schema** | 工作流定义、规范 | 用户 + AI Agent |

---

## Ingest 工作流（知识编译）

将原始文章编译为结构化知识。

### 触发条件

```
- 用户添加新文件到 00-raw/inbox/
- 用户请求 "compile <文件名>"
- 用户请求 "compile all" 批量处理
- 用户请求 "compile inbox" 处理收件箱
```

### 执行流程

```
1. 读取 raw source 内容
   └─ 检查 frontmatter 是否完整

2. 分析主题，确定分类
   └─ AI-Agent / Claude-Code / Career-Skills / ...

3. 提取 3-5 个核心概念
   └─ 识别文章中的关键术语、方法论、技术概念

4. 为每个概念创建/更新 entity 页面
   └─ 写入 10-wiki/entities/

5. 创建/更新 topic 页面
   └─ 整合文章要点，写入 10-wiki/topics/

6. 更新 index.md
   └─ 添加新的 entity 和 topic 条目

7. 记录到 log.md
   └─ 记录编译操作详情

8. 移动 raw source 到对应分类目录
   └─ 从 inbox/ 移到 web-clips/{分类}/
```

### 示例

**Raw Source**: `00-raw/inbox/knowledge-work-dying.md`

**执行 Ingest 后**：

| 输出 | 内容 |
|-----|------|
| Entity 页面 | `Knowledge-Work.md`, `AI-Displacement.md`, `Human-Moat.md` |
| Topic 页面 | `Knowledge-Work-Evolution.md` |
| 索引更新 | index.md 添加新条目 |
| 日志记录 | log.md 记录操作 |
| 文件移动 | inbox/ → web-clips/Knowledge-Work/ |

---

## Query 工作流（知识检索）

### 检索优先级

```
1. Schema (README.md)  → 了解知识库边界和结构
2. index.md            → 快速定位相关内容
3. Entity pages        → 概念定义和关联
4. Topic pages         → 主题深度分析
5. Raw sources         → 原始证据（仅溯源时）
```

### 查询模式

| 模式 | 示例查询 | 检索路径 |
|-----|---------|---------|
| 概念查询 | "什么是 Knowledge Work?" | Schema → index → Entity → Raw |
| 主题查询 | "关于 AI 替代有什么讨论？" | Schema → index → Topic → Entities |
| 对比查询 | "A 和 B 有什么区别？" | Schema → index → comparisons |
| 溯源查询 | "这个观点来自哪篇文章？" | Wiki → Raw → source URL |

### 响应格式

```markdown
## 直接回答
{一句话核心答案}

## 详细解释
{来自 entity/topic 页面的内容}

## 相关概念
- [[entity-A]] - 关系说明
- [[entity-B]] - 关系说明

## 扩展阅读
- [[topic-X]] - 深入了解
- [[00-raw/web-clips/.../文章]] - 原始文章

## 来源
- 原始链接: {source URL}
```

---

## Lint 工作流（知识审计）

### 检查项

| 检查项 | 频率 | 条件 | 处理方式 |
|-------|------|------|---------|
| Raw backlog | 每次 | inbox/ 中超过 7 天的文件 | 提醒 compile |
| 孤儿 entity | 每周 | 无 topic 页面引用的 entity | 关联到相关 topic |
| 过期 entity | 每月 | 超过 30 天未更新的 entity | 检查是否需要更新 |
| 失效链接 | 每月 | wikilinks 指向不存在的页面 | 修复或删除链接 |

### Lint 报告格式

```markdown
---
type: lint-report
date: {YYYY-MM-DD}
---

# Lint Report - {YYYY-MM-DD}

## 健康度

| 指标 | 数值 | 状态 |
|-----|------|-----|
| Raw backlog | {n} items | 🟢/🟡/🔴 |
| 孤儿 entity | {n} items | 🟢/🟡/🔴 |
| 过期 entity | {n} items | 🟢/🟡/🔴 |
| 失效链接 | {n} items | 🟢/🟡/🔴 |

## 需要处理

{列出需要处理的问题}

## 建议操作

- [ ] Compile 00-raw/inbox/xxx.md
- [ ] 将 xxx entity 关联到相关 topic
- [ ] 更新过期 entity
```

### 触发 Lint

```
用户请求 "lint" 或 "lint check"
```

---

## 文件命名规范

### Raw Sources

```
格式: {YYYYMMDD}-{关键词}.md
示例: 20260408-knowledge-work-dying.md

注意:
- 中文标题可保留原样
- 必须包含 YAML frontmatter
```

### Entity Pages

```
格式: {概念名}.md (英文，kebab-case)
示例: Knowledge-Work.md, AI-Agent.md, Human-Moat.md
```

### Topic Pages

```
格式: {主题名}.md
示例: Knowledge-Work-Evolution.md, AI-Agent-Development.md
```

### Comparison Pages

```
格式: {概念A}-vs-{概念B}.md
示例: RAG-vs-LLM-Wiki.md, PTY-Mode-vs-Headless-Mode.md
```

---

## YAML Frontmatter 规范

### Raw Sources

```yaml
---
type: raw
source: "https://example.com/article"
author:
  - "作者名"
published: "2026-04-08"
created: "2026-04-08"
tags:
  - clippings
  - {主题标签}
description: "文章简介"
---
```

### Entity Pages

```yaml
---
type: entity
title: {概念名}
definition: "{一句话定义}"
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
tags:
  - {领域}
related_entities:
  - "[[相关概念A]]"
  - "[[相关概念B]]"
source_raw:
  - "[[../00-raw/web-clips/xxx/文章名]]"
---
```

### Topic Pages

```yaml
---
type: topic
title: {主题名}
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
tags:
  - {领域}
related_entities:
  - "[[entities/概念A]]"
  - "[[entities/概念B]]"
source_raw:
  - "[[../00-raw/web-clips/xxx/文章1]]"
  - "[[../00-raw/web-clips/xxx/文章2]]"
---
```

### Comparison Pages

```yaml
---
type: comparison
title: {概念A} vs {概念B}
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
tags:
  - {领域}
related_entities:
  - "[[entities/概念A]]"
  - "[[entities/概念B]]"
---
```

---

## 操作命令

### Ingest（编译）

```
compile                    # 编译 inbox 中所有文件
compile <文件名>           # 编译指定文件
compile inbox              # 同 compile
compile <分类>             # 编译指定分类的所有文件
```

### Query（查询）

```
什么是 <概念>?             # 概念查询
关于 <主题> 有什么讨论?     # 主题查询
<概念A> 和 <概念B> 有什么区别?  # 对比查询
<观点> 来自哪篇文章?        # 溯源查询
```

### Lint（审计）

```
lint                       # 执行完整 lint 检查
lint backlog               # 只检查 raw backlog
lint orphans               # 只检查孤儿 entity
lint links                 # 只检查失效链接
```

### Status（状态）

```
status                     # 显示知识库状态
stats                      # 显示统计数据
```

---

## 关键文件

| 文件 | 用途 |
|-----|------|
| `README.md` | Schema 文件，定义工作流和规范 |
| `index.md` | 知识库索引，列出所有 entity/topic/comparison |
| `log.md` | 操作日志，记录所有编译和审计操作 |
| `10-wiki/lint-report.md` | 最新 lint 报告 |