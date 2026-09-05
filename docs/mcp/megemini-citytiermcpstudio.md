---
title: "CitytierMCPStudio"
description: "City Tier Query MCP Server Description This project is created via https://modelscope.cn/studios/megemini/CitytierMCPStudio Service Introduction This city tier query service, based on the 2025 New Fir…"
---

# CitytierMCPStudio

City Tier Query MCP Server Description This project is created via https://modelscope.cn/studios/megemini/CitytierMCPStudio Service Introduction This city tier query service, based on the 2025 New Fir…

# City Tier Query MCP Server

**Description** This project is created via https://modelscope.cn/studios/megemini/CitytierMCPStudio

## Service Introduction

This city tier query service, based on the 2025 New First-Tier Cities Charm Ranking, uses FastMCP and SSE protocol. The service provides a complete set of features for querying city tiers, including querying by city name, listing all cities in a specified tier, obtaining statistical information, and keyword search.

## Service Description

This is a professional city tier query MCP service based on the latest 2025 City Charm Rankings data. The service offers four main functions: querying the tier of a city by its name, listing all cities within a specific tier, obtaining statistical information about all tiers, and searching for cities using keywords. The service is implemented using the FastMCP framework and SSE protocol to ensure an efficient and stable query experience.

## Type

Data Query, City Information, Geographical Services

## Features

- Query which tier a city belongs to by its name
- List all cities in a specified tier
- Obtain statistical information about all city tiers
- Search for cities using keywords

## City Tiers

- **First-tier Cities (4)**: Shanghai, Beijing, Shenzhen, Guangzhou
- **New First-tier Cities (15)**: Chengdu, Hangzhou, Chongqing, Wuhan, Suzhou, Xi'an, Nanjing, Changsha, Zhengzhou, Tianjin, Hefei, Qingdao, Dongguan, Ningbo, Foshan
- **Second-tier Cities (30)**: Jinan, Wuxi, Shenyang, Kunming, Fuzhou, Xiamen, Wenzhou, Shijiazhuang, etc.
- **Third-tier Cities (70)**: Urumqi, Lanzhou, Zhongshan, Yancheng, Haikou, Yangzhou, etc.
- **Fourth-tier Cities (90)**: Zaozhuang, Yibin, Yulin, Kaifeng, Shaoyang, Yuncheng, etc.
- **Fifth-tier Cities (128)**: Xinzhou, Panjin, Ili, Dandong, Yanbian, Jiuquan, etc.

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

**Official site: ** [https://modelscope.cn/studios/megemini/CitytierMCPStudio](https://modelscope.cn/studios/megemini/CitytierMCPStudio)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `location services`, `search`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `mcp-remote https://megemini-citytiermcpstudio.ms.show/gradio_api/mcp/sse --transport sse-only`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/megemini-citytiermcpstudio.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
