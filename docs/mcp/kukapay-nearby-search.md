---
title: "nearby-search-mcp"
description: "An MCP server for nearby place searches with IP-based location detection."
---

# nearby-search-mcp

An MCP server for nearby place searches with IP-based location detection.

# NearbySearch MCP Server

An MCP server for nearby place searches with IP-based location detection.

![GitHub License](/mcp-assets/5816f652aa1f0cc4eedb21a2f733e09e.svg) 
![GitHub Last Commit](/mcp-assets/4e70b12afff6d1394e76925e2c277c74.svg) 
![Python Version](/mcp-assets/405b7b46d001e379991916d79670861b.svg)

## Features

- **IP-based Location Detection**: Uses ipapi.co to determine your current location
- **Google Places Integration**: Searches for nearby places based on keywords and optional type filters
- **Simple Interface**: Single tool endpoint with customizable radius

## Requirements

- Python 3.10+
- Google Cloud Platform API Key with Places API enabled
- Internet connection

## Installation

1. Clone the repository:
```bash
git clone https://github.com/kukapay/nearby-search-mcp.git
cd nearby-search-mcp
```

2. Install dependencies:
```bash
# Using uv (recommended)
uv add "mcp[cli]" httpx python-dotenv

# Or using pip
pip install mcp httpx python-dotenv
```

3. Client Configuration

```json
{
  "mcpServers": {
    "nearby-search": {
      "command": "uv",
      "args": ["--directory", "path/to/nearby-search-mcp", "run", "main.py"],
      "env": {
        "GOOGLE_API_KEY": "your google api key"
      }
    }
  }
}
```

## Usage

### Running the Server

- **Development Mode** (with MCP Inspector):
```bash
mcp dev main.py
```

- **Install in Claude Desktop**:
```bash
mcp install main.py --name "NearbySearch"
```

- **Direct Execution**:
```bash
python main.py
```

### Available Endpoints

**Tool: `search_nearby`**
 - Searches for places near your current location
 - Parameters:
   - `keyword` (str): What to search for (e.g., "coffee shop")
   - `radius` (int, optional): Search radius in meters (default: 1500)
   - `type` (str, optional): Place type (e.g., "restaurant", "cafe")

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/kukapay/nearby-search-mcp/blob/HEAD/LICENSE) file for details.

**Official site: ** [https://github.com/kukapay/nearby-search-mcp](https://github.com/kukapay/nearby-search-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `location services`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uv`
- Args: `--directory path/to/nearby-search-mcp run main.py`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/kukapay-nearby-search.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
