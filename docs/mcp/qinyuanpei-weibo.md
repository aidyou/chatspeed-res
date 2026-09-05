---
title: "mcp-server-weibo"
description: "A Model Context Protocol server for scraping Weibo user information, feeds, and search functionality. It helps retrieve detailed user profiles, timeline content, and perform user searches on Weibo."
---

# mcp-server-weibo

A Model Context Protocol server for scraping Weibo user information, feeds, and search functionality. It helps retrieve detailed user profiles, timeline content, and perform user searches on Weibo.

# Weibo MCP Server

This is a server based on the [Model Context Protocol](https://modelcontextprotocol.io) for scraping Weibo user information, feeds, and search functionality. This server can help obtain detailed Weibo user info, feed content, and perform user searches.

## Installation

Install from source:

```json
{
    "mcpServers": {
        "weibo": {
            "command": "uvx",
            "args": [
                "--from",
                "git+https://github.com/qinyuanpei/mcp-server-weibo.git",
                "mcp-server-weibo"
            ]
        }
    }
}
```

Install from a package manager:

```json
{
    "mcpServers": {
        "weibo": {
            "command": "uvx",
            "args": ["mcp-server-weibo"],
        }
    }
}
```

## Components

### Tools

- `search_users(keyword, limit)`: searches for Weibo users
- `get_profile(uid)`: gets detailed user info
- `get_feeds(uid, limit)`: gets user feeds

### Resources

None

### Prompts

None

## Requirements

- Python >= 3.10
- httpx >= 0.24.0

## License

MIT License - see the [LICENSE](https://github.com/qinyuanpei/mcp-server-weibo/blob/HEAD/LICENSE) file

## Disclaimer

This project is not affiliated with Weibo and is for learning and research purposes only.

**Official site: ** [https://github.com/qinyuanpei/mcp-server-weibo](https://github.com/qinyuanpei/mcp-server-weibo)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `browser`
- Tags: `browser automation`, `social media`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `--from git+https://github.com/qinyuanpei/mcp-server-weibo.git mcp-server-weibo`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/qinyuanpei-weibo.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
