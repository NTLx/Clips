---
name: smart-web-clipper
description: |
  将网页智能剪藏到 Obsidian 知识库，自动提取标题、作者、日期、正文，生成 AI 分析摘要和知识图谱链接。
  
  Use this skill when:
  - 用户说 "clip", "save", "capture", "剪藏", "抓取", "保存" 网页/文章/链接
  - 用户提供了 URL 并希望保存到知识库
  - 用户想要批量采集多个网页
  - 用户想要提取文章内容并生成元数据
  - 用户说 "帮我看看这篇文章并保存" 等隐含剪藏意图
  
  Automatically triggered by: "clip this", "save article", "剪藏这篇", "帮我抓取", "保存这个链接", "网页剪藏", "收藏文章"
  
  Features: Full Obsidian Web Clipper parity (18 preset variables, meta/schema extraction, 13 filters, AI analysis, auto wikilinks)
---

# Smart Web Clipper

将网页智能剪藏到 Obsidian 知识库，支持 AI 分析、知识图谱链接、批量采集。

## Dependencies

### Required
- **Chrome DevTools MCP** (`mcp__plugin_chrome-devtools-mcp_chrome-devtools__*`)

### Optional (auto-detected)
- **Obsidian CLI** (`obsidian` command) - 首选写入方式
- **obsidian-markdown Skill** - 无 CLI 时的备选

---

## Workflow

### Step 1: Navigate and Capture

```
1. Navigate to URL: mcp__plugin_chrome-devtools-mcp_chrome-devtools__navigate_page type="url" url="<URL>"
2. Take snapshot: mcp__plugin_chrome-devtools-mcp_chrome-devtools__take_snapshot
3. If dynamic content, wait and re-snapshot
```

### Step 2: Variables Extraction

提取 5 类变量（详见 `references/variables.md`）：

| 类型 | 示例 | 说明 |
|------|------|------|
| **Preset** | `{{title}}`, `{{author}}`, `{{content}}` | 18 个内置变量 |
| **Meta** | `{{meta:property:og:title}}` | Open Graph 等 |
| **Selector** | `{{selector:.author}}` | CSS 选择器提取 |
| **Schema** | `{{schema:@Article:author}}` | JSON-LD 结构化数据 |
| **Prompt** | AI 分析内置 | 摘要、标签、实体、立场 |

**关键：Author Wikilink 检测**
```
1. 提取作者名
2. 检查 10-wiki/entities/{Author-Name}.md 是否存在
3. 存在 → author: ["[[Author Name]]"]
4. 不存在 → author: ["Author Name"]（纯文本，无注释）
```

### Step 3: Filters Processing

使用过滤器链处理提取值（详见 `references/filters.md`）：

```yaml
# 多作者转 wikilink
author: "{{author|split:', '|wikilink}}"
# "John, Jane" → ["[[John]]", "[[Jane]]"]

# 日期标准化
published: "{{published|date:'YYYY-MM-DD'}}"

# 安全文件名
filename: "{{title|lower|replace:' ':'-'|safe_name}}"
```

### Step 4: Link Discovery

扫描页面链接，AI 评估是否值得剪藏：

| 链接类型 | 处理 |
|---------|------|
| 同站相关文章 | 评估相关性 |
| 外部引用 | 跳过 |
| PDF/文档 | 标记用户处理 |

**爬取深度决策**：
- 单篇文章 → 0
- 博客/教程 → 1-2
- 列表/汇总 → 2

### Step 5: Category Classification

映射到知识库分类：

```
AI-Agent/        - AI、LLM、Agent
Codex/     - Codex 相关
Career-Skills/   - 职业技能、生产力
Knowledge-Work/  - 知识管理、PKM
General/         - 通用文章
OpenClaw/        - OpenClaw 产品
```

### Step 6: Generate Output

生成 Markdown 文件：

```markdown
---
type: raw
source: "https://example.com/article"
author:
  - "[[Author Name]]"
published: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
created: "YYYY-MM-DD"
tags: [clippings, category, ai-tags]
description: "AI 生成摘要"
reading_time: "N min"
stance: "objective|opinion|promotional"
credibility: "high|medium|low"
language: "zh|en"
changes_url: "https://..."  # 可选
---

# {Title}

> [!info] 文章来源
> - 作者: [[Author Name]]
> - 发布: {published}
> - 原文: [{title}]({source})

{Content}

---

## AI Metadata

- Domain: example.com
- Category: {category}
- Relevance: {1-10}

## Entities Found

| Entity | Type | Exists |
|--------|------|--------|
| {concept} | concept | Yes → [[Entity]] / No → Candidate |

## Related Links

| URL | Worth Clipping | Reason |
|-----|---------------|--------|
| ... | Yes/No | {AI assessment} |
```

### Step 7: Environment Detection & Write

```
1. Check: obsidian --version
2. Available → obsidian create
3. Not available → Write tool with Obsidian Markdown compliance
```

**文件命名**：`{YYYYMMDD}-{sanitized-title}.md`

---

## Content Modes

| Mode | 适用场景 |
|------|---------|
| **preserve** | 技术文档、教程、参考资料 |
| **synthesize** | 观点文章、新闻分析、快速阅读 |

---

## Team Mode (Batch Clipping)

```
1. TeamCreate team_name="clip-batch"
2. Spawn agents (max 3-5 concurrent)
3. Each agent: navigate → snapshot → extract → write
4. Aggregate results
5. Shutdown team
```

---

## Edge Cases Quick Reference

详细处理见 `references/edge-cases.md`

| 情况 | 处理 |
|------|------|
| 付费墙/登录 | 通知用户，跳过 |
| 404 | 尝试 archive.org |
| 无 Obsidian CLI | 直接文件写入 |
| 重复检测 | 提示用户，显示已有 |
| 低可信度 | 标记 `credibility: flagged` |
| 作者实体存在 | 使用 `[[Author]]` wikilink |
| 页面有更新日期 | 提取到 `updated:` 字段 |
| 页面有变更链接 | 存储到 `changes_url:` |

---

## Output Format

```
✅ Clipped: {title}
📁 Location: {path}/{filename}.md
🏷️ Category: {category}
📊 Relevance: {score}/10
🔗 Links: {n} found ({m} worth clipping)
```

---

## Feature Summary

| Feature | Status |
|---------|--------|
| Preset Variables (18) | ✅ Full parity |
| Meta/Schema Variables | ✅ Full extraction |
| Filters System (13 core) | ✅ wikilink, split, join, date, etc. |
| AI Analysis | ✅ Built-in (summary, tags, entities, stance) |
| Knowledge Linking | ✅ Auto wikilinks to wiki |
| Batch Processing | ✅ Team mode |
| Dynamic Content | ✅ Full JS rendering |
| Credibility Check | ✅ Auto assessment |

完整对比见 `references/comparison.md`