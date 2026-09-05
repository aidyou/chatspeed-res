---
title: "VJshi-MCP"
description: "You can search for licensed high-definition commercial video material in AI model clients that support the MCP protocol."
---

# VJshi-MCP

You can search for licensed high-definition commercial video material in AI model clients that support the MCP protocol.

# GuangChang (VJSHI) MCP Video Material Search Tool

## Special Note
If the translated text contains garbled characters (caused by forced translation), please switch back to the original text (Chinese) for readability.

---

## Project Overview
Search for licensed high-definition commercial video material in AI model clients that support the MCP protocol.

---

## Core Features
Search and recommend relevant video material from tens of millions of licensed high-definition commercial videos on GuangChang.

### Key Features:
- Massive, licensed, high-definition video material
- Commercial licensing, no copyright risk
- Fast, precise smart search experience
- Structured output for easy downstream processing

---

## Quick Start

### Step 1: Get an API key
Get a server-side key from the [GuangChang MCP official website](https://open.vjshi.com/mcp) page.

> Tip: you need the key to use the search feature.

### Step 2: Complete the configuration
Replace `YOUR_API_KEY` with your actual key, and add the following configuration to an MCP-capable model client.

**Supported clients:** Claude App, Cherry Studio, Cursor, Cline, Windsurf, etc.

```json
{
  "mcpServers": {
    "vjshi-video-mcp": {
      "command": "npx",
      "args": [
        "-y",
        "@vjshi/vjshi-video-mcp@latest"
      ],
      "env": {
        "VJSHI_API_KEY": "YOUR_API_KEY"
      },
      "disabled": false,
      "isActive": true
    }
  }
}
```

---

## License
This project is licensed under the **MIT License**; see the LICENSE file for details.

---

## Contact Us
If you have questions or suggestions, visit [GuangChang MCP](https://open.vjshi.com/mcp) for more help!

**Official site: ** [https://github.com/dioa-design/vjshi-video-mcp](https://github.com/dioa-design/vjshi-video-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `search`, `art and culture`, `entertainment and media`, `光厂`, `vj师网`, `视频素材网`, `高清视频素材下载`, `ae模板下载`, `免费视频素材`, `素材搜索推荐`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @vjshi/vjshi-video-mcp@latest`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/guangchangvjshi-vjshi.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
