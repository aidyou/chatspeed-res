---
title: "whattimeisit-mcp"
description: "A lightweight mcp server that tells you exactly what time is it based on your IP."
---

# whattimeisit-mcp

A lightweight mcp server that tells you exactly what time is it based on your IP.

# WhatTimeIsIt MCP Server

A lightweight mcp server that tells you exactly what time is it, powered by [World Time](http://worldtimeapi.org/).

![GitHub](/mcp-assets/5816f652aa1f0cc4eedb21a2f733e09e.svg) 
![GitHub last commit](/mcp-assets/fbff8007b8fe8bc1f07f654c3f3c57ca.svg)

## Installation

1. **Clone the Repository**
```bash
   git clone https://github.com/kukapay/whattimeisit-mcp.git
```

2. **Client Configuration**
```json
    {
      "mcpServers": {
        "whattimeisit": {
          "command": "uv",
          "args": ["--directory", "path/to/whattimeisit-mcp", "run", "main.py"]
        }
      }
    }
```
   
## Usage

### MCP Tool
The server provides a single tool:
- **Tool Name**: `what_time_is_it`
- **Description**: Returns the current time string based on the your current IP.
- **Output**: A string in ISO 8601 format (e.g., `"2025-03-17T03:17:00+11:00"`).

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/kukapay/whattimeisit-mcp/blob/HEAD/LICENSE) file for details.

**Official site: ** [https://github.com/kukapay/whattimeisit-mcp](https://github.com/kukapay/whattimeisit-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `location services`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uv`
- Args: `--directory path/to/whattimeisit-mcp run main.py`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/kukapay-whattimeisit.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
