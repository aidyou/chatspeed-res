---
title: "baidu-maps"
description: "Baidu Maps has fully embraced the MCP protocol - the first map service provider in China to support it. The Baidu Maps MCP Server exposes 10 MCP-standard API endpoints covering reverse geocoding, plac…"
---

# baidu-maps

Baidu Maps has fully embraced the MCP protocol - the first map service provider in China to support it. The Baidu Maps MCP Server exposes 10 MCP-standard API endpoints covering reverse geocoding, plac…

# Baidu Maps MCP Server

## Overview

Baidu Maps API is now fully compatible with the [MCP protocol](https://modelcontextprotocol.io/), making Baidu Maps the first map service provider in China to support MCP.

The Baidu Maps MCP Server provides 10 MCP-protocol-compliant API endpoints covering reverse geocoding, place search, route planning, and more.

Built on the `MCP Python SDK` and `MCP TypeScript SDK`, it can be quickly integrated by any MCP-capable agent assistant (such as `Claude`, `Cursor`, or `Qianfan AppBuilder`).

**We strongly recommend connecting to the Baidu Maps MCP Server via [SSE](https://lbsyun.baidu.com/faq/api?title=mcpserver/quickstart) for lower latency and higher stability. Please remember to enable the `MCP (SSE)` service for your AK in the [console](https://lbsyun.baidu.com/apiconsole/key).**

## Tools

1. Geocoding `map_geocode`
    - Description: Resolves an address into location coordinates; the more complete and accurate the address structure, the higher the coordinate precision
    - Parameters: `address` address text
    - Output: `location` latitude/longitude coordinates

2. Reverse geocoding `map_reverse_geocode`
    - Description: Given latitude/longitude coordinates, returns the address description, administrative division, roads, and related POI info at that location
    - Parameters:
      - `latitude` latitude coordinate
      - `longitude` longitude coordinate
    - Output: semantic address info such as `formatted_address`, `uid`, `addressComponent`

3. Place search `map_search_places`
    - Description: Supports searching for places within a city (down to `city` level) as well as nearby places within a circular region
    - Parameters:
      - `query` search keyword, by name or type; separate multiple keywords with English commas, e.g. `query=Tiananmen,Food`
      - `tag` type preference, e.g. `tag=Food` or `tag=Food,Hotel`
      - `region` administrative division, formatted as `region=cityname` or `region=citycode`
      - `location` center coordinates of the circular search, formatted as `location=lat,lng`
      - `radius` radius of the circular search
    - Output: POI list including `name`, `location`, `address`, etc.

4. Place details `map_place_details`
    - Description: Retrieves detail info for a POI by its uid, such as rating, business hours, etc. (different POI types expose different detail data)
    - Parameters: `uid` unique identifier of the POI
    - Output: POI details including `name`, `location`, `address`, `brand`, `price`, etc.

5. Batch route matrix `map_directions_matrix`
    - Description: Computes route distance and travel time between origin and destination coordinates; supports driving, cycling, and walking. For walking, the distance between any origin and destination must not exceed 200 km. Batch driving routing supports up to 100 routes per call, and the product of the number of origins and destinations must not exceed 100.
    - Parameters:
      - `origins` list of origin coordinates, formatted as `origins=lat,lng`, multiple origins separated by `|`
      - `destinations` list of destination coordinates, formatted as `destinations=lat,lng`, multiple destinations separated by `|`
      - `model` routing mode: `driving`, `walking`, or `riding`; defaults to `driving`
    - Output: duration and distance for each route, including `distance`, `duration`, etc.

6. Route planning `map_directions`
    - Description: Plans a travel route and duration from origin to destination by name or coordinates; supports driving, walking, cycling, and transit
    - Parameters:
      - `origin` origin place name or coordinates, formatted as `origin=lat,lng`
      - `destination` destination place name or coordinates, formatted as `destination=lat,lng`
      - `model` travel mode: `driving`, `walking`, `riding`, or `transit`; defaults to `driving`
    - Output: route details including `steps`, `distance`, `duration`, etc.

7. Weather query `map_weather`
    - Description: Queries real-time weather and a 5-day forecast by administrative division or coordinates
    - Parameters:
      - `district_id` administrative division code
      - `location` coordinates, formatted as `location=lng,lat`
    - Output: weather info including `temperature`, `weather`, `wind`, etc.

8. IP location `map_ip_location`
    - Description: Returns the location and city name for a given IP, useful for locating an IP or the user's current position. The `ip` parameter is optional; if empty, the local machine's IP is used (supports IPv4 and IPv6).
    - Parameters:
      - `ip` (optional) the IP address to locate
    - Output: the current city and the city center `location`

9. Real-time traffic `map_road_traffic`
    - Description: Queries real-time traffic congestion by road name or region shape (rectangle, polygon, or circle).
    - Parameters:
      - `model` traffic query type (`road`, `bound`, `polygon`, `around`; defaults to `road`)
      - `road_name` road name and direction, required when `model=road` (e.g. `Chaoyang Rd southbound`)
      - `city` city name or adcode, required when `model=road` (e.g. `Beijing`)
      - `bounds` coordinates of the bottom-left and top-right corners of the region, required when `model=bound` (e.g. `39.9,116.4;39.9,116.4`)
      - `vertexes` vertex coordinates of the polygon region, required when `model=polygon` (e.g. `39.9,116.4;39.9,116.4;39.9,116.4;39.9,116.4`)
      - `center` center coordinates of the circular region, required when `model=around` (e.g. `39.912078,116.464303`)
      - `radius` radius of the circular region in meters, range `[1,1000]`, required when `model=around` (e.g. `200`)
    - Output: traffic info including `road_name`, `traffic_condition`, etc.

10. POI extraction `map_poi_extract`
    - Description: Only available when the given `API_KEY` has **advanced permissions**. Extracts relevant POI info from the provided text content.
    - Parameters: `text_content` the text to extract POIs from (e.g. complete travel itineraries, trip plans, attraction recommendation descriptions; for example: "The Duku Highway and Tarim Lake in Xinjiang are stunning, and the drive from Dushanzi Grand Canyon to Tianshan Mysterious Grand Canyon is also a great experience")
    - Output: relevant POI info including `name`, `location`, etc.

## Getting Started

You can use the Baidu Maps MCP Server in two ways: with `Python` or with `TypeScript`. Both are described below.

### Get an AK

Before choosing either approach, create a server-side AK in the [Baidu Maps Open Platform console](https://lbsyun.baidu.com/apiconsole/key); the AK lets you call Baidu Maps API capabilities.

### Python integration

If you want to customize the Baidu Maps MCP Server, you can integrate from the [source code](https://github.com/baidu-maps/mcp/blob/HEAD/src/baidu-map/python/src/mcp_server_baidu_maps/map.py). See the [Python integration guide](https://github.com/baidu-maps/mcp/blob/HEAD/src/baidu-map/python/README.md) for details.

In the v1.1 release, we published the Baidu Maps MCP Server to PyPI as *mcp-server-baidu-maps*, so you can install it easily with any Python package manager and get started quickly.

#### Installation

##### Using uv (recommended)
With [`uv`](https://docs.astral.sh/uv/) no special installation is needed; we run *mcp-server-baidu-maps* directly via [`uvx`](https://docs.astral.sh/uv/guides/tools/).

##### Using pip
Alternatively, install *mcp-server-baidu-maps* with pip:
```bash
pip install mcp-server-baidu-maps
```

After installation, you can run it as a script:
```bash
python -m mcp_server_baidu_maps
```

#### Configuration
Add the following configuration to any MCP client (e.g. Claude Desktop); some clients may require minor formatting adjustments.

Replace the value of *BAIDU_MAPS_API_KEY* with your own AK.

Using uvx

```json
{
  "mcpServers": {
    "baidu-maps": {
      "command": "uvx",
      "args": ["mcp-server-baidu-maps"],
      "env": {
        "BAIDU_MAPS_API_KEY": ""
      }
    }
  }
}
```

Using pip installation

```json
{
  "mcpServers": {
    "baidu-maps": {
      "command": "python",
      "args": ["-m", "mcp_server_baidu_maps"],
      "env": {
          "BAIDU_MAPS_API_KEY": ""
      }
    }
  }
}
```

After saving the configuration, restart your MCP client and the Baidu Maps MCP Server is ready to use.

### TypeScript integration

#### Install Node.js
For TypeScript integration, you only need to install [node.js](https://nodejs.org/en/download).

Once you can run

```bash
node -v
```

your `node.js` installation is confirmed.

#### Configuration
Open `Claude for Desktop` -> `Settings`, switch to `Developer`, click `Edit Config`, and open the config file with any IDE.

Add the following configuration to the config file. BAIDU_MAP_API_KEY is the AK for accessing the Baidu Maps Open Platform API; apply for one on [this page](https://lbs.baidu.com/faq/search?id=299&title=677):

```json
{
    "mcpServers": {
        "baidu-map": {
            "command": "npx",
            "args": [
                "-y",
                "@baidumap/mcp-server-baidu-map"
            ],
            "env": {
                "BAIDU_MAP_API_KEY": "xxx"
            }
        }
    }
}
```
On Windows, add a separate configuration in the JSON:
```json
"mcpServers": {
 "baidu-map": {
      "command": "cmd",
      "args": [
        "/c",
        "npx",
        "-y",
        "@baidumap/mcp-server-baidu-map"
      ],
      "env": {
        "BAIDU_MAP_API_KEY": "xxx"
      },
    }
}
```
Restart Claude; the settings panel will now show that the Baidu Maps MCP Server has loaded successfully. In the main chat window you should see 8 available MCP tools; click them to view details.

#### Try it out

Now you can ask questions and test the travel-planning assistant.

### Integration via the Qianfan AppBuilder platform

The Qianfan platform supports both SDK and API integration. Build an app with AppBuilder - each app has its own app\_id. Call the corresponding app\_id in your Python file, then call the Baidu Maps Python MCP Tool.

Template code is below: use the SDK Agent with the Maps MCP Server to get navigation routes and route info, then make travel suggestions.

#### Agent configuration

Go to the [Qianfan platform](https://console.bce.baidu.com/ai_apaas/personalSpace/app), create a new app, and publish it.

Set the Agent's thinking rounds to 6. Publish the app.

#### Calling it

You can use this code as a template: call the already-built and published app on the Qianfan platform via the SDK, download the MCP Server locally, and write the file's relative path into the code.

***(Note: use your actual app_id, token, query, and mcp file)***

```python
import os
import asyncio
import appbuilder
from appbuilder.core.console.appbuilder_client.async_event_handler import (
    AsyncAppBuilderEventHandler,
)
from appbuilder.mcp_server.client import MCPClient
class MyEventHandler(AsyncAppBuilderEventHandler):
    def __init__(self, mcp_client):
        super().__init__()
        self.mcp_client = mcp_client
    def get_current_weather(self, location=None, unit="Celsius"):
        return "{} has a temperature of {} {}".format(location, 20, unit)
    async def interrupt(self, run_context, run_response):
        thought = run_context.current_thought
        # Print in green
        print("\033[1;31m", "-> Agent intermediate thought: ", thought, "\033[0m")
        tool_output = []
        for tool_call in run_context.current_tool_calls:
            tool_res = ""
            if tool_call.function.name == "get_current_weather":
                tool_res = self.get_current_weather(**tool_call.function.arguments)
            else:
                print(
                    "\033[1;32m",
                    "MCP tool name: {}, MCP params:{}\n".format(tool_call.function.name, tool_call.function.arguments),
                    "\033[0m",
                )
                mcp_server_result = await self.mcp_client.call_tool(
                    tool_call.function.name, tool_call.function.arguments
                )
                print("\033[1;33m", "MCP result: {}\n\033[0m".format(mcp_server_result))
                for i, content in enumerate(mcp_server_result.content):
                    if content.type == "text":
                        tool_res += mcp_server_result.content[i].text
            tool_output.append(
                {
                    "tool_call_id": tool_call.id,
                    "output": tool_res,
                }
            )
        return tool_output
    async def success(self, run_context, run_response):
        print("\n\033[1;34m", "-> Agent non-streaming answer: ", run_response.answer, "\033[0m")
async def agent_run(client, mcp_client, query):
    tools = mcp_client.tools
    conversation_id = await client.create_conversation()
    with await client.run_with_handler(
        conversation_id=conversation_id,
        query=query,
        tools=tools,
        event_handler=MyEventHandler(mcp_client),
    ) as run:
        await run.until_done()
### User token
os.environ["APPBUILDER_TOKEN"] = (
    ""
)
async def main():
    appbuilder.logger.setLoglevel("DEBUG")
    ### Published app ID
    app_id = ""
    appbuilder_client = appbuilder.AsyncAppBuilderClient(app_id)
    mcp_client = MCPClient()
    
    ### Note: the path here is the relative path of the MCP Server file on your machine
    await mcp_client.connect_to_server(".//map.py")
    print(mcp_client.tools)
    await agent_run(
        appbuilder_client,
        mcp_client,
        'Drive from Beijing to Shanghai with navigation',
    )
    await appbuilder_client.http_client.session.close()
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```

#### Try it out

After the Agent's own reasoning, it calls multiple tools (place search, geocoding, route planning, etc.) through the MCP Server to get navigation routes and route info, then makes travel suggestions.

Example user request: **"Please plan a day trip in Beijing to enjoy the cherry blossoms. Try to make the arrangements as comfortable as possible, and also take the weather into account."**

#### Reasoning process

#### Agent result

## Notes

Parameter specifications for the Baidu Maps MCP Server:

Administrative division codes use the [Baidu adcode mapping table](https://lbsyun.baidu.com/faq/api?title=webapi/download).

Latitude/longitude coordinates use the National Geomatics Bureau coordinate system `bd09ll`; see the [Baidu coordinate system](https://lbsyun.baidu.com/index.php?title=coordinate).

Type and other Chinese string parameters should conform to the [Baidu POI type](https://lbs.baidu.com/index.php?title=open/poitags) standard.

## License

[MIT](https://github.com/baidu-maps/mcp/blob/HEAD/LICENSE) &copy; baidu-maps

## Authorization

Some advanced capabilities in the Baidu Maps MCP Server require **advanced permissions** to use. If needed, please [contact us](https://lbsyun.baidu.com/apiconsole/fankui?typeOne=%E4%BA%A7%E5%93%81%E9%9C%80%E6%B1%82&typeTwo=%E9%AB%98%E7%BA%A7%E6%9C%8D%E5%8A%A1).

## Feedback

If you run into any issues while using the Baidu Maps MCP Server, please report them via `issue` or the [Baidu Maps Open Platform](https://lbsyun.baidu.com/apiconsole/fankui?typeOne=30046&typeTwo=53524&typeThree=1032776). We also welcome every active `PR`. Thank you all for your support and contributions. &lt;3

## Updates

The team is currently focused on Remote service delivery, so open-source updates will be relatively infrequent. Thank you for your understanding.

| Version | Description | Date |
| ---- | ------------------------------ | ------------- |
| V1.0 | Baidu Maps MCP Server officially launched | 2025-03-21 |
| V1.1 | Added quick integration via `uvx` and `pip` | 2025-03-28 |
| V1.2 | Added `Qianfan AppBuilder` integration | 2025-04-05 |
| V2.0 | Supports MCP `1.9.0` protocol | 2025-05-16 |

**Official site: ** [https://github.com/baidu-maps/mcp](https://github.com/baidu-maps/mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `location services`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `mcp-server-baidu-maps`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/lumia19980510-baidu-maps.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
