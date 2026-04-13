# Claude Code 最小闭环核心文档：必知必会操作指南

> **文档目的**：为 OpenClaw 提供一份完整的 Claude Code 操作知识体系，使其作为 agent skill 能够顺畅地调用和操控 Claude Code 完成编码、调试、部署等任务。
>
> **文档性质**：这是关于 **Claude Code** 的操作说明（被操控对象），而非 OpenClaw 本身的配置文档。
>
> **信息来源**：本文档综合了 Anthropic 官方文档、社区最佳实践、Discord/Reddit/X/Substack 等平台的实战经验编写而成。来源链接附于文末。

---

## 第一章：Claude Code 是什么

Claude Code 是 Anthropic 出品的**终端原生 AI 编程助手**（CLI 工具）。它不是聊天机器人——它是一个**代理式编码环境（agentic coding environment）**，可以读取文件、执行命令、编辑代码、运行测试，并在你观察或离开时自主解决问题。

核心特征：

- 运行在终端中，理解整个代码库的文件结构、依赖关系和 Git 历史
- 使用 Claude Opus 4.6（最强推理）或 Claude Sonnet 4.6（快速高效）
- 拥有专有的 agentic loop：收集上下文→执行操作→验证结果，循环进行
- 200K token 上下文窗口，可将整个项目保持在记忆中
- 支持 VS Code、JetBrains、桌面应用、Web 界面等多种使用方式

---

## 第二章：安装与启动

### 2.1 安装方式

```bash
# 方式一：npm（推荐，自动更新）
npm install -g @anthropic-ai/claude-code

# 方式二：Homebrew（macOS，不自动更新）
brew install claude-code

# 方式三：WinGet（Windows，不自动更新）
winget install Anthropic.ClaudeCode
```

**前置要求**：Node.js 18+；Windows 需先安装 Git for Windows。

### 2.2 认证登录

```bash
# 首次运行，按提示浏览器登录
claude

# 或使用 API Key
export ANTHROPIC_API_KEY="sk-ant-..."
```

支持：Claude Pro/Max 订阅 或 Anthropic API Key。

### 2.3 在项目中启动

```bash
cd ~/your-project
claude
```

Claude Code 会自动扫描项目结构，理解代码库。

---

## 第三章：交互模式与核心命令

### 3.1 两种运行模式

| 模式 | 说明 | 启动方式 |
|------|------|----------|
| **交互模式** | 在终端中对话式操作 | `claude` |
| **非交互模式（Headless）** | 单次执行，输出到 stdout，适合自动化 | `claude -p "提示词"` |

### 3.2 必知 Slash 命令

```
/init          — 扫描代码库生成 CLAUDE.md（首次必做）
/help          — 查看所有可用命令
/clear         — 清除对话上下文（切换任务时用）
/compact       — 压缩上下文（保留核心信息）
/compact focus on API changes  — 带焦点的压缩
/model         — 切换模型（opus/sonnet/haiku）和推理模式
/context       — 查看当前上下文使用量
/usage         — 设置每周用量限制
/config        — 配置设置（如开启 thinking mode）
/permissions   — 管理工具权限
/agents        — 管理子代理（subagents）
/mcp           — 查看 MCP 服务器及其上下文开销
/rewind        — 回退对话或代码（支持分别回退）
/output-style  — 切换输出风格
/add-dir       — 会话中添加额外工作目录
```

### 3.3 核心快捷键

```
Shift+Tab    — 循环切换权限模式：Normal → Auto-Accept → Plan Mode
Ctrl+C       — 取消当前操作
Ctrl+B       — 将任务放到后台运行
Ctrl+T       — 切换任务列表显示
Esc+Esc      — 回退到之前状态（rewind）
```

### 3.4 会话管理

```bash
claude                    # 开启新会话
claude -c                 # 继续上一个会话（--continue）
claude --resume           # 恢复指定会话（交互选择）
claude --resume <id>      # 恢复指定 session ID 的会话
```

---

## 第四章：权限模式（Permission Modes）

Claude Code 有 **五种权限模式**，这是操控 Claude Code 的关键：

| 模式 | 行为 | 适用场景 |
|------|------|----------|
| **Normal（默认）** | 每个危险操作都要确认 | 生产环境、敏感操作 |
| **Auto-Accept Edits** | 自动批准文件编辑，其他操作仍需确认 | 快速原型迭代 |
| **Plan Mode** | 只读模式，不做任何修改 | 代码探索、方案规划 |
| **Don't Ask** | 除了预先批准的工具外，自动拒绝所有 | 受限自动化 |
| **Bypass Permissions** | 自动批准所有操作（危险！） | 仅限隔离容器/CI |

