---
title: "wuwa-mcp-server"
description: "A MCP server providing information on Wuthering Waves characters, team compositions, Echoes, and guides Data sourced from community."
---

# wuwa-mcp-server

A MCP server providing information on Wuthering Waves characters, team compositions, Echoes, and guides Data sourced from community.

# Wuthering Waves MCP Server

[Smithery](https://smithery.ai/server/@jacksmith3888/wuwa-mcp-server)

A Model Context Protocol (MCP) server for retrieving character and echo information from the game *Wuthering Waves* and returning it in Markdown format, optimized for use by large language models.

## Features

- **Character Information Query**: Retrieve detailed information about characters in *Wuthering Waves*
- **Echo Information Query**: Retrieve detailed information about echo sets in *Wuthering Waves*
- **Character Profile Query**: Retrieve profile information about characters in *Wuthering Waves*
- **LLM-Friendly Output**: Results are formatted specifically for optimization with large language models

## Installation Methods

### Install via Smithery

To automatically install WuWa MCP Server via [Smithery](https://smithery.ai/server/@jason/wuwa-mcp-server):

```bash
npx -y @smithery/cli@latest install @jacksmith3888/wuwa-mcp-server --client claude --key YOUR_SMITHERY_KEYs
```

### Install via `uv`

Install directly from PyPI:

```bash
uv pip install wuwa-mcp-server
```

## Usage

### Running with Cherry Studio

1. Download [Cherry Studio](https://github.com/CherryHQ/cherry-studio)
2. Click on MCP Server in the settings

Add the following configuration:

```json
{
  "mcpServers": {
    "wuwa-mcp": {
      "command": "uvx",
      "args": ["wuwa-mcp-server"]
    }
  }
}
```

### Running with Claude Desktop

1. Download [Claude Desktop](https://claude.ai/download)
2. Create or edit your Claude Desktop configuration file:
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`

Add the following configuration:

```json
{
  "mcpServers": {
    "wuwa-mcp": {
      "command": "uvx",
      "args": ["wuwa-mcp-server"]
    }
  }
}
```

3. Restart Claude Desktop

## Available Tools

### 1. Character Information Tool

```python
async def get_character_info(character_name: str) -> str
```

Queries detailed character information on the database block and returns it in Markdown format.

**Parameters:**

- `character_name`: The Chinese name of the character to query

**Returns:**
A Markdown string containing the character information, or an error message if the character is not found or data retrieval fails.

### 2. Echo Information Tool

```python
async def get_artifact_info(artifact_name: str) -> str
```

Queries detailed echo information on the database block and returns it in Markdown format.

**Parameters:**

- `artifact_name`: The Chinese name of the echo set to query

**Returns:**
A Markdown string containing the echo information, or an error message if the echo is not found or data retrieval fails.

### 3. Character Profile Tool

```python
async def get_character_profile(character_name: str) -> str
```

Queries character profile information on the database block and returns it in Markdown format.

**Parameters:**

- `character_name`: The Chinese name of the character to query

**Returns:**
A Markdown string containing the character profile information, or an error message if the character is not found or data retrieval fails.

## Detailed Features

### Result Processing

- Cleans and formats database block data
- Optimizes format for LLM consumption

## Contribution

Issues and pull requests are welcome! Some potential areas for improvement:

- Add support for more *Wuthering Waves* game content
- Enhance content parsing options
- Add a caching layer for frequently accessed content

## License

This project is licensed under the MIT License.

**Official site: ** [https://github.com/jacksmith3888/wuwa-mcp-server](https://github.com/jacksmith3888/wuwa-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `entertainment and media`, `search`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `wuwa-mcp-server`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/jacksmith3888-wuwa.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
