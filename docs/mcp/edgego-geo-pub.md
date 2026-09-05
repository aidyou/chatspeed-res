---
title: "mcp-geo-pub"
description: "Integrates EdgeOne Pages Functions with large language models to retrieve and utilize user geolocation information through the Model Context Protocol (MCP)."
---

# mcp-geo-pub

Integrates EdgeOne Pages Functions with large language models to retrieve and utilize user geolocation information through the Model Context Protocol (MCP).

# MCP with Pages Functions ：Geo Location Demo 

This project demonstrates how to use EdgeOne Pages Functions to retrieve user geolocation information and integrate it with large language models through MCP (Model Context Protocol).

## Demo

![](/mcp-assets/67f6315167cad0d50116e51ef937c048.gif)

## Deploy

[![Deploy with EdgeOne Pages](/mcp-assets/0e43c38e86c821a6cca6f1708caf1c7c.svg)](https://edgeone.ai/pages/new?template=mcp-geo)

More Templates: [EdgeOne Pages](https://edgeone.ai/pages/templates)

## Components

### 1. EdgeOne Pages Functions: Geolocation

The project includes an EdgeOne Pages Function that retrieves user geolocation information:

* Uses the EdgeOne request context to access geolocation data
* Returns location information in a JSON format
* Located in `functions/get_geo.ts`

### 2. MCP Server Integration

The MCP server component provides an interface for large language models to access geolocation data:

* Implements the Model Context Protocol (MCP)
* Exposes a `get_geolocation` tool that can be used by AI models
* Uses the EdgeOne Pages Function to fetch geolocation data
* Located in `mcp-server/index.ts`

## MCP Configuration

To use the MCP server with large language models, add the following configuration:

```json
{
  "mcpServers": {
    "edgeone-geo-mcp-server": {
      "command": "tsx",
      "args": ["path/to/mcp-server/index.ts"]
    }
  }
}
```

## Learn More

* [EdgeOne Pages](https://edgeone.ai/products/pages)
* [EdgeOne Pages Functions documentation](https://edgeone.ai/document/162227908259442688)
* [Model Context Protocol (MCP)](https://modelcontextprotocol.github.io) - Learn about integrating AI models with external tools and services

**Official site: ** [https://github.com/edgego/mcp-geo-pub](https://github.com/edgego/mcp-geo-pub)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `location services`, `rag systems`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `tsx`
- Args: `path/to/mcp-server/index.ts`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/edgego-geo-pub.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
