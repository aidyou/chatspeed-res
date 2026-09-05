---
title: "grobal_mcp_stock_server"
description: "Provides real-time access to global stock market data including current prices, historical charts, and company financial information through a Model Context Protocol (MCP) server for AI assistants."
---

# grobal_mcp_stock_server

Provides real-time access to global stock market data including current prices, historical charts, and company financial information through a Model Context Protocol (MCP) server for AI assistants.

# Global MCP Stock Server

A Model Context Protocol (MCP) server for global stock market data and analysis

## Overview

This project provides an MCP server for accessing stock market data. It allows AI assistants to access stock prices, chart data, and company information in real time.

## What is MCP (Model Context Protocol)?

The Model Context Protocol (MCP) is a standardized method that allows applications to provide context to large language models (LLMs). See the [Model Context Protocol website](https://modelcontextprotocol.github.io/) for details.

## Features

- Fetch real-time stock price information
- Historical stock price data and charts
- Support for major stock market indicators
- Company information and financial data
- Implemented in TypeScript with strict type checking

# User Guide

## Prerequisites

- Node.js 18 or higher
- npm or yarn

## Installation

1. Clone the repository:

```bash
   git clone https://github.com/sakura-ku/grobal_mcp_stock_server.git
   cd grobal_mcp_stock_server
```

2. Install dependencies:

```bash
   npm install
```

3. Build and run the server:

```bash
   npm run build
   npm start
```

## Usage

### 1. Setting environment variables

First, set the required environment variables. Create a `.env` file or copy the existing `.env.example` file:

```bash
# Windows PowerShell
Copy-Item .env.example .env

# Unix-like systems
cp .env.example .env
```

Edit the `.env` file to configure the required API keys:

```
# Basic settings
PORT=3000
HOST=localhost
NODE_ENV=development

# Polygon.io API key (for stock price data)
POLYGON_API_KEY=your_polygon_api_key_here

# Other API keys...
```

### 2. Running the server

To start the server in development mode:

```bash
npm run dev
```

To start the server in production mode:

```bash
npm run build
npm run start:prod
```

### 3. How to use the API

#### Access directly from a browser

Once the server is running, you can access stock price data from your browser at the following URL:

```
http://localhost:3000/api/stock/price?symbol=AAPL
```

#### Example using cURL

You can fetch data from the command line using cURL:

```bash
# Get stock price data
curl "http://localhost:3000/api/stock/price?symbol=AAPL"

# Get stock price history (past 30 days)
curl "http://localhost:3000/api/stock/history?symbol=AAPL&days=30"
```

#### Example of using it programmatically

Example of using it from a Node.js application:

```javascript
// Function to get stock price data
async function getStockPrice(symbol) {
  const response = await fetch(`http://localhost:3000/api/stock/price?symbol=${symbol}`);
  const data = await response.json();
  return data;
}

// Usage example
getStockPrice('AAPL').then(data => {
  console.log(`Current price of ${data.symbol}: ${data.price} ${data.currency}`);
});
```

### 4. Integration with AI assistants

For information on integrating with AI assistants such as Claude and GPT-4, see the "Working with MCP clients" section.

#### Example with Claude

Example Claude prompt:

```
Please look up the stock price.
Tell me the current price of Tesla (TSLA) and its trend over the past week.
```

#### Example AI assistant response

```
Here is the stock price information for Tesla (TSLA):

Current price: $248.42 USD
Change from previous day: +$5.21 (+2.14%)
Volume: 3,421,532 shares

Past week trend:
- 7 days ago: $230.15
- 6 days ago: $232.05
- 5 days ago: $235.87
- 4 days ago: $239.14
- 3 days ago: $242.33
- 2 days ago: $243.21
- 1 day ago: $248.42

