---
type: entity
title: Mythos
aliases:
  - Mythos
  - Claude Mythos
  - Anthropic Mythos
definition: "Anthropic (2026) 的安全专用 LLM 模型，在网络安全任务上表现'strikingly capable'，因安全考虑未公开发布，仅向关键软件制造商提供访问。"
created: 2026-04-21
updated: 2026-04-21
tags:
  - ai-model
  - cybersecurity
  - anthropic
related_entities:
  - "[[Cybersecurity-Proof-of-Work]]"
  - "[[Drew-Breunig]]"
  - "[[AISI]]"
source_raw:
  - "20260414-cybersecurity-proof-of-work"
---

# Mythos

> [!definition] 定义
> Anthropic (2026) 的安全专用 LLM 模型，在网络安全任务上表现卓越。

## 关键数据点

- **发布**: 2026 年 4 月（preview）
- **访问限制**: 仅向关键软件制造商提供（Glasswing 项目）
- **安全能力**: AISI 测试中完成 32 步企业网络攻击模拟（人类需 20 小时）
- **成本**: 100M tokens per attempt = `$12,500`
- **成功率**: 10 次尝试中成功 3 次（唯一完成任务的模型）

## 前提与局限性

- **前提**: Anthropic 判断模型安全能力过高，公开风险大于收益
- **局限性**: 
  1. 测试结果来自 AISI，需更多独立验证
  2. 真实攻击场景可能比测试更复杂
  3. 模型仍未显示边际收益递减，意味着持续投入 tokens 可能持续发现漏洞

## 关联概念

- [[Cybersecurity-Proof-of-Work]] — 模型能力支撑的概念
- [[AISI]] — 测试机构（英国 AI 安全研究所）
- [[Drew-Breunig]] — 分析者

## Anthropic Glasswing 项目

Anthropic 为 Mythos 创建的访问控制机制：
- 仅"critical software makers"可获得访问
- 提供时间窗口进行安全硬化
- 体现 Anthropic 对 AI 安全的谨慎态度