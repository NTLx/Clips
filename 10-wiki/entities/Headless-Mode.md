---
type: entity
title: Headless Mode
definition: "Claude Code 的非交互模式（Headless Mode）通过 -p 参数实现单次执行，输出到 stdout，适合自动化和 CI/CD 场景。"
created: 2026-04-09
updated: 2026-04-09
tags:
  - AI-Agent
  - Claude-Code
  - Automation
related_entities:
  - "[[Claude-Code-CLI]]"
  - "[[PTY-Mode]]"
  - "[[Agent-Orchestration]]"
source_raw:
  - "[[Claude code最小闭环核心文档 openclaw agent skill]]"
---

# Headless Mode

> [!definition] 定义
> Headless Mode（非交互模式）是 Claude Code 通过 `-p` 或 `--print` 参数运行的模式，实现单次执行、输出到 stdout，适合自动化脚本、CI/CD 和 OpenClaw 编排场景。

## 基本语法

```bash
# 基本用法：-p 或 --print
claude -p "分析这个项目的架构"

# 指定输出格式
claude -p "总结项目" --output-format text    # 纯文本（默认）
claude -p "总结项目" --output-format json    # JSON 带元数据
claude -p "总结项目" --output-format stream-json  # 实时流式 JSON
```

## 关键 Flags

| Flag | 用途 | 示例 |
|-----|------|------|
| `--allowedTools` | 限制工具权限（安全关键） | `--allowedTools "Read,Grep,Glob"` |
| `--max-turns` | 限制执行轮次（防止无限循环） | `--max-turns 5` |
| `--model` | 选择模型 | `--model opus` / `--model sonnet` |
| `--permission-mode` | 设置权限模式 | `--permission-mode plan` |
| `--session-id` | 保持多轮对话上下文 | `--session-id my-review-001` |
| `--output-format` | 输出格式 | `text` / `json` / `stream-json` |

## OpenClaw 调用模式

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

# 模式三：多轮会话
claude -p "分析 src/ 目录的代码" --session-id review-001
claude -p "刚才发现了什么 bug？" --session-id review-001
claude -p "修复最严重的那个 bug" --session-id review-001
```

## JSON 输出格式

使用 `--output-format json` 时，返回结构化数据：

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

## CI/CD 集成示例

```yaml
# GitHub Actions 示例
- name: Review PR
  env:
    ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
  run: |
    claude -p "Review the code changes for security issues" \
      --allowedTools Read,Grep,Glob \
      --max-turns 3 \
      --output-format json > review.json
```

## 与交互模式的对比

| 特性 | 交互模式 | Headless 模式 |
|-----|---------|--------------|
| 启动方式 | `claude` | `claude -p "..."` |
| 适用场景 | 人工操作、实时调试 | 自动化、CI/CD、编排 |
| 输出方式 | 终端交互 | stdout（可捕获） |
| 权限处理 | 实时确认 | 预配置或跳过 |

## 来源

- Raw Source: [[Claude code最小闭环核心文档 openclaw agent skill]]