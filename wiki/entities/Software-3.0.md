---
type: entity
title: Software 3.0
aliases:
  - Software 3.0
definition: "Andrej Karpathy 提出的编程范式第三阶段：上下文窗口是内存，提示词是程序语言，LLM 是解释器——编程从写代码变为设计给 agent 的指令文本"
created: 2026-05-08
updated: 2026-05-08
tags:
  - programming-paradigm
  - AI
  - LLM
related_entities:
  - "[[Software-2.0]]"
  - "[[Agentic-Engineering]]"
  - "[[Vibe-Coding]]"
  - "[[Agent-Native]]"
  - "[[Andrej-Karpathy]]"
source_raw:
  - "[[Andrej Karpathy: From Vibe Coding to Agentic Engineering]]"
---

# Software 3.0

> [!definition] 定义
> **Software 3.0** 是 Andrej Karpathy 在 Software 2.0（2017）的基础上提出的编程范式第三阶段。Software 1.0 = 人写代码规则；Software 2.0 = 人通过准备数据集和优化目标来训练神经网络；Software 3.0 = 人通过提示词和上下文窗口编程，LLM 成为新的"计算机"——上下文窗口是内存，提示词是程序语言，模型是解释器。

## 关键数据点

- **OpenClaw 安装案例**：传统方式需要应对多平台的复杂 shell 脚本（Software 1.0）；Software 3.0 方式是"复制粘贴一段文本给 agent"——agent 自带智能，能感知目标环境、调试循环，远比确定性脚本强大
- **MenuGen 案例**：Karpathy 用 Software 1.0+2.0 方式写了 OCR+图像生成的完整 app；但 Software 3.0 版本只用 Gemini + NanoBanana 一句话，LLM 直接在像素层渲染结果——"app 不应存在"
- **与 Software 2.0 的关系**：Software 2.0 是训练专用模型执行特定任务；Software 3.0 是用通用 LLM 通过提示词执行任意信息处理任务
- **CPU 角色翻转**：Karpathy 预测未来神经网络成为"主机进程"，CPU 退化为"协处理器"——翻转为当前虚拟化架构的镜像

## 前提与局限性

- Software 3.0 的"app 不应存在论"倾向激进——忽略了隐私、离线、定制化等真实需求
- LLM 作为解释器的可靠性远不如传统 CPU——输出不稳定、不可完全预测
- 当前仍处于过渡期——多数产品是 Software 1.0/2.0/3.0 的混合体
- 需要全新的工具链和最佳实践，整个行业仍在摸索

## 关联概念

- [[Software-2.0]] — 前序范式，从写代码到训练网络
- [[Agentic-Engineering]] — Software 3.0 时代的工程实践
- [[Vibe-Coding]] — Software 3.0 的普及化表达
- [[Agent-Native]] — Software 3.0 要求的基础设施范式
