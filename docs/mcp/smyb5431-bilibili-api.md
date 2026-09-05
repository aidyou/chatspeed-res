---
title: "bilibili-api-mcp-server"
description: "MCP (Model Context Protocol) server for Bilibili API, supporting multiple operations. - - A project management tool that can conveniently manage dependencies. Configure this Server in any MCP client…"
---

# bilibili-api-mcp-server

MCP (Model Context Protocol) server for Bilibili API, supporting multiple operations. - - A project management tool that can conveniently manage dependencies. Configure this Server in any MCP client…

# Bilibili API MCP Server

An MCP (Model Context Protocol) server for the Bilibili API, supporting multiple operations.

## Environment Requirements

- [uv](https://docs.astral.sh/uv/) - a project management tool that makes dependency management convenient.

## Usage

### Method 1: Use via PyPI (recommended)

Configure this Server in any MCP client; the system will automatically download and enable it.

```json
{
  "mcpServers": {
    "bilibili": {
      "type": "stdio",
      "isActive": true,
      "command": "uvx",
      "args": [
        "bilibili-api-mcp-server"
      ]
    }
  }
}
```

> **Tip**: You can also use the `mcp-config.json` file in the project root as a configuration reference.

### Method 2: Local development

1. Clone this project

```bash
git clone https://github.com/SMYB5431/bilibili-api-mcp-server.git
cd bilibili-api-mcp-server
```

2. Install dependencies with uv

```bash
uv sync
```

3. Configure this Server in any MCP client

```json
{
  "mcpServers": {
    "bilibili": {
      "command": "uvx",
      "args": [
        "--directory",
        "/your-project-path/bilibili-api-mcp-server",
        "run",
        "bilibili.py"
      ]
    }
  }
}
```

### Getting started

## Supported Operations

The following operations are supported:

### Basic search
1. `search_and_recommend_videos`: intelligent video search and recommendation.
   - Search video content by comprehensive ranking
   - Automatically filter out classroom videos (cheese links)
   - Return the top 15 video results (configurable count)
   - Provide recommendation reasons based on search results
   - Analyze video quality and popularity
   - Generate content summary and recommendation report

2. `search_user`: specifically for searching Bilibili users, sortable by follower count.

3. `get_user_id_by_name`: get a user ID by username, supporting exact search and detailed info.
   - Default mode: returns only the user ID for quick identification
   - Detailed mode: returns full user info and exact-match status
   - Exact matching: prioritizes results that exactly match the username
   - Error handling: provides detailed error messages and exception handling

### User content
4. `get_user_dynamics`: get the latest dynamics of a specified user.
   - Supports fetching directly by username (e.g. "Tech Crawler Shrimp")
   - Configurable number of dynamics (default 10)
   - Returns dynamic content, timestamps, links, etc.

5. `get_user_videos`: get the latest videos posted by a specified user.
   - Supports fetching directly by username
   - Configurable number of videos (default 10)
   - Returns detailed info such as title, BV ID, play count, duration

6. `get_user_collections`: get the collections of a specified user.
   - Supports fetching directly by username
   - Returns collection title, video count, play count, etc.
   - Includes collection links for easy access

7. `get_collection_videos`: get the video list in a specified collection.
   - Supports fetching by collection name or collection ID
   - Configurable number of videos (default 10)
   - Returns detailed video info (title, play count, likes, coins, etc.)
   - Supports fuzzy matching of collection names

8. `search_collection_by_keyword`: search a user's collections for videos containing a keyword.
   - Supports searching all collections for a specific keyword
   - Returns matching collections and their video lists
   - Useful for quickly locating videos on a specific topic

### Other features
9. `get_video_danmaku`: get video danmaku (bullet comments).
   - Supports video link or BV ID input
   - Automatically extracts the BV ID from links
   - Supports multi-part (multi-P) videos
   - Returns detailed video info and danmaku data

## Statement

During development and testing, this project used public content from Bilibili creator [Tech Crawler Shrimp](https://space.bilibili.com/316183842) as example data.

This project is for technical learning and research purposes only. All example data usage follows Bilibili's terms of use. If there are any copyright concerns, please contact the project maintainer.

## License

MIT

**Official site: ** [https://github.com/SMYB5431/bilibili-api-mcp-server](https://github.com/SMYB5431/bilibili-api-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `search`, `entertainment and media`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `bilibili-api-mcp-server`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/smyb5431-bilibili-api.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
