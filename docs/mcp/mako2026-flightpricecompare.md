---
title: "FlightPriceCompare"
description: "✈️ Cross-Platform Flight Price Comparison MCP v4.0.0 Real-time price comparison for direct flights across five major platforms, automatically matched by flight number across platforms, with booking li…"
---

# FlightPriceCompare

✈️ Cross-Platform Flight Price Comparison MCP v4.0.0 Real-time price comparison for direct flights across five major platforms, automatically matched by flight number across platforms, with booking li…

✈️ Cross-Platform Flight Price Comparison MCP v4.0.0

Real-time price comparison for direct flights across five major platforms, automatically matched by flight number across platforms, with booking links following the lowest price. No need to apply for a Key; use it directly via URL.

✨ Core Features

▸ Lowest Price Priority — Automatically matches the same flight across platforms, and the booking link follows the lowest price

▸ Time Slot Filtering — Supports early morning/AM/midday/PM/evening/night/red-eye, or specify a specific time (with a 45-minute buffer)

▸ Multiple Airport Recognition — Automatically identifies Beijing (Capital/Daxing), Shanghai (Hongqiao/Pudong), Chengdu (Shuangliu/Tianfu)

▸ Price Anomaly Detection — Automatically alerts when the lowest price is 60% lower than the second-lowest price, avoiding abnormally low-price traps

▸ Direct Flights Only — Automatically filters out connecting flights, resulting in cleaner results

▸ Sorting Modes — Default sorting by platform coverage + price / cheapest (lowest price) / earliest (earliest departure)

🛠 Tools

flight_compare — Cross-Platform Flight Price Comparison

Simultaneously searches for direct flight prices on Feizhu, Tuniu, Tongcheng, Meituan, and RG, matching by flight number across platforms, with booking links following the lowest price.

Parameters:

▸ fromCity (required) — Departure city, e.g., "Shanghai", "Beijing", "Guangzhou"

▸ toCity (required) — Arrival city, e.g., "Sanya", "Guangzhou", "Shanghai"

▸ date (required) — Departure date, format YYYY-MM-DD, e.g., "2026-07-10"

▸ timePref (optional) — Time preference: early morning/AM/midday/PM/evening/night/red-eye, or specific time like "10:00" (with a 45-minute buffer)

▸ sortMode (optional) — Sorting mode: cheapest (lowest price priority), earliest (earliest departure priority), default sorting by platform coverage + price

Data Sources:

▸ Feizhu — One of the largest OTAs in China, under Alibaba

▸ Tuniu — Comprehensive travel platform with broad coverage

▸ Tongcheng — Part of Tencent, competitive pricing

▸ Meituan — Local life + travel (starting price)

▸ RG — Global travel booking (full-price ticket reference)

📝 Usage Examples

▸ "How much is a flight from Shanghai to Beijing tomorrow?" → flight_compare(fromCity="上海", toCity="北京", date="2026-07-01")

▸ "Check the morning flights from Guangzhou to Sanya on July 10th" → flight_compare(fromCity="广州", toCity="三亚", date="2026-07-10", timePref="上午")

▸ "Flights from Beijing to Chengdu next Friday, sorted by lowest price" → flight_compare(fromCity="北京", toCity="成都", date="2026-07-04", sortMode="cheapest")

▸ "Are there any red-eye flights from Shenzhen to Hangzhou on National Day?" → flight_compare(fromCity="深圳", toCity="杭州", date="2026-10-01", timePref="红眼")

🎯 Use Cases

▸ Business Travel Comparison — Simultaneously checks five platforms, finds the lowest price with one click, saving the trouble of switching between apps

▸ Holiday Travel — Filters by specified time preferences, quickly locates flights that fit your schedule

▸ Multi-Airport Cities — Automatically recognizes multiple airports in Beijing, Shanghai, and Chengdu, clearly marking departure and arrival airports

▸ Price Monitoring — Alerts for price anomalies, avoiding problematic tickets with abnormally low prices

⚙️ MCP Server Configuration

Standard Edition (Mac/Linux):

plaintext
{
  "mcpServers": {
    "flight-price-compare": {
      "command": "uvx",
      "args": ["flight-price-compare-mcp==4.0.0"]
    }
  }
}

Windows Edition:

plaintext
{
  "mcpServers": {
    "flight-price-compare": {
      "command": "cmd",
      "args": ["/c", "uvx", "flight-price-compare-mcp==4.0.0"]
    }
  }
}

📄 License

MIT

**Official site: ** [https://pypi.org/project/flight-price-compare-mcp/](https://pypi.org/project/flight-price-compare-mcp/)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `search`, `development`
- Tags: `search`, `developer tools`, `other`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `flight-price-compare-mcp==4.0.2`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/mako2026-flightpricecompare.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
