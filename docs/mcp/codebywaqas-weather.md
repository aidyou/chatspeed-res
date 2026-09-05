---
title: "weather-mcp-server"
description: "An MCP server that provides real-time weather information including temperature, humidity, wind speed, and sunrise/sunset times through the OpenWeatherMap API."
---

# weather-mcp-server

An MCP server that provides real-time weather information including temperature, humidity, wind speed, and sunrise/sunset times through the OpenWeatherMap API.

# Weather MCP Server

[Smithery](https://smithery.ai/server/@CodeByWaqas/weather-mcp-server)

A Modern Code Protocol (MCP) server that provides weather information using the OpenWeatherMap API.

## Features

- Real-time weather data retrieval
- Metric units for temperature
- Detailed weather information including:
  - Temperature
  - Humidity
  - Wind Speed
  - Sunrise/Sunset times
  - Weather description

## Prerequisites

- Python 3.12 or higher
- OpenWeatherMap API key

## Installation

### Installing via Smithery

To install Weather MCP Server for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@CodeByWaqas/weather-mcp-server):

```bash
npx -y @smithery/cli install @CodeByWaqas/weather-mcp-server --client claude
```

### Manual Installation
1. Clone the repository
2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venvScriptsactivate
```
3. Install dependencies:
```bash
pip install -e .
```

## Setup Intructions

### Setup with Claude Desktop
```json
# claude_desktop_config.json
# Can find location through:
# Claude -> Settings -> Developer -> Edit Config
{
  "mcpServers": {
      "mcp-weather-project": {
          "command": "uv",
          "args": [
              "--directory",
              "/
/weather-mcp-server/src/resources",
              "run",
              "server.py"
          ],
          "env": {
            "WEATHER_API_KEY": "YOUR_API_KEY"
          }
      }
  }
}
```
## Local/Dev Setup Instructions
### Clone repo
`git clone https://github.com/CodeByWaqas/weather-mcp-server`
### Install dependencies
Install MCP server dependencies:
```bash
cd weather-mcp-server

# Create virtual environment and activate it
uv venv

source .venv/bin/activate # MacOS/Linux
# OR
.venv/Scripts/activate # Windows

# Install dependencies
uv add "mcp[cli]" python-dotenv requests httpx
```

## Configuration

1. Copy `src/resources/env.example` to `src/resources/.env`
2. Add your OpenWeatherMap API key to the `.env` file:
```
WEATHER_API_KEY=your_api_key_here
```

## Usage

Run the Claude Desktop and use LLM to retrieve weather info

## License

This project is licensed under the MIT License - see the LICENSE file for details.

**Official site: ** [https://github.com/CodeByWaqas/weather-mcp-server](https://github.com/CodeByWaqas/weather-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `search`
- Tags: `search`, `other`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uv`
- Args: `--directory /<absolute-path>/weather-mcp-server/src/resources run server.py`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/codebywaqas-weather.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
