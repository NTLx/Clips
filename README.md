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

## 两层架构

```
┌─────────────────────────────────────────────────────────────────┐
│                    Clips LLM Wiki 架构                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Layer 0: Raw Sources (raw/)                                   │
│  ├── 所有剪藏文章直接存放于此（扁平结构）                       │
│  ├── pdf-docs/       PDF 文档                                  │
│  └─ log.md          Raw 层操作日志                              │
│                                                                 │
│  Layer 1: Wiki (wiki/) ← LLM 维护层                            │
│  ├── entities/       概念页面（从文章提取的核心概念）           │
│  ├── topics/         主题页面（整合多篇文章的主题）             │
│  ├── comparisons/    对比分析页面                              │
│  ├── outputs/        输出作品（博客、笔记等）                   │
│  └─ lint-report.md   Lint 报告                                 │
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
- 用户添加新文件到 raw/
- 用户请求 "compile <文件名>"
- 用户请求 "compile all" 批量处理
```

### 执行流程

```
1. 读取 raw source 内容
   └─ 检查 frontmatter 是否完整

2. 分析主题，确定分类
   └─ AI-Agent / Claude-Code / Career-Skills / ...

3. 提取 3-5 个核心概念
   └─ 识别文章中的关键术语、方法论、技术概念

4. **文章关联验证**
   ├─ 检查 raw source 的 author 字段格式
   ├─ 若 author 为 wikilink `[[Author Name]]`：
   │  ├─ 验证 `wiki/entities/{Author-Name}.md` 存在
   │  ├─ 验证 entity 的 `source_raw` 包含当前文章文件名
   │  ├─ 若不一致：停止编译，输出错误信息：
   │  │  ⚠️ 文章关联验证失败
   │  │  文章: {当前文章名}
   │  │  作者 entity: {Author Name}
   │  │  entity.source_raw: {现有内容}
   │  │  应包含: {当前文章文件名}
   │  │  请手动修复后重新执行 compile
   │  └─ 一致则继续
   └─ 若 author 为纯文本：
      ├─ 触发 Author Entity 工作流（见上方）
      └─ 验证通过后才继续编译

5. 为每个概念创建/更新 entity 页面
   └─ 写入 wiki/entities/
   └─ ⚠️ source_raw 必须使用短链接格式，禁止使用相对路径

6. 创建/更新 topic 页面
   └─ 写入 wiki/topics/

7. 更新 index.md
   └─ 添加新的 entity 和 topic 条目

8. 记录到 log.md
   └─ 记录编译操作详情
```

### 示例

**Raw Source**: `raw/knowledge-work-dying.md`

**执行 Ingest 后**：

| 输出 | 内容 |
|-----|------|
| Entity 页面 | `Knowledge-Work.md`, `AI-Displacement.md`, `Human-Moat.md` |
| Topic 页面 | `Knowledge-Work-Evolution.md` |
| 索引更新 | index.md 添加新条目 |
| 日志记录 | log.md 记录操作 |

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
- [[raw/文章]] - 原始文章

## 来源
- 原始链接: {source URL}
```

---

## Lint 工作流（知识审计）

### 检查项

| 检查项 | 频率 | 条件 | 处理方式 |
|-------|------|------|---------|
| Raw backlog | 每次 | raw/ 中超过 7 天的文件 | 提醒 compile |
| 孤儿 entity | 每周 | 无 topic 页面引用的 entity | 关联到相关 topic |
| 过期 entity | 每月 | 超过 30 天未更新的 entity | 检查是否需要更新 |
| 失效链接 | 每月 | wikilinks 指向不存在的页面 | 修复或删除链接 |
| **Wikilink 格式** | 每月 | related_entities 使用空格而非连字符 | 标记为建议改进 |

### 失效链接类型

| 类型 | 示例 | 修复方式 |
|-----|------|---------|
| Entity 缺失 | `[[Coding-Agents]]` 不存在 | 创建 entity 页面 |
| 类型错误 | Topic 作为 Entity 引用 | 修正链接或创建正确类型 |

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

- [ ] Compile raw/xxx.md
- [ ] 将 xxx entity 关联到相关 topic
- [ ] 更新过期 entity
```

### 触发 Lint

```
用户请求 "lint" 或 "lint check"
```

### Lint 修复流程

1. **创建缺失 Entity**：`related_entities` 引用但不存在的 entity
2. **更新 index.md**：新增 entity 条目和统计数字
3. **更新 lint-report.md**：记录修复结果和健康度

---

## 文件命名规范

### Raw Sources

```
格式: {YYYYMMDD}-{关键词}.md 或原文章标题
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
  - "[[Author Name]]"  # 当 entity 页面存在时使用 wikilink
  - "作者名"           # 当 entity 页面不存在时使用纯文本
published: "2026-04-08"
created: "2026-04-08"
tags:
  - clippings
  - {主题标签}
description: "文章简介"
---

# Author 字段规范
# - 只包含作者姓名或 wikilink，不添加注释/描述
# - 作者详细信息应通过 entity 页面维护
```

