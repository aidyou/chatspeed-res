---
title: "weather_query"
description: "Obtain weather information based on specified conditions (MCP standardized interface). Core pain point addressed: Replaces the repetitive labor of manually checking the weather, supports automation in…"
---

# weather_query

Obtain weather information based on specified conditions (MCP standardized interface). Core pain point addressed: Replaces the repetitive labor of manually checking the weather, supports automation in…

Obtain weather information based on specified conditions (MCP standardized interface).  
    Core pain point addressed: Replaces the repetitive labor of manually checking the weather, supports automation integration in multiple scenarios (such as travel guides, office reminders, agricultural alerts).

    Args:  
        location (str, required): Specific city/region (e.g., "Chaoyang District, Beijing", "Paris"), needs to be specified at the city level;  
        time_range (str, optional): Time range, possible values are ["Real-time", "Next 1 day", "Next 3 days"], default is "Real-time";  
        need_type (str, optional): Type of requirement, possible values are ["Comprehensive", "Temperature + Precipitation", "Wind + Air quality"], default is "Comprehensive".

    Returns:  
        tuple[Dict, str]: Structured data (for MCP integration), human-readable feedback (for direct display).

**Official site: ** [https://www.modelscope.cn/studios/blackcomfortable/weather_query](https://www.modelscope.cn/studios/blackcomfortable/weather_query)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `search`
- Tags: `search`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `mcp-remote https://blackcomfortable-weather-query.ms.show/gradio_api/mcp/sse --transport sse-only`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/blackcomfortable-weather-query.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
