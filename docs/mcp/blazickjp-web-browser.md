---
title: "web-browser-mcp-server"
description: "Enables web browsing capabilities using BeautifulSoup4"
---

# web-browser-mcp-server

Enables web browsing capabilities using BeautifulSoup4

[![Twitter Follow](/mcp-assets/3e82fabdd3d7f3c8bffecf68b940346e.svg)](https://twitter.com/JoeBlazick)
[Smithery](https://smithery.ai/server/web-browser-mcp-server)
[![Python Version](/mcp-assets/4f6146f128339189f0d4b97607879041.svg)](https://www.python.org/downloads/)
[![License: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://opensource.org/licenses/MIT)
[![PyPI Downloads](/mcp-assets/f8c1de5b3c366a7630260f8a746beba5.svg)](https://pypi.org/project/web-browser-mcp-server/)
[![PyPI Version](/mcp-assets/0002d1bc4f92679c760e34714252a2a1.svg)](https://pypi.org/project/web-browser-mcp-server/)

## ✨ Features

> 🌐 Enable AI assistants to browse and extract content from the web through a simple MCP interface.

The Web Browser MCP Server provides AI models with the ability to browse websites, extract content, and understand web pages through the Message Control Protocol (MCP). It enables smart content extraction with CSS selectors and robust error handling.

  
🤝 **[Contribute](https://github.com/blazickjp/web-browser-mcp-server/blob/main/CONTRIBUTING.md)** • 
📝 **[Report Bug](https://github.com/blazickjp/web-browser-mcp-server/issues)**

## ✨ Core Features

- 🎯 **Smart Content Extraction**: Target exactly what you need with CSS selectors
- ⚡ **Lightning Fast**: Built with async processing for optimal performance
- 📊 **Rich Metadata**: Capture titles, links, and structured content
- 🛡️ **Robust & Reliable**: Built-in error handling and timeout management
- 🌍 **Cross-Platform**: Works everywhere Python runs

## 🚀 Quick Start

### Installing via Smithery

To install Web Browser Server for Claude Desktop automatically via [Smithery](https://smithery.ai/server/web-browser-mcp-server):

```bash
npx -y @smithery/cli install web-browser-mcp-server --client claude
```

### Installing Manually
Install using uv:

```bash
uv tool install web-browser-mcp-server
```

For development:

```bash
# Clone and set up development environment
git clone https://github.com/blazickjp/web-browser-mcp-server.git
cd web-browser-mcp-server

# Create and activate virtual environment
uv venv
source .venv/bin/activate

# Install with test dependencies
uv pip install -e ".[test]"
```

### 🔌 MCP Integration

Add this configuration to your MCP client config file:

```json
{
    "mcpServers": {
        "web-browser-mcp-server": {
            "command": "uv",
            "args": [
                "tool",
                "run",
                "web-browser-mcp-server"
            ],
            "env": {
                "REQUEST_TIMEOUT": "30"
            }
        }
    }
}
```

For Development:

```json
{
    "mcpServers": {
        "web-browser-mcp-server": {
            "command": "uv",
            "args": [
                "--directory",
                "path/to/cloned/web-browser-mcp-server",
                "run",
                "web-browser-mcp-server"
            ],
            "env": {
                "REQUEST_TIMEOUT": "30"
            }
        }
    }
}
```

## 💡 Available Tools

The server provides a powerful web browsing tool:

### browse_webpage
Browse and extract content from web pages with optional CSS selectors:

```python
# Basic webpage fetch
result = await call_tool("browse_webpage", {
    "url": "https://example.com"
})

# Target specific content with CSS selectors
result = await call_tool("browse_webpage", {
    "url": "https://example.com",
    "selectors": {
        "headlines": "h1, h2",
        "main_content": "article.content",
        "navigation": "nav a"
    }
})
```

## ⚙️ Configuration

Configure through environment variables:

| Variable | Purpose | Default |
|----------|---------|---------|
| `REQUEST_TIMEOUT` | Webpage request timeout in seconds | 30 |

## 🧪 Testing

Run the test suite:

```bash
python -m pytest
```

## 📄 License

Released under the MIT License. See the LICENSE file for details.

---

Made with ❤️ by the Pear Labs Team

**Official site: ** [https://github.com/blazickjp/web-browser-mcp-server](https://github.com/blazickjp/web-browser-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `browser`
- Tags: `browser automation`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uv`
- Args: `tool run web-browser-mcp-server`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/blazickjp-web-browser.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