**切换方式**：
- 交互模式：按 `Shift+Tab` 循环
- 命令行启动：`claude --permission-mode plan`
- 非交互模式：`claude -p "..." --dangerously-skip-permissions`（仅限容器内）

---

## 第五章：非交互模式（Headless Mode）——OpenClaw 操控核心

**这是 OpenClaw 操控 Claude Code 的最关键章节。**

### 5.1 基本语法

```bash
# 基本用法：-p 或 --print
claude -p "分析这个项目的架构"

# 指定输出格式
claude -p "总结项目" --output-format text    # 纯文本（默认）
claude -p "总结项目" --output-format json    # JSON 带元数据
claude -p "总结项目" --output-format stream-json  # 实时流式 JSON
```

### 5.2 关键标志（Flags）

```bash
# 限制工具权限（安全关键）
--allowedTools "Read,Grep,Glob"          # 只读
--allowedTools "Read,Write,Edit,Bash"    # 读写+执行
--allowedTools "*"                       # 全部（危险）

# 限制执行轮次（防止无限循环）
--max-turns 5        # 简单任务用 3-5
--max-turns 10       # 复杂任务用 10

# 选择模型
--model opus         # 最强推理
--model sonnet       # 快速高效（推荐日常）
--model haiku        # 最快最便宜

# 权限模式
--permission-mode plan              # 只读分析
--permission-mode acceptEdits       # 自动接受编辑
--dangerously-skip-permissions      # 跳过所有权限（仅限容器）

# 系统提示
--append-system-prompt "你是安全工程师"    # 追加提示
--system-prompt "完全替换的系统提示"        # 替换默认提示

# 会话保持（多轮对话）
--session-id my-review-001     # 指定会话 ID
--continue                     # 继续最近会话
--resume <session-id>          # 恢复指定会话
```

### 5.3 OpenClaw 调用 Claude Code 的推荐模式

**关键原则**：不要尝试"驱动 TUI"，把 Claude Code 当作 CLI 工具用。

```bash
# 模式一：单次任务（最常用）
claude -p "实现用户认证功能，运行测试，总结变更" \
  --allowedTools "Read,Write,Edit,Bash" \
  --max-turns 10 \
  --output-format json

# 模式二：管道输入
cat error.log | claude -p "分析错误日志，找到根本原因"
git diff HEAD~1 | claude -p "审查这个 diff，列出潜在问题"

# 模式三：后台长期运行（PTY 模式）
bash pty:true workdir:~/your-project background:true \
  command:"claude 'Refactor Y. Keep behavior. Run tests.'"

# 模式四：多轮会话
claude -p "分析 src/ 目录的代码" --session-id review-001
claude -p "刚才发现了什么 bug？" --session-id review-001
claude -p "修复最严重的那个 bug" --session-id review-001
```

### 5.4 监控后台进程

```bash
process action:log sessionId:<id>       # 查看日志
process action:poll sessionId:<id>      # 轮询状态
process action:submit sessionId:<id> data:"yes"  # 回答提示
```

### 5.5 PTY 的重要性

OpenClaw 通过 exec 调用 Claude Code 时**必须使用 PTY**。没有 PTY，CLI 经常会挂起或输出不可用。推荐模式：

```bash
bash pty:true workdir:~/your-project command:"claude 'your task'"
```

---

## 第六章：CLAUDE.md — 持久化记忆系统

CLAUDE.md 是 Claude Code 在每个会话开始时自动读取的配置文件，**相当于 Claude Code 的记忆和宪法**。

### 6.1 层级结构

```
~/.claude/CLAUDE.md            — 全局（所有项目通用）
~/project/CLAUDE.md            — 项目级（当前项目专用）
~/project/src/CLAUDE.md        — 子目录级（进入该目录时加载）
```

所有层级是**叠加**的，不会覆盖。

### 6.2 初始化

```bash
# 进入项目后运行
/init
```

这会扫描代码库自动生成 CLAUDE.md，包括构建系统、测试框架、代码模式等。

### 6.3 最佳实践

