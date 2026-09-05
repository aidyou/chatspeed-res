---
title: "Weather"
description: "MCP Weather Query Service This is a weather query service based on MCP (Minimalist Chat Protocol), allowing users to query weather information for different cities through simple commands. Features -…"
---

# Weather

MCP Weather Query Service This is a weather query service based on MCP (Minimalist Chat Protocol), allowing users to query weather information for different cities through simple commands. Features -…

# MCP Weather Query Service

This is a weather query service based on MCP (Minimalist Chat Protocol), allowing users to query weather information for different cities through simple commands.

## Features

- Supports querying weather information for major cities globally
- Provides detailed information such as temperature, weather conditions, humidity, and wind speed
- Uses asynchronous processing to improve response speed
- Comprehensive error handling mechanism
- Supports a mock data mode, enabling testing without an API key

## Installation Requirements

- Python 3.13 or higher
- Dependencies:
  - httpx >= 0.28.1
  - mcp >= 1.11.0

## Usage

1. Ensure all dependencies are installed:
   
   pip install -r requirements.txt
   
   Or use the project configuration:
   
   pip install -e .
   

2. Enter your API key in the OpenWeatherMap API configuration section (optional):
   python
   OPENWEATHER_API_KEY = "你的API密钥"  # Replace with your OpenWeatherMap API key
   
   If no API key is set, the service will use mock data.

3. Run the server:
   
   python main.py
   

4. Use the following command to query the weather:
   
   /weather 城市名
   
   For example: `/weather 北京`

## Getting an OpenWeatherMap API Key

1. Visit the [OpenWeatherMap official website](https://openweathermap.org/) and register an account
2. Log in and go to the API key page
3. Create a new API key
4. Copy the obtained API key into the `OPENWEATHER_API_KEY` variable in the code

## Development Notes

- `main.py` - The main program file, containing the MCP server and weather query functionality
- Uses the FastMCP framework to handle requests and responses
- Retrieves weather data via the OpenWeatherMap API
- Supports a mock data mode for ease of development and testing

## Important Notes

- The free OpenWeatherMap API has request limits; please use it reasonably
- If no API key is set, the service will use mock data

**Official site: ** [https://www.modelscope.cn/studios/chance617/Weather](https://www.modelscope.cn/studios/chance617/Weather)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `productivity`
- Tags: `calendar management`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uv`
- Args: `--directory D:\MCP\MCP_Minimalist_Development\example run main.py`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/chance617-weather.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
