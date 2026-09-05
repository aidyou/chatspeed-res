---
title: "mcp-rollinggo-flight"
description: "✈️ RollingGo Global Flight Search and Booking Search for global flights in one sentence, supporting direct input of Chinese city names, separate display of direct and connecting flights, Chinese mappi…"
---

# mcp-rollinggo-flight

✈️ RollingGo Global Flight Search and Booking Search for global flights in one sentence, supporting direct input of Chinese city names, separate display of direct and connecting flights, Chinese mappi…

✈️ RollingGo Global Flight Search and Booking

Search for global flights in one sentence, supporting direct input of Chinese city names, separate display of direct and connecting flights, Chinese mapping of airline codes, filtering of non-civil airports, and clear value-for-money tags. New features include seat availability and baggage allowance queries, providing all travel information at once.

✨ Core Features

▸ Direct Input of Chinese City Names — Over 100 city mappings, simply say "Beijing to Tokyo" to search, no need to remember airport codes

▸ Chinese Mapping of Airline Codes — Over 60 airlines, CA→Air China, NH→ANA, SQ→Singapore Airlines, making it easy to read

▸ Filtering of Non-Civil Airports — Automatically excludes military bases, ferry terminals, helipads, and other non-civil facilities

▸ Layover Waiting Time — Clearly displays layover duration for connecting flights, helping to assess the reasonableness of transfers

▸ Value-for-Money Tag SmartValueScore — Integrates price, duration, and timing scores to quickly identify high-value flights

▸ Seat Availability Query — View the distribution of available seats across different cabin classes, making seat selection and booking more informed

▸ Baggage Allowance Query — Clearly shows checked and carry-on baggage limits, avoiding extra charges for oversized luggage

🛠 Tools

search_flights — Global Flight Search

Query real-time prices and schedules for global flights, supporting Chinese city names, cabin class filtering, one-way/round-trip, and separate display of direct and connecting flights.

Parameters:

▸ from_city (required) — Departure city, supports Chinese (e.g., "北京", "上海", "东京") or city codes (e.g., "BJS", "SHA"), Chinese names are automatically mapped to codes

▸ to_city (required) — Arrival city, supports Chinese (e.g., "三亚", "首尔", "曼谷") or city codes (e.g., "SYX", "SEL", "BKK")

▸ from_date (required) — Departure date, format YYYY-MM-DD, e.g., "2026-06-15"

▸ from_airport (optional) — Departure airport code, e.g., "PEK", "PVG", used to specify the exact airport

▸ to_airport (optional) — Arrival airport code, e.g., "NRT", "HKT", used to specify the exact airport

▸ cabin_grade (optional) — Cabin class: ECONOMY=经济舱 (default), BUSINESS=商务舱, FIRST=头等舱

▸ trip_type (optional) — Trip type: ONE_WAY=单程 (default), ROUND_TRIP=往返

▸ ret_date (optional) — Return date, required for round trips, format YYYY-MM-DD

▸ adult_number (optional) — Number of adults, default is 1

▸ child_number (optional) — Number of children, default is 0

search_airports — Airport/City Code Search

Search for airport information by keyword, returning cityCode and airportCode for flight searches. Chinese city names are prioritized through built-in mappings, and non-civil airports are automatically filtered out.

Parameters:

▸ keyword (required) — Search keyword, supports city name (e.g., "杭州"), airport name (e.g., "浦东"), or IATA code (e.g., "PVG")

check_flight_seats — Seat Availability Query

Query the distribution of available seats on a specified flight, supporting cabin class filtering, allowing you to understand seat availability before traveling and make more informed seat selections and bookings.

Parameters:

▸ flight_id (required) — Flight ID, obtained from search_flights results

▸ cabin_grade (optional) — Cabin class: ECONOMY=经济舱 (default), BUSINESS=商务舱, FIRST=头等舱

check_baggage_allowance — Baggage Allowance Query

Query the checked and carry-on baggage limits for a flight, as policies vary by cabin class and airline, confirming this information before traveling can help avoid extra charges.

Parameters:

▸ flight_id (required) — Flight ID, obtained from search_flights results

▸ cabin_grade (optional) — Cabin class: ECONOMY=经济舱 (default), BUSINESS=商务舱, FIRST=头等舱

📝 Usage Examples

▸ "Flights from Shanghai to Beijing tomorrow" → search_flights(from_city="上海", to_city="北京", from_date="2026-06-04")

▸ "Price of tickets from Beijing to Tokyo next week" → search_flights(from_city="北京", to_city="东京", from_date="2026-06-10")

▸ "Economy class tickets for a family of three from Guangzhou to Bangkok during summer vacation" → search_flights(from_city="广州", to_city="曼谷", from_date="2026-07-01", adult_number=2, child_number=1)

▸ "Round-trip business class tickets from Shanghai to Paris" → search_flights(from_city="上海", to_city="巴黎", from_date="2026-07-01", trip_type="ROUND_TRIP", ret_date="2026-07-10", cabin_grade="BUSINESS")▸ "Which airports are in Hangzhou" → search_airports(keyword="杭州")

▸ "Which airport is PVG" → search_airports(keyword="PVG")

▸ "Are there any seats left on this flight" → check_flight_seats(flight_id="CA1234", cabin_grade="ECONOMY")

▸ "How much baggage can be checked on this flight" → check_baggage_allowance(flight_id="CA1234", cabin_grade="ECONOMY")

Applicable Scenarios

▸ Business Travel — Quickly query flight schedules and prices, with direct and connecting flights presented separately for efficient price comparison and decision-making.

▸ Trip Planning — Directly input Chinese city names without needing to look up airport codes, completing the flight search in one go.

▸ Seat Confirmation — Check the remaining seats on a flight, and get ahead of full booking situations for popular flights.

▸ Luggage Preparation — Confirm luggage allowances before departure to avoid unexpected overcharge fees at the airport.

▸ Airport Information Verification — When unsure which airport corresponds to a city, quickly query cityCode and airportCode.

**Official site: ** [https://pypi.org/project/mcp-rollinggo-flight/](https://pypi.org/project/mcp-rollinggo-flight/)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `search`, `developer tools`, `全球航班`, `航班查询`, `机票搜索`, `国际航班`, `国内航班`, `ai航班查询`, `机票比价`, `机票查询`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `mcp-rollinggo-flight==2.0.1`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/mako2026-rollinggo-flight.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
