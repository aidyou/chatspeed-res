---
title: "GaodeMapPro"
description: "🗺️ AMap MCP Service The AMap MCP service, ready to use without a key, covers 17 location capabilities, and requires no application for an AMap API Key, making it instantly usable out of the box. ✨ Cor…"
---

# GaodeMapPro

🗺️ AMap MCP Service The AMap MCP service, ready to use without a key, covers 17 location capabilities, and requires no application for an AMap API Key, making it instantly usable out of the box. ✨ Cor…

🗺️ AMap MCP Service

The AMap MCP service, ready to use without a key, covers 17 location capabilities, and requires no application for an AMap API Key, making it instantly usable out of the box.

✨ Core Features

▸ Zero Configuration — No need to apply for an AMap API Key or fill in any environment variables; directly connect with the MCP URL and start using it.

▸ 17 Capabilities — Comprehensive coverage including geocoding, POI search, route planning, weather query, administrative division queries, and more.

▸ Address-based Routes — Directly input addresses to plan driving/public transit/walking/cycling routes without manually converting to latitude and longitude.

▸ Exclusive Features — Input suggestions (auto-complete for search boxes) and administrative division queries, which are not available in other AMap MCP services.

▸ Enterprise-level Proxy — Server-side hosted API Keys ensure stability and reliability, free from daily limits imposed on personal keys.

🛠 Tools

geocode — Geocoding

Converts detailed structured addresses into latitude and longitude coordinates, supporting landmark scenic spots and building name resolution.

▸ address — Structured address, e.g., "No. 6 Futong East Street, Chaoyang District, Beijing"

▸ city — Specified city (optional), e.g., "Beijing"

regeocode — Reverse Geocoding

Converts AMap latitude and longitude coordinates into administrative division address information.

▸ location — Latitude and longitude coordinates, format "lng,lat", e.g., "116.397428,39.90923"

poi_search — Keyword Search for POIs

Searches for POIs based on keywords, returning a list of related location information.

▸ keywords — Search keywords, such as "restaurant" or "Home Inn"

▸ city — Query city (optional), e.g., "Beijing"

▸ citylimit — Whether to limit the search within the city range, "true" or "false", default is "false"

poi_around — Nearby POI Search

Searches for points of interest within a specified radius based on the central point coordinates and keywords.

▸ location — Central point's latitude and longitude, format "lng,lat"

▸ keywords — Search keywords (optional), e.g., "gas station"

▸ radius — Search radius, in meters, default is 1000, maximum is 50000

poi_detail — POI Details

Queries detailed information about a POI, requiring the POI ID obtained from keyword or nearby searches.

▸ id — POI ID, obtained from the results of keyword or nearby searches

input_tips — Input Suggestions

Returns a list of matching POI suggestions based on user input keywords, suitable for auto-completion in search boxes.

▸ keywords — Input keywords, e.g., "KFC"

▸ city — Query city (optional)

▸ datatype — Data type, "all" for all, "poi" for only POIs, "bus" for only buses, default is "all"

driving_route — Driving Route Planning

Plans driving routes based on the origin and destination latitude and longitude.

▸ origin — Origin's latitude and longitude, format "lng,lat"

▸ destination — Destination's latitude and longitude, format "lng,lat"

transit_route — Public Transit Route Planning

Plans travel routes integrating trains, buses, subways, and other public transportation methods. The destination city must be provided for intercity scenarios.

▸ origin — Origin's latitude and longitude, format "lng,lat"

▸ destination — Destination's latitude and longitude, format "lng,lat"

▸ city — Origin city, e.g., "Beijing"

▸ cityd — Destination city (required for intercity), e.g., "Shanghai"

walking_route — Walking Route Planning

Plans walking routes up to 100km based on the origin and destination latitude and longitude.

▸ origin — Origin's latitude and longitude, format "lng,lat"

▸ destination — Destination's latitude and longitude, format "lng,lat"

cycling_route — Cycling Route Planning

Plans cycling routes based on the origin and destination latitude and longitude, supporting up to 500km.

▸ origin — Origin's latitude and longitude, format "lng,lat"

▸ destination — Destination's latitude and longitude, format "lng,lat"

driving_route_by_address — Driving Route (Address Version)

Directly input addresses to plan driving routes without manually converting to latitude and longitude, recommended for priority use.

▸ origin_address — Origin address, e.g., "No. 6 Futong East Street, Chaoyang District, Beijing"

▸ destination_address — Destination address, e.g., "No. 10 Shangdi 10th Street, Haidian District, Beijing"

▸ origin_city — Origin city (optional), used to improve geocoding accuracy

▸ destination_city — Destination city (optional)

transit_route_by_address — Public Transit Route (Address Version)

Directly input addresses to plan public transit routes without manually converting to latitude and longitude, recommended for priority use.▸ origin_address — Origin address

▸ destination_address — Destination address

▸ city — Origin city

▸ cityd — Destination city (required for inter-city routes)

▸ origin_city — Origin city (for geocoding, optional)

▸ destination_city — Destination city (for geocoding, optional)

walking_route_by_address — Walking route (address version)

You can plan a walking route by directly entering the addresses without manually converting them to latitude and longitude.

▸ origin_address — Origin address

▸ destination_address — Destination address

▸ origin_city — Origin city (optional)

▸ destination_city — Destination city (optional)

cycling_route_by_address — Cycling route (address version)

You can plan a cycling route by directly entering the addresses without manually converting them to latitude and longitude.

▸ origin_address — Origin address

▸ destination_address — Destination address

▸ origin_city — Origin city (optional)

▸ destination_city — Destination city (optional)

weather — Weather query

Query weather information for a specified city based on the city name or adcode.

▸ city — City name or adcode, such as "Beijing" or "110000"

district — Administrative division query

Query administrative division information for provinces, cities, and districts. Supports keyword search and level control.

▸ keywords — Search keywords (optional), such as "Beijing"; if left blank, it returns a list of all provincial-level divisions

▸ subdistrict — Number of sub-levels, 0 for no return, 1 for one level, 2 for two levels, 3 for three levels, default is 1

ip_location — IP location

Locate the position based on the IP address. If no IP is provided, it will locate the IP of the current request.

▸ ip — IP address (optional), such as "114.247.50.1"; if left blank, it locates the current IP

📝 Usage Examples

▸ "Find the latitude and longitude of Tiananmen in Beijing" → geocode

▸ "What gas stations are within 3 kilometers?" → poi_around

▸ "How to walk from Beijing Station to Tiananmen" → walking_route_by_address

▸ "Driving route from Beijing to Shanghai" → driving_route_by_address

▸ "What's the weather like in Shanghai tomorrow" → weather

▸ "What can be recommended by entering 'KFC'" → input_tips

Applicable Scenarios

▸ Travel planning agent for location queries and route planning

▸ Local life assistant for POI search and nearby recommendations

▸ Smart customer service for address parsing and weather queries

▸ IDE plugin for geocoding and travel suggestions

**Official site: ** [https://pypi.org/project/mcp-gaode-map/](https://pypi.org/project/mcp-gaode-map/)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `search`, `developer tools`, `location services`, `高德地图`, `路线规划`, `周边搜索`, `位置服务`, `驾车导航`, `步行导航`, `骑行路线`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `--from mcp-gaode-map==1.2.0 mcp-gaode-map`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/mako2026-gaodemappro.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
