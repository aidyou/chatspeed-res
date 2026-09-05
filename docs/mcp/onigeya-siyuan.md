---
title: "siyuan-mcp-server"
description: "An MCP server implementation that integrates with SiYuan Note system, enabling AI models to access and manipulate note data through comprehensive commands for notebook management, document operations…"
---

# siyuan-mcp-server

An MCP server implementation that integrates with SiYuan Note system, enabling AI models to access and manipulate note data through comprehensive commands for notebook management, document operations…

# SiYuan Note MCP Server
[Smithery](https://smithery.ai/server/@onigeya/siyuan-mcp-server)

An MCP server implementation that provides integration with the SiYuan Note system, enabling AI models to access and manipulate note data.

An MCP server implementation that provides integration with the SiYuan Note system, enabling AI models to access and manipulate note data.

## Features

* Notebook Management
* Document Operations
* Block Control
* File and Asset Management
* SQL Query Support
* Attribute Management
* Export and Conversion
* System Functions

## Command List

All commands support detailed documentation via the `help` command. For example:

All commands support detailed documentation via the `help` command. For example:

```json
{
  "type": "help",
  "params": {
    "type": "block.insertBlock"
  }
}
```

### Asset Management

* Upload assets

### Attribute Management

* Set block attributes
* Get block attributes

### Block Operations

* Insert a block
* Update block content
* Delete a block
* Move a block
* Get block Kramdown content

### Format Conversion

* Convert content using Pandoc

### Export Functions

* Export notebook
* Export document

### File Operations

* Get file content
* Put file content
* Remove file
* List files in directory

### File Tree Operations

* Create document with Markdown
* Rename document
* Remove document
* Move documents
* Get document HPath by path
* Get document HPath by ID

### Network Proxy

* Forward proxy request

### Notebook Management

* List all notebooks
* Open notebook
* Close notebook
* Rename notebook
* Create notebook
* Remove notebook
* Get notebook configuration
* Set notebook configuration

### Notifications

* Push message notification
* Push error message notification

### Query Functions

* Execute SQL query
* Query block by ID

### Search Functions

* Full text search

### SQL Query

* Execute SQL query

### System Functions

* Get boot progress
* Get system version
* Get current time

### Template Functions

* Render template
* Render Sprig template

## Usage

### Environment Variables

The server requires the following environment variables:
The server requires the following environment variables:

* `SIYUAN_TOKEN` - SiYuan Note API token (required)
  * Check in SiYuan Note Settings - About
  * Used for API authentication

### Using in Claude Desktop

Add the following configuration to `claude_desktop_config.json`:
Add the following configuration to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "siyuan": {
      "command": "npx",
      "args": [
        "-y",
        "@onigeya/siyuan-mcp-server"
      ],
      "env": {
        "SIYUAN_TOKEN": "your-siyuan-token"
      }
    }
  }
}
```

### Local Run

1. Install dependencies:
```bash
pnpm install
```

2. Set environment variables:
```bash
# Windows
set SIYUAN_TOKEN=your-siyuan-token

# Linux/macOS
export SIYUAN_TOKEN=your-siyuan-token
```

3. Start service:
```bash
pnpm start
```

### Docker Run

```bash
docker run --rm -i 
  -e SIYUAN_TOKEN=your-siyuan-token 
  mcp/siyuan
```

## Build

### Requirements

* Node.js >= 23.10.0
* pnpm

### Local Build

```bash
pnpm build
```

### Docker Build

```bash
docker build -t mcp/siyuan .
```

## License

This project is released under the ISC License, meaning you can freely use, modify, and distribute this software, subject to the terms and conditions of the ISC License. For details, see the LICENSE file in the project repository.

This project is released under the ISC License. This means you can freely use, modify, and distribute this software, subject to the terms and conditions of the ISC License. For detailed information, please refer to the LICENSE file in the project repository.

## Related Resources

- SiYuan Note](https://github.com/siyuan-note/siyuan)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- SiYuan Note API Documentation](https://github.com/siyuan-note/siyuan/blob/master/API.md)

**Official site: ** [https://github.com/onigeya/siyuan-mcp-server](https://github.com/onigeya/siyuan-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `memory`
- Tags: `note taking`, `knowledge and memory`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @onigeya/siyuan-mcp-server`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/onigeya-siyuan.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
