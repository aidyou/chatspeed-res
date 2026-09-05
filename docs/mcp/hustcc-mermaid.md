---
title: "mcp-mermaid"
description: "MCP Mermaid Generate mermaid diagram and chart with AI MCP dynamically. Also you can use mcp-server-chart to generate chart, graph, map."
---

# mcp-mermaid

MCP Mermaid Generate mermaid diagram and chart with AI MCP dynamically. Also you can use mcp-server-chart to generate chart, graph, map.

# 
 MCP Mermaid ![](/mcp-assets/c1486b4e2d8cfd67ed0257afeefda188.svg 'MCP Server')  [![build](/mcp-assets/028e5ab54615f767fa595703c0ea8476.svg)](https://github.com/hustcc/mcp-mermaid/actions/workflows/build.yml) [![npm Version](/mcp-assets/bd2769ecb427064450e03819af05aed2.svg)](https://www.npmjs.com/package/mcp-mermaid) [Smithery](https://smithery.ai/server/@hustcc/mcp-mermaid) [![npm License](/mcp-assets/5816f652aa1f0cc4eedb21a2f733e09e.svg)](https://www.npmjs.com/package/mcp-mermaid)

Generate 
 [mermaid](https://mermaid.js.org/) diagram and chart with AI MCP dynamically. Also you can use 
 [mcp-server-chart](https://github.com/antvis/mcp-server-chart) to generate chart, graph, map.

## ✨ Features

- Fully support all features and syntax of `Mermaid`.
- Support configuration of `backgroundColor` and `theme`, enabling large AI models to output rich style configurations.
- Support exporting to `png`, `svg`, and `mermaid` formats, with validation for `Mermaid` to facilitate the model's multi-round output of correct syntax and graphics.

## 🤖 Usage

To use with `Desktop APP`, such as Claude, VSCode, Cline, Cherry Studio, and so on, add the  MCP server config below. On Mac system:

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

On Window system:

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

Also, you can use it on aliyun, modelscope, glama.ai, smithery.ai or others with HTTP, SSE Protocol.

## 🚰 Run with SSE or Streamable transport

Install the package globally.

```bash
npm install -g mcp-mermaid
```

Run the server with your preferred transport option:

```bash
# For SSE transport (default endpoint: /sse)
mcp-mermaid -t sse

# For Streamable transport with custom endpoint
mcp-mermaid -t streamable
```

Then you can access the server at:
- SSE transport: `http://localhost:3033/sse`
- Streamable transport: `http://localhost:3033/mcp`

## 🎮 CLI Options

You can also use the following CLI options when running the MCP server. Command options by run cli with `-h`.

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

**Official site: ** [https://github.com/hustcc/mcp-mermaid](https://github.com/hustcc/mcp-mermaid)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `developer tools`, `mcp`, `mermaid`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y mcp-mermaid`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/hustcc-mermaid.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
