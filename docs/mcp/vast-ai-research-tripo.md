---
title: "tripo-mcp"
description: "Provides an interface between AI assistants and Tripo AI via Model Context Protocol, enabling generation of 3D assets from natural language and importing them to Blender."
---

# tripo-mcp

Provides an interface between AI assistants and Tripo AI via Model Context Protocol, enabling generation of 3D assets from natural language and importing them to Blender.

# Tripo MCP Server

Tripo MCP provides an interface between AI assistants and [Tripo AI](https://www.tripo3d.ai) via [Model Context Protocol (MCP)](https://github.com/anthropics/anthropic-cookbook/tree/main/mcp). 

> **Note:** This project is in alpha. Currently, it supports Tripo Blender Addon integration.

## Current Features

- Generate 3D asset from natural language using Tripo's API and import to Blender
- Compatible with Claude and other MCP-enabled AI assistants

## Quick Start

### Prerequisites
- Python 3.10+
- [Blender](https://www.blender.org/download/)
- [Tripo AI Blender Addon](https://www.tripo3d.ai/app/home)
- Claude for Desktop or Cursor IDE

### Installation

1. Install Tripo AI Blender Addon from [Tripo AI's website](https://www.tripo3d.ai/app/home)

2. Configure the MCP server in Claude Desktop or Cursor.

3. Happy creating in 3D! E.g., "Generate a 3D model of a futuristic chair".

## Acknowledgements

- **[Tripo AI](https://www.tripo3d.ai)**
- **[blender-mcp](https://github.com/ahujasid/blender-mcp)** by [Siddharth Ahuja](https://github.com/ahujasid)

**Special Thanks**  
Special thanks to Siddharth Ahuja for the blender-mcp project, which provided inspiring ideas for MCP + 3D.

**Official site: ** [https://github.com/VAST-AI-Research/tripo-mcp](https://github.com/VAST-AI-Research/tripo-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `art and culture`, `image and video processing`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `tripo-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/vast-ai-research-tripo.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
