---
title: "mcp-weather"
description: "Provides hourly weather forecasts using the AccuWeather API, enabling users to access current weather conditions and detailed 12-hour forecasts tailored to specific locations."
---

# mcp-weather

Provides hourly weather forecasts using the AccuWeather API, enabling users to access current weather conditions and detailed 12-hour forecasts tailored to specific locations.

# MCP Weather Server

A simple MCP server that provides hourly weather forecasts using the AccuWeather API.

## Setup

1. Install dependencies using `uv`:
```bash
uv venv
uv sync
```

2. Create a `.env` file with your AccuWeather API key:
```
ACCUWEATHER_API_KEY=your_api_key_here
```

You can get an API key by registering at [AccuWeather API](https://developer.accuweather.com/).

## Running the Server

```json
{
    "mcpServers": {
        "weather": {
            "command": "uvx",
            "args": ["--from", "git+https://github.com/adhikasp/mcp-weather.git", "mcp-weather"],
            "env": {
                "ACCUWEATHER_API_KEY": "your_api_key_here"
            }
        }
    }
}
```

## API Usage

### Get Hourly Weather Forecast

Response:
```json
{
    "location": "Jakarta",
    "location_key": "208971",
    "country": "Indonesia",
    "current_conditions": {
        "temperature": {
            "value": 32.2,
            "unit": "C"
        },
        "weather_text": "Partly sunny",
        "relative_humidity": 75,
        "precipitation": false,
        "observation_time": "2024-01-01T12:00:00+07:00"
    },
    "hourly_forecast": [
        {
            "relative_time": "+1 hour",
            "temperature": {
                "value": 32.2,
                "unit": "C"
            },
            "weather_text": "Partly sunny",
            "precipitation_probability": 40,
            "precipitation_type": "Rain",
            "precipitation_intensity": "Light"
        }
    ]
}
```

The API provides:
- Current weather conditions including temperature, weather description, humidity, and precipitation status
- 12-hour forecast with hourly data including:
  - Relative time from current time
  - Temperature in Celsius
  - Weather description
  - Precipitation probability, type, and intensity

**Official site: ** [https://github.com/adhikasp/mcp-weather](https://github.com/adhikasp/mcp-weather)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `location services`, `other`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `--from git+https://github.com/adhikasp/mcp-weather.git mcp-weather`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/adhikasp-weather.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
