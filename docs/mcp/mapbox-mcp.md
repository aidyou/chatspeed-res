---
title: "Mapbox MCP 服务器"
description: "Mapbox MCP Server Node.js server implementing Model Context Protocol (MCP) for Mapbox APIs. Unlock Geospatial Intelligence for Your AI Applications The Mapbox MCP Server transforms any AI agent or application into a geos"
---

# Mapbox MCP 服务器

Mapbox MCP Server Node.js server implementing Model Context Protocol (MCP) for Mapbox APIs. Unlock Geospatial Intelligence for Your AI Applications The Mapbox MCP Server transforms any AI agent or application into a geos

# Mapbox MCP Server


Node.js server implementing Model Context Protocol (MCP) for Mapbox APIs.

## Unlock Geospatial Intelligence for Your AI Applications

The Mapbox MCP Server transforms any AI agent or application into a geospatially-aware system by providing seamless access to Mapbox's comprehensive location intelligence platform. With this server, your AI can understand and reason about places, navigate the physical world, and access rich geospatial data including:

- **Global geocoding** to convert addresses and place names to coordinates and vice versa
- **Points of interest (POI) search** across millions of businesses, landmarks, and places worldwide
- **Multi-modal routing** for driving, walking, and cycling with real-time traffic
- **Travel time matrices** to analyze accessibility and optimize logistics
- **Route optimization** to find the optimal visiting order for multiple stops (traveling salesman problem)
- **Map matching** to snap GPS traces to the road network for clean route visualization
- **Isochrone generation** to visualize areas reachable within specific time or distance constraints
- **Live, interactive map rendering** (`render_map_tool`) to display routes, search results, and your own custom GeoJSON on a real Mapbox GL JS map directly inside the chat
- **Static map images** to create visual representations of locations, routes, and geographic data
- **Offline geospatial calculations** for distance, area, bearing, buffers, and spatial analysis without requiring API calls

Whether you're building an AI travel assistant, logistics optimizer, location-based recommender, or any application that needs to understand "where", the Mapbox MCP Server provides the spatial intelligence to make it possible. You can also enable it on popular clients like Claude Desktop and VS Code. See below for details

