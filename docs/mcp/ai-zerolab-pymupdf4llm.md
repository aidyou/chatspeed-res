---
title: "pymupdf4llm-mcp"
description: "An MCP server that exports PDF documents to markdown format optimized for LLM processing."
---

# pymupdf4llm-mcp

An MCP server that exports PDF documents to markdown format optimized for LLM processing.

# pymupdf4llm-mcp

[![Release](/mcp-assets/b95d01c9e536e0b145783f66c5b61a56.svg)](https://img.shields.io/github/v/release/ai-zerolab/pymupdf4llm-mcp)
[![Build status](/mcp-assets/315ded2d2e09548d7e64cb1ec1bd0c55.svg)](https://github.com/ai-zerolab/pymupdf4llm-mcp/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](/mcp-assets/41152979705a66ad9c096b25277fbfe9.svg)](https://codecov.io/gh/ai-zerolab/pymupdf4llm-mcp)
[![Commit activity](/mcp-assets/40f4dbd4ced8845c945315127dbf74d8.svg)](https://img.shields.io/github/commit-activity/m/ai-zerolab/pymupdf4llm-mcp)
[![License](/mcp-assets/3558c36785ba77f4575ce643a3a48f2a.svg)](https://img.shields.io/github/license/ai-zerolab/pymupdf4llm-mcp)

MCP Server for pymupdf4llm, best for export PDF to markdown for LLM.

- **Github repository**: 
- **Documentation** 

## Quick Start

Run the following command to run the MCP server:

```bash
uvx pymupdf4llm-mcp@latest stdio # stdio mode
# or
uvx pymupdf4llm-mcp@latest sse # sse mode
```

Configure your cursor/windsurf/... and other MCP client to this server:

```json
{
  "mcpServers": {
    "pymupdf4llm-mcp": {
      "command": "uvx",
      "args": [
        "pymupdf4llm-mcp@latest",
        "stdio"
      ],
      "env": {}
    }
  }
}
```

**Official site: ** [https://github.com/ai-zerolab/pymupdf4llm-mcp](https://github.com/ai-zerolab/pymupdf4llm-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `files`
- Tags: `file systems`, `other`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `pymupdf4llm-mcp@latest stdio`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/ai-zerolab-pymupdf4llm.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
