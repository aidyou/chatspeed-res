---
title: "bing-cn-mcp-enhanced"
description: "A Chinese Bing search tool based on the MCP (Model Context Protocol) that lets you search Bing and fetch webpage content directly through Claude or other MCP-capable AI."
---

# bing-cn-mcp-enhanced

A Chinese Bing search tool based on the MCP (Model Context Protocol) that lets you search Bing and fetch webpage content directly through Claude or other MCP-capable AI.

# Bing CN MCP Enhanced

A Chinese Bing search tool based on MCP (Model Context Protocol) that can directly search Bing and fetch web content through Claude or other AI supporting MCP. It solves the issue of random data return due to anti-scraping mechanisms, which is common in existing BingMcp search tools. However, because modelscope.cn hosting does not support playwright, only the stdio solution can be used.

## Features
- Completes Bing queries and quickly acquires content using page parsing methods
- Fixes various bugs in other Bing queries, especially the issue where Bing randomly provides data if it identifies you as a bot, leading to failed searches
- Continuously maintained; report issues via GitHub
- No API key required, directly scrapes Bing search results
- Lightweight, easy to install and use
- Supports invocation by AI tools like Claude

## Installation
Relying on playwright, it will automatically download at the start. Please ensure your machine has internet access.

### Global Installation

```bash

npm install -g bing-cn-mcp-enhanced

```
### Or run directly with npx

```bash

npx bing-cn-mcp-enhanced

```
## Usage

### Start the Server

```bash

bing-cn-mcp-enhanced

```
Or use npx:

```bash

npx bing-cn-mcp-enhanced

```
### Use in MCP Supported Environments

In an environment that supports MCP (such as Cursor), configure the MCP server to use it:

1. Locate the MCP configuration file (e.g., `.cursor/mcp.json`)
2. Add the server configuration:

```json

{

  "mcpServers": {

    "EnhancedBing": {

      "args": [

        "bing-cn-mcp-enhanced"

      ],

      "command": "npx"

    }

  }

}

```
Configuration for Windows users

```json

{

  "mcpServers": {

    "EnhancedBing": {

        "command": "cmd",

        "args": [

          "/c",

          "npx",

          "bing-cn-mcp-enhanced"

      ]

    }

  }

}

```
3. You can now use the `mcp__bing_search` and `mcp__fetch_webpage` tools in Claude

4. You can also use Lynxe to utilize this tool  [Lynxe github](https://github.com/spring-ai-alibaba/Lynxe)

### View Logs

The MCP server logs are output to stderr. If you want to save the logs to a file for viewing, you can achieve this by modifying the MCP configuration:

Logs from Lynxe can be viewed directly in the background log

## Author

Lynxe

## License

MIT

**Official site: ** [https://github.com/Lynxe-public/bing-mcp-cn-enhanced](https://github.com/Lynxe-public/bing-mcp-cn-enhanced)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `search`
- Tags: `search`, `bing mcp 持续维护 增强`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `bing-cn-mcp-enhanced`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/rainerwjy-bing-cn-enhanced.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
