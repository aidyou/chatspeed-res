---
title: "video-downloader-mcp"
description: "Social media video and audio downloads: Users provide the video URL, and the current service parses it to obtain download links for videos and audios of different qualities. Users only need to use the…"
---

# video-downloader-mcp

Social media video and audio downloads: Users provide the video URL, and the current service parses it to obtain download links for videos and audios of different qualities. Users only need to use the…

# MCP Video Download URL Parser

An MCP server (stdio transport) that provides video download URL parsing capabilities. This service allows you to extract download URLs for both video and audio streams from various video platforms. It can be integrated with LLM apps like Claude Desktop, Cursor or any other MCP compatible client.


## Features

- Exposes `parse_video_url` tool
- Extracts direct download URLs for:
  - Video streams
  - Audio streams
  - Combined formats
- Supports multiple video platforms
- Returns detailed metadata including:
  - Available quality options
  - Format information
  - File sizes
  - Video duration

## Installation and Execution

### Installing via Smithery

To install MCP Video Download URL Parser for Claude Desktop automatically via Smithery:

```bash
npx -y @smithery/cli install @tansunyj/mcp_video_download_url_parser --client claude
```

### Installing Manually
1. Clone the repo: `git clone https://github.com/tansunyj/mcp_video_download_url_parser.git`
2. Change directory: `cd mcp_video_download_url_parser`
3. Start the server: `python main.py`

## Configuring Claude Desktop

1. Add the following configuration:

```json
{
    "mcpServers": {
        "video-url-parser": {
            "command": "ux",
            "args": [
                "run"
                "/path/to/mcp_video_download_url_parser/main.py"
            ]
        }
    }
}
```

## Example Usage

Once configured, you can use prompts like:

- "Get download links for this video: [video_url]"
- "What quality options are available for: [video_url]"
- "Extract audio download URL from: [video_url]"

## Development

To contribute to development:

```bash
git clone https://github.com/tansunyj/mcp_video_download_url_parser.git
cd mcp_video_download_url_parser
python -m pytest tests/
```

## Security

This MCP server runs locally on your machine. While it doesn't execute arbitrary code, please be careful when parsing URLs from untrusted sources.

## License

MIT License

---

[![GitHub repo](/mcp-assets/03c4dfa55a996f04097bbc75cff96c91.svg)](https://github.com/tansunyj/mcp_video_download_url_parser)

**Official site: ** [https://github.com/tansunyj/mcp_video_download_url_parser.git](https://github.com/tansunyj/mcp_video_download_url_parser.git)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `entertainment and media`, `youtube`, `tiktok`, `videodownload`

## MCP Configuration

- Transport: `stdio`
- Command: `uv`
- Args: `--directory /path/to/mcp_video_download_url_parser run main.py`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/tansunyj-video-downloader.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
