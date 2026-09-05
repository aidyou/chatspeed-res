---
title: "atlas-tools-mcp-server"
description: "DataV Atlas MCP service is a geospatial data visualization MCP service provided by the Alibaba Cloud DataV team. It offers large-scale model visual analytics capabilities for geospatial data, includin…"
---

# atlas-tools-mcp-server

DataV Atlas MCP service is a geospatial data visualization MCP service provided by the Alibaba Cloud DataV team. It offers large-scale model visual analytics capabilities for geospatial data, includin…

# 🗺️ Atlas GIS MCP Toolset 🚀

> The Atlas GIS MCP Toolset is designed by the DataV team for intelligent processing of geospatial data by large models, including common GIS tools such as geocoding, route planning, spatial data generation and processing, and administrative division parsing.

---

### ⚙️ Prerequisites

**Please ensure you have obtained a valid TOKEN before starting, otherwise you will not be able to call the tools properly.**

**⚠️ MCP requires Node.js v18.x or higher to run properly.**

Tool calls require `TOKEN` for authentication. You can obtain a Token from the [Atlas Tools official website](https://atlas.datav.aliyun.com/maptool) page, and you can also view the latest tool list.

### 🖥️ MCP Server Configuration

The Atlas GIS MCP Toolset supports two connection methods: **stdio mode** (traditional) and **HTTP mode** (newly supported).

#### 📡 stdio Mode (Recommended for Local Development)

> 💡 **Tip:** Follow the JSON configuration below to quickly integrate the Atlas GIS toolset.

```json
{
  "mcpServers": {
    "atlas-gis-tools": {
      "name": "Atlas GIS Toolset",
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "atlas-tools-mcp-server@latest"],
      "env": {
        "TOKEN": ""
      }
    }
  }
}
```

#### 🌐 HTTP Mode (Recommended for Production Environments and Multi-user Scenarios)

**Start HTTP Server:**

```bash
# Using default port 3001
npx -y atlas-tools-mcp-server --http

# Using custom port
npx -y atlas-tools-mcp-server --http --port 8080
```

**MCP Client Configuration:**

```json
{
  "mcpServers": {
    "atlas-gis-tools": {
      "name": "Atlas GIS Toolset",
      "type": "streamableHttp",
      "url": "http://localhost:3001/mcp?token="
    }
  }
}
```

**Authentication Methods:**

1. **URL Query Parameters** (Recommended):

```
   http://localhost:3001/mcp?token=your_token
```

2. **HTTP Request Header**:

```bash
   curl -H "Authorization: Bearer your_token" \
        http://localhost:3001/mcp
```

3. **Custom Header**:
```bash
   curl -H "X-Atlas-Token: your_token" \
        http://localhost:3001/mcp
```

#### 🔄 HTTP Mode vs stdio Mode

| Feature           | stdio Mode             | HTTP Mode                     |
| ----------------- | ---------------------- | ----------------------------- |
| **Multi-user**    | ❌ Single user         | ✅ Multi-user concurrency, authentication isolation |
| **Deployment**    | Each client starts independent process | Single server instance |
| **Resource Usage** | High (multi-process)   | Low (single process)         |
| **Network Access** | Local only             | Supports remote access        |
| **Load Balancing** | Not supported           | Supported                    |
| **Monitoring & Logs** | Distributed          | Centralized                  |
| **Authentication** | Environment variables   | Multiple methods (URL params, headers, etc.) |
| **Use Cases**     | Local development, single user | Production, multi-user, enterprise deployment |

#### 🚀 Command Line Options

```bash
npx -y atlas-tools-mcp-server [OPTIONS]

Options:
  --help, -h              Show help information
  --http                  Enable HTTP mode (default: stdio)
  --stdio                 Enable stdio mode (default)
  --port, -p      HTTP server port (default: 3001)

Environment Variables:
  TOKEN, token, ATLAS_TOKEN    Atlas API token
  PORT                        HTTP server port
```

#### 🔒 Multi-tenant Support

**Multi-tenant Scenario Example:**

```bash
# User A uses their own token
curl -X POST "http://localhost:3001/mcp?token=user_a_token" \
     -H "Content-Type: application/json" \
     -H "Accept: application/json, text/event-stream" \
     -d '{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}'

# User B simultaneously uses their own token (no interference)
curl -X POST "http://localhost:3001/mcp?token=user_b_token" \
     -H "Content-Type: application/json" \
     -H "Accept: application/json, text/event-stream" \
     -d '{"jsonrpc": "2.0", "id": 2, "method": "tools/list"}'
```

**Migration Guide (from stdio to HTTP):**

1. **Backward Compatibility**: Existing stdio configurations remain valid
2. **Gradual Migration**: Can run both stdio and HTTP modes simultaneously
3. **Configuration Update**: Change MCP client configuration from `stdio` to `streamableHttp`
4. **Authentication Adjustment**: Change from environment variables to URL parameters or request headers
5. **Simplified Configuration**: Only need to configure the `token` parameter

### 💡 Use Cases

**Actual Configuration for CherryStudio**

![CherryStudio Configuration](/mcp-assets/6ae8f5bfc7cacb30116fb4f5c95dba50.jpg)

**Effect when used with Baijian qwen-max-latest model**

![CherryStudio Usage](/mcp-assets/f6e887af6621613d76942eadda6ac7fb.png)

### 📝 Usage Tips

You can add the following content to the Agent's system prompt to improve tool usage success rate and generate preview links for geographic data output:

```markdown
## Atlas GIS Tool Usage Guide

### Core Principles

1. **Tool Chaining**: Call tools in sequence according to data processing logic, using the fileUrl returned by previous tools as subsequent input
2. **Result Visualization**: When tools return fileUrl, generate preview link: https://datav.aliyun.com/portal/school/atlas/area_generator?fileUrl=
3. **Concise Description**: Provide concise labels for preview links, such as "Provincial Boundary", "Simplified Map", "Buffer Analysis"

_See tool definition schema for specific tool list and parameters_
```

**💡 Clients Supporting MCP Prompts**

For clients with MCP Prompts capabilities (such as Claude Desktop, CherryStudio, etc.), this toolset provides the `preview-geo` prompt that includes a complete tool usage guide. You can directly call this prompt without manually copying the above content to the system prompt.

### 📚 Appendix: Tool List (Continuously Updated)

**The following are the main tools currently supported, continuously expanding. Stay tuned!**

#### 📍 Data Acquisition

| Tool Name           | Tool Description                                                                                                                                                                                                                  |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 🧭 GeoCoding        | **Geocoding Tool**: Used to convert addresses to geographic coordinates                                                                                                                                                           |
| 🗺️ NearbySearch     | **Nearby POI Search Tool**: Searches for nearby POI information within a specified radius based on a center point coordinate, returning POI data in GeoJSON format including name, address, business hours, ratings, etc.        |
| 🚗 Routing          | **Map Route Planning Tool**: Plans the best route based on start point, end point, and optional waypoints, supporting driving, walking, cycling, and electric vehicle modes. Returns path data in GeoJSON format. **Note**: Waypoint function is only available in driving mode, supporting up to 16 waypoints |
| 🏷️ AdcodeToGeojson  | **Administrative Division Data Acquisition Tool**: Obtains corresponding GeoJSON data based on Chinese administrative division codes (must be six-digit codes, multiple separated by commas). Supports province, city, and district levels. To include all sub-level regions, add `_full` after the code, e.g., `330000_full` to get all sub-divisions of Zhejiang Province |
| 📋 GeoJsonPick      | **GeoJSON Feature Selection Tool**: Extracts specified features from a file URL by index range, supporting selective inclusion of attribute fields, maximum of 1000 records |

#### 🛠️ Data Generation

| Tool Name                       | Tool Description                                                                                                                                         |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 🎯 RandomPointsInPolygon        | **Random Point Generation in Polygon Tool**: Randomly generates point data within a specified polygon, supporting random, uniform, and cluster distributions |
| 📏 RandomPointsAlongLine         | **Random Point Generation Around Line Tool**: Randomly generates point data within a specified distance around line segments                               |
| 🕸️ Fishnet                      | **Rectangular Grid Generation Tool**: Creates rectangular fishnet grids in specified input feature data according to specified side lengths                |
| 🟡 DotDensity                   | **Dot Density Map Generation Tool**: Creates dot density maps by randomly distributing points within polygons to represent quantitative information, with point count proportional to specified field values, commonly used for thematic maps such as population distribution and disease distribution |
| ⚫ InterpolatedPointsAlongLine   | **Interpolated Point Generation on Line Tool**: Generates interpolated points at specified distance intervals along line features, supporting various feature types (non-line features automatically converted), with distance unit in meters |

#### 🧰 Data Processing

| Tool Name            | Tool Description                                                                                                                                                                                                                     |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ✂️ Simplify          | **Geometry Simplification Tool**: Simplifies line or polygon geographic feature data, significantly reducing data size while maintaining basic shape                                                                               |
| 🧩 Dissolve          | **Polygon Dissolve Tool**: Fuses geographic features with adjacent boundaries into unified features, eliminating internal boundaries. Supports grouping-based fusion based on attribute fields, mainly used for administrative region merging and boundary simplification. **Note**: Used to fuse adjacent features within a single data source, limitations: only supports line and polygon features, features must have shared boundaries |
| ➕ AddField          | **Field Addition Tool**: Adds new fields to geographic feature data, supporting JavaScript expression calculation of field values, can be calculated based on existing attributes and geometric features, suitable for data enhancement and attribute calculation scenarios |
| 🔍 FilterFeatures    | **Feature Filtering Tool**: Filters geographic features based on JavaScript boolean expressions, supporting complex conditional filtering based on attribute values and geometric features, suitable for data filtering and conditional queries |
| ➡️ ConvertToLine     | **Point/Polygon to Line Tool**: Converts point or polygon features to line features, supporting grouping by field. |
| ⬛ ConvertToPolygon   | **Line/Point to Polygon Tool**: Converts line or point features to polygon features. |

#### 🔄 Data Conversion

| Tool Name              | Tool Description                                                                                                                                                                                                            |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 🔧 GeoFormatConverter  | **Geographic Data Format Conversion Tool**: Supports conversion of Shapefile, TopoJSON, KML, CSV and other formats to GeoJSON. Automatically identifies file formats, CSV files need to specify longitude and latitude field names, can be used with FileUrlContentReader to preview file content and select appropriate fields |
| 🔗 MergeGeoFile        | **Multi-file Merge Tool**: Merges multiple independent geographic data files into a unified GeoJSON file. Supports Shapefile, GeoJSON, TopoJSON, KML, CSV and other formats. **Note**: Used to merge multiple files, not to fuse features within a single file. Limitation: Only layers of the same geometry type can be merged |

#### 🧰 Auxiliary Tools

| Tool Name                | Tool Description                                                                                                                     |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| 📄 FileUrlContentReader  | **URL Content Reading Tool**: Reads the first N bytes of content from a specified URL file, automatically detects character encoding and parses text, commonly used to preview CSV file headers to identify field names |
| 🖼️ SvgRender            | **Geographic Data Rendering Tool**: Renders a single geographic data file as SVG/PNG, supports various styles, symbols, labels and mainstream map projections, suitable for quick preview and export. |
| 🗺️ CreateMap            | **Map Visualization Generation Tool**: Can comprehensively generate temporary map visualization project previews from multiple geographic data files, supports multi-layers, style configuration and interaction, suitable for project-level map display. |

#### 🔍 Spatial Analysis

| Tool Name        | Tool Description                                                                                                                                     |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| 🔵 Buffer        | **Buffer Analysis Tool**: Creates buffers for geographic feature data, supporting point, line, and polygon features, can specify buffer radius and distance units (meters or kilometers) |
| 🏷️ SymbolPoint   | **Polygon Label Point Tool**: Calculates the best label point location for polygons, generating points located inside the polygon, can be used to place labels, icons or perform spatial analysis, ensuring label content does not exceed polygon boundaries |
| 🪢 InnerLines    | **Shared Boundary Extraction Tool**: Extracts shared boundaries between polygons, creating line layers without attribute data, can be used to obtain boundary lines between administrative divisions and analyze adjacent area connections |
| 🟢 TrackSurface  | **Track Surface Generation Tool**: Generates track surfaces through trajectory points, supports setting radius parameters. |

---

### ❓ Frequently Asked Questions (FAQ)

**Q: What if tool calls fail?**

> Check if the TOKEN is correct and valid, if the network is unimpeded, and troubleshoot based on detailed error information output by the client tool.

**Q: How to get the latest tool list?**

> Visit [Atlas Tools Official Website](https://atlas.datav.aliyun.com/maptool) to view the latest supported tools.

**Q: How to preview result data?**

> Splice the tool-generated fileUrl link with the rule `https://datav.aliyun.com/portal/school/atlas/area_generator/?fileUrl=` to preview.

**Q: How long are the generated files kept?**

> Tool-generated files are temporary files, only kept for one day (24 hours). Please download and save to local storage before the files expire to avoid data loss.

**Q: What's the difference between HTTP mode and stdio mode?**

> HTTP mode supports multi-user concurrent access, with each user using independent authentication information, suitable for production environments; stdio mode is suitable for local development and single-user scenarios. See the comparison table above for details.

**Q: How to handle multi-user authentication in HTTP mode?**

> HTTP mode adopts request-level authentication isolation. Each request can pass independent authentication information through URL parameters, Authorization headers, or custom headers to ensure data security between users.

**Q: What is the health check endpoint for the HTTP server?**

> Visit `http://localhost:3001/health` to check server status, returning health information in JSON format.

**Q: How to migrate from stdio mode to HTTP mode?**

> 1. Start HTTP server: `npx -y atlas-tools-mcp-server --http`
> 2. Update MCP client configuration: Change `type` from `stdio` to `streamableHttp`, set `url` to `http://localhost:3001/mcp?token=`
> 3. Test connection to ensure it works properly, then stop stdio mode

If you have more questions, feel free to contact us through the [Atlas Tools Official Website](https://atlas.datav.aliyun.com/maptool)!

---

### 🗒️ Release Notes

- 2025-07-10:
  - Added **➡️ ConvertToLine** tool, supporting point/polygon to line conversion with grouping.
  - Added **⬛ ConvertToPolygon** tool, supporting line/point to polygon conversion.
  - Added **🟢 TrackSurface** tool, supporting trajectory point to trajectory surface generation with radius parameter setting.
- 2025-07-08:
  - Added **🖼️ SvgRender** tool, supporting SVG/PNG rendering of single geographic data files with various style configurations.
  - Added **🗺️ CreateMap** tool, supporting comprehensive temporary map visualization project previews from multiple geographic data files, suitable for multi-layer project-level map display.
- 2025-07-21:
  - Added **StreamableHTTP** mode support

**Official site: ** [https://www.npmjs.com/package/atlas-tools-mcp-server](https://www.npmjs.com/package/atlas-tools-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`, `search`, `data`
- Tags: `search`, `developer tools`, `location services`, `aigc`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y atlas-tools-mcp-server@latest`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/datav-atlas-atlas-tools.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
