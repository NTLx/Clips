# Factual Error Prevention in LLM Wiki Workflow

> **For agentic workers:** This spec modifies `README.md` workflow definitions. Implementation involves updating documentation constraints, not code.

**Goal:** Prevent factual errors (like the Wes Botman incident) from entering the Wiki through validation at entity creation and article compilation stages.

**Approach:** Add mandatory verification steps to the Author Entity and Ingest workflows, with hard blocking on validation failure.

**Scope:** Documentation-only changes to README.md workflow sections.

---

## Problem Statement

### The Wes Botman Incident

An Author Entity was created with incorrect information:
- Entity claimed Wes Botman wrote "10 Must-Have Skills for Claude in 2026"
- This was never verified — no source article linked
- Error propagated to other entities via `related_entities`
- User discovered the error through external fact-checking

### Root Cause Analysis

| Weakness | Current Behavior | Consequence |
|---------|-----------------|------------|
| No author verification | LLM creates entity based on assumption | Incorrect definition, false associations |
| No association validation | `source_raw` filled without checking raw source | Entity links to articles it shouldn't |
| No blocking mechanism | Errors continue through workflow | Propagation to related entities |

---

## Solution Design

### Two-Gate Protection System

```
┌─────────────────────────────────────────────────────────────────┐
│                 Factual Error Prevention Gates                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Gate 1: Author Identity Verification                           │
│  Trigger: Creating Author Entity                                │
│  Action: BrowserOS search → confirm existence                   │
│  Failure: Block creation, use plain text author name            │
│                                                                 │
│  Gate 2: Article Association Validation                         │
│  Trigger: Ingest workflow (compile article)                     │
│  Action: Check entity.source_raw matches raw.author             │
│  Failure: Block compile, prompt user to fix association         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Gate 1: Author Identity Verification

**When:** Creating a new Author Entity (type=entity for a person)

**Process:**
```
1. BrowserOS search for author name
   ├─ Query: "{Author Name}" + context clues (blog, company, domain)
   ├─ Find: Official site, LinkedIn, Twitter, publications

2. Verify identity matches context
   ├─ Confirm: Author exists and has public profile
   ├─ Record: Validation source URL and date

3. Decision:
   ├─ Verified → Create entity with validated_source, validated_at
   └─ Not verified → Stop, use plain text author name (no wikilink)
```

**New Frontmatter Fields:**
```yaml
validated_source: "https://..."  # URL where identity was confirmed
validated_at: "2026-04-13"      # Date of verification
```

**Blocking Rule:**
- Cannot create Author Entity without `validated_source`
- If search fails, use plain text author name in raw source frontmatter

### Gate 2: Article Association Validation

**When:** Ingest workflow, step 4 (between concept extraction and entity creation)

**Process:**
```
1. Read raw source frontmatter
   └─ Check author field format

2. If author is wikilink [[Author Name]]:
   ├─ Verify: Author entity file exists in 10-wiki/entities/
   ├─ Verify: Author entity's source_raw contains current article filename
   └─ Cross-check: Article content mentions author name

3. If author is plain text:
   ├─ Trigger: Gate 1 (Author Identity Verification)
   └─ Wait for verification before continuing compile

4. Decision:
   ├─ Match → Continue with entity creation
   └─ Mismatch → Stop, output error message with specific inconsistency
```

**Blocking Rule:**
- Ingest stops if `entity.source_raw` doesn't contain the compiling article
- Error message shows exact mismatch for user to fix

---

## Implementation Changes

### README.md Section Updates

#### 1. Author Entity Workflow (revise existing section)

**Current:**
```markdown
**Author Entity 工作流**：
1. 联网搜索作者信息（Tavily）
2. 创建 entity 页面
3. 更新文章 author 字段为 `[[Author Name]]`
```

**New:**
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

#### 2. Entity Pages Frontmatter (add new fields)

**Add to existing section:**
```yaml
validated_source: "https://验证来源URL"  # 🆕 新增：身份验证来源
validated_at: "2026-04-13"              # 🆕 新增：验证日期
```

**Note:** Only required for Author entities (type=entity where content describes a person)

#### 3. Ingest Workflow (insert step 4)

**Current steps 1-3, then add:**
```markdown
4. **文章关联验证**（新增步骤）
   ├─ 检查 raw source 的 author 字段格式
   ├─ 若 author 为 wikilink `[[Author Name]]`：
   │  ├─ 验证 `10-wiki/entities/{Author-Name}.md` 存在
   │  ├─ 验证 entity 的 `source_raw` 包含当前文章文件名
   │  ├─ 若不一致：停止编译，输出错误信息：
   │  │  ```
   │  │  ⚠️ 文章关联验证失败
   │  │  文章: {当前文章名}
   │  │  作者 entity: {Author Name}
   │  │  entity.source_raw: {现有内容}
   │  │  应包含: {当前文章文件名}
   │  │  请手动修复后重新执行 compile
   │  │  ```
   │  └─ 一致则继续
   └─ 若 author 为纯文本：
      ├─ 触发 Author Entity 工作流（见上方）
      └─ 验证通过后才继续编译
```

**Then continue with existing step 5:**
```markdown
5. 为每个概念创建/更新 entity 页面
```

---

## Expected Outcomes

| Scenario | Old Behavior | New Behavior |
|---------|-------------|--------------|
| Creating unverified author | Entity created with guessed info | Blocked, plain text author used |
| Wrong article association | Error propagates silently | Blocked at compile, error shown |
| Author entity missing | Wikilink to non-existent entity | Blocked at compile, trigger creation |
| Correct association | Works normally | Works normally (with validation pass) |

---

## Non-Goals

- Lint-time periodic validation (deferred for future iteration)
- Automated script-based validation (deferred; this is documentation-only approach)
- Verification of non-author entities (concepts, topics) — out of scope

---

## Open Questions

None. Design is complete for trial period.

---

*Spec created: 2026-04-13*
*Author: Claude (AI Agent)*
*Status: Ready for user review*