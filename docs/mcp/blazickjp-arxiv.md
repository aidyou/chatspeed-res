---
title: "arxiv-mcp-server"
description: "The ArXiv MCP Server bridges the gap between AI models and academic research by providing a sophisticated interface to arXiv's extensive research repository. This server enables AI assistants to perfo…"
---

# arxiv-mcp-server

The ArXiv MCP Server bridges the gap between AI models and academic research by providing a sophisticated interface to arXiv's extensive research repository. This server enables AI assistants to perfo…

[![Twitter Follow](/mcp-assets/3e82fabdd3d7f3c8bffecf68b940346e.svg)](https://twitter.com/JoeBlazick)
[Smithery](https://smithery.ai/server/arxiv-mcp-server)
[![Python Version](/mcp-assets/4f6146f128339189f0d4b97607879041.svg)](https://www.python.org/downloads/)
[![Tests](/mcp-assets/5bb2427016803e209dad2b0fd1539cd3.svg)](https://github.com/blazickjp/arxiv-mcp-server/actions/workflows/tests.yml)
[![License: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://opensource.org/licenses/MIT)
[![PyPI Downloads](/mcp-assets/b34bb44d64ff71c74ae1877588884af5.svg)](https://pypi.org/project/arxiv-mcp-server/)
[![PyPI Version](/mcp-assets/d8e739c53aee35cbca3756a05279530b.svg)](https://pypi.org/project/arxiv-mcp-server/)

# ArXiv MCP Server

> 🔍 Enable AI assistants to search and access arXiv papers through a simple MCP interface.

The ArXiv MCP Server provides a bridge between AI assistants and arXiv's research repository through the Message Control Protocol (MCP). It allows AI models to search for papers and access their content in a programmatic way.

  
🤝 **[Contribute](https://github.com/blazickjp/arxiv-mcp-server/blob/main/CONTRIBUTING.md)** • 
📝 **[Report Bug](https://github.com/blazickjp/arxiv-mcp-server/issues)**

## ✨ Core Features

- 🔎 **Paper Search**: Query arXiv papers with filters for date ranges and categories
- 📄 **Paper Access**: Download and read paper content
- 📋 **Paper Listing**: View all downloaded papers
- 🗃️ **Local Storage**: Papers are saved locally for faster access
- 📝 **Prompts**: A Set of Research Prompts

## 🚀 Quick Start

### Installing via Smithery

To install ArXiv Server for Claude Desktop automatically via [Smithery](https://smithery.ai/server/arxiv-mcp-server):

```bash
npx -y @smithery/cli install arxiv-mcp-server --client claude
```

### Installing Manually
Install using uv:

```bash
uv tool install arxiv-mcp-server
```

For development:

```bash
# Clone and set up development environment
git clone https://github.com/blazickjp/arxiv-mcp-server.git
cd arxiv-mcp-server

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
        "arxiv-mcp-server": {
            "command": "uv",
            "args": [
                "tool",
                "run",
                "arxiv-mcp-server",
                "--storage-path", "/path/to/paper/storage"
            ]
        }
    }
}
```

For Development:

```json
{
    "mcpServers": {
        "arxiv-mcp-server": {
            "command": "uv",
            "args": [
                "--directory",
                "path/to/cloned/arxiv-mcp-server",
                "run",
                "arxiv-mcp-server",
                "--storage-path", "/path/to/paper/storage"
            ]
        }
    }
}
```

## 💡 Available Tools

The server provides four main tools:

### 1. Paper Search
Search for papers with optional filters:

```python
result = await call_tool("search_papers", {
    "query": "transformer architecture",
    "max_results": 10,
    "date_from": "2023-01-01",
    "categories": ["cs.AI", "cs.LG"]
})
```

### 2. Paper Download
Download a paper by its arXiv ID:

```python
result = await call_tool("download_paper", {
    "paper_id": "2401.12345"
})
```

### 3. List Papers
View all downloaded papers:

```python
result = await call_tool("list_papers", {})
```

### 4. Read Paper
Access the content of a downloaded paper:

```python
result = await call_tool("read_paper", {
    "paper_id": "2401.12345"
})
```

## 📝 Research Prompts

The server offers specialized prompts to help analyze academic papers:

### Paper Analysis Prompt
A comprehensive workflow for analyzing academic papers that only requires a paper ID:

```python
result = await call_prompt("deep-paper-analysis", {
    "paper_id": "2401.12345"
})
```

This prompt includes:
- Detailed instructions for using available tools (list_papers, download_paper, read_paper, search_papers)
- A systematic workflow for paper analysis
- Comprehensive analysis structure covering:
  - Executive summary
  - Research context
  - Methodology analysis
  - Results evaluation
  - Practical and theoretical implications
  - Future research directions
  - Broader impacts

## ⚙️ Configuration

Configure through environment variables:

| Variable | Purpose | Default |
|----------|---------|---------|
| `ARXIV_STORAGE_PATH` | Paper storage location | ~/.arxiv-mcp-server/papers |

## 🧪 Testing

Run the test suite:

```bash
python -m pytest
```

## 📄 License

Released under the MIT License. See the LICENSE file for details.

---

Made with ❤️ by the Pearl Labs Team

**Official site: ** [https://github.com/blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `search`, `data`
- Tags: `research and data`, `search`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uv`
- Args: `tool run arxiv-mcp-server --storage-path /path/to/paper/storage`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/blazickjp-arxiv.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
