---
title: "Openclaw自己操作Claude code完整开发了TikTok爆款分析系统"
source: "https://mp.weixin.qq.com/s/Nlu_8FZZ2y-6Z7eZZbABtQ"
author:
  - "[[饼干哥哥]]"
published:
created: 2026-03-08
description: "OpenClaw 当项目经理，Claude Code 当工程师。我当老板。"
tags:
  - "clippings"
---
原创 饼干哥哥 *2026年3月8日 20:46*

OpenClaw 火了两个月，199K star，全网都在吹。

但我实测下来只有一个结论—— 凡是涉及到产品开发，它就是一坨💩

不是说它不能写代码。它能写。问题是写完就崩，崩了不知道，你第二天早上起来发现昨晚安排的活全部白费。进程死了没人管，参数传错了没人报，卡在一个交互提示上一等就是一整夜。

我连着踩了两周的坑，每天早上的心情都是：又白跑了。

直到我换了一个思路—— 让它去操作目前编程能力最强的工具——Claude Code。

然后就有了这个东西：

![Image](https://mmbiz.qpic.cn/mmbiz_jpg/UQ9fsOliarQ9K8picmgTYIMEAibfKSlHqqicly6FqP78hCaOUNfLoMzhjnLG6opopWGdnicadJia02LCgtdRXauxz8X4Fia3BKOkicSpekssppfBibmg/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

这是一个 TikTok 爆款视频拆解网站。上传一个视频，自动分析它的营销策略、逐帧拆解每个镜头、逆向生成可以直接用在 Sora 里的提示词、还能把语音转成结构化脚本。

![Image](https://mmbiz.qpic.cn/mmbiz_jpg/UQ9fsOliarQ8UJWcfrSmOOYjyMG6zO3Z9VSibZbXKibLE7UPXzTJeEnnX6kuO2OQBmjKlB6zSzTB14VoVwvfJyJ9fkOWsq1BshGZDCZsIAibRmM/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1) ![Image](https://mmbiz.qpic.cn/mmbiz_jpg/UQ9fsOliarQ9PibcOcXzVfaJCzzm3laq2sPRIzKseXb20Wnep9ndbETFmLY6Czaqjcu8WRiabr4yZrPwGWfAgXcsj9WlPsDCURHb3Lwh4WLopE/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

从我说出需求到产品可用，我只在飞书讲了我的需求：

```
我要开发的产品是：tiktok视频拆解网站。功能是，用户上传一个视频后，能逆向出它的提示词、拆成多个视频片段做更细致的分析。主要目的是帮助用户分析爆款视频，并且提炼出来一套玩法后，自己能复刻、模拟生成这类爆款。
```

剩下的，全是 OpenClaw 自己跟 Claude Code 之间在搞。

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/UQ9fsOliarQic3ibeeB8GK9ibYicd2yBCwfe8tqsYRuRCEaORsoMzLkBe1ANbBl72l7oHiaZYOoibibIPQowBaOeoMIIjhJWUu2K9erYzJPWBPbpX9c/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3) ![Image](https://mmbiz.qpic.cn/mmbiz_png/UQ9fsOliarQicSdZmRdHAOEITrpV6qB4OWprdynJ50OsHUrtyVzHeRTcgVOEoOu5MKoLXtxNG7bbdPzAU8ufkSSpV6RagBXIFGOIy2TZiaRaW8/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4) ![Image](https://mmbiz.qpic.cn/mmbiz_png/UQ9fsOliarQ8icf4YqhVWhHu8ASEeic7c0S3AJ5sWibmOE7taLbRlW58UiaicYYhSGsQrF6q9ZBx1XKq4U7uChBnIvondtaibjYiaKHlLJ6M0OJeXeo/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

## OpenClaw是项目经理

这是我踩了两周坑之后想通的一件事。

OpenClaw 的优势是什么？24 小时在线、能连飞书/Telegram/Discord、有持久记忆、能同时管理多个任务。

Claude Code 的优势是什么？编程能力碾压级、理解整个代码库、自主调试修复、有完整的工具链。

那答案就很明显了——

让 OpenClaw 当项目经理，让 Claude Code 当高级开发工程师。

我只跟项目经理说需求，项目经理自己拆任务、盯进度、处理报错、测试验收。开发工程师闷头写代码就行。

这套架构跑通之后，流程变成了这样：

👻

我在飞书发一段话描述产品 → OpenClaw 自己写 PRD 和技术方案发给我确认 → 我说 OK → 它自己指挥 Claude Code 初始化项目、逐功能开发 → 中间需要 API Key 才来问我 → 开发完自动跑 Playwright 测试 → 把测试报告和截图发到飞书

全程我只参与两个节点：确认方案、看最终效果。

## 跟直接用 Claude Code 有什么区别

你可能会问：我直接在终端操作 Claude Code 不也能开发吗？为什么要套一层 OpenClaw？

三个区别：

第一，你不用坐在电脑前盯着。

Claude Code 是交互式的。它改完一个文件会问你要不要继续，遇到模糊需求会停下来问你，测试失败了等你决定怎么处理。你不在，它就卡着。

OpenClaw 替你盯着。它能自己判断大部分情况该怎么处理，处理不了的才来飞书问你。凌晨三点它自己修 bug，你早上起来看结果就行。

第二，Claude Code 遇到问题就停，OpenClaw 会自己先扛。

Claude Code 碰到依赖冲突、类型报错、测试失败，它会停下来等你。OpenClaw 会自己读错误日志、自己发修复指令给 Claude Code，修不好才来找你。大部分技术问题你根本不需要知道它发生过。

第三，Claude Code 一次只能盯一个事，OpenClaw 能并行调度。

在 Claude Code 里开发后端 API 的时候没法同时让它调前端样式。OpenClaw 可以起多个 Claude Code 后台进程，一个写后端一个调前端，自己协调合并，你不需要手动切来切去。

  

## OpenClaw 直接调 Claude Code 最痛的问题

在讲配置之前，先说清楚三个致命问题，不然你不知道这套方案在解决什么。

1. 1\. 进程管理是空白的。

Claude Code 每次调用会启动一个子进程。这个进程随时可能因为内存不够、网络断开、上下文太长等原因死掉。死了之后 OpenClaw 完全不知道，它以为任务还在跑。

1. 2\. 交互阻塞会卡死一切。

Claude Code 干活的时候经常会停下来问问题。你坐在电脑前打个字就行了，但 OpenClaw 是凌晨在后台跑的，没人回答它就永远等着。

1. 3\. 结果送不回来。

Claude Code 干完了，结果在终端里。OpenClaw 不知道干完了，你也不知道。没人通知任何人。

  

这些问题不解决，OpenClaw + Claude Code 就是两个各干各的工具，不是一个系统。

![图片](https://mmbiz.qpic.cn/mmbiz_png/UQ9fsOliarQ9toua2CICSOeRRbGzHWlvlLIYtQv0ias8nxIzAZ6WrXyU1Ny8J44vgEiavicTWkb0B5xqzBoOUZ3yMtEtgrDpiaNFOCPILeqIfKBE/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

## 我的解法：一个 Skill 文件搞定所有

这个 Skill 文件定义了完整的开发流程：

- 收到产品需求 → 自己写 PRD + 技术方案 → 发给用户确认
- 确认后 → 用 PTY 模式启动 Claude Code → 初始化项目
- 逐功能拆解 → 一个一个交给 Claude Code 开发
- 每个功能完成后自己检查输出，报错了自己修
- 需要 API Key 这种敏感信息才来问用户
- 全部开发完 → 用 Playwright 自动测试 → 截图发报告

关键技术细节在于： 调用 Claude Code 必须用 PTY 模式。

没有 PTY，Claude Code 的 CLI 会挂起或者输出乱码。OpenClaw 社区里无数人踩过这个坑。

加上 pty:true 就解决了。

```
bash pty:true workdir:~/projects/xxx background:true command:"claude --session-id xxx --permission-mode acceptEdits '你的任务指令'"
```

就这一行命令，解决了上面说的三个问题：

- background:true 让任务后台运行，OpenClaw 可以继续处理其他事
- \--session-id 保持会话上下文，中断了可以 \--resume 恢复
- \--permission-mode acceptEdits 让 Claude Code 不用每改一个文件都停下来问

  

同时，为了让Openclaw能懂Claude Code的操作，最好可以单独让AI整理一份实操文档作为 Skill

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/UQ9fsOliarQibgVWRHEGpD5l3z3DS8uZxYKrcKCkpGhHKbUfsS22ibuuvLZcaQLZOAoU3gnPbNWXzSQLdDfmK2Z5tUzrE37KLqVC1RNY6Ijfe8/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

👻

限于篇幅，关注公众号「饼干哥哥AGI」后台回复「Claude code」

获取： Claude code最小闭环核心文档 openclaw agent skill.md

## 开箱即用的配置教程

下面是完整配置，照抄就能用。

### 第一步：在 AGENTS.md 末尾加这段

打开你 OpenClaw 工作空间里的 AGENTS.md，在最后面加上：

```
## 🔧 Claude Code 开发集成

当用户描述一个想做的产品/网站/工具时，使用 skills/fullstack-dev/SKILL.md 中的流程自主完成开发。

核心规则：
- 你是项目经理，Claude Code 是开发工程师
- 调用 Claude Code 必须用 bash pty:true，否则会挂起
- 用户只需要确认 PRD 和最终验收，中间不要打扰
- 出了技术问题自己解决，需要密码/Key 才问用户
- 开发完用 Playwright 自动测试，截图发给用户
```

这段话是告诉 OpenClaw：你现在有开发能力了，收到开发需求就去干。

### 第二步：在 TOOLS.md 里加开发工具信息

```
## 开发工具
- Claude Code：已安装，用 OAuth 登录
- 项目目录：~/projects/
- Playwright：用于端到端测试
- FFmpeg：视频处理
```

### 第三步：改 USER.md

把你的信息填进去，特别是加一条：

```
- 偏好：我只说产品需求，技术方案你自己定。别问我技术细节。
```

这条很重要。不写的话 OpenClaw 会不停来问你技术问题。

### 第四步：创建核心 Skill 文件

在你的 OpenClaw 工作空间创建这个路径：

```
skills/fullstack-dev/SKILL.md
```

把下面这整段内容粘贴进去。这是整套方案的核心，教会 OpenClaw 怎么自主完成一个项目的全流程：

```
---
description: "全栈项目开发技能。当用户描述一个想做的产品/网站/工具时自动触发。你负责从需求理解到开发执行、测试验收的全流程。用户只需要描述想法，你自主完成一切。"
---

# Fullstack Development Skill

你是一个资深技术合伙人。用户是产品负责人，他只说想要什么，剩下的全部由你搞定。

你有一个高级开发工程师：Claude Code。你通过命令行指挥它写代码。

## 核心原则
## 完整流程

## Phase 1：需求理解 → PRD
## Phase 2：项目初始化
## Phase 3：逐功能开发
## Phase 4：自动化测试
## Phase 5：交付报告
```

👻

限于篇幅，关注公众号「饼干哥哥AGI」后台回复「Claude code」

在源文档看完整版 skill.md

### 第五步：开始用

以后你想做任何产品，就发这样一段话：

```
我想做一个 [产品名]。

[3-5 句话描述给谁用、解决什么问题]

核心功能：
1. xxx
2. xxx
3. xxx

做好后测试一遍发我看效果。
```

OpenClaw 会自己走完全部流程，你只需要确认 PRD 和看最终效果。

## 这套方案真正解决了什么

不是解决了一个开发需求。

是解决了一类问题：以后任何时候我想做一个工具、一个网站、一个小产品，我只需要在飞书里发一段话。

不需要打开终端，不需要写一行代码，不需要懂任何技术细节。

OpenClaw 当项目经理，Claude Code 当工程师。我当老板。

这才是 OpenClaw 该干的事。

继续滑动看下一个

饼干哥哥AGI

向上滑动看下一个