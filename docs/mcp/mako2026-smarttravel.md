---
title: "SmartTravel"
description: "🧳 All-in-One Travel Assistant 16-in-1 one-stop travel MCP service, covering itinerary planning, train tickets, flight tickets, hotels, attractions, food, transportation, weather, bus tickets, group to…"
---

# SmartTravel

🧳 All-in-One Travel Assistant 16-in-1 one-stop travel MCP service, covering itinerary planning, train tickets, flight tickets, hotels, attractions, food, transportation, weather, bus tickets, group to…

🧳 All-in-One Travel Assistant

16-in-1 one-stop travel MCP service, covering itinerary planning, train tickets, flight tickets, hotels, attractions, food, transportation, weather, bus tickets, group tours, cruises, vacation routes, and exclusive services for Marriott hotels.

✨ Core Features

▸ One-Stop Full Coverage — 16 tools cover the entire travel journey, from planning to booking in one go

▸ Natural Language Planning — Input "5-day family trip to Sanya" to generate a complete itinerary plan

▸ Multi-Source Data Aggregation — Data from Fliggy, AutoNavi, Tongcheng, and Tuniu aggregated

▸ Direct Booking Links — Search results come with booking links, click to place an order

▸ Zero Configuration Access — Use MCP URL directly without needing to apply for a Key

🛠 Tools

plan_travel - Intelligent Travel Planning

Describe your travel needs in natural language, and it will automatically recommend destinations, itinerary arrangements, and transportation and accommodation plans. After planning, you can continue to check tickets, book hotels, check the weather, and generate taxi links.

Parameters:

▸ query (string, ✅ required): Description of travel needs, such as "5-day family trip to Sanya with a budget of 10,000 RMB", "2-day weekend trip to Hangzhou"

search_train - Train Ticket Search

Query train tickets/high-speed rail tickets, returning real-time availability, schedules, and prices.

Parameters:

▸ query (string, ✅ required): Departure + destination + date, such as "Guangzhou to Beijing tomorrow"

search_flight - Flight Ticket Search

Query domestic flight tickets, returning real-time prices, flight schedules, and booking links.

Parameters:

▸ query (string, ✅ required): Departure + destination + date, such as "Shanghai to Beijing on June 25th"

search_hotel - Hotel Search

Search for hotel accommodations, returning real-time prices and booking links, supporting multi-dimensional filtering by star rating, price, and landmarks, with 8-field structured display.

Parameters:

▸ query (string, ✅ required): City + hotel keywords, such as "5-star hotel near the Bund in Shanghai, 300-800 RMB"

search_poi - Attraction Ticket Search

Search for attraction tickets, returning ticket prices and booking links, supporting city, keyword, and scenic area level filtering.

Parameters:

▸ query (string, ✅ required): City + attraction keywords, such as "Beijing Forbidden City tickets", "Shanghai Disneyland"

search_fast - Quick Search

Lightweight intent response within seconds, suitable for simple keyword search scenarios.

Parameters:

▸ query (string, ✅ required): Search keywords, such as "Sanya homestay", "Chengdu hotpot"

search_marriott_hotel - Marriott Hotel Search

Search for Marriott-branded hotels, with brand-specific filtering, returning real-time prices and booking links.

Parameters:

▸ query (string, ✅ required): City + brand keywords, such as "JW Marriott in Shanghai", "Ritz-Carlton in Beijing"

get_marriott_hotel_info - Marriott Hotel Details

Get detailed information about Marriott hotels, including facilities, policies, and images.

Parameters:

▸ hotel_id (string, ✅ required): Hotel ID, obtained from the search_marriott_hotel result

search_marriott_package - Marriott Hotel Package Search

Search for Marriott hotel packages, including meal and attraction combinations and other promotional offers.

Parameters:

▸ query (string, ✅ required): City + package keywords, such as "Marriott breakfast package in Shanghai"

search_food - Food Recommendations

Search for nearby restaurants and cuisine, returning ratings, average cost per person, and addresses.

Parameters:

▸ query (string, ✅ required): City + food keywords, such as "Chengdu hotpot recommendations", "Cantonese dim sum in Guangzhou"

search_transport - In-City Transportation Query

Query in-city transportation options, including subway/bus transfer routes, estimated taxi fares, and generate one-click taxi links. Only supports domestic cities.

Parameters:

▸ query (string, ✅ required): Departure + destination + city, such as "from Nanjing Road to the Bund in Shanghai"

search_weather - Weather Query

Query the weather forecast at the destination, understand the weather before departure to assist in itinerary planning and luggage preparation.

Parameters:

▸ query (string, ✅ required): City name, such as "Sanya weather", "Beijing weather for the next week"

bus_search - Bus Ticket Search

Search for long-distance bus and intercity bus schedules, returning departure times, vehicle types, ticket prices, availability, and booking links.

Parameters:

▸ departure (string, optional): Departure city, such as "Shanghai", "Beijing"

▸ destination (string, optional): Arrival city, such as "Hangzhou", "Suzhou"▸ date (string, optional): Departure date, such as "2026-06-25", default is today

travel_search - Group Tour Search

Search for group tours and free travel products, returning the number of travel days, price, included attractions, and booking links.

Parameters:

▸ departure (string, optional): Departure city, such as "Shanghai" or "Beijing"

▸ destination (string, optional): Destination, such as "Yunnan" or "Jiuzhaigou"

▸ date (string, optional): Departure date

▸ days (string, optional): Number of travel days, such as "5" or "7"

cruise_search - Cruise Search

Search for cruise travel products, returning the cruise brand, route, number of travel days, price, and booking link.

Parameters:

▸ departure (string, optional): Departure city, such as "Shanghai" or "Tianjin"

▸ destination (string, optional): Destination route, such as "Japan" or "Southeast Asia"

▸ month (string, optional): Departure month, such as "2026-07"

holiday_search - Holiday Route Search

Search for holiday travel routes, supporting keyword, departure city, budget, and duration filters.

Parameters:

▸ query (string, optional): Keywords, such as "Hainan vacation" or "Japan group tour"

▸ departure (string, optional): Departure city

▸ budget (string, optional): Budget range, such as "5000" or "3000-8000"

▸ days (string, optional): Duration, such as "5" or "7"

📝 Usage Examples

▸ "Sanya 5-day family trip budget 10,000" → plan_travel generates a 5-day itinerary for Sanya

▸ "Guangzhou to Beijing train ticket tomorrow" → search_train queries train tickets

▸ "Shanghai Bund five-star hotel" → search_hotel searches for hotels

▸ "Beijing Forbidden City ticket" → search_poi searches for attraction tickets

▸ "Chengdu hotpot recommendation" → search_food recommends food

▸ "From Nanjing Road to the Bund, Shanghai" → search_transport queries urban transportation

**Official site: ** [https://pypi.org/project/mcp-travel-smart-plan/](https://pypi.org/project/mcp-travel-smart-plan/)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `search`, `developer tools`, `location services`, `旅行规划`, `行程规划`, `旅游攻略`, `火车票`, `高铁票`, `机票查询`, `酒店搜索`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `mcp-travel-smart-plan==7.0.2`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/mako2026-smarttravel.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
