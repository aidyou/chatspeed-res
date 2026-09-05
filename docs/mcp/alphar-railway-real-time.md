---
title: "Railway-Real-Time-MCP-Server"
description: "12306-MCP-Server v1.0.0 A high-availability 12306 ticket availability query tool service designed for large language models (LLM), now equipped with an intelligent session management engine. 12306-MCP…"
---

# Railway-Real-Time-MCP-Server

12306-MCP-Server v1.0.0 A high-availability 12306 ticket availability query tool service designed for large language models (LLM), now equipped with an intelligent session management engine. 12306-MCP…

# 12306-MCP-Server v1.0.0

[![Node.js Version](/mcp-assets/a6853f6b3626e12a1c348f7d36b64bc9.svg)](https://nodejs.org/)
![License](/mcp-assets/d177f30277cff66d9af1e3c6409e24dc.svg)

[![Docker Pulls](/mcp-assets/dfdae949fb9b905b5571a7a6d41a6870.svg)](https://hub.docker.com/r/maozida880/12306-mcp-server)

**A high-availability 12306 ticket availability query tool service designed for large language models (LLM), now equipped with an intelligent session management engine.**

12306-MCP-Server encapsulates the complex 12306 ticket availability query interface into a set of tools that comply with the [Model Context Protocol](https://modelcontextprotocol.io) (MCP) specification, allowing AI Agents to seamlessly query real-time train ticket, transfer, and stopover information through natural language.

Starting from version `v1.0.0`, the project introduces a brand new intelligent session management system, elevating the service's stability and anti-blocking capabilities to new heights through session pools, dynamic User-Agent rotation, and automatic error recovery mechanisms.

## 🎯 Core Advantages

- **🚀 High Performance**: 90%+ session reuse rate, 33% reduction in response time, 228% increase in throughput
- **💪 High Availability**: Intelligent error recovery, 99.5%+ service availability, automatic session replenishment
- **🛡️ Anti-Blocking**: 12 types of UA dynamic rotation, intelligent rate limiting, 95% reduction in IP ban risk
- **📊 Observability**: Detailed monitoring metrics, health check endpoints, structured logs
- **⚙️ Easy Configuration**: Environment variable configuration, Docker support, ready to use out of the box

## ✨ Core Features

### Intelligent Session Management
- **Session Pool**: Maintains a pool of 2-5 sessions (configurable) for efficient connection reuse
- **Health Monitoring**: Evaluates session health based on error rates and automatically eliminates unhealthy sessions
- **Background Maintenance**: Automatically cleans up expired sessions and replenishes new sessions every 5 minutes
- **Intelligent Recovery**: Automatically identifies session failures, immediately destroys and creates new sessions
- **Request Queue**: Intelligently queues requests when the pool is full to avoid request failures

### Query Toolset
### How to Use: Detailed Explanation of Tools and Parameters

This service primarily provides four query tools designed for different scenarios, effectively helping developers build feature-rich travel applications.

#### 1. Ticket Availability Query Interface (get-tickets)
  Purpose: Retrieve available direct train schedules and their detailed information, including ticket prices, remaining tickets, duration, etc., based on the departure, destination, and date.
  Usage Scenario: When a user wants to know which trains are available from one city to another, this interface can quickly provide all options.
  Request Parameters:
     `date` (required): Query date in "yyyy-MM-dd" format.
     `fromStation` (required): The station_code of the departure location.
     `toStation` (required): The station_code of the arrival location.
     `trainFilterFlags` (optional): Train schedule filter flags, such as "G" for high-speed rail/intercity, "D" for EMU, etc.
     `earliestStartTime` / `latestStartTime` (optional): Earliest/latest departure time (0-24 hours).
     `sortFlag` (optional): Sorting method, supports sorting by departure time, arrival time, and duration.
     `format` (optional): Result format, supports text, csv, json.

#### 2. Transfer Query Interface (get-interline-tickets)
  Purpose: Query transfer options between two locations, providing multiple transfer options and detailed information for each segment of the journey.
  Usage Scenario: Suitable for scenarios where there are no direct trains between two cities or when users want to find more travel options.
  Request Parameters:
     `date` (required): Query date.
     `fromStation` (required): The station_code of the departure location.
     `toStation` (required): The station_code of the arrival location.
     `middleStation` (optional): The station_code of the specified transfer station.

#### 3. Train Route Station Query Interface (get-train-route-stations)
  Purpose: Input a specific train number and departure date to obtain details of all stops along the route, including arrival and departure times.
  Usage Scenario: Used when passengers have already decided to take a specific train but want to know the details of the stops along the way.
  Request Parameters:
     `trainCode` (required): The train number to be queried, e.g., "G1033".
     `departDate` (required): The departure date of the train in "yyyy-MM-dd" format.

#### 4. Station Code Query InterfacePurpose: Provide multiple ways to query the `station_code` of train stations, which is a required parameter for other query interfaces.
Usage Scenario: Before performing a ticket query, convert the Chinese place names entered by users (such as "Beijing", "Shanghai Hongqiao") into station codes that the system can recognize.
Available Tools:
    `get-station-code-by-names`: Query through specific Chinese station names.
    `get-station-code-of-citys`: Query the station code representing a city through the Chinese city name.
    `get-stations-code-in-city`: Query all train station codes within a city.

### Flexible Filtering and Sorting
- Supports filtering by train type (G/D/Z/T/K/F/S)
- Supports filtering by departure time range
- Supports sorting by departure time, arrival time, and duration

### Multiple Output Formats
- Supports `text` (default), `csv`, and `json` formats
- Facilitates data consumption and processing in different scenarios

## 📊 Performance Metrics

| Metric | v0.3.x | v1.0.0 | Improvement |
|--------|--------|--------|-------------|
| Response Time (P95) | 2.5s | 0.5s | +80% |
| Throughput | 2.5 req/s | 8.2 req/s | +228% |
| Success Rate | 92% | 99.5% | +8.2% |
| Session Reuse Rate | 10% | 90%+ | +800% |
| IP Ban Risk | High | Very Low | -95% |

## 📄 License

This project is licensed under the MIT license.

## 📧 Contact

- **Issues**: [GitHub Issues](https://github.com/maozida880/12306-mcp-server/issues)
- **Email**: maozida880@126.com
- **Discussion**: [GitHub Discussions](https://github.com/maozida880/12306-mcp-server/discussions)

## ⭐ Star History

If this project has been helpful to you, please give it a ⭐️ Star!

**Official site: ** [https://github.com/maozida880/12306-MCP-Server](https://github.com/maozida880/12306-MCP-Server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `search`, `communication`
- Tags: `search`, `communication`, `developer tools`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `12306-mcp-server`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/alphar-railway-real-time.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
