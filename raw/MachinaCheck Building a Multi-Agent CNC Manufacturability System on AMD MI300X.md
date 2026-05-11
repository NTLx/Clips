---
title: "MachinaCheck: Building a Multi-Agent CNC Manufacturability System on AMD MI300X"
source: "https://huggingface.co/blog/lablab-ai-amd-developer-hackathon/machinacheck"
author:
  - "[[Syed Muhammad Sarmad]]"
published: 2026-05-11
created: 2026-05-11
description: "A Blog post by Lablab.ai AMD Developer Hackathon on Hugging Face"
tags:
  - "clippings"
---
*Built at the AMD Developer Hackathon on lablab.ai — May 2026*

---

## The Problem We Solved

Walk into any small CNC machine shop and ask the manager how they decide whether to accept a customer job.

The answer is almost always the same: they print the drawing, read every dimension by hand, walk around the shop checking which tools are available, estimate whether their machines can hold the required tolerances, and write notes on a clipboard. The whole process takes 30 to 60 minutes per drawing. For a busy shop receiving 10 to 20 RFQs per week, that is 5 to 20 hours of skilled manager time spent on feasibility analysis alone.

Sometimes they get it wrong. They accept a job, start production, and discover halfway through that they don't have the right tap or that their mill cannot hold the tolerance on a critical feature. The part gets scrapped. The customer is unhappy. The machine time is lost.

We built MachinaCheck to eliminate this problem entirely.

---

## What MachinaCheck Does

MachinaCheck is a multi-agent AI system. You upload a STEP file — the standard CAD format that customers send to machine shops — along with three simple inputs: material type, required tolerance, and any thread specifications. Thirty seconds later you have a complete manufacturability report telling you exactly whether you can make the part, what tools you need, what is missing, and what actions to take before starting production.

No manual drawing reading. No walking around the shop. No guesswork.

---

## Why We Built It on AMD MI300X

Before explaining the architecture, this point deserves its own section because it is not just a technical choice — it is a business requirement.

Manufacturing customers sign NDAs. Their STEP files contain proprietary geometry representing years of engineering work and millions of dollars in R&D. The hole pattern on a medical device or the pocket geometry on an aerospace component is confidential intellectual property.

Sending that data to OpenAI, Anthropic, or any commercial API endpoint is a confidentiality violation. Full stop.

The AMD Instinct MI300X changes this equation completely. With 192GB of HBM3 VRAM and 5.3 TB/s of memory bandwidth, we run Qwen 2.5 7B Instruct entirely on-premise. No data leaves the shop's infrastructure. No STEP geometry is transmitted to a third-party server. The customer's IP stays where it belongs.

This is what "privacy by design" actually means in a manufacturing context — not a checkbox, but a fundamental architectural decision that makes the product viable for real enterprise customers.

---

## The Agent Architecture

MachinaCheck uses a five-component pipeline built with LangChain and orchestrated via FastAPI.

### Component 1 — STEP File Parser (Pure Python, No LLM)

We use cadquery, a Python library built on OpenCASCADE, to parse STEP files directly. This gives us mathematically exact feature extraction:

- All cylindrical holes with diameter and depth
- Flat surfaces and their areas
- Chamfers and fillets
- Bounding box dimensions
- Total volume and surface area

This extraction is 100% accurate because it reads the mathematical geometry directly — no vision model, no OCR, no approximation. A Ø6.0mm hole is exactly Ø6.0mm in the output.

```python
def extract_features(step_file_path: str) -> dict:
    model = cq.importers.importStep(step_file_path)
    shape = model.val()
    bb = shape.BoundingBox()
    
    holes = {}
    for face in model.faces().vals():
        adaptor = BRepAdaptor_Surface(face.wrapped)
        if adaptor.GetType() == GeomAbs_Cylinder:
            radius = adaptor.Cylinder().Radius()
            diameter = round(radius * 2, 3)
            holes[diameter] = holes.get(diameter, 0) + 1
    
    return {
        "bounding_box_mm": {"length": round(bb.xlen, 3), ...},
        "holes": [...],
        "flat_surfaces_count": len(flat_surfaces),
    }
```

### Agent 1 — Operations Classifier (Qwen 2.5 7B)

The extracted geometry plus user inputs — material, tolerance, threads — are passed to Qwen 2.5 7B running on AMD MI300X via vLLM.

The agent answers: *"What CNC operations and tools are required to manufacture this part?"*

It applies manufacturing domain knowledge: Steel 304 needs carbide tooling. A cylindrical hole needs a drill, not an end mill. A tolerance of ±0.005mm requires a precision machine, not a standard mill.

### Agent 2 — Tool Matcher (Pure Python)

This agent does not use an LLM. It queries the shop's tool inventory database and checks each required tool against what is available. Pure deterministic logic — database lookup, comparison, result. LLMs are not needed for database queries and using them here would add unnecessary latency and hallucination risk.

### Agent 3 — Feasibility Decision Agent (Qwen 2.5 7B)

The match results go back to Qwen. The agent reasons about the overall situation and produces a structured decision:

```json
{
  "decision": "CONDITIONAL",
  "confidence": "HIGH",
  "reason": "All tools available except M10x1.5 tap",
  "action_items": ["Purchase M10x1.5 tap ($15)"],
  "risk_flags": ["Verify spindle speed for Steel 304"],
  "estimated_setup_hours": 2.5
}
```

### Agent 4 — Report Generator (Qwen 2.5 7B)

The final agent synthesizes everything into a professional manufacturability report with an overall status, executive summary, part analysis, tools status, machine status, and final recommendation.

