---
title: "bilibili-mcp"
description: "A Model Context Protocol (MCP) server for parsing Bilibili videos, supporting video info extraction, download link retrieval, and collection parsing."
---

# bilibili-mcp

A Model Context Protocol (MCP) server for parsing Bilibili videos, supporting video info extraction, download link retrieval, and collection parsing.

# Bilibili MCP Server

A Model Context Protocol (MCP) server for parsing Bilibili videos, supporting video info extraction, download link retrieval, and collection parsing.

## Features

- Parse Bilibili video links (supports b23.tv short links)
- Get detailed video info (title, cover, description, user info, etc.)
- Get video download links (1080P quality)
- Support collection video parsing
- Get the collection video list

## Installation

### Method 1: Use npx (recommended)

No installation needed, run directly:

```json
{
  "mcpServers": {
    "bilibili": {
      "command": "npx",
      "args": ["-y", "mcp-server-bilibili"]
    }
  }
}
```

### Method 2: Global installation

```bash
npm install -g mcp-server-bilibili
```

Then use it in the config file:

```json
{
  "mcpServers": {
    "bilibili": {
      "command": "mcp-server-bilibili"
    }
  }
}
```

### Method 3: Run from source

```bash
# Clone the repository
git clone https://github.com/fysh1010/bilibili-mcp.git
cd bilibili-mcp

# Install dependencies
npm install

# Build
npm run build
```

Then use it in the config file:

```json
{
  "mcpServers": {
    "bilibili": {
      "command": "node",
      "args": ["E:\\path\\to\\bilibili-mcp\\build\\index.js"]
    }
  }
}
```

## Configuring Claude Desktop

### Windows

1. Open the Claude Desktop config file:
```
   %APPDATA%\Claude\claude_desktop_config.json
```

2. Add the following configuration:

```json
{
  "mcpServers": {
    "bilibili": {
      "command": "npx",
      "args": ["-y", "mcp-server-bilibili"]
    }
  }
}
```

3. Restart Claude Desktop

### macOS

1. Open the Claude Desktop config file:
```
   ~/Library/Application Support/Claude/claude_desktop_config.json
```

2. Add the following configuration:

```json
{
  "mcpServers": {
    "bilibili": {
      "command": "npx",
      "args": ["-y", "mcp-server-bilibili"]
    }
  }
}
```

3. Restart Claude Desktop

### Linux

1. Open the Claude Desktop config file:
```
   ~/.config/Claude/claude_desktop_config.json
```

2. Add the following configuration:

```json
{
  "mcpServers": {
    "bilibili": {
      "command": "npx",
      "args": ["-y", "mcp-server-bilibili"]
    }
  }
}
```

3. Restart Claude Desktop

## Available Tools

### 1. parse_bilibili_video

Parses a Bilibili video link and gets complete info.

**Parameters:**
- `url` (required): Bilibili video link, supports b23.tv short links

**Example:**
```
Please parse this Bilibili video: https://b23.tv/XhtfoyZ
```

**Returned data:**
```json
{
  "code": 200,
  "msg": "Parsed successfully",
  "data": {
    "title": "video title",
    "cover": "cover image URL",
    "description": "video description",
    "url": "video download link",
    "user": {
      "name": "uploader name",
      "avatar": "uploader avatar URL"
    },
    "videos": [
      {
        "title": "video title",
        "duration": video duration (seconds),
        "durationFormat": "04:45:58",
        "url": "video download link",
        "index": 1
      }
    ],
    "totalVideos": 2
  }
}
```

### 2. get_bilibili_video_info

Gets detailed info of a Bilibili video.

**Parameters:**
- `url` (required): Bilibili video link

**Example:**
```
Get the detailed info of this video: https://b23.tv/XhtfoyZ
```

### 3. get_bilibili_download_urls

Gets the download link list of a Bilibili video.

**Parameters:**
- `url` (required): Bilibili video link

**Example:**
```
Get the download links of this video: https://b23.tv/XhtfoyZ
```

### 4. get_bilibili_basic_info

Gets the basic info of a Bilibili video.

**Parameters:**
- `url` (required): Bilibili video link

**Example:**
```
Get the basic info of this video: https://b23.tv/XhtfoyZ
```

### 5. get_bilibili_collection

Gets the video list of a Bilibili collection.

**Parameters:**
- `url` (required): Bilibili video link (collection link)

**Example:**
```
Get all videos in this collection: https://b23.tv/XhtfoyZ
```

## Usage Examples

### Example 1: Parse a single video

**User input:**
```
Help me parse this Bilibili video: https://b23.tv/XhtfoyZ
```

**Claude will automatically call:**
- the `parse_bilibili_video` tool

**Result:**
Complete video info, including title, cover, download links, uploader info, etc.

### Example 2: Get download links

**User input:**
```
Get the download links of this video: https://b23.tv/XhtfoyZ
```

**Claude will automatically call:**
- the `get_bilibili_download_urls` tool

**Result:**
The video download link list, including all videos in the collection.

### Example 3: View a collection

**User input:**
```
What videos are in this collection? https://b23.tv/XhtfoyZ
```

**Claude will automatically call:**
- the `get_bilibili_collection` tool

**Result:**
The list of all videos in the collection, including each video's title and duration.

## Testing

Use MCP Inspector to test the tools:

```bash
npm run inspector
```

This starts an interactive test interface where you can test all available tools.

## Development

### Project structure

```
bilibili-mcp/
├── src/
│   ├── BilibiliApi.ts    # Bilibili API wrapper layer
│   └── index.ts          # MCP server main entry
├── build/                # Build output directory
├── package.json          # Project config
├── tsconfig.json         # TypeScript config
└── README.md            # Project readme
```

### Build the project

```bash
npm run build
```

### Watch mode development

```bash
npm run watch
```

## API Notes

This MCP Server uses the third-party API: `https://api.bugpk.com/api/bilibili`

**Supported features:**
- Parsing Bilibili short videos
- 1080P quality
- Collection video support
- b23.tv short link support

## Notes

1. **Video link format**: supports full Bilibili links and b23.tv short links
2. **Quality limit**: currently only 1080P is supported
3. **API limits**: uses a third-party API and may have call frequency limits
4. **Copyright**: please comply with Bilibili's user agreement and copyright rules; use it only for personal learning and research

## Troubleshooting

### Issue: cannot connect to the MCP Server

**Solution:**
1. Check whether the Claude Desktop config file is correct
2. Confirm the network connection is normal
3. Check the Claude Desktop logs for detailed error info

### Issue: video parsing fails

**Solution:**
1. Confirm the video link format is correct
2. Check whether the video is public
3. Confirm the third-party API service is working

### Issue: the npx command is slow

**Solution:**
- Use global installation: `npm install -g mcp-server-bilibili`
- Or run from source

## License

MIT License

## Contributing

Issues and Pull Requests are welcome!

## Contact

- GitHub: https://github.com/fysh1010/bilibili-mcp
- Issues: https://github.com/fysh1010/bilibili-mcp/issues

## Acknowledgments

- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Bilibili](https://www.bilibili.com/)
- [API provider](https://api.bugpk.com/)

**Official site: ** [https://github.com/fysh1010/bilibili-mcp](https://github.com/fysh1010/bilibili-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `entertainment and media`, `视频`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y mcp-server-bilibili`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/fysh1010-bilibili.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
