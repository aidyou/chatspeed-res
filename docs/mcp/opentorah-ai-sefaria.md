---
title: "mcp-sefaria-server"
description: "Enables Large Language Models to retrieve Jewish texts and commentaries from the Sefaria library through a standardized interface."
---

# mcp-sefaria-server

Enables Large Language Models to retrieve Jewish texts and commentaries from the Sefaria library through a standardized interface.

# Sefaria Jewish Library MCP Server

[Smithery](https://smithery.ai/server/mcp-sefaria-server)
An MCP (Model Context Protocol) server that provides access to Jewish texts from the Sefaria library. This server enables Large Language Models to retrieve and reference Jewish texts through a standardized interface.

## Features

- Retrieve Jewish texts by reference
- Retrieve commentaries on a given text

## Installation

Requires Python 3.10 or higher.

### Installing via Smithery

To install Sefaria Jewish Library for Claude Desktop automatically via [Smithery](https://smithery.ai/server/mcp-sefaria-server):

```bash
npx -y @smithery/cli install mcp-sefaria-server --client claude
```

### Clone the repository
```bash
git clone https://github.com/sivan22/mcp-sefaria-server.git
cd mcp-sefaria-server
```

## Running the Server

The server can be run directly:

```bash
uv --directory path/to/directory run sefaria_jewish_library
```

Or through an MCP client that supports the Model Context Protocol.
for claude desktop app and cline you should use the following config:
```
{
  "mcpServers": {        
      "sefaria_jewish_library": {
          "command": "uv",
          "args": [
              "--directory",
              "C:/dev/mcp-sefaria-server",
              "run",
              "sefaria_jewish_library"
          ],
          "env": {
            "PYTHONIOENCODING": "utf-8" 
          }
      }
  }
}
```

## Available tools

The server provides the following tools through the MCP interface:

### get_text

Retrieves a specific Jewish text by its reference.

Example:
```
reference: "Genesis 1:1"
reference: "שמות פרק ב פסוק ג"
reference: "משנה ברכות פרק א משנה א"
```

### get_commentaries

Retrieves a list of commentaries for a given text.

Example:
```
reference: "Genesis 1:1"
reference: "שמות פרק ב פסוק ג"
reference: "משנה ברכות פרק א משנה א"
```

## Development

This project uses:
- [MCP SDK](https://github.com/modelcontextprotocol/sdk) for server implementation
- [Sefaria API](https://github.com/Sefaria/Sefaria-API) for accessing Jewish texts

## Requirements

- Python >= 3.10
- MCP SDK >= 1.1.1
- Sefaria API

## License

MIT License

**Official site: ** [https://github.com/opentorah-ai/mcp-sefaria-server](https://github.com/opentorah-ai/mcp-sefaria-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `art and culture`, `search`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uv`
- Args: `--directory C:/dev/mcp-sefaria-server run sefaria_jewish_library`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/opentorah-ai-sefaria.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
