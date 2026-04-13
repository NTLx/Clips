---
type: comparison
title: PTY Mode vs Headless Mode
created: 2026-04-09
tags:
  - comparison
  - Claude-Code
  - Automation
related_entities:
  - "[[PTY-Mode]]"
  - "[[Headless-Mode]]"
  - "[[Claude-Code-CLI]]"
---

# PTY Mode vs Headless Mode

> [!summary] 对比概述
PTY Mode 模拟真实终端交互环境，适合需要实时交互的场景；Headless Mode 完全无界面运行，适合自动化流水线场景。

## 核心维度对比

| 维度 | PTY Mode | Headless Mode |
|-----|----------|---------------|
| **交互方式** | 模拟终端，支持实时输入输出 | 无交互，预设参数运行 |
| **输出处理** | 实时流式输出到终端 | 输出重定向到日志文件 |
| **错误处理** | 交互式确认，可中途干预 | 预定义策略，自动失败或重试 |
| **环境感知** | 能感知终端能力（颜色、尺寸） | 无终端特性，纯文本输出 |
| **权限控制** | 用户实时授权工具调用 | 预配置权限策略 |
| **调试体验** | 可实时观察和调整 | 只能事后分析日志 |

## 详细分析

### PTY Mode（伪终端模式）

PTY（Pseudo Terminal）Mode 创建一个虚拟终端环境，让 CLI 工具以为自己连接到了真实终端。

**核心特性**：
- 模拟 stdin/stdout/stderr 的终端行为
- 支持终端控制序列（ANSI escape codes）
- 实时双向通信通道
- 能处理交互式提示（如密码输入、确认对话框）

**技术实现**：
- 使用 fork 与 exec 创建子进程
- 通过 PTY master/slave 端点通信
- 支持信号传递（SIGINT, SIGTERM）

### Headless Mode（无头模式）

Headless Mode 完全脱离终端环境运行，不依赖任何显示或交互设备。

**核心特性**：
- 纯后台进程运行
- 所有输出重定向到文件或管道
- 无终端控制序列处理
- 依赖预配置而非实时决策

**技术实现**：
- 直接 exec 启动，无 PTY 包装
- 通过环境变量或配置文件传递参数
- 输出写入日志文件或标准流

## 使用场景

### PTY Mode 适用场景

| 场景 | 说明 |
|-----|------|
| **OpenClaw Agent 调用** | Agent 需实时观察 Claude Code 输出并做出决策 |
| **本地开发调试** | 开发者需要看到实时进度和错误信息 |
| **交互式工具调用** | 需要用户实时授权敏感操作 |
| **实时监控** | 需要流式输出供外部系统解析 |

### Headless Mode 适用场景

| 场景 | 说明 |
|-----|------|
| **CI/CD 自动化** | 在流水线中无人值守运行 |
| **批量处理任务** | 大规模并行执行，无需人工干预 |
| **定时任务** | Cron 或调度器触发的后台任务 |
| **容器化部署** | 在 Docker/Kubernetes 中运行 |

## OpenClaw Agent 集成示例

在 OpenClaw 项目中，PTY Mode 是调用 Claude Code 的核心方式：

```
Agent Process ←→ PTY Master ←→ PTY Slave ←→ Claude Code CLI
     ↑              实时读取              模拟终端
     └────────────── 流式输出 ──────────────┘
```

**关键优势**：
1. Agent 能实时解析 Claude Code 的输出流
2. 根据输出内容动态调整策略
3. 模拟用户交互（如通过 PTY 发送确认）

## 选择指南

> [!tip] 如何选择
> - 需要实时交互 → **PTY Mode**
> - 全自动化无人值守 → **Headless Mode**
> - 需要终端特性（颜色、进度条） → **PTY Mode**
> - 只关心最终结果 → **Headless Mode**

## 关联实体

- [[PTY-Mode]] - PTY 模式实体详情
- [[Headless-Mode]] - Headless 模式实体详情
- [[Claude-Code-CLI]] - Claude Code CLI 实体
- [[Agent-Integration]] - Agent 集成概念