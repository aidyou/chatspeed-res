---
title: "FinDataMCP"
description: "An MCP server that enables Claude Desktop to access and analyze financial data through Yahoo Finance integration."
---

# FinDataMCP

An MCP server that enables Claude Desktop to access and analyze financial data through Yahoo Finance integration.

# FinDataMCP

## To run:
1. Clone repo

2. Install uv (package manager):
```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
```

3. Navigate to folder:
```bash
   cd FinDataMCP
```

3. Install dependencies:
```bash
   # Create virtual env and activate it
   uv venv
   source .venv/bin/activate

   # Install dependencies
   uv add "mcp[cli]" httpx yfinance
```

4. Check that everything s working by running server:
```bash
   uv run findata.py
```

## Connecting to Claude Desktop

1. Install [Claude Desktop](https://claude.ai/desktop) if you haven t already

2. Edit Claude Desktop configuration file (Claude>settings>developer>edit config):

3. Add the following configuration:
```json
   {
       "mcpServers": {
           "findata": {
               "command": "uv",
               "args": [
                   "--directory",
                   "/ABSOLUTE/PATH/TO/PARENT/FOLDER/FinDataMCP",
                   "run",
                   "findata.py"
               ]
           }
       }
   }
```

4. Restart Claude Desktop

For windows cmds: see https://modelcontextprotocol.io/quickstart/server

**Official site: ** [https://github.com/coreyjwang/FinDataMCP](https://github.com/coreyjwang/FinDataMCP)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `finance`
- Tags: `finance`, `rag systems`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uv`
- Args: `--directory /ABSOLUTE/PATH/TO/PARENT/FOLDER/FinDataMCP run findata.py`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/coreyjwang-findatamcp.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
