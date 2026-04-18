---
type: entity
title: Software 2.0
aliases:
  - Software 2.0
definition: "Andrej Karpathy 提出的概念，指明软件开发范式的转变：从程序员编写代码（Software 1.0）转向程序员编写目标、神经网络通过数据编程（Software 2.0）。"
created: 2026-04-13
updated: 2026-04-15
tags:
  - AI-Agent
  - neural-networks
  - programming-paradigm
  - deep-learning
related_entities:
  - "[[Andrej-Karpathy]]"
  - "[[Vibe-Coding]]"
  - "[[Agentic-Engineering]]"
  - "[[Coding-Agents]]"
  - "[[AI-Capability-Gap]]"
  - "[[AI-Psychosis]]"
source_raw:
  - "[[20260413-llm-wiki]]"
  - "[[20260409-ai-capability-gap-ai-psychosis]]"
---

# Software 2.0

> **核心洞察**：程序员不再写代码，而是写目标

## 定义

**Software 2.0** 是 Andrej Karpathy 提出的软件开发范式转变概念：

| 范式 | 程序员的工作 | 程序的来源 |
|-----|-------------|-----------|
| **Software 1.0** | 编写明确的代码逻辑 | 人类编写的源代码 |
| **Software 2.0** | 编写目标和约束 | 神经网络通过数据学习生成 |

## 核心差异

### Software 1.0（传统编程）

```
程序员 → 写代码 → 编译/运行 → 输出结果
```

特征：
- 明确的逻辑流程
- 可读的源代码
- 可调试的步骤
- 确定性输出

### Software 2.0（神经网络编程）

```
程序员 → 定义目标 + 提供数据 → 神经网络训练 → 输出结果
```

特征：
- 目标驱动而非逻辑驱动
- 数据是"源代码"
- 神经网络权重是"程序"
- 概率性输出

## 技术栈对比

| Software 1.0 | Software 2.0 |
|--------------|--------------|
| C++, Python, Java | PyTorch, TensorFlow |
| 编译器 | 优化器 (SGD, Adam) |
| 源代码文件 | 数据集 |
| 调试器 | 可视化工具 |
| Git 版本控制 | 模型 checkpoint |
| 代码审查 | 数据清洗 |
| 单元测试 | 验证集评估 |

## 为什么是"编程"？

Karpathy 认为神经网络训练本质上是编程：

1. **数据 = 源代码** — 数据定义了程序的行为
2. **权重 = 程序** — 训练后的神经网络是可执行的"程序"
3. **目标函数 = 规格说明** — Loss function 定义了期望行为
4. **优化 = 编译** — 训练过程将"源代码"编译为"程序"

## 适用领域

### Software 2.0 更适合

- 视觉识别（图像分类、目标检测）
- 语音处理（语音识别、语音合成）
- 自然语言处理（翻译、对话）
- 推荐系统
- 游戏策略（AlphaGo）
- 自动驾驶

### Software 1.0 仍有优势

- 确定性计算（银行系统）
- 明确逻辑需求（编译器）
- 安全敏感场景（加密算法）
- 资源受限环境（嵌入式）

## 混合架构

实践中常见混合模式：

```
Software 1.0（框架层）
    ↓
Software 2.0（核心能力层）
    ↓
Software 1.0（接口层）
```

示例：
- **自动驾驶**：感知层用 Software 2.0，控制层用 Software 1.0
- **搜索引擎**：排序用 Software 2.0，索引用 Software 1.0
- **推荐系统**：模型用 Software 2.0，展示用 Software 1.0

## 与相关概念的关系

| 概念 | 关系 |
|-----|------|
| **[[Vibe-Coding]]** | Software 2.0 的实践方式之一，但更极端 |
| **[[Agentic-Engineering]]** | 在 Software 2.0 时代的人类角色转变 |
| **[[Coding-Agents]]** | Software 2.0 的自动化工具 |

## 历史意义

Software 2.0 标志着：

1. **编程范式转变** — 从逻辑驱动转向目标驱动
2. **程序员角色转变** — 从写逻辑转向写目标和数据
3. **代码概念扩展** — "源代码"不再只是文本文件

> [!quote] Karpathy 原文
> "The 'program' is the weights of the neural network... the 'compiler' is the optimizer... the 'source code' is the dataset."

---

## 关键数据点

- Karpathy 认为：数据 = 源代码，权重 = 程序，目标函数 = 规格说明，优化 = 编译
- Software 2.0 更适合的领域：视觉识别、语音处理、NLP、推荐系统、游戏策略、自动驾驶
- Software 1.0 仍有优势的领域：确定性计算（银行系统）、明确逻辑需求（编译器）、安全敏感场景（加密算法）、资源受限环境（嵌入式）
- 实践中常见混合架构：1.0（框架层）→ 2.0（核心能力层）→ 1.0（接口层）

## 前提与局限性

- **前提**: 神经网络训练可以类比为"编程"，这个类比取决于对"程序"的广义定义
- **边界条件**: 在安全敏感和确定性要求极高的场景，Software 1.0 不可替代
- **局限性**: Karpathy 的原始论述（2017）主要针对深度学习，LLM Agent 时代的"Software 2.0"含义已扩展
- **局限性**: "数据 = 源代码"的类比忽略了数据清洗、标注等人工劳动的成本
- **局限性**: 该概念提出时（2017）尚未有 LLM Agent 编程范式，当前需要重新审视其适用范围

## 关联概念

- [[Andrej-Karpathy]] - Software 2.0 的提出者
- [[Vibe-Coding]] - Software 2.0 的实践方式之一，但更极端
- [[Agentic-Engineering]] - 在 Software 2.0 时代的人类角色转变
- [[Coding-Agents]] - Software 2.0 的自动化工具

## 外部链接

- [Software 2.0 博客原文](https://karpathy.medium.com/software-2-0-a6c4ba5203d4) (Medium)
- [Andrej Karpathy](https://karpathy.ai/)