---
title: "mcp-server-weibo"
description: "A Model Context Protocol server for scraping Weibo that provides tools to search users, retrieve detailed user profiles, and fetch user feeds."
---

# mcp-server-weibo

A Model Context Protocol server for scraping Weibo that provides tools to search users, retrieve detailed user profiles, and fetch user feeds.

# Weibo MCP Server (TypeScript Version)

This is a server based on the [Model Context Protocol](https://modelcontextprotocol.io) for scraping Weibo user information, feeds, and search functionality. This server can help retrieve detailed information about Weibo users, feed content, and perform user searches.

  

## Installation

Install from source code:

```json
{
    "mcpServers": {
        "weibo": {
            "command": "npx",
            "args": [
                "--from",
                "git+https://github.com/Selenium39/mcp-server-weibo.git",
                "mcp-server-weibo"
            ]
        }
    }
}
```

Install from package manager:

```json
{
    "mcpServers": {
        "weibo": {
            "command": "npx",
            "args": ["mcp-server-weibo"],
        }
    }
}
```

## Components

### Tools

- `search_users(keyword, limit)`: searches Weibo users by keyword
- `get_profile(uid)`: gets detailed user profile info
- `get_feeds(uid, limit)`: gets user Weibo feeds
- `get_hot_search(limit)`: gets the Weibo hot search list
- `search_content(keyword, limit, page?)`: searches Weibo content by keyword

### Resources

None

### Prompts

None

## Requirements

- Node.js >= 18.0.0

## License

MIT License

## Disclaimer

This project is not affiliated with Weibo and is for learning and research purposes only.

**Official site: ** [https://github.com/Selenium39/mcp-server-weibo](https://github.com/Selenium39/mcp-server-weibo)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `browser`
- Tags: `browser automation`, `social media`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `--from git+https://github.com/Selenium39/mcp-server-weibo.git mcp-server-weibo`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/selenium39-weibo.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
