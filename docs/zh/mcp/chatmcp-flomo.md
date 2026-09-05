---
title: "MCP Flomo笔记助手"
description: "一个基于 TypeScript 的 MCP 服务器，帮助您将笔记写入 Flomo。"
---

# MCP Flomo笔记助手

一个基于 TypeScript 的 MCP 服务器，帮助您将笔记写入 Flomo。

# 正文
# mcp-server-flomo MCP服务器

将笔记写入Flomo。

这是一个基于TypeScript的MCP服务器，可帮助您将笔记写入Flomo。

## 功能

### 工具

- `write_note` - 将文本笔记写入Flomo
  - 需要内容作为必需参数

## 开发

安装依赖项：

```bash
npm install
```

构建服务器：

```bash
npm run build
```

用于开发时自动重建：

```bash
npm run watch
```

## 安装

要在Claude桌面版中使用，请添加服务器配置：

在MacOS上：`~/Library/Application Support/Claude/claude_desktop_config.json`
在Windows上：`%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "mcp-server-flomo": {
      "command": "npx",
      "args": ["-y", "@chatmcp/mcp-server-flomo"],
      "env": {
        "FLOMO_API_URL": "https://flomoapp.com/iwh/xxx/xxx/"
      }
    }
  }
}
```

找到您的Flomo_API_URL [在此处](https://v.flomoapp.com/mine?source=incoming_webhook)

### 调试

由于MCP服务器通过标准输入输出进行通信，调试可能会具有挑战性。我们建议使用[MCP检查器](https://github.com/modelcontextprotocol/inspector)，它作为包脚本可用：

```bash
npm run inspector
```

检查器将提供一个URL，您可以在浏览器中访问调试工具。

**官方网站：** [https://github.com/chatmcp/mcp-server-flomo](https://github.com/chatmcp/mcp-server-flomo)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`memory`
- 标签：`knowledge and memory`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @chatmcp/mcp-server-flomo`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/chatmcp-flomo.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
