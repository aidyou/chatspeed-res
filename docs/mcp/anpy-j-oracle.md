---
title: "mcp-oracle"
description: "A Model Context Protocol server that enables Claude to access and interact with Oracle databases through natural language queries."
---

# mcp-oracle

A Model Context Protocol server that enables Claude to access and interact with Oracle databases through natural language queries.

# mcp-server-oracle
Model Context Protocol server to access oracle

[![Python 3.12](/mcp-assets/e1a2b83f0b6cdff8bd20352d9134afb6.svg)](https://www.python.org/downloads/release/python-3120/)
[![License: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://opensource.org/licenses/MIT)

## Demos

https://github.com/user-attachments/assets/dc4e377b-4efb-43e6-85fa-93ed852fe21f

## Quickstart

To try this in Claude Desktop app, add this to your claude config files:

```json
{
  "mcpServers": {
    "mcp-server-oracle": {
      "command": "uvx",
      "args": [
        "mcp-server-oracle"
      ],
      "env": {
        "ORACLE_CONNECTION_STRING": "username/password@hostname:password/service_name"
      }
    }
  }
}
```

### Prerequisites

- UV (pacakge manager)
- Python 3.12+
- Claude Desktop

### Installation

#### Claude Desktop Configuration

Add the server configuration to your Claude Desktop config file:

**MacOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`  
**Windows**: `%APPDATA%/Claude/claude_desktop_config.json`

## Contributing

1. Fork the repository from [mcp-server-oracle](https://github.com/hdcola/mcp-server-oracle)
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/anpy-j/mcp-oracle/blob/HEAD/LICENSE) file for details.

**Official site: ** [https://github.com/anpy-j/mcp-oracle](https://github.com/anpy-j/mcp-oracle)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `search`
- Tags: `databases`, `search`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `mcp-server-oracle`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/anpy-j-oracle.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
