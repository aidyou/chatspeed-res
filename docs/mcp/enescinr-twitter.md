---
title: "twitter-mcp"
description: "An MCP server that enables Claude to interact with Twitter, allowing for posting tweets and searching Twitter content."
---

# twitter-mcp

An MCP server that enables Claude to interact with Twitter, allowing for posting tweets and searching Twitter content.

# Twitter MCP Server

[Smithery](https://smithery.ai/server/@enescinar/twitter-mcp)

This MCP server allows Clients to interact with Twitter, enabling posting tweets and searching Twitter.

  

## Quick Start

1. Create a Twitter Developer account and get your API keys from [Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard)

2. Add this configuration to your Claude Desktop config file:

**Windows**: `%APPDATA%Claudeclaude_desktop_config.json`  
**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "twitter-mcp": {
      "command": "npx",
      "args": ["-y", "@enescinar/twitter-mcp"],
      "env": {
        "API_KEY": "your_api_key_here",
        "API_SECRET_KEY": "your_api_secret_key_here",
        "ACCESS_TOKEN": "your_access_token_here",
        "ACCESS_TOKEN_SECRET": "your_access_token_secret_here"
      }
    }
  }
}
```

3. Restart Claude Desktop

That's it! Claude can now interact with Twitter through two tools:

- `post_tweet`: Post a new tweet
- `search_tweets`: Search for tweets

## Example Usage

Try asking Claude:
- "Can you post a tweet saying 'Hello from Claude!'"
- "Can you search for tweets about Claude AI?"

## Troubleshooting

Logs can be found at:
- **Windows**: `%APPDATA%Claudelogsmcp-server-twitter.log`
- **macOS**: `~/Library/Logs/Claude/mcp-server-twitter.log`

## Development

If you want to contribute or run from source:

1. Clone the repository:
```bash
git clone https://github.com/EnesCinr/twitter-mcp.git
cd twitter-mcp
```

2. Install dependencies:
```bash
npm install
```

3. Build:
```bash
npm run build
```

4. Run:
```bash
npm start
```

## License

MIT

**Official site: ** [https://github.com/EnesCinr/twitter-mcp](https://github.com/EnesCinr/twitter-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `communication`
- Tags: `social media`, `communication`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @enescinar/twitter-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/enescinr-twitter.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
