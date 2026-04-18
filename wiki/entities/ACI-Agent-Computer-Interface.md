---
type: entity
title: ACI (Agent-Computer Interface)
aliases:
  - ACI Agent Computer Interface
definition: "Agent 与计算机交互的接口设计，类比 HCI 但针对 AI Agent 优化"
created: 2026-04-10
updated: 2026-04-15
tags:
  - AI-Agent
  - tool-design
  - best-practices
related_entities:
  - "[[Coding-Agents]]"
  - "[[Agentic-Engineering]]"
source_raw:
  - "[[building-effective-agents]]"
---

# ACI (Agent-Computer Interface)

> **核心类比**：ACI = Agent-Computer Interface，正如 HCI = Human-Computer Interface

## 定义

**ACI (Agent-Computer Interface)** 是 Anthropic 在"Building Effective AI Agents"中提出的概念：

> 思考人机交互 (HCI) 投入了多少努力，就应该在 Agent-计算机接口 (ACI) 上投入同等努力。

## 设计原则

### 1. 给 Agent 足够 Token 思考

> 不要让 Agent 在写代码时把自己逼入死角。

### 2. 保持格式自然

> 格式应接近模型在网上自然见过的文本。

### 3. 避免格式开销

> 不要让 Agent 计算数千行代码的行数，或转义引号。

## 工具格式选择建议

| 格式 | 适用性 | Agent 难度 |
|------|--------|-----------|
| **Markdown 代码块** | 高 | 低（自然格式） |
| **JSON 内嵌代码** | 低 | 高（需转义） |
| **Diff 格式** | 低 | 高（需计算行号） |
| **重写整个文件** | 高 | 低（无格式开销） |

## ACI 设计检查清单

1. **模型视角测试**
   - 根据描述和参数，使用方式是否明显？
   - 需要深思熟虑吗？（如果需要，对 Agent 也难）

2. **命名清晰性**
   - 参数名/描述是否让事情更明显？
   - 想象为初级开发者写文档字符串

3. **测试迭代**
   - 在 workbench 运行多组示例输入
   - 观察模型犯什么错误并迭代

4. **Poka-yoke（防错设计）**
   - 改变参数让错误更难发生
   - 例如：始终使用绝对路径而非相对路径

## 案例研究：SWE-bench Agent

> [!tip] 实践经验
> Anthropic 团队在构建 SWE-bench Agent 时，**工具优化时间超过整体 prompt 优化**。
> 
> 发现问题：Agent 移出根目录后，相对路径工具出错。
> 解决方案：工具改为始终要求绝对路径 → Agent 完美使用。

## 与 HCI 的对比

| 维度 | HCI | ACI |
|------|-----|-----|
| 用户 | 人类 | AI Agent |
| 设计目标 | 直观、易学 | 明确、无歧义 |
| 反馈机制 | 视觉/触觉 | 文本/工具结果 |
| 错误处理 | 容错、引导 | 防错、清晰报错 |

## 关键数据点

- Anthropic 在构建 SWE-bench Agent 时，**工具优化时间超过整体 prompt 优化时间**
- 问题案例：Agent 移出根目录后，相对路径工具出错；改为绝对路径后 Agent 完美使用
- Markdown 代码块格式适用性高、Agent 难度低（自然格式）；JSON 内嵌代码和 Diff 格式适用性低、难度高

## 前提与局限性

- ACI 设计原则假定 Agent 是 LLM 驱动，对非 LLM Agent 可能不适用
- "给 Agent 足够 Token 思考" 的前提是上下文窗口足够大，成本可接受
- 工具格式选择需权衡：自然格式（如 Markdown）对 Agent 友好但可能增加 token 消耗
- SWE-bench 的优化经验不一定直接迁移到非代码场景

## 关联概念

- [[Coding-Agents]] - ACI 的主要使用者
- [[Agent-Workflow-Patterns]] - 使用 ACI 的模式
- [[Agentic-Engineering]] - ACI 设计的上下文

---

> **来源**：Anthropic, "Building Effective AI Agents", 2024-12-19