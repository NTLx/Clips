---
type: output
title: 将 Obsidian 知识库部署为 LLM Wiki 网站
created: 2026-04-13
tags:
  - tutorial
  - quartz
  - obsidian
  - github-pages
  - llm-wiki
---

# 将 Obsidian 知识库部署为 LLM Wiki 网站

> 本教程教你如何将 Obsidian vault 自动部署为具有 Obsidian 同款体验的网站，实现本地与网页端的知识库无缝切换，便于分享和协作。

---

## 第1章：缘起 —— 从 Memex 到 LLM Wiki

### 1.1 Memex：知识存储的思想先驱

1945 年，Vannevar Bush 在《As We May Think》中提出了 **Memex** 的概念——一个个人知识存储设备，可以存储所有书籍、记录和通信，并通过关联链接快速检索。

这个思想影响了后来的超文本系统、万维网，以及今天的个人知识管理工具。

### 1.2 Andrej Karpathy 的 LLM Wiki

2026 年，AI 领域传奇人物 Andrej Karpathy（OpenAI 创始成员、Tesla AI 前总监）提出了 **LLM Wiki** 的理念：

> 用 LLM 作为知识库的「运营者」，持续编译和整理原始材料，构建一个可以累积知识的 Wiki。

核心思想：
- **知识编译**：Raw Sources → Wiki，LLM 将原始文章提炼为结构化知识
- **概念提取**：从文章中提取 Entity（概念页面），建立知识图谱
- **持续累积**：每次处理都沉淀到 Wiki 层，避免重复劳动

### 1.3 为什么我们需要"不止本地"的 Wiki

LLM Wiki 本质上是一个本地工具——你在自己的 Obsidian vault 中运营知识库。但这个模式有一个限制：

> **分享困难**。别人想查看你的知识库，必须：
> 1. 安装 Obsidian
> 2. 获取你的 vault 文件
> 3. 在本地打开

本教程的解决方案：通过 **Quartz + GitHub Actions + GitHub Pages**，将 Obsidian vault 自动部署为网站，让 LLM Wiki 更进一步——不止本地，还可网页访问。

---

## 第2章：架构 —— 本知识库的设计

### 2.1 目录结构一览

```
Clips/                        # 仓库根目录（也是 Quartz 的 content 源）
├── index.md                  # 知识库首页
├── raw/                      # Layer 0: 原始剪藏文章
│   ├── 20260408-article.md
│   └── ...
├── wiki/                     # Layer 1: 编译后的 Wiki
│   ├── entities/             # 概念页面
│   ├── topics/               # 主题页面
│   ├── comparisons/          # 对比分析
│   ├── outputs/              # 输出作品（本教程在这里）
│   └── lint-report.md        # 健康度报告
├── quartz.config.ts          # Quartz 配置
├── quartz.layout.ts          # Quartz 布局
├── package.json              # Node.js 配置
├── .github/
│   └── workflows/
│       └── deploy.yml        # GitHub Actions 部署流程
└── .obsidian/                # Obsidian 配置（被 ignorePatterns 排除）
```

### 2.2 三层架构简介

| 层级 | 路径 | 职责 | 维护者 |
|-----|------|------|--------|
| **Raw Sources** | `raw/` | 存储原始文章，不可变 | 用户 |
| **Wiki** | `wiki/` | 结构化知识，可更新 | AI Agent |
| **Schema** | `CLAUDE.md` | 工作流定义、规范 | 用户 + AI Agent |

> **注意**：本教程不会教你完整复制三层架构（那需要 AI Agent 编译流程）。这里重点是 Quartz 部署，架构理念帮助你理解"为什么这样组织目录"。

### 2.3 与纯 Quartz 部署的区别

标准 Quartz 部署通常使用单独的 `content/` 目录存放 Markdown 文件。本知识库的方案不同：

> **方案 C**：直接使用仓库根目录作为 content，通过 `ignorePatterns` 排除无关文件。

优势：
- Obsidian vault 和网站内容完全同步
- 无需维护两个位置的文件
- `raw/` 和 `wiki/` 自然映射为网站目录结构

### 2.4 核心特性

网站保持 Obsidian 的核心体验：

