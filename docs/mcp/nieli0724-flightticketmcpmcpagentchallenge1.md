---
title: "FlightTicketMCPMCPAgentChallenge1"
description: "一个基于模型上下文协议(MCP)的航空机票查询服务器。该服务器为AI助手提供标准化的航班实时动态查询功能接口。 Flight Ticket MCP Server 实现了供航空机票相关查询操作的工具和资源。它作为AI助手与航空服务系统之间的桥梁，专注于航班实时动态查询功能。 该服务器采用模块化架构，将核心功能、工具和实用程序分离，使其具有高度的可维护性和可扩展性。 - 根据出发地、目的地和出发日期查…"
---

# FlightTicketMCPMCPAgentChallenge1

一个基于模型上下文协议(MCP)的航空机票查询服务器。该服务器为AI助手提供标准化的航班实时动态查询功能接口。 Flight Ticket MCP Server 实现了供航空机票相关查询操作的工具和资源。它作为AI助手与航空服务系统之间的桥梁，专注于航班实时动态查询功能。 该服务器采用模块化架构，将核心功能、工具和实用程序分离，使其具有高度的可维护性和可扩展性。 - 根据出发地、目的地和出发日期查…

# Flight Ticket MCP Server

A flight ticket query server based on the Model Context Protocol (MCP). This server provides standardized real-time flight dynamic query interfaces for AI assistants.

## Overview

The Flight Ticket MCP Server implements tools and resources for flight ticket-related queries. It serves as a bridge between AI assistants and aviation service systems, focusing on real-time flight dynamic query functionalities.

The server adopts a modular architecture, separating core functions, tools, and utilities to ensure high maintainability and scalability.

## Features

### Flight Route Query
- Query available flights based on departure, destination, and departure date
- Supports 282 domestic cities and airport codes
- Intelligent city name resolution (supports city names, airport codes, full format)
- Real-time flight prices and schedules
- Airline and aircraft information
- Terminal and gate information
- Price statistics and airline distribution
- Formatted output results

### Transfer Flight Route Query
- Query connecting flights based on departure, transfer, and destination
- Supports custom minimum and maximum transfer times (default 2-5 hours)
- Intelligent filtering of flight combinations that meet transfer time requirements
- Provides complete two-segment journey information
- Supports domestic and international route transfer queries
- Detailed transfer time calculation and validation

### Weather Information Query
- **By Latitude and Longitude**: Precise geographical weather query
- **By City Name**: Supports direct queries for major cities
- Supports historical, current, and future weather data
- Provides detailed information such as temperature, humidity, wind speed, and weather conditions
- Automatically handles time zones and date ranges
- Supports preset major cities like Wuhan, Beijing, Shanghai, etc.

### Flight Information Query
- Query detailed flight information by flight number
- Includes flight status, seat configuration, and price information
- Provides weather information (for departure and destination)
- Displays basic flight information (airline, aircraft type, route type)
- Detailed terminal and gate information
- Real-time dynamic status (on time, delayed, boarding, in flight, etc.)
- Seat price and availability information
- Additional service information (meals, WiFi, entertainment system, etc.)

### Real-Time Flight Tracking
- **Real-Time Flight Status Query**: Query real-time location and status of flights
- **Flights Around Airport Query**: Query all flights within a 30-kilometer radius of a specified airport
- **Regional Flight Query**: Query all real-time flights within a specified geographic area
- **Batch Flight Tracking**: Track the real-time status of multiple flights simultaneously
- Supports major Chinese airport codes (PEK, PVG, CAN, etc., over 70 airports)
- Provides detailed flight location, speed, altitude, and status information
- Public API without authentication, with real-time flight data updates

### Date and Time Tools
- Get the current system date (YYYY-MM-DD format)
- Get the current system date and time (YYYY-MM-DD HH:mm:ss format)
- Provides standardized date and time support for other features
- Automatically handles time zone and format conversions

### Data Processing and Intelligence
- **Intelligent City Resolution**: Supports multiple city input formats (city names, airport codes, full format)
- **Parameter Validation**: Comprehensive input parameter validation and error handling
- **Result Formatting**: Unified JSON format output, easy for AI assistants to parse
- **Error Recovery**: Robust exception handling and fallback mechanisms
- **Logging**: Detailed operation logs and debugging information

## Technical Architecture

### Core Module (Core)
- Flight data models and structure definitions
- Data models for airports, airlines, flights, and prices
- Data structures for flight transfers and seat configurations

