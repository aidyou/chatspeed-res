---
title: "视频下载地址解析"
description: "社交媒体视频、音频下载，用户提供视频地址，当前服务解析后可以得到不同品质视频、音频下载地址，用户只需要使用这些地址来下载即可。当前该MCP支持像youtube、tiktok、instagram、douyin、bilibili、xiaohongshu、X、等等平台的视频下载"
---

# 视频下载地址解析

社交媒体视频、音频下载，用户提供视频地址，当前服务解析后可以得到不同品质视频、音频下载地址，用户只需要使用这些地址来下载即可。当前该MCP支持像youtube、tiktok、instagram、douyin、bilibili、xiaohongshu、X、等等平台的视频下载

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

**官方网站：** [https://github.com/tansunyj/mcp_video_download_url_parser.git](https://github.com/tansunyj/mcp_video_download_url_parser.git)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`entertainment and media`, `youtube`, `tiktok`, `videodownload`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`--directory /path/to/mcp_video_download_url_parser run main.py`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/tansunyj-video-downloader.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
