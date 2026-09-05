---
title: "slidev-mcp"
description: "Let AI help you easily create professional slide presentations!"
---

# slidev-mcp

Let AI help you easily create professional slide presentations!

## Project Introduction

slidev-mcp is an intelligent slide generation tool based on [Slidev](https://github.com/slidevjs/slidev). By integrating large language model technology, users only need to describe their requirements briefly to automatically generate professional online PPT presentations.

**Core value**:
- Significantly lowers the barrier to using Slidev
- Create slides interactively with natural language
- Automatically generate professional-grade presentations

## Demo Video

The video below shows the basic flow of creating a Slidev project with the MCP tools:

## Quick Start

For detailed setup and usage instructions, see the [Quick Start Guide](https://github.com/LSTM-Kirigaya/slidev-mcp/blob/main/docs/quickstart.zh.md).

## Available Tools

The MCP server provides the following tools for slide creation and management:

### Environment & Project Management

| Tool | Input parameters | Output | Purpose |
|---------|---------|---------|------|
| `check_environment` | none | environment status and version info | verify dependencies are installed |
| `create_slidev` | `path` (string), `title` (string), `author` (string) | project creation status and path | initialize a new Slidev project |
| `load_slidev` | `path` (string) | project content and slide data | load an existing presentation |

### Slide Content Management

| Tool | Input parameters | Output | Purpose |
|---------|---------|---------|------|
| `make_cover` | `title` (string), `subtitle` (string, optional), `author` (string, optional), `background` (string, optional), `python_string_template` (string, optional) | cover creation status | create/update the cover page |
| `add_page` | `content` (string), `layout` (string, optional) | new slide index | add a new slide to the presentation |
| `set_page` | `index` (integer), `content` (string), `layout` (string, optional) | update status | modify existing slide content |
| `get_page` | `index` (integer) | slide content in Markdown format | get the content of a specific slide |

### Utility Tools

| Tool | Input parameters | Output | Purpose |
|---------|---------|---------|------|
| `websearch` | `url` (string) | extracted Markdown text | collect slide content from the web |
| `get_slidev_usage` | none | Slidev layout guide and templates | provide layout documentation reference |
| `start_slidev` | none | server startup command string | start the presentation server |

### AI Assistant

| Tool | Input parameters | Output | Purpose |
|---------|---------|---------|------|
| `guide` | none | system prompt | guide the AI to use the tools effectively |

> **Note**: `optional` = optional parameter

## License

MIT License (c) 2023 [LSTM-Kirigaya](https://github.com/LSTM-Kirigaya)

**Official site: ** [https://github.com/LSTM-Kirigaya/slidev-mcp](https://github.com/LSTM-Kirigaya/slidev-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `developer tools`, `entertainment and media`, `research and data`, `slidev`, `幻灯片`, `markdown`

## MCP Configuration

- Transport: `stdio`
- Command: `uv`
- Args: `--directory <REPLACE_WITH_YOUR_SLIDEV_MCP_PATH> run servers\themes\academic\server.py`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/peacesheep-slidev.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
