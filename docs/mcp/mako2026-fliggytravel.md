---
title: "FliggyTravel"
description: "✈️ Fliggy Travel One-stop travel MCP service, covering 11 tools such as flights, hotels, train tickets, attractions, food, and in-city transportation, fully compatible with the official Fliggy MCP sch…"
---

# FliggyTravel

✈️ Fliggy Travel One-stop travel MCP service, covering 11 tools such as flights, hotels, train tickets, attractions, food, and in-city transportation, fully compatible with the official Fliggy MCP sch…

✈️ Fliggy Travel

One-stop travel MCP service, covering 11 tools such as flights, hotels, train tickets, attractions, food, and in-city transportation, fully compatible with the official Fliggy MCP schema.

✨ Core Features

▸ Official Compatibility — Fliggy tool parameter names are exactly the same (camelCase) as the official MCP, allowing seamless endpoint switching

▸ Zero-Configuration Access — Built-in proxy service, no need to apply for an API Key, ready to use upon configuration

▸ Nine Layers of Security — Multiple reinforcements including rate limiting, caching, daily limits, and log desensitization, ensuring stability and reliability

▸ Multiple Data Sources — Fliggy Travel + Amap, covering all travel scenarios

▸ 11 Tools — Flights/Hotels/Trains/Attractions/Food/Transport/Marriott/Travel Planning/Rapid Search

🛠 Tools

travel_plan — Travel Planning

Generates personalized travel plans based on destination and travel needs, including itinerary arrangements, attraction recommendations, and accommodation suggestions.

Parameters:

▸ query (required) — Description of the travel plan in natural language, including destination + days + preferences, e.g., "Sanya 5-day family travel guide"

search_flight — Flight Search

Queries real-time ticket prices, flight numbers, and departure/arrival times for domestic flights. Supports precise filtering by origin, destination, date, and cabin class, returning real-time prices and booking links.

Parameters:

▸ origin (required) — Origin city name, e.g., "Shanghai"

▸ destination (optional) — Destination city name, e.g., "Sanya"

▸ depDate (optional) — Departure date, format YYYY-MM-DD, defaults to today if not provided

▸ backDate (optional) — Return date, format YYYY-MM-DD, single trip if not provided

▸ seatClassName (optional) — Cabin class, e.g., "Economy", "Business", "First Class"

▸ journeyType (optional) — Journey type, 0=one-way, 1=direct, 2=transfer, default is 0

search_train — Train Ticket Search

Queries real-time ticket prices, train numbers, and departure/arrival times for domestic trains. Supports precise filtering by origin, destination, date, and seat class.

Parameters:

▸ origin (required) — Origin city name, e.g., "Shanghai"

▸ destination (optional) — Destination city name, e.g., "Hangzhou"

▸ depDate (optional) — Departure date, format YYYY-MM-DD, defaults to today if not provided

▸ backDate (optional) — Return date, format YYYY-MM-DD, single trip if not provided

▸ seatClassName (optional) — Seat class, e.g., "Second Class", "First Class", "Business Class"

▸ journeyType (optional) — Journey type, 0=one-way, 1=round-trip, 2=transfer, default is 0

search_hotel — Hotel Search

Searches for hotels, returning real-time prices and booking links. Supports multi-dimensional filtering by destination, star rating, price, keywords, etc.

Parameters:

▸ destName (required) — Destination, city or area name, e.g., "Sanya", "West Lake, Hangzhou"

▸ checkInDate (optional) — Check-in date, format YYYY-MM-DD

▸ checkOutDate (optional) — Check-out date, format YYYY-MM-DD

▸ keyWords (optional) — Keywords, e.g., "family-friendly", "business", "sea view"

▸ hotelStars (optional) — Hotel star ratings, 1-5, multiple selections separated by commas, e.g., "4,5"

▸ maxPrice (optional) — Maximum price (CNY)

▸ hotelTypes (optional) — Hotel types: hotel, homestay, inn

▸ hotelBedTypes (optional) — Bed types: king bed, twin beds, multiple beds

search_poi — Attraction Tickets

Searches for attraction tickets, returning ticket prices and booking links. Supports filtering by keywords, city, type, and level.

Parameters:

▸ keyword (optional) — Keyword for the attraction name, e.g., "Forbidden City", "Great Wall"

▸ cityName (optional) — City name, e.g., "Hangzhou", "Xi'an"

