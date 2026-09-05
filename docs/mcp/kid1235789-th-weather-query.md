---
title: "th-weather-query"
description: "Query weather conditions by place name, latitude and longitude, area code and postal code, IP address, or scenic spot name. You can obtain data on the current 24-hour weather, a 7-day forecast, a 15-d…"
---

# th-weather-query

Query weather conditions by place name, latitude and longitude, area code and postal code, IP address, or scenic spot name. You can obtain data on the current 24-hour weather, a 7-day forecast, a 15-d…

# Tonghu Weather Forecast Query MCP Service Documentation

## What is the Tonghu Weather Forecast Query MCP Service?
The Tonghu weather forecast query MCP Server provides the following core features:
- Query weather conditions by place name, latitude/longitude, area code/postal code, IP address, or scenic spot name.
- Get data for the current 24-hour weather, 7-day forecast, 15-day forecast, and historical weather conditions.

Service features:
- **Comprehensive coverage**: direct official data connection, detailed and accurate data, supporting queries across various dimensions.
- **Real-time updates**: real-time verification, millisecond response, precise validation.
- **Wide application**: widely used in energy, power, agriculture, life service apps, smart hardware, aerospace, navigation, tourism, construction, and other fields.

---

## How to use the Tonghu Weather Forecast Query MCP Service?
### Getting an API Key
1. Register and log in to the [Tonghu MCP platform](https://mcp.tonghu.top "Tonghu MCP")
2. Create your API Key (an existing one can be used directly)
3. Enable the [Weather Forecast Query] service in the [Product Center](https://mcp.tonghu.top/#/layout/prodCenter "Tonghu MCP")

### Deployment method 1 (SSE)
```
{
  "mcpServers": {
    "TH_MCP": {
      "url": "https://mcp.tonghu.top/sse?apiKey=YOUR_API_KEY_FROM_TONGHU_MCP"
    }
  }
}
```

### Deployment method 2 (Streamable HTTP)
```
{
  "mcpServers": {
    "TH_MCP": {
      "url": "https://mcp.tonghu.top/streamable?apiKey=YOUR_API_KEY_FROM_TONGHU_MCP"
    }
  }
}
```

> **Notes**:
- The service already supports integration into agents and workflows

---

## Use cases for the Tonghu Weather Forecast Query MCP Service

1. **Smart travel planning**
   - After the user enters a destination name or selects GPS positioning, the app automatically calls the MCP weather forecast query API to get real-time weather and the forecast for the coming days.
   - Suggests clothing and items to bring based on the weather.
   - Improves travel comfort and avoids inconvenience caused by weather changes.

3. **Agricultural production guidance**
   - Use the MCP query service to get weather forecasts and historical data for specific farmland locations, combined with agricultural expert systems to provide planting advice.
   - Increase crop yields and reduce losses from natural disasters.
   - Manage farm resources scientifically and optimize production processes.

4. **Outdoor event organization**
   - Use MCP to query detailed weather information for the target area, including temperature, precipitation probability, wind speed, and other key indicators.
   - Decide whether to proceed with the activity as planned or adjust the date and location based on the forecast.
   - Ensure participant safety and improve event quality. Avoid unnecessary economic losses and improve organizational efficiency.

---

## FAQ

**Q: Does using the Tonghu Weather Forecast Query MCP Service cost money?**
A: The first activation of the product includes a free trial quota. When the quota runs out, you can choose:
- Purchase a package (limited-time discount)
- Top up your balance and pay per use
- For large volumes, contact customer service for custom discounts

**Q: What should I note when using the Tonghu Weather Forecast Query MCP Service?**
A: For first-time use:
1. Log in to the [Tonghu MCP platform](https://mcp.tonghu.top "Tonghu MCP") and register with your phone number
2. Create an API Key
3. Enable the service in the Product Center (you can additionally purchase a package)

> **Technical support**
> Contact platform customer service or Mr. Wang: 18363092551 (also on WeChat)

**Official site: ** [https://mcp.tonghu.top](https://mcp.tonghu.top)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `location services`, `other`, `天气服务`

## MCP Configuration

- Transport: `http`
- Command: ``
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/kid1235789-th-weather-query.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
