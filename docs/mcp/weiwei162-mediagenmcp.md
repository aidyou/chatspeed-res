---
title: "MediaGenMCP"
description: "Integrating Alibaba Cloud's Qwen Platform Tongyi Wanxiang Model to Achieve Text-to-Image and Text-to-Video Functionality 1. Introduction This document will guide you through using the Tongyi Wanxiang…"
---

# MediaGenMCP

Integrating Alibaba Cloud's Qwen Platform Tongyi Wanxiang Model to Achieve Text-to-Image and Text-to-Video Functionality 1. Introduction This document will guide you through using the Tongyi Wanxiang…

# Media Generator MCP Server

Integrates the Alibaba Cloud Bailian platform's Tongyi Wanxiang model to implement text-to-image and text-to-video functionality.

## Features

### 1. Generate Image (`generate_image`)

Generates an image from a text description.

**Parameters:**
- `prompt` (required): image text description
- `negative_prompt` (optional): description of content you do not want in the image
- `size` (optional): image size, options:
  - 1024*1024 (default)
  - 720*1280
  - 1280*720
  - 768*1152
  - 1152*768
  - 512*512
  - 1440*1440
- `n` (optional): number of images to generate, 1-4, default 1
- `seed` (optional): random seed for reproducible results
- `prompt_extend` (optional): whether to enable smart prompt rewriting, default true
- `watermark` (optional): whether to add the AI-generated watermark, default false

### 2. Generate Video (`generate_video`)

Generates a video from a text description.

**Parameters:**
- `prompt` (required): video text description
- `negative_prompt` (optional): description of content you do not want in the video
- `size` (optional): video resolution, options:
  - 1920*1080 (default, 1080P landscape)
  - 1080*1920 (1080P portrait)
  - 1440*1440 (1080P square)
  - 1632*1248 (1080P 4:3)
  - 1248*1632 (1080P 3:4)
  - 1280*720 (720P landscape)
  - 720*1280 (720P portrait)
  - 960*960 (720P square)
  - 1088*832 (720P 4:3)
  - 832*1088 (720P 3:4)
  - 832*480 (480P landscape)
  - 480*832 (480P portrait)
  - 624*624 (480P square)
- `model` (optional): video model, options:
  - wan2.2-t2v-plus (default)
  - wanx2.1-t2v-turbo
  - wanx2.1-t2v-plus
- `seed` (optional): random seed for reproducible results
- `prompt_extend` (optional): whether to enable smart prompt rewriting, default true
- `watermark` (optional): whether to add the AI-generated watermark, default false

## Examples

### Generate an image
Generate a picture of a cat:
```json
{
  "prompt": "A cute orange tabby cat basking in the sun on a windowsill",
  "size": "1024*1024"
}
```

### Generate a video
Generate a video of a little cat running under the moonlight:
```json
{
  "prompt": "A little cat running under the moonlight, ink painting style, set in an atmospheric traditional Chinese courtyard",
  "size": "1920*1080",
  "model": "wan2.2-t2v-plus"
}
```

## MCP Service Configuration

### Claude Desktop Configuration
Add the following to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "media-gen": {
      "command": "npx",
      "args": ["-y", "media-gen-mcp"],
      "env": {
        "DASHSCOPE_API_KEY": "your_DashScope_API_key"
      }
    }
  }
}
```

### Cursor Configuration
Add the following to `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "media-gen": {
      "command": "npx",
      "args": ["-y", "media-gen-mcp"],
      "env": {
        "DASHSCOPE_API_KEY": "your_DashScope_API_key"
      }
    }
  }
}
```

### VS Code Configuration
Add the following to `settings.json`:

```json
{
  "mcp": {
    "servers": {
      "media-gen": {
        "command": "npx",
        "args": ["-y", "media-gen-mcp"],
        "env": {
          "DASHSCOPE_API_KEY": "your_DashScope_API_key"
        }
      }
    }
  }
}
```

### HTTP Mode Usage
To use it over HTTP, first run:
```bash
npm run build
npm start stream
```

Then configure the MCP client to connect to `http://localhost:8080`

**Official site: ** [https://github.com/weiwei162/MediaGenMCP.git](https://github.com/weiwei162/MediaGenMCP.git)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `developer tools`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y media-gen-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/weiwei162-mediagenmcp.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
