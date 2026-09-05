---
title: "fastapi_mcp"
description: "A zero-configuration tool that automatically exposes FastAPI endpoints as Model Context Protocol (MCP) tools, allowing LLM systems like Claude to interact with your API without additional coding."
---

# fastapi_mcp

A zero-configuration tool that automatically exposes FastAPI endpoints as Model Context Protocol (MCP) tools, allowing LLM systems like Claude to interact with your API without additional coding.

alt="fastapi-to-mcp" height="100"/>

FastAPI-MCP

A zero-configuration tool for automatically exposing FastAPI endpoints as Model Context Protocol (MCP) tools.

[![PyPI version](/mcp-assets/3eb159d4ab449e5582c03af5bccbf46e.svg)](https://pypi.org/project/fastapi-mcp/)
[![Python Versions](/mcp-assets/1828c31a371deac816fc5f6b8a6e3bbb.svg)](https://pypi.org/project/fastapi-mcp/)
[![FastAPI](/mcp-assets/d8d3fe385930007a18cb14a71733aa21.svg)](#)
![](/mcp-assets/096e1130aefa8ee21de38bd1147752bc.svg 'MCP Dev')

 alt="fastapi-mcp-usage" height="400"/>

## Features

- **Direct integration** - Mount an MCP server directly to your FastAPI app
- **Zero configuration** required - just point it at your FastAPI app and it works
- **Automatic discovery** of all FastAPI endpoints and conversion to MCP tools
- **Preserving schemas** of your request models and response models
- **Preserve documentation** of all your endpoints, just as it is in Swagger
- **Extend** - Add custom MCP tools alongside the auto-generated ones

## Installation

We recommend using [uv](https://docs.astral.sh/uv/), a fast Python package installer:

```bash
uv add fastapi-mcp
```

Alternatively, you can install with pip:

```bash
pip install fastapi-mcp
```

## Basic Usage

The simplest way to use FastAPI-MCP is to add an MCP server directly to your FastAPI application:

```python
from fastapi import FastAPI
from fastapi_mcp import add_mcp_server

# Your FastAPI app
app = FastAPI()

# Mount the MCP server to your app
add_mcp_server(
    app,                    # Your FastAPI app
    mount_path="/mcp",      # Where to mount the MCP server
    name="My API MCP",      # Name for the MCP server
)
```

That's it! Your auto-generated MCP server is now available at `https://app.base.url/mcp`.

## Advanced Usage

FastAPI-MCP provides several ways to customize and control how your MCP server is created and configured. Here are some advanced usage patterns:

```python
from fastapi import FastAPI
from fastapi_mcp import add_mcp_server

app = FastAPI()

mcp_server = add_mcp_server(
    app,                                    # Your FastAPI app
    mount_path="/mcp",                      # Where to mount the MCP server
    name="My API MCP",                      # Name for the MCP server
    describe_all_responses=True,            # False by default. Include all possible response schemas in tool descriptions, instead of just the successful response.
    describe_full_response_schema=True      # False by default. Include full JSON schema in tool descriptions, instead of just an LLM-friendly response example.
)

# Optionally add custom tools in addition to existing APIs.
@mcp_server.tool()
async def get_server_time() -> str:
    """Get the current server time."""
    from datetime import datetime
    return datetime.now().isoformat()
```

## Examples

See the examples directory for complete examples.

## Connecting to the MCP Server using SSE

Once your FastAPI app with MCP integration is running, you can connect to it with any MCP client supporting SSE, such as Cursor:

1. Run your application.

2. In Cursor -> Settings -> MCP, use the URL of your MCP server endpoint (e.g., `http://localhost:8000/mcp`) as sse.

3. Cursor will discover all available tools and resources automatically.

## Connecting to the MCP Server using [mcp-proxy stdio](https://github.com/sparfenyuk/mcp-proxy?tab=readme-ov-file#1-stdio-to-sse) 

If your MCP client does not support SSE, for example Claude Desktop: 

1. Run your application.

2. Install [mcp-proxy](https://github.com/sparfenyuk/mcp-proxy?tab=readme-ov-file#installing-via-pypi), for example: `uv tool install mcp-proxy`.

3. Add in Claude Desktop MCP config file (`claude_desktop_config.json`):

On Windows:
```json
{
  "mcpServers": {
    "my-api-mcp-proxy": {
        "command": "mcp-proxy",
        "args": ["http://127.0.0.1:8000/mcp"]
    }
  }
}
```
On MacOS: 
```json
{
  "mcpServers": {
    "my-api-mcp-proxy": {
        "command": "/Full/Path/To/Your/Executable/mcp-proxy",
        "args": ["http://127.0.0.1:8000/mcp"]
    }
  }
}
```
Find the path to mcp-proxy by running in Terminal: `which mcp-proxy`.

4. Claude Desktop will discover all available tools and resources automatically

## Development and Contributing

Thank you for considering contributing to FastAPI-MCP open source projects! It’s people like you that make it a reality for users in our community.

Before you get started, please see [CONTRIBUTING.md](https://github.com/tadata-org/fastapi_mcp/blob/HEAD/CONTRIBUTING.md).

## Community

Join [MCParty Slack community](https://join.slack.com/t/themcparty/shared_invite/zt-30yxr1zdi-2FG~XjBA0xIgYSYuKe7~Xg) to connect with other MCP enthusiasts, ask questions, and share your experiences with FastAPI-MCP.

## Requirements

- Python 3.10+
- uv

## License

MIT License. Copyright (c) 2024 Tadata Inc.

## About

Developed and maintained by [Tadata Inc.](https://github.com/tadata-org)

**Official site: ** [https://github.com/tadata-org/fastapi_mcp](https://github.com/tadata-org/fastapi_mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `developer tools`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `mcp-proxy`
- Args: `http://127.0.0.1:8000/mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/tadata-org-fastapi.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