| 特性 | Obsidian 本地 | 网站端 |
|-----|--------------|--------|
| Wikilinks | ``文件名`` | ✅ 支持（短链接解析） |
| Callouts | `> [!info] 内容` | ✅ 支持美观渲染 |
| 知识图谱 | 本地 Graph View | ✅ 右侧面板显示 |
| 文件导航 | 文件树 | ✅ Explorer 组件 |
| 反向链接 | Backlinks 面板 | ✅ 右侧显示 |
| 搜索 | Ctrl+K | ✅ 全文搜索 |

---

## 第3章：配置 —— Quartz 核心文件详解

### 3.1 quartz.config.ts（完整配置）

这是 Quartz 的核心配置文件，定义网站行为、主题、插件和排除规则。

```typescript
import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4 Configuration for Obsidian Wiki
 *
 * 方案 C：直接使用仓库根目录作为 content
 * - 通过 ignorePatterns 排除所有无关文件
 * - 支持 Obsidian Flavored Markdown（wikilinks、callouts）
 * - shortest 链接解析：支持短链接跨目录引用
 */

const config: QuartzConfig = {
  configuration: {
    pageTitle: "你的 Wiki 名称",
    pageTitleSuffix: "",
    enableSPA: true,               // 单页应用模式，更流畅
    enablePopovers: true,          // 链接预览浮窗
    analytics: null,
    locale: "zh-CN",
    baseUrl: "your-username.github.io/your-repo",  // GitHub Pages 地址
    
    // ─────────────────────────────────────────────
    // ignorePatterns：哪些文件和文件夹不发布到网站
    // ─────────────────────────────────────────────
    ignorePatterns: [
      // Obsidian 配置和回收站
      ".obsidian",     // Obsidian 工作区配置（窗口布局、插件等）
      ".trash",         // Obsidian 回收站

      // 系统文件
      ".DS_Store",      // macOS 系统文件
      "._*",            // macOS 资源分支文件
      ".gitignore",     // Git 忽略规则

      // 开发配置文件
      "package.json",         // Node.js 配置
      "package-lock.json",    // 依赖锁定文件
      "tsconfig.json",        // TypeScript 配置
      "quartz.config.ts",     // Quartz 配置本身
      "quartz.layout.ts",     // Quartz 布局配置
      "node_modules",         // Node.js 依赖目录

      // Git/GitHub 相关
      ".git",           // Git 仓库数据
      ".github",        // GitHub Actions 配置

      // Schema 和日志文件（index.md 是首页，不应排除）
      "README.md",          // 仓库说明
      "CLAUDE.md",          // AI Agent Schema 文件
      "**/lint-report.md",  // 健康度报告

      // 非发布内容
      "docs",            // 内部文档目录
    ],
    
    defaultDateType: "modified",  // 文章日期默认使用修改时间
    
    // ─────────────────────────────────────────────
    // 主题配置
    // ─────────────────────────────────────────────
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Noto Sans SC",   // 中文标题字体
        body: "Noto Sans SC",     // 中文正文字体
        code: "JetBrains Mono",   // 代码字体
      },
      colors: {
        lightMode: {
          light: "#faf8f8",
          lightgray: "#e5e5e5",
          gray: "#b8b8b8",
          darkgray: "#4e4e4e",
          dark: "#2b2b2b",
          secondary: "#284b63",
          tertiary: "#84a59d",
          highlight: "rgba(143, 159, 169, 0.15)",
          textHighlight: "#fff23688",
        },
        darkMode: {
          light: "#161618",
          lightgray: "#393639",
          gray: "#646464",
          darkgray: "#d4d4d4",
          dark: "#ebebec",
          secondary: "#7b97aa",
          tertiary: "#84a59d",
          highlight: "rgba(143, 159, 169, 0.15)",
          textHighlight: "#b3aa0288",
        },
      },
    },
  },
  
  // ─────────────────────────────────────────────
  // 插件配置
  // ─────────────────────────────────────────────
  plugins: {
    transformers: [
      Plugin.FrontMatter(),      // 解析 YAML frontmatter
      
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "git", "filesystem"],  // 日期优先级
      }),
      
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      
      // ⭐ 核心：Obsidian Markdown 支持
      Plugin.ObsidianFlavoredMarkdown({
        enableInHtmlEmbed: false,
        comments: true,          // 支持 %% 注释 %%
      }),
      
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      
      // ⭐ 核心：短链接解析（支持 `文件名` 跨目录引用）
      Plugin.CrawlLinks({
        markdownLinkResolution: "shortest",  // 关键配置！
        linkProcessing: true,
      }),
      
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),  // 数学公式
    ],
    
    filters: [
      Plugin.RemoveDrafts(),  // 排除 draft: true 的文章
    ],
    
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),     // 文件夹索引页
      Plugin.TagPage(),        // 标签聚合页
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      Plugin.CustomOgImages(),  // 社交分享图片
    ],
  },
}

export default config
```

