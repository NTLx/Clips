# Clips LLM Wiki Schema

本文档定义 Clips 知识库的架构、工作流和规范，指导 AI Agent 运营和维护这个 LLM Wiki。

---

## 知识库定位

Clips 是一个**大杂烩文章剪藏 Wiki**，收集各类有价值的网络文章，通过 LLM Wiki 模式实现：

- **知识编译**：将原始文章提炼为结构化知识
- **概念提取**：从文章中提取核心概念，建立 entity 页面
- **持续累积**：每次编译都沉淀到 wiki 层，避免重复处理

---

## ljg 集成层（知识编译引擎）

Clips 集成 ljg 系列技能作为知识编译引擎。**前提：已安装 `md` branch 的 ljg 技能**（输出 Markdown 格式，非 Org-mode）。

---

## Obsidian 渲染规范（Obsidian Flavored Markdown）

Clips 的所有 `.md` 文件最终在 Obsidian 中渲染。编写文档时必须遵循 Obsidian Flavored Markdown 规范，避免渲染崩溃。

### MathJax 冲突 — `$` 符号必须转义或包裹

Obsidian 使用 `$` 作为行内 LaTeX 公式分隔符。**任何 `$` 出现在正文中都会触发 MathJax 解析**，如果没有配对闭合的 `$`，会导致段落乃至整个文件渲染崩溃。

| 写法 | 效果 | 示例 |
|------|------|------|
| `$200` | ❌ 渲染崩溃（MathJax 当作公式起始符） | `Even if people paid $200/month...` |
| `$$value$$` | ❌ 渲染为数学公式 | `$$E=mc^2$$` |
| `` `$200` `` | ✅ 内联代码，正确显示美元符 | 价格、金额用反引号包裹 |
| `\$200` | ✅ 转义，渲染为文本 | `Even if people paid \$200...` |

**规则**: 编写包含 `$`、`$xx`、`$$$` 等美元符号的文本时，必须用**反引号包裹**或用**反斜杠转义**。

### 常见渲染问题对照表

| 问题 | 原因 | 修复 |
|------|------|------|
| 整段文字消失或变成公式 | `$` 触发 MathJax | 反引号包裹 `` `$200` `` 或转义 `\$200` |
| 粗体/斜体不生效 | `*` 数量不匹配 | 检查配对 `*text*` / `**text**` |
| 引用块断裂 | 空行未加 `>` 或加了多余 `>` | 多段引用用 `>` 开头 + 空行分隔 |
| 表格列不对齐 | 每行 `|` 数量不一致 | 确保表头、分隔线、数据行列数一致 |
| 链接变文本 | wikilink 含空格 | 使用 kebab-case：`[[AI-Psychosis]]` |
| YAML 解析失败 | frontmatter 中出现特殊字符未引号包裹 | 值用双引号包裹 `"value"` |

### 编写前检查清单

在写入任何 `.md` 文件前，Agent 必须调用 **obsidian-markdown** 技能进行格式校验。

1. **调用 obsidian-markdown 技能**：确保 Obsidian Flavored Markdown 合规（wikilink、callout、properties 语法，避免 MathJax 冲突、emphasis 错位、frontmatter 错误）
2. **aliases 字段**：Entity 必须包含 `aliases` 字段，值为自然语言名称（供 Obsidian "未链接提及" 识别）
3. **$ 符号扫描**：全文无裸露的 `$`（在 frontmatter 和正文中）
4. **emphasis 配对**：`*` / `_` / `~` 成对出现
5. **YAML 有效性**：frontmatter 中 special chars（`#`, `:`, `{}`, `[]`, `&`, `*`）必须用引号包裹
6. **wikilink 格式**：双括号内使用 kebab-case，无空格；正文引用优先使用管道语法 `[[Kebab-Case|Natural Name]]`
7. **无隐藏字符**：无 BOM、零宽字符（U+200B 等）

### 快速诊断命令

对可疑文件运行 Python 检查：