- **控制在 200 行以内**，太长会导致指令被忽略
- 包含：构建命令、代码风格、项目架构、工作流规则
- 可以用 `@path/to/file` 语法引用其他文件：
  ```markdown
  See @README.md for project overview
  @docs/git-instructions.md
  ```
- 把 CLAUDE.md 加入 Git，让团队共同维护
- 如果 Claude 不遵守规则，检查文件是否太长导致规则被淹没
- 用 "IMPORTANT" 或 "YOU MUST" 等强调词可以提高遵守率

### 6.4 示例

```markdown
# Project: MyApp

## Tech Stack
- Frontend: React, TypeScript, Tailwind
- Backend: Node.js, PostgreSQL

## Commands
- `npm run dev` - Start dev server
- `npm test` - Run tests
- `npm run build` - Production build

## Code Style
- Use TypeScript strict mode
- Prefer functional components with hooks
- All functions must have JSDoc comments

## Git Workflow
- Branch naming: feature/xxx, fix/xxx
- MUST run tests before committing
- Commit messages follow conventional commits
```

---

## 第七章：Skills（技能）— 可复用知识包

### 7.1 概念

Skills 是 markdown 文件，存放在 `.claude/skills/` 目录中。与 CLAUDE.md 不同，Skills 是**按需加载**的——Claude 看到技能描述后，只在需要时才加载完整内容。

### 7.2 创建 Skill

```
.claude/skills/
  deploy/
    SKILL.md           ← 必须的主文件
    reference.md       ← 可选的详细参考
    examples.md        ← 可选的用法示例
    scripts/
      helper.py        ← 可选的辅助脚本
```

**SKILL.md 示例**：

```markdown
---
description: "Deploy the application to staging or production"
allowed-tools: Bash(npm:*), Bash(git:*), Read, Write
---

# Deploy Skill

## Steps
1. Run `npm test` to verify all tests pass
2. Run `npm run build` to create production bundle
3. Deploy using `npm run deploy -- --env $ARGUMENTS`
4. Verify deployment at the target URL

## Additional resources
- For environment configs, see [reference.md](reference.md)
```

### 7.3 调用方式

- 用 `/deploy staging` 显式调用
- Claude 根据对话上下文自动识别并调用

### 7.4 与 Slash Commands 的区别

| 特性 | Slash Commands | Skills |
|------|---------------|--------|
| 文件位置 | `.claude/commands/name.md` | `.claude/skills/name/SKILL.md` |
| 调用方式 | `/name` 手动调用 | 自动或 `/name` |
| 支持文件 | 单文件 | 可包含目录 |
| 上下文加载 | 调用时加载 | 描述始终可见，内容按需 |

---

## 第八章：Subagents（子代理）— 上下文隔离

### 8.1 概念

Subagents 是拥有**独立上下文窗口**的 Claude 实例。主对话不会被子代理的工作内容膨胀。

### 8.2 创建方式

**文件方式**（推荐）：

```markdown
<!-- .claude/agents/code-reviewer.md -->
---
name: code-reviewer
description: "Expert code reviewer. Use after code changes."
model: sonnet
tools:
  - Read
  - Grep
  - Glob
  - Bash
---

You are a senior code reviewer. Focus on:
- Security vulnerabilities
- Performance issues
- Code quality and maintainability
```

**CLI 方式**：

```bash
claude --agents '{
  "code-reviewer": {
    "description": "Expert code reviewer",
    "prompt": "You are a senior code reviewer...",
    "tools": ["Read", "Grep", "Glob", "Bash"],
    "model": "sonnet"
  }
}'
```

### 8.3 使用策略

- 用子代理做**研究、验证、审查**等不需要修改代码的工作
- 让主代理决定何时委派工作（Master-Clone 模式）
- 内置子代理类型：`Explore`（探索）、`Plan`（规划）、`Verify`（验证）
- 子代理完成后只返回摘要，不污染主上下文

### 8.4 异步代理

```
Ctrl+B  — 将当前任务放到后台
```

可以启动多个后台子代理并行工作，主对话继续。

---

## 第九章：Hooks（钩子）— 自动化触发器

Hooks 可在 Claude Code 操作前后自动执行 shell 命令。

### 9.1 配置位置

