---
title: "mcp-server-tapd"
description: "TAPD is Tencent's agile R&D management platform, covering the entire R&D lifecycle of requirements, planning, development, testing, and release. Supports natural language conversations with TAPD for m…"
---

# mcp-server-tapd

TAPD is Tencent's agile R&D management platform, covering the entire R&D lifecycle of requirements, planning, development, testing, and release. Supports natural language conversations with TAPD for m…

# TAPD MCP Server

TAPD is Tencent's agile R&D management platform, covering the entire R&D lifecycle of requirements, planning, development, testing, and release. It supports natural language conversations with TAPD to manage requirements, defects, tasks, iterations, etc.

* Seamless integration with the TAPD API to improve development efficiency

## System requirements

* uv
* TAPD API Token

## Setup Guide
### Install uv
```
brew install uv
# OR
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Get TAPD API Token
Get API tokens from: https://www.tapd.cn/open_platform/open_api_redirect

1. Not registered yet? Please go to [Register](https://www.tapd.cn?from_partner=copilot&source=tapd_operation_copilot)
2. Registered but haven't authorized the API? Go to the API configuration: log in to TAPD and click ["Company Management - API Account Management"](https://www.tapd.cn/open_platform/open_api_redirect), then copy the API account and API key.
3. Parameters
- TAPD_API_USER: API account
- TAPD_API_PASSWORD: API key
- BOT_URL: WeCom bot webhook address, optional; only needed if you want to send messages to a WeCom group

## Configuration and Usage
### Claude Desktop Setup
```
{
  "mcpServers": {
    "mcp-server-tapd": {
      "command": "uvx",
      "args": ["mcp-server-tapd"],
      "env": {
        "TAPD_API_USER": "",
        "TAPD_API_PASSWORD": "",
        "TAPD_API_BASE_URL": "https://api.tapd.cn",
        "TAPD_BASE_URL": "https://www.tapd.cn",
        "BOT_URL": ""
      }
    }
  }
}
```

### Cursor IDE Setup
1. Open Cursor Settings
2. Navigate to Features > MCP Servers
3. Click Add new MCP server

For stdio transport:
```
name: mcp-server-tapd
type: command
command: uvx mcp-server-tapd --api-user=your_api_user --api-password=your_api_password --api-base-url=https://api.tapd.cn --tapd-base-url=https://www.tapd.cn  --bot-url=https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=XXX
```

**Official site: ** [https://cnb.cool/tapd_mcp/mcp-server-tapd](https://cnb.cool/tapd_mcp/mcp-server-tapd)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `developer tools`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `mcp-server-tapd`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/tapd-mcp-tapd.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
