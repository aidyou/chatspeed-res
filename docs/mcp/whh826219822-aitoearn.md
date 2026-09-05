---
title: "aitoearn"
description: "A Model Context Protocol (MCP) server that provides social media publishing and account management capabilities for AI-driven content creation and automation."
---

# aitoearn

A Model Context Protocol (MCP) server that provides social media publishing and account management capabilities for AI-driven content creation and automation.

# AiToEarn MCP

A Model Context Protocol (MCP) server that provides social media publishing and account management capabilities for AI-driven content creation and automation.

## Features

- **Account Management**: retrieve and manage social media accounts
- **Content Publishing**: publish video and article content to social media platforms
- **Batch Operations**: publish content to multiple accounts simultaneously
- **Type Validation**: automatic validation based on content type requirements
- **Error Handling**: comprehensive error handling with detailed feedback

## Requirements

- Node.js >= 18.0.0
- npm or yarn
- AiToEarn API access with a valid API key

## Installation

### Via npm (recommended)

```bash
npm install aitoearn-mcp
```

### Via GitHub

1. Clone the repository:
```bash
git clone https://github.com/aitoearn/aitoearn-mcp-server.git
cd aitoearn-mcp
```

2. Install dependencies:
```bash
npm install
```

3. Build the project:
```bash
npm run build
```

## Usage

### Using as a global CLI tool

After installing globally:
```bash
npm install -g aitoearn-mcp
aitoearn-mcp
```

### Using as a local package

After installing locally:
```bash
npm install aitoearn-mcp
npx aitoearn-mcp
```

### Programmatic usage

```javascript
import { spawn } from 'child_process';

// Start the MCP server as a subprocess
const server = spawn('npx', ['aitoearn-mcp']);

server.stdout.on('data', (data) => {
  console.log(`Server: ${data}`);
});
```

### Running the MCP server

```bash
npm start
```

### Available tools

#### 1. get-skKey
Opens the AiToEarn platform website for account management and platform access.

#### 2. create-publish-list
Batch-publishes content to all accounts associated with your API key.

**Parameters:**
- `skKey` (string): your AiToEarn API key
- `type` (string): content type ("video" or "article")
- `title` (string): content title
- `coverUrl` (string): cover image URL
- `topics` (string): comma-separated topics/hashtags
- `desc` (string, optional): content description
- `videoUrl` (string): video URL (required for video type)
- `imgUrlList` (string): comma-separated image URLs (required for article type)
- `publishTime` (string, optional): scheduled publish time

**Example (video):**
```json
{
  "skKey": "sk-YOUR_API_KEY_HERE",
  "type": "video",
  "title": "My Amazing Video",
  "videoUrl": "https://example.com/video.mp4",
  "coverUrl": "https://example.com/cover.jpg",
  "topics": "lifestyle,entertainment"
}
```

**Example (article):**
```json
{
  "skKey": "sk-YOUR_API_KEY_HERE",
  "type": "article",
  "title": "My Article Title",
  "imgUrlList": "https://example.com/img1.jpg,https://example.com/img2.jpg",
  "coverUrl": "https://example.com/cover.jpg",
  "topics": "technology,innovation"
}
```

#### 3. get-publish-task-list
Gets the list of publish tasks.

**Parameters:**
- `skKey` (string): your AiToEarn API key
- `flowId` (string): the flow ID returned during batch publishing

**Example:**
```json
{
  "skKey": "sk-YOUR_API_KEY_HERE",
  "flowId": "flowId"
}
```

### MCP client configuration

#### Claude Desktop

Add the server configuration to your Claude Desktop config file:

**macOS/Linux:** `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows:** `%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "aitoearn": {
      "command": "npx",
      "args": ["aitoearn-mcp"]
    }
  }
}
```

Or if installed globally:

```json
{
  "mcpServers": {
    "aitoearn": {
      "command": "aitoearn-mcp"
    }
  }
}
```

#### Other MCP clients

For other MCP clients, refer to their documentation on how to configure MCP servers. This server runs over stdio transport.

**Description:**
This tool provides information about the AiToEarn platform (https://aitoearn.ai), including:
- Account management and configuration
- Content creation and scheduling
- Analytics and performance tracking
- API key management
- Social media account integration

## Content Type Requirements

### Video content (`type: "video"`)
- **Required**: `videoUrl` - video file URL
- **Optional**: `imgUrlList` - additional images

### Article content (`type: "article"`)
- **Required**: `imgUrlList` - comma-separated list of image URLs
- **Optional**: `videoUrl` - additional video content

## Error Handling

The server provides comprehensive error handling with detailed error messages:

- **Validation errors**: clear messages about missing required fields
- **API errors**: detailed information about API communication issues
- **Network errors**: helpful guidance for connectivity problems
- **Authentication errors**: clear feedback about API key issues

## Development

### Build
```bash
npm run build
```

### Development mode
```bash
npm run dev
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Related Links

- [ModelScope MCP Documentation](https://modelscope.cn/docs/mcp/create)
- [Model Context Protocol Specification](https://spec.modelcontextprotocol.io/)
- [AiToEarn Platform](https://aitoearn.ai)

**Official site: ** [https://github.com/yikart/aitoearn-mcp-server](https://github.com/yikart/aitoearn-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `communication`, `media`
- Tags: `communication`, `entertainment and media`, `娱乐与多媒体`, `社交媒体发布工具`, `矩阵工具`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `aitoearn-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/whh826219822-aitoearn.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
