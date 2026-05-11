---
type: entity
title: MachinaCheck
aliases:
  - MachinaCheck
definition: "基于多 Agent 流水线的 CNC 可制造性分析系统，通过 STEP 文件解析 + 选择性 LLM 推理，在 30 秒内完成原本 30-60 分钟的人工可制造性评估。"
created: 2026-05-11
updated: 2026-05-11
tags:
  - Multi-Agent
  - Manufacturing
  - Privacy-by-Design
  - AMD
related_entities:
  - "[[Hardware-Sovereignty]]"
  - "[[Agent-Orchestration]]"
  - "[[Agentic-Engineering]]"
  - "[[Dual-Tier-LLM-Architecture]]"
source_raw:
  - "[[MachinaCheck Building a Multi-Agent CNC Manufacturability System on AMD MI300X]]"
---

> [!definition] 定义
> MachinaCheck 是一个领域专用多 Agent 系统，解决 CNC 小型车间的可制造性分析痛点。用户上传 STEP 文件（标准 CAD 格式）并输入材料、公差、螺纹规格，30 秒内获得完整可制造性报告。核心架构决策：选择性 LLM 使用（仅在需要推理处用 Qwen 2.5 7B，数据库查询用纯 Python）+ 本地推理（AMD MI300X，数据不出域）。

## 五组件流水线架构

```
STEP 文件上传
    ↓
[Component 1] STEP 文件解析器（纯 Python / cadquery + OpenCASCADE）
    ↓ 几何特征（孔径/深度/平面/倒角/包围盒）
[Agent 1] 操作分类器（Qwen 2.5 7B / MI300X）
    ↓ 所需 CNC 操作和工具列表
[Agent 2] 工具匹配器（纯 Python / 数据库查询）
    ↓ 匹配结果（可用/缺失）
[Agent 3] 可行性决策 Agent（Qwen 2.5 7B / MI300X）
    ↓ 结构化决策（JSON）
[Agent 4] 报告生成器（Qwen 2.5 7B / MI300X）
    ↓
完整可制造性报告
```

## 关键数据点

- **人工耗时**: 30-60 分钟/图 × 10-20 RFQ/周 = 5-20 小时/周人工投入
- **MachinaCheck 耗时**: 30 秒端到端（全流水线 25-40 秒）
- **特征提取精度**: cadquery 直接读取数学几何，Ø6.0mm 孔就是 Ø6.0mm，无 OCR/视觉近似
- **特征提取速度**: < 1 秒（50 个特征以内的零件）
- **推理栈**: Qwen 2.5 7B → vLLM → ROCm → AMD MI300X（192GB HBM3）
- **GPU 利用率**: gpu-memory-utilization 0.5（约 96GB），留充足余量
- **推理延迟**: < 3 秒/Agent 调用
- **隐私**: 零字节 STEP 几何数据外传
- **测试结果**: 所有测试零件可制造性评估正确（未公布样本量和复杂度）

## 选择性 LLM 使用

这是 MachinaCheck 最值得学习的架构决策：

| 组件 | 是否用 LLM | 原因 |
|------|-----------|------|
| STEP 文件解析 | 否 | 数学几何提取，100% 确定性 |
| 操作分类 | 是 | 需要制造领域推理（材料→刀具映射） |
| 工具匹配 | 否 | 数据库查询，LLM 只会增加延迟和幻觉 |
| 可行性决策 | 是 | 需要综合推理（多因素权衡） |
| 报告生成 | 是 | 需要语言组织能力 |

**原则**: 数据库查询不需要 LLM，用 LLM 是浪费且危险的。只在需要推理的地方使用 LLM。

## 前提与局限性

- **前提**: 需要 AMD MI300X 级别硬件（192GB HBM3），成本较高
- **前提**: 需要 STEP 文件作为输入，不支持 PDF 图纸或手绘草图
- **前提**: 依赖 cadquery/OpenCASCADE 生态，安装配置门槛较高
- **局限性**: 当前仅支持 3 个输入维度（材料、公差、螺纹），未覆盖表面处理、热处理、装配约束
- **局限性**: 测试样本量和复杂度未公开，7B 模型对复杂 5 轴零件的推理能力未经验证
- **局限性**: 未与人工评估做量化对比（准确率、召回率）

## 关联概念

- [[Hardware-Sovereignty]] — MachinaCheck 是硬件主权在制造业的实例：MI300X 本地推理确保客户 IP 不出域
- [[Agent-Orchestration]] — 五组件流水线是领域专用的 Agent 编排模式
- [[Agentic-Engineering]] — "选择性 LLM 使用"直接体现 Agentic Engineering 的工程原则
- [[Dual-Tier-LLM-Architecture]] — LLM Agent + 纯 Python Agent 的分层架构与双层 LLM 架构理念一致

## 来源

- [[MachinaCheck Building a Multi-Agent CNC Manufacturability System on AMD MI300X]]