#### 关键配置说明

| 配置项 | 作用 | 推荐值 |
|-------|------|--------|
| `markdownLinkResolution: "shortest"` | Wikilinks 使用短链接，无需完整路径 | **必须设置** |
| `ObsidianFlavoredMarkdown` | 支持 Obsidian 特有语法（callouts、wikilinks） | 启用 |
| `ignorePatterns` | 排除不发布的文件和目录 | 根据需要调整 |
| `locale` | 语言设置，影响日期格式等 | `"zh-CN"` |

---

### 3.2 quartz.layout.ts（完整布局）

布局配置决定网站的 UI 结构：左侧导航、右侧面板、页面组件。

```typescript
import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"

/**
 * Quartz Layout Configuration for Obsidian Wiki
 *
 * 布局设计（模拟 Obsidian 界面）：
 * - 左侧：文件导航 (Explorer) + 搜索
 * - 右侧：知识图谱 (Graph) + 目录 (TOC) + 反向链接 (Backlinks)
 */

// 所有页面共享的组件
export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],  // 无顶部导航栏，保持简洁
  afterBody: [],
  footer: Component.Footer({
    links: {
      GitHub: "https://github.com/your-username/your-repo",
    },
  }),
}

// 单页内容布局（文章、Entity、Topic 页面）
export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    // 面包屑导航（首页除外）
    Component.ConditionalRender({
      component: Component.Breadcrumbs(),
      condition: (page) => page.fileData.slug !== "index",
    }),
    Component.ArticleTitle(),
    Component.ContentMeta(),   // 显示日期、阅读时间等
    Component.TagList(),       // 标签列表
  ],
  
  // ─────────────────────────────────────────────
  // 左侧面板：文件导航 + 搜索
  // ─────────────────────────────────────────────
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),  // 全文搜索
          grow: true,
        },
        { Component: Component.Darkmode() },   // 深色模式切换
        { Component: Component.ReaderMode() }, // 阅读模式
      ],
    }),
    
    // ⭐ Explorer：文件树导航
    Component.Explorer({
      title: "Explorer",
      folderDefaultState: "collapsed",   // 文件夹默认折叠
      folderClickBehavior: "collapse",   // 点击文件夹行为
      useSavedState: true,               // 保存折叠状态
      
      // 排序：文件夹优先，然后按名称
      sortFn: (a, b) => {
        if (!a.isFolder && b.isFolder) return 1
        if (a.isFolder && !b.isFolder) return -1
        return a.displayName.localeCompare(b.displayName, undefined, {
          numeric: true,
          sensitivity: "base",
        })
      },
      
      // 过滤：隐藏日志文件和标签目录
      filterFn: (node) => {
        if (node.displayName === "lint-report.md") {
          return false
        }
        if (node.slugSegment === "tags") {
          return false
        }
        return true
      },
      order: ["filter", "map", "sort"],
    }),
  ],

  // ─────────────────────────────────────────────
  // 右侧面板：知识图谱 + 目录 + 反向链接
  // ─────────────────────────────────────────────
  right: [
    // ⭐ Graph：知识图谱（模拟 Obsidian Graph View）
    Component.Graph({
      localGraph: {
        showTags: true,
        showAttachments: false,
        collapse: false,
        depth: 1,  // 当前页面 + 1层邻居
      },
      globalGraph: {
        showTags: true,
        showAttachments: false,
        collapse: true,
        depth: -1, // 显示全站图谱
      },
    }),
    
    Component.DesktopOnly(Component.TableOfContents()),  // 目录
    Component.Backlinks(),  // 反向链接面板
  ],
}

// 列表页布局（标签页、文件夹页）
export const defaultListPageLayout: PageLayout = {
  beforeBody: [
    Component.Breadcrumbs(),
    Component.ArticleTitle(),
    Component.ContentMeta()
  ],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        { Component: Component.Darkmode() },
      ],
    }),
    Component.Explorer({
      title: "Explorer",
      folderDefaultState: "collapsed",
      folderClickBehavior: "collapse",
      useSavedState: true,
      filterFn: (node) => {
        if (node.displayName === "lint-report.md") {
          return false
        }
        if (node.slugSegment === "tags") {
          return false
        }
        return true
      },
      order: ["filter", "map", "sort"],
    }),
  ],
  right: [],  // 列表页无右侧面板
}
```