### Author Entity Pages

```yaml
---
type: entity
title: {Author Name}
definition: "{一句话定义作者身份}"
validated_source: "https://验证来源URL"  # 身份验证来源
validated_at: "2026-04-13"              # 验证日期
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
tags:
  - {领域}
related_entities:
  - "[[相关作者]]"
source_raw:
  - "[[文章名]]"  # ⚠️ 使用短链接格式（纯文件名）
---
```

**说明**：`validated_source` 和 `validated_at` 仅用于 Author Entity（描述人物的 entity），其他概念 entity 无需此字段。

**Author Entity 工作流**：
1. **联网验证作者身份**（强制步骤）
   ├─ 使用 BrowserOS 搜索 "{Author Name}" + 相关领域关键词
   ├─ 确认作者确实存在且有公开身份信息（官网、LinkedIn、博客等）
   ├─ 记录验证来源 URL 到 `validated_source` 字段
   ├─ 记录验证日期到 `validated_at` 字段
   └─ ⚠️ 若无法验证：停止创建，文章 author 字段使用纯文本

2. 创建 entity 页面（`wiki/entities/{Author-Name}.md`）
   └─ 必须包含 `validated_source` 和 `validated_at` 字段

3. 更新文章 author 字段为 `[[Author Name]]`

**阻断规则**：
- 无法验证作者身份 → 不创建 entity，文章 author 使用纯文本
- 验证来源不明确 → 使用纯文本，等待用户确认

**中文作者文件名**：特殊字符转义（如 `盛兰雅(岚遥)` → `盛兰雅-岚遥`）

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
  - "[[相关概念A]]"  # 必须使用文件名格式（kebab-case）
  - "[[相关概念B]]"  # 禁止使用空格格式如 [[Dan Shipper]]
source_raw:
  - "[[文章名]]"  # ⚠️ 使用短链接格式（纯文件名）
---
```

**链接格式规则**：
- `source_raw` 使用**短链接格式**（纯文件名），如 `[[文章名]]`
- Quartz 配置 `markdownLinkResolution: "shortest"` 支持短链接跨目录解析
- 文件名在知识库中唯一时，短链接可正确解析

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
  - "[[文章1]]"
  - "[[文章2]]"
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
compile                    # 编译 raw 中所有文件
compile <文件名>           # 编译指定文件
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
| `wiki/lint-report.md` | 最新 lint 报告 |

---

## Quartz 网站部署

Clips 通过 Quartz 自动部署为数字花园 Wiki 网站（GitHub Pages）。

### 关键配置

- **ignorePatterns**: 使用 `**/pattern` 匹配子目录文件（如 `**/log.md`）
- **链接解析**: `markdownLinkResolution: "shortest"` 支持短链接跨目录
- **Explorer 过滤**: 过滤 `displayName === "wiki"` 避免导航栏嵌套
- **Graph 配置**: `depth` 参数含义：`N>0` = N层邻居（BFS），`-1` = 全站图谱

### index.md 维护

- **统计验证**: 定期检查 Entity/Topic 数量与实际文件数量是否一致
- **链接完整性**: 使用脚本验证所有 Wikilinks 指向存在的文件

### Git 提交规范

- **Wiki 文件必须提交**: 新建 Entity/Topic 后立即 commit，否则网站链接失效
- **检查 git status**: 推送前确认无未提交的 Wiki 文件（`??` 状态）

### Mermaid 图表规范

Wiki 文档中的 Mermaid 图表必须使用有效语法：

| 规范项 | 说明 |
|-------|------|
| **图表类型** | `flowchart TD/LR/BT/RL` 或 `graph TD`（流程图） |
| **节点语法** | 必须包含 ID，如 `NodeID[显示文本]`，不能只写 `[文本]` |
| **无效关键字** | `querydown` 等非标准关键字会导致解析失败 |

---

## 实践技巧

### 批量编译效率

- 读取多篇文章时**并行调用 Read 工具**（一次调用多个）
- 创建 entity/topic 时批量写入（一次 Write 多个文件）
- 识别文章间的**共同主题**，创建连接它们的 entity/topic

### Quartz 调试

- **本地无 node_modules 是正常现象**：构建在 GitHub Actions 中进行，本地 TypeScript 类型警告可忽略

### Entity 设计模式

- **一句话定义**：frontmatter 的 `definition` 字段应简洁，正文展开细节
- **概念网络**：通过 `related_entities` 建立关联，而非在 entity 内重复定义
- **溯源链**：`source_raw` 使用 wikilink 指向原始文章，支持反向追溯

### Index 更新清单

编译完成后更新 index.md：
1. 修改概览统计数字
2. 添加新 entity 到 entity 表格
3. 添加新 topic 到 topic 表格

---

*本文件由 Claude Code 维护，用于指导 AI Agent 在 Clips LLM Wiki 中的工作。*