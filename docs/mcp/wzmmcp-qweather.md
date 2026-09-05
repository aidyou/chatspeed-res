---
title: "qweather"
description: "English | MCP server for API, providing comprehensive weather information query capabilities through Model Context Protocol (MCP)."
---

# qweather

English | MCP server for API, providing comprehensive weather information query capabilities through Model Context Protocol (MCP).

# qweather-mcp
[mseep.ai](https://mseep.ai/app/ae24a36c-f029-49b3-9c42-fc111021add0)
[![MseeP.ai Security Assessment Badge](/mcp-assets/35c8dbcff4c38d1b415e403e20aa31bd.png)](https://mseep.ai/app/overstarry-qweather-mcp)
[Smithery](https://smithery.ai/server/@overstarry/qweather-mcp)

English | [简体中文](https://github.com/hello634528/qweather-mcp/blob/HEAD/README.zh-CN.md)

> MCP server for [QWeather](https://www.qweather.com/) API, providing comprehensive weather information query capabilities through Model Context Protocol (MCP).

## ✨ Features

- 🌤️ Real-time weather queries
- 📍 Latitude/longitude-based queries (no city lookup)
- 📅 Multi-day weather forecasts (3/7/10/15/30 days)
- 🔑 Simple API key configuration
- 🔌 Custom API base URL support
- 🛠️ Complete tool integration

## 📦 Installation

### Via Smithery

Recommended: Install automatically for Claude Desktop using [Smithery](https://smithery.ai/server/@overstarry/qweather-mcp):

```bash
npx -y @smithery/cli install @overstarry/qweather-mcp --client claude
```

### Manual Configuration

1. First, get your API Key from the [QWeather Console](https://console.qweather.com/).

2. Start the server:

```bash
# stdio server
npx -y qweather-mcp
```

3. Configure environment variables:

```bash
QWEATHER_API_BASE=https://api.qweather.com
QWEATHER_API_KEY=
```

### JSON Configuration

Add to your configuration file:

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

## 🛠️ Available Tools

All tools accept **latitude** and **longitude** parameters (in degrees).

### get-weather-now

Get current weather information for a specified latitude/longitude.

### get-weather-forecast

Get weather forecast information for a specified latitude/longitude with customizable forecast days:
- 3-day forecast
- 7-day forecast
- 10-day forecast
- 15-day forecast
- 30-day forecast

Forecast data includes:
- Temperature range (min/max)
- Day/night weather conditions
- Sunrise/sunset times
- Precipitation
- Humidity
- Wind conditions
- UV index

### get-minutely-precipitation

Provides minute-by-minute precipitation forecast for the next 2 hours at a specified latitude/longitude, including:
- Precipitation type (rain/snow)
- Precipitation amount per minute
- Precise time predictions
- Real-time forecast descriptions

### get-hourly-forecast

Provides hourly weather forecasts for 24, 72, or 168 hours at a specified latitude/longitude, including:
- Temperature changes
- Weather conditions
- Wind direction and force
- Relative humidity
- Atmospheric pressure
- Precipitation probability
- Cloud coverage

### get-weather-warning

Provides real-time weather warning information for a specified latitude/longitude, including:
- Warning issuing authority
- Warning level and type
- Detailed warning content
- Warning validity period
- Related recommendations

### get-weather-indices

Provides weather life indices information for a specified latitude/longitude, supporting various index types:
- Sports index
- Car wash index
- Dressing index
- Fishing index
- UV index
- Tourism index
- Allergy index
and 16 other life indices

### get-air-quality

Provides real-time air quality data for a specified latitude/longitude, including:
- AQI index
- Air quality level
- Primary pollutants
- Health advice
- Pollutant concentrations

### get-air-quality-hourly

Provides hourly air quality forecast for the next 24 hours at a specified latitude/longitude:
- Hourly AQI predictions
- Pollutant concentration changes
- Health impact assessment
- Protection recommendations

### get-air-quality-daily

Provides air quality forecast for the next 3 days at a specified latitude/longitude:
- Daily AQI predictions
- Primary pollutant forecasts
- Air quality level changes
- Health protection advice

## 🤝 Contributing

Issues and improvements are welcome! Please check our contribution guidelines.

## 📄 License

MIT

## 🔗 Related Links

- [QWeather Official Website](https://www.qweather.com/)
- [API Documentation](https://dev.qweather.com/)
- [Console](https://console.qweather.com/)

**Official site: ** [https://github.com/hello634528/qweather-mcp](https://github.com/hello634528/qweather-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `research and data`, `location services`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @wangzmwzm/qweather-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/wzmmcp-qweather.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
