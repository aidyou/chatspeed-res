---
title: "earthdata-mcp-server"
description: "A Model Context Protocol server that enables efficient discovery and retrieval of NASA Earth Data for geospatial analysis."
---

# earthdata-mcp-server

A Model Context Protocol server that enables efficient discovery and retrieval of NASA Earth Data for geospatial analysis.

[![Datalayer](/mcp-assets/ebffabe66603ffc5befd3fb0a80b406d.svg)](https://datalayer.io)

[![Become a Sponsor](/mcp-assets/ac64e82bf123c4e77c9539d7abadcb39.svg)](https://github.com/sponsors/datalayer)

# 🪐 ✨ Earthdata MCP Server

[Actions](https://github.com/datalayer/earthdata-mcp-server/actions/workflows/build.yml)
[![PyPI - Version](/mcp-assets/072238d536766621834bd11be56da91f.svg)](https://pypi.org/project/earthdata-mcp-server)

Earthdata MCP Server is a [Model Context Protocol](https://modelcontextprotocol.io/introduction) (MCP) server implementation that provides tools to interact with [NASA Earth Data](https://www.earthdata.nasa.gov/). It enables efficient dataset discovery and retrieval for Geospatial analysis.

The following demo uses this MCP server to search for datasets and data granules on NASA Earthdata, the [jupyter-earth-mcp-server](https://github.com/datalayer/jupyter-earth-mcp-server) to download the data in Jupyter and the [jupyter-mcp-server](https://github.com/datalayer/jupyter-mcp-server) to run further analysis.

  

    
Analyzing Sea Level Rise with AI-Powered Geospatial Tools and Jupyter - Watch Video

  

  

    

  

## Use with Claude Desktop

To use this with Claude Desktop, add the following to your `claude_desktop_config.json`.

```json
{
  "mcpServers": {
    "earthdata": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "datalayer/earthdata-mcp-server:latest"
      ]
    }
  }
}
```

If you are using Linux, start Claude with the following command.

```bash
make claude-linux
```

## Tools

The server offers 2 tools.

### `search_earth_datasets`

- Search for datasets on NASA Earthdata.
- Input:
  - search_keywords (str): Keywords to search for in the dataset titles.
  - count (int): Number of datasets to return.
  - temporal (tuple): (Optional) Temporal range in the format (date_from, date_to).
  - bounding_box (tuple): (Optional) Bounding box in the format (lower_left_lon, lower_left_lat, upper_right_lon, upper_right_lat).
- Returns: List of dataset abstracts.

### `search_earth_datagranules`

- Search for data granules on NASA Earthdata.
- Input:
  - short_name (str): Short name of the dataset.
  - count (int): Number of data granules to return.
  - temporal (tuple): (Optional) Temporal range in the format (date_from, date_to).
  - bounding_box (tuple): (Optional) Bounding box in the format (lower_left_lon, lower_left_lat, upper_right_lon, upper_right_lat).
- Returns: List of data granules.

## Prompts

1. `sealevel_rise_dataset`
   - Search for datasets related to sea level rise worldwide.
   - Input:
     - `start_year` (int): Start year to consider.
      - `end_year` (int): End year to consider.
   - Returns: Prompt correctly formatted.

2. `ask_datasets_format`
    - To ask about the format of the datasets.
    - Returns: Prompt correctly formatted.

## Building

```bash
# or run `docker build -t datalayer/earthdata-mcp-server .`
make build-docker
```

If you prefer, you can pull the prebuilt images.

```bash
make pull-docker
```

**Official site: ** [https://github.com/datalayer/earthdata-mcp-server](https://github.com/datalayer/earthdata-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `research and data`, `location services`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `docker`
- Args: `run -i --rm datalayer/earthdata-mcp-server:latest`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/datalayer-earthdata.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
