---
title: "SmartPoi"
description: "Intelligent Attraction Recommendation MCP Server (mcp-poi-smart-recommend) I. Product Introduction A 6-in-1 intelligent recommendation service centered on attraction recommendations, covering the enti…"
---

# SmartPoi

Intelligent Attraction Recommendation MCP Server (mcp-poi-smart-recommend) I. Product Introduction A 6-in-1 intelligent recommendation service centered on attraction recommendations, covering the enti…

Intelligent Attraction Recommendation MCP Server (mcp-poi-smart-recommend)

I. Product Introduction

A 6-in-1 intelligent recommendation service centered on attraction recommendations, covering the entire process from "where to go" to "how to get there." By integrating Fliggy travel ticket data with AMap location services, it provides capabilities such as AI recommendations, structured search, nearby discovery, weather forecasting, and transportation planning.

II. Tool Capabilities

▸ recommend_poi: AI intelligent attraction recommendation, where a natural language description returns the most suitable attractions along with ticket prices and booking links

▸ search_poi: Structured search for attraction tickets, supporting multi-dimensional filtering by city, keyword, type, and level

▸ search_fast: Rapid search, quickly querying information about attractions, tickets, and routes

▸ nearby_poi: Nearby attraction discovery, searching for nearby attractions based on location, returning distance, rating, and address

▸ search_weather: Querying destination weather forecasts to assist in travel decision-making

▸ search_transport: Transportation planning, including taxi fare estimates, subway/bus transfer plans, and one-click taxi booking links

III. Usage Scenarios

▸ Travel Planning: Recommending destination attractions based on interest preferences

▸ Ticket Inquiry: Searching for attraction ticket prices and booking links by city, type, and level

▸ Nearby Exploration: Discovering hidden gems near the current location

▸ Travel Preparation: Getting ahead of the game by understanding the destination's weather and transportation options

IV. Usage Instructions

This MCP service is distributed via PyPI. Install it using the following command:

bash
pip install mcp-poi-smart-recommend

After installation, add the Server command in the MCP client configuration:

bash
mcp-poi-smart-recommend

V. Parameter Explanation

recommend_poi (AI Intelligent Recommendation)

▸ query (required): Description for attraction recommendation, in natural language, e.g., "seaside attractions suitable for families in Sanya," "5A scenic spots recommended in Hangzhou"

search_poi (Structured Search for Attraction Tickets)

▸ cityName (required): City name, such as Hangzhou, Xi'an

▸ keyword (optional): Keywords for the attraction name, such as the Forbidden City, the Great Wall, Disneyland

▸ category (optional): Type of attraction, such as natural scenery, theme parks, cultural relics

▸ poiLevel (optional): Attraction level 1-5 (5 being 5A), 0 indicates no limit

search_fast (Rapid Search)

▸ query (required): Search term, such as "Sanya attractions," "Beijing Forbidden City tickets," "Shanghai Disneyland"

nearby_poi (Nearby Attraction Discovery)

▸ location (required): Current location or landmark, such as West Lake, The Bund, the Forbidden City

▸ city (optional): City, such as Hangzhou, Shanghai, Beijing

▸ radius (optional): Search radius (in meters), default is 3000

search_weather (Weather Forecast)

▸ query (required): Weather query description, such as "Sanya weather forecast," "Hangzhou weather tomorrow"

search_transport (Transportation Planning)

▸ query (required): Transportation query description, such as "Pudong Airport to The Bund (Shanghai)," "Beijing South Railway Station to the Forbidden City"

**Official site: ** [https://pypi.org/project/mcp-poi-smart-recommend/](https://pypi.org/project/mcp-poi-smart-recommend/)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `search`, `developer tools`, `location services`, `景点推荐`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `mcp-poi-smart-recommend==5.0.1`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/mako2026-smartpoi.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
