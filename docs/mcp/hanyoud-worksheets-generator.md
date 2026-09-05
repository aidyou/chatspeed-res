---
title: "Worksheets_generator"
description: "The Danmoshui MCP remote server can generate and create high-definition PDF format Chinese character sheets, word dictation/pinyin practice sheets, math mental arithmetic exercises, Hengshui-style Eng…"
---

# Worksheets_generator

The Danmoshui MCP remote server can generate and create high-definition PDF format Chinese character sheets, word dictation/pinyin practice sheets, math mental arithmetic exercises, Hengshui-style Eng…

Light Ink Character Sheet MCP Remote Service, after configuration, can directly generate and download character sheets in AI conversations.

SSE address: https://danmoshui.com/sse

Kouzi Space configuration example:

```

{

  "mcpServers": {

    "淡墨水字帖": {

      "url": "https://danmoshui.com/sse"

    }

  }

}

```
Cherry-Studio configuration example:

```

{

  "mcpServers": {

    "淡墨水字帖": {

      "type": "sse",

      "url": "https://danmoshui.com/sse"

    }

  }

}

```

**Official site: ** [https://danmoshui.com/software](https://danmoshui.com/software)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `knowledge and memory`, `art and culture`, `字帖生成`, `chinese`

## MCP Configuration

- Transport: `http`
- Command: ``
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/hanyoud-worksheets-generator.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
