---
title: "yfinance-mcp"
description: "A simple MCP server for Yahoo Finance using yfinance. This server provides a set of tools to fetch stock data, news, and other financial information."
---

# yfinance-mcp

A simple MCP server for Yahoo Finance using yfinance. This server provides a set of tools to fetch stock data, news, and other financial information.

# Yahoo Finance MCP Server

A simple MCP server for Yahoo Finance using yfinance. This server provides a set of tools to fetch stock data, news, and other financial information.

## Tools

- **get_ticker_info**

  - Retrieve stock data including company info, financials, trading metrics and governance data.
  - Inputs:
    - `symbol` (string): The stock symbol.

- **get_ticker_news**

  - Fetches recent news articles related to a specific stock symbol with title, content, and source details.
  - Inputs:
    - `symbol` (string): The stock symbol.

- **search**

  - Fetches and organizes search results from Yahoo Finance, including stock quotes and news articles.
  - Inputs:
    - `query` (string): The search query (ticker symbol or company name).
    - `search_type` (string): Type of search results to retrieve (options: "all", "quotes", "news").

- **get_top**

  - Get top entities (ETFs, mutual funds, companies, growth companies, or performing companies) in a sector.
  - Inputs:
    - `sector` (string): The sector to get.
    - `top_type` (string): Type of top companies to retrieve (options: "top_etfs", "top_mutual_funds", "top_companies", "top_growth_companies", "top_performing_companies").
    - `top_n` (number, optional): Number of top entities to retrieve (default 10).

## Usage

You can use this MCP server either via uv (Python package installer) or Docker.

### Via uv

1. [Install uv](https://docs.astral.sh/uv/getting-started/installation/)
2. Add the following configuration to your MCP server configuration file:

```json
{
  "mcpServers": {
    "yfmcp": {
      "command": "uvx",
      "args": ["yfmcp"]
    }
  }
}
```

### Via Docker

Add the following configuration to your MCP server configuration file:

```json
{
  "mcpServers": {
    "yfmcp": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "narumi/yfinance-mcp"]
    }
  }
}
```

**Official site: ** [https://github.com/narumiruna/yfinance-mcp](https://github.com/narumiruna/yfinance-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `finance`
- Tags: `finance`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `yfmcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/narumiruna-yfinance.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
