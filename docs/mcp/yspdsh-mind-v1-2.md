---
title: "mind-mcp-v1.2"
description: "An MCP (Model Context Protocol) server for generating mind maps. It automatically generates mind maps from text content and returns accessible mind map image links. It supports MCP clients such as Cod…"
---

# mind-mcp-v1.2

An MCP (Model Context Protocol) server for generating mind maps. It automatically generates mind maps from text content and returns accessible mind map image links. It supports MCP clients such as Cod…

# @jiushan93/mind-map-mcp

An MCP (Model Context Protocol) server for generating mind maps.

## Features

- Automatically generates mind maps from text content
- Returns accessible mind map image links
- Supports MCP clients such as CodeBuddy and Cursor
- Powerful mind map generation built on the Coze API

## Installation

### Install via NPM

```bash
npm install -g @jiushan93/mind-map-mcp
```

### Use directly with npx

```bash
npx @jiushan93/mind-map-mcp
```

## Configuration

### Configuring in CodeBuddy

1. Open CodeBuddy settings
2. Find the MCP server configuration
3. Add a new server:

```json
{
  "mcpServers": {
    "mind-map": {
      "command": "npx",
      "args": ["@jiushan93/mind-map-mcp"]
    }
  }
}
```

### Configuring in Cursor

1. Open Cursor settings (Ctrl/Cmd + ,)
2. Search for "MCP"
3. Add to the MCP server configuration:

```json
{
  "mind-map": {
    "command": "npx",
    "args": ["@jiushan93/mind-map-mcp"]
  }
}
```

## Usage

After configuration, you can use the following features in MCP-capable tools:

### Generate a mind map

```
Please help me generate a mind map about "Distributed System Architecture"
```

Or call the tool directly:

```
Use the generate_mindmap tool with the content: "The basic concepts and applications of machine learning"
```

## Available Tools

### generate_mindmap

Generates a mind map based on the input content.

**Parameters:**
- `content` (string, required): description of the content to convert into a mind map

**Returns:**
- A mind map image link
- Generation status info

**Example:**
```json
{
  "content": "The development history and main technologies of deep learning"
}
```

## Development

### Local development

1. Clone the repository:
```bash
git clone https://github.com/jiushan-test/Mind-map-mcp.git
cd Mind-map-mcp
```

2. Install dependencies:
```bash
npm install
```

3. Build the project:
```bash
npm run build
```

4. Start development mode:
```bash
npm run dev
```

### Project structure

```
Mind-map-mcp/
├── src/
│   └── index.ts          # Main MCP server code
├── dist/                 # Compiled JavaScript files
├── package.json          # Project config
├── tsconfig.json         # TypeScript config
└── README.md            # Project readme
```

## API Description

This tool uses the Coze API to generate mind maps. API details:

- **Endpoint**: `https://api.coze.cn/v1/workflow/run`
- **Method**: POST
- **Authentication**: Bearer Token
- **Returns**: mind map image link

## Troubleshooting

### Common issues

1. **"Unknown tool" error**
   - Make sure the MCP server is configured correctly
   - Check that the tool name is correct (`generate_mindmap`)

2. **API request failure**
   - Check the network connection
   - Confirm the API service status

3. **Chinese encoding issues**
   - This tool already handles Chinese encoding and supports Chinese content input

### Debug mode

Debug info is printed to stderr on startup; you can diagnose issues by checking the logs.

## License

MIT License

## Contributing

Issues and Pull Requests are welcome!

## Changelog

### v1.0.1
- Updated API configuration
- Renamed the package to @jiushan93/mind-map-mcp
- Updated the repository address

### v1.0.0
- Initial release
- Basic mind map generation support
- CodeBuddy and Cursor integration

**Official site: ** [https://github.com/jiushan-test/Mind-map-mcp](https://github.com/jiushan-test/Mind-map-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `memory`
- Tags: `knowledge and memory`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `@jiushan93/mind-map-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/yspdsh-mind-v1-2.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
