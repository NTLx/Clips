---
type: entity
title: Lean-Stack
aliases:
  - Lean Stack
definition: "极低成本（`$20/月`）独立运营盈利产品的技术栈，反共识选择 SQLite+Go+单机 VPS"
created: 2026-04-15
updated: 2026-04-15
tags:
  - software-engineering
  - bootstrap
  - indie-developer
related_entities:
  - "[[Steve-Hanov]]"
  - "[[Anti-Enterprise-Mindset]]"
  - "[[Runway-Math]]"
  - "[[Time-Moat]]"

source_raw:
  - "[[每月20成本，60000+营收：加拿大程序员的“最穷”技术栈]]"
---

# Lean-Stack（精益技术栈）

## 定义

**Lean-Stack** 是一种将月技术开销压到极低水平（`$20/月`或以下）仍能支撑盈利产品的技术架构选择。核心哲学：**成本接近零 = 无限跑道**。

## 标准配置

| 组件 | Lean-Stack 选择 | 传统选择 |
|------|---------------|---------|
| 服务器 | Linode/DigitalOcean `$5/月` (1GB RAM) | AWS/GCP `$50-500/月` |
| 数据库 | SQLite + WAL | PostgreSQL/MySQL |
| 语言 | Go (静态二进制) | Python/Node.js/Java |
| 认证 | 自写 OAuth2 (30 行) | Auth0/Clerk |
| 部署 | systemd service | Docker + K8s |

## 关键数据点

### SQLite vs PostgreSQL 性能对比

跑 10 万次 `SELECT 1` benchmark:
- PostgreSQL (localhost TCP): 2.77 秒
- PostgreSQL (Unix socket): 1.93 秒
- SQLite (内存): 0.07 秒 — **差距近 40 倍**

SQLite + WAL 支持多读者、单写者并发，查询走 C 函数调用（纳秒级），而 Postgres 需要经过 TCP 往返（毫秒级）。

### 内存效率

- Python gunicorn 4 workers: 基线 500MB
- Go 静态二进制: 几 MB

## 前提与局限性

- **适用场景**: 独立开发者、小型产品、月活 < 百万级的应用
- **不适用场景**: 需要多区域部署、PB 级数据、复杂分布式事务
- **关键前提**: WAL 模式下单写者限制，高并发写入场景需要额外设计
- **认知偏差**: 部分选择依赖 Steve Hanov 个人经验，不同产品可能需要不同方案

## 关联概念

- [[Anti-Enterprise-Mindset]] — 不买"万一"的账
- [[Runway-Math]] — 低成本的数学逻辑
- [[Constraint-Driven-Engineering]] — 约束决定技术选择
- [[Steve-Hanov]] — 实践者
