---
title: "zoom-mcp-server"
description: "An AI-assisted server that enables dating within Zoom meetings, requiring Zoom API credentials (Client ID, Client Secret, Account ID) for setup."
---

# zoom-mcp-server

An AI-assisted server that enables dating within Zoom meetings, requiring Zoom API credentials (Client ID, Client Secret, Account ID) for setup.

# Zoom MCP Server

[![NPM Version](/mcp-assets/8cbae245c0357e4b060d80948c0bef6f.svg)](https://www.npmjs.com/package/@yitianyigexiangfa/zoom-mcp-server) ![MIT licensed](/mcp-assets/5816f652aa1f0cc4eedb21a2f733e09e.svg) [Smithery](https://smithery.ai/server/@JavaProgrammerLB/zoom-mcp-server) ![Zoom MCP Server](/mcp-assets/c1486b4e2d8cfd67ed0257afeefda188.svg "MCP Server")

Now you can date a Zoom meeting with AI's help

## Usage

### 1. list meetings

- `list my meetings`
- `list my upcoming meetings`

### 2. create a meeting

- `Schedule a meeting at today 3 pm with a introduce mcp topic`

### 3. delete a meeting

- `delete the latest meeting`
- `delete the 86226580854 meeting`

### 4. get a meeting detail

- `Retrieve the latest meeting's details`
- `Retrieve 86226580854 meeting's details`

## 2 Steps to play with zoom-mcp-server

- Get Zoom Client ID, Zoom Client Secret and Account ID
- Config MCP server

### 1. Get Zoom Client ID, Zoom Client Secret and Account ID

1. vist [Zoom Marketplace](https://marketplace.zoom.us/)
1. Build App and choose **Server to Server OAuth App**
1. Add Scope > Meeting > Select All Meeting Permissions
1. Active your app
   then you can get **Account ID**, **Client ID**, **Client Secret** in App Credentials page

### 2. Config MCP Server

```json
{
  "mcpServers": {
    "zoom-mcp-server": {
      "command": "npx",
      "args": ["-y", "@yitianyigexiangfa/zoom-mcp-server@latest"],
      "env": {
        "ZOOM_ACCOUNT_ID": "${ZOOM_ACCOUNT_ID}",
        "ZOOM_CLIENT_ID": "${ZOOM_CLIENT_ID}",
        "ZOOM_CLIENT_SECRET": "${ZOOM_CLIENT_SECRET}"
      }
    }
  }
}
```

**Official site: ** [https://github.com/JavaProgrammerLB/zoom-mcp-server](https://github.com/JavaProgrammerLB/zoom-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `communication`
- Tags: `communication`, `social media`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @yitianyigexiangfa/zoom-mcp-server@latest`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/javaprogrammerlb-zoom.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
