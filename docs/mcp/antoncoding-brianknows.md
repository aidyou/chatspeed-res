---
title: "mcp-brianknows"
description: "An MCP server that connects Claude to BrianKnows' blockchain knowledge base, allowing users to search for blockchain/DeFi information and interact with a specialized agent across multiple knowledge ba…"
---

# mcp-brianknows

An MCP server that connects Claude to BrianKnows' blockchain knowledge base, allowing users to search for blockchain/DeFi information and interact with a specialized agent across multiple knowledge ba…

# BrianKnows MCP Server 
[Smithery](https://smithery.ai/server/@antoncoding/mcp-brianknows)

A Model Context Protocol (MCP) server that connects Claude to BrianKnows' blockchain knowledge base.

  

## What is MCP? 🤔

The Model Context Protocol (MCP) lets AI assistants like Claude Desktop connect to external tools and data sources in a secure way while keeping users in control.

## What does this server do? 🚀

The BrianKnows MCP server provides three main tools:

1. **Ping Tool**: Check if the BrianKnows API server is responsive
2. **Search Tool**: Query BrianKnows' knowledge engine for blockchain and DeFi information
3. **Agent Tool**: Chat with the BrianKnows agent about DeFi protocols

Supported knowledge bases include:
- public-knowledge-box (default)
- circle_kb, lido_kb, Polygon_kb, taiko_kb
- near_kb, clave_kb, starknet_kb, consensys_kb

The server maintains a cache of your 5 most recent searches for quick reference.

## Prerequisites 📋

- [Node.js](https://nodejs.org/) (v18 or higher)
- [Claude Desktop](https://claude.ai/download) 
- A [BrianKnows API key](https://docs.brianknows.org/)

## Configuration ⚙️

Add this to your Claude Desktop configuration file (accessible via Developer Settings):

```json
{
  "mcpServers": {
    "brianknows": {
      "command": "npx",
      "args": ["mcp-brianknows"],
      "env": {
        "BRIAN_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

Replace `your-api-key-here` with your actual BrianKnows API key.

## Example Usage 🎯

```
Can you check if the BrianKnows API is online?

Use BrianKnows to search for information about Ethereum's Layer 2 solutions.

Ask the BrianKnows agent to explain how Uniswap V3 works.
```

## Features ✨

* **Multiple Knowledge Bases**: Access specialized knowledge for different blockchain protocols
* **Cached Searches**: Quick access to your 5 most recent searches
* **Error Handling**: User-friendly error messages
* **Type Safety**: Full TypeScript implementation

## Acknowledgments 🙏

* [BrianKnows](https://brianknows.org) for their blockchain knowledge API
* [Model Context Protocol](https://modelcontextprotocol.io)
* [Anthropic](https://anthropic.com) for Claude Desktop

**Official site: ** [https://github.com/antoncoding/mcp-brianknows](https://github.com/antoncoding/mcp-brianknows)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `finance`
- Tags: `search`, `knowledge and memory`, `finance`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `mcp-brianknows`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/antoncoding-brianknows.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
