---
title: "mcp-file-preview"
description: "Provides HTML file preview and analysis capabilities. This server enables capturing full-page screenshots of local HTML files and analyzing their structure."
---

# mcp-file-preview

Provides HTML file preview and analysis capabilities. This server enables capturing full-page screenshots of local HTML files and analyzing their structure.

# MCP File Preview Server

A Model Context Protocol (MCP) server that provides HTML file preview and analysis capabilities. This server enables capturing full-page screenshots of local HTML files and analyzing their structure.

## Features

- **File Preview**: Capture full-page screenshots of HTML files with proper CSS styling
- **Content Analysis**: Analyze HTML structure (headings, paragraphs, images, links)
- **Local File Support**: Handle local file paths and resources
- **Screenshot Management**: Save screenshots to a dedicated directory

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/mcp-file-preview.git
cd mcp-file-preview
```

2. Install dependencies:
```bash
npm install
```

3. Build the project:
```bash
npm run build
```

## Configuration

Add the server to your Claude or Cline MCP settings:

### Claude Desktop App
Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "file-preview": {
      "command": "node",
      "args": ["/path/to/mcp-file-preview/build/index.js"]
    }
  }
}
```

### Cline VSCode Extension
Add to VSCode's MCP settings:
```json
{
  "mcpServers": {
    "file-preview": {
      "command": "node",
      "args": ["/path/to/mcp-file-preview/build/index.js"]
    }
  }
}
```

## Usage

The server provides two main tools:

### preview_file
Captures a screenshot and returns HTML content:
```typescript

file-preview
preview_file

{
  "filePath": "/path/to/file.html",
  "width": 1024,  // optional
  "height": 768   // optional
}

```

Screenshots are saved to `screenshots/` directory in the project folder.

### analyze_content
Analyzes HTML structure:
```typescript

file-preview
analyze_content

{
  "filePath": "/path/to/file.html"
}

```

Returns counts of:
- Headings
- Paragraphs
- Images
- Links

## Development

1. Install dependencies:
```bash
npm install @modelcontextprotocol/sdk puppeteer typescript @types/node @types/puppeteer
```

2. Make changes in `src/`
3. Build:
```bash
npm run build
```
4. Test locally:
```bash
npm run dev
```

## Implementation Details

The server uses the MCP SDK's Server class with proper initialization:

```typescript
this.server = new Server(
  // Metadata object
  {
    name: 'file-preview-server',
    version: '0.1.0'
  },
  // Options object with capabilities
  {
    capabilities: {
      tools: {
        preview_file: {
          description: 'Preview local HTML file and capture screenshot',
          inputSchema: {
            // ... schema definition
          }
        }
      }
    }
  }
);
```

Key points:
- Server constructor takes separate metadata and options objects
- Tools are declared in capabilities.tools
- Each tool needs a description and inputSchema
- Screenshots are saved to a local `screenshots/` directory

## Debugging

1. Use the MCP Inspector:
```bash
npx @modelcontextprotocol/inspector
```

2. Connect with:
   - Transport Type: STDIO
   - Command: node
   - Arguments: /path/to/build/index.js

3. Check Claude OS logs if tools don't appear in the dropdown

## Contributing

Please read [CONTRIBUTING.md](https://github.com/seanivore/mcp-file-preview/blob/HEAD/CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/seanivore/mcp-file-preview/blob/HEAD/LICENSE) file for details.

**Official site: ** [https://github.com/seanivore/mcp-file-preview](https://github.com/seanivore/mcp-file-preview)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `files`
- Tags: `file systems`, `browser automation`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `node`
- Args: `/path/to/mcp-file-preview/build/index.js`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/seanivore-file-preview.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
