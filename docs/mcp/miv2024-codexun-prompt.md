---
title: "codexun-prompt-mcp"
description: "Preface This is a tool for managing your prompts, allowing you to search for your own prompts directly within AI conversations. It's very simple to use, hence the name EasyPrompt. Usage Environment -…"
---

# codexun-prompt-mcp

Preface This is a tool for managing your prompts, allowing you to search for your own prompts directly within AI conversations. It's very simple to use, hence the name EasyPrompt. Usage Environment -…

# Preface

This is a tool for managing your prompts, allowing you to search for your own prompts directly within AI conversations. It's very simple to use, hence the name EasyPrompt.

# Usage Environment
- EasyPrompt supports usage in CherryStdio and Chatbox.
- EasyPrompt supports usage in programming tools like Trae and Cursor that support mcp.
- EasyPrompt can be used in Chrome browser and Doupao PC browser environments. Through a browser extension, you can easily access your own prompts with one click. (Recommended for beginners!)

# How to Use

1. First, go to the official website https://prompt.code2ai.top and register an account.
2. Click on [Avatar] -> [User Center] -> api-keys.
3. Create an API key.

# Configuring mcp

{
  "mcpServers": {
    "codexun-prompt": {
      "command": "npx",
      "args": [
        "codexun-prompt-mcp@1.0.11",
        "--token",
        "sk-you-api-key"
      ],
      "disabled": false,
      "alwaysAllow": []
    }
  }
}

When configuring, replace `sk-you-api-key` with your actual API key.

Note: `codexun-prompt-mcp` may have updates, so it's recommended to use the latest version.

# Tutorial

https://mp.weixin.qq.com/s/Sm58jONFtsLEa38aF0rkPQ

# Browser Extension

https://prompt.code2ai.top/posts/prompt-browser-ext

# Official Website

https://prompt.code2ai.top/

**Official site: ** [https://www.npmjs.com/package/codexun-prompt-mcp?activeTab=code](https://www.npmjs.com/package/codexun-prompt-mcp?activeTab=code)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `browser`, `media`
- Tags: `developer tools`, `browser automation`, `entertainment and media`, `prompt`, `prompt管理`, `prompt收藏`, `prompt插件`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `codexun-prompt-mcp@1.0.11 --token sk-you-api-key`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/miv2024-codexun-prompt.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
