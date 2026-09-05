---
title: "wechat_send_mcp_serve"
description: "wechatsend MCP service: an MCP (Model Context Protocol) service that sends files to WeChat groups through the WeCom bot Webhook interface. Features - Supports multiple file input methods: local files…"
---

# wechat_send_mcp_serve

wechatsend MCP service: an MCP (Model Context Protocol) service that sends files to WeChat groups through the WeCom bot Webhook interface. Features - Supports multiple file input methods: local files…

# wechat_send MCP Service

An MCP (Model Context Protocol) service that sends files to WeChat groups through the WeCom bot Webhook interface.

## Features

- Supports multiple file input methods: local files, network files, and Base64-encoded files
- Built on the MCP protocol, integrable into various AI assistants and automation tools
- Designed for WeCom group chats, supporting file sharing
- Complete error handling and temporary file management

## Install dependencies

```bash
pip install -r requirements.txt
```

## Startup

### 1. Start as a standalone MCP Server via stdio:
```bash
python server.py
```

### 2. Start as an HTTP service (for platforms like Dify):
```bash
python server.py --http 8000
```

## Tools

### send_file tool

Sends files to a group chat via the WeCom bot.

**Parameters:**
- `webhook_url` (required): the WeCom bot Webhook address
- `file_path` (optional): local file path
- `file_url` (optional): a file URL downloaded over HTTP(S)
- `file_base64` (optional): Base64 encoding of the file content

**Usage:**
Choose one of three file input methods:
- Pass `file_path` directly - specify a local file path
- Pass `file_url` - automatically download the network file to a temporary directory
- Pass `file_base64` - decode the Base64-encoded file content into a temporary file

## Configuration

### WeCom bot configuration

1. Add a bot to the WeCom group
2. Get the Webhook address, in the format: `https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=YOUR_KEY`
3. Pass the Webhook address as the `webhook_url` parameter

### Environment variables

- `WEBHOOK_URL`: the default WeCom bot Webhook address (optional)

## Usage Examples

### MCP client call example

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "send_file",
    "arguments": {
      "webhook_url": "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=YOUR_KEY",
      "file_url": "https://example.com/file.pdf"
    }
  }
}
```

### HTTP API call example

```bash
curl -X POST https://your-server.com/ \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/call",
    "params": {
      "name": "send_file",
      "arguments": {
        "webhook_url": "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=YOUR_KEY",
        "file_path": "/path/to/your/file.pdf"
      }
    }
  }'
```

## Technical Architecture

- **Core module**: `main.py` - contains the core file-sending logic
- **MCP service**: `server.py` - the MCP server built on the FastMCP framework
- **Configuration**: `mcp.json` - service config and metadata
- **Dependencies**: `requirements.txt` - Python package dependencies

## Deployment

### Local deployment
```bash
git clone
cd wechat_send
pip install -r requirements.txt
python server.py
```

### Cloud platform deployment
- Supports Railway, Heroku, Docker, and other platforms
- Make sure Python 3.8+ and the required dependencies are installed
- Set the necessary environment variables

## License

MIT License

## Contributing

Issues and Pull Requests are welcome to improve this project.

**Official site: ** [https://github.com/NANYAN-01/wechat-send-mcp](https://github.com/NANYAN-01/wechat-send-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `communication`
- Tags: `communication`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx wechat-send`
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/nanyan001-wechat-send-serve.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