#### 布局组件说明

| 组件 | 位置 | 功能 |
|-----|------|------|
| `Explorer` | 左侧 | 文件树导航，模拟 Obsidian 文件列表 |
| `Search` | 左侧 | 全文搜索 |
| `Graph` | 右侧 | 知识图谱，模拟 Obsidian Graph View |
| `TableOfContents` | 右侧 | 文章目录 |
| `Backlinks` | 右侧 | 反向链接，显示哪些页面引用了当前页 |
| `Breadcrumbs` | 页面顶部 | 面包屑导航 |

---

## 第4章：部署 —— GitHub Actions 自动化

### 4.1 GitHub Pages 基础设置

在 GitHub 仓库中启用 Pages：

1. 进入仓库 **Settings → Pages**
2. Source 选择 **GitHub Actions**（不是 Deploy from a branch）
3. 保存设置

### 4.2 deploy.yml（完整 Workflow）

```yaml
name: Deploy Obsidian Wiki to GitHub Pages

on:
  push:
    branches:
      - main  # 推送到 main 分支时触发

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false  # 不取消正在进行的部署

jobs:
  # ─────────────────────────────────────────────
  # 构建阶段：生成静态网站
  # ─────────────────────────────────────────────
  build:
    runs-on: ubuntu-22.04
    steps:
      # Step 1: Checkout 你的 Obsidian vault（content 源）
      - name: Checkout Wiki content
        uses: actions/checkout@v4
        with:
          fetch-depth: 0  # 获取完整 git 历史（用于日期提取）
          path: wiki      # 放在 wiki 目录

      # Step 2: Checkout Quartz 源码（构建引擎）
      - name: Checkout Quartz
        uses: actions/checkout@v4
        with:
          repository: jackyzha0/quartz  # Quartz 官方仓库
          ref: v4                       # 使用 v4 版本
          path: quartz                  # 放在 quartz 目录

      # Step 3: 安装 Node.js
      - uses: actions/setup-node@v4
        with:
          node-version: 22  # Quartz v4 需要 Node 22+

      # Step 4: 安装 Quartz 依赖
      - name: Install Quartz Dependencies
        working-directory: quartz
        run: npm ci

      # Step 5: 复制你的配置文件到 Quartz 目录
      - name: Setup Quartz Configuration
        run: |
          cp wiki/quartz.config.ts quartz/
          cp wiki/quartz.layout.ts quartz/

      # Step 6: 构建网站
      # 关键：-d ../wiki 表示使用 wiki 目录作为 content
      - name: Build Quartz Site
        working-directory: quartz
        run: npx quartz build -d ../wiki

      # Step 7: 上传构建产物
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: quartz/public  # Quartz 输出目录

  # ─────────────────────────────────────────────
  # 部署阶段：发布到 GitHub Pages
  # ─────────────────────────────────────────────
  deploy:
    needs: build  # 等待构建完成
    environment:
      name: github-pages
      url: `${{ steps.deployment.outputs.page_url }}`
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

### 4.3 构建流程详解

```
┌──────────────────────────────────────────────────────────────────┐
│                    GitHub Actions 构建流程                        │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. Checkout Wiki Content                                        │
│     └─ 你的 Obsidian vault → wiki/ 目录                          │
│                                                                  │
│  2. Checkout Quartz Source                                       │
│     └─ jackyzha0/quartz@v4 → quartz/ 目录                        │
│                                                                  │
│  3. Copy Config Files                                            │
│     └─ wiki/quartz.config.ts → quartz/                           │
│     └─ wiki/quartz.layout.ts → quartz/                           │
│                                                                  │
│  4. Build                                                        │
│     └─ npx quartz build -d ../wiki                               │
│     └─ 读取 ../wiki（你的 vault）作为 content                     │
│     └─ 应用 ignorePatterns 排除无关文件                           │
│     ├─ 处理 Markdown（wikilinks、callouts、frontmatter）          │
│     └─ 生成静态 HTML → quartz/public/                            │
│                                                                  │
│  5. Deploy                                                       │
│     └─ quartz/public → GitHub Pages                              │
│     └ 网站上线：https://your-username.github.io/your-repo/       │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