### Tools Module (Tools)
- **Flight Search Tool** (`flight_search_tools.py`) - Flight route query functionality
- **Flight Transfer Tool** (`flight_transfer_tools.py`) - Multi-segment journey and transfer queries
- **Flight Information Tool** (`flight_info_tools.py`) - Detailed information query by flight number
- **Real-Time Flight Tracking Tool** (`simple_opensky_tools.py`) - Real-time flight tracking based on OpenSky Network
- **Weather Query Tool** (`weather_tools.py`) - Weather queries based on latitude/longitude and city
- **Date and Time Tool** (`date_tools.py`) - Date and time retrieval and processing

### Utility Module (Utils)
- **City Dictionary** (`cities_dict.py`) - Mapping of 282 cities and airport codes- **Data Validator** (`validators.py`) - Input parameter validation and format checking
- **Date Utilities** (`date_utils.py`) - Date formatting and timezone handling
- **API Client** (`api_client.py`) - HTTP request encapsulation and error handling

### MCP Integration Layer
- **FastMCP Server** - MCP protocol implementation based on the FastMCP framework
- **Multi-Transport Protocol Support** - stdio, SSE, HTTP transport protocols
- **Tool Registration Management** - Unified tool registration and invocation mechanism
- **Environment Configuration Management** - Flexible configuration and environment variable support

## Supported Transport Protocols

This server supports three transport protocols:

1. **sse** - Server-Sent Events (default, suitable for web applications)
2. **stdio** - Standard input/output (suitable for Claude Desktop)
3. **streamable-http** - Streamable HTTP (suitable for HTTP clients)

## Installation

### Prerequisites
- Python 3.11 or higher
- pip package manager (or uvx tool)

### Method One: Install from PyPI (Recommended)

```bash

# 使用pip安装

pip install flight-ticket-mcp-server

# 或使用uvx直接运行（无需安装）

uvx flight-ticket-mcp-server

# 或使用uvx安装后运行

uvx --install flight-ticket-mcp-server

```
### Method Two: Local Development Installation
```bash
# 克隆或下载项目
cd FlightTicketMCP

# 安装依赖
pip install -r requirements.txt

# 或从本地源码安装
pip install -e .
```
### uvx Usage Guide

uvx is a modern Python package running tool that can directly run PyPI packages without first installing them into the system environment:

```bash

# 安装uv（包含uvx工具）

pip install uv

# 直接运行MCP服务器（无需安装）

uvx flight-ticket-mcp-server

# 使用最新版本（推荐）

uvx flight-ticket-mcp-server@latest

# 带参数运行

uvx flight-ticket-mcp-server --help

# 指定版本运行

uvx flight-ticket-mcp-server==1.0.1

# 强制重新安装最新版本

uvx flight-ticket-mcp-server@latest --help

```
**Advantages of uvx:**
- 🚀 No need to pollute the global Python environment
- 📦 Automatic management of virtual environments
- 🔄 Supports running the latest version directly
- 🛡️ Isolates dependencies to avoid conflicts

## Startup Methods

### 1. Direct Startup (Default SSE Mode)

```bash

# 使用主启动文件（默认启动SSE模式，监听127.0.0.1:8000）

python flight_ticket_server.py

# 或者直接运行main.py

python main.py

```
### 2. Start in Debug Mode

```bash

# 启用调试模式，会输出详细日志

set MCP_DEBUG=true

python flight_ticket_server.py

# Linux/macOS

export MCP_DEBUG=true

python flight_ticket_server.py

```
### 3. Start with Different Transport Protocols

#### SSE Mode (Default)
```bash
# 直接启动，使用默认SSE配置（127.0.0.1:8000）
python flight_ticket_server.py
```
#### stdio Mode
```bash
# Windows
set MCP_TRANSPORT=stdio
python flight_ticket_server.py

# Linux/macOS
export MCP_TRANSPORT=stdio
python flight_ticket_server.py
```
#### HTTP Mode
```bash
# Windows
set MCP_TRANSPORT=streamable-http
set MCP_HOST=127.0.0.1
set MCP_PORT=8000
python flight_ticket_server.py

# Linux/macOS
export MCP_TRANSPORT=streamable-http
export MCP_HOST=127.0.0.1
export MCP_PORT=8000
python flight_ticket_server.py
```
### 4. Environment Variable Configuration

#### Using .env File (Recommended)

