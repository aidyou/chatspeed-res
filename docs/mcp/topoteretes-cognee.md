---
title: "cognee"
description: "Memory manager for AI apps and Agents using various graph and vector stores and allowing ingestion from 30+ data sources"
---

# cognee

Memory manager for AI apps and Agents using various graph and vector stores and allowing ingestion from 30+ data sources

# cognee MCP server

### Installing Manually
A MCP server project
=======
1. Clone the [cognee](https://github.com/topoteretes/cognee) repo

2. Install dependencies

```
brew install uv
```

```jsx
cd cognee-mcp
uv sync --dev --all-extras --reinstall
```

3. Activate the venv with

```jsx
source .venv/bin/activate
```

4. Add the new server to your Claude config:

The file should be located here: ~/Library/Application Support/Claude/
```
cd ~/Library/Application Support/Claude/
```
You need to create claude_desktop_config.json in this folder if it doesn't exist
Make sure to add your paths and LLM API key to the file bellow
Use your editor of choice, for example Nano:
```
nano claude_desktop_config.json
```

```
{
	"mcpServers": {
		"cognee": {
			"command": "/Users/{user}/cognee/.venv/bin/uv",
			"args": [
        "--directory",
        "/Users/{user}/cognee/cognee-mcp",
        "run",
        "cognee"
      ],
      "env": {
        "ENV": "local",
        "TOKENIZERS_PARALLELISM": "false",
        "LLM_API_KEY": "sk-"
      }
		}
	}
}
```

Restart your Claude desktop.

### Installing via Smithery

To install Cognee for Claude Desktop automatically via [Smithery](https://smithery.ai/server/cognee):

```bash
npx -y @smithery/cli install cognee --client claude
```

Define cognify tool in server.py
Restart your Claude desktop.

To use debugger, run:
```bash
mcp dev src/server.py
```
Open inspector with timeout passed:
```
http://localhost:5173?timeout=120000
```

To apply new changes while developing cognee you need to do:

1. `poetry lock` in cognee folder
2. `uv sync --dev --all-extras --reinstall`
3. `mcp dev src/server.py`

**Official site: ** [https://github.com/topoteretes/cognee/tree/dev/cognee-mcp](https://github.com/topoteretes/cognee/tree/dev/cognee-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `memory`
- Tags: `knowledge and memory`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `/Users/{user}/cognee/.venv/bin/uv`
- Args: `--directory /Users/{user}/cognee/cognee-mcp run cognee`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/topoteretes-cognee.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
