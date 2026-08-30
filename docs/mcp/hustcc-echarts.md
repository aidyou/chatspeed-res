---
title: "ECharts 图表可视化 MCP"
description: "使用AI MCP动态生成Apache ECharts图表。支持所有ECharts功能，导出为png、svg和option格式，轻量且安全。"
---

# ECharts 图表可视化 MCP

使用AI MCP动态生成Apache ECharts图表。支持所有ECharts功能，导出为png、svg和option格式，轻量且安全。

# MCP ECharts

![](/mcp-assets/c1486b4e2d8cfd67ed0257afeefda188.svg 'MCP Server')

使用AI MCP动态生成[Apache ECharts](https://echarts.apache.org/)图表和图形。用于图表生成和数据分析。

  

## ✨ 特性

- 完全支持`ECharts`的所有特性和语法，包括数据、样式、主题等。
- 支持导出为`png`、`svg`和`option`格式，并对`ECharts`进行验证，以便模型多轮输出正确的语法和图形。
- 轻量级，可以使用`零依赖`安装。
- 极其`安全`，完全在本地生成，不依赖任何远程服务。

## 🤖 使用方法

与`桌面应用程序`一起使用，如Claude、VSCode、Cline、Cherry Studio等，添加以下MCP服务器配置。在Mac系统上：

```json

{

  "mcpServers": {

    "mcp-echarts": {

      "command": "npx",

      "args": [

        "-y",

        "mcp-echarts"

      ]

    }

  }

}

```
在Windows系统上：

```json

{

  "mcpServers": {

    "mcp-echarts": {

      "command": "cmd",

      "args": [

        "/c",

        "npx",

        "-y",

        "mcp-echarts"

      ]

    }

  }

}

```
此外，您还可以通过HTTP、SSE协议在阿里云、modelscope、glama.ai、smithery.ai或其他平台上使用它。

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

**官方网站：** [https://github.com/hustcc/mcp-echarts](https://github.com/hustcc/mcp-echarts)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y mcp-echarts`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/hustcc-echarts.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
