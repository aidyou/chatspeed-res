---
title: "confluence-mcp-server"
description: "Enables querying and retrieving content from Confluence through CQL searches and page content fetching, allowing Claude to seamlessly access information stored in Confluence workspaces."
---

# confluence-mcp-server

Enables querying and retrieving content from Confluence through CQL searches and page content fetching, allowing Claude to seamlessly access information stored in Confluence workspaces.

# Confluence Communication Server MCP Server

Interact with Confluence

This is a TypeScript-based MCP server that provides tools to interact with Confluence. It demonstrates core MCP concepts by providing:

- Tools for executing CQL queries to search pages
- Tools for retrieving the content of Confluence pages

## Features

## Confluence Tools

### `execute_cql_search`
- **Purpose**: Run a CQL query to search for Confluence pages.
- **Parameters**: `cql`, `limit` (default: 10).

### `get_page_content`
- **Purpose**: Fetch the content of a Confluence page.
- **Parameters**: `pageId`.

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
    "Confluence communication server": {
      "command": "node",
      "args": [
        "/PATH_TO_THE_PROJECT/build/index.js"
      ],
      "env": {
        "CONFLUENCE_URL": "https://XXXXXXXX.atlassian.net/wiki",
        "CONFLUENCE_API_MAIL": "Your email",
        "CONFLUENCE_API_KEY": "KEY_FROM: https://id.atlassian.com/manage-profile/security/api-tokens"
      }
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

**Official site: ** [https://github.com/KS-GEN-AI/confluence-mcp-server](https://github.com/KS-GEN-AI/confluence-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `memory`, `communication`
- Tags: `communication`, `knowledge and memory`, `search`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `node`
- Args: `/PATH_TO_THE_PROJECT/build/index.js`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/ks-gen-ai-confluence.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
