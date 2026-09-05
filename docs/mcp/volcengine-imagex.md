---
title: "mcp-imagex"
description: "Volcengine ImageX MCP is a Model Context Protocol (MCP) Server implementation for Volcengine ImageX. It integrates Volcengine services into the LLM context, enabling large models to upload and process…"
---

# mcp-imagex

Volcengine ImageX MCP is a Model Context Protocol (MCP) Server implementation for Volcengine ImageX. It integrates Volcengine services into the LLM context, enabling large models to upload and process…

# Volcengine ImageX MCP

[Volcengine ImageX](https://t.zijieimg.com/MIURnXrQfvU/) Model Context Protocol (MCP) Server implementation

## Project Introduction

Volcengine ImageX MCP is an MCP-server based on the [Model Context Protocol](https://github.com/modelcontextprotocol/python-sdk).
It integrates Volcengine services into the LLM context, enabling large models to upload and process image resources directly.

## Features

- Provides multiple resource access interfaces so LLMs can get veImageX service information, image resources, etc.
- Implements tool wrappers for multiple veImageX features, including image resource management, text-to-image, AIGC quality repair, quality evaluation, and common usage/quality query capabilities
- Provides multiple predefined prompt templates to help LLMs better understand and use veImageX features

## Installation

### Requirements

- Python 3.11+
- [Volcengine account and AccessKey/SecretKey](https://console.volcengine.cn/imagex)

## Usage

Configure the MCP service in the MCP client. The MCP JSON configuration:

```json
{
  "mcpServers": {
    "volcengine": {
      "disabled": false,
      "command": "uvx",
      "args": ["veimagex-mcp"],
      "env": {
        "VOLCENGINE_ACCESS_KEY": "Your Volcengine AK",
        "VOLCENGINE_SECRET_KEY": "Your Volcengine SK",
        "SERVICE_ID": "Your Service ID",
        "DOMAIN": "Your Domain"
      }
    }
  }
}
```

**Official site: ** [https://github.com/volcengine/mcp-imagex](https://github.com/volcengine/mcp-imagex)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `art and culture`, `aigc`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `veimagex-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/volcengine-imagex.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
