---
title: "amap-mcp-weather"
description: "MCP Weather Service is a weather forecast service based on the AMap API, providing real-time weather conditions and forecast data. As part of the MCP (Model Control Protocol) ecosystem, it can be easi…"
---

# amap-mcp-weather

MCP Weather Service is a weather forecast service based on the AMap API, providing real-time weather conditions and forecast data. As part of the MCP (Model Control Protocol) ecosystem, it can be easi…

# MCP Weather Service

[English](https://github.com/merulas/amap-mcp-weather/blob/HEAD/README_EN.md) | Chinese

## Project Introduction

MCP Weather Service is a weather forecast service based on the AMap (Gaode Maps) API, providing real-time weather conditions and forecast data. As part of the MCP (Model Control Protocol) ecosystem, it can be easily integrated into MCP-supporting applications.

## Features

- **Real-time weather data**: get the current weather conditions for a specified location
- **Weather forecast**: provides future weather forecast data
- **China city coverage**: supports weather queries for all cities and districts in China
- **Easy integration**: as an MCP service, it is easy to integrate with other applications

## What is MCP?

MCP (Model Control Protocol) is a framework for building tools that can be used by AI models. MCP services can provide various functions, such as weather forecasts, search, calculation, etc., for AI models to call.

## Installation and Configuration

### Prerequisites

- Go 1.18 or higher
- AMap API key

### Installation steps

1. Clone the repository:
```bash
git clone https://github.com/tung/mcp.git
cd mcp
```

2. Create a `.env` file and add your AMap API key:
```
AMAP_API_KEY=your_api_key_here
```

> Note: you can get an API key by registering at the [AMap Open Platform](https://lbs.amap.com/).

## Running the Service

### Run directly

```bash
go run cmd/server/main.go
```

The service will run at `http://localhost:8080`.

### Run via the MCP framework

1. Create an MCP config file (see the configuration docs)
2. Start the service with the MCP framework:
```bash
mcp --config mcp-config.json
```

## API Usage

### Get a weather forecast

#### Request format

```
POST /weather
Content-Type: application/json

{
    "location": "Beijing"
}
```

#### Response format

```json
{
    "location": "Beijing",
    "location_key": "110000",
    "country": "China",
    "current_conditions": {
        "temperature": {
            "value": 25.6,
            "unit": "C"
        },
        "weather_text": "Sunny",
        "relative_humidity": 65,
        "precipitation": false,
        "observation_time": "2024-03-10T15:00:00+08:00"
    },
    "hourly_forecast": [
        {
            "relative_time": "+1 hour",
            "temperature": {
                "value": 26.1,
                "unit": "C"
            },
            "weather_text": "Sunny",
            "precipitation_probability": 10,
            "precipitation_type": "None",
            "precipitation_intensity": "None"
        },
        // more hourly forecasts...
    ]
}
```

### Response field description

#### Current weather conditions (`current_conditions`)
- `temperature`: current temperature (Celsius)
- `weather_text`: weather condition description
- `relative_humidity`: relative humidity percentage
- `precipitation`: whether there is precipitation
- `observation_time`: observation time

#### Hourly forecast (`hourly_forecast`)
- `relative_time`: time relative to the current time
- `temperature`: expected temperature
- `weather_text`: weather condition description
- `precipitation_probability`: precipitation probability
- `precipitation_type`: precipitation type
- `precipitation_intensity`: precipitation intensity

## Documentation

- API documentation
- MCP configuration documentation
- Claude MCP protocol documentation

## Development

### Project structure

```
mcp/
├── cmd/
│   └── server/
│       └── main.go         # Main program entry
├── internal/
│   ├── bean/
│   │   ├── weather.go      # Data models
│   │   ├── mcp.go          # MCP protocol data models
│   │   └── amap_weather.go # AMap API data models
│   ├── service/
│   │   ├── weather_service.go     # Original service layer (interacts with the AccuWeather API)
│   │   └── amap_weather_service.go # AMap service layer
│   ├── logic/
│   │   └── weather.go     # Business logic layer
│   └── handler/
│       ├── weather_handler.go # HTTP handler layer
│       └── mcp_handler.go     # MCP protocol handler layer
├── docs/
│   ├── weather.md         # API docs
│   ├── mcp-config.md      # MCP config docs
│   └── claude-mcp.md      # Claude MCP protocol docs
├── .env.example           # Environment variable example
└── README.md             # Project readme
```

## Using in the MCP configuration

You can use this service in the MCP config like this:

```json
{
    "mcpServers": {
        "weather": {
            "command": "go",
            "args": ["run", "cmd/server/main.go"],
            "env": {
                "AMAP_API_KEY": "your_api_key_here"
            }
        }
    }
}
```

## AMap API

This service uses the [AMap weather query API](https://lbs.amap.com/api/webservice/guide/api/weatherinfo) to get weather data. The AMap API provides real-time weather and forecasts, supporting weather queries for cities and districts nationwide.

Since the AMap API does not provide hourly weather forecasts, this service simulates hourly forecast data based on the daily forecast data, in order to stay compatible with the original interface.

## Limitations

- API calls are limited by the AMap free account tier
- Weather data update frequency depends on the AMap API's update frequency

## Contribution Guide

Pull Requests and Issues are welcome to improve this project.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [AMap](https://lbs.amap.com/) provides the weather data
- [MCP protocol](https://github.com/anthropics/anthropic-cookbook/tree/main/mcp) provides the model control protocol framework

**Official site: ** [https://github.com/merulas/amap-mcp-weather](https://github.com/merulas/amap-mcp-weather)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `research and data`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `go`
- Args: `run cmd/server/main.go`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/homeant-amap-weather.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
