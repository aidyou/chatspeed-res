---
title: "modao-proto-mcp"
description: "A prototype generation service built on the Model Context Protocol, focused on HTML code generation, design description generation, and HTML import. - HTML code generation: generates complete HTML cod…"
---

# modao-proto-mcp

A prototype generation service built on the Model Context Protocol, focused on HTML code generation, design description generation, and HTML import. - HTML code generation: generates complete HTML cod…

# modao-proto-mcp

A prototype generation service built on the Model Context Protocol, focused on HTML code generation, design description generation, and HTML import.

## Features

- **HTML code generation**: generate complete HTML code from user descriptions, supporting modern design and responsive layouts
- **Design description generation**: generate detailed design specification documents from brief user requirements
- **HTML import**: import generated HTML into the user's personal space via a key
- **MCP protocol**: fully compatible with the Model Context Protocol standard
- **Extensible**: easy to add new tools and features
- **Efficient handling**: supports multiple parameter formats and an error handling mechanism

## Installation

```bash
npm install
```

## Build

```bash
npm run build
```

## Usage

### Starting the server

```bash
# Basic usage
node dist/index.js --token YOUR_API_TOKEN

# Specify the API address
node dist/index.js --token YOUR_API_TOKEN --url https://modao.cc

# Enable debug mode
node dist/index.js --token YOUR_API_TOKEN --debug
```

### Parameters

