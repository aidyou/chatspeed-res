---
title: "mcp-server-flomo"
description: "A TypeScript-based MCP server to help you write notes into Flomo."
---

# mcp-server-flomo

A TypeScript-based MCP server to help you write notes into Flomo.

# mcp-server-flomo MCP Server

Writes notes to Flomo.

This is a TypeScript-based MCP server that helps you write notes to Flomo.

## Features

### Tools

- `write_note` - Writes a text note to Flomo
  - Requires content as a mandatory parameter

## Development

Install dependencies:

```bash

npm install

```
Build the server:

```bash

npm run build

```
For auto-rebuilding during development:

```bash

npm run watch

```
## Installation

To use in Claude Desktop, add the server configuration:

On MacOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
On Windows: `%APPDATA%/Claude/claude_desktop_config.json`

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
Find your Flomo_API_URL [here](https://v.flomoapp.com/mine?source=incoming_webhook)

### Debugging

Since the MCP server communicates via standard input and output, debugging can be challenging. We recommend using the [MCP Inspector](https://github.com/modelcontextprotocol/inspector), which is available as a package script:

```bash

npm run inspector

```
The inspector will provide a URL where you can access the debugging tools in your browser.

**Official site: ** [https://github.com/chatmcp/mcp-server-flomo](https://github.com/chatmcp/mcp-server-flomo)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `memory`
- Tags: `knowledge and memory`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @chatmcp/mcp-server-flomo`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/chatmcp-flomo.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
