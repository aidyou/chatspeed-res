---
title: "mcp-webhook"
description: "Enables sending messages to webhook endpoints through the MCP protocol, supporting custom content, display names, and avatar URLs."
---

# mcp-webhook

Enables sending messages to webhook endpoints through the MCP protocol, supporting custom content, display names, and avatar URLs.

# MCP Webhook Server

An MCP server implementation that integrates with webhooks, providing message sending capabilities.

## Features

* **Generic Webhook Support**: Send messages to any webhook endpoint
* **Custom Username**: Set custom display name for messages
* **Avatar Support**: Customize message avatar
* **MCP Integration**: Works with Dive and other MCP-compatible LLMs

## Installation

```bash
npm install @kevinwatt/mcp-webhook
```

## Configuration with [Dive Desktop](https://github.com/OpenAgentPlatform/Dive)

1. Click "+ Add MCP Server" in Dive Desktop
2. Copy and paste this configuration:

```json
{
  "mcpServers": {
    "webhook": {
      "command": "npx",
      "args": [
        "-y",
        "@kevinwatt/mcp-webhook"
      ],
      "env": {
        "WEBHOOK_URL": "your-webhook-url"
      },
      "alwaysAllow": [
        "send_message"
      ]
    }
  }
}
```

3. Click "Save" to install the MCP server

## Tool Documentation

* **send_message**
  * Send message to webhook endpoint
  * Inputs:
    * `content` (string, required): Message content to send
    * `username` (string, optional): Display name
    * `avatar_url` (string, optional): Avatar URL

## Usage Examples

Ask your LLM to:
```
"Send a message to webhook: Hello World!"
"Send a message with custom name: content='Testing', username='Bot'"
```

## Manual Start

If needed, start the server manually:

```bash
npx @kevinwatt/mcp-webhook
```

## Requirements

* Node.js 18+
* MCP-compatible LLM service

## License

MIT

## Author

kevinwatt

## Keywords

* mcp
* webhook
* chat
* dive
* llm
* automation

**Official site: ** [https://github.com/kevinwatt/mcp-webhook](https://github.com/kevinwatt/mcp-webhook)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `communication`
- Tags: `communication`, `other`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @kevinwatt/mcp-webhook`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/kevinwatt-webhook.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
