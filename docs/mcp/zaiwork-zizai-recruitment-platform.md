---
title: "ZIZAI-Recruitment-Platform"
description: "ZIZAI Recruitment Platform(https://zizai.work) is a core API service that is fully compatible with the MCP protocol, making it the first recruitment platform service provider in China to support this…"
---

# ZIZAI-Recruitment-Platform

ZIZAI Recruitment Platform(https://zizai.work) is a core API service that is fully compatible with the MCP protocol, making it the first recruitment platform service provider in China to support this…

# 自在招聘 MCP Server

MCP Server for 自在招聘 API.

# 自在招聘
自在招聘（[https://zizai.work](https://zizai.work)）是一个基于专业测评的新一代智能招聘平台，帮助人才与职位高效、精准的智能匹配。

加入我们，立即体验智能招聘的魅力！

## Tools

1. `get-job-list`
   - 获取推荐的职位列表
   - Input:
     - `keyword` (string, 可选): 职位搜索关键词。
     - `recruitType` (number, 可选): 职位类型，1-社招，2-校招，2-实习
   - Returns:
     - Array of {
       - `workPin`: string
       - `name`: string
       - `entityName`: string
       - `entityShortname`: string
       - `responsibility`: string
       - `requirement`: string
       - `welfare`: string
       - `salary`: { minSalary: number, maxSalary: number } | string
       - `detailUrl`: string
     }

2. `apply-for-job`
   - 投递职位
   - Inputs:
     - `workPin` (string) 职位唯一码
   - Returns:

## Setup

### API Key
Get a ZIZAI Work API key by following the instructions [here](https://zizai.work/user/apikey).

### Usage with Claude Desktop

Add the following to your `claude_desktop_config.json`:

### NPX

```json
{
  "mcpServers": {
    "zaiwork": {
      "command": "npx",
      "args": [
        "-y",
        "@zizaiwork/mcp"
      ],
      "env": {
        "ZAI_API_KEY": ""
      }
    }
  }
}
```

## License

This MCP server is licensed under the Apache-2.0 License. This means you are free to use, modify, and distribute the software, subject to the terms and conditions of the Apache-2.0 License. For more details, please see the LICENSE file in the project repository.

**Official site: ** [https://github.com/zaiwork/mcp](https://github.com/zaiwork/mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `search`, `research and data`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @zizaiwork/mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/zaiwork-zizai-recruitment-platform.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
