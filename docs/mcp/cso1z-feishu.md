---
title: "Feishu-MCP"
description: "Provides access to Feishu (Lark) documents for AI-driven coding tools like Cursor, Windsurf, and Cline based on Model Context Protocol implementation."
---

# Feishu-MCP

Provides access to Feishu (Lark) documents for AI-driven coding tools like Cursor, Windsurf, and Cline based on Model Context Protocol implementation.

# Feishu MCP Server

Provides access to Feishu documents for [Cursor](https://cursor.sh/), [Windsurf](https://codeium.com/windsurf), [Cline](https://cline.bot/), and other AI-driven coding tools, implemented as a [Model Context Protocol](https://modelcontextprotocol.io/introduction) server.

When Cursor can access Feishu document data, it can understand and process document content more accurately and efficiently than other approaches (such as copy-pasting text).

## Core Features

### Document Management
- **Create Feishu documents**: supports creating new Feishu documents in a specified folder

### Document Content Operations
- **Get document info**:
  - Get basic document info (title, version, etc.)
  - Get the document block structure and hierarchy
  - Get detailed content of a specific block
- **Get document plain text**: supports extracting the full plain-text content of a document for analysis and processing
- **Edit document content**:
  - **Text block operations**:
    - Create and update rich-styled text blocks (bold, italic, underline, strikethrough, inline code)
    - Supports text color settings (gray, brown, orange, yellow, green, blue, purple)
    - Supports text alignment (left, center, right)
  - **Heading block operations**: create headings from level 1 to level 9
  - **Code block operations**:
    - Create code blocks in multiple programming languages
    - Supports code syntax highlighting
    - Supports automatic line wrapping
  - **List operations**:
    - Create ordered lists (numbered lists)
    - Create unordered lists (bullet lists)
  - **Batch content creation**: supports creating multiple content blocks of different types in a single operation

### Planned Features
- **Advanced content insertion**:
  - Table insertion: supports structured row/column data
  - Chart insertion: supports various data visualization charts
  - Flowchart insertion: supports flowcharts and mind maps
  - Formula insertion: supports math formulas and scientific symbols
- Content recognition and parsing for charts and flowcharts

Quick start, see the [Configuration](#configuration) section:

```bash
npx feishu-mcp --feishu-app-id= --feishu-app-secret=
```

## How It Works

1. Open the editor in Cursor's Agent mode.
2. Paste the Feishu document link.
3. Ask Cursor to perform operations based on the Feishu document - for example, analyze the document content or create related code.
4. Cursor will fetch the relevant metadata from Feishu and use it to help write code.

This MCP server is designed for Cursor. Before responding with content from the [Feishu API](https://open.feishu.cn/document/home/introduction-to-lark-open-platform/overview), it simplifies and transforms the response, ensuring only the most relevant document information is provided to the model.

## Installation

### Running the server quickly with NPM

You can run the server quickly with NPM without installing or building the repository:

```bash
npx feishu-mcp --feishu-app-id= --feishu-app-secret=

# or
pnpx feishu-mcp --feishu-app-id= --feishu-app-secret=

# or
yarn dlx feishu-mcp --feishu-app-id= --feishu-app-secret=

# or
bunx feishu-mcp --feishu-app-id= --feishu-app-secret=
```

**Published to the Smithery platform, available at: https://smithery.ai/server/@cso1z/feishu-mcp**

Instructions on creating a Feishu app and obtaining app credentials can be found [here](https://open.feishu.cn/document/home/develop-a-bot-in-5-minutes/create-an-app).

### JSON configuration for config-file-based tools

Many tools such as Windsurf, Cline, and [Claude Desktop](https://claude.ai/download) use config files to launch servers.

The `feishu-mcp` server can be configured by adding the following to your config file:

```json
{
  "mcpServers": {
    "feishu-mcp": {
      "command": "npx",
      "args": ["-y", "feishu-mcp", "--stdio"],
      "env": {
        "FEISHU_APP_ID": "",
        "FEISHU_APP_SECRET": ""
      }
    }
  }
}
```

### Running the server from local source

1. Clone the repository
2. Install dependencies with `pnpm install`
3. Copy `.env.example` to `.env` and fill in your [Feishu app credentials](https://open.feishu.cn/document/home/develop-a-bot-in-5-minutes/create-an-app).
4. Run the server with `pnpm run dev`, using any flags from the [command line arguments](#command-line-arguments) section.

## Configuration

The server can be configured via environment variables (through a `.env` file) or command line arguments. Command line arguments take precedence over environment variables.

### Environment variables

- `FEISHU_APP_ID`: your [Feishu app ID](https://open.feishu.cn/document/home/develop-a-bot-in-5-minutes/create-an-app) (required)
- `FEISHU_APP_SECRET`: your [Feishu app secret](https://open.feishu.cn/document/home/develop-a-bot-in-5-minutes/create-an-app) (required)
- `PORT`: the port the server runs on (default: 3333)

### Command line arguments

- `--version`: show the version number
- `--feishu-app-id`: your Feishu app ID
- `--feishu-app-secret`: your Feishu app secret
- `--port`: the port the server runs on
- `--stdio`: run the server in command mode instead of the default HTTP/SSE
- `--help`: show the help menu

## Connecting to Cursor

### Configuring Cursor

1. Open Cursor settings
2. Navigate to `Settings > AI > MCP Servers`
3. Add a new server with the URL `http://localhost:3333` (or your configured port)
4. Click "Verify Connection" to make sure the connection works

## Usage

1. In Cursor, open the AI panel (default shortcut `Cmd+K` or `Ctrl+K`)
2. To create a new Feishu document editing session, explicitly specify a folderToken; you can open a Feishu document folder such as: `https://vq5xxxxx7bc.feishu.cn/drive/folder/FPKvfjdxxxxx706RnOc`
2. To modify Feishu document content, clearly provide the document link, e.g.: `https://vq5ixxxx7bc.feishu.cn/docx/J6T0d6exxxxxxxDdc1zqwnph`
3. Ask questions about the document or request operations based on the document content
4. Creating and editing documents requires permissions; you can test with your account in the Feishu Open Platform: `https://open.feishu.cn/api-explorer/cli_a75a8ca0ac79100c?apiName=tenant_access_token_internal&from=op_doc&project=auth&resource=auth&version=v3`

## Document Permissions & Troubleshooting

### Permission types
There are two types of permissions: bot permissions and document access permissions

### Permission verification & troubleshooting
1. Get a token: [https://open.feishu.cn/api-explorer/cli_a7582508c93ad00d?apiName=tenant_access_token_internal&project=auth&resource=auth&version=v3](https://open.feishu.cn/api-explorer/cli_a7582508c93ad00d?apiName=tenant_access_token_internal&project=auth&resource=auth&version=v3)
2. Use the token from step 1 to verify whether you can access the document: [https://open.feishu.cn/api-explorer/cli_a7582508c93ad00d?apiName=get&project=docx&resource=document&version=v1](https://open.feishu.cn/api-explorer/cli_a7582508c93ad00d?apiName=get&project=docx&resource=document&version=v1)

### Troubleshooting methods
Test permissions in the Feishu Open Platform (when debugging in the Open Platform, failures come with sufficient prompts and guidance)

### Document authorization
If you encounter permission issues, refer to [Cloud docs FAQ](https://open.feishu.cn/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN), especially how to enable document permissions for an app or user.

## Cursor Best Practices

Add Rules to guide the model's workflow:

`When uploading documents to Feishu, follow these guidelines: 1. If no folderToken is specified, the default is FPKvf*********6RnOc. 2. If block creation fails, query all block information in the document to confirm whether the failure actually occurred. 3. To append information to an existing document, first get all block information for that document, then determine the content to insert and its index position based on the returned results. 4. Once all document content modifications are complete, provide the document link in the following format: https://vq5iay***bc.feishu.cn/docx/documentId. 5. When retrieving document information, prefer querying its plain-text content; if that is not sufficient, determine the content by querying all blocks`

## License

MIT

**Official site: ** [https://github.com/cso1z/feishu-mcp](https://github.com/cso1z/feishu-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `files`
- Tags: `note taking`, `file systems`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y feishu-mcp --stdio`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/cso1z-feishu.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
