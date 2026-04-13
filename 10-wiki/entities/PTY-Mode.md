---
type: entity
title: PTY Mode
definition: "PTY（伪终端）模式是 OpenClaw 调用 Claude Code 时必须使用的终端技术，确保 CLI 工具正确运行而不挂起或输出乱码。"
created: 2026-04-09
updated: 2026-04-09
tags:
  - AI-Agent
  - Claude-Code
  - Technical-Implementation
related_entities:
  - "[[Claude-Code-CLI]]"
  - "[[Headless-Mode]]"
  - "[[Agent-Orchestration]]"
source_raw:
  - "[[Claude code最小闭环核心文档 openclaw agent skill]]"
  - "[[Openclaw自己操作Claude code完整开发了TikTok爆款分析系统]]"
---

# PTY Mode

> [!definition] 定义
> PTY（Pseudo Terminal，伪终端）模式是 OpenClaw 通过 exec 调用 Claude Code 时**必须使用**的技术。没有 PTY，Claude Code 的 CLI 会挂起或输出不可用，这是 OpenClaw 社区中无数人踩过的坑。

## 为什么必须使用 PTY

Claude Code 是一个交互式 CLI 工具，它期望运行在真实的终端环境中。当通过普通的 exec 调用时：

- CLI 可能**挂起**（waiting for input that never comes）
- 输出可能**乱码**（terminal escape sequences not interpreted）
- 进程可能**异常退出**

PTY 提供了一个"虚拟终端"，让 Claude Code 认为自己运行在真实终端中，从而正常工作。

## 推荐调用模式

```bash
# OpenClaw 调用 Claude Code 的标准模式
bash pty:true workdir:~/projects/xxx background:true \
  command:"claude --session-id xxx --permission-mode acceptEdits '你的任务指令'"
```

### 关键参数解析

| 参数 | 作用 |
|-----|------|
| `pty:true` | 使用伪终端模式，防止 CLI 挂起 |
| `background:true` | 后台运行，OpenClaw 可继续处理其他任务 |
| `--session-id` | 保持会话上下文，中断后可 --resume 恢复 |
| `--permission-mode acceptEdits` | 自动接受编辑，不用每改一个文件都停下来问 |

## 解决的三大问题

PTY + background + session-id 组合解决了 OpenClaw 直接调用 Claude Code 的三个致命问题：

1. **进程管理空白**：Claude Code 进程可能因内存、网络、上下文等原因死掉，session-id 支持恢复
2. **交互阻塞卡死**：Claude Code 经常停下来问问题，background:true 让任务后台运行
3. **结果送不回来**：--output-format json 提供结构化输出，OpenClaw 可获取执行结果

## 实战案例

在 TikTok 爆款分析系统开发中，作者发现：

> "没有 PTY，Claude Code 的 CLI 会挂起或者输出乱码。OpenClaw 社区里无数人踩过这个坑。加上 pty:true 就解决了。"

## 来源

- Raw Source: [[Claude code最小闭环核心文档 openclaw agent skill]]
- Raw Source: [[Openclaw自己操作Claude code完整开发了TikTok爆款分析系统]]