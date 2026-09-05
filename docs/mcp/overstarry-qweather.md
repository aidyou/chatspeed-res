---
title: "qweather-mcp"
description: "qweather mcp"
---

# qweather-mcp

qweather mcp

# qweather-mcp
[Smithery](https://smithery.ai/server/@overstarry/qweather-mcp)

MCP server for [QWeather](https://www.qweather.com/) API.

This project provides weather information query capabilities through Model Context Protocol (MCP).

## Usage

Get your API Key [here](https://console.qweather.com/).

### Installing via Smithery

To install qweather-mcp for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@overstarry/qweather-mcp):

```bash
npx -y @smithery/cli install @overstarry/qweather-mcp --client claude
```

### Configure manually

```bash
# stdio server
npx -y qweather-mcp

```

Environment variables:

```
QWEATHER_API_BASE=https://api.qweather.com
QWEATHER_API_KEY=
```

### JSON config

```json
{
  "mcpServers": {
    "qweather": {
      "command": "npx",
      "args": ["-y", "qweather-mcp"],
      "env": {
        "QWEATHER_API_BASE": "",
        "QWEATHER_API_KEY": ""
      }
    }
  }
}
```

### Available Tools

- `lookup-city`: Look up city information by name
- `get-weather-now`: Get current weather for a location

## License

MIT.

**Official site: ** [https://github.com/overstarry/qweather-mcp](https://github.com/overstarry/qweather-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `search`
- Tags: `search`, `other`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y qweather-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/overstarry-qweather.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
