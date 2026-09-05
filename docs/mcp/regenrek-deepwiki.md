---
title: "mcp-deepwiki"
description: "📖 MCP Server is used to fetch the latest knowledge from deepwiki.com and utilize it in Cursor and other code editors."
---

# mcp-deepwiki

📖 MCP Server is used to fetch the latest knowledge from deepwiki.com and utilize it in Cursor and other code editors.

# Deepwiki MCP Server

This is an **unofficial Deepwiki MCP server**.

It receives a Deepwiki URL via MCP, scrapes all related pages, converts them to Markdown format, and returns a document or a list of pages.

## Features

- 🔒 **Domain Security**: Only handles URLs from deepwiki.org
- 🧹 **HTML Cleanup**: Removes headers, footers, navigation, scripts, and ads
- 🔗 **Link Rewriting**: Adjusts links to work in Markdown
- 📄 **Multiple Output Formats**: Get a single document or structured pages
- 🚀 **Performance**: Fast scraping with adjustable concurrency and depth
- **NLP**: Used only for library name search

## Usage

Prompts you can use:

```

deepwiki fetch how can i use gpt-image-1 with "vercel ai" sdk

deepwiki fetch how can i create new blocks in shadcn?

deepwiki fetch i want to understand how X works

```
Get the full document (default)

```

use deepwiki https://deepwiki.org/shadcn-ui/ui

use deepwiki multiple pages https://deepwiki.org/shadcn-ui/ui

```
Single page

```

use deepwiki fetch single page https://deepwiki.org/tailwindlabs/tailwindcss/2.2-theme-system

```
Use short form to get

```

use deepwiki fetch tailwindlabs/tailwindcss

deepwiki fetch library

deepwiki fetch url

deepwiki fetch /

deepwiki multiple pages ...

deepwiki single page url ...

```
## Cursor

Add the following to your `.cursor/mcp.json` file.

```json

{

  "mcpServers": {

    "mcp-deepwiki": {

      "command": "npx",

      "args": [

        "-y",

        "mcp-deepwiki@latest"

      ]

    }

  }

}

```

### MCP Tool Integration

This package registers a tool named `deepwiki_fetch` that you can use in any MCP-compatible client:

```json

{

  "action": "deepwiki_fetch",

  "params": {

    "url": "https://deepwiki.org/user/repo",

    "mode": "aggregate",

    "maxDepth": "1"

  }

}

```
#### Parameters

- `url` (required): The starting URL of the Deepwiki repository
- `mode` (optional): Output mode, can be "aggregate" for a single Markdown document (default), or "pages" for structured page data
- `maxDepth` (optional): Maximum page depth to scrape (default: 10)

### Response Format

#### Successful Response (Aggregate Mode)

```json

{

  "status": "ok",

  "data": "# Page title

Page content...

---

# Another page

More content...",

  "totalPages": 5,

  "totalBytes": 25000,

  "elapsedMs": 1200

}

```
#### Successful Response (Pages Mode)

```json

{

  "status": "ok",

  "data": [

    {

      "path": "index",

      "markdown": "# Home

Welcome to the repository."

    },

    {

      "path": "section/page1",

      "markdown": "# Page 1

This is the content of page 1."

    }

  ],

  "totalPages": 2,

  "totalBytes": 12000,

  "elapsedMs": 800

}

```
#### Error Response

```json

{

  "status": "error",

  "code": "DOMAIN_NOT_ALLOWED",

  "message": "Only deepwiki.org domains are allowed"

}

```
#### Partial Success Response

```json

{

  "status": "partial",

  "data": "# Page title

Page content...",

  "errors": [

    {

      "url": "https://deepwiki.org/user/repo/page2",

      "reason": "HTTP error: 404"

    }

  ],

  "totalPages": 1,

  "totalBytes": 5000,

  "elapsedMs": 950

}

```
### Progress Events

While using the tool, you will receive progress events during the scraping process:

Fetched https://deepwiki.org/user/repo: 12500 bytes in 450ms (status: 200)
Fetched https://deepwiki.org/user/repo/page1: 8750 bytes in 320ms (status: 200)
Fetched https://deepwiki.org/user/repo/page2: 6200 bytes in 280ms (status: 200)

## Local Development - Installation

### Local Use

