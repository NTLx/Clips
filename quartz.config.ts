import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4 Configuration for Clips Wiki
 *
 * 方案 C：直接使用仓库根目录作为 content
 * - 通过 ignorePatterns 排除所有无关文件
 * - raw/ 和 wiki/ 自然映射为网站目录结构
 */

const config: QuartzConfig = {
  configuration: {
    pageTitle: "Clips Wiki",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    analytics: null,
    locale: "zh-CN",
    baseUrl: "ntlx.github.io/Clips",
    ignorePatterns: [
      // Obsidian 配置和回收站
      ".obsidian",
      ".trash",

      // 系统文件
      ".DS_Store",
      "._*",
      ".gitignore",

      // 开发配置文件
      "package.json",
      "package-lock.json",
      "tsconfig.json",
      "quartz.config.ts",
      "quartz.layout.ts",
      "node_modules",

      // Git/GitHub 相关
      ".git",
      ".github",

      // MCP 缓存
      ".playwright-mcp",

      // Schema 和日志文件（index.md 是首页，不应排除）
      "README.md",
      "CLAUDE.md",
      "AGENTS.md", // 兼容其他 AI Coding 工具的软链接
      "log.md",
      "**/log.md",
      "**/lint-report.md",

      // 非发布内容
      "docs",
    ],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Noto Sans SC",
        body: "Noto Sans SC",
        code: "JetBrains Mono",
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
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "git", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({
        enableInHtmlEmbed: false,
        comments: true,
      }),
      Plugin.GitHubFlavoredMarkdown({
        enableSmartyPants: false,
        linkHeadings: true,
      }),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({
        markdownLinkResolution: "shortest",
        linkProcessing: true,
      }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [
      Plugin.RemoveDrafts(),
    ],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      Plugin.CustomOgImages(),
    ],
  },
}

export default config