---

## The AMD Stack

Running Qwen 2.5 7B on AMD MI300X via ROCm and vLLM was straightforward. The vLLM Quick Start image on AMD Developer Cloud has everything pre-configured.

```bash
python -m vllm.entrypoints.openai.api_server \
  --model Qwen/Qwen2.5-7B-Instruct \
  --host 0.0.0.0 \
  --port 8000 \
  --dtype float16 \
  --gpu-memory-utilization 0.5
```

With `gpu-memory-utilization 0.5` we use approximately 96GB of the available 192GB, leaving plenty of headroom. Inference latency for our agent calls averages under 3 seconds.

LangChain connects to vLLM via the OpenAI-compatible endpoint:

```python
from langchain_community.llms import VLLMOpenAI

llm = VLLMOpenAI(
    openai_api_base="http://localhost:8000/v1",
    openai_api_key="EMPTY",
    model_name="Qwen/Qwen2.5-7B-Instruct",
    temperature=0.1,
    max_tokens=1000
)
```

---

## Results

Testing with real STEP files from GrabCAD:

- Feature extraction: under 1 second for parts with up to 50 features
- Full pipeline (all 4 agents): 25 to 40 seconds end-to-end
- Decision accuracy: correct manufacturability assessment on all test parts
- Privacy: zero bytes of STEP geometry transmitted externally

---

## What We Learned

**Use LLMs only where reasoning is needed.** Agent 2 (tool matching) is pure Python. Putting an LLM there would be slower, more expensive, and less reliable. The right tool for database lookup is a database query.

**Prompt engineering for structured output matters.** Getting Qwen to reliably output valid JSON required careful rules in the prompt — explicitly stating that cylindrical holes need drills not end mills, that diameters must match exactly, that taps only appear when threads are specified.

**AMD MI300X is genuinely impressive for this use case.** The 192GB VRAM means we could run a much larger model if needed. For a production deployment, Qwen 2.5 72B would fit comfortably and deliver significantly better reasoning quality.

---

## Try It

- **HF Space:** [huggingface.co/spaces/lablab-ai-amd-developer-hackathon/MachinaCheck](https://huggingface.co/spaces/lablab-ai-amd-developer-hackathon/MachinaCheck)
- **GitHub:** [github.com/SyedMuhammadSarmad/Manufacturing-Agent](https://github.com/SyedMuhammadSarmad/Manufacturing-Agent)

Upload any STEP file and see the full pipeline in action.

---

*Built by Syed Muhammad Sarmad and Sabari Doss R at the AMD Developer Hackathon, May 2026.*

*Stack: Qwen 2.5 7B · AMD Instinct MI300X · ROCm · vLLM · LangChain · cadquery · FastAPI · Next.js · Hugging Face Spaces*

---

## 编译摘要

### 1. 浓缩
- **核心结论1**: CNC 小型车间可制造性分析完全依赖人工（30-60 分钟/图），MachinaCheck 用 5 组件多 Agent 流水线在 30 秒内完成，消除人工判断误差
  - 关键证据: 10-20 RFQ/周 × 30-60 分钟 = 5-20 小时/周人工投入；STEP 文件通过 cadquery（OpenCASCADE）精确解析几何特征，100% 数学精度
- **核心结论2**: 制造业客户 NDA 要求 STEP 文件（专有几何 IP）不能离开本地——AMD MI300X（192GB HBM3）使本地运行 Qwen 2.5 7B 成为隐私合规的必要条件
  - 关键证据: 零字节 STEP 几何数据外传；gpu-memory-utilization 0.5 仅用 96GB，留充足余量；推理延迟 < 3 秒
- **核心结论3**: "选择性 LLM 使用"是关键架构决策——只在需要推理的地方用 LLM（操作分类/可行性决策/报告生成），数据库查询用纯 Python（工具匹配），避免不必要的延迟和幻觉风险
  - 关键证据: Agent 2（工具匹配）是纯 Python 数据库查询，不用 LLM；全流水线 25-40 秒端到端

### 2. 质疑
- **关于"正确性"的质疑**: 文章称"correct manufacturability assessment on all test parts"，但未给出测试零件数量、复杂度分布、与人工评估的对比。7B 模型对复杂 5 轴加工零件、非常规材料的推理能力存疑
- **关于可扩展性的质疑**: 当前仅支持 3 个输入（材料、公差、螺纹规格），真实车间场景还包括表面处理、热处理、装配约束等，Qwen 2.5 7B 的领域知识深度是否足够？
- **关于成本的质疑**: MI300X 硬件成本未提及，对小型车间而言本地部署的 ROI 需要量化——对比云 API 的成本节省 vs 硬件投入

### 3. 对标
- **跨域关联1**: 与 [[OncoAgent A Dual-Tier Multi-Agent Framework for Privacy-Preserving Oncology Clinical Decision Support]] 高度相似——两者都是"多 Agent + 本地推理 + 隐私合规"架构，只是领域不同（医疗 vs 制造）
- **跨域关联2**: "选择性 LLM 使用"模式与 [[Agentic-Engineering]] 中"LLM 只在需要推理处使用"的工程原则一致——Agent 2 纯 Python 是对这一原则的直接实践
- **跨域关联3**: 硬件选择逻辑与 [[Hardware-Sovereignty]] 概念直接对应——MI300X 的 192GB HBM3 使隐私合规的本地推理成为可能

### 关联概念
- [[Hardware-Sovereignty]]
- [[Agent-Orchestration]]
- [[Agentic-Engineering]]
- [[Dual-Tier-LLM-Architecture]]
