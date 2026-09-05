---
title: "paper-search-mcp"
description: "Paper Search MCP"
---

# paper-search-mcp

Paper Search MCP

# Paper Search MCP

A Model Context Protocol (MCP) server for searching and downloading academic papers from multiple sources, including arXiv, PubMed, bioRxiv, and Sci-Hub (optional). Designed for seamless integration with large language models like Claude Desktop.

![PyPI](/mcp-assets/6267836e7841a13fc47a93760874d69a.svg) ![License](/mcp-assets/d177f30277cff66d9af1e3c6409e24dc.svg) ![Python](/mcp-assets/405b7b46d001e379991916d79670861b.svg)
[Smithery](https://smithery.ai/server/@openags/paper-search-mcp)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
  - [Quick Start](#quick-start)
    - [Install Package](#install-package)
    - [Configure Claude Desktop](#configure-claude-desktop)
  - [For Development](#for-development)
    - [Setup Environment](#setup-environment)
    - [Install Dependencies](#install-dependencies)
- [Contributing](#contributing)
- [Demo](#demo)
- [License](#license)
- [TODO](#todo)

---

## Overview

`paper-search-mcp` is a Python-based MCP server that enables users to search and download academic papers from various platforms. It provides tools for searching papers (e.g., `search_arxiv`) and downloading PDFs (e.g., `download_arxiv`), making it ideal for researchers and AI-driven workflows. Built with the MCP Python SDK, it integrates seamlessly with LLM clients like Claude Desktop.

---

## Features

- **Multi-Source Support**: Search and download papers from arXiv, PubMed, bioRxiv, and Sci-Hub (optional).
- **Standardized Output**: Papers are returned in a consistent dictionary format via the `Paper` class.
- **Asynchronous Tools**: Efficiently handles network requests using `httpx`.
- **MCP Integration**: Compatible with MCP clients for LLM context enhancement.
- **Extensible Design**: Easily add new academic platforms by extending the `academic_platforms` module.

---

## Installation

`paper-search-mcp` can be installed using `uv` or `pip`. Below are two approaches: a quick start for immediate use and a detailed setup for development.

### Installing via Smithery

To install paper-search-mcp for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@openags/paper-search-mcp):

```bash
npx -y @smithery/cli install @openags/paper-search-mcp --client claude
```

### Quick Start

For users who want to quickly run the server:

1. **Install Package**:
```bash
   uv add paper-search-mcp
```

2. **Configure Claude Desktop**:
   Add this configuration to `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac) or `%APPDATA%Claudeclaude_desktop_config.json` (Windows):
```json
   {
     "mcpServers": {
       "paper_search_server": {
         "command": "uv",
         "args": [
           "run",
           "--directory",
           "/path/to/your/paper-search-mcp",
           "-m",
           "paper_search_mcp.server"
         ]
       }
     }
   }
```
   > Note: Replace `/path/to/your/paper-search-mcp` with your actual installation path.

### For Development

For developers who want to modify the code or contribute:

1. **Setup Environment**:
```bash
   # Install uv if not installed
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Clone repository
   git clone https://github.com/openags/paper-search-mcp.git
   cd paper-search-mcp

   # Create and activate virtual environment
   uv venv
   source .venv/bin/activate  # On Windows: .venvScriptsactivate
```

2. **Install Dependencies**:
```bash
   # Install project in editable mode
   uv add -e .

   # Add development dependencies (optional)
   uv add pytest flake8
```
---

## Contributing

We welcome contributions! Here's how to get started:

1. **Fork the Repository**:
   Click "Fork" on GitHub.

2. **Clone and Set Up**:
```bash
   git clone https://github.com/yourusername/paper-search-mcp.git
   cd paper-search-mcp
   pip install -e ".[dev]"  # Install dev dependencies (if added to pyproject.toml)
```

3. **Make Changes**:
   - Add new platforms in `academic_platforms/`.
   - Update tests in `tests/`.

4. **Submit a Pull Request**:
   Push changes and create a PR on GitHub.

---

## Demo
 alt="Demo" width="800">

## TODO

### Planned Academic Platforms
- [√] arXiv
- [√] PubMed
- [√] bioRxiv
- [√] medRxiv
- [√] Google Scholar
- [ ] Semantic Scholar
- [ ] PubMed Central (PMC)
- [ ] Science Direct
- [ ] Springer Link
- [ ] IEEE Xplore
- [ ] ACM Digital Library
- [ ] Web of Science
- [ ] Scopus
- [ ] JSTOR
- [ ] ResearchGate
- [ ] CORE
- [ ] Microsoft Academic

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Happy researching with `paper-search-mcp`! If you encounter issues, open a GitHub issue.

**Official site: ** [https://github.com/openags/paper-search-mcp](https://github.com/openags/paper-search-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `search`
- Tags: `search`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uv`
- Args: `run --directory /path/to/your/paper-search-mcp -m paper_search_mcp.server`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/openags-paper-search.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