在 `settings.json`（用户或项目级）中配置：

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write(*.py)",
        "hooks": [
          {
            "type": "command",
            "command": "python -m black \"$file\""
          }
        ]
      }
    ]
  }
}
```

### 9.2 常用 Hook 类型

| Hook | 触发时机 | 典型用途 |
|------|----------|----------|
| PreToolUse | 工具使用前 | 权限检查、请求修改 |
| PostToolUse | 工具使用后 | 自动格式化、lint |
| SessionStart | 会话启动时 | 环境初始化 |

---

## 第十章：MCP（Model Context Protocol）— 外部工具连接

### 10.1 概念

MCP 让 Claude Code 连接外部服务（GitHub、Slack、Jira、数据库等）。

### 10.2 添加 MCP 服务器

```bash
# CLI 方式
claude mcp add github --scope user -- npx -y @modelcontextprotocol/server-github

# JSON 方式
claude mcp add-json github '{"command":"npx","args":["-y","@modelcontextprotocol/server-github"],"env":{"GITHUB_PERSONAL_ACCESS_TOKEN":"ghp_xxx"}}'

# 查看已添加
claude mcp list

# 删除
claude mcp remove github
```

### 10.3 配置文件位置

```
.mcp.json                     — 项目级（可 Git 共享）
~/.claude/settings.local.json — 用户级
```

### 10.4 权限配置

在 `settings.json` 中允许 MCP 工具：

```json
{
  "permissions": {
    "allow": [
      "mcp__github__*",
      "mcp__slack__*"
    ]
  }
}
```

### 10.5 注意事项

- MCP 服务器会在每次请求中添加工具定义，**消耗大量上下文**
- 用 `/mcp` 检查每个服务器的上下文开销
- 不需要的 MCP 及时关闭

---

## 第十一章：上下文管理——核心生存技能

Claude Code 的 200K token 窗口看似很大，但复杂项目中很快会耗尽。

### 11.1 上下文节省策略

| 方法 | 说明 |
|------|------|
| `/compact` | 压缩当前对话，保留关键信息 |
| `/clear` | 切换任务时清空上下文 |
| 使用 Subagents | 隔离上下文，只返回摘要 |
| Skills 按需加载 | 设置 `disable-model-invocation: true` 减少描述开销 |
| 精简 CLAUDE.md | 控制在 200 行以内 |
| 减少 MCP 服务器 | 每个服务器都消耗上下文 |

### 11.2 关键规则

- 上下文用量超过 50% 时执行 `/compact`
- 不要在 "agent dumb zone"（上下文快满时）继续工作
- 切换任务时用 `/clear` 重置
- 持久化规则放在 CLAUDE.md，不要依赖对话历史
- 用 `/context` 随时查看使用量

---

## 第十二章：Git 集成与工作流

### 12.1 基础操作

Claude Code 原生理解 Git：

```
"创建一个新分支 feature/auth，实现用户认证，提交并推送"
"查看当前 diff 并创建有意义的提交消息"
"解决当前的合并冲突"
```

### 12.2 推荐安装 gh CLI

```bash
# GitHub CLI 让 Claude 能创建 PR、管理 Issue
brew install gh  # 或对应系统的安装方式
gh auth login
```

Claude 可以用 gh 做：创建 Issue、开 PR、读评论等。

### 12.3 Git Worktrees（并行开发）

```bash
# 创建 worktree 并行开发
git worktree add ../feature-auth feature/auth
cd ../feature-auth
claude
```

### 12.4 远程执行

```bash
# 在云端运行，不阻塞本地
claude --remote "Fix the flaky test in auth.spec.ts"
claude --remote "Update API documentation"

# 查看所有远程任务
/tasks

# 将远程会话拉到本地
/teleport
```

---

## 第十三章：settings.json 配置体系

### 13.1 层级优先级（从高到低）

1. **Managed**（企业管理策略）——不可覆盖
2. **CLI 参数**——临时会话覆盖
3. **Local**（`.claude/settings.local.json`）——项目本地
4. **Project**（`.claude/settings.json`）——项目级共享
5. **User**（`~/.claude/settings.json`）——全局默认

### 13.2 核心配置示例

```json
{
  "model": "sonnet",
  "permissions": {
    "allow": [
      "Bash(npm:*)",
      "Bash(git:*)",
      "Read",
      "Write",
      "Edit"
    ],
    "deny": [
      "Bash(rm -rf:*)",
      "Bash(sudo:*)"
    ]
  },
  "env": {
    "NODE_ENV": "development"
  }
}
```

### 13.3 权限规则语法

```
Read                     — 所有文件读取
Write(*.py)             — 只写 Python 文件
Bash(npm test:*)        — 只允许 npm test 命令
Bash(git diff *)        — 注意 * 前的空格很重要
mcp__github__*          — GitHub MCP 所有工具
Task(Explore)           — 允许使用 Explore 子代理
```

规则评估顺序：deny → ask → allow，先匹配到的生效。

---

## 第十四章：CI/CD 集成

### 14.1 GitHub Actions 示例

```yaml
name: Claude Code Review
on:
  pull_request:
    types: [opened, synchronize]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install Claude Code
        run: npm install -g @anthropic-ai/claude-code
      - name: Review PR
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          claude -p "Review the code changes for security issues" \
            --allowedTools Read,Grep,Glob \
            --max-turns 3 \
            --output-format json > review.json
