---
title: "MeituanTravel"
description: "🧳 Meituan Travel Assistant One-stop travel inquiry MCP service, supporting hotel, flight, train ticket, attraction ticket booking, and itinerary planning. ✨ Core Features ▸ One-stop travel inquiry — C…"
---

# MeituanTravel

🧳 Meituan Travel Assistant One-stop travel inquiry MCP service, supporting hotel, flight, train ticket, attraction ticket booking, and itinerary planning. ✨ Core Features ▸ One-stop travel inquiry — C…

🧳 Meituan Travel Assistant

One-stop travel inquiry MCP service, supporting hotel, flight, train ticket, attraction ticket booking, and itinerary planning.

✨ Core Features

▸ One-stop travel inquiry — Covers hotel/flight/train ticket/attraction ticket/itinerary planning with a single tool

▸ Natural language interaction — Simply state your needs, such as "flights from Beijing to Shanghai" or "hotels near West Lake under 500 yuan"

▸ Coverage of over 300 cities nationwide — Data sourced from Meituan Travel, covering major travel destinations

▸ Real-time pricing and booking links — Provides real-time prices and direct booking links

🛠 Tools

meituan_travel_query

Comprehensive Meituan Travel inquiry, supporting one-stop travel services including hotel recommendations, flight and train ticket inquiries, attraction tickets, and itinerary planning.

Parameters:

▸ city (string, ✅ required): The current city, in Chinese, such as "北京" (Beijing), "上海" (Shanghai), "广州" (Guangzhou), "成都" (Chengdu)

▸ query (string, ✅ required): Natural language query for your needs, such as "flights from Beijing to Shanghai", "hotels near West Lake in Hangzhou", "tickets for Shanghai Disneyland", "two-day weekend travel guide in Chengdu"

📝 Usage Examples

▸ "Help me find flights from Beijing to Shanghai" → `meituan_travel_query(city="北京", query="北京到上海的机票")`

▸ "Hotels near West Lake in Hangzhou under 500 yuan" → `meituan_travel_query(city="杭州", query="杭州西湖附近500元以内的酒店")`

▸ "How much are the tickets for Shanghai Disneyland" → `meituan_travel_query(city="上海", query="上海迪士尼门票")`

▸ "Two-day weekend travel guide in Chengdu" → `meituan_travel_query(city="成都", query="周末两天成都游玩攻略")`

▸ "Train tickets from Guangzhou to Sanya" → `meituan_travel_query(city="广州", query="广州到三亚的火车票")`

▸ "What fun activities are there for kids in Beijing" → `meituan_travel_query(city="北京", query="带小孩去北京旅游推荐")`

**Official site: ** [https://pypi.org/project/mcp-meituan-travel/](https://pypi.org/project/mcp-meituan-travel/)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `search`, `developer tools`, `location services`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `--from mcp-meituan-travel==1.1.0 mcp-meituan-travel`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/mako2026-meituantravel.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
