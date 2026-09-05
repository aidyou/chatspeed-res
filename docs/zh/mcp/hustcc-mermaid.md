---
title: "Mermaid MCP"
description: "使用AI MCP动态生成Mermaid图表。支持所有Mermaid功能、背景颜色和主题配置，并可以导出为png、svg和mermaid格式。"
---

# Mermaid MCP

使用AI MCP动态生成Mermaid图表。支持所有Mermaid功能、背景颜色和主题配置，并可以导出为png、svg和mermaid格式。

# 
 MCP Mermaid ![](/mcp-assets/c1486b4e2d8cfd67ed0257afeefda188.svg 'MCP Server')  [![build](/mcp-assets/028e5ab54615f767fa595703c0ea8476.svg)](https://github.com/hustcc/mcp-mermaid/actions/workflows/build.yml) [![npm Version](/mcp-assets/bd2769ecb427064450e03819af05aed2.svg)](https://www.npmjs.com/package/mcp-mermaid) [Smithery](https://smithery.ai/server/@hustcc/mcp-mermaid) [![npm License](/mcp-assets/5816f652aa1f0cc4eedb21a2f733e09e.svg)](https://www.npmjs.com/package/mcp-mermaid)

使用AI MCP动态生成
 [mermaid](https://mermaid.js.org/)图表。您还可以使用
 [mcp-server-chart](https://github.com/antvis/mcp-server-chart)来生成图表、图形和地图。

## ✨ 特性

- 完全支持`Mermaid`的所有特性和语法。
- 支持配置`backgroundColor`和`theme`，使大型AI模型能够输出丰富的样式配置。
- 支持导出为`png`、`svg`和`mermaid`格式，并对`Mermaid`进行验证，以方便模型多轮输出正确的语法和图形。

## 🤖 使用方法

与`Desktop APP`（如Claude, VSCode, Cline, Cherry Studio等）一起使用时，请添加以下MCP服务器配置。在Mac系统上：

```json

{

  "mcpServers": {

    "mcp-mermaid": {

      "command": "npx",

      "args": [

        "-y",

        "mcp-mermaid"

      ]

    }

  }

}

```
在Windows系统上：

```json

{

  "mcpServers": {

    "mcp-mermaid": {

      "command": "cmd",

      "args": [

        "/c",

        "npx",

        "-y",

        "mcp-mermaid"

      ]

    }

  }

}

```
您也可以通过HTTP或SSE协议在阿里云、modelscope、glama.ai、smithery.ai或其他平台上使用它。

## 🚰 通过SSE或可流式传输运行

全局安装包。

```bash

npm install -g mcp-mermaid

```
使用您偏好的传输选项运行服务器：

```bash

# For SSE transport (default endpoint: /sse)

mcp-mermaid -t sse

# For Streamable transport with custom endpoint

mcp-mermaid -t streamable

```
然后您可以访问服务器：
- SSE传输: `http://localhost:3033/sse`
- 可流式传输: `http://localhost:3033/mcp`

## 🎮 CLI选项

运行MCP服务器时，您还可以使用以下CLI选项。通过运行带有`-h`的CLI命令查看选项。

```plain

MCP Mermaid CLI

Options:

  --transport, -t  Specify the transport protocol: "stdio", "sse", or "streamable" (default: "stdio")

  --port, -p       Specify the port for SSE or streamable transport (default: 3033)

  --endpoint, -e   Specify the endpoint for the transport:

                    - For SSE: default is "/sse"

                    - For streamable: default is "/mcp"

  --help, -h       Show this help message

```
## 🔨 开发

安装依赖项：

```bash

npm install

```
构建服务器：

```bash

npm run build

```
启动MCP服务器：

```bash

npm run start

```
## 📄 许可证

MIT@[hustcc](https://github.com/hustcc)

**官方网站：** [https://github.com/hustcc/mcp-mermaid](https://github.com/hustcc/mcp-mermaid)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`, `mcp`, `mermaid`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y mcp-mermaid`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/hustcc-mermaid.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