```

### 14.2 CI 安全要点

- **始终用 `--allowedTools` 限制工具**
- **用 `--max-turns` 防止无限循环**
- 在隔离容器中才用 `--dangerously-skip-permissions`
- 用专用 API Key，设置月度预算上限
- 重定向 JSON 输出到日志文件以便审计

---

## 第十五章：常见问题与踩坑经验

### 15.1 Claude 忽略 CLAUDE.md 规则

- CLAUDE.md 太长，规则被淹没——精简到 200 行
- 措辞不够强烈——用 "MUST"、"IMPORTANT"、"NEVER" 等强调
- 规则放在文件底部——重要规则放顶部

### 15.2 上下文耗尽

- 症状：Claude 变"笨"，忘记之前的讨论
- 解决：在 50% 时执行 `/compact`，或 `/clear` 重新开始
- 预防：使用 Subagents 隔离大量读取操作

### 15.3 非交互模式挂起

- 原因：没有使用 PTY，或没有设置 `--max-turns`
- 解决：OpenClaw 调用时始终用 PTY 和 max-turns
- 保护：`timeout 30m claude -p "..."` 加系统级超时

### 15.4 MCP 权限问题

- 在 `settings.json` 的 `permissions.allow` 中添加 `mcp__servername__*`
- headless 环境中需要预先配置权限，无法弹出交互确认

### 15.5 Prompt 引号问题

```bash
# 错误——shell 会拆分
claude -p Analyze this file

# 正确——用引号包裹
claude -p 'Analyze this file and generate a report'
```

### 15.6 费用控制

- Sonnet 处理 90% 的任务，日均 $2-5
- Opus 用于深度推理，日均 $10-15+
- 用 `/usage` 设置每周限制
- CI 中用 `--max-turns` 控制 token 消耗

---

## 第十六章：OpenClaw 调用 Claude Code 的最佳实践总结

### 16.1 黄金法则

1. **用 `-p` 非交互模式**，不要尝试驱动 TUI
2. **始终指定 `--max-turns`**，防止无限循环
3. **始终指定 `--allowedTools`**，最小权限原则
4. **用 PTY 启动**，否则 CLI 可能挂起
5. **用 `--output-format json`** 获取结构化输出
6. **用 `--session-id`** 保持多轮对话的上下文

### 16.2 任务模板

**代码审查**：
```bash
claude -p "Review src/ for bugs, security issues, and performance problems" \
  --allowedTools "Read,Grep,Glob" \
  --permission-mode plan \
  --max-turns 5 \
  --output-format json
```

**实现功能**：
```bash
claude -p "Implement user authentication with JWT. Write tests. Run tests." \
  --allowedTools "Read,Write,Edit,Bash" \
  --max-turns 15 \
  --output-format json
```

**修复 Bug**：
```bash
claude -p "Fix the login bug where users see blank screen after wrong password" \
  --allowedTools "Read,Write,Edit,Bash" \
  --max-turns 10 \
  --output-format json
```

**代码探索**：
```bash
claude -p "Explain the authentication architecture of this project" \
  --allowedTools "Read,Grep,Glob" \
  --permission-mode plan \
  --max-turns 3 \
  --output-format text
```

**Git 操作**：
```bash
git diff HEAD~1 | claude -p "Create a meaningful commit message for these changes" \
  --allowedTools "Read" \
  --max-turns 1 \
  --output-format text
```

### 16.3 错误处理

```bash
# 始终检查退出码
if claude -p 'Fix the bug' --output-format json > result.json 2>&1; then
  echo "成功"
  cat result.json | jq -r '.result'
else
  echo "Claude Code 失败，退出码: $?"
  exit 1
