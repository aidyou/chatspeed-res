---
title: "mcp-server-yinxiang"
description: "YXBJ-MCP is an MCP (Model Context Protocol) server that lets AI assistants (such as Cursor) interact directly with Evernote (Yinxiang), enabling note creation and saving. It supports connection testin…"
---

# mcp-server-yinxiang

YXBJ-MCP is an MCP (Model Context Protocol) server that lets AI assistants (such as Cursor) interact directly with Evernote (Yinxiang), enabling note creation and saving. It supports connection testin…

# YXBJ-MCP

> YXBJ-MCP is an MCP service that supports saving text content to your Evernote (Yinxiang)

## Introduction

YXBJ-MCP is an MCP (Model Context Protocol) service that lets you save content directly to Evernote while chatting with AI tools such as Cursor, Claude, Cherry Studio, etc.

## Features

- **Connection test** - test the MCP connection status
- **Save notes** - save content to Evernote
- **Markdown support** - supports rich text formats
- **Environment variable configuration** - secure authentication

## Installation and Usage

### 1. Get an authorization token
- Visit the Evernote OAuth authorization page: https://app.yinxiang.com/third/mcp-oauth/
- Log in to your Evernote account and get the MCP service authorization token

### 2. Use npx to install

```bash
# Run directly, no install needed
npx yxbj-mcp
```

### 3. Environment configuration
Before using, set the environment variable:
```bash
# Set the environment variable temporarily and run
YINXIANG_AUTH_TOKEN="your_token" npx yxbj-mcp
```
> Replace "your_token" with the authorization token you obtained

## Using in Cursor

1. Add to Cursor's MCP configuration:
```json
{
  "mcpServers": {
    "yxbj-mcp": {
      "command": "npx",
      "args": ["yxbj-mcp"],
      "env": {
        "YINXIANG_AUTH_TOKEN": "your_token_here"
      }
    }
  }
}
```
> Replace "your_token_here" with the authorization token you obtained
2. Restart Cursor to use Evernote features in the AI assistant

## Available Tools

### test-connection
Tests the MCP connection status and returns system info

### save-note
Saves a note to Evernote
- `title`: note title
- `content`: note content (supports Markdown)

## Development

```bash
# Install dependencies
npm install

# Development mode (TypeScript)
npm run build

# Tests
npm test
```

## License

ISC

## Contributing

Issues and Pull Requests are welcome!

**Official site: ** [https://github.com/yinxiang-team/YXBJ-MCP](https://github.com/yinxiang-team/YXBJ-MCP)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `memory`
- Tags: `knowledge and memory`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `yxbj-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/yinxiangnote-yinxiang.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
