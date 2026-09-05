---
title: "ms-365-mcp-server"
description: "A Model Context Protocol server that enables interaction with Microsoft 365 services (Excel, Calendar, Mail, OneDrive, Teams, etc.) through the Graph API, allowing AI assistants to manage Microsoft 36…"
---

# ms-365-mcp-server

A Model Context Protocol server that enables interaction with Microsoft 365 services (Excel, Calendar, Mail, OneDrive, Teams, etc.) through the Graph API, allowing AI assistants to manage Microsoft 36…

# ms-365-mcp-server

![npm version](/mcp-assets/a31704b4715177030b77326640272691.svg) ![build status](/mcp-assets/a360cf14c31b446d557b2bc79fbedc72.svg) ![license](/mcp-assets/d177f30277cff66d9af1e3c6409e24dc.svg)

Microsoft 365 MCP Server

A Model Context Protocol (MCP) server for interacting with Microsoft 365 services through the Graph API.

## Prerequisites

- Node.js >= 14

## Features

- Authentication via Microsoft Authentication Library (MSAL)
- Excel file operations
- Calendar event management
- Mail operations
- OneDrive file management
- OneNote notebooks and pages
- To Do tasks and task lists
- Planner plans and tasks
- Outlook contacts
- User management
- Dynamic tools powered by Microsoft Graph OpenAPI spec
- Built on the Model Context Protocol

## Quick Start Example

Test login in Claude Desktop:

## Examples

## Integration

### Claude Desktop

To add this MCP server to Claude Desktop:

Edit the config file under Settings > Developer:

```json
{
  "mcpServers": {
    "ms365": {
      "command": "npx",
      "args": [
        "-y",
        "@softeria/ms-365-mcp-server"
      ]
    }
  }
}
```

### Claude Code CLI

```bash
claude mcp add ms365 -- npx -y @softeria/ms-365-mcp-server
```

For other interfaces that support MCPs, please refer to their respective documentation for the correct
integration method.

### Authentication

> ⚠️ You must authenticate before using tools.

1. **MCP client login**:
    - Call the `login` tool (auto-checks existing token)
    - If needed, get URL+code, visit in browser
    - Use `verify-login` tool to confirm
2. **Optional CLI login**:
```bash
   npx @softeria/ms-365-mcp-server --login
```
   Follow the URL and code prompt in the terminal.

Tokens are cached securely in your OS credential store (fallback to file).

## License

MIT © 2025 Softeria

**Official site: ** [https://github.com/softeria/ms-365-mcp-server](https://github.com/softeria/ms-365-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `productivity`
- Tags: `app automation`, `cloud platforms`, `calendar management`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @softeria/ms-365-mcp-server`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/softeria-ms-365.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