fi
```

### 16.4 并行任务

OpenClaw 可以同时启动多个 Claude Code 进程：

```bash
# 并行启动多个任务
claude -p "Fix flaky test" --session-id fix-test &
claude -p "Update docs" --session-id update-docs &
claude -p "Refactor logger" --session-id refactor &
wait
```

---

## 第十七章：Agent SDK（程序化集成）

Claude Agent SDK（原 Claude Code SDK）提供 Python 和 TypeScript 的程序化接口：

```python
# Python 示例
from claude_code import ClaudeCode

result = ClaudeCode.query(
    "Analyze this codebase and suggest improvements",
    permission_mode="plan",
    allowed_tools=["Read", "Grep", "Glob"],
    max_turns=5
)
```

SDK 提供：
- 自动上下文管理和压缩
- 结构化输出和工具审批回调
- 会话管理和恢复
- MCP 扩展性

---

## 第十八章：内置工具清单

Claude Code 可使用的内置工具：

| 工具 | 功能 |
|------|------|
| **Read** | 读取文件内容 |
| **Write** | 创建/覆写文件 |
| **Edit** | 编辑现有文件的特定部分 |
| **Bash** | 执行 shell 命令 |
| **Glob** | 文件模式匹配搜索 |
| **Grep** | 在文件中搜索文本 |
| **Task** | 启动子代理执行任务 |
| **WebFetch** | 获取网页内容 |
| **WebSearch** | 搜索互联网 |

---

## 第十九章：输出格式详解

### 19.1 text（默认）
纯文本响应，适合人类阅读。

### 19.2 json
```json
{
  "result": "Claude 的回答文本",
  "session_id": "xxx-xxx",
  "total_cost_usd": 0.05,
  "duration_ms": 15000,
  "num_turns": 3,
  "usage": {
    "input_tokens": 5000,
    "output_tokens": 1200
  }
}
```

### 19.3 stream-json
实时流式输出，每行是一个独立 JSON 对象：
```json
{"type": "system", "subtype": "init", "session_id": "xxx"}
{"type": "assistant", "message": {...}}
{"type": "result", "subtype": "success", "result": "..."}
```

---

## 第二十章：关键文件与目录结构

```
~/.claude/
├── CLAUDE.md              ← 全局指令
├── settings.json          ← 用户级设置
├── settings.local.json    ← 本地覆盖
├── skills/                ← 全局技能
├── agents/                ← 全局子代理
├── commands/              ← 全局自定义命令
└── projects/              ← 会话历史数据

