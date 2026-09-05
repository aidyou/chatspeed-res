---
title: "mcp-google-gmail"
description: "Provides comprehensive Gmail integration with LLM processing capabilities, allowing users to read, search, filter emails and handle attachments through the Model Context Protocol."
---

# mcp-google-gmail

Provides comprehensive Gmail integration with LLM processing capabilities, allowing users to read, search, filter emails and handle attachments through the Model Context Protocol.

# Gmail MCP Server

A powerful Model Context Protocol (MCP) server providing comprehensive Gmail integration with LLM processing capabilities.

## Features

### Email Management

- Read and search emails
- Process email content with various formats
- Advanced email filtering
- Attachment handling

## Demo on Dive Desktop

## Installation

### Manual Installation

```bash
npm install -g @cablate/mcp-gmail
```

## Usage

### CLI

```bash
map-gmail
```

### With [Dive Desktop](https://github.com/OpenAgentPlatform/Dive)

1. Click "+ Add MCP Server" in Dive Desktop
2. Copy and paste this configuration:

```json
{
  "mcpServers": {
    "gmail": {
      "command": "npx",
      "args": ["-y", "@cablate/mcp-gmail"],
      "env": {
        "GMAIL_CLIENT_ID": "your_client_id",
        "GMAIL_CLIENT_SECRET": "your_client_secret",
        "GMAIL_REFRESH_TOKEN": "your_refresh_token"
      },
      "enabled": true
    }
  }
}
```

3. Click "Save" to install the MCP server

## Gmail API Authentication Setup

For detailed instructions on setting up Gmail API authentication and obtaining necessary credentials, please refer to our [Gmail API Setup Guide](https://github.com/cablate/mcp-google-gmail/blob/HEAD/guide.md).

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

**Official site: ** [https://github.com/cablate/mcp-google-gmail](https://github.com/cablate/mcp-google-gmail)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `communication`
- Tags: `communication`, `search`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @cablate/mcp-gmail`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/cablate-google-gmail.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