The project provides a `.env.example` file as a configuration template:

1. **Copy the Configuration Template**:
```bash
   # 复制配置模板
   cp .env.example .env
```
2. **Edit the Configuration File**:
   Open the `.env` file and modify the configuration values as needed:
```env
   # MCP服务器配置
   MCP_TRANSPORT=sse
   MCP_HOST=127.0.0.1
   MCP_PORT=8000
   MCP_SSE_PATH=/sse
   
   # 日志配置
   LOG_LEVEL=INFO
   LOG_FILE_PATH=logs/flight_server.log
   LOG_MAX_SIZE=10
   LOG_BACKUP_COUNT=5
   
   # 开发配置
   MCP_DEBUG=false
```
3. **Configuration Explanation**:
   - The `.env` file contains sensitive configurations and will not be committed to version control.
   - The `.env.example` is a safe template file that can be committed to Git.
   - Environment variable priority: System environment variables > .env file > Program default values

#### Setting Environment Variables Directly

If you do not use the `.env` file, you can also set environment variables directly:

Supported environment variables:

| Variable Name | Description | Default Value | Possible Values |
|---------------|-------------|---------------|-----------------|
| `MCP_TRANSPORT` | Transport protocol type | `sse` | `stdio`, `sse`, `streamable-http` |
| `MCP_HOST` | Server host address | `127.0.0.1` | Any valid IP address |
| `MCP_PORT` | Server port | `8000` | 1-65535 |
| `MCP_PATH` | HTTP path | `/mcp` | Any valid path |
| `MCP_SSE_PATH` | SSE path | `/sse` | Any valid path |
| `MCP_DEBUG` | Debug mode | `false` | `true`, `false`, `1`, `0` |
| `LOG_LEVEL` | Log level | `INFO` | `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL` |
| `LOG_FILE_PATH` | Log file path | `logs/flight_server.log` | Any valid path |
| `LOG_MAX_SIZE` | Maximum log file size (MB) | `10` | Positive integer |
| `LOG_BACKUP_COUNT` | Number of log backups | `5` | Positive integer |
| `FASTMCP_LOG_LEVEL` | FastMCP log level | `INFO` | `DEBUG`, `INFO`, `WARNING`, `ERROR` |

### 5. Startup Verification

After a successful startup, you will see output similar to:

```

Transport: sse

Logging enabled - logs will be saved to logs/ directory

Flight Ticket MCP Server starting...

Transport: sse

All tools registered successfully

Starting SSE transport on 127.0.0.1:8000/sse

```
### 6. Log Files

After the server starts, the following log files will be generated in the `logs/` directory:

- `flight_server.log` - General logs (INFO level and above)
- `flight_server_error.log` - Error logs (ERROR level)
- `flight_server_debug.log` - Debug logs (generated only in debug mode)

### 7. Stopping the Server

- **stdio mode**: Press `Ctrl+C` to stop
- **HTTP/SSE mode**: Press `Ctrl+C` or send a SIGTERM signal

## Usage

### MCP Client Configuration

#### Method One: Using uvx (Recommended)

Using uvx to run the MCP server, no pre-installation required, simple and elegant:

```json

{

  "mcpServers": {

    "flight-ticket-server": {

      "command": "uvx",

      "args": ["flight-ticket-mcp-server@latest"]

    }

  }

}

```
**Advantages of uvx configuration:**
- 🚀 No need to pre-install packages
- 📦 Automatic management of dependencies and virtual environments
- 🔄 Always runs the latest version
- 🛡️ Isolated environment to avoid conflicts

#### Method Two: Run After Installing with pipIf installed via pip, you can directly use the command-line tool:

bash
```json
{
  "mcpServers": {
    "flight-ticket-server": {
      "command": "flight-ticket-mcp-server"
    }
  }
}
```
#### Method Three: Local Development Version

For local development or custom versions:

bash
```json
{
  "mcpServers": {
    "flight-ticket-server": {
      "command": "python",
      "args": ["D:\\FlightTicketMCP\\flight_ticket_server.py"],
      "env": {
        "MCP_TRANSPORT": "stdio"
      }
    }
  }
}
```
#### Configuration File Location

