---
title: "browser-use-mcp-server"
description: "An MCP server that enables AI assistants to control a web browser through natural language commands, allowing them to navigate websites and extract information via SSE transport."
---

# browser-use-mcp-server

An MCP server that enables AI assistants to control a web browser through natural language commands, allowing them to navigate websites and extract information via SSE transport.

# ➡️ browser-use mcp server

[browser-use](https://github.com/browser-use/browser-use) MCP Server with SSE
transport

### requirements

- uv

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### quickstart

```
uv sync
uv pip install playwright
uv run playwright install --with-deps --no-shell chromium
uv run server --port 8000
```

- the .env requires the following:

```
OPENAI_API_KEY=[your api key]
CHROME_PATH=[only change this if you have a custom chrome build]
PATIENT=false # Set to true if you want api calls to wait for tasks to complete (default is false)
```

- we will be adding support for other LLM providers to power browser-use
  (claude, grok, bedrock, etc)

when building the docker image, you can use Docker secrets for VNC password:

```
# With Docker secrets (recommended for production)
echo "your-secure-password" > vnc_password.txt
docker run -v $(pwd)/vnc_password.txt:/run/secrets/vnc_password your-image-name

# Or during development with the default password
docker build .
```

### tools

- [x] SSE transport
- [x] browser_use - Initiates browser tasks with URL and action
- [x] browser_get_result - Retrieves results of async browser tasks
- [x] VNC server - stream the dockerized browser to your client

### VNC

the dockerfile has a vnc server with a default password of browser-use. connect
to it:

```
docker build -t  browser-use-mcp-server .
docker run --rm -p8000:8000 -p5900:5900 browser-use-mcp-server
git clone https://github.com/novnc/noVNC
cd noVNC
./utils/novnc_proxy --vnc localhost:5900
```

### supported clients

- cursor.ai
- claude desktop
- claude code
- windsurf ([windsurf](https://codeium.com/windsurf) does not support SSE
  yet)

### usage

after running the server, add http://localhost:8000/sse to your client UI, or in
a mcp.json file:

```json
{
  "mcpServers": {
    "browser-use-mcp-server": {
      "url": "http://localhost:8000/sse"
    }
  }
}
```

#### cursor

- `./.cursor/mcp.json`

#### windsurf

- `~/.codeium/windsurf/mcp_config.json`

#### claude

- `~/Library/Application Support/Claude/claude_desktop_config.json`
- `%APPDATA%Claudeclaude_desktop_config.json`

then try asking your LLM the following:

`open https://news.ycombinator.com and return the top ranked article`

### help

for issues or interest reach out @ https://cobrowser.xyz

# stars

**Official site: ** [https://github.com/co-browser/browser-use-mcp-server](https://github.com/co-browser/browser-use-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `browser`
- Tags: `browser automation`, `chinese`

## MCP Configuration

- Transport: `http`
- Command: ``
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/co-browser-browser-use.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
