---
title: "MCP-ECharts"
description: "MCP ECharts Generate Apache ECharts diagram and chart with AI MCP dynamically. Using for chart generation and data analysis."
---

# MCP-ECharts

MCP ECharts Generate Apache ECharts diagram and chart with AI MCP dynamically. Using for chart generation and data analysis.

# MCP ECharts

![](/mcp-assets/c1486b4e2d8cfd67ed0257afeefda188.svg 'MCP Server')

Generate [Apache ECharts](https://echarts.apache.org/) diagram and chart with AI MCP dynamically. Using for chart generation and data analysis.

  

## ✨ Features

- Fully support all features and syntax of `ECharts`, include data, style, theme and so on.
- Support exporting to `png`, `svg`, and `option` formats, with validation for `ECharts` to facilitate the model's multi-round output of correct syntax and graphics.
- Lightweight, we can install it with `zero dependence`.
- Extremely `secure`, fully generated locally, without relying on any remote services.

## 🤖 Usage

To use with `Desktop APP`, such as Claude, VSCode, Cline, Cherry Studio, and so on, add the  MCP server config below. On Mac system:

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

On Window system:

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

Also, you can use it on aliyun, modelscope, glama.ai, smithery.ai or others with HTTP, SSE Protocol.

## 🔨 Development

Install dependencies:

```bash
npm install
```

Build the server:

```bash
npm run build
```

Start the MCP server:

```bash
npm run start
```

## 📄 License

MIT@[hustcc](https://github.com/hustcc).

**Official site: ** [https://github.com/hustcc/mcp-echarts](https://github.com/hustcc/mcp-echarts)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `developer tools`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y mcp-echarts`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/hustcc-echarts.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
