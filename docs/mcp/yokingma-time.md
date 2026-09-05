---
title: "time-mcp"
description: "Giving LLMs Time Awareness Capabilities. Empower your LLMs with time awareness capabilities. Access current time, convert between timezones, and get timestamps effortlessly. Enhance your applications…"
---

# time-mcp

Giving LLMs Time Awareness Capabilities. Empower your LLMs with time awareness capabilities. Access current time, convert between timezones, and get timestamps effortlessly. Enhance your applications…

# 🚀 Time MCP Server: Giving LLMs Time Awareness Capabilities

[Smithery](https://smithery.ai/server/@yokingma/time-mcp) 

 

 
 alt="Report a bug">

A Model Context Protocol (MCP) server implementation that allows LLMs to have time awareness capabilities.

 >

## Tools

- `current_time`: Get current time (UTC and local time)
- `relative_time`: Get relative time
- `get_timestamp`: Get timestamp for the time
- `days_in_month`: Get days in month
- `convert_time`: Convert time between timezones
- `get_week_year`: Get week and isoWeek of the year

## Installation

### Installing via Smithery

To install time-mcp for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@yokingma/time-mcp):

```bash
npx -y @smithery/cli install @yokingma/time-mcp --client claude
```

### Manually install (Optional)
```shell
npm install -g time-mcp
```

### using npx
```shell
npx -y time-mcp
```

## Running on Cursor

Your `mcp.json` file will look like this:

```json
{
  "mcpServers": {
    "time-mcp": {
      "command": "npx",
      "args": ["-y", "time-mcp"]
    }
  }
}
```

## Running on Windsurf

Add this to your `./codeium/windsurf/model_config.json` file:

```json
{
  "mcpServers": {
    "time-mcp": {
      "command": "npx",
      "args": ["-y", "time-mcp"]
    }
  }
}
```

## License

MIT License - see [LICENSE](https://github.com/yokingma/time-mcp/blob/HEAD/LICENSE) file for details.

**Official site: ** [https://github.com/yokingma/time-mcp](https://github.com/yokingma/time-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `productivity`
- Tags: `other`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y time-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/yokingma-time.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
