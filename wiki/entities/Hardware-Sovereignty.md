---
type: entity
title: Hardware Sovereignty
aliases:
  - 硬件主权
definition: "AI 系统在本地硬件上完成全部训练、推理和数据处理，不依赖任何云 API 或外部服务，确保数据完全不出域，满足隐私法规要求。"
created: 2026-05-10
updated: 2026-05-11
tags:
  - AI-Infrastructure
  - Privacy
  - Enterprise-AI
related_entities:
  - "[[Zero-PHI-Policy]]"
  - "[[Agent-First-Enterprise]]"
source_raw:
  - "[[OncoAgent A Dual-Tier Multi-Agent Framework for Privacy-Preserving Oncology Clinical Decision Support]]"
  - "[[MachinaCheck Building a Multi-Agent CNC Manufacturability System on AMD MI300X]]"
---

> [!definition] 定义
> 硬件主权是指 AI 系统的完整技术栈（训练、推理、RAG、UI）在本地硬件上运行，不依赖任何云 API 或外部服务。这不仅是工程便利，更是在 HIPAA/GDPR 等隐私法规框架下的法律和伦理要求——数据必须留在受控基础设施内。

## 关键数据点

- **OncoAgent 实例**: 完整栈（训练+推理+RAG+UI）运行在单块 AMD Instinct MI300X（192 GB HBM3）
- **训练栈**: Unsloth + QLoRA + ROCm，无需 CUDA
- **推理栈**: 本地 BF16 推理 + Featherless.ai API 优雅降级
- **向量存储**: ChromaDB 本地持久化索引，零云端
- **合规**: 满足 HIPAA（US）、GDPR（EU）及同等国家标准
- **ROI**: 56 倍合成数据生成加速 + 6 倍训练时间压缩，单卡即可完成

## 前提与局限性

- **前提**: 需要高端本地硬件（如 MI300X 的 192 GB HBM3），成本较高
- **前提**: 需要开源模型和框架支持（如 Qwen、Unsloth、ChromaDB）
- **局限性**: 高端硬件获取门槛高，多数中小机构难以部署
- **局限性**: 缺乏云服务的弹性扩展能力，高峰期可能需要排队

## 关联概念

- [[Zero-PHI-Policy]] — 硬件主权为 Zero-PHI 策略提供基础设施保障
- [[Agent-First-Enterprise]] — 硬件主权是企业 Agent 化转型的基础设施前提
