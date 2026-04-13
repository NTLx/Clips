# Clips LLM Wiki Schema

本文档定义 Clips 知识库的架构、工作流和规范，指导 AI Agent 运营和维护这个 LLM Wiki。

---

## 知识库定位

Clips 是一个**大杂烩文章剪藏 Wiki**，收集各类有价值的网络文章，通过 LLM Wiki 模式实现：

- **知识编译**：将原始文章提炼为结构化知识
- **概念提取**：从文章中提取核心概念，建立 entity 页面
- **持续累积**：每次编译都沉淀到 wiki 层，避免重复处理

---

## 两层架构

```
┌─────────────────────────────────────────────────────────────────┐
│                    Clips LLM Wiki 架构                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Layer 0: Raw Sources (raw/)                                   │
│  ├── 所有剪藏文章直接存放于此（扁平结构）                       │
│  └─ log.md          Raw 层操作日志                              │
│                                                                 │
│  Layer 1: Wiki (wiki/) ← LLM 维护层                            │
│  ├── entities/       概念页面（从文章提取的核心概念）           │
│  ├── topics/         主题页面（整合多篇文章的主题）             │
│  ├── comparisons/    对比分析页面                              │
│  ├── outputs/        输出作品（博客、笔记等）                   │
│  └─ lint-report.md   Lint 报告                                 │
│                                                                 │
│  Schema (README.md) ← 当前文件                                 │
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

### 执行流程

```
1. 读取 raw source 内容
   └─ 检查 frontmatter 是否完整（author 字段必须存在且格式正确）
   └─ 验证 wikilink 使用 kebab-case 格式

2. 分析主题，确定分类
   └─ AI-Agent / Claude-Code / Career-Skills / ...

3. 提取 3-5 个核心概念
   └─ 识别文章中的关键术语、方法论、技术概念
   └─ 核心概念表格标注"已有 Entity ✅"或"新建"

4. 为每个概念创建/更新 entity 页面
   └─ 写入 wiki/entities/
   └─ ⚠️ wikilink 必须使用 kebab-case 文件名格式（如 [[Vibe-Coding]]）
   └─ ⚠️ source_raw 必须使用短链接格式（纯文件名）

5. 创建/更新 topic 页面
   └─ 写入 wiki/topics/

6. 更新 comparisons（如有对比概念）
   └─ 添加新论述、关联已有 entity

7. 更新 index.md
   └─ 添加新的 entity 和 topic 条目

8. 记录到 log.md
   └─ 记录编译操作详情
```

**触及范围**：单篇 source 编译可能影响 10-15 个 wiki 页面
- 新建 entities（3-5 个）
- 更新相关 entities（添加关联）
- 创建/更新 topic（整合主题）
- 更新 comparisons（如有对比）
- 更新 index.md
- 记录到 log.md

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

---

## Lint 工作流（知识审计）

### 检查项

| 检查项 | 条件 | 处理方式 |
|-------|------|---------|
| Raw backlog | raw/ 中超过 7 天的文件 | 提醒 compile |
| 孤儿 entity | 无 topic 页面引用的 entity | 关联到相关 topic |
| 失效链接 | wikilinks 指向不存在的页面 | 修复或删除链接 |

---

## 文件命名规范

| 类型 | 格式 | 示例 |
|-----|------|------|
| Raw Sources | `{YYYYMMDD}-{关键词}.md` 或原标题 | `20260408-knowledge-work-dying.md` |
| Entity Pages | `{概念名}.md` (kebab-case) | `Knowledge-Work.md` |
| Topic Pages | `{主题名}.md` | `Knowledge-Work-Evolution.md` |
| Comparison Pages | `{概念A}-vs-{概念B}.md` | `RAG-vs-LLM-Wiki.md` |

---

## YAML Frontmatter 规范

### Raw Sources

```yaml
---
type: raw
source: "https://example.com/article"
author:
  - "[[Author-Name]]"  # ⚠️ 必须使用 kebab-case 文件名格式（而非 "Author Name"）
  - "作者名"           # 不存在时用纯文本
published: "2026-04-08"
created: "2026-04-08"
tags:
  - clippings
  - {主题标签}
---
```

**相关链接部分结构**（知识图谱链接）：
- 作者 Entity: `[[Author-Name]]`
- 相关概念 entities: `[[Concept-A]], [[Concept-B]]`
- 思想先驱: `[[Memex]]`（如有历史关联）
- 对比分析: `[[Concept-A-vs-Concept-B]]`
- 思想体系 topic: `[[Topic-Name]]`

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
  - "[[Concept-A]]"  # ⚠️ 必须使用 kebab-case 文件名格式
source_raw:
  - "[[文章名]]"  # ⚠️ 短链接格式（纯文件名，不含路径）
---
```

**Wikilink 格式规范**：
- ✅ 正确：`[[Vibe-Coding]]`、`[[Software-2.0]]`、`[[Andrej-Karpathy]]`
- ❌ 错误：`[[Vibe Coding]]`、`[[Software 2.0]]`（空格格式会失效）

### Author Entity Pages

```yaml
---
type: entity
title: {Author Name}
definition: "{一句话定义作者身份}"
validated_source: "https://验证来源URL"
validated_at: "2026-04-13"
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
tags:
  - {领域}
source_raw:
  - "[[文章名]]"
---
```

**Author Entity 工作流**：
1. 使用 BrowserOS 搜索验证作者身份
2. 记录验证来源 URL 和日期
3. 无法验证时，文章 author 使用纯文本

---

## Quartz 网站部署

Clips 通过 Quartz 自动部署为 GitHub Pages 网站。

### 关键配置

- **部署方案**: 仓库根目录作为 content，通过 `ignorePatterns` 排除无关文件
- **链接解析**: `markdownLinkResolution: "shortest"` 支持短链接跨目录

### ignorePatterns 排除内容

- 系统文件：`.obsidian`, `.git`, `.DS_Store`
- 配置文件：`package.json`, `quartz.config.ts`, `tsconfig.json`
- Schema 文件：`README.md`, `CLAUDE.md`, `AGENTS.md`（兼容其他 AI 工具）
- 日志文档：`log.md`, `lint-report.md`
- 其他目录：`docs`, `node_modules`

---

## 时间与事实规范

### 时间标注

- **概念/事件必标注年份**：如 "Software 2.0 (2017)"、"Vibe Coding (2025)"
- **时间线表格按时间排序**：职业履历、概念创新等表格必须按年份升序排列
- **跨文件一致性**：同一概念在 definition、正文、index.md 中年份标注必须一致

### 事实核查

- **年份验证**：涉及历史事件、概念提出年份时，必须联网确认确切日期
- **人物贡献对齐**：概念提出年份需与作者职业履历时间线匹配
- **优先级**：时间信息 > 描述性信息，年份错误比描述模糊更严重

---

## 操作命令

| 命令 | 说明 |
|-----|------|
| `compile` | 编译 raw 中所有文件 |
| `compile <文件名>` | 编译指定文件 |
| `lint` | 执行完整 lint 检查 |
| `什么是 <概念>?` | 概念查询 |
| `关于 <主题> 有什么讨论?` | 主题查询 |

---

## 关键文件

| 文件 | 用途 |
|-----|------|
| `README.md` | Schema 文件，定义工作流和规范 |
| `AGENTS.md` | README.md 软链接，兼容其他 AI Coding 工具 |
| `index.md` | 知识库索引 |
| `log.md` | 操作日志 |
| `wiki/lint-report.md` | 最新 lint 报告 |

---

*本文件由 Claude Code 维护，用于指导 AI Agent 在 Clips LLM Wiki 中的工作。*