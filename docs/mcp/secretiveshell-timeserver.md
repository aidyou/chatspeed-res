---
title: "MCP-timeserver"
description: "Access the time in any timezone and get the current local time"
---

# MCP-timeserver

Access the time in any timezone and get the current local time

# MCP-timeserver

A simple MCP server that exposes datetime information to agentic systems and chat REPLs

## Components

### Resources

The server implements a simple datetime:// URI scheme for accessing the current date/time in a given timezone, for example:
```
datetime://Africa/Freetown/now
datetime://Europe/London/now
datetime://America/New_York/now
```

### Tools

The server exposes a tool to get the current local time in the system timezone:
```python
>>> get_current_time()
"The current time is 2024-12-18 19:59:36"
```

## Quickstart

### Install

use the following json

```json
{
  "mcpServers": {
    "MCP-timeserver": {
      "command": "uvx",
      "args": ["MCP-timeserver"]
    }
  }
}
```

**Official site: ** [https://github.com/SecretiveShell/MCP-timeserver](https://github.com/SecretiveShell/MCP-timeserver)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `productivity`
- Tags: `other`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `MCP-timeserver`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/secretiveshell-timeserver.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
