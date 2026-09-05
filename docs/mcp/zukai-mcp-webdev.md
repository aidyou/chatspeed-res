---
title: "webdev-mcp"
description: "An MCP server providing web development tools such as screen capturing capabilities that let AI agents take and work with screenshots of the user's screen."
---

# webdev-mcp

An MCP server providing web development tools such as screen capturing capabilities that let AI agents take and work with screenshots of the user's screen.

# webdev-mcp

An MCP server that provides useful web development tools.

## Usage

### Cursor

- To install in a project, add the MCP server to your `.cursor/mcp.json`:

```json
{
	"mcpServers": {
		"webdev": {
			"command": "npx",
			"args": ["webdev-mcp"],

		}
	}
}
```

- To install globally, add this command to your Cursor settings:

```bash
npx webdev-mcp
```

### Windsurf

- Add the MCP server to your `~/.codeium/windsurf/mcp_config.json` file:

```json
{
	"mcpServers": {
		"webdev": {
			"command": "npx",
			"args": ["webdev-mcp"]
		}
	}
}
```

## Tools

Currently, the only 2 tools are `takeScreenshot` and `listScreens`. Your agent can use the list screens tool to get the screen id of the screen it wants to screenshot.

The tool will return the screenshot as a base64 encoded string.

## Tips

Make sure YOLO mode is on and MCP tools protection is off in your Cursor settings for the best experience. You might have to allow Cursor to record your screen on MacOS.

**Official site: ** [https://github.com/ZukAi-MCP/webdev-mcp](https://github.com/ZukAi-MCP/webdev-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `browser`
- Tags: `developer tools`, `image and video processing`, `browser automation`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `webdev-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/zukai-mcp-webdev.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
