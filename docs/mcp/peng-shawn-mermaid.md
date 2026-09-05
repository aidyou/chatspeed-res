---
title: "mermaid-mcp-server"
description: "A Model Context Protocol (MCP) server that converts Mermaid diagrams to PNG images."
---

# mermaid-mcp-server

A Model Context Protocol (MCP) server that converts Mermaid diagrams to PNG images.

# Mermaid MCP Server

A Model Context Protocol (MCP) server that converts Mermaid diagrams to PNG images. This server allows AI assistants and other applications to generate visual diagrams from textual descriptions using the Mermaid markdown syntax.

## Features

- Converts Mermaid diagram code to PNG images
- Supports multiple diagram themes (default, forest, dark, neutral)
- Customizable background colors
- Uses Puppeteer for high-quality headless browser rendering
- Implements the MCP protocol for seamless integration with AI assistants
- Flexible output options: return images directly or save to disk
- Error handling with detailed error messages

## How It Works

The server uses Puppeteer to launch a headless browser, render the Mermaid diagram to SVG, and capture a screenshot of the rendered diagram. The process involves:

1. Launching a headless browser instance
2. Creating an HTML template with the Mermaid code
3. Loading the Mermaid.js library
4. Rendering the diagram to SVG
5. Taking a screenshot of the rendered SVG as PNG
6. Either returning the image directly or saving it to disk

## Build

```bash
npx tsc
```

## Usage

### Use with Claude desktop

```json
"mcpServers": {
  "mermaid": {
    "command": "npx",
    "args": [
      npx @peng-shawn/mermaid-mcp-server
    ]
  }
}
```

### Use with Cursor and Cline

```bash
env CONTENT_IMAGE_SUPPORTED=false npx @peng-shawn/mermaid-mcp-server
```

You can find a list of mermaid diagrams under `./diagrams`, they are created using Cursor agent with prompt: "generate mermaid diagrams and save them in a separate diagrams folder explaining how renderMermaidPng work"

### Run with inspector

Run the server with inspector for testing and debugging:

```bash
npx @modelcontextprotocol/inspector node dist/index.js
```

The server will start and listen on stdio for MCP protocol messages.

Learn more about inspector [here](https://modelcontextprotocol.io/docs/tools/inspector).

### Installing via Smithery

To install Mermaid Diagram Generator for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@peng-shawn/mermaid-mcp-server):

```bash
npx -y @smithery/cli install @peng-shawn/mermaid-mcp-server --client claude
```

### Docker and Smithery Environments

When running in Docker containers (including via Smithery), you may need to handle Chrome dependencies:

1. The server now attempts to use Puppeteer's bundled browser by default
2. If you encounter browser-related errors, you have two options:

   **Option 1: During Docker image build:**
   - Set `PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true` when installing Puppeteer
   - Install Chrome/Chromium in your Docker container
   - Set `PUPPETEER_EXECUTABLE_PATH` at runtime to point to the Chrome installation

   **Option 2: Use Puppeteer's bundled Chrome:**
   - Ensure your Docker container has the necessary dependencies for Chrome
   - No need to set `PUPPETEER_SKIP_CHROMIUM_DOWNLOAD`
   - The code will use the bundled browser automatically

For Smithery users, the latest version should work without additional configuration.

## API

The server exposes a single tool:

- `generate`: Converts Mermaid diagram code to a PNG image
  - Parameters:
    - `code`: The Mermaid diagram code to render
    - `theme`: (optional) Theme for the diagram. Options: "default", "forest", "dark", "neutral"
    - `backgroundColor`: (optional) Background color for the diagram, e.g. 'white', 'transparent', '#F0F0F0'
    - `name`: Name for the generated file (required when CONTENT_IMAGE_SUPPORTED=false)
    - `folder`: Absolute path to save the image to (required when CONTENT_IMAGE_SUPPORTED=false)

The behavior of the `generate` tool depends on the `CONTENT_IMAGE_SUPPORTED` environment variable:

- When `CONTENT_IMAGE_SUPPORTED=true` (default): The tool returns the image directly in the response
- When `CONTENT_IMAGE_SUPPORTED=false`: The tool saves the image to the specified folder and returns the file path

## Environment Variables

- `CONTENT_IMAGE_SUPPORTED`: Controls whether images are returned directly in the response or saved to disk
  - `true` (default): Images are returned directly in the response
  - `false`: Images are saved to disk, requiring `name` and `folder` parameters

## Examples

### Basic Usage

```javascript
// Generate a flowchart with default settings
{
  "code": "flowchart TD
    A[Start] --> B{Is it?}
    B -->|Yes| C[OK]
    B -->|No| D[End]"
}
```

### With Theme and Background Color

```javascript
// Generate a sequence diagram with forest theme and light gray background
{
  "code": "sequenceDiagram
    Alice->>John: Hello John, how are you?
    John-->>Alice: Great!",
  "theme": "forest",
  "backgroundColor": "#F0F0F0"
}
```

### Saving to Disk (when CONTENT_IMAGE_SUPPORTED=false)

```javascript
// Generate a class diagram and save it to disk
{
  "code": "classDiagram
    Class01 
  

## License

MIT
```

**Official site: ** [https://github.com/peng-shawn/mermaid-mcp-server](https://github.com/peng-shawn/mermaid-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `developer tools`, `image and video processing`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @peng-shawn/mermaid-mcp-server`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/peng-shawn-mermaid.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
