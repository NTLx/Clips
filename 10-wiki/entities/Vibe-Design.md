---
type: entity
title: Vibe Design
definition: "AI 时代的设计范式：描述感受而非操作软件，AI 生成高保真设计"
created: 2026-04-10
updated: 2026-04-10
tags:
  - AI-Agent
  - design
  - coding-agents
related_entities:
  - "[[Vibe-Coding]]"
  - "[[ACI-Agent-Computer-Interface]]"
source_raw:
  - "[[../00-raw/inbox/100% 免费开源！Google Stitch 发布了 DESIGN.md...md]]"
---

# Vibe Design（氛围设计）

> **核心类比**：Vibe Design = Vibe Coding 在设计端的平替

## 定义

**Vibe Design** 是 Google Stitch 提出的概念，描述 AI 时代的设计范式转变：

> 不在设计软件中操作，而是描述想要的风格、感受、要解决的业务问题，AI 直接生成高保真设计稿。

## 与传统设计对比

| 维度 | 传统设计 | Vibe Design |
|------|---------|-------------|
| 操作方式 | 拖拽按钮、调整间距 | 描述风格和感受 |
| 配色 | 手动选择、担心不协调 | 选择预置主题 |
| 修改 | 逐个调整 | 主题应用全局 |
| 输出 | 设计文件 | HTML 代码 + 设计图 |

## Stitch 2.0 能力

### 专业配色方案

- 内置 10+ 专业配色方案
- 涵盖深色模式到清新亮色
- 切换主题自动更新所有设计

### 无限画布

- 类 Figma 的无限延展界面
- 更顺滑的交互效果
- 全选下载：每个页面 HTML + 设计图

## DESIGN.md：教会 Agent 设计系统

> 一个 Markdown 文件，让 AI Coding Agent 理解整个设计系统

### 特点

- 不需要导出 Figma
- 不需要 JSON
- 不需要繁琐配置
- Agent 直接读取，理解按钮样式、字体、间距

### 预构建模板

40+ 预构建文件，提取自真实产品：

- Stripe, Vercel, Linear, Notion
- Lovable, Claude, EleLabs
- Warp, Zapier 等

## 自动化交付工作流

```
Stitch 设计参考 → Agent 实现 → Sub-agent 审计验证 → 编译确认
```

### Sub-agent 验证逻辑

- 审计每个改动视图
- 检查间距、链接
- 确保符合设计要求
- 自动编译测试

## 角色转变

> [!tip] 核心转变
> 设计师从"画图"转变为"定义感受"。
> 
> 工具在变，但创造美好体验的核心永远不变。

## 相关概念

- [[Vibe-Coding]] - 编程端的对应概念
- [[ACI-Agent-Computer-Interface]] - Agent 理解设计的接口
- [[Compound-Engineering]] - 持续改进设计系统

---

> **来源**：Google Stitch 2.0, "DESIGN.md", 2026-04