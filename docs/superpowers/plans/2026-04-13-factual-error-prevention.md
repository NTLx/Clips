# Factual Error Prevention Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Modify README.md to add mandatory verification steps for Author Entity creation and Ingest workflow, preventing factual errors from entering the Wiki.

**Architecture:** Documentation-only changes. Two modification points: (1) Author Entity workflow section adds validation steps and new frontmatter fields, (2) Ingest workflow inserts article association validation between concept extraction and entity creation.

**Tech Stack:** Markdown documentation, YAML frontmatter

---

## File Structure

| File | Action | Purpose |
|------|--------|---------|
| `README.md` | Modify | Add validation workflow steps and frontmatter fields |

**Modification Locations:**
- Lines ~295-318: Author Entity Pages section
- Lines ~78-93: Ingest workflow execution flow section

---

## Task 1: Update Author Entity Frontmatter Fields

**Files:**
- Modify: `README.md:295-311` (Author Entity Pages YAML example)

- [ ] **Step 1: Add validated_source and validated_at fields to YAML example**

Replace the YAML block in Author Entity Pages section with:

```yaml
---
type: entity
title: {Author Name}
definition: "{一句话定义作者身份}"
validated_source: "https://验证来源URL"  # 🆕 新增：身份验证来源
validated_at: "2026-04-13"              # 🆕 新增：验证日期
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

- [ ] **Step 2: Verify YAML syntax is correct**

Run: Visual check that YAML indentation and field names are valid
Expected: All fields properly indented, no syntax errors

- [ ] **Step 3: Commit this change**

```bash
git add README.md
git commit -m "docs: 添加 Author Entity validated_source 和 validated_at 字段定义"
```

---

## Task 2: Update Author Entity Workflow Section

**Files:**
- Modify: `README.md:313-318` (Author Entity 工作流 section)

- [ ] **Step 1: Replace the Author Entity workflow description**

Replace lines 313-318 with:

```markdown
**Author Entity 工作流**：
1. **联网验证作者身份**（强制步骤）
   ├─ 使用 BrowserOS 搜索 "{Author Name}" + 相关领域关键词
   ├─ 确认作者确实存在且有公开身份信息（官网、LinkedIn、博客等）
   ├─ 记录验证来源 URL 到 `validated_source` 字段
   ├─ 记录验证日期到 `validated_at` 字段
   └─ ⚠️ 若无法验证：停止创建，文章 author 字段使用纯文本

2. 创建 entity 页面（`10-wiki/entities/{Author-Name}.md`）
   └─ 必须包含 `validated_source` 和 `validated_at` 字段

3. 更新文章 author 字段为 `[[Author Name]]`
```

- [ ] **Step 2: Verify workflow steps are clear and actionable**

Run: Visual check that each step has clear action and failure handling
Expected: Step 1 has blocking rule, Step 2 has field requirement

- [ ] **Step 3: Commit this change**

```bash
git add README.md
git commit -m "docs: 修改 Author Entity 工作流，添加强制验证步骤"
```

---

## Task 3: Insert Article Association Validation in Ingest Workflow

**Files:**
- Modify: `README.md:78-93` (Ingest 执行流程 section)

- [ ] **Step 1: Insert new step 4 between concept extraction and entity creation**

Modify the Ingest execution flow to insert new step 4. The current steps 3-4 become 3-5:

```markdown
### 执行流程

```
1. 读取 raw source 内容
   └─ 检查 frontmatter 是否完整

2. 分析主题，确定分类
   └─ AI-Agent / Claude-Code / Career-Skills / ...

3. 提取 3-5 个核心概念
   └─ 识别文章中的关键术语、方法论、技术概念

4. **文章关联验证**（新增步骤）
   ├─ 检查 raw source 的 author 字段格式
   ├─ 若 author 为 wikilink `[[Author Name]]`：
   │  ├─ 验证 `10-wiki/entities/{Author-Name}.md` 存在
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
   └─ 写入 10-wiki/entities/
   └─ ⚠️ source_raw 必须使用短链接格式，禁止使用相对路径

6. 创建/更新 topic 页面
   └─ 写入 10-wiki/topics/

7. 更新 index.md
   └─ 添加新的 entity 和 topic 条目

8. 记录到 log.md
   └─ 记录编译操作详情

9. ⚠️ 移动 raw source 并同步路径（关键步骤）
```
```

- [ ] **Step 2: Update subsequent step numbers**

Ensure steps 5-9 maintain correct numbering after inserting new step 4.

- [ ] **Step 3: Verify the error message format is usable**

Run: Visual check that error message has all necessary fields for user to debug
Expected: Message shows article name, entity name, current source_raw, expected value

- [ ] **Step 4: Commit this change**

```bash
git add README.md
git commit -m "docs: 在 Ingest 工作流插入文章关联验证步骤"
```

---

## Task 4: Final Review and Push

**Files:**
- Verify: `README.md`

- [ ] **Step 1: Verify all changes are consistent**

Run: `git diff README.md`
Expected: Three distinct changes visible:
- Author Entity frontmatter with new fields
- Author Entity workflow with validation steps
- Ingest workflow with step 4 inserted

- [ ] **Step 2: Check README.md readability**

Run: Visual check that the document flows logically
Expected: Validation steps clearly marked as mandatory, blocking rules visible

- [ ] **Step 3: Push to remote repository**

```bash
git push origin main
```

---

## Self-Review Checklist

**1. Spec coverage:**
- ✅ Task 1 covers: Entity Pages Frontmatter (validated_source, validated_at)
- ✅ Task 2 covers: Author Entity Workflow revision
- ✅ Task 3 covers: Ingest workflow step 4 insertion

**2. Placeholder scan:**
- ✅ No TBD/TODO found
- ✅ All steps have actual content (not just descriptions)
- ✅ Commit messages specified

**3. Type consistency:**
- ✅ `validated_source` and `validated_at` field names used consistently
- ✅ Step numbering (1-9) correct after insertion

---

*Plan created: 2026-04-13*