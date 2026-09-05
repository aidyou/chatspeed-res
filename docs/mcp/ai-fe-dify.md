---
title: "dify-mcp-server"
description: "Integrates Dify AI API to provide code generation for Ant Design components, supporting both text and image inputs with stream processing capabilities."
---

# dify-mcp-server

Integrates Dify AI API to provide code generation for Ant Design components, supporting both text and image inputs with stream processing capabilities.

# dify-server MCP Server

An MCP server that integrates the Dify AI API

This is a TypeScript-based MCP server that provides Ant Design business component code generation by integrating the Dify AI API. It demonstrates the following core MCP concepts:

- Integrates the Dify AI API to implement chat completion
- Supports both text and image inputs
- Streaming response handling

## Features

### Tools

- `antd-component-codegen-mcp-tool` - generates Ant Design business component code
  - Supports text and optional image inputs
  - Handles image file uploads
  - Supports streaming responses from the Dify AI API

## Development Guide

Install dependencies:

```bash
npm install
```

Development mode (automatic rebuild):

```bash
npm run watch
```

Build the server:

```bash
npm run build
```

## Installation

### Integrating with Continue

Add the following configuration to `~/.continue/config.json`:

```json
{
  "experimental": {
    "modelContextProtocolServers": [
      {
        "transport": {
          "type": "stdio",
          "command": "node",
          "args": ["your/path/dify-server/build/index.js"],
          "env": {
            "DIFY_API_KEY": "***"
          }
        }
      }
    ]
  }
}
```

### Integrating with Cline

Add the following configuration to `your/path/cline_mcp_settings.json`:

```json
{
  "mcpServers": {
    "dify-server": {
      "command": "node",
      "args": ["your/path/dify-server/build/index.js"],
      "env": {
        "DIFY_API_KEY": "***"
      }
    }
  }
}
```

### Debugging

Since the MCP server communicates through standard input/output (stdio), debugging can be tricky. We recommend using [MCP Inspector](https://github.com/modelcontextprotocol/inspector), which you can start with:

```bash
npm run inspector
```

The Inspector provides a debugging tool URL accessible in the browser.

**Official site: ** [https://github.com/AI-FE/dify-mcp-server](https://github.com/AI-FE/dify-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`, `media`
- Tags: `developer tools`, `image and video processing`, `other`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `node`
- Args: `your/path/dify-server/build/index.js`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/ai-fe-dify.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
