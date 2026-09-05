---
title: "obs-mcp"
description: "A server that provides tools to control OBS Studio remotely via the OBS WebSocket protocol, enabling management of scenes, sources, streaming, and recording through an MCP client interface."
---

# obs-mcp

A server that provides tools to control OBS Studio remotely via the OBS WebSocket protocol, enabling management of scenes, sources, streaming, and recording through an MCP client interface.

# OBS MCP Server

An MCP server for OBS Studio that provides tools to control OBS via the OBS WebSocket protocol.

## Features

- Connect to OBS WebSocket server
- Control OBS via MCP tools
- Provides tools for:
  - General operations
  - Scene management
  - Source control
  - Scene item manipulation
  - Streaming and recording
  - Transitions

## Installation

```bash
npm install
npm run build
```

## Usage

1. Make sure OBS Studio is running with WebSocket server enabled (Tools > WebSocket Server Settings). Note the password for the WS.
2. Set the WebSocket password in environment variable (if needed):

```bash
export OBS_WEBSOCKET_PASSWORD="your_password_here"
```

3. Run the OBS MCP server to see that it is able to build and connect:

```bash
npm run build
npm run start
```

4. Provision you Claude desktop with the MCP server settings:

```json
{
  "mcpServers": {
    "obs": {
      "command": "node",
      "args": [
        "/build/index.js"
      ],
      "env": {
        "OBS_WEBSOCKET_PASSWORD": "
"
      }
    }
  }
}
```

5. Use Claude to control your OBS!

## Available Tools

The server provides tools organized by category:

- General tools: Version info, stats, hotkeys, studio mode
- Scene tools: List scenes, switch scenes, create/remove scenes
- Source tools: Manage sources, settings, audio levels, mute/unmute
- Scene item tools: Manage items in scenes (position, visibility, etc.)
- Streaming tools: Start/stop streaming, recording, virtual camera
- Transition tools: Set transitions, durations, trigger transitions

## Environment Variables

- `OBS_WEBSOCKET_URL`: WebSocket URL (default: ws://localhost:4455)
- `OBS_WEBSOCKET_PASSWORD`: Password for authenticating with OBS WebSocket (if required)

## Requirements

- Node.js 16+
- OBS Studio 31+ with WebSocket server enabled
- Claude desktop

## License

See the [LICENSE](https://github.com/royshil/obs-mcp/blob/HEAD/LICENSE) file for details.

**Official site: ** [https://github.com/royshil/obs-mcp](https://github.com/royshil/obs-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `os automation`, `entertainment and media`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `node`
- Args: `<obs-mcp_root>/build/index.js`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/royshil-obs.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
