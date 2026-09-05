---
title: "mcp-google-calendar"
description: "Integrates Google Calendar with AI assistants through the Model Context Protocol, allowing users to view and manage calendar events through natural language interaction."
---

# mcp-google-calendar

Integrates Google Calendar with AI assistants through the Model Context Protocol, allowing users to view and manage calendar events through natural language interaction.

# Google Calendar MCP Server

A Model Context Protocol (MCP) server that integrates with Google Calendar, built with TypeScript.

## Features

- Seamless Google Calendar integration with OAuth 2.0 authentication
- Persistent token storage for automatic authentication
- List and manage calendars with comprehensive event operations
- Create, read, update, and delete calendar events
- Fetch calendar events between specified dates
- Server-Sent Events (SSE) transport option for real-time updates
- Simple integration with Claude and other MCP-compatible AI assistants

## Installation

```bash
npm install -g mcp-google-calendar
```

Or run directly with:

```bash
npx -y mcp-google-calendar
```

## Prerequisites

1. Node.js (v16 or higher)
2. Google Cloud Platform account
3. Google Calendar API enabled
4. OAuth 2.0 credentials

## Setup

### 1. Google Cloud Configuration

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Google Calendar API:
   - Navigate to "APIs & Services" > "Library"
   - Search for "Google Calendar API"
   - Click "Enable"
4. Configure OAuth consent screen:
   - Go to "APIs & Services" > "OAuth consent screen"
   - Choose "External" user type (or "Internal" for Google Workspace)
   - Fill in required information:
     - App name: mcp-calendar
     - User support email: (your email)
     - Developer contact information: (your email)
   - Add scopes:
     - Click "Add or Remove Scopes"
     - Find and select "https://www.googleapis.com/auth/calendar.events"
     - Add your email as a test user
   - Complete the setup
5. Create OAuth credentials:
   - Go to "Credentials"
   - Click "Create Credentials" > "OAuth Client ID"
   - Choose "Desktop app" as application type
   - Name it (e.g., "MCP Calendar Desktop Client")
   - Download the JSON file and save as `credentials.json` in your project directory

### 2. Environment Configuration

Create a `.env` file in your project root:

```
# Server configuration
PORT=3420

# Google Calendar API configuration
CREDENTIALS_PATH=./credentials.json
```

## Usage

### Starting the Server

Start with standard WebSockets:
```bash
npx -y mcp-google-calendar
```

Start with Server-Sent Events (SSE):
```bash
npx -y mcp-google-calendar --sse
```

### With Claude Desktop

Add this to your `claude_desktop_config.json`:
```json
{
   "mcpServers": {
      "mcp-google-calendar": {
         "command": "npx",
         "args": ["-y", "mcp-google-calendar"],
         "env": {
            "CREDENTIALS_PATH": "/path/to/your/credentials.json"
         }
      }
   }
}
```

### Authentication Process

The first time you run the server:
1. A browser window will open automatically
2. Sign in with your Google account
3. Grant the requested calendar permissions
4. The authentication token is saved to `token.json`

On subsequent launches:
- The server uses the saved token automatically
- No browser interaction is required unless the token expires

## Available Tools

| Tool | Description |
|------|-------------|
| `list_calendars` | Get all available calendars |
| `list_calendar_events` | Retrieve events between specified dates |
| `create_calendar_event` | Add a new event to your calendar |
| `get_calendar_event` | Fetch details for a specific event |
| `edit_calendar_event` | Modify an existing calendar event |
| `delete_calendar_event` | Remove an event from your calendar |

## Development

Clone and set up the project:
```bash
git clone https://github.com/am2rican5/mcp-google-calendar.git
cd mcp-google-calendar
npm install
```

Build the project:
```bash
npm run build
```

Run in development mode:
```bash
npm start
```

## Security Considerations

⚠️ **Important Security Warning** ⚠️

- `credentials.json` and `token.json` contain sensitive authentication information
- Never commit these files to version control or share them publicly
- Each user should create their own OAuth credentials
- If you suspect credential compromise, revoke them immediately in Google Cloud Console
- The token grants access to your Google Calendar data

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/am2rican5/mcp-google-calendar/blob/HEAD/LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

**Official site: ** [https://github.com/am2rican5/mcp-google-calendar](https://github.com/am2rican5/mcp-google-calendar)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `productivity`
- Tags: `calendar management`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y mcp-google-calendar`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/am2rican5-google-calendar.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
