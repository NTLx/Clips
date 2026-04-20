---
type: raw
source: "https://mp.weixin.qq.com/s/EsfS-zmfD17PT4DlD_wjBw"
author:
  - "AI大模型应用实践"
published: "2026-04-20"
created: "2026-04-20"
tags:
  - clippings
  - Ontology
  - AI-Agent
  - Enterprise-AI
---

# 实战案例｜当本体遇上 Agent：让 AI 真正"听懂业务"并"按规矩办事"【上】

本篇是"企业级本体应用"系列的第三篇文章。

回顾：
1. 从 0 到 1 带你理解 "本体论" 与 6 块核心"积木"
2. 手把手带你构建第一个业务本体（Ontology）

在前两篇文章中，我们介绍了本体的核心概念，并借助 Protégé 工具构建了一个制造业场景的简单业务本体。今天，我们将直面本体落地过程中的核心问题：本体这个"业务地图"究竟该如何无缝融入企业的智能体（Agent）系统中？

内容较多，我们将分两篇介绍不同的本体应用案例。

**一句话回顾：为什么 Agent 需要本体？**
本体为 AI Agent 提供了一幅"业务地图"。有了这幅地图的导航，Agent 才能在复杂的业务环境中看清方向，减少幻觉和错误。

---

## 01 误区：本体不是另一个数据库或图谱

很多人第一次接触"本体 + Agent"时，可能会有一个疑惑：
**是不是要把企业所有数据都装进本体里，让 Agent 直接查本体？**

这是一种完全错误的想法。

本体不是关系数据库或者知识图谱，不适合存储海量业务数据。本体的核心价值在于承载业务语义结构与规则（也就是 TBox），而不是当现实数据源使用（ABox）。这是"地图"和"仓库"的区别：

- **"地图"**：承载的是业务概念（客户、订单、库存等）、关系（谁依赖谁、谁属于谁、谁拥有谁）、规则（什么条件可以发货？什么客户是VIP？）、语义映射（客户在哪些系统里有对应）等等。
- **"仓库"**：承载的则是海量明细数据、事务更新、分析结果等。

本体的定位不是和数据源平行的一条路，它不存储数据，但它可以作为 Agent 与企业系统/数据源之间的语义层。

举一个例子：
Agent 如果发现需要做一个规则判断（比如：这个订单能否加急发货？），不应该"想当然"的推理，而可以让本体来告诉你是否符合规则。

理解本体的定位非常重要，这关联到你如何来应用本体。

---

## 02 本体放到 Agent 系统中，长什么样？

在 Agent 中引入本体，本质上并不会改变现有 Agent 系统构建的架构与方法，主要的变化无非是：
你需要在必要的时候借助本体这个统一的语义层，来帮助 LLM 完成它并不擅长的部分 — 理解业务语义、判断业务规则、推理业务结果。

那么如果把本体放到 Agent 系统中，其高层概念架构如下所示：

在这张图中，展示了一些本体在 Agent 系统中的价值和承担职责，比如：
- **规则引擎**：比如告诉 Agent 什么算符合"加急发货"的条件？
- **复杂关系推理**：典型的比如多跳关联 — 如集团股权穿透
- **充当映射层**：把业务语言翻译成数据库实现
- **统一业务视图**：比如将客户映射到不同系统中的数据实体
- **查询语义层**：告诉 Agent 复杂查询怎么查，哪些过滤条件和关系

这些用法我们将在下文进行案例实操演示。

### 构建基础的本体 Agent

为了让 Agent 能够借助本体，最简单的方式是给 Agent 增加本体工具（查询业务概念、推理业务规则、查找数据库映射等）。

用以下技术构建一个Demo：
- Agent 框架：LangChain
- 后端数据层：PostgreSQL
- 本体存储推理：owl文件 + owlready2 + HermiT 推理机
- LLM：OpenAI Like

