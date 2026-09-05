---
title: "substack-fetcher-mcp"
description: "Enables fetching and reading subscriber-only content from Trade Companion by Adam Mancini on Substack, allowing Claude to access and discuss the latest financial trading articles."
---

# substack-fetcher-mcp

Enables fetching and reading subscriber-only content from Trade Companion by Adam Mancini on Substack, allowing Claude to access and discuss the latest financial trading articles.

# Substack Reader

A tool to fetch and read articles from Trade Companion by Adam Mancini on Substack.

## Setup

### Prerequisites

1. Python 3.8+
2. uv package manager for Python
3. Claude AI assistant

### Installation

1. Install uv package manager if you do not have it already:
```bash
   curl -sSf https://install.ultraviolet.dev | sh
```

2. Create and activate a virtual environment:
```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venvScriptsactivate
```

3. Install dependencies using the pyproject.toml file:
```bash
   uv pip install -e .
```

### Setting up Substack Authentication

To access subscriber-only content, you'll need to provide your Substack cookies:

1. Install the Cookie-Editor extension for your browser:
   - [Chrome Web Store](https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm)
   - [Firefox Add-ons](https://addons.mozilla.org/en-US/firefox/addon/cookie-editor/)

2. Log in to your Substack account at [tradecompanion.substack.com](https://tradecompanion.substack.com)

3. Click on the Cookie-Editor extension icon

4. Click "Export" and select "Export as JSON" (This copies the cookies to your clipboard)

5. Create a file named `substack_cookies.json` in the root directory of this project

6. Paste the copied cookies into this file and save

## Usage with Claude

This tool is designed to be used with Claude AI assistant. To set it up:

1. Configure Claude to use this MCP server by adding the following to your Claude config file:

```json
{
  "mcpServers": {
    "substack_reader": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/substack_reader",
        "run",
        "substack_reader.py"
      ]
    }
  },
  "globalShortcut": "Ctrl+Space"
}
```

Replace `/path/to/substack_reader` with the actual path to your substack_reader directory.

2. When properly configured, Claude will automatically connect to this MCP server when launched.

3. You can then ask Claude to fetch the latest Trade Companion article.

## Features

- Fetches the latest Trade Companion articles by Adam Mancini
- Extracts article content in plain text format
- Preserves headings, paragraphs, and list items
- Excludes the "My Trade Methodology Fundamentals" article

## Privacy Note

Your Substack cookies are stored locally in the `substack_cookies.json` file and are only used to authenticate requests to Substack. They are not sent anywhere else or exposed in any way.

**Official site: ** [https://github.com/pl728/substack-fetcher-mcp](https://github.com/pl728/substack-fetcher-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `finance`, `data`
- Tags: `finance`, `browser automation`, `research and data`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uv`
- Args: `--directory /path/to/substack_reader run substack_reader.py`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/pl728-substack-fetcher.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
