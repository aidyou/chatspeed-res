---
title: "Quickchart-MCP-Server"
description: "An MCP server for generating customizable data visualizations using QuickChart.io, supporting multiple chart types and Chart.js configuration."
---

# Quickchart-MCP-Server

An MCP server for generating customizable data visualizations using QuickChart.io, supporting multiple chart types and Chart.js configuration.

# quickchart-server MCP Server

![image](/mcp-assets/a495ea4a6dfe48b593c9635600caa82a.png)

  

>
 ![](/mcp-assets/c1486b4e2d8cfd67ed0257afeefda188.svg 'MCP Server')

A Model Context Protocol server for generating charts using QuickChart.io

This is a TypeScript-based MCP server that provides chart generation capabilities. It allows you to create various types of charts through MCP tools.

## Overview

This server integrates with QuickChart.io's URL-based chart generation service to create chart images using Chart.js configurations. Users can generate various types of charts by providing data and styling parameters, which the server converts into chart URLs or downloadable images.

## Features

### Tools
- `generate_chart` - Generate a chart URL using QuickChart.io
  - Supports multiple chart types: bar, line, pie, doughnut, radar, polarArea, scatter, bubble, radialGauge, speedometer
  - Customizable with labels, datasets, colors, and additional options
  - Returns a URL to the generated chart

- `download_chart` - Download a chart image to a local file
  - Takes chart configuration and output path as parameters
  - Saves the chart image to the specified location
![image](/mcp-assets/86b981a650a9c915c04fdfa0a91bd674.png)

![image](/mcp-assets/8dc7ec4ba11f643eaffb375b92838cc1.png)

## Supported Chart Types
- Bar charts: For comparing values across categories
- Line charts: For showing trends over time
- Pie charts: For displaying proportional data
- Doughnut charts: Similar to pie charts with a hollow center
- Radar charts: For showing multivariate data
- Polar Area charts: For displaying proportional data with fixed-angle segments
- Scatter plots: For showing data point distributions
- Bubble charts: For three-dimensional data visualization
- Radial Gauge: For displaying single values within a range
- Speedometer: For speedometer-style value display

## Usage

### Chart Configuration
The server uses Chart.js configuration format. Here's a basic example:

```javascript
{
  "type": "bar",
  "data": {
    "labels": ["January", "February", "March"],
    "datasets": [{
      "label": "Sales",
      "data": [65, 59, 80],
      "backgroundColor": "rgb(75, 192, 192)"
    }]
  },
  "options": {
    "title": {
      "display": true,
      "text": "Monthly Sales"
    }
  }
}
```

### URL Generation
The server converts your configuration into a QuickChart URL:
```
https://quickchart.io/chart?c={...encoded configuration...}
```

## Development

Install dependencies:
```bash
npm install
```

Build the server:
```bash
npm run build
```

## Installation

### Installing

```bash
 npm install @gongrzhe/quickchart-mcp-server
```

### Installing via Smithery
 
 To install QuickChart Server for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@GongRzhe/Quickchart-MCP-Server):
 
```bash
 npx -y @smithery/cli install @gongrzhe/quickchart-mcp-server --client claude
```

To use with Claude Desktop, add the server config:

On MacOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
On Windows: `%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "quickchart-server": {
      "command": "node",
      "args": ["/path/to/quickchart-server/build/index.js"]
    }
  }
}
```

or

```json
{
  "mcpServers": {
    "quickchart-server": {
      "command": "npx",
      "args": [
        "-y",
        "@gongrzhe/quickchart-mcp-server"
      ]
    }
  }
}
```

## Documentation References
- [QuickChart Documentation](https://quickchart.io/documentation/)
- [Chart Types Reference](https://quickchart.io/documentation/chart-types/)

## 📜 License

This project is licensed under the MIT License.

**Official site: ** [https://github.com/GongRzhe/Quickchart-MCP-Server](https://github.com/GongRzhe/Quickchart-MCP-Server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `developer tools`, `other`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @gongrzhe/quickchart-mcp-server`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/gongrzhe-quickchart.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
