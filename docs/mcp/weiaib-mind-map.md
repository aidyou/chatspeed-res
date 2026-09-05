---
title: "mind-map-mcp"
description: "一个用于生成思维导图的 MCP (Model Context Protocol) 服务器。"
---

# mind-map-mcp

一个用于生成思维导图的 MCP (Model Context Protocol) 服务器。

# mind-map-mcp

A MCP (Model Context Protocol) server for generating mind maps.

## Features

- 🧠 Automatically generate mind maps based on text content
- 🔗 Return accessible mind map image links
- 🚀 Supports MCP clients such as CodeBuddy, Cursor, Qoder
- 🌐 Powerful mind map generation capabilities based on the Coze API

## Innovations

First use of Coze as the core workflow for MCP:

- No need to worry about errors. Errors can be directly traced to their cause through Coze.
- Logic processing. You can modify the Coze workflow arbitrarily, and simply update and publish without needing to re-modify the MCP.
- Already maintained

## Installation

### Install via NPM

bash
npm install -g @lucianaib/mind-map-mcp

### Use directly with npx

bash
npx @lucianaib/mind-map-mcp

## Configuration

### Configure in CodeBuddy, Qoder

1. Open CodeBuddy settings
2. Find the MCP server configuration
3. Add a new server:

json
{
  "mcpServers": {
    "mind-map": {
      "command": "npx",
      "args": ["@lucianaib/mind-map-mcp"]
    }
  }
}



### Configure in Cursor

1. Open Cursor settings (Ctrl/Cmd + ,)
2. Search for "MCP"
3. Add in the MCP server configuration:

json
{
  "mind-map": {
    "command": "npx",
    "args": ["@lucianaib/mind-map-mcp"]
  }
}

## Usage

After configuration, you can use the following features in MCP-supported tools:

### Generate Mind Map

Use MCP to help me generate a mind map about "distributed system architecture"

Or call the tool directly:

Use the generate_mindmap tool, content: "basic concepts and applications of machine learning"

## Available Tools

### generate_mindmap

Generates a mind map based on the input content.

**Parameters:**

- `content` (string, required): Description of the content to be converted into a mind map

**Returns:**

- Link to the mind map image
- Generation status information

## Development

### Local Development

1. Clone the repository:

bash
git clone git@github.com:OnePieceLwc/mind-map-mcp.git
cd mind-map-mcp

2. Install dependencies:

bash
npm install

3. Build the project:

bash
npm run build

4. Start the development mode:

bash
npm run dev

### Project Structure

Mind-map-mcp/
├── src/
│   └── index.ts          # Main MCP server code
├── dist/                 # Compiled JavaScript files
├── package.json          # Project configuration
├── tsconfig.json         # TypeScript configuration
└── README.md            # Project documentation

## API Documentation

This tool uses the Coze API to generate mind maps. API details:

- **Endpoint**: `https://api.coze.cn/v1/workflow/run`
- **Method**: POST
- **Authentication**: Bearer Token
- **Return**: Link to the mind map image

## Troubleshooting

### Common Issues

1. **"Unknown Tool" Error**
   - Ensure the MCP server is correctly configured
   - Check if the tool name is correct (`generate_mindmap`)

2. **API Request Failure**
   - Check network connection
   - Confirm the API service status

3. **Chinese Encoding Issue**
   - This tool has already handled Chinese encoding and supports Chinese content input

### Debug Mode

Debugging information will be output to stderr when starting. You can diagnose issues by checking the logs.

## License

MIT License

## Contributions

Feel free to submit Issues and Pull Requests!

**Official site: ** [https://github.com/OnePieceLwc/mind-map-mcp](https://github.com/OnePieceLwc/mind-map-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`, `files`, `communication`
- Tags: `developer tools`, `file systems`, `communication`, `思维导图`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `@lucianaib/mind-map-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/weiaib-mind-map.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
