---
title: "dingding-mcp"
description: "A Model Control Protocol server that provides access to DingDing (Chinese workplace collaboration platform) API features, including retrieving access tokens, department lists, user information, and se…"
---

# dingding-mcp

A Model Control Protocol server that provides access to DingDing (Chinese workplace collaboration platform) API features, including retrieving access tokens, department lists, user information, and se…

# DingTalk MCP Service

This is a DingTalk service based on MCP (Model Control Protocol) that provides access to DingTalk API features.

## Features

1. Get the DingTalk Access Token
2. Get the department list
3. Get the user list of a department
4. Query user details by name (including traversing departments to find users)

## Requirements

- Python 3.12+
- Docker (recommended)
- DingTalk app credentials

## Installation and Configuration

### 1. Get DingTalk app credentials

1. Log in to the [DingTalk Open Platform](https://open.dingtalk.com/)
2. Create an internal enterprise app
3. Get the app's AppKey and AppSecret

### 2. Configure environment variables

Set the following environment variables:
```bash
DINGDING_APP_KEY=YOUR_APP_KEY
DINGDING_APP_SECRET=YOUR_APP_SECRET
```

## Usage

### In the Claude Desktop client

1. Add the following configuration to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "dingding": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e", "DINGDING_APP_KEY=YOUR_APP_KEY",
        "-e", "DINGDING_APP_SECRET=YOUR_APP_SECRET",
        "ghcr.io/YOUR_USERNAME/dingding-mcp:latest"
      ]
    }
  }
}
```

### Local development

1. Clone the repository:
```bash
git clone
cd dingding_chat
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the service:
```bash
python src/server.py
```

### Docker deployment

1. Pull the image:
```bash
docker pull ghcr.io/YOUR_USERNAME/dingding-mcp:latest
```

2. Run the container:
```bash
docker run -d --name dingding-mcp \
  -e DINGDING_APP_KEY=YOUR_APP_KEY \
  -e DINGDING_APP_SECRET=YOUR_APP_SECRET \
  ghcr.io/YOUR_USERNAME/dingding-mcp:latest
```

## API Description

### 1. Get Access Token
- Function: get the DingTalk API access token
- Tool name: `get_access_token`
- Parameters: none
- Returns: access token string

### 2. Get the department list
- Function: get the enterprise department list
- Tool name: `get_department_list`
- Parameters:
  - fetch_child: whether to fetch the sub-department list (optional, default true)
- Returns: department list info (including department ID, name, parent department ID, etc.)

### 3. Get the user list of a department
- Function: get the user list of a specified department
- Tool name: `get_department_users`
- Parameters:
  - department_id: department ID (required)
- Returns: department user list (including user ID, name, etc.)

### 4. Search users by name
- Function: query detailed user information by user name
- Tool name: `search_user_by_name`
- Parameters:
  - name: user name
- Returns: detailed user info (including user ID, name, phone, email, position, department, etc.)

## Notes

1. Make sure the DingTalk app credentials are configured correctly
2. Due to DingTalk API limitations, querying user information requires traversing all departments, which may take some time
3. We recommend using Docker deployment in production to ensure environment consistency

## License

MIT License

**Official site: ** [https://github.com/wllcnm/dingding-mcp](https://github.com/wllcnm/dingding-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `communication`
- Tags: `communication`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `docker`
- Args: `run -i --rm -e DINGDING_APP_KEY=YOUR_APP_KEY -e DINGDING_APP_SECRET=YOUR_APP_SECRET ghcr.io/YOUR_USERNAME/dingding-mcp:latest`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/wllcnm-dingding.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