```python
tools = [
        # 数据库直接查询
        query_customer, list_orders, query_order,
        # 本体规则推理（根据实际需要修改定制）
        check_shipment_eligibility, check_expedite_eligibility,
        # 本体规则查询等
        get_business_rules,
    ]

    system_prompt = (
        "你是一个本体增强的企业管理助手。你背后接入了基于 OWL 本体的业务推理引擎。"
        "## 工具选择原则\n"
        "- 日常查询（客户、订单列表）→ 直接用数据库查询工具"
        "- 规则判定（能否发货、能否加急等）→ 使用本体推理工具"
        "- 基于语义概念查询（VIP客户、待处理订单等）→ 使用语义概念查询"
        "## 回答原则"
        "- 推理结果要说明判定依据"
        "- 用简洁清晰的中文回答"
    )

    llm = ChatOpenAI(model="gpt-5-mini", temperature=0)
    return create_agent(llm, tools, system_prompt=system_prompt)
```

后续我们都会在这个 Agent 基础上做完善，增加新的工具，解决新的问题。

### 是否一定要用到推理机？

尽管推理机是本体的重要设施。但在使用本体的过程中，也并非每次都一定用到。具体来说，本体也有两种不同的使用方式。

| 场景 | 使用推理机（推理） | 不使用推理机（查阅） |
|------|-------------------|---------------------|
| 示例 | 比如做规则推理、多跳关系推理 | 比如查询"客户"关联的概念、对应的数据实体 |
| 调用 | 需要调用推理机 | 直接查询属性 |
| 性能 | 较慢 | 较快 |
| 实现 | 把实例数据注入，交给推理机计算 | 直接读取本体中的定义、属性、注解 |

所以，不经过推理机，不代表不经过本体。在企业系统中，可以灵活根据自身需要来使用本体。

---

## 03 案例一：用本体做基本业务规则判断

延续上一篇中的场景：
客户要求对一笔订单进行加急发货，如何判断加急规则？

在这个业务中有两条规则：
- **可发货条件**：订单已占用库存，且质检通过
- **可加急条件**：在可发货基础上，客户还是 VIP

这两条规则当然可以用 if/else 搞定。但问题在于，企业规则很少只有两条，也很少永远不变。比如明天可能变成"VIP 且订单金额超过10万才可以申请加急"，后天又限定了某些特殊品类不能加急......。很快就会发现：
规则一旦散落在各个工具函数里，代码会越改越碎，解释也越来越难。

而基于本体的 Agent 做法是：
1. 首先把"什么才算符合条件"用形式化方式声明出来（OWL）
2. Agent 按需调用本体里的这些规则做推理
3. Agent 根据推理反馈来决定下一步动作（如回复客户）

### 本体定义

使用 Protégé 本体定义工具进行定义，并导出成 OWL 文件用于推理（在真实应用中通常会使用图数据库）。

详请参考我们上一篇文章。

### 推理逻辑实现

Agent 基于本体推理的核心逻辑，可以概括成三步：
1. 从数据库取事实：订单、客户、库存、质检状态（ABox）
2. 把这些事实临时注入本体：相当于把"各种事实"摆上台面
3. 让推理机根据规则分类：这笔订单是否属于"可发货""可加急"这两个类型

核心的推理实现大致如下（把方法包装成 Tool 给 Agent）：

```python
class OntologyReasoner:
    """按需将单笔订单数据注入本体，推理后返回业务分类结果。"""

    def reason_order(self, customer_tier, customer_id, order_id, required_qty, allocations):
        onto = self._base_onto
        self._clear_abox() # 清空旧的临时实例数据

        # 1. 注入客户
        cust_cls = self._cls("VIPCustomer") if customer_tier == "VIP"else self._cls("Customer")
        cust_ind = cust_cls("customer_id")

        # 2. 注入库存与质检信息
        alloc_inds = []
        for a in allocations:
            alloc_ind = self._cls("InventoryAllocation")(a["id"])
            alloc_ind.qcPassed = [a["qc_passed"]]
            alloc_inds.append(alloc_ind)

        # 3. 注入订单并建立关系
        order_ind = self._cls("Order")(order_id)
        order_ind.hasCustomer = [cust_ind]
        order_ind.hasAllocation = alloc_inds

        # 4. 调用推理机
        with onto:
            sync_reasoner(infer_property_values=True)

        # 5. 读取推理结果
        return {
            "ready_to_ship": order_ind in self._cls("ReadyToShipOrder").instances(),
            "expedite_eligible": order_ind in self._cls("ExpediteEligibleOrder").instances(),
        }
```

