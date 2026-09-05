---
title: "mcp-server-blastengine-mailer"
description: "A TypeScript-based MCP server that implements an email sending system, allowing Claude to send emails via the blastengine service."
---

# mcp-server-blastengine-mailer

A TypeScript-based MCP server that implements an email sending system, allowing Claude to send emails via the blastengine service.

# blastengine-mailer MCP Server

A Model Context Protocol server

This is a TypeScript-based MCP server that implements a sending email system.

## Features

### Tools
- `send_email` - send a email

## Development

Install dependencies:
```bash
npm install
```

Build the server:
```bash
npm run build
```

For development with auto-rebuild:
```bash
npm run watch
```

## Installation

To use with Claude Desktop, add the server config:

On MacOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
On Windows: `%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "blastengine-mailer": {
      "command": "node",
      "env": {
        "BLASTENGINE_USER_ID": "userid-of-blastengine",
        "BLASTENGINE_API_KEY": "apikey-of-blastengine"
      },
      "args": [
        "/path/to/blastengine-mailer/server.js"
      ]
    }
  }
}
```

### Debugging

Since MCP servers communicate over stdio, debugging can be challenging. We recommend using the [MCP Inspector](https://github.com/modelcontextprotocol/inspector), which is available as a package script:

```bash
npm run inspector
```

The Inspector will provide a URL to access debugging tools in your browser.

**Official site: ** [https://github.com/r3-yamauchi/mcp-server-blastengine-mailer](https://github.com/r3-yamauchi/mcp-server-blastengine-mailer)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `communication`
- Tags: `communication`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `node`
- Args: `/path/to/blastengine-mailer/server.js`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/r3-yamauchi-blastengine-mailer.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
