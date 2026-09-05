---
title: "答案之书"
description: "答案之书 MCP 服务 一个基于Model Context Protocol的智慧答案生成服务，为你的问题提供随机而富有哲理的答案。 来源地址 - https://github.com/liuyvan2025-art/answer-book-mcp 功能特点 - 🎯 随机生成智慧答案 - 📊 查询历史记录和统计 - 🎨 支持自定义答案 - 💾 持久化存储配置 Inspector 1. 执行：npx…"
---

# 答案之书

答案之书 MCP 服务 一个基于Model Context Protocol的智慧答案生成服务，为你的问题提供随机而富有哲理的答案。 来源地址 - https://github.com/liuyvan2025-art/answer-book-mcp 功能特点 - 🎯 随机生成智慧答案 - 📊 查询历史记录和统计 - 🎨 支持自定义答案 - 💾 持久化存储配置 Inspector 1. 执行：npx…

# 答案之书 MCP 服务

一个基于Model Context Protocol的智慧答案生成服务，为你的问题提供随机而富有哲理的答案。

## 来源地址
- https://github.com/liuyvan2025-art/answer-book-mcp

## 功能特点

- 🎯 随机生成智慧答案
- 📊 查询历史记录和统计
- 🎨 支持自定义答案
- 💾 持久化存储配置

## Inspector

1. 执行：`npx @modelcontextprotocol/inspector uvx answer-book-mcp`

## MCP服务器配置

```json
{
  "mcpServers": {
    "answer-book-mcp": {
      "args": [
        "answer-book-mcp@latest"
      ],
      "command": "uvx"
    }
  }
}
```

## API说明

- `ask_question(question: str)` - 提问获取答案
- `get_recent_history(limit: int)` - 获取历史记录
- `get_statistics()` - 获取使用统计
- `add_custom_answer(answer_text: str)` - 添加自定义答案

## 使用示例
这个MCP服务可以通过各种MCP客户端使用，比如Claude、Cursor等：

```python
# 示例对话
用户：我应该接受这个工作机会吗？
答案之书：跟随你内心的声音。

用户：这个项目能成功吗？
答案之书：风险太大，建议谨慎。

用户：查看我的历史记录
答案之书：显示最近5条提问记录
```

**官方网站：** [https://github.com/liuyvan2025-art/answer-book-mcp](https://github.com/liuyvan2025-art/answer-book-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`art and culture`, `mcp`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`answer-book-mcp@latest`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/liuyvan-answer-book.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
