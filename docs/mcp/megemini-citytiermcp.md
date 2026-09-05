---
title: "CitytierMCP"
description: "Based on the 2025 New First-Tier Cities Charm Ranking, this city tier query service uses FastMCP and SSE protocol. The service provides a complete set of functions for querying city tiers, supporting…"
---

# CitytierMCP

Based on the 2025 New First-Tier Cities Charm Ranking, this city tier query service uses FastMCP and SSE protocol. The service provides a complete set of functions for querying city tiers, supporting…

# City Tier Query MCP Server

**Note** This project is created via GitHub.

## Service Introduction

This city tier query service, based on the 2025 New First-Tier Cities Charm Ranking, uses FastMCP and SSE protocol. The service provides a complete set of functions for querying city tiers, including searching by city name, listing all cities within a specified tier, obtaining statistical information, and keyword-based searches.

## Service Description

This is a professional city tier query MCP service, built upon the latest 2025 City Charm Rankings data. The service offers four main functionalities: querying the tier of a city by its name, listing all cities in a specific tier, getting statistical information about all tiers, and searching for cities using keywords. The service is implemented using the FastMCP framework and SSE protocol to ensure an efficient and stable query experience.

## Categories

Data Query, City Information, Geographical Services

## Features

- Query which tier a city belongs to by its name
- List all cities within a specified tier
- Obtain statistical information about all city tiers
- Search for cities based on keywords

## City Tiers

- **First-tier Cities (4)**: Shanghai, Beijing, Shenzhen, Guangzhou
- **New First-tier Cities (15)**: Chengdu, Hangzhou, Chongqing, Wuhan, Suzhou, Xi'an, Nanjing, Changsha, Zhengzhou, Tianjin, Hefei, Qingdao, Dongguan, Ningbo, Foshan
- **Second-tier Cities (30)**: Jinan, Wuxi, Shenyang, Kunming, Fuzhou, Xiamen, Wenzhou, Shijiazhuang, etc.
- **Third-tier Cities (70)**: Urumqi, Lanzhou, Zhongshan, Yancheng, Haikou, Yangzhou, etc.
- **Fourth-tier Cities (90)**: Zaozhuang, Yibin, Yulin, Kaifeng, Shaoyang, Yuncheng, etc.
- **Fifth-tier Cities (128)**: Xinzhou, Panjin, Ili, Dandong, Yanbian, Jiuquan, etc.

## Installation

bash
pip install -r requirements.txt

## Usage

### Running as an MCP Server (SSE Protocol)

bash
python server.py

The server will run in SSE mode, listening on the default port.

### Available Tools

1. **get_city_tier** - Query city tier
   - Parameters: `city_name` (string) - Name of the city
   - Example: Querying "Shanghai" returns "Shanghai belongs to First-tier Cities"

2. **list_cities_by_tier** - List cities by tier
   - Parameters: `tier` (string) - City tier
   - Possible values: First-tier Cities, New First-tier Cities, Second-tier Cities, Third-tier Cities, Fourth-tier Cities, Fifth-tier Cities

3. **get_all_tiers** - Get statistics for all tiers
   - No parameters
   - Returns the count of cities in each tier

4. **search_cities** - Search for cities
   - Parameters: `keyword` (string) - Search keyword
   - Returns a list of cities containing the keyword along with their tiers

## Service Configuration

Add the following to your MCP client configuration file:

### SSE Protocol Configuration

json
{
  "mcpServers": {
    "city-tier": {
      "command": "python",
      "args": ["main.py"],
      "cwd": "/path/to/mcp_server/city",
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "enabled": true,
      "sse": {
        "url": "http://localhost:8080/sse"
      }
    }
  }
}

Or use the project script to start:

json
{
  "mcpServers": {
    "city-tier": {
      "command": "bash",
      "args": ["start_server.sh"],
      "cwd": "/path/to/mcp_server/city",
      "enabled": true,
      "sse": {
        "url": "http://localhost:8080/sse"
      }
    }
  }
}

### Running with uvx

json
{
  "mcpServers": {
    "city-tier": {
      "command": "uvx",
      "args": ["fastmcp", "run", "main.py"],
      "cwd": "/path/to/mcp_server/city",
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "enabled": true,
      "sse": {
        "url": "http://localhost:8080/sse"
      }
    }
  }
}

## Environment Variable Configuration

Supported environment variables:

- `FASTMCP_LOG_LEVEL`: Log level, possible values are DEBUG, INFO, WARNING, ERROR, default is ERROR

**Official site: ** [https://github.com/megemini/CitytierMCP](https://github.com/megemini/CitytierMCP)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `location services`, `search`, `mcp`, `city tier`, `城市分级`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `fastmcp run main.py`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/megemini-citytiermcp.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
