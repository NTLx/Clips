# Wikilinks 短链接格式修复 实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将 76 个 Wiki 文件中的 208 处相对路径链接转换为短链接格式，确保 Obsidian 和 Quartz 正确解析。

**Architecture:** 使用 sed 正则表达式批量替换，先扫描生成完整链接列表，再逐类替换，最后验证无残留。

**Tech Stack:** bash/sed (正则替换), grep (扫描验证), git (提交)

---

## 文件结构

| 操作 | 文件路径 | 说明 |
|-----|---------|------|
| Modify | `10-wiki/entities/*.md` | ~60 个 Entity 文件 |
| Modify | `10-wiki/topics/*.md` | ~15 个 Topic 文件 |
| Modify | `10-wiki/comparisons/*.md` | ~5 个 Comparison 文件 |
| Modify | `README.md` | Schema 文件 |
| Create | `docs/superpowers/plans/2026-04-13-wikilinks-short-format-fix.md` | 本计划文件 |

---

### Task 1: 扫描并生成完整链接列表

**Files:**
- Create: `/tmp/wikilinks_scan.txt` (临时扫描结果)

- [ ] **Step 1: 扫描所有相对路径链接**

```bash
grep -rn '\[\[\.\./' 10-wiki/ README.md > /tmp/wikilinks_scan.txt
cat /tmp/wikilinks_scan.txt | wc -l
```

Expected: ~208 行输出

- [ ] **Step 2: 统计链接类型分布**

```bash
echo "=== source_raw 字段链接 ===" && grep -c 'source_raw:' /tmp/wikilinks_scan.txt
echo "=== 正文 Raw Source 行 ===" && grep -c 'Raw Source:' /tmp/wikilinks_scan.txt
echo "=== 正文普通链接 ===" && grep -cv 'source_raw:|Raw Source:' /tmp/wikilinks_scan.txt
```

Expected: 了解各类链接分布

---

### Task 2: 替换 source_raw 字段中的链接

**Files:**
- Modify: `10-wiki/entities/*.md`, `10-wiki/topics/*.md`, `10-wiki/comparisons/*.md`

- [ ] **Step 1: 替换 source_raw 中的 `[[../00-raw/web-clips/{分类}/{文件名}]]` 格式**

```bash
# 正则说明:
# \[\[\.\./00-raw/web-clips/[^/]+/  匹配 [[../00-raw/web-clips/{分类}/
# ([^\]]+)                         捕获文件名部分（不含 .md）
# \]\]                             匹配结束括号
# 替换为 [[{文件名}]]

find 10-wiki -name "*.md" -type f -exec sed -i '' 's/\[\[\.\./00-raw\/web-clips\/[^\/]*\/\([^\]]*\)\]\]/\[\[\1\]\]/g' {} \;
```

Expected: source_raw 字段链接已替换

- [ ] **Step 2: 验证 source_raw 替换结果**

```bash
grep -n 'source_raw:' 10-wiki/entities/*.md | head -20
grep -n 'source_raw:' 10-wiki/entities/*.md | grep '\[\[\.\./' | wc -l
```

Expected: 第二条命令返回 0（无残留）

---

### Task 3: 替换正文中的 Raw Source 行

**Files:**
- Modify: `10-wiki/entities/*.md`, `10-wiki/topics/*.md`

- [ ] **Step 1: 替换 `Raw Source: [[../00-raw/web-clips/{分类}/{文件名}]]` 格式**

```bash
# 正文 Raw Source 行格式: - Raw Source: [[../00-raw/web-clips/...]]
# 使用相同正则替换

find 10-wiki -name "*.md" -type f -exec sed -i '' 's/Raw Source: \[\[\.\./00-raw\/web-clips\/[^\/]*\/\([^\]]*\)\]\]/Raw Source: \[\[\1\]\]/g' {} \;
```

Expected: 正文 Raw Source 行已替换

- [ ] **Step 2: 验证 Raw Source 替换结果**

```bash
grep -n 'Raw Source:' 10-wiki/entities/*.md 10-wiki/topics/*.md | head -10
grep -n 'Raw Source:' 10-wiki/entities/*.md 10-wiki/topics/*.md | grep '\[\[\.\./' | wc -l
```

Expected: 第二条命令返回 0（无残留）

---

### Task 4: 替换 README.md 中的链接

**Files:**
- Modify: `README.md`

- [ ] **Step 1: 检查 README.md 中的相对路径链接**

```bash
grep -n '\[\[\.\./' README.md
```

Expected: 显示 README.md 中的链接位置

- [ ] **Step 2: 替换 README.md 中的链接**

```bash
# README.md 中的 source_raw 链接格式相同
sed -i '' 's/\[\[\.\./00-raw\/web-clips\/[^\/]*\/\([^\]]*\)\]\]/\[\[\1\]\]/g' README.md
```

Expected: README.md 链接已替换

- [ ] **Step 3: 验证 README.md 替换结果**