~/your-project/
├── CLAUDE.md              ← 项目指令
├── .claude/
│   ├── settings.json      ← 项目设置（可 Git 共享）
│   ├── settings.local.json ← 项目本地设置
│   ├── skills/            ← 项目技能
│   ├── agents/            ← 项目子代理
│   └── commands/          ← 项目自定义命令
└── .mcp.json              ← 项目 MCP 配置
```

---

## 附录 A：完整 CLI 参数速查

```
claude                          交互模式
claude -p "prompt"              非交互模式
claude -c                       继续上次会话
claude --resume                 恢复指定会话
claude --model opus|sonnet|haiku  选择模型
claude --permission-mode plan|acceptEdits|bypassPermissions
claude --allowedTools "tools"    限制工具
claude --max-turns N            限制轮次
claude --output-format text|json|stream-json
claude --session-id "id"        指定会话 ID
claude --append-system-prompt "..."  追加系统提示
claude --system-prompt "..."    替换系统提示
claude --agents '{...}'         定义子代理
claude --add-dir /path          添加工作目录
claude --remote "prompt"        远程云执行
claude --verbose                详细日志
claude --dangerously-skip-permissions  跳过权限（危险）
claude mcp add|remove|list      管理 MCP 服务器
```

---

## 附录 B：社区经验来源

以下是本文档整理信息时参考的真实社区资源（按类别组织）：

### 官方文档
1. **Claude Code Overview** — https://code.claude.com/docs/en/overview
2. **CLI Reference** — https://code.claude.com/docs/en/cli-reference
3. **How Claude Code Works** — https://code.claude.com/docs/en/how-claude-code-works
4. **Best Practices** — https://code.claude.com/docs/en/best-practices
5. **Extend Claude Code** — https://code.claude.com/docs/en/features-overview
6. **Skills Documentation** — https://code.claude.com/docs/en/skills
7. **Common Workflows** — https://code.claude.com/docs/en/common-workflows
8. **Headless Mode** — https://code.claude.com/docs/en/headless
9. **Settings** — https://code.claude.com/docs/en/settings
10. **Agent SDK Overview** — https://code.claude.com/docs/en/sdk/sdk-overview

### OpenClaw + Claude Code 集成实践
11. **OpenClaw Discord: Best way to use Claude Code with OpenClaw** — 社区讨论了 PTY 模式、后台进程管理、编排策略 — https://www.answeroverflow.com/m/1473453929403650209
12. **Managing OpenClaw with Claude Code (Rahul Subramaniam)** — 用 Claude Code Skills 管理 OpenClaw 配置的系统方法 — https://trilogyai.substack.com/p/managing-openclaw-with-claude-code
13. **How to Make Your OpenClaw Agent Useful and Secure (Aman Khan)** — 安全配置、记忆系统、模型选择 — https://amankhan1.substack.com/p/how-to-make-your-openclaw-agent-useful
14. **One Week with OpenClaw (Dustin Davis)** — Claude Code 用户转 OpenClaw 的实战体验 — https://dustindavis.me/blog/one-week-with-openclaw/
15. **The OpenClaw Guide (everything-claude-code repo)** — 安全分析、架构评估、tmux 持久化 — https://github.com/affaan-m/everything-claude-code/blob/main/the-openclaw-guide.md
16. **openclaw-claude-code-skill (GitHub)** — MCP 协议集成、会话管理、工具控制 — https://github.com/Enderfga/openclaw-claude-code-skill
17. **Claude Code Mastery (LobeHub Skill)** — OpenClaw 技能包：子代理编排、诊断、自改进 — https://lobehub.com/skills/openclaw-skills-claude-code-mastery
18. **Claude Code Usage Monitor (LobeHub)** — 配额监控、用量跟踪 — https://lobehub.com/skills/openclaw-skills-claude-code-usage

### 对比分析
19. **OpenClaw vs Claude Code (DataCamp)** — 功能、安全、价格全面对比 — https://www.datacamp.com/blog/openclaw-vs-claude-code
20. **OpenClaw vs Claude Code (ClaudeFast)** — 开发者视角的深度对比 — https://claudefa.st/blog/tools/extensions/openclaw-vs-claude-code
21. **OpenClaw vs Claude Code in 5 mins (Medium)** — 快速对比 — https://medium.com/@hugolu87/openclaw-vs-claude-code-in-5-mins-1cf02124bc08

### Claude Code 深度教程
22. **How I Use Every Claude Code Feature (Shrivu Shankar)** — 全功能实战评测，Master-Clone 架构 — https://blog.sshh.io/p/how-i-use-every-claude-code-feature
23. **Claude Code Customization Guide (alexop.dev)** — CLAUDE.md、Skills、Subagents、Commands 完全指南 — https://alexop.dev/posts/claude-code-customization-guide-claudemd-skills-subagents/
24. **Claude Code Explained (Medium/Avinash)** — 新手友好的概念解释 — https://avinashselvam.medium.com/claude-code-explained-claude-md-command-skill-md-hooks-subagents-e38e0815b59b
25. **How to Use Claude Code Features (ProductTalk)** — Slash Commands、Skills、Agents 实战 — https://www.producttalk.org/how-to-use-claude-code-features/
26. **Skills vs Commands vs Subagents vs Plugins (Young Leaders)** — 功能区分与架构模式 — https://www.youngleaders.tech/p/claude-skills-commands-subagents-plugins
27. **Claude Code CLI Cheatsheet (Shipyard)** — 配置、命令、最佳实践速查 — https://shipyard.build/blog/claude-code-cheat-sheet/
28. **Claude Code Commands Including Hidden Ones (DEV)** — 隐藏命令、任务列表、输出模式 — https://dev.to/akari_iku/ive-organised-the-claude-code-commands-including-some-hidden-ones-op0
29. **Claude Code Best Practice (GitHub/shanraisshan)** — 来自 Anthropic 团队成员推文的实践汇总 — https://github.com/shanraisshan/claude-code-best-practice
30. **Awesome Claude Code (GitHub)** — 技能、钩子、命令、插件的精选列表 — https://github.com/hesreallyhim/awesome-claude-code

---

*文档版本：2026-03-07 | 基于 Claude Code 最新稳定版编写*
