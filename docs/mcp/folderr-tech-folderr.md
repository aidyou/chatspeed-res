---
title: "folderr-mcp-server"
description: "A Model Context Protocol (MCP) server that provides tools to interact with Folderr's API, specifically for managing and communicating with Folderr Assistants."
---

# folderr-mcp-server

A Model Context Protocol (MCP) server that provides tools to interact with Folderr's API, specifically for managing and communicating with Folderr Assistants.

# Folderr MCP Server

A Model Context Protocol (MCP) server that provides tools to interact with Folderr's API, specifically for managing and communicating with Folderr Assistants.

## Installation

Add to your MCP Settings

```
{
  "mcpServers": {
    "folderr": {
      "command": "npx",
      "args": ["-y", "@folderr/folderr-mcp-server"]
    }
  }
}
```

## Features

The server provides the following tools:

### Authentication

Two methods of authentication are supported:

1. **Login with Email/Password**
```typescript
   {
     "name": "login",
     "arguments": {
       "email": "user@example.com",
       "password": "your-password"
     }
   }
```

2. **API Token Authentication**
```typescript
   {
     "name": "set_api_token",
     "arguments": {
       "token": "your-api-token"
     }
   }
```
   API tokens can be generated from the Folderr developers section. This method is recommended for automated or long-running processes.

### Assistant Management

1. **List Assistants**
```typescript
   {
     "name": "list_assistants",
     "arguments": {}
   }
```
   Returns a list of all available assistants for the authenticated user.

2. **Ask Assistant**
```typescript
   {
     "name": "ask_assistant",
     "arguments": {
       "assistant_id": "assistant-id",
       "question": "Your question here"
     }
   }
```
   Send a question to a specific assistant and receive their response.

## Configuration

The server stores its configuration in a `config.json` file, which includes:
- Base URL for the Folderr API
- Authentication token (from login or API key)

## Error Handling

The server provides detailed error messages for common scenarios:
- Authentication failures
- Invalid requests
- API errors
- Network issues

## Development

To build the server:
```bash
npm install
npm run build
```

## Usage in MCP Settings

Add the following to your MCP settings configuration:
```json
{
  "mcpServers": {
    "folderr": {
      "command": "node",
      "args": ["/path/to/folderr-server/build/index.js"]
    }
  }
}
```

## Authentication Flow

1. Either:
   - Use the `login` tool with email and password
   - Use the `set_api_token` tool with an API token from Folderr's developers section
2. The authentication token is automatically saved and used for subsequent requests
3. All assistant-related tools require authentication before use

## Error Messages

Common error messages and their meanings:
- "Not logged in": No authentication token is set
- "Login failed": Invalid credentials
- "Failed to list assistants": Error retrieving assistant list
- "Failed to ask assistant": Error sending question to assistant

**Official site: ** [https://github.com/folderr-tech/folderr-mcp-server](https://github.com/folderr-tech/folderr-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `communication`
- Tags: `communication`, `developer tools`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @folderr/folderr-mcp-server`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/folderr-tech-folderr.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
