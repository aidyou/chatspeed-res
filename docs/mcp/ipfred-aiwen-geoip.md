---
title: "aiwen-mcp-server-geoip"
description: "Aiwen Mcp Server Geoip , quickly query IP and determine user location"
---

# aiwen-mcp-server-geoip

Aiwen Mcp Server Geoip , quickly query IP and determine user location

# Aiwen IP Location MCP Server

## Introduction
[Aiwen Technology](https://www.ipplus360.com/) is a global leader in high-precision real-time IP address location technology and a provider of big data services for the global cyberspace map.

Aiwen's IP location API is now fully compatible with the MCP protocol.

MCP Server for the Aiwen IP Location API

## Tool Introduction

1. IP Location `aiwen_ip_location`
- Description: Returns detailed information about the requested IP address, including country, province, city, operator, user, latitude and longitude, etc.
- Parameters:
  - `ip`: IP address, required (IPv4)

- Example Output

json
{
  "code": "Success",
  "data": {
    "continent": "Asia",
    "country": "China",
    "owner": "China Telecom",
    "isp": "China Telecom",
    "zipcode": "510000",
    "timezone": "UTC+8",
    "accuracy": "City",
    "source": "Data Mining",
    "areacode": "CN",
    "adcode": "440100",
    "asnumber": "4134",
    "lat": "23.116548",
    "lng": "113.295827",
    "radius": "87.3469",
    "prov": "Guangdong Province",
    "city": "Guangzhou"
  },
  "charge": true,
  "msg": "Query successful",
  "ip": "202.97.89.109",
  "coordsys": "WGS84"
}

2. Get Current Network IP Address and Location Information `user_network_ip`
- Description: Based on IP location detection, retrieves the current network IP address and location information of the user.
- Parameters: None
- Output: Same as above

## Quick Start

### Obtain API Key
Get your API key from the Aiwen official website: https://mall.ipplus360.com/pros/IPVFourGeoAPI

### Configuration in MCP HOST
#### cursor
json
{
    "mcpServers": {
        "aiwen-iplocation": {
            "command": "npx",
            "args": [
                "-y",
                "aiwen-mcp-server-geoip"
            ],
            "env": {
                "AIWEN_API_KEY": "xxxxxx"
            }
        }
    }
}

#### vscode
json
{
    "mcpServers": {
        "aiwen-iplocation": {
            "command": "npx",
            "args": [
                "-y",
                "aiwen-mcp-server-geoip"
            ],
            "env": {
                "AIWEN_API_KEY": "xxxxxx"
            }
        }
    }
}

**Official site: ** [https://github.com/ipfred/aiwen-mcp-server-geoip](https://github.com/ipfred/aiwen-mcp-server-geoip)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `location services`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y aiwen-mcp-server-geoip`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/ipfred-aiwen-geoip.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
