---
type: topic
title: Claude Code Automation
created: 2026-04-09
updated: 2026-04-14
tags:
  - Claude-Code
  - Automation
  - OpenClaw
related_entities:
  - "[[Agent-Orchestration]]"
  - "[[Claude-Code-CLI]]"
  - "[[Headless-Mode]]"
  - "[[Wes-Botman]]"
  - "[[同学都叫我-饶老师]]"
source_raw: []
---

# Claude Code Automation

> [!summary] 概要
> Claude Code 自动化是将 Claude Code CLI 工具转化为可编程、可编排的编码引擎的核心技术。通过 PTY 模式、Headless 模式、Skill 文件等组合，实现 OpenClaw 对 Claude Code 的自主调用，让"项目经理"指挥"工程师"完成开发闭环。

## 核心架构

Claude Code 自动化依赖三个关键技术支柱：

```
┌─────────────────────────────────────────────────────────────┐
│              Claude Code 自动化调用架构                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐     │
│  │  PTY Mode   │ +  │ Headless    │ +  │ Skill File  │     │
│  │  终端交互   │    │ Mode        │    │ 流程定义    │     │
│  └─────────────┘    └─────────────┘    └─────────────┘     │
│         ↓                  ↓                  ↓            │
│  ┌─────────────────────────────────────────────────────┐  │
│  │           OpenClaw 编排层                            │  │
│  │    任务拆解 → 进度监控 → 错误处理 → 结果汇总         │  │
│  └─────────────────────────────────────────────────────┘  │
│                          ↓                                 │
│  ┌─────────────────────────────────────────────────────┐  │
│  │           自动化开发闭环                             │  │
│  │    需求 → PRD → 开发 → 测试 → 报告 → 用户验收       │  │
│  └─────────────────────────────────────────────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## 三大核心概念

### 终端交互技术

PTY（伪终端）是 OpenClaw 调用 Claude Code 的**必须技术**：

```bash
bash pty:true workdir:~/projects/xxx background:true \
  command:"claude --session-id xxx --permission-mode acceptEdits '任务'"
```

解决的问题：
- CLI 挂起（无终端输入）
- 输出乱码（terminal escape sequences）
- 进程失控（无后台管理）

### [[Headless-Mode]] - 非交互自动化

Headless Mode 通过 `-p` 参数实现单次执行：

```bash
claude -p "实现用户认证功能" \
  --allowedTools "Read,Write,Edit,Bash" \
  --max-turns 10 \
  --output-format json
```

关键参数：
- `--allowedTools`：限制工具权限（安全）
- `--max-turns`：防止无限循环
- `--session-id`：多轮对话上下文保持
- `--output-format json`：结构化输出

### Skill 文件 - 流程定义

Skill 文件定义完整的开发流程：

```markdown
---
description: "全栈项目开发技能"
---

# Fullstack Development Skill

## Phase 1：需求理解 → PRD
## Phase 2：项目初始化
## Phase 3：逐功能开发
## Phase 4：自动化测试
## Phase 5：交付报告
```

## 项目经理模式

OpenClaw 作为项目经理，Claude Code 作为工程师：

| 角色 | 职责 |
|-----|------|
| **项目经理（OpenClaw）** | 接需求 → 写 PRD → 拆任务 → 盯进度 → 处理报错 → 测试验收 |
| **工程师（Claude Code）** | 接任务 → 写代码 → 跑测试 → 返回结果 |
| **用户** | 确认方案 → 看最终效果 |

> "我当老板。全程我只参与两个节点：确认方案、看最终效果。"

## 自动化开发闭环

```
用户发需求（飞书）
    ↓
OpenClaw 写 PRD + 技术方案 → 用户确认
    ↓
OpenClaw 拆功能 → 逐个委派 Claude Code（PTY + background）
    ↓
Claude Code 开发 → 需要敏感信息才问用户
    ↓
开发完成 → Playwright 自动测试 → 截图发报告
    ↓
用户验收 → 部署上线
```

## 解决的三大痛点

直接用 Claude Code 的问题：

| 问题 | 解决方案 |
|-----|---------|
| **进程管理空白** | `--session-id` + `--resume` 支持恢复 |
| **交互阻塞卡死** | `background:true` 后台运行 |
| **结果送不回来** | `--output-format json` 结构化输出 |

## 实战案例

### TikTok 爆款分析系统

用户需求（飞书发送）：
```
我要开发的产品是：tiktok视频拆解网站。
功能是，用户上传一个视频后，能逆向出它的提示词、拆成多个视频片段做更细致的分析。
主要目的是帮助用户分析爆款视频，并且提炼出来一套玩法后，自己能复刻、模拟生成这类爆款。
```

OpenClaw 自主流程：
- 写 PRD + 技术方案 → 发给用户确认
- PTY 模式启动 Claude Code → 初始化项目
- 逐功能拆解 → 一个一个委派开发
- 每功能完成自动检查输出 → 报错自动修
- 需要 API Key 才问用户
- 开发完 Playwright 测试 → 截图发飞书

## 最佳实践总结

### 黄金法则

1. **用 `-p` 非交互模式**，不要尝试驱动 TUI
2. **始终指定 `--max-turns`**，防止无限循环
3. **始终指定 `--allowedTools`**，最小权限原则
4. **用 PTY 启动**，否则 CLI 可能挂起
5. **用 `--output-format json`** 获取结构化输出
6. **用 `--session-id`** 保持多轮对话上下文

### 任务模板

```bash
# 代码审查
claude -p "Review src/ for bugs" \
  --allowedTools "Read,Grep,Glob" \
  --permission-mode plan \
  --max-turns 5

# 实现功能
claude -p "Implement user auth with JWT" \
  --allowedTools "Read,Write,Edit,Bash" \
  --max-turns 15

# 修复 Bug
claude -p "Fix the login bug" \
  --allowedTools "Read,Write,Edit,Bash" \
  --max-turns 10
```

## 相关 Entity

- [[Claude-Code-CLI]] - Claude Code CLI 工具定义
- [[Headless-Mode]] - Headless 模式详解
- [[Agent-Orchestration]] - 编排层架构

## 参见

- [[Wes-Botman]] - Claude Code 实践文章作者
- [[同学都叫我-饶老师]] - Prompt 工程与 Claude Code 实践文章作者

## 来源