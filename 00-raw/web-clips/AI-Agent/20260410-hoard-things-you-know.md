---
type: raw
source: "https://simonwillison.net/guides/agentic-engineering-patterns/hoard-things-you-know-how-to-do/"
author:
  - "[[Simon Willison]]"
published: "2026-02-26"
updated: "2026-03-16"
created: "2026-04-10"
tags:
  - clippings
  - AI-Agent
  - agentic-engineering
  - coding-agents
  - knowledge-management
description: "作者分享了'囤积你知道如何做的事情'这一重要实践，作为与编码代理高效工作的核心技巧。文章强调收集可运行的代码示例的价值，以及如何将这些资产作为编码代理的输入来构建新工具。"
changes_url: "https://simonwillison.net/guides/agentic-engineering-patterns/hoard-things-you-know-how-to-do/changes/"
---

# Hoard things you know how to do

许多关于高效使用编码代理的建议都是我职业生涯中在没有它们时也觉得有用的建议的延伸。**囤积你知道如何做的事情**就是一个很好的例子。

## 核心观点

构建软件技能的一个重要部分是理解什么是可能的、什么是不可能的，并且至少对这些事情如何实现有一个粗略的想法。

这些问题可以是广泛的，也可以是相当晦涩的：
- 网页能否仅用 JavaScript 运行 OCR 操作？
- iPhone 应用能否在不运行时与蓝牙设备配对？
- 我们能否在 Python 中处理 100GB 的 JSON 文件而不将其全部加载到内存中？

你对这类问题的答案越多，你就越有可能发现用技术解决问题的机会，而其他人可能还没想到这些方式。

## 运行代码是最好的证明

对这些问题有信心回答的最佳方式是**看到运行中的代码**来证明它们。

知道某事理论上可能与你亲眼看到它完成是不同的。作为软件专业人士需要发展的关键资产是对这类问题的答案的深度收集，并附带这些答案的证明。

## 囤积解决方案的方式

我用多种方式囤积解决方案：

- **博客和 TIL 博客** - 充满了我弄清楚如何做的事情的笔记
- **GitHub repos** - 超过一千个仓库，收集我为不同项目编写的代码，许多是演示关键想法的小型概念验证
- **tools.simonwillison.net** - LLM 辅助工具和原型的大型集合，收集"HTML tools" - 嵌入 JavaScript 和 CSS 并解决特定问题的单 HTML 页面
- **simonw/research 仓库** - 更大、更复杂的示例，挑战编码代理研究问题并返回工作代码和书面报告

## 从囤积中重组

为什么要收集这些东西？除了帮助你构建和扩展自己的能力，你在过程中生成的资产成为编码代理的强大输入。

我最喜欢的提示模式之一是告诉代理**通过组合两个或更多现有的工作示例来构建新东西**。

### OCR 工具案例

一个帮助我认识到这有多有效的项目是我添加到工具集合的第一个东西 - 一个基于浏览器的 OCR 工具。

我想要一个简单的、基于浏览器的工具来 OCR PDF 文件的页面 - 特别是完全由扫描图像组成且没有提供文本版本的 PDF。

我之前尝试过在浏览器中运行 Tesseract.js OCR 库，发现它非常强大。该库提供了成熟 Tesseract OCR 引擎的 WebAssembly 构建，可以从 JavaScript 调用它从图像中提取文本。

我不想处理图像，我想处理 PDF。然后我记得我也用过 Mozilla 的 PDF.js 库，它可以将 PDF 的各个页面转换为渲染的图像。

我在笔记中有这两个库的 JavaScript 片段。我把两个例子组合起来描述我要的解决方案，喂给模型，结果完美运行。

## 编码代理让囤积更有价值

编码代理让囤积工作示例变得更加有价值。

如果你的编码代理有互联网访问，你可以让它做类似：

> Use curl to fetch the source of https://tools.simonwillison.net/ocr and https://tools.simonwillison.net/gemini-bbox and build a new tool that lets you select a page from a PDF and pass it to Gemini to return bounding boxes for illustrations on that page.

编码代理擅长搜索，这意味着你可以在自己的机器上运行它们，告诉它们在哪里找到你想让它们做的事情的示例：

> Add mocked HTTP tests to the ~/dev/ecosystem/datasette-oauth project inspired by how ~/dev/ecosystem/llm-mistral is doing it.

由于我的很多研究代码是公开的，我经常告诉编码代理克隆我的仓库到 `/tmp` 并用作输入：

> Clone simonw/research from GitHub to /tmp and find examples of compiling Rust to WebAssembly, then use that to build a demo HTML page for this project.

## 关键思想

编码代理意味着我们只需要一次找出一个有用的技巧。如果那个技巧随后被某个地方用工作代码示例记录下来，我们的代理可以查阅那个示例并用它来解决未来任何类似形状的项目。

---

> [!info] 元数据
> - Created: 26th February 2026
> - Last modified: 16th March 2026
> - 9 changes
> - Author: [[Simon Willison]]
> - Previous: [[Writing code is cheap now]]
> - Next: [[AI should help us produce better code]]
> - Series: Agentic Engineering Patterns

## AI 提取摘要

### 核心概念
1. **Knowledge Hoarding** - 囤积你知道如何做的事情，收集可运行代码示例作为资产
2. **Proof-of-Concept Collection** - 概念验证集合，小型代码示例演示关键想法
3. **Recombination Pattern** - 重组模式，组合多个现有工作示例构建新工具
4. **HTML Tools** - 单 HTML 页面工具，嵌入 JS/CSS 解决特定问题

### 关键洞察
- 理解"什么可能"和"如何实现"是软件构建的核心技能
- 运行代码比理论知识更能证明可行性
- 编码代理让囤积的价值倍增 - 只需一次找到技巧，代理可复用
- 公开的研究代码可成为代理的有效输入

### 实践建议
- 维护博客/TIL 记录解决方案
- 收集 GitHub repos 作为概念验证
- 构建 HTML tools 集合
- 用 prompt 指引代理组合现有示例

### 案例研究
OCR 工具开发：组合 Tesseract.js（图像 OCR）和 PDF.js（PDF 转图像）两个库的工作示例，通过单个 prompt 生成完整的 PDF OCR 工具。