---
title: "mcp-notify"
description: "💬 Notify MCP Server An MCP (Model Context Protocol) server for message push, supporting WeCom, DingTalk, Telegram, Bark, Lark, Feishu, and Home Assistant. Installation Method 1: uvx yaml { \"mcpServers…"
---

# mcp-notify

💬 Notify MCP Server An MCP (Model Context Protocol) server for message push, supporting WeCom, DingTalk, Telegram, Bark, Lark, Feishu, and Home Assistant. Installation Method 1: uvx yaml { "mcpServers…

# 💬 Notify MCP Server

An MCP (Model Context Protocol) server for message push, supporting WeCom, DingTalk, Telegram, Bark, Lark, Feishu, and Home Assistant.

## Installation

### Method 1: uvx
```yaml
{
  "mcpServers": {
    "mcp-notify": {
      "command": "uvx",
      "args": ["mcp-notify"],
      "env": {
        "WEWORK_BOT_KEY": "your-wework-bot-key"
      }
    }
  }
}
```
### Method 2: [Smithery](https://smithery.ai/server/@aahl/mcp-notify)
> Requires OAuth authorization or Smithery key

```yaml

{

  "mcpServers": {

    "mcp-aktools": {

      "url": "https://server.smithery.ai/@aahl/mcp-notify/mcp" # Streamable HTTP

    }

  }

}

```
### Method 3: Docker
```bash
mkdir /opt/mcp-notify
cd /opt/mcp-notify
wget https://raw.githubusercontent.com/aahl/mcp-notify/refs/heads/main/docker-compose.yml
docker-compose up -d
```
```yaml
{
  "mcpServers": {
    "mcp-notify": {
      "url": "http://0.0.0.0:8809/mcp" # Streamable HTTP
    }
  }
}
```
### Environment Variables

#### WeCom Group Bot
- `WEWORK_BOT_KEY`: Default key for the WeCom group bot, can also be specified in the prompt

#### WeCom App
- `WEWORK_APP_CORPID`: The ID of the enterprise to which the WeCom app belongs
- `WEWORK_APP_SECRET`: Credential key for the WeCom app
- `WEWORK_APP_AGENTID`: ID of the WeCom app, default: `1000002`
- `WEWORK_APP_TOUSER`: Default recipient ID for WeCom, can also be specified in the prompt, default: `@all`
- `WEWORK_BASE_URL`: Reverse proxy address for the WeCom API, used for trusted IPs, default: `https://qyapi.weixin.qq.com`

#### DingTalk Group Bot
- `DINGTALK_BOT_KEY`: Access token for the DingTalk group bot
- `DINGTALK_BASE_URL`: DingTalk API address, default: `https://oapi.dingtalk.com`

#### Feishu/Lark Group Bot
- `FEISHU_BOT_KEY`: Key for the Feishu group bot, can also be specified in the prompt
- `FEISHU_BASE_URL`: Feishu API address, default: `https://open.feishu.cn`
- `LARK_BOT_KEY`: Key for the Lark group bot, can also be specified in the prompt
- `LARK_BASE_URL`: Lark API address, default: `https://open.larksuite.com`

#### Bark
- `BARK_DEVICE_KEY`: Bark device key, can also be specified in the prompt
- `BARK_BASE_URL`: Bark base URL, default: `https://api.day.app`

#### Telegram
- `TELEGRAM_DEFAULT_CHAT`: Default chat ID for Telegram, can also be specified in the prompt
- `TELEGRAM_BOT_TOKEN`: Telegram bot token
- `TELEGRAM_BASE_URL`: Telegram base URL, default: `https://api.telegram.org`

#### Home Assistant
- `HASS_BASE_URL`: Base URL for Home Assistant, default: `http://homeassistant.local:8123`
- `HASS_ACCESS_TOKEN`: Long-lived access token for Home Assistant
- `HASS_MOBILE_KEY`: Home Assistant mobile device key, can also be specified in the prompt

### Quick Start
- Online Experience: [![fastmcp.cloud](/mcp-assets/0c8c5954cd83912dfc8e38f61cbd6b98.svg)](https://fastmcp.cloud/xiaomi/notify/chat)
- Online Experience: [Smithery](https://smithery.ai/server/@aahl/mcp-notify)
- Add to Cursor [![Install MCP Server](/mcp-assets/ec1e84b0a4f6576d1ecdf0b2651745c5.svg)](https://cursor.com/zh/install-mcp?name=notify&config=eyJjb21tYW5kIjoidXZ4IiwiYXJncyI6WyJtY3Atbm90aWZ5Il19)
- Add to VS Code [![Install MCP Server](/mcp-assets/a81c1fe0f0f40e3d2dd0ff4b019b0fc6.svg)](https://insiders.vscode.dev/redirect?url=vscode:mcp/install%3F%7B%22name%22%3A%22notify%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22mcp-notify%22%5D%7D)
- Add to Cherry Studio [![Install MCP Server](/mcp-assets/973fda9f33903868f3842a3f8c2c4449.svg)](https://gitee.com/link?target=cherrystudio%3A%2F%2Fmcp%2Finstall%3Fservers%3DeyJtY3BTZXJ2ZXJzIjp7Im5vdGlmeSI6eyJjb21tYW5kIjoidXZ4IiwiYXJncyI6WyJtY3Atbm90aWZ5Il19fX0%3D)
- Add to Claude Code, run command: `claude mcp add notify -- uvx mcp-notify`
- Add to OpenAI CodeX, run command: `codex mcp add notify -- uvx mcp-notify`

------

## Related Links
- [Big Pie Report](https://t.me/s/mcpBtc) - A Telegram channel based on this MCP implementation
- https://github.com/hasscc/ai-conversation/discussions/3
- https://linux.do/t/topic/1098688

**Official site: ** [https://github.com/aahl/mcp-notify](https://github.com/aahl/mcp-notify)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `productivity`, `communication`, `media`
- Tags: `communication`, `entertainment and media`, `calendar management`, `notify`, `weixin`, `telegram`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `mcp-notify`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/aalone-notify.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
