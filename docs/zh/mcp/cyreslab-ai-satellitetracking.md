---
title: "Satellite Tracking MCP服务器"
description: "卫星跟踪MCP服务器"
---

# Satellite Tracking MCP服务器

卫星跟踪MCP服务器

# Satellite Tracking MCP Server

A Model Context Protocol (MCP) server that provides access to satellite tracking data using the N2YO API.

## Features

This MCP server provides the following capabilities:

### Tools

- **get_satellite_position**: Get real-time position of a satellite by NORAD ID
- **get_satellite_tle**: Get TLE (Two-Line Element) data for a satellite by NORAD ID
- **predict_visual_passes**: Predict visible passes of a satellite over a location
- **predict_radio_passes**: Predict radio frequency passes of a satellite over a location
- **get_satellites_above**: Get satellites currently above a specified location
- **search_satellites**: Search for satellites by name or category

### Resources

- **satellite://{norad_id}**: Information about a satellite by NORAD ID
- **satellites://category/{category_id}**: List of satellites in a specific category
- **satellites://above/{lat}/{lon}/{radius}**: List of satellites above a specified location

## Installation

### Prerequisites

- Node.js 18 or higher
- A N2YO API key (available from [N2YO API Services](https://www.n2yo.com/api/))

### Setup

1. Clone this repository or download the source code
2. Install dependencies:

```bash
cd satellite-tracking-server
npm install
```

3. Build the server:

```bash
npm run build
```

## Configuration

The server requires a N2YO API key to function. You can provide this through the environment variable `N2YO_API_KEY`.

### MCP Settings Configuration

To use this server with Claude, add it to your MCP settings configuration file:

#### For Claude Desktop App (macOS)

Edit `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "satellite-tracking": {
      "command": "node",
      "args": ["/path/to/satellite-tracking-server/build/index.js"],
      "env": {
        "N2YO_API_KEY": "your-api-key-here"
      },
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

#### For Claude VSCode Extension

Edit `~/Library/Application Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`:

```json
{
  "mcpServers": {
    "satellite-tracking": {
      "command": "node",
      "args": ["/path/to/satellite-tracking-server/build/index.js"],
      "env": {
        "N2YO_API_KEY": "your-api-key-here"
      },
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

## Usage Examples

Once the server is configured and running, you can use it with Claude to access satellite tracking data:

### Get Satellite Position

```

satellite-tracking
get_satellite_position

{
  "norad_id": 25544,
  "observer_lat": 40.7128,
  "observer_lng": -74.0060
}

```

### Get Satellite TLE Data

```

satellite-tracking
get_satellite_tle

{
  "norad_id": 25544
}

```

### Predict Visual Passes

```

satellite-tracking
predict_visual_passes

{
  "norad_id": 25544,
  "observer_lat": 40.7128,
  "observer_lng": -74.0060,
  "days": 7
}

```

### Search for Satellites

```

satellite-tracking
search_satellites

{
  "query": "ISS"
}

```

### Get Satellites Above Location

```

satellite-tracking
get_satellites_above

{
  "observer_lat": 40.7128,
  "observer_lng": -74.0060,
  "search_radius": 45
}

```

### Access Satellite Resource

```

satellite-tracking
satellite://25544

```

## Satellite Categories

The server supports the following satellite categories:

| Category ID | Description  |
| ----------- | ------------ |
| 0           | All          |
| 1           | Amateur      |
| 2           | CubeSat      |
| 3           | Education    |
| 4           | Engineering  |
| 5           | Galileo      |
| 6           | GLO-OPS      |
| 7           | GPS-OPS      |
| 8           | Military     |
| 9           | Radar        |
| 10          | Resource     |
| 11          | SARSAT       |
| 12          | Science      |
| 13          | TDRSS        |
| 14          | Weather      |
| 15          | XM/Sirius    |
| 16          | Iridium-NEXT |
| 17          | Globalstar   |
| 18          | Intelsat     |
| 19          | SES          |
| 20          | Telesat      |
| 21          | Orbcomm      |
| 22          | Gorizont     |
| 23          | Raduga       |
| 24          | Molniya      |
| 25          | DMC          |
| 26          | Argos        |
| 27          | Planet       |
| 28          | Spire        |
| 29          | Starlink     |
| 30          | OneWeb       |

## API Key Limitations

The N2YO API has usage limits based on your subscription plan. The free tier allows:

- 1,000 requests per hour
- Basic functionality across all endpoints

Be aware of these limits when using the server to avoid exceeding your quota.

## Troubleshooting

- **API Key Errors**: Ensure your N2YO API key is valid and correctly set in the environment variables.
- **Rate Limiting**: If you encounter rate limiting errors, the server will automatically retry with exponential backoff, but you may need to wait before making additional requests.
- **No Data Found**: Some satellites may not have real-time tracking data available, especially older or inactive satellites.

## License

This project is licensed under the ISC License.

**官方网站：** [https://github.com/Cyreslab-AI/satellitetracking-mcp-server](https://github.com/Cyreslab-AI/satellitetracking-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`location services`, `government data`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`/path/to/satellite-tracking-server/build/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/cyreslab-ai-satellitetracking.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