Add the above configuration to the Claude Desktop configuration file:
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/claude/claude_desktop_config.json`

#### Applying the Configuration

1. Save the configuration file.
2. Restart Claude Desktop.
3. In Claude Desktop, you should see that the flight-ticket-server connection is successful.

### Configuration for Different Transport Protocols

#### SSE Mode (Default)
json
```json
{
  "mcpServers": {
    "flight-ticket-server": {
      "command": "python",
      "args": ["D:\\FlightTicketMCPServer\\flight_ticket_server.py"],
      "env": {
        "MCP_TRANSPORT": "sse",
        "MCP_HOST": "127.0.0.1",
        "MCP_PORT": "8000",
        "MCP_SSE_PATH": "/sse"
      }
    }
  }
}
```
#### Stdio Mode
json
```json
{
  "mcpServers": {
    "flight-ticket-server": {
      "command": "python",
      "args": ["D:\\FlightTicketMCPServer\\flight_ticket_server.py"],
      "env": {
        "MCP_TRANSPORT": "stdio"
      }
    }
  }
}
```
#### HTTP Mode
json
```json
{
  "mcpServers": {
    "flight-ticket-server": {
      "command": "python",
      "args": ["D:\\FlightTicketMCPServer\\flight_ticket_server.py"],
      "env": {
        "MCP_TRANSPORT": "streamable-http",
        "MCP_HOST": "127.0.0.1",
        "MCP_PORT": "8000",
        "MCP_PATH": "/mcp"
      }
    }
  }
}
```
### MCP Client Testing

#### Test Connection

After configuring, you can test the MCP server connection in the following ways:

1. **Claude Desktop Test**:
   - Restart Claude Desktop.
   - Check if the status bar shows "flight-ticket-server" connected successfully.
   - Try asking in a conversation: "What tools are available to you now?"

2. **Command Line Test**:
bash
```bash
   # 使用uvx直接测试
   uvx flight-ticket-mcp-server --help
   
   # 或使用已安装的包测试
   flight-ticket-mcp-server --help
   
   # 测试模块化运行
   python -m flight_ticket_mcp_server --help
```
3. **MCP Protocol Test**:
bash
```bash
   # 使用MCP inspector工具测试（如果安装了）
   npx @modelcontextprotocol/inspector uvx flight-ticket-mcp-server
```
#### Verify Tool Registration

After a successful connection, your Claude should be able to access the following tools:

- ✈️ **searchFlightRoutes** - Flight route query
- 📅 **getCurrentDate** - Get current date
- 🔄 **getTransferFlightsByThreePlace** - Transfer flight query
- 🌤️ **getWeatherByLocation** - Weather query by latitude and longitude
- 🏙️ **getWeatherByCity** - Weather query by city
- ℹ️ **getFlightInfo** - Flight information query
- 📡 **getFlightStatus** - Real-time flight status query
- 🛫 **getAirportFlights** - Flights around the airport query
- 🗺️ **getFlightsInArea** - Area flights query
- 📊 **trackMultipleFlights** - Batch flight tracking

#### Troubleshooting

If the connection fails, please check:

1. **uvx Configuration**:
bash
```bash
   # 检查uv/uvx是否安装
   uvx --version
   
   # 手动测试包运行
   uvx flight-ticket-mcp-server@latest
```
2. **Package Version**:
bash
```bash
   # 强制使用最新版本
   uvx flight-ticket-mcp-server@latest
   
   # 清除uvx缓存后重试
   uv cache clean
   uvx flight-ticket-mcp-server@latest
