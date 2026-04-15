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

将原始文章编译为结构化知识，采用三步编译法。

### 执行流程

```
1. 读取 raw source 内容
   └─ 检查 frontmatter 是否完整（author 字段必须存在且格式正确）
   └─ 验证 wikilink 使用 kebab-case 格式

2. 执行三步编译法（浓缩 → 质疑 → 对标）
   └─ 浓缩：提取核心结论（≤3条）+ 关键证据
   └─ 质疑：审视前提假设、数据可靠性、边界条件
   └─ 对标：跨领域找类似现象，建立知识迁移

3. 在原文件末尾追加编译摘要
   └─ 按照编译摘要输出模板格式

4. 为每个概念创建/更新 entity 页面
   └─ 写入 wiki/entities/
   └─ ⚠️ wikilink 必须使用 kebab-case 文件名格式（如 [[Vibe-Coding]]）
   └─ ⚠️ source_raw 必须使用短链接格式（纯文件名）
   └─ 如有冲突，在 entity 中标注冲突标记

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

### 三步编译法

当执行 compile 或 rebuild 时，对每篇文章执行：

#### 第一步：浓缩
- 应用"剃刀法则"：删除此信息会影响理解吗？不会就删
- 输出：核心结论（不超过 3 条）+ 支撑每条结论的关键证据
- 格式：每条结论一行，证据缩进在下方

#### 第二步：质疑
针对每条核心结论，回答：
1. 这个结论依赖哪些前提假设？
2. 如果这些前提不成立（换行业/换市场/换规模），结论还成立吗？
3. 作者的数据来源可靠吗？样本量、时间范围、地域限制？
4. 有没有作者没提到的反例或边界条件？

#### 第三步：对标
1. 其他领域有没有类似现象？（技术↔商业↔管理↔科学）
2. 这个知识可以迁移到哪些场景？
3. 如果有跨域关联，创建或更新对应的概念条目

#### 编译摘要输出模板

在原文件末尾追加：

```markdown
---

## 编译摘要

### 1. 浓缩
- **核心结论1**: xxx
  - 关键证据: xxx
- **核心结论2**: xxx
  - 关键证据: xxx
- **核心结论3**: xxx（可选）

### 2. 质疑
- **关于"结论1"的质疑**: xxx
- **关于"结论2"的质疑**: xxx
- **关于数据可靠性的质疑**: xxx（如有）

### 3. 对标
- **跨域关联1**: 此现象类似 [xxx领域]，可迁移到 yyy 场景
- **跨域关联2**: ...（如有）

### 关联概念
- [[概念A]]
- [[概念B]]
```

### 冲突标记模板

当同一概念在不同来源中出现矛盾时，在 Entity 页面添加：

```markdown
## 冲突标记

| 来源 | 观点 | 前提条件 |
|------|------|---------|
| [[文章A]] | xxx | yyy |
| [[文章B]] | xxx | zzz |

> [!warning] 前提条件不同，结论不可直接比较
```

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
| **一致性检查** | 同一概念在不同 Entity 中的定义是否冲突 | 列出冲突位置和建议统一方向 |
| **完整性检查** | Entity 是否包含必填字段（定义、关键数据点、前提与局限性、关联概念） | 标记缺失字段 |
| **孤岛检测** | 入链和出链都少于 2 的页面（仅实体 entities 和对比 comparisons，排除 outputs 和 topics） | 建议建立关联或合并 |
| **摘要覆盖检查** | raw/ 中哪些文件尚未包含编译摘要 | 列出待处理文件 |

---

### Entity 章节规范

**概念 Entity**（42 个，tags 不含 person）必须包含以下三个标准章节：
1. `## 关键数据点` — 从 raw 源提取的关键数据、统计、事实
2. `## 前提与局限性` — 概念成立的前提条件和适用边界
3. `## 关联概念` — 与其他概念的关系（统一标题，非"相关概念"/"外部链接"等变体）

**作者 Entity**（tags 含 person）不需要以上三章，但必须有：
- `validated_source` + `validated_at` frontmatter 字段

### Lint 评分计算规则

- 每个检查项按权重扣分（总分 100）
- 扣分必须对应具体缺失项数量，不应用主观权重
- 某检查项全部修复后必须恢复满分

### Lint 执行注意事项

- **Agent 结果必须用 grep 二次验证**（文件系统是真相，agent 可能基于过期缓存）
- 失效链接检查中，代码块内的 `[[wikilink]]` 占位符（如教程示例）不算真实断裂
- 评分报告必须列出具体扣分项及每项对应文件，不使用笼统描述

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
- ❌ 错误：`[[Vibe-Coding]]`、`[[Software-2.0]]`（空格格式会失效）

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
| `compile` | 编译 raw 中所有未处理的文件 |
| `compile <文件名>` | 编译指定文件 |
| `rebuild` | 重新编译全部 31 篇 Raw 文件（批量回溯） |
| `lint` | 执行完整 lint 检查（8 项检查，输出具体扣分和缺失文件清单） |
| `fix-lint` | 按 lint 报告逐项修复，输出修复前后对比 |
| `什么是 <概念>?` | 概念查询 |
| `关于 <主题> 有什么讨论?` | 主题查询 |

---

## 调试技巧

### 读取 git 状态中的 Unicode 文件名

```bash
# git status 显示的中文字符是编码格式，需要解码
python3 -c "import sys; print(sys.argv[1].encode().decode('unicode_escape').encode('latin1').decode('utf8'))" 'raw/文件名'
```

### Edit 工具常见问题

- 字符串匹配失败时，尝试读取精确行内容查看实际字符
- 可先更新其他字段（如 updated 日期）作为突破口
- index.md 编辑时注意统计数字和 footer 分开更新

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