这里推理机做了什么？它根据 TBox 中的等价类定义，自动判断：
- 这笔订单有库存占用 -> 质检通过了 -> 属于 ReadyToShipOrder
- 客户是 VIP -> 属于 ExpediteEligibleOrder

注意，这里的判断是本体中规则驱动的，而不是把数据让 LLM 来判定。

### Agent运行效果

当用户询问："ORD-2024-001 能否加急发货？"
Agent 的工作流程是：

Demo的运行效果如下：

这里可以看到本体带来的可解释性 — 每个结论都能追溯到具体规则，而不是 LLM 来自通用知识的模糊解释。每一个推理结果都是推理机根据本体TBox 规则自动分类，既不是 LLM 推理，也不是 if/else 编码判断。

---

## 04 案例二：基于属性组合的多维归类

假设这样一个场景：需要对产品做自动分拣归类/打标签 — 哪些是危险品、哪些是冷链产品、哪些是出口管控产品、哪些需要特殊处理等等。

要做到这样的精准分类当然不难。
但问题不在于分类本身，而在于很多时候会有维度交叉。 比如某个产品既是危险品又是冷链产品；某个产品既需要冷链又是管控物资等等，当分类维度变成5个10个，复杂度就会上升。

传统的做法是用简单的IF/ELSE，类似于：

```python
def classify_product(product):
    categories = []
    if product["is_hazardous"]:
        categories.append("危险品")
    if product["requires_cold_chain"]:
        categories.append("冷链")
    if product["is_export_controlled"]:
        categories.append("出口管控")
    if categories:
        categories.append("特殊处理")
    return categories
```

不过，当规则变复杂时，问题就来了：
- 产品属性从数据库来，分类规则写在代码里 — 两处维护
- 新增一个分类维度，就要改代码与回归测试
- 多个不同厂家的 Agent 可能会各自维护一套分类逻辑
- 想知道"系统里有哪些分类规则" — 只能翻代码，没有统一视图

而借助于本体的做法是：
1. 在本体声明分类业务规则，也就是"什么产品是危险品"等
2. 从数据库获取数据，注入本体做推理，得出产品类型
3. 一个产品可以同时属于多个类型 — 本体不要求类之间互斥，多重分类是默认行为，这和传统编程中"一个对象只属于一个类型"有区别。

### 本体定义

也就是Tbox的声明，用 Protégé 这样的工具定义后导出OWL，也可以直接用代码来定义（owlready2）：

```python
# 危险品：含危险成分 → 自动归类
class DangerousGoods(Product):
    equivalent_to = [Product & isHazardous.value(True)]

# 冷链产品：需要冷链运输 → 自动归类
class ColdChainProduct(Product):
    equivalent_to = [Product & requiresColdChain.value(True)]

# 出口管控产品：受出口管制 → 自动归类
class ExportControlledProduct(Product):
    equivalent_to = [Product & isExportControlled.value(True)]

# 特殊处理产品 = ①②③ 的并集
class SpecialHandlingProduct(Product):
    equivalent_to = [Product & (
        isHazardous.value(True)
        | requiresColdChain.value(True)
        | isExportControlled.value(True)
    )]
```

这里SpecialHandlingProduct 是三个类的并集，不是第四个独立维度。它的 equivalent_to（等价类定义） 引用了前三个类的条件，推理机自动处理这层聚合。

### 推理逻辑实现

主要的推理流程与上一节案例类似，即查询事实 --> 注入本体 --> 推理结果：

```python
def reason_product_classification(self, products):
    """把产品属性注入本体，推理机自动完成所有分类。"""
    onto = self._base_onto
    self._clear_abox()

    prod_cls = self._cls("Product")

    # 四个分类类别，全部在本体初始化时由 equivalent_to 声明
    category_classes = {
        "DangerousGoods": self._cls("DangerousGoods"),
        "ColdChainProduct": self._cls("ColdChainProduct"),
        "ExportControlledProduct": self._cls("ExportControlledProduct"),
        "SpecialHandlingProduct": self._cls("SpecialHandlingProduct"),
    }

    # 1. 将数据库中的产品属性注入本体（ABox）
    individuals = {}
    for p in products:
        ind = prod_cls(p["name"])
        individuals[p["name"]] = ind
        ind.isHazardous = [p.get("is_hazardous", False)]
        ind.requiresColdChain = [p.get("requires_cold_chain", False)]
        ind.isExportControlled = [p.get("is_export_controlled", False)]

    # 2. 推理机一次运行 —— 所有分类自动完成
    with onto:
        sync_reasoner(infer_property_values=True)

    # 3. 读取分类结果（不是 if/else，是检查推理机的归类结论）
    .......省略......
```

