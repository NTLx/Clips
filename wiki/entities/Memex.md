---
type: entity
title: Memex
definition: "Vannevar Bush 1945 年提出的个人知识存储概念，强调关联路径（associative trails）比文档本身更有价值，是 LLM Wiki 的思想先驱。"
created: 2026-04-13
updated: 2026-04-13
tags:
  - knowledge-management
  - history
  - information-science
  - hypertext
related_entities:
  - "[[Andrej-Karpathy]]"
  - "[[Knowledge-Work]]"
  - "[[RAG-vs-LLM-Wiki]]"
source_raw:
  - "[[20260413-llm-wiki]]"
---

# Memex

> **核心愿景**：个人知识存储，关联路径比文档更有价值

## 定义

**Memex**（Memory Extender）是 Vannevar Bush 在 1945 年文章《As We May Think》中提出的概念设备：

> "...a device in which an individual stores all his books, records, and communications, and which is mechanized so that it may be consulted with exceeding speed and flexibility."

## 核心特征

### 1. 个人知识存储

- 存储个人的所有书籍、记录、通信
- 机械化设备，可高速灵活查阅
- 个人拥有，个人管理

### 2. 关联路径（Associative Trails）

Memex 的核心创新：

> "The most essential feature of the Memex is not the storage itself, but the **associative trails** between documents."

- 用户可以创建文档间的"路径"
- 路径可以命名、保存、分享
- 路径本身是知识资产

### 3. 与 Web 的区别

| 维度 | Memex 愿景 | Web 现状 |
|-----|-----------|---------|
| 所有权 | 个人私有 | 公共/分散 |
| 链接类型 | 用户创建的路径 | 页面间超链接 |
| 链接价值 | 路径本身是资产 | 链接只是导航 |
| 维护责任 | 用户主动维护 | 被动发现 |
| 知识形态 | 主动 curated | 被动索引 |

## 历史背景

### 1945 年的思考

Vannevar Bush 当时是 MIT 副校长、科学研究与发展办公室主任。他思考：

- 科学家如何应对信息爆炸？
- 如何让知识工作者更高效？
- 如何保存和利用研究积累？

### 为什么没有实现？

Bush 无法解决的核心问题：

> **谁来做维护？**

- 创建关联路径需要大量劳动
- 维护路径需要持续投入
- 人类很快厌倦这种工作

## LLM Wiki 的关联

Andrej Karpathy 在 LLM Wiki 文章中明确关联 Memex：

> "The idea is related in spirit to Vannevar Bush's Memex (1945) — a personal, curated knowledge store with associative trails between documents. Bush's vision was closer to this than to what the web became: private, actively curated, with the connections between documents as valuable as the documents themselves. The part he couldn't solve was who does the maintenance. **The LLM handles that.**"

### Memex → LLM Wiki 的进化

| 挑战 | Memex (1945) | LLM Wiki (2026) |
|-----|--------------|-----------------|
| **谁创建路径？** | 人类 | LLM |
| **谁维护路径？** | 人类（很快厌倦） | LLM（不知疲倦） |
| **如何累积？** | 手动关联 | 自动编译 |
| **成本如何？** | 高，人类劳动 | 低，LLM 自动 |

## 现代实现

### Obsidian + LLM

当前最接近 Memex 愿景的组合：

- **Obsidian** = Memex 的存储设备
- **LLM Agent** = 路径创建和维护者
- **Wikilinks** = Associative trails

### 三层架构对应

| Memex 概念 | LLM Wiki 实现 |
|-----------|--------------|
| 存储设备 | Raw Sources |
| 关联路径 | Wiki 层的 Wikilinks |
| 索引机制 | index.md + log.md |
| 维护者 | LLM Agent |

## 相关概念演进

```
Memex (1945)
    ↓
Hypertext (1960s, Nelson)
    ↓
Web (1990s)
    ↓
Wiki (1995)
    ↓
Personal Knowledge Management (PKM, 2010s)
    ↓
LLM Wiki (2026)
```

## 原文引用

> [!quote] Vannevar Bush, 1945
> "He can add a marginal note... build a path... And when he ties two items together, he is not tying them as a librarian might... He is building a trail of interest."

---

## 外部链接

- [As We May Think 原文](https://www.theatlantic.com/magazine/archive/1945/07/as-we-may-think/303881/) (Atlantic Magazine, 1945)
- [Wikipedia: Memex](https://en.wikipedia.org/wiki/Memex)