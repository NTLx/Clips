---
type: entity
title: Cybersecurity Proof of Work
aliases:
  - Cybersecurity Proof of Work
  - 安全 Proof of Work
  - Security as Proof of Work
definition: "Drew Breunig (2026) 提出的概念：网络安全变成 token 成本博弈，防御者需要花费比攻击者更多的 tokens 发现漏洞，而非依靠技术巧思。"
created: 2026-04-21
updated: 2026-04-21
tags:
  - cybersecurity
  - ai-security
  - proof-of-work
related_entities:
  - "[[Drew-Breunig]]"
  - "[[Mythos]]"
  - "[[Security-Hardening-Phase]]"
  - "[[Agentic-Engineering]]"
source_raw:
  - "20260414-cybersecurity-proof-of-work"
---

# Cybersecurity Proof of Work

> [!definition] 定义
> Drew Breunig (2026) 提出的概念：网络安全变成 token 成本博弈，防御者需要花费比攻击者更多的 tokens 发现漏洞。

## 关键数据点

- **核心方程**: "to harden a system you need to spend more tokens discovering exploits than attackers will spend exploiting them"
- **成本基准**: AISI 测试中 100M tokens = $12,500 per Mythos attempt
- **测试结果**: Mythos 完成 32 步企业网络攻击（人类需 20 小时），10 次尝试中成功 3 次
- **边际收益**: 100M tokens 预算仍未显示 diminishing returns

## 前提与局限性

- **前提**: 
  1. AI 模型持续发现漏洞的能力随 tokens 增加
  2. Tokens 成本相对稳定或下降
  3. 漏洞市场价值决定了攻击者投入上限
- **局限性**: 
  1. 推理成本变化可能改变博弈规则
  2. 真实攻击场景比测试更复杂
  3. 未考虑新型防御技术（如 AI 检测 AI 生成的攻击）

## 关联概念

- [[Drew-Breunig]] — 提出者
- [[Mythos]] — Anthropic 安全专用模型
- [[Security-Hardening-Phase]] — Agentic Coding 第三阶段
- [[Agentic-Engineering]] — 受影响的编程范式

## 跨域对标

| 类比 | 原域 | 映射 |
|------|------|------|
| **加密货币 Proof of Work** | 比特币挖矿 | 成功概率 ∝ 算力投入 |
| **Linus's Law 扩展** | 开源软件 | "eyeballs + tokens = shallow bugs" |

## 实践影响

1. **开源软件仍然重要**: 企业投入 tokens 审计 OSS，比自建更安全（Linus's law 扩展）
2. **Agentic Coding 三阶段**: 开发 → 代码审查 → 安全硬化（money 是硬化阶段瓶颈）
3. **代码成本**: 代码便宜，除非需要安全；安全成本由漏洞市场价值决定