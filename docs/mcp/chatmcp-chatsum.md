---
title: "MCP聊天摘要"
description: "总结你的聊天信息。"
---

# MCP聊天摘要

总结你的聊天信息。

# mcp-server-chatsum

这个MCP服务器用于总结您的聊天消息。

[中文说明](https://github.com/chatmcp/mcp-server-chatsum/blob/HEAD/README_CN.md)

> **在开始之前**
>
> 移动到[chatbot](https://github.com/chatmcp/mcp-server-chatsum/tree/HEAD/chatbot)目录，按照[README](https://github.com/chatmcp/mcp-server-chatsum/blob/HEAD/chatbot/README.md)设置聊天数据库。
>
> 启动聊天机器人以保存您的聊天消息。

## 功能

### 资源

### 工具

- `query_chat_messages` - 查询聊天消息
  - 根据给定参数查询聊天消息
  - 基于查询提示总结聊天消息

### 提示

## 开发

1. 设置环境变量：

在根目录创建`.env`文件，并设置您的聊天数据库路径。

```txt
CHAT_DB_PATH=path-to/chatbot/data/chat.db
```

2. 安装依赖项：

```bash
pnpm install
```

构建服务器：

```bash
pnpm build
```

对于带有自动重建的开发：

```bash
pnpm watch
```

## 安装

要与Claude Desktop一起使用，请添加服务器配置：

在MacOS上: `~/Library/Application Support/Claude/claude_desktop_config.json`
在Windows上: `%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "mcp-server-chatsum": {
      "command": "path-to/bin/node",
      "args": ["path-to/mcp-server-chatsum/build/index.js"],
      "env": {
        "CHAT_DB_PATH": "path-to/mcp-server-chatsum/chatbot/data/chat.db"
      }
    }
  }
}
```

### 调试

由于MCP服务器通过标准输入输出进行通信，调试可能会有些困难。我们建议使用[MCP Inspector](https://github.com/modelcontextprotocol/inspector)，它作为包脚本提供：

```bash
pnpm inspector
```

Inspector将提供一个URL，以便您在浏览器中访问调试工具。

## 社区

- [MCP Server Telegram](https://t.me/+N0gv4O9SXio2YWU1)
- [MCP Server Discord](https://discord.gg/RsYPRrnyqg)

## 关于作者

- [idoubi](https://bento.me/idoubi)

**官方网站：** [https://github.com/chatmcp/mcp-server-chatsum](https://github.com/chatmcp/mcp-server-chatsum)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`productivity`
- 标签：`other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`path-to/bin/node`
- 参数：`path-to/mcp-server-chatsum/build/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/chatmcp-chatsum.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
