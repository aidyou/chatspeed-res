---
title: "BiliBiliMCP"
description: "BiliBili MCP Processor A Bilibili video content processing tool based on the Model Context Protocol (MCP), capable of loading, analyzing, and exporting Bilibili video subtitles and content. Features -…"
---

# BiliBiliMCP

BiliBili MCP Processor A Bilibili video content processing tool based on the Model Context Protocol (MCP), capable of loading, analyzing, and exporting Bilibili video subtitles and content. Features -…

# BiliBili MCP Processor

A Bilibili video content processing tool based on the Model Context Protocol (MCP), capable of loading, analyzing, and exporting Bilibili video subtitles and content.

## Features

- 🎥 **Video Content Loading**: Use LangChain loader to fetch Bilibili video content and subtitles
- 🔍 **Content Search**: Perform text search within video content with context display
- 📝 **Smart Summarization**: Automatically generate summaries of video content
- 📤 **Multi-Format Export**: Supports exporting to TXT, JSON, SRT subtitle formats
- 🔐 **Authentication Support**: Supports Bilibili login authentication for full content access
- 🌐 **MCP Protocol**: Fully compatible with MCP protocol, integrable with clients like Claude Desktop

## Installation Dependencies

### Using uv (Recommended)

bash
uv add "mcp[cli]"
uv add langchain langchain-community bilibili-api-python

### Using pip

bash
pip install -r requirements.txt

## Environment Configuration

To obtain complete video content, configure Bilibili authentication information (optional):

bash
export BILIBILI_SESSDATA="your_sessdata_value"
export BILIBILI_BUVID3="your_buvid3_value"
export BILIBILI_BILI_JCT="your_bili_jct_value"
export BILIBILI_EXPORT_PATH="./export"  # Optional, default is ./export

These values can be obtained from the browser's cookies after logging into Bilibili.

## Quick Start

### Install to Claude Desktop:

bash
mcp install BiliBiliProcessor.py --name "BiliBili Processor"

## Tool Usage

### 1. load_bilibili_video
Loads Bilibili video content into memory.

Parameters:

- `video_url (str)`: Bilibili video URL
- `use_auth (bool)`: Whether to use authentication information, defaults to True

Returns: A dictionary containing video ID, number of documents, content length, etc.

### 2. get_video_content
Fetches the content of a loaded video.

Parameters:

- `video_id (str)`: Video ID
- `page_index (int, optional)`: Page index, if not specified, returns all pages

Returns: Video content data

### 3. search_in_video
Searches for specified text within the video content.

Parameters:

- `video_id (str)`: Video ID
- `query (str)`: Search query
- `case_sensitive (bool)`: Whether case-sensitive, defaults to False

Returns: Search results, including match positions and context

### 4. extract_video_summary
Extracts a summary of the video content.

Parameters:

- `video_id (str)`: Video ID
- `max_length (int)`: Maximum summary length, defaults to 500 characters

Returns: Video summary and statistics

### 5. export_video_content
Exports video content to a file.

Parameters:

- `video_id (str)`: Video ID
- `target_format (str)`: Target format (txt/json/srt), defaults to txt
- `output_path (str, optional)`: Output path, if not specified, auto-generated

Returns: Export result information

### 6. get_bilibili_auth_status
Checks Bilibili authentication status.

Returns: Authentication status and configuration instructions

**Official site: ** [https://github.com/TaoPeiLing/BiliBiliMCP](https://github.com/TaoPeiLing/BiliBiliMCP)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `entertainment and media`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uv`
- Args: `run --with mcp[cli] --with langchain --with langchain-community --with bilibili-api-python mcp run /path/to/your/BiliBiliProcessor.py`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/taopl1990-bilibilimcp.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
