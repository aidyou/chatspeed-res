---
title: "amap-maps"
description: "Amap Maps is a server that supports any MCP protocol client, allowing users to easily utilize the Amap Maps MCP server for various location-based services."
---

# amap-maps

Amap Maps is a server that supports any MCP protocol client, allowing users to easily utilize the Amap Maps MCP server for various location-based services.

## Product Introduction

To achieve better interaction between LBS services and LLM, Amap's MCP Server now covers 12 core service interfaces, providing comprehensive map services for all scenarios, including geocoding, reverse geocoding, IP location, weather queries, cycling route planning, walking route planning, driving route planning, public transport route planning, distance measurement, keyword search, nearby search, and detail search.

To further enhance developer access efficiency and experience, Amap Open Platform provides developers with a [general-level SSE protocol](https://lbs.amap.com/api/mcp-server/gettingstarted) MCP service solution.

## Amap Open Platform General-Level SSE Protocol MCP Service Solution

#### Product Architecture Diagram

![](/mcp-assets/d20fa1ab7ce32e945458280acfb2c5a9.png)

#### What is SSE?

Server-Sent Events (SSE) is a technology based on the HTTP protocol that allows servers to push data to clients in a unidirectional and real-time manner. In the SSE mode, developers can establish a persistent connection with the server by creating an EventSource object on the client-side. The server then continuously sends data streams through this connection without the client needing to repeatedly send requests.

#### Product Features

+   Easy to Use: Suitable for regular users based on MCP (SSE) mode, no need to deploy local services, and can be used simply by configuring a URL address.
    
+   Automatic Upgrades: We will continue to iterate and update without any additional operation needed from users.
    
+   Easier for LLM Understanding: We have semantically converted the original JSON results, making it easier for LLM to understand the content.
    
+   Zero Maintenance Cost: Adopts a fully managed cloud service architecture, so users do not need to worry about server maintenance, resource expansion, and other underlying operational issues.
    
+   Protocol Compatibility: Supports SSE long connections to meet the technical needs of different business scenarios.
    

Visit the [Quick Access](https://lbs.amap.com/api/mcp-server/gettingstarted) documentation to learn how to access the MCP Server SSE service.

## Capability Introduction

#### Geocoding

Convert detailed structured addresses into latitude and longitude coordinates.

Input

address (location information),

 city (city information, optional)

Output

location (latitude and longitude)

#### Reverse Geocoding

Convert Amap latitude and longitude coordinates into administrative district address information.

Input

location (latitude and longitude)

Output

addressComponent (location information, including province, city, district, etc.)

#### IP Location

IP location determines the location of an IP based on the user-provided IP address.

Input

IP

Output

province (province), city (city), adcode (city code)

#### Weather Query

Query the weather of a specified city based on the city name or standard adcode.

Input

city (city name or city adcode)

Output

forecasts (weather forecasts)

#### Cycling Route Planning

Used for planning cycling commuting routes, considering overpasses, one-way streets, road closures, etc. Supports cycling route planning up to 500km.

Input

origin (start latitude and longitude),

 destination (end latitude and longitude)

Output

distance (planned distance), duration (planned time), steps (planned step information)

#### Walking Route Planning

Plan walking commuting routes within 100km based on the input starting and ending latitude and longitude coordinates and return the data of the commuting plan.

Input

origin (start latitude and longitude),

 destination (end latitude and longitude)

Output

origin (start information), destination (end information), paths (planned specific information)

#### Driving Route Planning

Plan commuting travel solutions for small cars and sedans based on the user's start and end latitude and longitude coordinates and return the commuting plan data.

Input

origin (start latitude and longitude),

 destination (end latitude and longitude)

Output

origin (start information), destination (end information), paths (planned specific information)

#### Public Transport Route Planning

Plan commuting solutions that integrate various public transport modes (train, bus, subway) based on the user's start and end latitude and longitude coordinates and return the commuting plan data. For cross-city scenarios, the start city and end city must be provided.

Input

origin (start latitude and longitude), destination (end latitude and longitude), city (start city), cityd (end city)

Output

origin (start information), destination (end information), distance (planned distance), transits (planned specific information)

#### Distance Measurement

Measure the distance between two latitude and longitude coordinates.

Input

origin (start latitude and longitude), destination (end latitude and longitude)

Output

origin_id (start information), dest_id (end information), distance (planned distance), duration (time)

#### Keyword Search

Search for related POI location information based on user-provided keywords.

Input

keywords (search keywords),

 city (query city, optional)

Output

suggestion (search suggestion), pois (location information list)

#### Nearby Search

Search for POI location information within a radius based on user-provided keywords and location coordinates.

Input

keywords (search keywords),

 location (central latitude and longitude), radius (search radius, optional)

Output

pois (location information list)

#### Detail Search

Query detailed information of POI ID obtained from keyword search or nearby search.

Input

id (POI ID obtained from keyword search or nearby search)

Output

Location detail information

location (latitude and longitude), address, business_area (business district), city, type (location type), etc.

**Official site: ** [https://www.npmjs.com/package/@amap/amap-maps-mcp-server](https://www.npmjs.com/package/@amap/amap-maps-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `location services`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @amap/amap-maps-mcp-server`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/amap-amap-maps.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
