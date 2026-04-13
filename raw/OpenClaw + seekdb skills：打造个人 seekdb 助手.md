---
title: "OpenClaw + seekdb skills：打造个人 seekdb 助手"
source: "https://mp.weixin.qq.com/s/HapC7qx3x57kXLEpJTVbEA"
author:
  - "[[从筠]]"
published:
created: 2026-03-06
description: "这篇文章由从筠大佬为大家介绍如何在 OpenClaw 中加载 seekdb Agent Skill，让它能够随时基于 seekdb 官方文档回答开发者有关 seekdb 部署、向量搜索、混合搜索、集成方式等常见问题。"
tags:
  - "clippings"
---
原创 从筠 *2026年3月4日 11:54*

这篇文章由从筠大佬为大家介绍如何在 **OpenClaw** 中加载 **seekdb Agent Skills** ，让它能够随时基于 seekdb 官方文档回答开发者有关 seekdb 部署、向量搜索、混合搜索、集成方式等常见问题。

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/Z9yXJ1qu4piaCiat5CWuHVLytbAVRQZyPYV1zBmmob3vFSR5nMSB7srdRWKzUpN8bqF5UYc4e03EVMFPyk917JHY2pehAn694sqhAI7tPCTTY/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

欢迎大家关注 OceanBase 社区公众号 “老纪的技术唠嗑局”，在这里，我们会持续为大家更新与 [#数据库](https://mp.weixin.qq.com/s/) 、 [#AI](https://mp.weixin.qq.com/s/) 相关的技术内容！

## 什么是 OpenClaw ？

> OpenClaw 实在太火了，其实可以不介绍。但为了保证内容的完整性，还是象征性地介绍下~

**OpenClaw** 是一款运行在你自己设备上的 **个人 AI 助手** 。它在你已有的沟通渠道上与你对话（如 WhatsApp、Telegram、Slack、Discord、Signal、iMessage、WebChat 等），也支持通过本地 TUI 或 Web 界面直接聊天。

![Clawdbot → Moltbot → OpenClaw. The Fastest Triple Rebrand in ...](https://mmbiz.qpic.cn/sz_mmbiz_png/Z9yXJ1qu4pjM1Q5j58nErll4AibJqIicpOIibfPg9ibtbaXcCxfCFdEichzLpk8deU4yZa8NSpW1HQL3pXbFox70oL67aHZulcjJYpSgz7SI8nRA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

Clawdbot → Moltbot → OpenClaw. The Fastest Triple Rebrand in...

特点概览：

- **本地优先** ：数据与对话由你掌控，可完全在本地或自建环境中运行。
- **多渠道** ：同一助手可接入多种即时通讯与开发工具。
- **可扩展** ：通过 **Skill（技能）** 为助手注入领域知识或工具能力。

## 什么是 seekdb ？

> seekdb 是 OceanBase 推出的 AI 原生数据库，可以运行在各种设备上。
> 
> 它将关系型数据、向量、全文、JSON、GIS 等多种数据类型统一在单一引擎中，支持通过一条 SQL 完成向量搜索 + 全文搜索 + 关系查询的混合操作。

![图片](https://mmbiz.qpic.cn/mmbiz_png/Z9yXJ1qu4piaS6gzrCqtwIuKzicQmXErHvPPf9ib0jFGO1pW6KR1VhyUib2hutyP8Sp4DaGNZGCZq0kWcIYmnGceA0y9s03KCQUj3SvK2cEDUY0/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

特点概览：

- AI 原生：内置 embedding 生成、重排序、LLM 推理能力，数据库内完成 RAG 工作流。
- 混合搜索：向量搜索 + 全文搜索 + 关系查询，一条 SQL 搞定所有。
- 轻量易部署：最低 1 核 CPU + 2GB 内存即可运行，支持嵌入式、Docker、RPM 多种部署方式。
- MySQL 兼容：兼容 MySQL 语法与生态，支持完整 ACID 事务，学习成本低。
- 开源免费：Apache 2.0 许可，代码开源在 GitHub。

## 什么是 seekdb Agent Skill

**seekdb Agent Skill** 是一组与 **seekdb** 向量数据库相关的 Agent 技能，用于增强 AI 助手在 seekdb 场景下的能力。本 Skill 包由 seekdb 生态插件 提供，支持多种 AI 工具（如 OpenClaw、Claude Code、Cursor、Codex 等）。

当前主要包含三类技能：

1. **seekdb-docs（文档技能）**
- 内置 seekdb 官方文档知识库，支持基于内容的语义检索。
	- 涵盖快速入门、开发指南（向量搜索、混合搜索、AI 函数等）、SDK/API 参考、多模型数据、集成与部署运维、实践教程等。
	- 助手在回答「如何部署 seekdb」「如何使用向量搜索」等问题时，会优先查阅远程文档，失败时回退到本地文档。
3. **importing-to-seekdb（导入技能）**
- 将 CSV/Excel 导入 seekdb，支持可选列向量化（如 all-MiniLM-L6-v2），便于后续语义搜索。
	- 支持预览、批量导入与集合管理。
5. **querying-from-seekdb（查询技能）**
- 对 seekdb 进行标量/混合搜索，支持元数据过滤与 RRF 排序，并可导出为 CSV/Excel。

本文以 **OpenClaw + seekdb 文档技能** 为例，介绍如何安装、加载技能并通过自然语言向助手提问（如「how to deploy seekdb」等），助手会基于该 Skill 检索文档并给出解答。

---

## 安装 OpenClaw

> 小编的 OpenClaw 是让 Qwen Code 直接替我安装的。
> 
> Qwen Code 是 Claude Code 的平替产品 ，默认的 Qwen3-Coder 模型免费额度是每日 2000 次请求，正常使用场景都够用，顺带在这里一起推荐给大家。

环境要求： **Node.js ≥ 22** 。

1. 一键安装脚本
```
curl -fsSL https://openclaw.ai/install.sh | bash
```
1. 先选择 QuickStart，后面有需要可以再手动配置
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Z9yXJ1qu4ph98lB8diaHHpgv4ph0VXaq7SpwaYIBA8DoI6eDqibAhmM8r9M2TwHC5EhkeLqiaQSW4PCy7owslcaNLunFAlyoZhA4qgcyY7icp9U/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

1. 选择一个 provider，在下一步输入 API Key，并选择一个模型
![图片](https://mmbiz.qpic.cn/mmbiz_png/Z9yXJ1qu4pj6XtiaQjEXHPoyAKvDV6WPdliayGPkvBHCXRDoUicsBCuHxpic8jktW7Jib04oe9AxD0r6nJ9FxV30OicxXE85iabwChZLKK6HElR4ro/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

1. 目前用不到，可以先跳过
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Z9yXJ1qu4pia2JHQic1ZgL4vQqmUxVicfUTU6tOsMh47VeWWng5JZQ9MvTpx4urmTw7Bv6HW42ktg53X6fZfqu61BP1QxEeWhNZYP6mjPZGlvs/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

1. 选择不配置 skill，后面再配置。这里显示的几个配置信息很重要:
- openclaw.json：OpenClaw 的配置文件，所有的配置都写入了这个文件，可以手动编辑这个 JSON 文件来修改配置
- Workspace 路径：~/.openclaw/workspace，OpenClaw 的默认操作目录，后面的 skill 也要放到这个文件夹下
- sessions：是与会话持久化有关的目录，OpenClaw 的会话在关闭终端时不会结束，当你再次打开终端时会继续上次的会话，除非输入「/new」，才会开启一个新会话
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Z9yXJ1qu4pgd5DibROJcLPSnNdTia5cJbdAAW0HKLcFjgwlnQrsvwtPEJibxiadibqESTg4sRh2WxmHJZ898TDAtl7zNzwXYWvHZdpO3RslfFZ2E/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

1. Hooks 是 OpenClaw 在执行特定操作（如启动、开启新会话）时运行的指令，可以在每个上面敲击空格多选，进行开启
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Z9yXJ1qu4pia0qTSzFkkvfapDxylicbcbWjKMDbt5siclzWVsk3Mb8PkU4BZZz0XtibJMJqo4dRDe8BLBM6L82Sm97KKDf3x6zGbnyt8BBagibFk/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

1. 这里选择使用 TUI，也可以使用 http://127.0.0.1:18789?token=... 打开 Web UI
![图片](https://mmbiz.qpic.cn/mmbiz_png/Z9yXJ1qu4piaEjzGwn3ia7icKibWHMKtj9ibAwksyb2NgcM5wiaFRMex0PsuxodicuicgaX6ZXB5U7x7vqbibBhXVca0dib3sXZibZXW4l5DiaNKCTibhew0/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)

1. 输入「what skills do you have?」，可以看到这里并没有 seekdb 相关的 skill。输入「/exit」，先退出。
![图片](https://mmbiz.qpic.cn/mmbiz_png/Z9yXJ1qu4pgDuQHAeAv9V0wa8hf2ZCbgK9e1ujPWicfZLicy3FJPZiabnXibU6aexTOB2T01icfoq2YA16MU4zqic6IlJpCJpOUp9sS1mRl0Ch8Ic/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9)

更多细节见官方：快速入门、安装说明。

## 通过 pip 安装 seekdb Agent Skill

seekdb Agent Skill 以 **Python 包** 形式发布在 PyPI，通过 `pip` 安装后，运行交互式安装器将技能安装到 OpenClaw 的工作区。

1. 安装 Python 包

**注意：Ubuntu 等系统可能无法直接运行下面的命令，如果有报错，请先创建虚拟环境**

```
pip install seekdb-agent-skills
```
1. 运行交互式安装器
```
seekdb-agent-skills
```
1. 在安装器中操作
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Z9yXJ1qu4pgrKGFLnhfADDSDChQXSoxZmmIicyZeOgDZdV3RJGIYKkxYVGhXg5jSkHKTJC5Cy1f1FHKIV7AevY0rs6pP5ib2UUgvZII1VibUt4/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10)

- **选择工具** ：在列表中选择 **OpenClaw** 。
- **确认安装路径** ：安装器会将技能安装到 `~/.openclaw/workspace/skills` ，确认即可。
- **选择技能** ：默认勾选了 **seekdb** （文档技能），可以直接点击 Enter 键确认。
- 用方向键与 Space 多选，Enter 确认，安装器会把对应技能目录复制到 OpenClaw 工作区。

安装完成后，如果在 Web 页面需要点击「New session」，如果在 TUI 需要输入「/new」，以便加载新技能（OpenClaw 会扫描 `~/.openclaw/workspace/skills` 下的技能）。

1. 确认技能是否已安装，有多种确认方式

命令行中确认：

```
openclaw skills
```

预期输出如下：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Z9yXJ1qu4phEnBOWe4DFFcxj9XmFoW8K72pXtXOZ19HDcMuUCfz07ibNGekZLiaOXDGB1m4yJ1P3lvIQmicwNojBRicQvicqBRFum9MNhSg8nIa8/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=11)

Web UI 确认：

点击 SKills 选项卡，输入 seekdb 进行查询

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Z9yXJ1qu4phWGdnQomsjZkw4HUyuxBl0Zy9l3icubD8xJfvLdFZxwFC8I5YaibMiblKYqicb53VjtQFn5ndtnlb3lN2ia3z4WbdIXbwWklxyKC7U/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=12)

## 通过 ClawHub 安装 seekdb Agent Skill

除 pip 外，你也可以通过 ClawHub 安装 seekdb Agent Skill。

两种安装方式的区别在于： ClawHub 不支持下载大量文件，在 ClawHub 上的 seekdb Agent Skill 仅提供 **远程模式** （从 GitHub 拉取文档），不包含本地文档，使用前需能访问 GitHub；而通过 PyPI 安装的版本则同时支持 **本地模式** 和 **远程模式** ，可在无网络或 GitHub 不可用时回退到本地文档。

1. 安装 clawhub
```
npm install -g clawhub
```
1. 安装 seekdb-docs 技能
```
clawhub install seekdb-docs
```

安装完成后，验证技能是否已安装的方式与 pip 相同：可在命令行执行 `openclaw skills` 查看技能列表，或在 Web UI 中点击 Skills 选项卡、输入 seekdb 进行查询。

## 开始对话

> 说明：这里 OpenClaw 的实际表现，会和模型的选择有较大的关系。

### 1\. 查看下当前都有什么技能

输入「what skills do you have?」，显示了 seekdb-docs 的技能

![图片](https://mmbiz.qpic.cn/mmbiz_png/Z9yXJ1qu4pjlOzM9xX7tXaXVk13X1sJcanJf4H2z7sqNMprm7WwmlSr9dXByy8uJUDJwyPFTWHpibdiaLjaiarjT6wLHrzViblDB2R9NMjPp7iaI/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=13)

### 2\. 再打开 TUI

因为 OpenClaw 的 Web UI 页面和 TUI 指向的是同一个会话，这个问题我们打开 TUI

输入下面的命令：

```
openclaw tui
```

我们并没有输入任何问题，打开 TUI，就把在 Web UI 上问的问题带进来了

![图片](https://mmbiz.qpic.cn/mmbiz_png/Z9yXJ1qu4phw5ufVWjRnfbIA2B3JpFeiaSJY6OkHiaDkODEqvGpdNHDqiaMTurJibcEzfl7htVxme6gKd30crXauavo0PsXHXbwuMAnDT1BicLzg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=14)

### 3\. 询问如何部署 seekdb

输入「how to deploy seekdb?」，它正确回答了 seekdb 的部署方式。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Z9yXJ1qu4pia6sTUdpeIjzTHoFW7xWKWJL82nQpwTdIFHfKIn6l0rdR3be7SpwAWnhJU3JuIic5BNia3y5NiaTQKf6ufCrpVicRiaia38JHPQp9Zz4/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=15)

你还可以继续追问，例如：

1. 「how to use vector search in seekdb?」
2. 「seekdb 支持哪些 AI 框架集成？」
3. 「如何在 seekdb 中实现混合搜索？」等等。

只要问题与 seekdb 文档相关，OpenClaw 都会优先使用这套 Skills 来进行解答和执行相关的任务。

![OpenClaw founder Peter Steinberger is joining OpenAI | The Verge](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Z9yXJ1qu4piapohUx5NW85LjHvjp4rUiayyRh3iayQoNzGiakATPkYHBTwqgAAibW25Obfpw7rqcZia27e6Y15icxgiaor0cs2HA14iaIeHqibj7b9M4k/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=16)

OpenClaw founder Peter Steinberger is joining OpenAI | The Verge

## 相关资料

- seekdb 官网：https://oceanbase.ai/zh-CN/
- seekdb 项目仓库：https://github.com/oceanbase/seekdb
- seekdb 官方文档：https://www.oceanbase.ai/docs/

作者提示: 个人观点，仅供参考

[阅读原文](https://mp.weixin.qq.com/s/)

继续滑动看下一个

老纪的技术唠嗑局

向上滑动看下一个