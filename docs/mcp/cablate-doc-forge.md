---
title: "mcp-doc-forge"
description: "Provides comprehensive document processing, including reading, converting, and manipulating various document formats with advanced text and HTML processing capabilities."
---

# mcp-doc-forge

Provides comprehensive document processing, including reading, converting, and manipulating various document formats with advanced text and HTML processing capabilities.

# Simple Document Processing MCP Server
[Smithery](https://smithery.ai/server/@cablate/mcp-doc-forge)

A powerful Model Context Protocol (MCP) server providing comprehensive document processing capabilities.

## Features

### Document Reader
- Read DOCX, PDF, TXT, HTML, CSV

### Document Conversion
- DOCX to HTML/PDF conversion
- HTML to TXT/Markdown conversion
- PDF manipulation (merge, split)

### Text Processing
- Multi-encoding transfer support (UTF-8, Big5, GBK)
- Text formatting and cleaning
- Text comparison and diff generation
- Text splitting by lines or delimiter

### HTML Processing
- HTML cleaning and formatting
- Resource extraction (images, links, videos)
- Structure-preserving conversion

## Installation

### Installing via Smithery

To install Document Processing Server for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@cablate/mcp-doc-forge):

```bash
npx -y @smithery/cli install @cablate/mcp-doc-forge --client claude
```

### Manual Installation
```bash
npm install -g @cablate/mcp-doc-forge
```

## Usage

### Cli

```bash
mcp-doc-forge
```

### With [Dive Desktop](https://github.com/OpenAgentPlatform/Dive)

1. Click "+ Add MCP Server" in Dive Desktop
2. Copy and paste this configuration:

```json
{
  "mcpServers": {
    "searxng": {
      "command": "npx",
      "args": [
        "-y",
        "@cablate/mcp-doc-forge"
      ],
      "enabled": true
    }
  }
}
```

3. Click "Save" to install the MCP server

## License

MIT

## Contributing

Welcome community participation and contributions! Here are ways to contribute:

- ⭐️ Star the project if you find it helpful
- 🐛 Submit Issues: Report problems or provide suggestions
- 🔧 Create Pull Requests: Submit code improvements

## Contact

If you have any questions or suggestions, feel free to reach out:

- 📧 Email: [reahtuoo310109@gmail.com](mailto:reahtuoo310109@gmail.com)
- 📧 GitHub: [CabLate](https://github.com/cablate/)
- 🤝 Collaboration: Welcome to discuss project cooperation
- 📚 Technical Guidance: Sincere welcome for suggestions and guidance

**Official site: ** [https://github.com/cablate/mcp-doc-forge](https://github.com/cablate/mcp-doc-forge)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `productivity`
- Tags: `other`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @cablate/mcp-doc-forge`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/cablate-doc-forge.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
