---
title: "mcp-server-weather"
description: "MCP Weather Query Server. An MCP (Model Context Protocol) weather query server based on the Tianxing Data API, providing real-time weather information queries for AI models. Features: city search (Chi…"
---

# mcp-server-weather

MCP Weather Query Server. An MCP (Model Context Protocol) weather query server based on the Tianxing Data API, providing real-time weather information queries for AI models. Features: city search (Chi…

# MCP Weather Query Server

An MCP (Model Context Protocol) weather query server based on the Tianxing Data API, providing real-time weather information query functionality for AI models.

## 🌟 Features

- **City Search**: Supports searching by city names in both Chinese and English
- **Real-Time Weather**: Retrieves detailed information such as current weather, temperature, humidity, wind conditions, etc.
- **Air Quality**: Provides AQI index and air quality level
- **Life Tips**: Offers clothing and travel advice based on weather conditions
- **Rich Display**: Uses emoji icons for an intuitive and friendly display of information

## 🛠️ MCP Tool Functions

### 1. `query_weather(city: str)`
Queries weather information based on the city name.

**Parameters:**
- `city`: City name (supports both Chinese and English, e.g., Guangzhou, Beijing, shanghai, etc.)

**Returns:**
- A formatted string of weather information, including temperature, humidity, wind conditions, air quality, etc.

**Example:**
```python
result = await query_weather("广州")
# 返回:
# 📍 广东 广州 (2025-06-14 星期六)
# 🌤️ 天气: 阴
# 🌡️ 当前温度: 26.4℃
# 📊 温度范围: 24℃ ~ 30℃
# ...
```
### 2. `search_city_info(city: str)`
Searches for detailed information about a city.

**Parameters:**
- `city`: City name (supports both Chinese and English)

**Returns:**
- A string containing detailed city information, including Chinese and English names, province, latitude and longitude, city code, etc.

**Example:**
```python
result = await search_city_info("广州")
# 返回:
# 🏙️ 城市信息
# 📍 中文名称: 广州
# 🔤 英文名称: guangzhou
# 🗺️ 所属省份: 广东 (guangdong)
# ...
```
## 📦 Installation and Usage

### 1. Install Dependencies
```bash
cd mcp-weather/mcp-server-weather
uv sync
```
### 2. Start the Server
```bash
# Use the built-in API key
python server.py

# Or use a custom API key
python server.py --api_key YOUR_API_KEY
```
### 3. Configure MCP Client (Cursor Integration)
Add the following configuration to the `.cursor/mcp.json` file in Cursor:

```json

{

  "mcpServers": {

    "weather": {

      "command": "uv",

      "args": [

        "--directory",

        "/Users/luoshui/Documents/Cursor/MCP/mcp-weather/mcp-server-weather",

        "run",

        "server.py"

      ],

      "disabled": false,

      "autoApprove": [

        "query_weather",

        "search_city_info"

      ]

    }

  }

}

```
**Parameter Explanation:**
- `command`: Run using `uv` as the package manager
- `--directory`: Specifies the service directory
- `run server.py`: Starts the weather service
- `autoApprove`: Automatically approves tool function calls without manual confirmation
- `disabled`: Whether to disable this service

> **Note:** Please adjust the paths according to your local setup.

### 4. Usage
- In Cursor, directly ask about the weather in natural language, such as "查询广州天气" or "北京空气质量如何", and the AI will automatically call the MCP tools.
- Supports querying detailed city information, such as "广州的城市代码是多少".

## 🔧 Technical Implementation

- **API Provider**: Tianxing Data (tianapi.com)
- **HTTP Client**: httpx
- **MCP Framework**: FastMCP
- **Asynchronous Support**: Fully asynchronous implementation, supporting concurrent requests
- **Error Handling**: Comprehensive error handling with user-friendly error messages

## 📊 API Endpoints

### City Search Endpoint
- **URL**: `https://apis.tianapi.com/citylookup/index`
- **Method**: GET
- **Parameters**: `key`, `area`

### Weather Query Endpoint
- **URL**: `https://apis.tianapi.com/tianqi/index`
- **Method**: GET
- **Parameters**: `key`, `city`, `type`

## 🧪 Test Results

✅ All features tested successfully:
- API connection is normal
- City search function works normally
- Weather query function works normally
- Data formatting is correct
- MCP tool functions work normally

## 📝 Notes

1. **City Names**: Supports Chinese city names; support for English names is limited
2. **API Limitations**: Uses a free API key, which may have request frequency limits
3. **Network Dependency**: Requires a stable internet connection to access the Tianxing Data API
4. **Data Accuracy**: Weather data is sourced from Tianxing Data, and accuracy depends on the data provider

## 🔄 Changelog

- **v0.1.0**: Initial version, implementing basic weather query functionality
- Supports city search and weather queries
- Comprehensive error handling and data formatting
- MCP tool function integration

## 📄 License

This project is licensed under the MIT License.

**Official site: ** [https://github.com/luoshui-coder/mcp-server-weather.git](https://github.com/luoshui-coder/mcp-server-weather.git)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `search`, `location services`, `天气`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uv`
- Args: `--directory /Users/luoshui/Documents/Cursor/MCP/mcp-weather/mcp-server-weather run server.py`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/luoshui2025-weather.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
