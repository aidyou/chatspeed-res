---
title: "MCP天气"
description: "MCP天气"
---

# MCP天气

MCP天气

# MCP Weather Server

![npm version](/mcp-assets/7b27162ba5415a81400e9b8a76a40418.svg)
![license](/mcp-assets/5816f652aa1f0cc4eedb21a2f733e09e.svg)
![node version](/mcp-assets/6176b88dbd8c31864dcd7185f406cea8.svg)
![issues](/mcp-assets/246bdfaf8869026642f59da7103dfd04.svg)

   alt="MCP Weather Server Logo" width="250"/>

A Model Context Protocol (MCP) server that provides hourly weather forecasts using the AccuWeather API.

---

## Quick Start

You need an AccuWeather API key (free tier available).  
[Sign up here](https://developer.accuweather.com/) and create an app to get your key.

Export your API key as an environment variable:

```bash
export ACCUWEATHER_API_KEY=your_api_key_here
```

Then run the MCP Weather server directly with:

```bash
npx -y @timlukahorstmann/mcp-weather
```

Or, for HTTP/REST access via [supergateway](https://github.com/supercorp-ai/supergateway):

```bash
npx -y supergateway --stdio "npx -y @timlukahorstmann/mcp-weather" 
  --port 4004 
  --baseUrl http://127.0.0.1:4004 
  --ssePath /messages 
  --messagePath /message 
  --cors "*" 
  --env ACCUWEATHER_API_KEY="$ACCUWEATHER_API_KEY"
```

---

## MCP Server Config Example

For integration with Claude Desktop or other MCP-compatible clients, add this to your config (e.g. `claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "weather": {
      "command": "npx",
      "args": ["-y", "@timlukahorstmann/mcp-weather"],
      "env": {
        "ACCUWEATHER_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

---

## Overview

This MCP server allows large language models (like Claude) to access real-time weather data. When integrated with an LLM, it enables the model to:

- Fetch accurate, up-to-date weather forecasts
- Provide hourly weather data for any location
- Access temperature, conditions, and other weather details

## Prerequisites

- Node.js ≥18  
- An AccuWeather API key (set via `.env` or your shell)

## Setup

1. **Clone this repository:**
```bash
   git clone https://github.com/TimLukaHorstmann/mcp-weather.git
   cd mcp-weather
```

2. **Install dependencies:**
```bash
   npm install
```

3. **Get an AccuWeather API key:**
   - Register at [AccuWeather API](https://developer.accuweather.com/)
   - Create a new app and obtain an API key

4. **Create a `.env` file with your API key:**
```
   ACCUWEATHER_API_KEY=your_api_key_here
```

5. **Build the project:**
```bash
   npm run build
```

## Usage with Claude Desktop

1. Configure Claude Desktop to use this MCP server:
   - Open Claude Desktop
   - Go to Settings > Developer > Edit Config
   - Add the following to your `claude_desktop_config.json`:

```json
   {
     "mcpServers": {
       "weather": {
         "command": "npx",
         "args": ["-y", "@timlukahorstmann/mcp-weather"],
         "env": {
           "ACCUWEATHER_API_KEY": "your_api_key_here"
         }
       }
     }
   }
```

2. Restart Claude Desktop

3. In a new conversation, enable the MCP server by clicking the plug icon and selecting "weather"

4. Now you can ask Claude for weather forecasts, such as:
   - "What s the weather forecast for New York City?"
   - "Will it rain in London tomorrow?"
   - "How hot will it be in Tokyo this afternoon?"

## Development

- Install dev dependencies: `npm install`
- Lint your code:           `npm run lint`  
- Build:                    `npm run build`  
- Run tests:                `npm test`
- Start in dev mode:        `npm run dev`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/TimLukaHorstmann/mcp-weather/blob/HEAD/LICENSE) file for details.

**官方网站：** [https://github.com/TimLukaHorstmann/mcp-weather](https://github.com/TimLukaHorstmann/mcp-weather)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`productivity`
- 标签：`weather services`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @timlukahorstmann/mcp-weather`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/timlukahorstmann-weather.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