```bash
grep '\[\[\.\./' README.md
```

Expected: 返回空（无残留）

---

### Task 5: 处理特殊链接格式

**Files:**
- Modify: `10-wiki/*.md` (可能包含特殊格式的文件)

- [ ] **Step 1: 检查带别名的链接**

```bash
# 搜索带别名的相对路径链接格式: [[../path/file|别名]]
grep -rn '\[\[\.\./[^|]*|' 10-wiki/
```

Expected: 列出所有带别名的链接

- [ ] **Step 2: 替换带别名的链接**

```bash
# 正则说明:
# \[\[\.\./00-raw/web-clips/[^/]+/  匹配前缀路径
# ([^|\]]+)                        捕获文件名（不含别名）
# |([^]]+)                         捕获别名部分
# \]\]                             结束括号
# 替换为 [[{文件名}|{别名}]]

find 10-wiki -name "*.md" -type f -exec sed -i '' 's/\[\[\.\./00-raw\/web-clips\/[^\/]*\/\([^|]*\)|\([^\]]*\)\]\]/\[\[\1|\2\]\]/g' {} \;
```

Expected: 带别名链接已替换

- [ ] **Step 3: 处理 `../index` 链接**

```bash
# 搜索 ../index 链接
grep -rn '\[\[\.\./index' 10-wiki/
```

Expected: 列出所有 ../index 链接

- [ ] **Step 4: 替换 ../index 链接**

```bash
# 替换 [[../index|别名]] → [[index|别名]]
find 10-wiki -name "*.md" -type f -exec sed -i '' 's/\[\[\.\./index|\([^\]]*\)\]\]/\[\[index|\1\]\]/g' {} \;
# 替换 [[../index]] → [[index]]
find 10-wiki -name "*.md" -type f -exec sed -i '' 's/\[\[\.\./index\]\]/\[\[index\]\]/g' {} \;
```

Expected: ../index 链接已替换

---

### Task 6: 全量残留验证

**Files:**
- None (验证任务)

- [ ] **Step 1: 执行全量残留扫描**

```bash
grep -rn '\[\[\.\./' 10-wiki/ README.md
```

Expected: 返回空（无任何残留相对路径链接）

- [ ] **Step 2: 统计修复后的链接数量**

```bash
# 统计转换后的短链接数量
grep -rn '\[\[.*\]\]' 10-wiki/entities/*.md | grep 'source_raw:' | wc -l
grep -rn '\[\[.*\]]]' 10-wiki/entities/*.md | grep 'Raw Source:' | wc -l
```

Expected: 链接数量与原始扫描一致

---

### Task 7: 链接有效性验证

**Files:**
- None (验证任务)

- [ ] **Step 1: 提取所有短链接文件名**

```bash
# 提取 source_raw 中的文件名
grep -h 'source_raw:' 10-wiki/entities/*.md 10-wiki/topics/*.md | sed 's/.*\[\[\([^|]*\)\]\].*/\1/' | sort | uniq > /tmp/linked_files.txt
cat /tmp/linked_files.txt | wc -l
```

Expected: 显示引用的文件名列表

- [ ] **Step 2: 验证文件存在性**

```bash
# 检查每个链接的文件是否存在
while read f; do
  found=$(find 00-raw/web-clips -name "$f*" -type f 2>/dev/null | head -1)
  if [ -z "$found" ]; then
    echo "MISSING: $f"
  fi
done < /tmp/linked_files.txt
```

Expected: 返回空（所有链接文件都存在）

---

### Task 8: Git 提交

**Files:**
- Modify: 所有已修改的 Wiki 文件

- [ ] **Step 1: 检查修改状态**

```bash
git status --short
git diff --stat
```

Expected: 显示 76 个已修改文件

- [ ] **Step 2: 添加所有修改文件**

```bash
git add 10-wiki/entities/*.md 10-wiki/topics/*.md 10-wiki/comparisons/*.md README.md
```

Expected: 文件已暂存

- [ ] **Step 3: 提交修改**

```bash
git commit -m "$(cat <<'EOF'
fix: 统一 Wikilinks 为短链接格式

将所有相对路径链接 [[../00-raw/web-clips/{分类}/{文件名}]]
转换为短链接格式 [[{文件名}]]，确保 Obsidian 和 Quartz
正确解析。

影响范围:
- Entities: 60 个文件
- Topics: 15 个文件
- Comparisons: 5 个文件
- README.md: 1 个文件

总计修复 208 处链接
EOF
)"
```

Expected: 提交成功

- [ ] **Step 4: 验证提交**

```bash
git log -1 --oneline
git show --stat HEAD
```

Expected: 显示最新提交详情

---

## 验收清单

- [ ] `grep -r '\[\[\.\./' 10-wiki/ README.md` 返回空
- [ ] 所有 source_raw 字段使用短链接格式
- [ ] 所有 Raw Source 行使用短链接格式
- [ ] 所有链接文件物理存在
- [ ] Git 提交完成，包含清晰的 commit message