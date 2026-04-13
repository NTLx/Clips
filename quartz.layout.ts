import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"

/**
 * Quartz Layout Configuration for Clips Wiki
 *
 * 布局设计：
 * - 左侧：文件导航 (Explorer) + 搜索
 * - 右侧：知识图谱 (Graph) + 目录 (TOC) + 反向链接 (Backlinks)
 */

// 所有页面共享的组件
export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  afterBody: [],
  footer: Component.Footer({
    links: {
      GitHub: "https://github.com/NTLx/Clips",
    },
  }),
}

// 单页内容布局（Entity/Topic/Comparison/文章）
export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    Component.ConditionalRender({
      component: Component.Breadcrumbs(),
      condition: (page) => page.fileData.slug !== "index",
    }),
    Component.ArticleTitle(),
    Component.ContentMeta(),
    Component.TagList(),
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
        { Component: Component.ReaderMode() },
      ],
    }),
    Component.Explorer({
      title: "Explorer",
      folderDefaultState: "collapsed",
      folderClickBehavior: "collapse",
      useSavedState: true,
      sortFn: (a, b) => {
        // 文件夹优先，然后按名称排序
        if (!a.isFolder && b.isFolder) return 1
        if (a.isFolder && !b.isFolder) return -1
        return a.displayName.localeCompare(b.displayName, undefined, {
          numeric: true,
          sensitivity: "base",
        })
      },
      filterFn: (node) => {
        // 隐藏 log.md 和 lint-report.md
        if (node.displayName === "log.md" || node.displayName === "lint-report.md") {
          return false
        }
        // 保留默认的 tags 过滤
        if (node.slugSegment === "tags") {
          return false
        }
        return true
      },
      order: ["filter", "map", "sort"],
    }),
  ],
  right: [
    Component.Graph({
      localGraph: {
        showTags: true,
        showAttachments: false,
        collapse: false,
        depth: 1,  // 恢复默认：当前页面 + 1层邻居
      },
      globalGraph: {
        showTags: true,
        showAttachments: false,
        collapse: true,
        depth: -1, // 恢复默认：显示全站图谱
      },
    }),
    Component.DesktopOnly(Component.TableOfContents()),
    Component.Backlinks(),
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
        if (node.displayName === "log.md" || node.displayName === "lint-report.md") {
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
  right: [],
}