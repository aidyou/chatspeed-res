---
title: "GaodeMapMCPServer"
description: "该高德地图 MCP Server 发布在 。 本服务提供以下工具： 将一个高德经纬度坐标转换为行政区划地址信息 参数： - location: 经纬度坐标 将详细的结构化地址转换为经纬度坐标。支持对地标性名胜景区、建筑物名称解析为经纬度坐标 参数： - address: 结构化地址 - city (可选): 指定查询的城市 IP 定位根据用户输入的 IP 地址，定位 IP 的所在位置 参数： -…"
---

# GaodeMapMCPServer

该高德地图 MCP Server 发布在 。 本服务提供以下工具： 将一个高德经纬度坐标转换为行政区划地址信息 参数： - location: 经纬度坐标 将详细的结构化地址转换为经纬度坐标。支持对地标性名胜景区、建筑物名称解析为经纬度坐标 参数： - address: 结构化地址 - city (可选): 指定查询的城市 IP 定位根据用户输入的 IP 地址，定位 IP 的所在位置 参数： -…

# AMap MCP Server

This AMap MCP Server is published on [PyPI](https://pypi.org/project/amap-mcp-server/).

## MCP Tools List

This service provides the following tools:

### Geocoding Tools

#### maps_regeocode
Converts an AMap latitude and longitude coordinate into administrative division address information.

**Parameters:**
- `location`: Latitude and longitude coordinates

#### maps_geo
Converts a detailed structured address into latitude and longitude coordinates. Supports parsing of landmark scenic spots and building names into latitude and longitude coordinates.

**Parameters:**
- `address`: Structured address
- `city` (optional): Specifies the city for the query

### Location Service Tools

#### maps_ip_location
IP location determines the location of the IP based on the user's input IP address.

**Parameters:**
- `ip`: IP address

#### maps_weather
Queries the weather of a specified city based on the city name or standard adcode.

**Parameters:**
- `city`: City name or adcode

### Route Planning Tools

#### Bicycling Routes
##### maps_bicycling_by_coordinates
Bicycling route planning is used to plan commuting routes, taking into account overpasses, one-way streets, and road closures. Supports up to 500km of bicycling route planning.

**Parameters:**
- `origin`: Origin latitude and longitude coordinates
- `destination`: Destination latitude and longitude coordinates

##### maps_bicycling_by_address
Bicycling route planning (address version), uses addresses for bicycling route planning. It is recommended to use this tool first.

**Parameters:**
- `origin_address`: Origin address (e.g., "No. 6 Futong East Street, Chaoyang District, Beijing")
- `destination_address`: Destination address (e.g., "No. 10 Shangdi 10th Street, Haidian District, Beijing")
- `origin_city` (optional): The city where the origin is located, to improve geocoding accuracy
- `destination_city` (optional): The city where the destination is located, to improve geocoding accuracy

#### Walking Routes
##### maps_direction_walking_by_coordinates
Walking route planning API can plan walking commuting routes within 100km based on the input origin and destination latitude and longitude coordinates, and return the commuting data.

**Parameters:**
- `origin`: Origin latitude and longitude coordinates
- `destination`: Destination latitude and longitude coordinates

##### maps_direction_walking_by_address
Walking route planning (address version), uses addresses for walking route planning. It is recommended to use this tool first.

**Parameters:**
- `origin_address`: Origin address (e.g., "No. 6 Futong East Street, Chaoyang District, Beijing")
- `destination_address`: Destination address (e.g., "No. 10 Shangdi 10th Street, Haidian District, Beijing")
- `origin_city` (optional): The city where the origin is located, to improve geocoding accuracy
- `destination_city` (optional): The city where the destination is located, to improve geocoding accuracy

#### Driving Routes
##### maps_direction_driving_by_coordinates
Driving route planning API can plan commuting travel schemes for small passenger cars and sedans based on the user's origin and destination latitude and longitude coordinates, and return the commuting data.

**Parameters:**
- `origin`: Origin latitude and longitude coordinates
- `destination`: Destination latitude and longitude coordinates

##### maps_direction_driving_by_address
Driving route planning (address version), uses addresses for driving route planning. It is recommended to use this tool first.

**Parameters:**
- `origin_address`: Origin address (e.g., "No. 6 Futong East Street, Chaoyang District, Beijing")
- `destination_address`: Destination address (e.g., "No. 10 Shangdi 10th Street, Haidian District, Beijing")
- `origin_city` (optional): The city where the origin is located, to improve geocoding accuracy
- `destination_city` (optional): The city where the destination is located, to improve geocoding accuracy

#### Public Transit Routes
##### maps_direction_transit_integrated_by_coordinates
Plans integrated public transit (train, bus, subway) commuting schemes based on the user's origin and destination latitude and longitude coordinates, and returns the commuting data. For intercity scenarios, the origin and destination cities must be provided.

**Parameters:**
- `origin`: Origin latitude and longitude coordinates
- `destination`: Destination latitude and longitude coordinates
- `city`: Origin city
- `cityd`: Destination city

##### maps_direction_transit_integrated_by_address
Public transit route planning (address version), uses addresses for public transit route planning. It is recommended to use this tool first.

**Parameters:**
- `origin_address`: Origin address (e.g., "No. 6 Futong East Street, Chaoyang District, Beijing")- `destination_address`: Destination address (e.g., "No. 10, Shangdi 10th Street, Haidian District, Beijing")
- `origin_city`: Origin city (required for intercity travel)
- `destination_city`: Destination city (required for intercity travel)

### Distance Measurement Tools

#### maps_distance
Measures the distance between two latitude and longitude coordinates, supporting driving, walking, and spherical distance measurements.

**Parameters:**
- `origins`: Origin latitude and longitude coordinates
- `destination`: Destination latitude and longitude coordinates
- `type` (optional, default is "1"): Type of measurement

### POI Search Tools

#### maps_text_search
The keyword search API performs POI searches based on user-input keywords and returns relevant information.

**Parameters:**
- `keywords`: Search keywords
- `city` (optional): City to query
- `citylimit` (optional, default is "false"): Whether to limit the search within the city range

#### maps_around_search
Searches for POIs within a radius based on the user-provided keywords and location coordinates.

**Parameters:**
- `location`: Latitude and longitude coordinates of the center point
- `radius` (optional, default is "1000"): Search radius
- `keywords` (optional): Search keywords

#### maps_search_detail
Queries detailed information about the POI ID obtained from keyword or nearby searches.

**Parameters:**
- `id`: POI ID

## Configuration Methods

To use this service, you need to add the following MCP configuration in your application. The service supports three transmission methods: `stdio` (default), `sse`, and `streamable-http`.

### stdio Transmission (Default)

Directly configure the MCP Server as follows in the client.

```json

{

    "mcpServers": {

        "amap-mcp-server": {

            "command": "uvx",

            "args": [

                "amap-mcp-server"

            ],

            "env": {

                "AMAP_MAPS_API_KEY": "your valid amap maps api key"

            }

        }

    }

}

```
### SSE Transmission

SSE transmission supports real-time data pushing, suitable for remotely deployed MCP Servers.

Run `amap-mcp-server` locally with SSE:

```bash

$ export AMAP_MAPS_API_KEY=你的有效API Key

$ uvx amap-mcp-server sse

INFO:     Started server process [50125]

INFO:     Waiting for application startup.

INFO:     Application startup complete.

INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)

```
MCP Client Configuration:

```json

{

    "mcpServers": {

        "amap-mcp-server": {

            "url": "http://0.0.0.0:8000/sse"

        }

    }

}

```
### Streamable HTTP Transmission

Run `amap-mcp-server` locally with Streamable HTTP:

```bash

$ export AMAP_MAPS_API_KEY=你的有效API Key

$ uvx amap-mcp-server streamable-http

INFO:     Started server process [50227]

INFO:     Waiting for application startup.

StreamableHTTP session manager started

INFO:     Application startup complete.

INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)

```
MCP Client Configuration:

```json

{

    "mcpServers": {

        "amap-mcp-server": {

            "url": "http://localhost:8000/mcp"

        }

    }

}

```
You can register and obtain an API key on the [Amap Open Platform](https://lbs.amap.com/).

**Official site: ** [https://github.com/sugarforever/amap-mcp-server](https://github.com/sugarforever/amap-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `location services`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `amap-mcp-server`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/linkun56-gaodemapmcpserver.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