The price has shown an upward trend of about 8% over the past week. The price increase has accelerated especially in the last 3 days.
```

## Available Tools

### Get stock price (get_stock_price)

Gets the current price and related information for a specified stock symbol.

**Parameters:**
- `symbol` (string): the stock ticker symbol (e.g. AAPL, MSFT, GOOGL)

**Returns:**
- Stock price information (price, change, currency, etc.)

## Working with MCP Clients

To use this MCP server in a client (Claude, Claude Desktop, or other MCP-supporting applications), create an mcp.json file that defines the MCP server.

### mcp.json definition example

Below is an example mcp.json definition for using this server. Add this configuration to your MCP client to access stock price information:

```json
{
  "servers": [
    {
      "id": "global-stock-server",
      "url": "http://localhost:3000",
      "description": "MCP server for stock market data and analysis",
      "tools": [
        {
          "name": "get_stock_price",
          "description": "Gets the current price and related information for a specified stock symbol",
          "parameters": {
            "type": "object",
            "required": ["symbol"],
            "properties": {
              "symbol": {
                "type": "string",
                "description": "Stock ticker symbol (e.g. AAPL, MSFT, GOOGL)"
              }
            }
          }
        }
      ]
    }
  ]
}
```

### How to configure it in an MCP client

1. Save the mcp.json definition above to any location
2. Open the settings screen of your MCP client (e.g. Claude Desktop)
3. In the MCP settings section, select the "Add Server" or "Import" option
4. Select the saved mcp.json file, or copy and paste its contents
5. Save the settings and restart the client

The stock price tools will now be available in the MCP client's prompts or chat.

### How to configure it in Cursor IDE

In Cursor IDE, you can add MCP server settings to the settings.json file so the AI assistant can use the tools.

#### Setup steps

1. Open Cursor settings:
   - Windows/Linux: `Ctrl+,`
   - macOS: `Cmd+,`

2. Select "Cursor Settings" and edit the settings.json file

3. Add the following configuration to the `mcpServers` section:

##### When running as a local project (recommended)

This project is intended to be developed and run locally. Using the npm scripts is the most reliable way to run it:

```json
{
  "mcpServers": {
    "global-stock-server": {
      "command": "npm",
      "args": ["run", "start"],
      "cwd": "/path/to/grobal_mcp_stock_server",
      "env": {
        "PORT": "3000",
        "HOST": "localhost",
        "NODE_ENV": "production",
        "STOCK_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

When running in development mode:

```json
{
  "mcpServers": {
    "global-stock-server": {
      "command": "npm",
      "args": ["run", "dev"],
      "cwd": "/path/to/grobal_mcp_stock_server",
      "env": {
        "PORT": "3000",
        "HOST": "localhost",
        "NODE_ENV": "development",
        "STOCK_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

##### How to install from GitHub Packages

This MCP server is published as a private npm registry using GitHub Packages. Follow these steps to install it:

1. Create or edit the `.npmrc` file to configure authentication:

```
@sakura-ku:registry=https://npm.pkg.github.com
//npm.pkg.github.com/:_authToken=${NPM_TOKEN}
```

2. Set your GitHub personal access token as the environment variable `NPM_TOKEN`:

```bash
# Windows
$env:NPM_TOKEN="your_github_token"

# macOS/Linux
export NPM_TOKEN="your_github_token"
```

3. Install the package:

```bash
npm install @sakura-ku/grobal-mcp-stock-server
```

4. Example setup in Cursor IDE:

```json
{
  "mcpServers": {
    "global-stock-server": {
      "command": "npx",
      "args": ["@sakura-ku/grobal-mcp-stock-server"],
      "env": {
        "PORT": "3000",
        "HOST": "localhost",
        "STOCK_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

For more details, refer to how to manage a private npm registry.

#### Troubleshooting

- **If the server does not start**:
  - Navigate to the project directory and run the command manually to check the error
  - Confirm that dependencies are installed correctly (run `npm install`)
  - Check whether the TypeScript version matches

- **If the tools are not found**:
  - Confirm that the server started correctly
  - Check the log output for the registered tool names
  - If necessary, start the server in debug mode with `npm run dev`

# Developer Guide

## Project Structure

```
grobal_mcp_stock_server/
├── build/                # Compiled JavaScript files
├── src/
│   ├── __tests__/        # Integration tests and test utilities
│   ├── config/           # Configuration files
│   ├── data/             # Data models and storage
│   ├── errors/           # Custom error classes
│   ├── services/         # Services for external API integration
│   ├── tools/            # MCP tool implementations
│   │   └── __tests__/    # Tool unit tests
│   ├── types/            # TypeScript type definitions
│   └── index.ts          # Main server entry point
├── package.json          # Project settings
├── tsconfig.json         # TypeScript settings
└── README.md             # Project documentation
```

## Setting Up the Development Environment

1. Install development dependencies:
```bash
   npm install
```

2. Start the server in development mode:
```bash
   npm run dev
```

## Development Workflow

- Start the TypeScript compiler in watch mode: `npm run dev`
- Run static analysis: `npm run lint`
- Auto-fix static analysis issues: `npm run lint:fix`
- Run tests: `npm test`

## Available Scripts

Detailed description of the scripts defined in package.json:

### Build scripts
- `build`: compiles the TypeScript code and outputs it to the dist directory
- `build:dev`: builds for development with source maps
- `build:prod`: builds for production without source maps
- `clean`: deletes and cleans the dist directory
- `prebuild`: automatically runs the clean script before building

### Server startup scripts
- `start`: starts the compiled server
- `start:dev`: starts the server with development configuration
- `start:prod`: starts the server with production configuration
- `dev`: development mode that watches source changes, and automatically rebuilds and restarts

### Code quality scripts
- `lint`: static analysis of TypeScript code with ESLint
- `lint:fix`: automatically fixes code issues with ESLint

### Test scripts
- `test`: runs all tests with Jest
- `test:watch`: runs tests in watch mode, re-running on changes
- `test:coverage`: generates a test coverage report
- `test:ci`: runs tests with CI environment configuration
- `test:unit`: runs only unit tests
- `test:integration`: runs only integration tests
- `test:services`: runs only service tests
- `test:debug`: runs tests in debug mode

### Deployment and packaging
- `deploy:staging`: deploys to the staging environment
- `deploy:production`: deploys to the production environment
- `publish:package`: publishes the package to the npm registry
- `prepare:package`: runs the production build before packaging and creates a tarball
- `prepublishOnly`: runs the production build before publishing the package

## License

ISC

## Contributing

If you are interested in contributing to this project, please submit a pull request.

**Official site: ** [https://github.com/sakura-ku/grobal_mcp_stock_server](https://github.com/sakura-ku/grobal_mcp_stock_server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `finance`
- Tags: `finance`, `search`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npm`
- Args: `run dev`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/sakura-ku-grobal-stock.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