- `--token`: API service access token (required)
- `--url`: API service address (optional, default: https://modao.cc)
- `--debug`: enable debug mode (optional)

## MCP Client Configuration

### Generic configuration

Works for all MCP-capable clients:

```json
{
  "mcpServers": {
    "modao-proto-mcp": {
      "command": "npx",
      "args": [
        "-y",
        "@modao-mcp/modao-proto-mcp",
        "--token=YOUR_TOKEN",
        "--url=https://modao.cc"
      ]
    }
  }
}
```

### Claude Desktop

**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
**Linux:** `~/.config/claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "modao-proto-mcp": {
      "command": "npx",
      "args": [
        "-y",
        "@modao-mcp/modao-proto-mcp",
        "--token=YOUR_TOKEN",
        "--url=https://modao.cc"
      ]
    }
  }
}
```

### Cursor

Add to `settings.json`:

```json
{
  "mcp.servers": {
    "modao-proto-mcp": {
      "command": "npx",
      "args": [
        "-y",
        "@modao-mcp/modao-proto-mcp",
        "--token=YOUR_TOKEN",
        "--url=https://modao.cc"
      ]
    }
  }
}
```

### Windsurf

Add to `~/.windsurf/config.json`:

```json
{
  "mcp": {
    "servers": {
      "modao-proto-mcp": {
        "command": "npx",
        "args": [
          "-y",
          "@modao-mcp/modao-proto-mcp",
          "--token=YOUR_TOKEN",
          "--url=https://modao.cc"
        ]
      }
    }
  }
}
```

### Claude Code

Add to `~/.claude-code/config.json`:

```json
{
  "mcpServers": {
    "modao-proto-mcp": {
      "command": "npx",
      "args": [
        "-y",
        "@modao-mcp/modao-proto-mcp",
        "--token=YOUR_TOKEN",
        "--url=https://modao.cc"
      ]
    }
  }
}
```

### FAQ

**Getting a Token:** If the token fails, log in at [modao.cc](https://modao.cc) or [modao.cc/ai](https://modao.cc/ai), click the avatar in the top-right corner -> Token settings -> Create token

**Insufficient credits:** If gen_html cannot generate (not enough credits), top up at [modao.cc/ai](https://modao.cc/ai)

## Tools

### 1. gen_html

Generates complete HTML code from user descriptions, supporting modern design and responsive layouts.

**Description:**
- Generates an HTML file matching the user's design requirements
- Supports multiple design styles and layout approaches
- Returns complete HTML code, including real image URLs
- Generated HTML automatically includes the required CSS styling

**Parameters:**
- `user_input` (string, required): the user's design requirement description, e.g. 'create a modern login page'
- `reference` (string, optional): optional reference information or context

**Returns:**
- Complete HTML code (from ` ` to ` `)
- A generated key (used for subsequent import operations)

**Example:**
```json
{
  "name": "gen_html",
  "arguments": {
    "user_input": "Create a modern login page with username and password input fields",
    "reference": "Use Material Design style with blue as the primary color"
  }
}
```

### 2. gen_description

Generates a detailed design specification document based on brief user design requirements.

**Description:**
- Expands a brief design idea into a detailed design spec
- Supports plain-text requirements, reference-image requirements, or text + reference image
- Only use it when the user explicitly asks to expand their design requirements

**Parameters:**
- `user_input` (string, required): the user's design idea or requirement description
- `reference` (string, optional): optional reference information or context

**Example:**
```json
{
  "name": "gen_description",
  "arguments": {
    "user_input": "E-commerce product list page",
    "reference": "Needs filtering, sorting and pagination support"
  }
}
```

### 3. import_html

Imports the HTML generated by the gen_html tool into the user's personal space.

**Description:**
- Uses the key returned by the gen_html tool to import HTML
- Saves the generated HTML content to the user's personal space
- Supports an optional HTML string parameter as a fallback

**Parameters:**
- `key` (string, recommended): the key obtained from the gen_html tool response; the primary parameter for the import operation
- `htmlString` (string, optional): optional HTML string content; usually not needed

**Usage suggestions:**
- Use the key parameter returned by gen_html for import
- The key contains all necessary import information, so no manual HTML content is required

**Example:**
```json
{
  "name": "import_html",
  "arguments": {
    "key": "key value obtained from the gen_html tool"
  }
}
```

## Complete Workflows

### Basic workflow

1. **Generate HTML**: use the `gen_html` tool to generate HTML code from the requirements
2. **Import HTML**: use the `import_html` tool to import the generated HTML into your personal space

### Extended workflow

If you need a more detailed design spec:

1. **Generate design description**: use the `gen_description` tool to expand the design requirements
2. **Generate HTML**: use the generated design description as a reference and call `gen_html`
3. **Import HTML**: use `import_html` to save it to your personal space

**Complete example:**

```json
# 1. Generate HTML (basic flow)
{
  "name": "gen_html",
  "arguments": {
    "user_input": "Create a modern login page with username and password input fields"
  }
}

# 2. Import HTML (using the returned key)
{
  "name": "import_html",
  "arguments": {
    "key": "key value returned by the gen_html tool"
  }
}
```

**Extended example (with design description):**

```json
# 1. Generate a detailed design description
{
  "name": "gen_description",
  "arguments": {
    "user_input": "E-commerce product list page",
    "reference": "Needs filtering, sorting and pagination support"
  }
}

# 2. Generate HTML based on the design description
{
  "name": "gen_html",
  "arguments": {
    "user_input": "E-commerce product list page",
    "reference": "The detailed design description generated in the previous step"
  }
}

# 3. Import HTML
{
  "name": "import_html",
  "arguments": {
    "key": "key value returned by the gen_html tool"
  }
}
```

## Project Structure

```
modao-proto-mcp/
├── src/
│   ├── tools/
│   │   ├── base-tool.ts       # Tool base class, provides common functionality
│   │   ├── gen-html.ts        # HTML generation tool
│   │   ├── gen-description.ts # Design description generation tool
│   │   └── import-html.ts     # HTML import tool
│   ├── http-util.ts           # HTTP utility class, handles API requests
│   ├── types.d.ts             # TypeScript type definitions
│   └── index.ts               # MCP server main entry point
├── bin/
│   └── cli.js                 # CLI executable
├── examples/                  # Usage examples and docs
├── scripts/                   # Build and publish scripts
├── build.js                   # Project build config
├── package.json              # Project dependencies and config
├── tsconfig.json             # TypeScript config
├── API.md                    # Detailed API docs
├── README.md                 # English README
└── README.zh-CN.md           # Chinese README
```

## Technical Architecture

```
User request -> MCP client -> MCP server -> HTTP utility -> Backend API
                                                         |
                        Response handling <- Result formatting <- API response
```

## Development Guide

### Adding a new tool

1. **Create the tool class**: create a new tool class file under `src/tools/`
2. **Inherit the base class**: extend the `BaseTool` abstract class
3. **Implement the required methods**:
   - `getToolDefinition()`: define the tool's MCP spec
   - `execute()`: implement the tool's core logic
4. **Register the tool**: register the new tool in the `initializeTools()` method of `src/index.ts`

### Tool development example

```typescript
import { Tool } from '@modelcontextprotocol/sdk/types.js';
import { BaseTool } from './base-tool.js';
import { ToolResult } from '../types.js';

export class MyNewTool extends BaseTool {
  getToolDefinition(): Tool {
    return {
      name: "my_new_tool",
      description: "Tool description",
      inputSchema: {
        type: "object",
        properties: {
          input_param: {
            type: "string",
            description: "Parameter description"
          }
        },
        required: ["input_param"]
      }
    };
  }

  async execute(args: Record): Promise {
    // Implement the tool logic
    const result = await this.httpUtil.post('/api/endpoint', args);
    return this.createSuccessResult(result.data);
  }
}
```

### Development notes

1. **Parameter validation**: use the `validateRequiredArgs()` method to validate required parameters
2. **Error handling**: use `createErrorResult()` and `formatApiError()` to handle errors
3. **HTTP requests**: send API requests through `this.httpUtil`
4. **Debug mode**: use the `--debug` parameter to enable verbose logging

## License

MIT License

## Contributing

Issues and Pull Requests are welcome!

## Changelog

### v1.3.7 (current)
- Improved the HTML import flow, importing via key
- Improved tool descriptions and parameter docs
- Simplified workflows; removed the organization file-tree feature
- Rewrote the README to more accurately reflect actual functionality
- Improved error handling and parameter validation

### v1.2.0
- Added HTML import (`import_html`)
- Full HTML generation-to-import workflow support
- Improved the HTTP utility class and error handling

### v1.1.0
- Added design description generation (`gen_description`)
- Improved HTML generation
- Completed MCP protocol compatibility
- Added detailed usage documentation

### v1.0.0
- Initial release
- HTML code generation (`gen_html`)
- Fully compatible with the Model Context Protocol standard
- Complete development and build toolchain

**Official site: ** [https://github.com/modao-dev/modao-proto-mcp](https://github.com/modao-dev/modao-proto-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `files`, `communication`
- Tags: `developer tools`, `communication`, `file systems`, `产品`, `产品经理`, `设计`, `原型`, `proto`, `ai生成`, `ui设计`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @modao-mcp/modao-proto-mcp --token=YOUR_TOKEN --url=https://modao.cc`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/mockingbot-modao-proto.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