```json

{

  "mcpServers": {

    "mcp-deepwiki": {

      "command": "node",

      "args": [

        "./bin/cli.mjs"

      ]

    }

  }

}

```
### Install from Source

```bash

# Clone the repository

git clone https://github.com/regenrek/mcp-deepwiki.git

cd mcp-deepwiki

# Install dependencies

npm install

# Build the package

npm run build

```
#### Direct API Call

For HTTP transport, you can make a direct API call:

```bash

curl -X POST http://localhost:3000/mcp 

-H "Content-Type: application/json" 

-d '{

"id": "req-1",

"action": "deepwiki_fetch",

"params": {

"url": "https://deepwiki.org/user/repo",

"mode": "aggregate"

}

}'

```
## Configuration

### Environment Variables

- `DEEPWIKI_MAX_CONCURRENCY`: Maximum number of concurrent requests (default: 5)
- `DEEPWIKI_REQUEST_TIMEOUT`: Request timeout in milliseconds (default: 30000)
- `DEEPWIKI_MAX_RETRIES`: Maximum number of retries for failed requests (default: 3)
- `DEEPWIKI_RETRY_DELAY`: Base delay for retry backoff in milliseconds (default: 250)

To configure these environment variables, create a `.env` file in the root of the project:

DEEPWIKI_MAX_CONCURRENCY=10
DEEPWIKI_REQUEST_TIMEOUT=60000
DEEPWIKI_MAX_RETRIES=5
DEEPWIKI_RETRY_DELAY=500

## Docker Deployment (Untested)

Build and run the Docker image:

```bash

# Build the image

docker build -t mcp-deepwiki .

# Run with stdio transport (for development)

docker run -it --rm mcp-deepwiki

# Run with HTTP transport (for production)

docker run -d -p 3000:3000 mcp-deepwiki --http --port 3000

# Run with environment variables

docker run -d -p 3000:3000 

-e DEEPWIKI_MAX_CONCURRENCY=10 

-e DEEPWIKI_REQUEST_TIMEOUT=60000 

mcp-deepwiki --http --port 3000

```
## Development

```bash

# Install dependencies

pnpm install

# Run in development mode with stdio

pnpm run dev-stdio

# Run tests

pnpm test

# Run lint

pnpm run lint

# Build the package

pnpm run build

```
## Troubleshooting

### Common Issues

1. **Permission Denied**: If you encounter an EACCES error when running the CLI, ensure the binary is executable:
   bash
   chmod +x ./node_modules/.bin/mcp-deepwiki
   

2. **Connection Refused**: Ensure the port is available and not blocked by a firewall:
   bash
   # Check if the port is in use
   lsof -i :3000
   

3. **Timeout Errors**: For large repositories, consider increasing the timeout and concurrency:
   bash
   DEEPWIKI_REQUEST_TIMEOUT=60000 DEEPWIKI_MAX_CONCURRENCY=10 npx mcp-deepwiki
   

## Contributing

We welcome contributions! See [CONTRIBUTING.md](https://github.com/regenrek/deepwiki-mcp/blob/HEAD/CONTRIBUTING.md) for details.

## License

MIT

## Links

- X/Twitter: [@kregenrek](https://x.com/kregenrek)
- Bluesky: [@kevinkern.dev](https://bsky.app/profile/kevinkern.dev)

## Courses

- Learn Cursor AI: [Ultimate Cursor Course](https://www.instructa.ai/en/cursor-ai)
- Learn to Build Software with AI: [instructa.ai](https://www.instructa.ai)

## Check Out My Other Projects:

* [AI Prompts](https://github.com/instructa/ai-prompts/blob/main/README.md) - Curated AI prompts for Cursor AI, Cline, Windsurf, and Github Copilot
* [codefetch](https://github.com/regenrek/codefetch) - Convert code to Markdown format with a simple terminal command, making it easy for LLMs to use* [aidex](https://github.com/regenrek/aidex) - A CLI tool that provides detailed information about AI language models, helping developers choose the right model for their needs.

**Official site: ** [https://github.com/regenrek/deepwiki-mcp](https://github.com/regenrek/deepwiki-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `search`, `memory`, `data`
- Tags: `search`, `knowledge and memory`, `research and data`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y mcp-deepwiki@latest`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/regenrek-deepwiki.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
