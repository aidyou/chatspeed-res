---
title: "tomtom-maps"
description: "TomTom open-source location services MCP The TomTom MCP (Map and Content Platform) is an open-source project designed to provide a series of location-related services. It allows developers to build th…"
---

# tomtom-maps

TomTom open-source location services MCP The TomTom MCP (Map and Content Platform) is an open-source project designed to provide a series of location-related services. It allows developers to build th…

# TomTom MCP Server

**TomTom MCP Server** simplifies geospatial development by providing seamless access to TomTom location services. These services include search, route planning, traffic, and static map data. It enables easy integration of precise geographic data into AI workflows and development environments.

---

## Quick Start

### Prerequisites
- Node.js 22 or higher
- A TomTom API key

**How to get a TomTom API key**:
1. Create a developer account at the [TomTom developer portal](https://developer.tomtom.com/).
2. Go to **API & SDK Keys** in the left menu.
3. Click the red **Create Key** button.
4. Give your key a name, select all available APIs for full access, and click **Create**.

For more details, visit the [TomTom API key management documentation](https://developer.tomtom.com/platform/documentation/dashboard/api-key-management).

### Installation
```bash
# Install into a local project
npm install @tomtom-org/tomtom-mcp@latest

# Or run directly without installing
npx @tomtom-org/tomtom-mcp@latest
```

### Configuration
Set up your TomTom API key using one of the following methods:

```bash
# Option 1: use a .env file (recommended)
echo "TOMTOM_API_KEY=YOUR_API_KEY" > .env

# Option 2: environment variable (Linux/macOS)
export TOMTOM_API_KEY=YOUR_API_KEY
# Windows CMD: set TOMTOM_API_KEY=YOUR_API_KEY
# Windows PowerShell: $env:TOMTOM_API_KEY="YOUR_API_KEY"

# Option 3: pass it as a CLI argument
npx @tomtom-org/tomtom-mcp@latest --key YOUR_API_KEY
```

### Usage
```bash
# Start the MCP server
npx @tomtom-org/tomtom-mcp@latest
# Get help
npx @tomtom-org/tomtom-mcp@latest --help
```

---

## Integration Guides

The TomTom MCP Server can be easily integrated into various AI development environments and tools.

These guides help you integrate the MCP server with your tools and environments:
- [Claude Desktop setup](https://github.com/tomtom-international/tomtom-mcp/blob/HEAD/docs/claude-desktop-setup.md) - instructions for configuring Claude Desktop to use the TomTom MCP server
- [VS Code setup](https://github.com/tomtom-international/tomtom-mcp/blob/HEAD/docs/vscode-setup.md) - set up the development environment in Visual Studio Code
- [Cursor AI integration](https://github.com/tomtom-international/tomtom-mcp/blob/HEAD/docs/cursor-setup.md) - guide for integrating the TomTom MCP server with Cursor AI
- [WindSurf integration](https://github.com/tomtom-international/tomtom-mcp/blob/HEAD/docs/windsurf-setup.md) - instructions for configuring WindSurf to use the TomTom MCP server
- [Smolagents integration](https://github.com/tomtom-international/tomtom-mcp/blob/HEAD/docs/smolagents/smolagents-setup.md) - example showing how to connect the Smolagents AI agent to the TomTom MCP server

---

## Available Tools

| Tool | Description | Documentation |
|------|-------------|---------------|
| `tomtom-geocode` | Converts addresses to coordinates with global coverage | https://developer.tomtom.com/geocoding-api/documentation/geocode |
| `tomtom-reverse-geocode` | Gets an address from GPS coordinates | https://developer.tomtom.com/reverse-geocoding-api/documentation/reverse-geocode |
| `tomtom-fuzzy-search` | Smart search with fault tolerance (typos) | https://developer.tomtom.com/search-api/documentation/search-service/fuzzy-search |
| `tomtom-poi-search` | Finds specific business categories (points of interest) | https://developer.tomtom.com/search-api/documentation/search-service/points-of-interest-search |
| `tomtom-nearby` | Discovers services within a specified radius | https://developer.tomtom.com/search-api/documentation/search-service/nearby-search |
| `tomtom-routing` | Computes optimal routes between locations | https://developer.tomtom.com/routing-api/documentation/tomtom-maps/calculate-route |
| `tomtom-waypoint-routing` | Multi-stop route planning | https://developer.tomtom.com/routing-api/documentation/tomtom-maps/calculate-route |
| `tomtom-reachable-range` | Determines coverage areas by time/distance | https://developer.tomtom.com/routing-api/documentation/tomtom-maps/calculate-reachable-range |
| `tomtom-traffic` | Real-time traffic incident data | https://developer.tomtom.com/traffic-api/documentation/traffic-incidents/traffic-incidents-service |
| `tomtom-static-map` | Generates custom map images | https://developer.tomtom.com/map-display-api/documentation/raster/static-image |

---
## Contributing & Local Development

### Setup
```bash
git clone <repo-url>  # clone the repository (replace with the actual address)
cd tomtom-mcp        # enter the project directory
npm install          # install dependencies
cp .env.example .env # copy the example env file and add your API key to .env
npm run build        # build the TypeScript files
node ./bin/tomtom-mcp.js  # start the MCP server
```

### Testing
```bash
npm run build       # build TypeScript
npm test            # run all tests
npm run test:unit   # run only unit tests
npm run test:comprehensive  # run integration tests
```

### Test requirements
**Important**: all tests require a valid API key in the `.env` file because they make real API calls (not mocked). This will consume your API quota.

### Project structure
```
src/
├── tools/             # MCP tool definitions
├── services/          # TomTom API wrappers
├── schemas/           # validation schemas
├── utils/             # utility functions
└── createServer.ts    # MCP server creation logic
  └── index.ts         # main entry point
```

## Troubleshooting

### API key issues
```bash
# Linux/macOS: check the environment variable
echo $TOMTOM_API_KEY
# Windows CMD: echo %TOMTOM_API_KEY%
# Windows PowerShell: echo $env:TOMTOM_API_KEY
```

### Test failures
```bash
ls -la .env          # verify the .env file exists (Linux/macOS)
# Windows: dir .env
cat .env             # check the API key (Linux/macOS)
# Windows: type .env
```

### Build issues
```bash
npm run build          # rebuild
npm cache clean --force  # clear the cache
```

**Official site: ** [https://github.com/tomtom-international/tomtom-mcp.git](https://github.com/tomtom-international/tomtom-mcp.git)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `location services`, `地图服务`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @tomtom-org/tomtom-mcp@latest`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/nanago-tomtom-maps.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