### 4.4 常见问题排查

| 问题 | 可能原因 | 解决方案 |
|-----|---------|---------|
| 构建失败 "Cannot find module" | Node 版本过低 | 确保 `node-version: 22` |
| Wikilinks 不解析 | 缺少 `ObsidianFlavoredMarkdown` | 检查 transformers 配置 |
| 链接指向错误页面 | 链接解析模式不对 | 设置 `markdownLinkResolution: "shortest"` |
| 文件出现在网站但不应出现 | ignorePatterns 配置错误 | 检查是否正确排除 `.obsidian`、配置文件等 |
| 日期显示不正确 | git 历史未获取 | 设置 `fetch-depth: 0` |

---

## 第5章：写作 —— Markdown 文档格式

为了让网站正确渲染 Obsidian 格式，你需要遵循以下规范。

### 5.1 YAML Frontmatter 规范

每篇 Markdown 文件开头应有 frontmatter：

```yaml
---
type: note           # 文档类型
title: 文章标题      # 显示标题
created: 2026-04-13  # 创建日期
updated: 2026-04-13  # 更新日期
tags:
  - 标签1
  - 标签2
draft: false         # 是否草稿（true 则不发布）
---
```

Quartz 会自动提取这些元数据用于：
- 文章标题和日期显示
- 标签聚合页面
- 排除草稿文章

### 5.2 Wikilinks 使用

Obsidian 的核心功能是 wikilinks（内部链接）。Quartz 通过 `markdownLinkResolution: "shortest"` 支持短链接格式：

```markdown
<!-- 基本引用 -->
`文件名`

<!-- 带别名 -->
`文件名\|显示文本`

<!-- 带锚点（跳转到某章节） -->
`文件名#章节标题`
```

> **关键**：使用**纯文件名**，不需要完整路径。Quartz 会自动找到匹配的文件。

例如：
- 文件位于 `wiki/entities/Taste.md`
- 引用时写 `[[Taste]]` 即可
- 不需要写 ``Taste``

### 5.3 Obsidian Callouts 语法

Callouts 是 Obsidian 的特色功能，用于突出显示信息块：

```markdown
> [!info] 信息提示
> 这是一个信息块，用于一般性说明。

> [!warning] 警告
> 这是警告内容，提醒读者注意潜在问题。

> [!tip] 建议
> 这是建议内容，提供最佳实践提示。

> [!important] 重要
> 这是重要内容，强调关键信息。

> [!note] 笔记
> 这是笔记内容，用于补充说明。

> [!example] 示例
> 这是示例内容，展示具体用法。

> [!quote] 引用
> 这是引用内容，来自其他来源。

> [!abstract] 摘要
> 这是摘要内容，总结文章要点。
```

网站会渲染为美观的彩色区块：

```
┌─────────────────────────────────────┐
│ 📌 信息提示                          │
│ 这是一个信息块，用于一般性说明。     │
└─────────────────────────────────────┘
```

### 5.4 图片引用方式

有两种方式引用图片：

**方式一：Obsidian 内部链接**
```markdown
!`image.png`
```
Quartz 会自动处理，图片显示在网站中。

**方式二：标准 Markdown**
```markdown
![图片描述](./images/image.png)
```
需要确保图片路径正确。

### 5.5 代码块与语法高亮

```markdown
```typescript
const config: QuartzConfig = {
  configuration: {
    pageTitle: "My Wiki",
  },
}
```

支持的语言：`typescript`, `javascript`, `python`, `bash`, `yaml`, `json`, `markdown` 等。

---

## 第6章：成果 —— 最终效果与进阶

### 6.1 本地 Obsidian vs 网站体验对比

