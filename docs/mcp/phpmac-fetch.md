---
title: "fetch_mcp"
description: "Provides functionality to fetch and transform web content in various formats (HTML, JSON, plain text, and Markdown) through simple API calls."
---

# fetch_mcp

Provides functionality to fetch and transform web content in various formats (HTML, JSON, plain text, and Markdown) through simple API calls.

# Fetch MCP Server


This MCP server provides functionality to fetch web content in various formats, including HTML, JSON, plain text, and Markdown.

### Tools

- **fetch_html**

  - Fetch website content and return as HTML
  - Input parameters:
    - `url` (string, required): URL of the website to fetch
    - `headers` (object, optional): Custom headers to include in the request
  - Returns the raw HTML content of the webpage

- **fetch_json**

  - Fetch JSON file from URL
  - Input parameters:
    - `url` (string, required): URL of the JSON to fetch
    - `headers` (object, optional): Custom headers to include in the request
  - Returns the parsed JSON content

- **fetch_txt**

  - Fetch website content and return as plain text (no HTML)
  - Input parameters:
    - `url` (string, required): URL of the website to fetch
    - `headers` (object, optional): Custom headers to include in the request
  - Returns the text content of the webpage with HTML tags, scripts, and styles removed

- **fetch_markdown**
  - Fetch website content and return as Markdown
  - Input parameters:
    - `url` (string, required): URL of the website to fetch
    - `headers` (object, optional): Custom headers to include in the request
  - Returns the webpage content converted to Markdown format

### 2 Ways to Start

1. bun

```bash
bun i
bun start
```

2. docker

```bash
docker compose up --build -d
```

### Usage

```json
{
  "mcpServers": {
    "fetch-mcp": {
      "transport": "sse",
      "url": "http://localhost:3000/sse",
      "headers": {
        "Authorization": "Bearer your-token-here",
        "X-Custom-Header": "custom-value"
      },
      "useNodeEventSource": true
    }
  }
}
```

### Resources

This server does not provide any persistent resources. It is designed to fetch and transform web content on demand.

### References

- [Original Repository zcaceres/fetch-mcp](https://github.com/zcaceres/fetch-mcp)

**Official site: ** [https://github.com/phpmac/fetch_mcp](https://github.com/phpmac/fetch_mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `browser`
- Tags: `browser automation`, `chinese`

## MCP Configuration

- Transport: `http`
- Command: ``
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/phpmac-fetch.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
