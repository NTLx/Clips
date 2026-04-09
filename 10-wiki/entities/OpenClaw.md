---
type: entity
title: OpenClaw
definition: "运行在用户自己设备上的个人 AI 助手，支持多渠道接入和 Skill 扩展"
created: 2026-04-09
updated: 2026-04-09
tags:
  - AI-Agent
  - personal-assistant
related_entities:
  - "[[Claude-Skills]]"
  - "[[seekdb]]"
source_raw:
  - "[[../00-raw/web-clips/OpenClaw/OpenClaw + seekdb skills：打造个人 seekdb 助手]]"
---

# OpenClaw

> [!definition] 定义
> OpenClaw 是一款运行在用户自己设备上的个人 AI 助手，在已有的沟通渠道（WhatsApp、Telegram、Slack、Discord、Signal、iMessage、WebChat 等）上对话，也支持通过本地 TUI 或 Web 界面直接聊天。

## 核心要点

### 三大特点

| 特点 | 说明 |
|------|------|
| **本地优先** | 数据与对话由用户掌控，可完全在本地或自建环境中运行 |
| **多渠道** | 同一助手可接入多种即时通讯与开发工具 |
| **可扩展** | 通过 Skill（技能）为助手注入领域知识或工具能力 |

### 安装方式

环境要求：Node.js ≥ 22

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

安装流程：
1. 选择 QuickStart 快速配置
2. 选择 provider 并输入 API Key
3. 选择模型
4. 配置 Hooks（可选）
5. 使用 TUI 或 Web UI

### 配置文件

- `openclaw.json`: 所有配置写入此文件，可手动编辑
- Workspace 路径: `~/.openclaw/workspace`，默认操作目录，Skills 放于此
- Sessions: 会话持久化，关闭终端不结束，输入 `/new` 开启新会话

### Skill 管理

查看已安装技能：
```bash
openclaw skills
```

或通过 Web UI 的 Skills 选项卡查询。

## 关联概念

- [[Claude-Skills]] - OpenClaw 支持 Agent Skills 开放标准
- [[seekdb]] - seekdb Agent Skill 是 OpenClaw 的典型应用

## 来源

- Raw Source: [[../00-raw/web-clips/OpenClaw/OpenClaw + seekdb skills：打造个人 seekdb 助手]]