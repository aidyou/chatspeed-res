---
title: "figma-mcp"
description: "Allow your AI coding agents to access Figma files & prototypes directly. You can DM me for any issues / improvements: https://x.com/jasonzhou1993 1. Access all figma pages 2. Access all figma componen…"
---

# figma-mcp

Allow your AI coding agents to access Figma files & prototypes directly. You can DM me for any issues / improvements: https://x.com/jasonzhou1993 1. Access all figma pages 2. Access all figma componen…

# Figma MCP Python

[![PyPI version](/mcp-assets/dec8b35f184274331a6b0bde60435e1d.svg)](https://badge.fury.io/py/figma-mcp)

Allow your AI coding agents to access Figma files & prototypes directly.
You can DM me for any issues / improvements: https://x.com/jasonzhou1993

  

## Quick Installation with pipx

```bash
pipx install figma-mcp
```

### For Cursor:

1. In settings, add an MCP server using the command:
```shell
figma-mcp --figma-api-key=your_figma_key
```

2. OR Add a `.cursor/mcp.json` file in your project:

```json
{
  "mcpServers": {
    "figma-python": {
      "command": "figma-mcp",
      "args": [
        "--figma-api-key=your_figma_key"
      ]
    } 
  }
}
```

### For other IDEs like Windsurf, use an MCP configuration file (e.g., `mcp_config.json`):

```json
{
  "mcpServers": {
    "figma-python": {
      "command": "figma-mcp",
      "args": [
        "--figma-api-key=your_figma_key"
      ]
    } 
  }
}
```

## Install uv and set up the environment
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv
source .venv/bin/activate
uv sync
```

## Test locally
```bash
python -m figma_mcp.main
```

**Official site: ** [https://github.com/JayZeeDesign/figma-mcp](https://github.com/JayZeeDesign/figma-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `art and culture`, `image and video processing`, `developer tools`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `figma-mcp`
- Args: `--figma-api-key=your_figma_key`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/jayzeedesign-figma.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
