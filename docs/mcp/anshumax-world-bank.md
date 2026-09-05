---
title: "world_bank_mcp_server"
description: "Enables AI assistants to interact with the World Bank open data API, allowing for listing and analysis of indicators across available countries."
---

# world_bank_mcp_server

Enables AI assistants to interact with the World Bank open data API, allowing for listing and analysis of indicators across available countries.

# World Bank MCP Server
[Smithery](https://smithery.ai/server/@anshumax/world_bank_mcp_server)

A Model Context Protocol (MCP) server that enables interaction with the open World Bank data API. This server allows AI assistants to list indicators and analyse those indicators for the countries that are available with the World Bank.

## Features

- List available countries in the World Bank open data API
- List available indicators in the World Bank open data API
- Analyse indicators, such as population segments, poverty numbers etc, for countries
- Comprehensive logging

## Usage

### With Claude Desktop

Add this to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "world_bank": {
      "command": "uv",
      "args": [
        "--directory", 
        "path/to/world_bank_mcp_server",
        "run",
        "world_bank_mcp_server"
      ]
    }
  }
}
```

### Installing via Smithery

To install World Bank Data Server for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@anshumax/world_bank_mcp_server):

```bash
npx -y @smithery/cli install @anshumax/world_bank_mcp_server --client claude
```

**Official site: ** [https://github.com/anshumax/world_bank_mcp_server](https://github.com/anshumax/world_bank_mcp_server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `finance`, `data`
- Tags: `research and data`, `finance`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uv`
- Args: `--directory path/to/world_bank_mcp_server run world_bank_mcp_server`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/anshumax-world-bank.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
