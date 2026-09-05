---
title: "mcp-server-dify"
description: "Enables LLMs to interact with Dify AI's chat completion API, including conversation context support and a restaurant recommendation tool."
---

# mcp-server-dify

Enables LLMs to interact with Dify AI's chat completion API, including conversation context support and a restaurant recommendation tool.

# mcp-server-dify
[![CI Status](/mcp-assets/90f677fd1e0f984b06982d3cb0c83958.svg)](https://github.com/yuru-sha/mcp-server-dify/actions)

Model Context Protocol Server for Dify AI. This server enables LLMs to interact with Dify AI's chat completion capabilities through a standardized protocol.

## Features

- Integration with Dify AI chat completion API
- Restaurant recommendation tool (meshi-doko)
- Support for conversation context
- Streaming response support
- TypeScript implementation

## Installation

### Using Docker

```bash
# Build the Docker image
make docker

# Run with Docker
docker run -i --rm mcp/dify https://your-dify-api-endpoint your-dify-api-key
```

## Usage

### With Claude Desktop

Add the following configuration to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "dify": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-dify",
        "https://your-dify-api-endpoint",
        "your-dify-api-key"
      ]
    }
  }
}
```

Replace `your-dify-api-endpoint` and `your-dify-api-key` with your actual Dify API credentials.

### Tools

#### meshi-doko

Restaurant recommendation tool that interfaces with Dify AI:

Parameters:
- `LOCATION` (string): Location of the restaurant
- `BUDGET` (string): Budget constraints
- `query` (string): Query to send to Dify AI
- `conversation_id` (string, optional): For maintaining chat context

## Development

```bash
# Initial setup
make setup

# Build the project
make build

# Format code
make format

# Run linter
make lint
```

## License

This project is released under the [MIT License](https://github.com/yuru-sha/mcp-server-dify/blob/HEAD/LICENSE).

## Security

This server interacts with Dify AI using your provided API key. Ensure to:
- Keep your API credentials secure
- Use HTTPS for the API endpoint
- Never commit API keys to version control

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

**Official site: ** [https://github.com/yuru-sha/mcp-server-dify](https://github.com/yuru-sha/mcp-server-dify)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `search`
- Tags: `search`, `other`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @modelcontextprotocol/server-dify https://your-dify-api-endpoint your-dify-api-key`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/yuru-sha-dify.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
