---
title: "ZIZAI-Recruitment-Platform"
description: "ZIZAI Recruitment Platform(https://zizai.work) is a core API service that is fully compatible with the MCP protocol, making it the first recruitment platform service provider in China to support this…"
---

# ZIZAI-Recruitment-Platform

ZIZAI Recruitment Platform(https://zizai.work) is a core API service that is fully compatible with the MCP protocol, making it the first recruitment platform service provider in China to support this…

# ZIZAI Recruitment MCP Server

MCP Server for the ZIZAI Recruitment API.

# ZIZAI Recruitment
ZIZAI Recruitment ([https://zizai.work](https://zizai.work)) is a new-generation intelligent recruitment platform based on professional assessment, helping talents and positions match efficiently and accurately.

Join us and experience the power of intelligent recruitment right away!

## Tools

1. `get-job-list`
   - Gets the recommended job list
   - Input:
     - `keyword` (string, optional): job search keyword.
     - `recruitType` (number, optional): job type, 1-social recruitment, 2-campus recruitment, 3-internship
   - Returns:
     - Array of:
       - `workPin`: string
       - `name`: string
       - `entityName`: string
       - `entityShortname`: string
       - `responsibility`: string
       - `requirement`: string
       - `welfare`: string
       - `salary`: { minSalary: number, maxSalary: number } | string
       - `detailUrl`: string

2. `apply-for-job`
   - Applies for a job
   - Inputs:
     - `workPin` (string): the unique job code
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