| 功能 | Obsidian 本地 | 网站端 |
|-----|--------------|--------|
| 编辑文档 | ✅ 完整编辑能力 | ❌ 只读（浏览） |
| Wikilinks 点击 | ✅ 立即跳转 | ✅ 页面导航 |
| 知识图谱 | ✅ 本地 Graph View | ✅ 右侧 Graph 面板 |
| 文件导航 | ✅ 文件树 | ✅ Explorer 组件 |
| 搜索 | ✅ Ctrl+K | ✅ 全文搜索 |
| 反向链接 | ✅ Backlinks 面板 | ✅ 右侧显示 |
| 深色模式 | ✅ 主题切换 | ✅ Darkmode 按钮 |
| 分享给他人 | ❌ 需发送文件 | ✅ 直接发送链接 |

> **核心价值**：网站端保留了 Obsidian 的**导航体验**（wikilinks、graph、backlinks），同时实现了**零门槛分享**——对方无需安装任何软件，打开浏览器即可访问。

### 6.2 效果展示

> **Clips 知识库**（本教程所属的真实案例）
> 
> 网站地址：**https://ntlx.github.io/Clips/**

这是一个基于 Andrej Karpathy LLM Wiki 理念设计的知识库，包含：
- 69 个 Entity 页面（核心概念）
- 12 个 Topic 页面（主题整合）
- 5 个 Comparison 页面（对比分析）
- 30+ 篇 Raw 文章（原始剪藏）

打开网站，你可以体验：
- 左侧 Explorer 导航整个知识库
- 右侧 Graph 查看知识图谱
- 点击 wikilinks 在概念间跳转
- Backlinks 面板显示引用关系

### 6.3 如何自定义主题和布局

**修改配色**：编辑 `quartz.config.ts` 中的 `colors` 部分：

```typescript
colors: {
  lightMode: {
    secondary: "#你的颜色",  // 链接、标签颜色
    tertiary: "#你的颜色",   // 辅助颜色
  },
  darkMode: {
    // 同理
  },
}
```

**修改字体**：编辑 `typography` 部分：

```typescript
typography: {
  header: "你的标题字体",
  body: "你的正文字体",
  code: "你的代码字体",
}
```

**调整布局**：编辑 `quartz.layout.ts`：
- 添加/移除左侧组件
- 调整右侧面板顺序
- 修改 Explorer 默认折叠状态

### 6.4 如何分享你的 Wiki

部署完成后，分享方式：

1. **直接链接**：`https://your-username.github.io/your-repo/`
2. **特定文章**：`https://your-username.github.io/your-repo/wiki/entities/Taste`
3. **社交分享**：Quartz 自动生成 OpenGraph 图片，分享到社交媒体时显示预览

### 6.5 延伸阅读与参考资源

- [Quartz 官方文档](https://quartz.jzhao.xyz/)
- [Andrej Karpathy LLM Wiki](https://github.com/karpathy/llm.c)（思想来源）
- [Memex 概念](https://en.wikipedia.org/wiki/Memex)（知识管理先驱思想）
- [Obsidian 官方网站](https://obsidian.md/)

---

## 附录：快速开始检查清单

按照以下步骤，你可以快速部署自己的 Obsidian Wiki：

1. **准备 Obsidian vault**
   - 确保使用 wikilinks 格式
   - 添加 frontmatter 元数据
   - 组织好目录结构

2. **创建 GitHub 仓库**
   - 将 vault 上传到 GitHub
   - 确保 `main` 分支存在

3. **添加 Quartz 配置**
   - 创建 `quartz.config.ts`（复制本教程代码）
   - 创建 `quartz.layout.ts`（复制本教程代码）
   - 创建 `package.json`（最小化配置）

4. **添加 GitHub Actions**
   - 创建 `.github/workflows/deploy.yml`
   - 复制本教程 workflow

5. **启用 GitHub Pages**
   - Settings → Pages → Source: GitHub Actions

6. **推送并等待构建**
   - `git push origin main`
   - 查看 Actions 页面等待构建完成

7. **访问网站**
   - 打开 `https://your-username.github.io/your-repo/`
   - 享受你的 Obsidian Wiki 网站！

---

*本教程由 Clips 知识库出品，基于 Andrej Karpathy LLM Wiki 理念设计。*

*教程地址：本文件位于 `wiki/outputs/` 目录*

*最后更新：2026-04-13*