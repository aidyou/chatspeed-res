---
title: "mcp-weather"
description: "MCP Weather"
---

# mcp-weather

MCP Weather

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

**Official site: ** [https://github.com/TimLukaHorstmann/mcp-weather](https://github.com/TimLukaHorstmann/mcp-weather)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `productivity`
- Tags: `weather services`, `other`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @timlukahorstmann/mcp-weather`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/timlukahorstmann-weather.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
