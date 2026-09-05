---
title: "mcp-google-calendar"
description: "Enables comprehensive calendar management with capabilities to create, list, update, and delete events through a Model Context Protocol server integrated with Google Calendar."
---

# mcp-google-calendar

Enables comprehensive calendar management with capabilities to create, list, update, and delete events through a Model Context Protocol server integrated with Google Calendar.

# Calendar Tools MCP Server

A powerful Model Context Protocol (MCP) server providing comprehensive calendar management capabilities.

## Features

### Calendar Management

- Create calendar events
- List calendar events
- Update existing events
- Delete events

## Demo on Dive Desktop

## Installation

### Manual Installation

```bash
npm install -g @cablate/mcp-google-calendar
```

## Usage

### Cli

```bash
mcp-google-calendar
```

### With [Dive Desktop](https://github.com/OpenAgentPlatform/Dive)

1. Click "+ Add MCP Server" in Dive Desktop
2. Copy and paste this configuration:

```json
{
  "mcpServers": {
    "calendar": {
      "command": "npx",
      "args": ["-y", "@cablate/mcp-google-calendar"],
      "env": {
        "GOOGLE_CALENDAR_ID": "your_calendar_id",
        "GOOGLE_TIME_ZONE": "your_time_zone",
        "GOOGLE_CREDENTIALS_PATH": "your_credentials_path"
      },
      "enabled": true
    }
  }
}
```

3. Click "Save" to install the MCP server

## Google Service Account and Credentials

Here is the simple steps to create a google service account and credentials:

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing project
3. Navigate to the "IAM & Admin" section
4. Click on "Service Accounts"
5. Click on "Create Service Account"
6. Enter a name for the service account (e.g., "MCP Google Calendar")
7. Click on "Create"
8. Click on "Create Key"
9. Select "JSON" as the key type
10. Click on "Create"
11. Download the JSON file and save it as `credentials.json`

if still got any question, google and find the answer.

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

**Official site: ** [https://github.com/cablate/mcp-google-calendar](https://github.com/cablate/mcp-google-calendar)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `productivity`
- Tags: `calendar management`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @cablate/mcp-google-calendar`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/cablate-google-calendar.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
