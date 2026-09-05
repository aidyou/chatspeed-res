---
title: "yt-dlp-mcp"
description: "Connects 'yt-dlp' with LLMs via the Model Context Protocol, allowing users to download YouTube content and integrate it with Dive and other MCP-compatible LLMs."
---

# yt-dlp-mcp

Connects 'yt-dlp' with LLMs via the Model Context Protocol, allowing users to download YouTube content and integrate it with Dive and other MCP-compatible LLMs.

# yt-dlp-mcp

An MCP server implementation that integrates with yt-dlp, providing video and audio content download capabilities (e.g. YouTube, Facebook, Tiktok, etc.) for LLMs.

## Features

* **Subtitles**: Download subtitles in SRT format for LLMs to read
* **Video Download**: Save videos to your Downloads folder with resolution control
* **Audio Download**: Save audios to your Downloads folder
* **Privacy-Focused**: Direct download without tracking
* **MCP Integration**: Works with Dive and other MCP-compatible LLMs

## Installation

### Prerequisites

Install `yt-dlp` based on your operating system:

```bash
# Windows
winget install yt-dlp

# macOS
brew install yt-dlp

# Linux
pip install yt-dlp
```

### With [Dive Desktop](https://github.com/OpenAgentPlatform/Dive)

1. Click "+ Add MCP Server" in Dive Desktop
2. Copy and paste this configuration:

```json
{
  "mcpServers": {
    "yt-dlp": {
      "command": "npx",
      "args": [
        "-y",
        "@kevinwatt/yt-dlp-mcp"
      ]
    }
  }
}
```
3. Click "Save" to install the MCP server

## Tool Documentation

* **list_subtitle_languages**
  * List all available subtitle languages and their formats for a video (including auto-generated captions)
  * Inputs:
    * `url` (string, required): URL of the video

* **download_video_subtitles**
  * Download video subtitles in any available format. Supports both regular and auto-generated subtitles
  * Inputs:
    * `url` (string, required): URL of the video
    * `language` (string, optional): Language code (e.g., 'en', 'zh-Hant', 'ja'). Defaults to 'en'

* **download_video**
  * Download video to user's Downloads folder
  * Inputs:
    * `url` (string, required): URL of the video
    * `resolution` (string, optional): Video resolution ('480p', '720p', '1080p', 'best'). Defaults to '720p'

* **download_audio**
  * Download audio in best available quality (usually m4a/mp3 format) to user's Downloads folder
  * Inputs:
    * `url` (string, required): URL of the video

## Usage Examples

Ask your LLM to:
```
"List available subtitles for this video: https://youtube.com/watch?v=..."
"Download a video from facebook: https://facebook.com/..."
"Download Chinese subtitles from this video: https://youtube.com/watch?v=..."
"Download this video in 1080p: https://youtube.com/watch?v=..."
"Download audio from this YouTube video: https://youtube.com/watch?v=..."
```

## Manual Start

If needed, start the server manually:
```bash
npx @kevinwatt/yt-dlp-mcp
```

## Requirements

* Node.js 20+
* `yt-dlp` in system PATH
* MCP-compatible LLM service

## Documentation

- [API Reference](https://github.com/kevinwatt/yt-dlp-mcp/blob/HEAD/docs/api.md)
- [Configuration](https://github.com/kevinwatt/yt-dlp-mcp/blob/HEAD/docs/configuration.md)
- [Error Handling](https://github.com/kevinwatt/yt-dlp-mcp/blob/HEAD/docs/error-handling.md)
- [Contributing](https://github.com/kevinwatt/yt-dlp-mcp/blob/HEAD/docs/contributing.md)

## License

MIT

## Author

Dewei Yen

**Official site: ** [https://github.com/kevinwatt/yt-dlp-mcp](https://github.com/kevinwatt/yt-dlp-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `browser`, `media`
- Tags: `browser automation`, `entertainment and media`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @kevinwatt/yt-dlp-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/kevinwatt-yt-dlp.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