▸ category (optional) — Attraction type, e.g., "natural scenery", "theme park", "cultural heritage"

▸ poiLevel (optional) — Attraction level 1-5 (5 being 5A)

search_food — Food Recommendations

Searches for nearby restaurants and food based on location, supporting cuisine filtering. Returns restaurant name, rating, average cost per person, and address.

Parameters:

▸ query (required) — Food search description in natural language, including location + optional cuisine, e.g., "hotpot near Nanjing Road, Shanghai"

search_transport — In-City TransportationQuery the estimated taxi fare and public transportation routes from A to B. Returns driving distance/time/cost and public transit options.

Parameters:

▸ query (required) — Description of the transportation query in natural language, including city + departure point + destination, e.g., "Shanghai Pudong Airport to the Bund"

search_fast — Fast Search

Fliggy's general fast search, quickly queries information on attractions, hotels, tickets, and travel packages. Suitable for simple keyword searches, faster than AI search.

Parameters:

▸ query (required) — Search term, such as "Sanya hotel", "Beijing Forbidden City ticket", "Shanghai Disneyland"

search_marriott_hotel — Marriott Hotel Search

Searches for hotels under the Marriott Group (including Marriott, Sheraton, Westin, Ritz-Carlton, etc.). Supports filtering by destination, date, and price.

Parameters:

▸ destName (required) — Destination, city or area name, e.g., "Shanghai", "Sanya"

▸ checkInDate (optional) — Check-in date, format YYYY-MM-DD

▸ checkOutDate (optional) — Check-out date, format YYYY-MM-DD

▸ keyWords (optional) — Keywords, such as "business", "vacation"

▸ maxPrice (optional) — Maximum price (CNY)

▸ hotelBedTypes (optional) — Bed types: King Room, Twin Room

get_marriott_hotel_info — Marriott Hotel Details

Fetches detailed information about a specific hotel under the Marriott Group, including facilities, ratings, room types, etc.

Parameters:

▸ hotelName (optional) — Hotel name, e.g., "W Shanghai - The Bund". At least one of hotelName or shId must be provided.

▸ shId (optional) — Hotel ID (if available). At least one of hotelName or shId must be provided.

▸ reviewKeyword (optional) — Review keywords, such as "breakfast", "service", "location"

search_marriott_package — Marriott Package Search

Searches for hotel package products offered by the Marriott Group (e.g., breakfast included, vacation packages, etc.).

Parameters:

▸ keyword (optional) — Search keyword

▸ hotelName (optional) — Hotel name

▸ provinceOrCity (optional) — Province or city

📝 Usage Examples

▸ "Honeymoon in Sanya for 5 days with a budget of 10,000 CNY" → travel_plan(query="Honeymoon in Sanya for 5 days with a budget of 10,000 CNY")

▸ "Flights from Shanghai to Beijing tomorrow" → search_flight(origin="Shanghai", destination="Beijing", depDate="2026-08-27")

▸ "Hotels near West Lake in Hangzhou within 500 CNY" → search_hotel(destName="West Lake, Hangzhou", maxPrice=500)

▸ "Hotpot near Nanjing Road in Shanghai" → search_food(query="Hotpot near Nanjing Road in Shanghai")

▸ "How to get from Pudong Airport to the Bund" → search_transport(query="Pudong Airport to the Bund, Shanghai")

▸ "Marriott Hotel in Shanghai within 1000 CNY" → search_marriott_hotel(destName="Shanghai", maxPrice=1000)

🎯 Use Cases

▸ Travel Agent — Provides full-scenario travel query capabilities for agents

▸ IDE Assistant — Quickly queries travel information in IDEs like Cursor/Cherry Studio/Windsurf

▸ Price Comparison System — Serves as a Fliggy data source for multi-source price comparison platforms

▸ Customer Service Robot — Provides real-time travel information queries for e-commerce and travel customer service

📄 License

MIT

**Official site: ** [https://pypi.org/project/mcp-fliggy-travel/](https://pypi.org/project/mcp-fliggy-travel/)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `search`, `developer tools`, `location services`, `飞猪旅行`, `旅行规划`, `火车票查询`, `机票查询`, `酒店搜索`, `景点门票`, `美食推荐`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `mcp-fliggy-travel==0.4.1`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/mako2026-fliggytravel.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
