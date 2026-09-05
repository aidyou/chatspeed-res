---
title: "彩云天气 MCP"
description: "Caiyun Weather MCP Server Hosted Server Caiyun Weather provides a hosted Streamable HTTP MCP server, so you can use the weather tools without installing or running this package locally. json { \"url\"…"
---

# 彩云天气 MCP

Caiyun Weather MCP Server Hosted Server Caiyun Weather provides a hosted Streamable HTTP MCP server, so you can use the weather tools without installing or running this package locally. json { "url"…

# Caiyun Weather MCP Server

## Hosted Server

Caiyun Weather provides a hosted Streamable HTTP MCP server, so you can use
the weather tools without installing or running this package locally.

```json
{
  "url": "https://mcp-weather.caiyunapp.com/mcp",
  "headers": {
    "X-Caiyun-API-Key": "YOUR_CAIYUN_WEATHER_API_KEY"
  }
}
```

The outer configuration format depends on your MCP client. Before getting
started, [register and apply for a Caiyun Weather API key](https://platform.caiyunapp.com),
then pass it in the `X-Caiyun-API-Key` request header.

## Setup Instructions

Install uv first.

MacOS/Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows:

```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Setup with Claude Desktop

```
# claude_desktop_config.json
# Can find location through:
# Hamburger Menu -> File -> Settings -> Developer -> Edit Config
{
  "mcpServers": {
    "caiyun-weather": {
      "command": "uvx",
      "args": ["mcp-caiyun-weather"],
      "env": {
        "CAIYUN_WEATHER_API_TOKEN": "YOUR_API_KEY_HERE"
      }
    }
  }
}
```

### Ask Claude a question requiring weather
e.g. "What's the weather in Beijing Now?"

## Local/Dev Setup Instructions

### Setup with Claude Desktop

```
# claude_desktop_config.json
# Can find location through:
# Hamburger Menu -> File -> Settings -> Developer -> Edit Config
{
  "mcpServers": {
    "caiyun-weather": {
      "command": "uv",
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/PARENT/FOLDER/mcp-caiyun-weather",
        "run",
        "mcp-caiyun-weather"
      ],
      "env": {
        "CAIYUN_WEATHER_API_TOKEN": "YOUR_API_TOKEN_HERE"
      }
    }
  }
}
```

### Debugging

Run:
```bash
npx @modelcontextprotocol/inspector \
      uv \
      --directory /ABSOLUTE/PATH/TO/PARENT/FOLDER/mcp-caiyun-weather \
      run \
      mcp-caiyun-weather
```

## Available Tools

- `get_realtime_weather`: Get real-time weather data for a specific location
  - Parameters:
    - `lng`: The longitude of the location
    - `lat`: The latitude of the location
  - Returns detailed information including:
    - Temperature and apparent temperature
    - Sky condition
    - Humidity
    - Wind speed and direction
    - Precipitation intensity
    - Air quality metrics (PM2.5, PM10, O3, SO2, NO2, CO)
    - AQI (China and USA standards)
    - Life indices (UV and Comfort)

- `get_hourly_forecast`: Get an hourly weather forecast for a configurable number of hours
  - Parameters:
    - `lng`: The longitude of the location
    - `lat`: The latitude of the location
    - `hours`: The number of hours to return (`1`–`360`, defaults to `72`)
  - Returns hourly forecast including:
    - Temperature
    - Weather conditions
    - Rain probability
    - Precipitation intensity (mm/hr)
    - Wind speed and direction

- `get_weekly_forecast`: Get daily weather forecast for the next 7 days
  - Parameters:
    - `lng`: The longitude of the location
    - `lat`: The latitude of the location
  - Returns daily forecast including:
    - Temperature range (min/max)
    - Weather conditions
    - Rain probability

- `get_historical_weather`: Get historical weather data for the past 24 hours
  - Parameters:
    - `lng`: The longitude of the location
    - `lat`: The latitude of the location
  - Returns historical data including:
    - Temperature
    - Weather conditions

- `get_weather_alerts`: Get weather alerts for a specific location
  - Parameters:
    - `lng`: The longitude of the location
    - `lat`: The latitude of the location
  - Returns weather alerts including:
    - Alert title
    - Alert code
    - Alert status
    - Alert description

Note: All tools require a valid Caiyun Weather API token to be set in the environment variable `CAIYUN_WEATHER_API_TOKEN`.

**官方网站：** [https://github.com/caiyunapp/mcp-caiyun-weather](https://github.com/caiyunapp/mcp-caiyun-weather)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`location services`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`mcp-caiyun-weather`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/wzmmcp-caiyun-weather.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
