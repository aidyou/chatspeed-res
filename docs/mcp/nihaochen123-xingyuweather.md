---
title: "XingYuWeather"
description: "Supports precise invocation through city name / latitude and longitude, returning structured, highly available weather information, suitable for integration in various scenarios such as AI agents, app…"
---

# XingYuWeather

Supports precise invocation through city name / latitude and longitude, returning structured, highly available weather information, suitable for integration in various scenarios such as AI agents, app…

Supports precise invocation through city name / latitude and longitude, returning structured, highly available weather information, suitable for integration in various scenarios such as AI agents, application development, and IoT devices.
### Core Functions and Data Output Specifications
- **Query Dimensions**: City name (including district/county level), Latitude and Longitude coordinates (WGS84)
- **Forecast Validity Period**: Up to 5 days (including the current day), with data returned split by natural days
- **Coverage Area**: Major cities globally (supports provincial/city/district/county level precise matching in China)

**Official site: ** [https://www.modelscope.cn/studios/nihaochen123/CXY/summary](https://www.modelscope.cn/studios/nihaochen123/CXY/summary)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `search`
- Tags: `search`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `mcp-remote https://nihaochen123-cxy.ms.show/gradio_api/mcp/sse --transport sse-only`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/nihaochen123-xingyuweather.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
