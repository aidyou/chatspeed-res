---
title: "hefeng-mcp-weather"
description: "Provides weather forecast data for locations in China using the HeFeng Weather API, with real-time, hourly, or daily forecasts and location-based queries."
---

# hefeng-mcp-weather

Provides weather forecast data for locations in China using the HeFeng Weather API, with real-time, hourly, or daily forecasts and location-based queries.

# HeFeng Weather MCP Server

A Model Context Protocol server that provides weather forecast data for locations in China through HeFeng Weather API.

## Features

- Get real-time weather data
- Get hourly weather forecast (24h/72h/168h)
- Get daily weather forecast (3d/7d/10d/15d/30d)
- Support location query by longitude and latitude coordinates
- Full Chinese weather description

## API

This MCP server provides the following tool:

### get-weather

Get weather forecast data for a specific location.

# Usage with MCP Host(eg. Claude Desktop)

Add this to your claude_desktop_config.json

## NPX

```json
{
  "mcpServers": {
    "hefeng-weather": {
      "command": "npx",
      "args": ["hefeng-mcp-weather@latest", "--apiKey=${API_KEY}"]
    }
  }
}
```

# License

This MCP server is licensed under the MIT License. This means you are free to use, modify, and distribute the software, subject to the terms and conditions of the MIT License. For more details, please see the LICENSE file in the project repository.

**Official site: ** [https://github.com/shanggqm/hefeng-mcp-weather](https://github.com/shanggqm/hefeng-mcp-weather)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `location services`, `travel and transportation`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `hefeng-mcp-weather@latest --apiKey=${API_KEY}`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/shanggqm-hefeng-weather.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