现在，比如我们要求 Agent "把所有产品做个分类，告诉我哪些是需要特殊处理的产品"，那么最终 Agent 的运行结果：

注意到某个产品可以同时被归为 DangerousGoods 和 ColdChainProduct 两个类别。传统做法需要显式处理这种交叉；但在本体中，多重分类是默认行为。而且实现非常优雅。

---

在以上的两个案例中，本质上展示的都是用本体来实现规则推理，从而让 Agent真正的调用业务规则，提高准确度与可解释性。

当然，这里只是非常基础的例子。而实际上，这样的能力可以驱动更多的业务场景，比如需求智能匹配与推荐、供应商智能匹配、仓储策略推荐等 — 所有有明确业务规则定义的地方。规则越复杂、变化越频繁，越适合本体。

最后总结关于规则的两个可能疑问。

### 两个问题

**这些规则用 if/else 也能写，为什么要用本体？**

区别在于：if/else 是硬编码在代码里的，改一条规则就要改代码、重新部署；而本体规则是声明式的，改模型文件即可，Agent 代码不用动。当企业有几十上百条业务规则时，这个差别会非常明显。

**之前也有一些独立的规则引擎产品，和本体有什么区别？**

传统的规则引擎产品通常是脚本定义的多条 IF/THEN 规则 — 更像把业务规则写成一条条可执行脚本：条件命中，就触发，直观高效。但当规则一多，不同规则之间容易重复定义，概念口径不一致，跨规则复用困难，改一处条件往往要连带排查多条规则。

而本体承载规则时，并不是堆很多规则定义脚本，而是先把"什么是可加急订单"这类概念定义清楚，再由推理机去判断某个对象是否属于这个概念。其好处是：多个判断共享同一套概念和关系；业务口径更统一，规则变更也更容易收敛到业务模型层，而不是散落在大量IF/THEN规则条目里。

---

我们将在下一篇继续探讨其他的一些本体+Agent的应用场景。

---

## 编译摘要

### 1. 浓缩
- **核心结论1**: 本体不是数据库，应作为 Agent 与企业系统之间的语义层，而非数据源
  - 关键证据: 本体承载"地图"（语义与规则），数据库承载"仓库"（海量数据）
- **核心结论2**: 本体 Agent 工具选择原则：日常查询用数据库，规则判定用本体推理
  - 关键证据: OntologyReasoner 注入事实 → 推理机分类 → 读取结论，而非 LLM 判断
- **核心结论3**: 本体规则声明式定义，改模型文件即可，Agent 代码不动 — 优于传统规则引擎
  - 关键证据: IF/THEN 规则引擎问题：概念口径不一致、跨规则复用困难；本体先定义概念再判断

### 2. 质疑
- **关于"本体定位"的质疑**: 本体作为语义层需要企业有统一的业务概念，但很多企业概念本身就是混乱的
- **关于"推理性能"的质疑**: 注入数据 + 运行推理机 相比 直接查询较慢，高频实时场景是否适用？
- **关于"规则声明式"的质疑**: OWL 等价类表达有限，复杂规则（如时间窗口、跨系统条件）可能需要 SWRL 或代码

### 3. 对标
- **跨域关联1**: 本体推理类似"编译器类型检查" — 声明式约束，自动验证，无需手动判断
- **跨域关联2**: Ontology Agent 类似"规则驱动的微服务" — 业务逻辑集中在语义层，Agent 调用而非实现

### 关联概念
- [[Ontology]]
- [[Ontology-Agent]]
- [[TBox]]
- [[ABox]]
- [[OWL]]
- [[HermiT]]
- [[Owlready2]]
- [[Enterprise-Ontology-Application]]