![Mapbox MCP Server Demo](https://github.com/mapbox/mcp-server/blob/HEAD/assets/mapbox_mcp_server.gif)

# Usage

**A Mapbox access token is required to use this MCP server.**

## Hosted MCP Endpoint

For quick access, you can use our hosted MCP endpoint:

**Endpoint**: https://mcp.mapbox.com/mcp

For detailed setup instructions for different clients and API usage, see the [Hosted MCP Server Guide](https://github.com/mapbox/mcp-server/blob/HEAD/docs/hosted-mcp-guide.md).

To get a Mapbox access token:

1. Sign up for a free Mapbox account at [mapbox.com/signup](https://www.mapbox.com/signup/)
2. Navigate to your [Account page](https://account.mapbox.com/)
3. Create a new token or use the default public token

For more information about Mapbox access tokens, see the [Mapbox documentation on access tokens](https://docs.mapbox.com/help/dive-deeper/access-tokens/).

## Integration Guides

For detailed setup instructions for different integrations, refer to the following guides:

- [Claude Desktop Setup](https://github.com/mapbox/mcp-server/blob/HEAD/docs/claude-desktop-setup.md) - Instructions for configuring Claude Desktop to work with this MCP server
- [Goose Setup](https://github.com/mapbox/mcp-server/blob/HEAD/docs/goose-setup.md) - Setting up Goose AI agent framework
- [VS Code Setup](https://github.com/mapbox/mcp-server/blob/HEAD/docs/vscode-setup.md) - Setting up a development environment in Visual Studio Code
- [Cursor AI IDE Setup](https://github.com/mapbox/mcp-server/blob/HEAD/docs/cursor-setup.md) - Setting up a development environment in Cursor AI IDE
- [Smolagents Integration](https://github.com/mapbox/mcp-server/blob/HEAD/docs/using-mcp-with-smolagents/README.md) - Example showing how to connect Smolagents AI agents to Mapbox's tools
- **[Importing Tools Directly](https://github.com/mapbox/mcp-server/blob/HEAD/docs/importing-tools.md)** - Use Mapbox tools in your own applications without running the MCP server
- **[`render_map_tool` Guide](https://github.com/mapbox/mcp-server/blob/HEAD/docs/render-map-tool.md)** - The map visualization primitive: full payload schema and how to render your own data standalone, without any other Mapbox tool
- **[Elicitations](https://github.com/mapbox/mcp-server/blob/HEAD/docs/elicitations.md)** - How `search_and_geocode_tool` and `directions_tool` ask the user to disambiguate results or pick a route, and how they fall back gracefully when the client doesn't support it

## Example Prompts

Try these prompts with Claude Desktop or other MCP clients after setup:

### Location Grounding

For coordinate-first queries — _"what's near me"_, _"what neighborhood is this"_, _"what's reachable in N minutes"_ — use `ground_location_tool`. It composes reverse geocoding, category search, and isochrone in a single call, adaptively choosing the right strategy based on the query, and returns typed records (names, addresses, coordinates, distances, reachability polygons) with citations.

Each of the four prompts below exercises a different strategy in one tool call:

- **Neighborhood** — _"What neighborhood is 47.6097, -122.3408, and what's around me?"_
- **POI** — _"Coffee shops within a 10-minute walk of 40.7580, -73.9855"_
- **Region** — _"What can I reach in a 15-minute walk from 37.7749, -122.4194?"_
- **Routing** — _"Closest routable point to drop someone off at 34.0522, -118.2437"_

### Location Discovery

- "Find coffee shops within walking distance of the Empire State Building"
- "I want to go from Seattle to Portland, is there a Starbucks along the way?"
- "Show me gas stations along the route from Boston to New York"
- "What restaurants are near Times Square?"

### Navigation & Travel

- "Get driving directions from LAX to Hollywood with current traffic"
- "How long would it take to walk from Central Park to Times Square?"
- "Calculate travel time from my hotel (Four Seasons) to JFK Airport by taxi during rush hour"

### Visualization & Maps

- "Using the Mapbox map render tool, show me directions from the Golden Gate Bridge to Union Square in San Francisco" — renders a live, interactive route on a real Mapbox map
- "Create a map image showing the route from Golden Gate Bridge to Fisherman's Wharf with markers at both locations"
- "Show me a satellite view of Manhattan with key landmarks marked"
- "Generate a map highlighting all Starbucks locations within a mile of downtown Seattle"
- "Show a fill polygon over these coordinates: [...], with a marker labeled 'Warehouse' at [...]" — renders your own GeoJSON directly via `render_map_tool`, no other Mapbox tool needed

### Analysis & Planning

- "Show me areas reachable within 30 minutes of downtown Portland by car"
- "Calculate a travel time matrix between these 3 hotel locations (Marriott, Sheraton and Hilton) and the convention center in Denver"
- "Find the optimal route visiting these 3 tourist attractions (Golden Gate, Musical Stairs and Fisherman's Wharf) in San Francisco"
- "Optimize a delivery route for these 8 addresses: [list of addresses]"

### GPS & Route Matching

- "Clean up this GPS trace and show the actual route on roads: [list of coordinates with timestamps]"
- "Snap this recorded bicycle ride to the cycling network: [GPS coordinates]"
- "Match this driving route to the road network and show traffic congestion levels"

### Offline Geospatial Calculations

- "What's the distance in miles between these two coordinates?"
- "Calculate the area of this polygon in square kilometers"
- "Is the point at 37.7749°N, 122.4194°W inside this service area polygon?"
- "What's the bearing from San Francisco to New York?"
- "Find the midpoint between London and Paris"
- "Create a 5-mile buffer zone around this location"
- "Calculate the centroid of this neighborhood boundary"
- "What's the bounding box for these route coordinates?"
- "Simplify this complex polygon to reduce the number of points"

### Tips for Better Results

- Be specific about locations (use full addresses or landmark names)
- Specify your preferred travel method (driving, walking, cycling)
- Include time constraints when relevant ("during rush hour", "at 3 PM")
- Ask for specific output formats when needed ("as a map image", "in JSON format")

> **Detailed examples:** See [examples/search-along-route.md](https://github.com/mapbox/mcp-server/blob/HEAD/examples/search-along-route.md) for comprehensive examples of the search-along-route prompt with different use cases and MCP Inspector testing instructions.

## Resources

The MCP server exposes static reference data as **MCP resources**. Resources provide read-only access to data that clients can reference directly without making tool calls.

### Available Resources

#### Mapbox Categories Resource

**URI Pattern**: `mapbox://categories` or `mapbox://categories/{language}`

Access the complete list of available category IDs for use with the category search tool. Categories can be used to filter search results by type (e.g., "restaurant", "hotel", "gas_station").

**Examples**:

- `mapbox://categories` - Default (English) category list
- `mapbox://categories/ja` - Japanese category names
- `mapbox://categories/es` - Spanish category names

**Accessing Resources**:

- **Clients with native MCP resource support**: Use the `resources/read` MCP protocol method
- **Clients without resource support**: Use the `resource_reader_tool` with the resource URI

## Rich Map Previews (`render_map_tool`)

Every geospatial tool in this server (directions, isochrone, search, and more) can display its result as a live, interactive Mapbox GL JS map via **`render_map_tool`** — the server's single visualization primitive. It renders through the **MCP Apps** protocol (`@modelcontextprotocol/ext-apps`) as a self-contained HTML panel directly inside the chat, with a Fullscreen toggle, in supported clients:

- **Claude Desktop** ✅
- **VS Code with GitHub Copilot** ✅
- **Claude Code** ✅
- **[Goose](https://github.com/block/goose)** ✅

**You don't need any of this server's other tools to use it.** `render_map_tool` also accepts hand-composed GeoJSON directly — your own polygons, markers, and routes — with no dependency on `directions_tool`, `isochrone_tool`, or any other Mapbox API call. See **[the full `render_map_tool` guide](https://github.com/mapbox/mcp-server/blob/HEAD/docs/render-map-tool.md)** for the payload schema and a complete standalone example.

If you need a guaranteed static image in clients without MCP Apps support, use `static_map_image_tool` instead — it returns a base64-encoded PNG/JPEG that every client can display.

#### CLIENT_NEEDS_RESOURCE_FALLBACK

**Resource Fallback Tools (Opt-In for Non-Compliant Clients)**

Resources are a core MCP feature supported by most clients (Claude Desktop, VS Code, MCP Inspector, etc.). However, some clients (like smolagents) don't support resources at all. For these clients, the server can provide "resource fallback tools" that deliver the same content as resources but via tool calls.

**Fallback Tools:**

- `resource_reader_tool` - Generic fallback for reading any resource by URI
- `category_list_tool` - Provides access to category list (mapbox://categories)

**By default, these tools are NOT included** (assumes your client supports resources). If your client doesn't support resources, enable the fallback tools:

```bash
export CLIENT_NEEDS_RESOURCE_FALLBACK=true
```

**When to set this:**

- ✅ Set to `true` if using smolagents or other clients without resource support
- ❌ Leave unset (default) if using Claude Desktop, VS Code, MCP Inspector, or any resource-capable client
- ❌ Leave unset if unsure (most clients support resources)

## Tools

### Utility Tools

#### Resource Reader Tool

Provides access to MCP resources for clients that don't support the native MCP resource API. Use this tool to read resources like the category list.

**Parameters**:

- `uri`: The resource URI to read (e.g., `mapbox://categories`, `mapbox://categories/ja`)

**Example Usage**:

- Read default categories: `{"uri": "mapbox://categories"}`
- Read Japanese categories: `{"uri": "mapbox://categories/ja"}`

**Note**: If your MCP client supports native resources, prefer using the resource API directly for better performance.

### Offline Geospatial Tools

These tools perform geospatial calculations completely offline without requiring Mapbox API calls. They use [Turf.js](https://turfjs.org/) for accurate geographic computations and work anywhere, even without internet connectivity.

#### Distance Tool

Calculate the distance between two geographic coordinates using the Haversine formula.

**Features**:

- Supports multiple units: kilometers, miles, meters, feet, nautical miles
- Accurate great-circle distance calculation
- No API calls required

**Example Usage**: "What's the distance between San Francisco (37.7749°N, 122.4194°W) and New York (40.7128°N, 74.0060°W)?"

#### Points Within Polygon Tool

Test one or more points against a polygon or multipolygon, returning only those inside. Handles a single point or a batch in one call.

**Features**:

- Works with complex polygons including holes
- Supports multipolygons
- Batch-tests any number of points in one call
- Useful for geofencing, delivery zone validation, and customer segmentation

**Example Usage**: "Which of these delivery addresses are inside our service area?"

#### Destination Tool

Calculate a destination point given a starting point, bearing, and distance using geodesic (great-circle) offset.

**Features**:

- Straight-line offset, not a routed path
- Useful for "find a point 5km north of X" or constructing search offsets
- No API calls required

**Example Usage**: "What's the point 10km northeast of the Space Needle?"

#### Bearing Tool

Calculate the compass direction (bearing) from one coordinate to another.

**Features**:

- Returns bearing in degrees (0-360°)
- Provides cardinal direction (N, NE, E, SE, S, SW, W, NW)
- Useful for navigation and directional queries

**Example Usage**: "What direction should I head to go from here to the airport?"

#### Midpoint Tool

Find the geographic midpoint between two coordinates along the great circle path.

**Features**:

- Calculates true midpoint on Earth's curved surface
- Useful for meeting point suggestions
- Handles long-distance calculations correctly

**Example Usage**: "What's halfway between San Francisco and New York?"

#### Centroid Tool

Calculate the geometric center (centroid) of a polygon or multipolygon.

**Features**:

- Works with complex shapes
- Returns arithmetic mean of all points
- Useful for placing labels or markers

**Example Usage**: "Where should I place a marker for this neighborhood boundary?"

#### Area Tool

Calculate the area of a polygon.

**Features**:

- Supports multiple units: square meters, square kilometers, acres, hectares, square miles, square feet
- Accurate area calculation on Earth's surface
- Works with polygons of any size

**Example Usage**: "What's the area of this park in acres?"

#### Bounding Box Tool

Calculate the minimum bounding box (bbox) that contains a geometry.

**Features**:

- Works with points, lines, polygons, and multipolygons
- Returns [minLongitude, minLatitude, maxLongitude, maxLatitude]
- Useful for viewport calculations and spatial indexing

**Example Usage**: "What's the bounding box for this route?"

#### Buffer Tool

Create a buffer zone (polygon) around a point, line, or polygon.

**Features**:

- Supports multiple distance units
- Creates circular buffers around points
- Useful for proximity analysis and creating zones of influence

**Example Usage**: "Show me a 5km buffer zone around this location"

#### Simplify Tool

Reduce the number of vertices in a line or polygon using the Douglas-Peucker algorithm.

**Features**:

- Configurable tolerance for detail level
- Preserves overall shape while reducing complexity
- Useful for reducing file sizes and improving rendering performance
- Option to maintain topology (prevent self-intersections)

**Example Usage**: "Simplify this complex boundary to reduce the number of points"

#### Length Tool

Measure the total length of a line defined by a series of coordinates.

**Features**:

- Supports kilometers, miles, meters, and feet
- Useful for measuring a drawn route, path, or boundary without a routing API call

**Example Usage**: "How long is this hiking trail?"

#### Convex Tool

Compute the convex hull of a set of points — the smallest convex polygon containing all of them.

**Features**:

- Useful for bounding-area analysis or estimating coverage area
- Works offline without API calls

**Example Usage**: "What's the smallest polygon that contains all of these store locations?"

#### Nearest Point Tool

Find the nearest point in a collection to a given target point.

**Features**:

- More efficient than calling `distance_tool` for each candidate and sorting
- Useful for finding the closest store, stop, or landmark to a location

**Example Usage**: "Which of these stores is closest to my current location?"

#### Nearest Point on Line Tool

Snap a point to the nearest position on a line or route, returning that point and the distance to it.

**Features**:

- Useful for "which point on this route is closest to my location?" or map-matching without an API call

**Example Usage**: "Where on this hiking trail am I closest to right now?"

#### Union, Intersect, and Difference Tools

Combine or compare two or more polygons — `union_tool` merges them into one geometry, `intersect_tool` finds the area they share, and `difference_tool` subtracts one from another.

**Features**:

- Useful for combining service areas, finding coverage overlap, or computing exclusion zones (e.g. "what's covered by zone A but not zone B?")
- Works entirely offline — no API calls required
- Each returns a `render_map_tool` reference so the result can be visualized directly

**Example Usage**: "Combine these two delivery zones into one coverage area" / "Where do these two isochrones overlap?" / "What part of this service area isn't covered by our 15-minute isochrone?"

### Mapbox API Tools

#### Category List Tool (Deprecated)

**⚠️ Deprecated**: Use the `resource_reader_tool` with URI `mapbox://categories` instead, or access the `mapbox://categories` resource directly if your client supports MCP resources.

This tool is maintained for backward compatibility with clients that don't support MCP resources or the resource_reader_tool.

#### Matrix Tool

Calculates travel times and distances between multiple points using [Mapbox Matrix API](https://www.mapbox.com/matrix-api). Features include:

- Efficient one-to-many, many-to-one or many-to-many routing calculations
- Support for different travel profiles (driving-traffic, driving, walking, cycling)
- Departure time specification for traffic-aware calculations
- Route summarization with distance and duration metrics
- Control approach (curb/unrestricted) and range of allowed departure bearings

#### Static image tool

Generates static map images using the [Mapbox static image API](https://docs.mapbox.com/api/maps/static-images/). Features include:

- Custom map styles (streets, outdoors, satellite, etc.)
- Adjustable image dimensions and zoom levels
- Support for multiple markers with custom colors and labels
- Overlay options including polylines and polygons
- Auto-fitting to specified coordinates

#### Category search tool

Performs a category search using the [Mapbox Search Box category search API](https://docs.mapbox.com/api/search/search-box/#category-search). Features include:

- Search for points of interest by category (restaurants, hotels, gas stations, etc.)
- Filtering by geographic proximity
- Customizable result limits
- Rich metadata for each result
- Support for multiple languages

#### Reverse geocoding tool

Performs reverse geocoding using the [Mapbox geocoding V6 API](https://docs.mapbox.com/api/search/geocoding/#reverse-geocoding). Features include:

- Convert geographic coordinates to human-readable addresses
- Customizable levels of detail (street, neighborhood, city, etc.)
- Results filtering by type (address, poi, neighborhood, etc.)
- Support for multiple languages
- Rich location context information

#### Ground location tool

Answers "what's near this coordinate" questions in a single call — place name, nearby points of interest, and travel-time reachability — sourced from live Mapbox data with citations. Use this instead of chaining `reverse_geocode_tool` with a web search.

**Features**:

- Classifies the query (routing, neighborhood context, POI search, or region/reachability) and fetches only the relevant data
- Nearby POI search by category, when requested
-

**官方网站：** [https://github.com/mapbox/mcp-server](https://github.com/mapbox/mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`mapbox`, `maps`, `geolocation`, `official`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`docker`
- 参数：`run -i --rm --env MAPBOX_ACCESS_TOKEN=YOUR_TOKEN mapbox-mcp-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/mapbox-mcp.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
