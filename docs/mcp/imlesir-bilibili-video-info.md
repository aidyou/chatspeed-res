---
title: "bilibili-video-info-mcp"
description: "This is a server based on the MCP (Model Context Protocol) that can fetch the subtitles, danmaku (bullet comments), and comments of Bilibili videos."
---

# bilibili-video-info-mcp

This is a server based on the MCP (Model Context Protocol) that can fetch the subtitles, danmaku (bullet comments), and comments of Bilibili videos.

# MCP Server for Bilibili Video Info

This is a server based on MCP (Model Context Protocol) that can fetch subtitles, danmaku (bullet comments), and comments information of Bilibili videos.

## MCP Tool List

### 1. Get Video Subtitles List

json
{
  "name": "get_subtitles",
  "arguments": {
    "url": "https://www.bilibili.com/video/BV1x341177NN"
  }
}

### 2. Get Video Danmaku

json
{
  "name": "get_danmaku",
  "arguments": {
    "url": "https://www.bilibili.com/video/BV1x341177NN"
  }
}

### 3. Get Video Comments

json
{
  "name": "get_comments",
  "arguments": {
    "url": "https://www.bilibili.com/video/BV1x341177NN"
  }
}

## Usage

MCP Client Configuration
json
{
    "mcpServers": {
        "bilibili-video-info-mcp": {
            "command": "uvx",
            "args": [
                "bilibili-video-info-mcp"
            ],
            "env": {
                "SESSDATA": "your valid sessdata"
            }
        }
    }
}

## Frequently Asked Questions

### 1. What to do if SESSDATA cannot be found?

1. Log in to the Bilibili website.
2. Open the browser developer tools (F12).
3. Go to Application/Storage -> Cookies.
4. Find the value corresponding to SESSDATA.

### 2. Error: "SESSDATA environment variable is required"

Make sure the environment variable is set:

bash
export SESSDATA="your SESSDATA value"

### 3. Which formats of video links are supported?

Standard Bilibili video links are supported, such as:
- https://www.bilibili.com/video/BV1x341177NN
- https://b23.tv/xxxxx (short link)
- Any link containing the BV number

## License

MIT

**Official site: ** [https://github.com/lesir831/bilibili-video-info-mcp](https://github.com/lesir831/bilibili-video-info-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `entertainment and media`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `bilibili-video-info-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/imlesir-bilibili-video-info.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
