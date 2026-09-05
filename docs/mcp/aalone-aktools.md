---
title: "aktools"
description: "📈 AkTools MCP Server An MCP (Model Context Protocol) server based on akshare, providing data query and analysis functions for stocks and cryptocurrencies. Features - Stock Search: Find stock codes bas…"
---

# aktools

📈 AkTools MCP Server An MCP (Model Context Protocol) server based on akshare, providing data query and analysis functions for stocks and cryptocurrencies. Features - Stock Search: Find stock codes bas…

# 📈 AkTools MCP Server

An MCP (Model Context Protocol) server based on akshare, providing data query and analysis functions for stocks and cryptocurrencies.

## Features

- **Stock Search**: Find stock codes based on keywords such as company name, stock name, etc.
- **Stock Information**: Obtain detailed information about stocks, including price, market capitalization, etc.
- **Historic Prices**: Get historical price data for stocks and cryptocurrencies, including technical analysis indicators.
- **Related News**: Access the latest news related to stocks and cryptocurrencies.
- **Financial Indicators**: Supports querying key financial report indicators for A-shares and H-shares.

## Installation

### Method 1: uvx
```yaml
{
  "mcpServers": {
    "mcp-aktools": {
      "command": "uvx",
      "args": ["mcp-aktools"]
    }
  }
}
```
### Method 2: Docker
```bash
mkdir /opt/mcp-aktools
cd /opt/mcp-aktools
wget https://raw.githubusercontent.com/aahl/mcp-aktools/refs/heads/main/docker-compose.yml
docker-compose up -d
```
```yaml
{
  "mcpServers": {
    "mcp-aktools": {
      "url": "http://0.0.0.0:8808/mcp" # Streamable HTTP
    }
  }
}
```
### One-Click Installation
- Add to Cursor [![Install MCP Server](/mcp-assets/ec1e84b0a4f6576d1ecdf0b2651745c5.svg)](https://cursor.com/zh/install-mcp?name=aktools&config=eyJjb21tYW5kIjoidXZ4IiwiYXJncyI6WyJtY3AtYWt0b29scyJdfQ%3D%3D)
- Add to VS Code [
](https://insiders.vscode.dev/redirect?url=vscode:mcp/install%3F%7B%22name%22%3A%22aktools%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22mcp-aktools%22%5D%7D)
- Add to Claude code, run command: `claude mcp add --transport stdio aktools -- uvx mcp-aktools`
- Add to OpenAI CodeX, run command: `codex mcp add aktools -- uvx mcp-aktools`

**Official site: ** [https://github.com/aahl/mcp-aktools](https://github.com/aahl/mcp-aktools)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `finance`
- Tags: `finance`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `mcp-aktools`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/aalone-aktools.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
