---
title: "excel-mcp-server"
description: "Provides Excel file manipulation capabilities. This server enables workbook creation, data manipulation, formatting, and advanced Excel features."
---

# excel-mcp-server

Provides Excel file manipulation capabilities. This server enables workbook creation, data manipulation, formatting, and advanced Excel features.

# Excel MCP Server

A Model Context Protocol (MCP) server that lets you manipulate Excel files without needing Microsoft Excel installed. Create, read, and modify Excel workbooks with your AI agent.

## Features

- 📊 Create and modify Excel workbooks
- 📝 Read and write data
- 🎨 Apply formatting and styles
- 📈 Create charts and visualizations
- 📊 Generate pivot tables
- 🔄 Manage worksheets and ranges

## Quick Start

### Prerequisites

- Python 3.10 or higher

### Installation

1. Clone the repository:
```bash
git clone https://github.com/haris-musa/excel-mcp-server.git
cd excel-mcp-server
```

2. Install using uv:
```bash
uv pip install -e .
```

### Running the Server

Start the server (default port 8000):
```bash
uv run excel-mcp-server
```

Custom port (e.g., 8080):

```bash
# Bash/Linux/macOS
export FASTMCP_PORT=8080 && uv run excel-mcp-server

# Windows PowerShell
$env:FASTMCP_PORT = "8080"; uv run excel-mcp-server
```

## Using with AI Tools

### Cursor IDE

1. Add this configuration to Cursor:
```json
{
  "mcpServers": {
    "excel": {
      "url": "http://localhost:8000/sse",
      "env": {
        "EXCEL_FILES_PATH": "/path/to/excel/files"
      }
    }
  }
}
```

2. The Excel tools will be available through your AI assistant.

### Remote Hosting & Transport Protocols

This server uses Server-Sent Events (SSE) transport protocol. For different use cases:

1. **Using with Claude Desktop (requires stdio):**
   - Use [Supergateway](https://github.com/supercorp-ai/supergateway) to convert SSE to stdio:

2. **Hosting Your MCP Server:**
   - [Remote MCP Server Guide](https://developers.cloudflare.com/agents/guides/remote-mcp-server/)

## Environment Variables

- `FASTMCP_PORT`: Server port (default: 8000)
- `EXCEL_FILES_PATH`: Directory for Excel files (default: `./excel_files`)

## Available Tools

The server provides a comprehensive set of Excel manipulation tools. See [TOOLS.md](https://github.com/haris-musa/excel-mcp-server/blob/HEAD/TOOLS.md) for complete documentation of all available tools.

## License

MIT License - see [LICENSE](https://github.com/haris-musa/excel-mcp-server/blob/HEAD/LICENSE) for details.

**Official site: ** [https://github.com/haris-musa/excel-mcp-server](https://github.com/haris-musa/excel-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `developer tools`, `databases`, `other`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `excel-mcp-server stdio`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/haris-musa-excel.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
