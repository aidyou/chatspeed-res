---
title: "dingding_mcp_v2"
description: "A Model Control Protocol server for integrating with DingTalk, enabling users to send messages, retrieve conversation/user information, and query calendar events through Claude."
---

# dingding_mcp_v2

A Model Control Protocol server for integrating with DingTalk, enabling users to send messages, retrieve conversation/user information, and query calendar events through Claude.

# DingTalk MCP Server V2

This is a DingTalk bot server implementation based on MCP (Model Control Protocol). It provides various features for interacting with DingTalk, including sending messages, getting conversation info, user info, and calendar events.

## Features

- Send messages to DingTalk conversations
- Get DingTalk conversation information
- Get DingTalk user information
- Query user calendar events
- Supports multiple message types (text, Markdown, links, etc.)

## Requirements

- Python 3.10+
- MCP 0.1.0+
- aiohttp 3.9.1+

## Environment Variable Configuration

The following environment variables need to be set before use:

- `DINGTALK_APP_KEY`: the AppKey of your DingTalk app
- `DINGTALK_APP_SECRET`: the AppSecret of your DingTalk app

## Using with the Claude client

1. Add the following configuration to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "dingding": {
      "command": "sh",
      "args": [
        "-c",
        "docker ps -a | grep mcp-dingding-v2 | awk '{print $1}' | xargs -r docker rm -f > /dev/null 2>&1; docker pull ghcr.io/wllcnm/mcp-dingding-v2:latest > /dev/null 2>&1; docker run -i --rm --name mcp-dingding-v2 -e DINGTALK_APP_KEY=YOUR_APP_KEY -e DINGTALK_APP_SECRET=YOUR_APP_SECRET ghcr.io/wllcnm/mcp-dingding-v2:latest"
      ]
    }
  }
}
```

2. Restart the Claude client

Note: the startup command above will:
1. Find and remove all old mcp-dingding-v2 containers
2. Pull the latest image from GitHub
3. Use the `--name` parameter to give the container a fixed name
4. Use the `--rm` parameter to remove the container automatically when it stops

Command explanation:
- `docker ps -a | grep mcp-dingding-v2 | awk '{print $1}' | xargs -r docker rm -f`: removes all old containers
- `docker pull ghcr.io/wllcnm/mcp-dingding-v2:latest`: pulls the latest image
- `docker run -i --rm --name mcp-dingding-v2 ...`: runs the new container
- `> /dev/null 2>&1`: hides unnecessary output

## Local Development

### Installation

```bash
pip install -r requirements.txt
```

### Running

Run the server directly:
```bash
python src/server.py
```

Run with Docker:
```bash
# Clean up old containers
docker ps -a | grep mcp-dingding-v2 | awk '{print $1}' | xargs -r docker rm -f

# Build and run a new container
docker build -t dingding-mcp-v2 .
docker run -i --rm --name mcp-dingding-v2 \
  -e DINGTALK_APP_KEY=your_app_key \
  -e DINGTALK_APP_SECRET=your_app_secret \
  dingding-mcp-v2
```

## API Tools

### 1. send_message
Sends a message to a DingTalk conversation
- Parameters:
  - conversation_id: conversation ID
  - message: message content
  - msg_type: message type (optional, default text)

### 2. get_conversation_info
Gets DingTalk conversation information
- Parameters:
  - conversation_id: conversation ID

### 3. get_user_info
Gets DingTalk user information
- Parameters:
  - user_id: user ID

### 4. get_calendar_list
Queries a user's calendar event list
- Parameters:
  - userid: user ID (required)
  - start_time: start timestamp (milliseconds, optional)
  - end_time: end timestamp (milliseconds, optional)
  - max_results: maximum number of results (optional, default 50)
  - next_token: pagination token (optional)
- Returns:
  - events: calendar event list
    - summary: event title
    - start_time: start time
    - end_time: end time
    - location: location
    - organizer: organizer
    - description: description
    - status: status
    - attendees: attendee list
  - next_token: token for the next page
  - total: number of events returned this time

## Usage Examples

In Claude, you can use the tools like this:

```json
{
  "tool": "send_message",
  "arguments": {
    "conversation_id": "YOUR_CONVERSATION_ID",
    "message": "Hello, DingTalk!",
    "msg_type": "text"
  }
}
```

Calendar query example:
```json
{
  "tool": "get_calendar_list",
  "arguments": {
    "userid": "USER_ID",
    "start_time": 1704067200000,  // 2024-01-01 00:00:00
    "end_time": 1704153600000,    // 2024-01-02 00:00:00
    "max_results": 10
  }
}
```

## Notes

1. Security
   - Keep your DingTalk API credentials safe
   - Do not share your config file in public places
   - Use environment variables instead of hardcoding credentials

2. Troubleshooting
   - Check that the API credentials are correct
   - Make sure the network connection is working
   - Check the log output for detailed error information

## License

MIT

**Official site: ** [https://github.com/wllcnm/dingding_mcp_v2](https://github.com/wllcnm/dingding_mcp_v2)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `productivity`, `communication`
- Tags: `communication`, `calendar management`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `sh`
- Args: `-c docker ps -a | grep mcp-dingding-v2 | awk '{print $1}' | xargs -r docker rm -f > /dev/null 2>&1; docker pull ghcr.io/wllcnm/mcp-dingding-v2:latest > /dev/null 2>&1; docker run -i --rm --name mcp-dingding-v2 -e DINGTALK_APP_KEY=YOUR_APP_KEY -e DINGTALK_APP_SECRET=YOUR_APP_SECRET ghcr.io/wllcnm/mcp-dingding-v2:latest`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/wllcnm-dingding-v2.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
