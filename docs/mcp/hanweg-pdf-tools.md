---
title: "mcp-pdf-tools"
description: "mcp using PyPDF2 to: • merge-pdfs • extract-pages • search-pdfs • merge-pdfs-ordered (merge in user spec. order) • find-related-pdfs (regex extracted text for related PDF files)"
---

# mcp-pdf-tools

mcp using PyPDF2 to: • merge-pdfs • extract-pages • search-pdfs • merge-pdfs-ordered (merge in user spec. order) • find-related-pdfs (regex extracted text for related PDF files)

# WORK IN PROGRESS - USE WITH CAUTION - Windows:

# MCP PDF Tools Server

An MCP (Model Context Protocol) server that provides PDF manipulation tools. This server allows LLMs to perform operations like merging PDFs and extracting pages through the Model Context Protocol.

## Features

- Merge multiple PDF files into a single PDF
- Merge multiple PDF files into a single PDF in user specified order
- Extract specific pages from a PDF file
- Search PDFs *filesystem search or Everything search works better than this*
- Find (and merge) related PDFs based on text extraction and regex pattern matching from a target input PDF

## Installation

1. Clone this repository
2. 
```bash
cd mcp-pdf-tools

# Create and activate virtual environment
uv venv
.venvScriptsactivate

# Install the package
uv pip install -e .
```

## Usage with Claude Desktop

Add this to your Claude Desktop configuration file (claude_desktop_config.json):

```json
{
    "mcpServers": {
        "pdf-tools": {
            "command": "uv",
            "args": [
                "--directory",
                "PATH_TO\mcp-pdf-tools",
                "run",
                "pdf-tools"
            ]
        }
    }
}
```

**Official site: ** [https://github.com/hanweg/mcp-pdf-tools](https://github.com/hanweg/mcp-pdf-tools)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `productivity`
- Tags: `other`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uv`
- Args: `--directory PATH_TO\mcp-pdf-tools run pdf-tools`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/hanweg-pdf-tools.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