```bash
python3 << 'PYEOF'
import re
path = "/path/to/file.md"
with open(path, 'r') as f:
    content = f.read()
for i, line in enumerate(content.split('\n'), 1):
    clean = re.sub(r'`[^`]+`', '', line)
    for m in re.finditer(r'(?<!\\)\$', clean):
        print(f"Line {i}: Unwrapped $ at: ...{line[max(0,m.start()-15):m.start()+15]}...")
PYEOF
```

---

### 技能与 Wiki 工作流映射

| 技能 | 定位 | Wiki 输出目录 | 编译产出 |
|------|------|-------------|---------|
| **ljg-read** (伴读) | Ingest 预处理 | 不直接输出，注入编译摘要 | 骨/肌/筋膜结构标注 + 碰撞提问 → 编译摘要的浓缩/质疑 |
| **ljg-learn** (概念解剖) | Entity 生成器 | `wiki/entities/` | 八维拆解决定 entity 定义、关键数据点、前提与局限性、关联概念 |
| **ljg-paper** (读论文) | 论文类文章编译器 | `wiki/entities/` | 8 段式结构 → 浓缩+质疑+对标 + 核心概念提取 |
| **ljg-paper-river** (倒读法) | 关系构建器 | `wiki/comparisons/` | 5 层倒读+正向追踪 → 概念演化脉络 + 对比分析维度 |
| **ljg-think** (追本之箭) | Topic 深度分析 | `wiki/topics/` | 4 层降深（表象→机理→原理→公理）→ 主题深度分析 |
| **ljg-rank** (降秩) | 领域级分析 | `wiki/topics/` | 找 2-3 个不可约生成器 → Topic 核心结构 |
| **ljg-plain** (白话) | 质量控制 | N/A | Entity definition 可读性校验（12 岁可读测试） |
| **ljg-writes** (写作引擎) | 输出放大器 | `wiki/outputs/` | 观点驱动写作 → 博客/笔记作品 |
| **ljg-card** (铸) | 视觉化 | `~/Downloads/` → 手动引用 | Entity/Topic/Output 转为 PNG 传播卡片 |
| **obsidian-markdown** (Obsidian 规范) | 写入守卫 | N/A（质量门） | **所有 `.md` 文件写入前必调用** — 确保 Obsidian Flavored Markdown 合规（wikilink、callout、properties 语法，避免 MathJax 冲突、emphasis 错位、frontmatter 错误） |

### 适配脚本: `.sisyphus/ljg-wiki-wrapper.py`

ljg 技能输出到 `~/Documents/notes/`，需通过 wrapper 脚本适配到 Wiki：

**功能**:
1. 读取 ljg 输出文件（`/Documents/notes/*__{skill_type}.md`）
2. 注入 Wiki 标准 YAML frontmatter（type/title/definition/tags/source_raw/created/updated）
3. 搬运到 `wiki/{entities|topics|comparisons|outputs}/`
4. 对 learn 类型自动追加 Entity 标准三章节（关键数据点、前提与局限性、关联概念）占位

**用法**:
```bash
# 处理单一技能最新输出
python3 .sisyphus/ljg-wiki-wrapper.py --skill learn --source-raw "20260408-knowledge-work.md"

# 扫描待处理文件
python3 .sisyphus/ljg-wiki-wrapper.py --scan

# 处理所有待处理文件
python3 .sisyphus/ljg-wiki-wrapper.py --all
```

---

## 两层架构

```
┌─────────────────────────────────────────────────────────────────┐
│                    Clips LLM Wiki 架构                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Layer 0: Raw Sources (raw/)                                   │
│  └── 所有剪藏文章直接存放于此（扁平结构）                       │
│                                                                 │
│  Layer 1: Wiki (wiki/) ← LLM 维护层                            │
│  ├── entities/       概念页面（从文章提取的核心概念）           │
│  ├── topics/         主题页面（整合多篇文章的主题）             │
│  ├── comparisons/    对比分析页面                              │
│  ├── outputs/        输出作品（博客、笔记等）                   │
│  └─ lint-report.md   Lint 报告                                 │
│                                                                 │
│  Git History ← 操作历史记录（替代 log.md）                     │
│  通过结构化 commit message 记录所有编译/修复/lint 操作          │
│                                                                 │
│  Schema (README.md) ← 当前文件                                 │
│  定义工作流、规范、约定                                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 各层职责

| 层级              | 职责       | 维护者           |
| --------------- | -------- | ------------- |
| **Raw Sources** | 存储原始文章   | 用户            |
| **Wiki**        | 结构化知识    | **AI Agent**  |
| **Schema**      | 工作流定义、规范 | 用户 + AI Agent |

---

## Ingest 工作流（知识编译）

将原始文章编译为结构化知识。提供两条路径：

- **标准路径**：三步编译法（浓缩 → 质疑 → 对标），适合普通文章
- **ljg 增强路径**：调用相关 ljg 技能进行深度编译，输出结构化知识 + Entity 页面

### ljg 增强路径

```
1. 读取 raw source 内容
   └─ 检查 frontmatter 是否完整
   └─ 验证 wikilink 使用 kebab-case 格式

2. 选择 ljg 技能（根据文章类型）
   ├─ ljg-read（伴读） → 所有文章通用预处理
   │  └─ 骨/肌/筋膜标注 → 直接输出编译摘要 + 碰撞提问
   ├─ ljg-learn（概念解剖） → 含核心概念的文章
   │  └─ 八维拆解 → 输出 entity 内容（定义、关键数据、局限、关联）
   ├─ ljg-paper（读论文） → 论文类文章
   │  └─ 8 段式结构 → 浓缩+质疑+对标 + 核心概念
   └─ ljg-paper-river（倒读法） → 研究型论文
      └─ 5 层倒读链路 → 概念演化脉络 → wiki/comparisons/

3. 执行 ljg 技能 → 输出到 ~/Documents/notes/*.md

4. 运行适配脚本
   └─ python3 .sisyphus/ljg-wiki-wrapper.py --skill {type} --source-raw "{源文件}"
   └─ 自动注入 frontmatter + 搬运到 wiki/{entities|topics|comparisons}/
   └─ learn 类型自动追加 Entity 标准三章节占位

5. 多主题文章 → 按需追加 ljg 深度编译
   ├─ ljg-think（追本之箭） → wiki/topics/ （4 层降深）
   └─ ljg-rank（降秩） → wiki/topics/ （不可约生成器）

6. 追加编译摘要到 raw 源（引用 ljg 输出）

7. 更新 index.md + comparisons（如有对比概念）

8. 提交 git commit（按 Commit 规范撰写）
```

### 标准路径（三步编译法）

```
1. 读取 raw source 内容
   └─ 检查 frontmatter 是否完整（author 字段必须存在且格式正确）
   └─ 验证 wikilink 使用 kebab-case 格式
   └─ 扫描 $ 符号（确保 MathJax 冲突已处理）

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

5. ⚠️ 写入校验：调用 obsidian-markdown 技能检查文件格式合规
   └─ 确保 frontmatter 有效（YAML 特殊字符引号包裹）
   └─ 确保 wikilink kebab-case 规范
   └─ 确保 MathJax 冲突已处理（$ 被包裹或转义）
   └─ 确保 callout/properties/emphasis 语法正确

6. 创建/更新 topic 页面
   └─ 写入 wiki/topics/

7. 更新 comparisons（如有对比概念）
   └─ 添加新论述、关联已有 entity

8. 更新 index.md
   └─ 添加新的 entity 和 topic 条目

9. 提交 git commit（按 Commit 规范撰写）
```

**触及范围**：单篇 source 编译可能影响 10-15 个 wiki 页面
- 新建 entities（3-5 个）
- 更新相关 entities（添加关联）
- 创建/更新 topic（整合主题）
- 更新 comparisons（如有对比）
- 更新 index.md
- 提交 git commit

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

### Query 增强（ljg 驱动）

| 增强 | 方式 | 效果 |
|------|------|------|
| **ljg-learn 概念解剖** | 对查询中的概念调用 ljg-learn | 输出八维拆解 + 一句话压缩，直接回答"什么是 X" |
| **ljg-think 追本之箭** | 对复杂观点/现象调用 ljg-think | 四

---

## Outputs 工作流

| 增强 | 方式 | 效果 |
|------|------|------|
| **ljg-writes 写作引擎** | 对 Topic/Entity 观点调用 ljg-writes | 输出 wiki/outputs/ 博客/笔记 |
| **ljg-plain 白话重写** | 对 Entity definition 调用 ljg-plain | 校验"12 岁可读"质量标准 |
| **ljg-card 铸** | 对 Entity/Topic/Comparison 调用 ljg-card | 输出 PNG 传播卡片到 ~/Downloads/ |

---
## Lint 工作流（知识审计）

| 检查项 | 条件 | 处理方式 |
|-------|------|---------|
| Raw backlog | raw/ 中超过 7 天的文件 | 提醒 compile |
| 孤儿 entity | 无 topic 页面引用的 entity | 关联到相关 topic |
| 失效链接 | wikilinks 指向不存在的页面 | 修复或删除链接 |
| **一致性检查** | 同一概念在不同 Entity 中的定义是否冲突 | 列出冲突位置和建议统一方向 |
| **完整性检查** | Entity 是否包含必填字段（定义、关键数据点、前提与局限性、关联概念） | 标记缺失字段 |
| **孤岛检测** | 入链和出链都少于 2 的页面（仅实体 entities 和对比 comparisons，排除 outputs 和 topics） | 建议建立关联或合并 |
| **摘要覆盖检查** | raw/ 中哪些文件尚未包含编译摘要 | 列出待处理文件 |
| **Comparison 元数据** | 所有 comparison 必须有 `updated` 字段 | 补全缺失 |

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
aliases:
  - {概念名自然写法}  # 自然语言名称，供 Obsidian "未链接提及" 识别
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

**引用显示规范**：
- 正文引用 Entity 时优先使用管道语法：`[[Kebab-Case|Natural Name]]`
- 示例：`[[Vibe-Coding|Vibe Coding]]`、`[[Knowledge-Work|Knowledge Work]]`
- 好处：渲染时显示自然名称，同时保持 kebab-case 文件名兼容性

### Author Entity Pages

```yaml
---
type: entity
title: {Author Name}
aliases:
  - {Author Name}  # 自然语言名称，供 Obsidian "未链接提及" 识别
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
- Schema 文件：`README.md`, `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`（兼容其他 AI 工具）
- 日志文档：`lint-report.md`
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

## Git Commit 规范（操作历史记录）

Clips 使用结构化 git commit 替代 log.md 记录所有操作历史。每次编译、修复、lint 等操作完成后，必须提交 git commit，commit message 即为操作日志。

### Commit Message 格式

```
<type>(<scope>): <subject>

<body>
```

**各段说明：**

| 段落 | 必填 | 说明 |
|------|------|------|
| `<type>(<scope>): <subject>` | ✅ | 标题行，不超过 72 字符 |
| `<body>` | ✅ | 详细描述变更内容 |

### Type 枚举

| Type | 含义 | 示例 |
|------|------|------|
| `compile` | 知识编译（Ingest） | `compile(Karpathy-AI-Capability-Gap): 编译 Karpathy AI 能力鸿沟帖` |
| `fix` | 修复问题（lint 修复、链接修复等） | `fix(wikilinks): 修复 18 处 ASCII/Unicode 撇号不匹配` |
| `refactor` | 重构（格式转换、架构调整） | `refactor(entities): 转换 4 个 ljg-learn 输出为标准格式` |
| `lint` | Lint 审计 | `lint: 执行完整 lint 检查，健康度 72→96` |
| `docs` | 文档/Schema 更新 | `docs(schema): 新增时间与事实规范章节` |
| `clip` | 剪藏新文章到 raw/ | `clip(steve-hanov): 剪藏 Steve Hanov 精益技术栈文章` |
| `output` | 创建 Output 作品 | `output(quartz-tutorial): 创建 Quartz 部署教程` |

### Scope 规范

Scope 标识操作的聚焦对象，使用 kebab-case：

| 场景 | Scope 示例 |
|------|-----------|
| 编译单篇文章 | 文章主题关键词：`Karpathy-AI-Capability-Gap`、`Lean-Stack` |
| 批量操作 | 操作范围：`entities`、`topics`、`all-raw` |
| 修复特定问题 | 问题对象：`wikilinks`、`frontmatter`、`source-raw` |
| Schema 更新 | `schema` |

### Body 模板（按 Type 分）

#### compile 类型

```
- 来源: {URL} ({平台}, {作者})
- 编译方式: {标准路径/ljg 增强路径}
- 新增 Entity: {Entity-A}, {Entity-B}
- 更新 Entity: {Entity-C}, {Entity-D}
- 新增 Topic: {Topic-A}
- 更新 Topic: {Topic-B}
- 索引: {N}→{M} entities, {X}→{Y} raw articles
```

#### fix 类型

```
- 修复内容: {具体问题描述}
- 影响文件: {文件列表}
- 修复方式: {如何修复}
```

#### lint 类型

```
- 检查项: {列出检查的 8 项}
- 发现问题: {具体问题}
- 修复情况: {修复了什么}
- 健康度: {旧分}→{新分}
```

#### refactor 类型

```
- 重构内容: {什么从什么变为什么}
- 影响文件: {文件列表}
```

#### clip 类型

```
- 来源: {URL}
- 作者: {作者名}
- 主题: {关键词}
```

### Commit 示例

**编译操作：**
```
compile(Karpathy-AI-Capability-Gap): 编译 Karpathy AI 能力鸿沟帖

- 来源: https://x.com/karpathy/status/... (X/Twitter, Andrej Karpathy)
- 编译方式: 标准路径（三步编译法）+ 附加思考整合
- 附加资料: 池建强微信公众号 + 墨问笔记
- 新增 Entity: AI-Psychosis, AI-Capability-Gap
- 更新 Entity: Andrej-Karpathy, Vibe-Coding, Software-2.0, Claude-Code-CLI
- 更新 Topic: Karpathy-AI-Thought (新增概念矩阵)
- 索引: 67→69 entities, 25→26 raw articles
```

**Lint 修复：**
```
fix(entity-completeness): 全面修复 Entity 完整性 (42/42) 并优化 lint 工作流

- 修复内容: 补全 42 个概念 Entity 的标准三章节（关键数据点、前提与局限性、关联概念）
- 影响文件: 42 个 entity 文件
- 修复方式: 为缺失章节添加占位内容，统一标题命名
```

**Schema 更新：**
```
docs(schema): 用 Git Commit 规范替代 log.md 记录操作历史

- 删除 3 个 log.md 文件（根目录、raw/、wiki/）
- 新增 Git Commit 规范章节（type/scope/body 模板）
- 更新所有 log.md 引用（架构图、工作流步骤、关键文件表、Quartz 配置）
```

### 操作历史查询命令

| 查询需求 | Git 命令 |
|---------|---------|
| 最近 10 次操作 | `git log --oneline -10` |
| 某篇文章的编译历史 | `git log --grep "文章关键词"` |
| 某个 Entity 的变更历史 | `git log -- wiki/entities/Entity-Name.md` |
| 所有编译操作 | `git log --grep "^compile"` |
| 所有修复操作 | `git log --grep "^fix"` |
| 某次操作的详细变更 | `git show <commit-hash>` |
| 某次操作的文件列表 | `git show --stat <commit-hash>` |
| 某段时间内的操作 | `git log --since="2026-04-01" --until="2026-04-15"` |
| 某个目录的所有变更 | `git log -- wiki/entities/` |
| 搜索 body 中的关键词 | `git log --grep="AI-Psychosis"` |

### Commit 规范强制检查

- **标题行不超过 72 字符**：超出时缩写 scope 或 subject
- **Body 必须填写**：至少包含「做了什么」和「影响了什么」
- **compile 类型必须列出 Entity 变更**：新增/更新的 Entity 必须在 body 中列出
- **fix 类型必须说明修复方式**：不能只写"修复了 bug"
- **每次操作一个 commit**：编译一个 raw source = 一个 commit，不要批量合并多个编译

---

## 操作命令

| 命令 | 说明 |
|-----|------|
| `compile` | 编译 raw 中所有未处理的文件 |
| `compile <文件名>` | 编译指定文件（优先使用 ljg 增强路径） |
| `rebuild` | 重新编译全部 Raw 文件（批量回溯） |
| `compile-ljg <文件名>` | 使用 ljg 增强路径深度编译 |
| `lint` | 执行完整 lint 检查（8 项检查，输出具体扣分和缺失文件清单） |
| `fix-lint` | 按 lint 报告逐项修复，输出修复前后对比 |
| `lint-plain <entity>` | 用 ljg-plain 校验 Entity definition 可读性 |
| `cast <页面>` | 用 ljg-card 将 Entity/Topic 转为 PNG 传播卡片 |
| `scan-entity-quality` | 扫描 entity ljg-learn 残留格式/缺失章节/末尾导航链接 |
| `什么是 <概念>?` | 概念查询（优先调用 ljg-learn） |
| `关于 <主题> 有什么讨论?` | 主题查询（优先调用 ljg-rank / ljg-think） |

---

## 调试技巧

### 读取 git 状态中的 Unicode 文件名

```bash
# git status 显示的中文字符是编码格式，需要解码
python3 -c "import sys; print(sys.argv[1].encode().decode('unicode_escape').encode('latin1').decode('utf8'))" 'raw/文件名'
```

## 联网工具偏好（事实核查/时间验证/溯源）

在需要联网查询内容时，Agent 必须遵循以下工具偏好：

| 需求 | 工具偏好 | 说明 |
|------|---------|------|
| **信息搜索** | `bailian_WebSearch` MCP 工具 | 总是优先使用此工具进行联网搜索查询 |
| **网页解析** | `bailian_WebParser` MCP 工具 | 总是优先使用此工具提取网页内容 |
| **浏览器操作** | `web-access` Skill | 需要登录态、交互操作、非公开内容时通过 CDP 操作 Chrome |
| **搜索引擎** | `google.com/ncr` | 通过 `web-access` 操作浏览器时，始终使用 Google 无重定向版作为搜索引擎 |

**执行顺序**:
1. 简单事实核查 → `bailian_WebSearch`
2. 验证具体网页内容 → `bailian_WebParser`
3. 复杂场景（登录/动态渲染/交互） → `web-access` Skill → `google.com/ncr`

### Edit 工具常见问题

- 字符串匹配失败时，尝试读取精确行内容查看实际字符
- 可先更新其他字段（如 updated 日期）作为突破口
- index.md 编辑时注意统计数字和 footer 分开更新

---

## Gotchas

### ljg-wrapper 残留 frontmatter

`.sisyphus/ljg-wiki-wrapper.py` 处理 ljg-learn 输出时，不会剥离 ljg 自带的 meta frontmatter
（`title: 概念解剖：X / tags: [concept] / date: YYYY-MM-DD`），导致 entity 正文中出现多余的 `---` 块。
**修复**: 创建 entity 后检查第 2 个 `---` 块并删除。

### Unicode 文件名与 Read 工具

`Read` 工具无法直接读取含中文的文件名。改用 Python：
```python
python3 << 'PYEOF'
import os
d = "/Users/lx/Obsidian/Clips/raw/"
files = [f for f in os.listdir(d) if "关键词" in f]
path = os.path.join(d, files[0])
with open(path, 'r') as f: content = f.read()
PYEOF
```

### 微信公众号文章剪藏不完整

Obsidian 浏览器插件剪藏 WeChat 文章会丢失正文段落。补全步骤：
1. 使用 `web-access` Skill → CDP 模式打开文章 URL
2. `/eval` 提取 `#js_content` 的完整 `innerText` 和元数据
3. 对比已有内容，补充缺失段落
4. 清理 WeChat 注入的 `<!--rehype:style=...-->` HTML 注释标记

### source_raw Wikilink 引号编码一致性

Raw 文件名若含弯引号 `" "`（U+201C/201D），entity 的 `source_raw` wikilink 必须使用相同的弯引号，不能用 ASCII 直引号 `"`（U+0022）。验证时通过 Python `repr()` 逐字符检查 `ord(ch)`。
⚠️ 来源区块（## 来源）中的 wikilink 同样适用此规则。

### 编辑含中文文件名的文件

`edit` 工具同样受 Unicode 文件名限制。使用 Python `open(path, 'w')` 直接写入是可靠方案。

### ljg-learn 原始输出格式转换

部分 entity 文件仍保留 ljg-learn 八维拆解原始输出（`# 定锚 / # 八刀 / # 内观 / # 压缩`），
缺少标准 entity 格式。需转换为：`> [!definition] 定义` + `## 关键数据点` + `## 前提与局限性` + `## 关联概念`。
已修复 Taste/Judgment/Coding-Agents/Dan-Shipper，但仍需批量扫描确认。

### 文件末尾导航链接

部分 wiki 文件末尾有 `**返回**: [知识库索引](index.md)` 无意义链接。
Obsidian 不需要手动导航链接，应删除。扫描命令: `grep -r '\*\*返回\*\*' wiki/`

### X/Twitter Obsidian 剪藏 Author 格式

Obsidian Web Clipper 自动生成的 author wikilink 带 `@` 前缀（如 `[[@intuitiveml]]`），
不符合 kebab-case 规范。必须替换为纯文本作者名（如 `"Peter Pang"`），
待创建 Author Entity 后再改为 `[[Peter-Pang]]`。

### Obsidian 数学公式冲突（MathJax）

**Clips 知识库中最高频的渲染崩溃原因**。任何包含 `$` 符号的文本（金额如 `$200`、缩写如 `$$$` 等），
都会被 Obsidian 的 MathJax 引擎当作行内公式处理，导致该段落及后续文本渲染崩溃。

**规则**：写入 `.md` 文件前，必须扫描全文中的 `$` 符号：
- **反引号包裹**：`` `$200` `` — 推荐，显示为内联代码
- **反斜杠转义**：`\$200` — 渲染为纯文本

**Python 扫描命令**：
```bash
python3 << 'PYEOF'
import re, sys
path = sys.argv[1]
with open(path) as f:
    content = f.read()
for i, line in enumerate(content.split('\n'), 1):
    clean = re.sub(r'`[^`]+`', '', line)
    for m in re.finditer(r'(?<!\\)\$', clean):
        print(f"Line {i}: {line[m.start()-10:m.end()+10]}")
PYEOF
```

---

## 概念筛选标准（决定是否建立 Entity）

| 类型 | 处理方式 | 示例 |
|------|---------|------|
| 工具/产品名 | 不建 Entity | OpenClaw, Obsidian, RAG |
| 框架/方法论（单篇出现） | 不建 Entity | HUMAN-3.0, Runtime-RAG |
| 人名（仅提及） | 不建 Entity | Dan-Koe |
| 通用泛概念（单篇出现） | 不建 Entity | AI-Adoption, AI-Transformation |
| 多篇文章重复出现 | ✅ 评估后建 Entity | Taste, Agentic-Engineering |

### 重复来源：保留一手来源

同一文章的多语言版本/翻译版本共存时，**只保留一手来源**（原文），删除翻译副本。
- 判断标准：语言（原文优先）、来源层级（X/博客 > 微信转载）、完整性

### Raw 关联概念规范

- 必须使用 `[[wikilink]]` 格式，禁止纯文本（如 `- ConceptName` 无效）
- 所有链接必须指向已存在的 Entity/Topic 页面
- 编译时在 Raw 末尾追加，确保每条引用都有对应 Wiki 页面

---

## 关键文件

| 文件 | 用途 |
|-----|------|
| `README.md` | Schema 主文件，定义工作流和规范（唯一真实文件） |
| `CLAUDE.md` | → README.md 软链接，兼容 Claude Code |
| `AGENTS.md` | → README.md 软链接，兼容其他 AI Coding 工具 |
| `index.md` | 知识库索引 |
| `wiki/lint-report.md` | 最新 lint 报告 |

---

### Compile 操作注意事项

- **append 编译摘要只执行一次** — 使用 Python `open(path, 'a')` 追加前先用 `grep` 检查 `## 编译摘要` 是否已存在，避免重复追加
- **git add 必须从根目录执行** — 子目录执行 `git add -A` 会意外添加外部符号链接（.codebuddy/ 等），应 `cd /Users/lx/Obsidian/Clips && git add <target-dir>/`
- **X/Twitter 剪藏 author 格式**：若 Author Entity 已存在，用 `[[Author-Name]]` wikilink 格式；若不存在，先用纯文本
- **web-access CDP Proxy**：通过 `localhost:3456` 操作，使用前先运行 `node "/Users/lx/.agents/skills/web-access/scripts/check-deps.mjs"` 检查

---

*本文件由 AI Agent 维护，用于指导 AI Agent 在 Clips LLM Wiki 中的工作。*