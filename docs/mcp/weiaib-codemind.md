---
title: "CodeMind-MCP"
description: "An MCP (Model Context Protocol) server that helps users quickly understand code repositories and generate mind maps through automated workflows. It includes managing repositories, pull requests, issue…"
---

# CodeMind-MCP

An MCP (Model Context Protocol) server that helps users quickly understand code repositories and generate mind maps through automated workflows. It includes managing repositories, pull requests, issue…

# CodeMind MCP

An MCP (Model Context Protocol) server that helps users quickly understand code repositories and generate mind maps through automated workflows.

## Background
Do you keep forgetting git commands?
- This MCP can be used to manage repositories, pull requests, issues, etc.

**Do you find a project hard to understand?**
- **This MCP acts as a professional architect to help you quickly understand the code repository and generate a mind map.**

## Core Features

1. **`gitcode_request`**: a general GitCode API call tool for managing repositories, pull requests, issues, etc.
2. **`mindmap`**: reads all README.md files in the current directory and its subdirectories to generate a mind map:
   * Recursively finds and collects all README.md files
   * Merges the file contents and calls the Coze workflow to generate a mind map
   * Returns a publicly accessible mind map link

## Installation and Usage

**Requirements**: Node.js >= 18.x

### Global installation
```bash
npm install -g @lucianaib/codemind-mcp
codemind-mcp
```

### Configure in the MCP client
```json
{
  "mcpServers": {
    "CodeMind": {
      "command": "npx",
      "args": ["@lucianaib/codemind-mcp"]
    }
  }
}
```

## Tool Call Parameters

### `gitcode_request`
- **baseUrl**: string (optional), e.g. `https://api.gitcode.com`
- **token**: string, auth token (supports `Bearer ` or a plain token)
- **method**: "GET" | "POST" | "PUT" | "PATCH" | "DELETE"
- **path**: string, e.g. `/v1/repos`
- **query**: Record (optional)
- **body**: Record (optional)
- **headers**: Record (optional)

### `mindmap`
- **prompt**: string (optional), a custom prompt for generating the mind map

## Development and Code Structure

- `src/index.ts`: MCP server entry, registers tools with `McpServer`
- `src/gitcode.ts`: general request wrapper for the GitCode API
- `src/mindmap.ts`: core logic for collecting README.md files and calling the Coze API

## Security Note

**Important**: the Coze API credentials are currently hardcoded in `src/mindmap.ts`, which is a security risk. Move them to environment variables for production.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/OnePieceLwc/CodeMind-MCP/blob/HEAD/LICENSE) file for details.

**Official site: ** [https://github.com/OnePieceLwc/CodeMind-MCP](https://github.com/OnePieceLwc/CodeMind-MCP)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `developer tools`, `思维导图`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `@lucianaib/codemind-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/weiaib-codemind.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
