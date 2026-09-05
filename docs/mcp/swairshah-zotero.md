---
title: "zotero-mcp-server"
description: "A server that enables MCP clients like Anthropic Claude App to interact with local Zotero libraries, allowing users to search papers, manage notes, and access research materials through natural langua…"
---

# zotero-mcp-server

A server that enables MCP clients like Anthropic Claude App to interact with local Zotero libraries, allowing users to search papers, manage notes, and access research materials through natural langua…

# Zotero MCP Server

A MCP (Model Context Protocol) server to let your MCP clients (e.g. Anthropic Claude App, Goose, possibly vscode Cline too) interact with your local Zotero repository. This server enables programmatic access to your Zotero library, allowing you to search papers, manage notes, and more.

## Setup

1. Install dependencies:
```bash
pip install -e .
```

2. Create a `.env` file in the root directory with your Zotero credentials:
```bash
ZOTERO_API_KEY=your_api_key_here
ZOTERO_USER_ID=your_user_id_here
```

You can get your Zotero API key and user ID from [Zotero's settings page](https://www.zotero.org/settings/keys).

## Integration with Anthropic Desktop App

To integrate with the Anthropic Desktop app, add the following configuration to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "zotero-mcp-server": {
      "command": "uv",
      "args": [
        "--directory",
        "/Users/swairshah/work/research/zotero-mcp",
        "run",
        "python",
        "-m",
        "zotero_mcp.server"
      ]
    }
  }
}
```
If this gives an error like
```
{"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"claude-ai","version":"0.1.0"}},"jsonrpc":"2.0","id":0}
  error: unexpected argument '--directory' found
```
Then use the following config, make sure to do `uv venv`; `source .venv/bin/activate`; `uv pip install ".[dev]"` to make sure the server can be run with all dependencies. 

```json
{
   "mcpServers": {
      "zotero-mcp-server": {
        "command": "bash",
        "args": [
          "-c",
          "cd /Users/shahswai/personal/zotero-mcp-server && source .venv/bin/activate && python -m zotero_mcp.server"
        ]
      }
    }
  }
```

## Example Usage

The server allows you to:
- Search papers by tags
- Get paper details and attached notes
- Add notes to papers
- Request paper summaries

**Official site: ** [https://github.com/swairshah/zotero-mcp-server](https://github.com/swairshah/zotero-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `research and data`, `note taking`, `search`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uv`
- Args: `--directory /Users/swairshah/work/research/zotero-mcp run python -m zotero_mcp.server`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/swairshah-zotero.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