```
3. **Configuration File Syntax**:
   - Ensure the JSON format is correct.
   - Check that quotes and brackets match.
   - Verify the configuration file path.

4. **Log Check**:
   - View the log output of Claude Desktop.
   - Check the server startup logs.

### Example Operations

After configuration, you can ask Claude to perform the following operations:

#### Flight Route Query
- "Query flights from Chongqing to Guangzhou tomorrow."
- "Search for all flights from Shanghai to Beijing the day after tomorrow."
- "Check the flight prices from Shenzhen to Chengdu on July 20, 2024."
- "What are the options for flights from Beijing to Sanya?"
- "Help me find the flight information from Chengdu to Hangzhou next Tuesday."

#### Transfer Flight Query
- "Query transfer flights from Beijing to New York via Hong Kong."
- "Search for connecting flights from Shanghai to London via Dubai, with a layover of 3-6 hours."
- "Find flights from Guangzhou to Sydney via Singapore, with the shortest layover of 2 hours."
- "What are the flights from Beijing to Los Angeles via Tokyo?"

#### Weather Information Query
- "Check the weather in Beijing today and tomorrow."
- "How's the weather in Shanghai?"
- "Query the weather at latitude 39.9042, longitude 116.4074." (Beijing coordinates)
- "Weekly weather forecast for Wuhan."
- "Check the weather in Chongqing from July 15, 2024, to July 17, 2024."

#### Flight Information Query
- "Query detailed information about flight CA1234."
- "What is the current status of flight MU5678?"
- "Help me check the seat and price information for flight HU7890."
- "Gate and terminal information for flight CZ3691."

#### Real-Time Flight Tracking Query
- "Query the real-time status and location of flight CCA1234."
- "View the flights around Beijing Capital Airport."
- "Query all flights within the Beijing area (latitude 39-41, longitude 115-118)."
- "Track the real-time status of flights CCA1234, CSN5678, and MU9876 simultaneously."
- "View the flights currently flying near Pudong Airport."
- "Where is this plane now? What is its altitude and speed?"

#### Date and Time Query
- "What's the date today?"
- "What is the current date and time?"
- "Help me get the current date."

#### Comprehensive Query Examples
- "I want to fly from Chengdu to Beijing, departing tomorrow. Also, tell me the weather in Beijing."
- "Query flights from Shanghai to Guangzhou, and also check the weather in Guangzhou."
- "Help me plan a trip from Chongqing to Tokyo, with a transfer, and check the destination weather."- "Query the information of flight CA1234, as well as the weather at the departure and arrival locations"
- "My flight is MU5678, please help me check the flight status and seat situation"
- "Check the real-time location of flight CCA1234, and also tell me the weather at the destination"
- "I want to know which flights are departing from Beijing airport now, and the current weather in Beijing"

## API Reference

### Flight Route Query
```python
searchFlightRoutes(departure_city, destination_city, departure_date)  # 根据出发地、目的地和日期查询可用航班
```
Input Parameters:
- `departure_city`: Departure city name or airport code (e.g., "Chongqing", "CKG", "Chongqing(CKG)")
- `destination_city`: Destination city name or airport code (e.g., "Guangzhou", "CAN", "Guangzhou(CAN)")
- `departure_date`: Departure date (in YYYY-MM-DD format)

Output Information:
- List of flights (including flight number, airline, departure and arrival times, airports, terminals, prices)
- Price statistics (lowest price, highest price, average price)
- Airline distribution statistics
- Formatted query result output
- Supported cities: 282 domestic cities and airports

Supported City Formats:
- City names: Shanghai, Beijing, Chongqing, Guangzhou, etc.
- Airport codes: SHA, BJS, CKG, CAN, etc.
- Full format: Shanghai(SHA), Beijing(BJS), etc.

### Transfer Flight Route Query
```python
getTransferFlightsByThreePlace(from_place, transfer_place, to_place, min_transfer_time, max_transfer_time)
```
Input Parameters:
- `from_place`: Departure city name or airport code (e.g., "Beijing", "BJS")
- `transfer_place`: Transfer city name or airport code (e.g., "Hong Kong", "HKG")  
- `to_place`: Destination city name or airport code (e.g., "New York", "NYC")
- `min_transfer_time`: Minimum transfer time (hours), default 2.0 hours
- `max_transfer_time`: Maximum transfer time (hours), default 5.0 hours

Output Information:
- List of qualifying transfer flight combinations
- Detailed information for the first leg (from departure to transfer point)
- Detailed information for the second leg (from transfer point to destination)
- Actual transfer time calculation
- Detailed information such as flight numbers, times, and airports

### Weather Information Query

#### By Latitude and Longitude
```python
getWeatherByLocation(latitude, longitude, start_date, end_date)
```
Input Parameters:
- `latitude`: Latitude (e.g., 39.9042)
- `longitude`: Longitude (e.g., 116.4074)
- `start_date`: Start date (in YYYY-MM-DD format), optional
- `end_date`: End date (in YYYY-MM-DD format), optional

#### By City Name
```python
getWeatherByCity(city_name, start_date, end_date)
```
Input Parameters:
- `city_name`: City name (e.g., "Beijing", "Sha

**Official site: ** [https://github.com/xiaonieli7/FlightTicketMCP](https://github.com/xiaonieli7/FlightTicketMCP)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `search`, `browser`
- Tags: `browser automation`, `other`, `search`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `flight-ticket-mcp-server@latest`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/nieli0724-flightticketmcpmcpagentchallenge1.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
