---
type: entity
title: seekdb
definition: "OceanBase 推出的 AI 原生数据库，将关系型数据、向量、全文、JSON、GIS 统一在单一引擎"
created: 2026-04-09
updated: 2026-04-09
tags:
  - database
  - AI
  - vector-search
related_entities:
  - "[[OpenClaw]]"
  - "[[Claude-Skills]]"
source_raw:
  - "[[OpenClaw + seekdb skills：打造个人 seekdb 助手]]"
---

# seekdb

> [!definition] 定义
> seekdb 是 OceanBase 推出的 AI 原生数据库，可运行在各种设备上。它将关系型数据、向量、全文、JSON、GIS 等多种数据类型统一在单一引擎中，支持通过一条 SQL 完成向量搜索 + 全文搜索 + 关系查询的混合操作。

## 核心要点

### 五大特点

| 特点 | 说明 |
|------|------|
| **AI 原生** | 内置 embedding 生成、重排序、LLM 推理能力，数据库内完成 RAG 工作流 |
| **混合搜索** | 向量搜索 + 全文搜索 + 关系查询，一条 SQL 搞定所有 |
| **轻量易部署** | 最低 1 核 CPU + 2GB 内存即可运行，支持嵌入式、Docker、RPM |
| **MySQL 兼容** | 兼容 MySQL 语法与生态，支持完整 ACID 事务，学习成本低 |
| **开源免费** | Apache 2.0 许可，代码开源在 GitHub |

### 数据类型统一

单一引擎支持：
- 关系型数据
- 向量（用于语义搜索）
- 全文（用于关键词搜索）
- JSON
- GIS（地理信息）

### 混合搜索示例

一条 SQL 完成：
- 向量搜索（语义相似度）
- 全文搜索（关键词匹配）
- 关系查询（元数据过滤）

## 关联概念

- [[OpenClaw]] - seekdb Agent Skill 可在 OpenClaw 中加载
- [[Claude-Skills]] - seekdb Agent Skill 是 Skills 的典型应用案例

## 来源

- Raw Source: [[OpenClaw + seekdb skills：打造个人 seekdb 助手]]