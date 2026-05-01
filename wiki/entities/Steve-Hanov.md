---
type: entity
title: Steve Hanov
aliases:
  - Steve Hanov
definition: "加拿大 Waterloo 独立开发者，一人运营 6 个 `$10K+` MRR 产品，月技术成本仅 `$20`，代表 Lean-Stack 实践者"
created: 2026-04-15
updated: 2026-04-15
tags:
  - person
  - indie-developer
  - bootstrap
source_raw:
  - "[[每月20成本，60000+营收：加拿大程序员的“最穷”技术栈]]"
validated_source: "https://stevehanov.ca/"
validated_at: "2026-04-15"
---

# Steve Hanov

## 简介

Steve Hanov 是加拿大 Waterloo 的独立开发者，一人运营 6 个月收入 `$10K+` MRR 的产品，总计月入六位数美元。他以极低的月固定成本（`$20/月`）和反共识的技术选型而闻名，2026 年在 Hacker News 上获得 952 分关注。

## 产品组合

| 产品 | 创建年份 | 商业模式 | 备注 |
|------|---------|---------|------|
| websequencediagrams.com | 2008 | Freemium + 企业版 | 18 年老产品，SEO 第一 |
| zwibbler.com | 2011-2013 | B2B 永久许可 `$5,999` | 嵌入式白板 SDK |
| rhymebrain.com | 2009-2010 | 广告 + API | 8 语种押韵词典 |
| rapt.ink | 2015-2018 | C 端 Freemium | 浏览器矢量图形编辑器 |
| xreplyextension.com | 2024 | 一次性点数 `$9/``$19/``$49` | X/Twitter AI 回复扩展 |
| eh-trade.ca | 2025-2026 | 金融订阅 | 加美股智能分析 |

## 技术栈

- **服务器**: Linode / DigitalOcean, 1GB RAM, `$5/月`
- **数据库**: SQLite + WAL (非 Postgres)
- **语言**: Go (非 Python/Node)
- **认证**: 自写 30 行 OAuth2
- **部署**: systemd service 文件
- **AI 开发**: GitHub Copilot per-request 定价漏洞, `$13/月`
- **本地 AI**: RTX 3090 + VLLM + Ollama

## 开源工具

- **laconic** — Go 写的 AI agent, 做"上下文分页"(类似 OS 虚拟内存, 把不相关对话 swap 出去)
- **llmhub** — LLM 统一接口抽象, 故障自动切换(Anthropic → OpenAI → 本地 VLLM)

## 核心哲学

> "Keeping costs near zero gives you the exact same runway as getting a million dollars in funding."

> "The tech industry wants you to believe that building a real business requires complex orchestration. It doesn't."
