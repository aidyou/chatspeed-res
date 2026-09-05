---
title: "Markmap"
description: "Markmap MCP Server"
---

# Markmap

Markmap MCP Server

# Markmap MCP Server

![Sample Mindmap](/mcp-assets/07821881e23a7de173334ab6f80a30cb.svg)

[![NPM Version](/mcp-assets/5215456c7a7c62a7b68a38ffe10a9510.svg)](https://www.npmjs.com/package/@jinzcdev/markmap-mcp-server)
[![NPM Downloads](/mcp-assets/587bcdeeb5029f0e24e6a02976346e6c.svg)](https://www.npmjs.com/package/@jinzcdev/markmap-mcp-server)
[![GitHub License](/mcp-assets/5816f652aa1f0cc4eedb21a2f733e09e.svg)](https://github.com/jinzcdev/markmap-mcp-server/blob/HEAD/LICENSE)
![English Doc](/mcp-assets/a01eeaa9426e702efc5bcbd844f06a1d.svg)
[![Stars](/mcp-assets/174243a363738db56c37c6a4cf1bbced.svg)](https://github.com/jinzcdev/markmap-mcp-server)

Markmap MCP Server is based on the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) and uses the open-source project [markmap](https://github.com/markmap/markmap) to convert Markdown into interactive mind maps. It supports exporting PNG / JPG / SVG on the **server side**, making it easy for Agents to consume directly in conversations. The conversion process is completed **locally** without the need for a third-party API Key.

## Features

- **Markdown to Mind Map**: Titles and nested lists → Interactive HTML map
- **Agent-friendly Return**: Can return file paths, inline HTML, and/or image content (configured at startup)
- **Server-side Export**: Export PNG / JPG / SVG via Playwright for in-chat preview
- **Browser Preview**: Configurable open behavior — always open, never open, or decided by Agent (configured at startup)
- **Page Export Toolbar**: One-click export of images or copy Markdown in the browser
- **Offline HTML**: Startup parameter `--offline` inlines resources, no CDN access required
- **File Workflow**: Supports `inputPath`, lists recent files, and cleans up old files
- **Privacy First**: Purely local generation, no cloud-based mind map API

## Prerequisites

1. Node.js **v20 or above**
2. When using **server-side image export** (`format: png|jpg|svg`), install Playwright and Chromium:

bash
```bash
npm install playwright
npx playwright install chromium
```
(`playwright` is an optional dependency of this package.)

## Installation

bash
```bash
# Install from npm
npm install @jinzcdev/markmap-mcp-server -g

# Basic run
npx -y @jinzcdev/markmap-mcp-server

# Specify an output directory and auto-open the browser
npx -y @jinzcdev/markmap-mcp-server --output /path/to/output/directory --open always
```
### Docker

bash
```bash
docker build -t markmap-mcp-server .
docker run --rm -i \
  -v /path/to/output:/data/markmap \
  -e MARKMAP_DIR=/data/markmap \
  markmap-mcp-server
```
or clone the repository and run locally:

bash
```bash
git clone https://github.com/jinzcdev/markmap-mcp-server.git
cd markmap-mcp-server
npm install && npm run build
# Optional: enable server-side image export
npx playwright install chromium
node build/index.js
```
## Usage

Add the following configuration to your MCP client (Cursor / Claude Desktop, etc.):

json
```json
{
  "mcpServers": {
    "markmap": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@jinzcdev/markmap-mcp-server"],
      "env": {
        "MARKMAP_DIR": "/path/to/output/directory",
        "MARKMAP_OPEN": "never",
        "MARKMAP_RETURN_MODE": "path"
      }
    }
  }
}
```
### Service Startup Preferences (CLI / Environment Variables)

The following options are determined **at service startup** and are **not** tool parameters:

| Preference     | CLI               | Environment Variable              | Possible Values                                                   | Default           |
| -------------- | ----------------- | --------------------------------- | ----------------------------------------------------------------- | ----------------- |
| Output Directory | `--output` / `-o` | `MARKMAP_DIR`                     | Any directory path                                                | `~/.markmap-mcp`  |
| Open Browser   | `--open [mode]`   | `MARKMAP_OPEN`                    | `always` \| `never` \| `agent` (bare `--open` = `always`)         | `never`           |
| Return Mode    | `--return-mode`   | `MARKMAP_RETURN_MODE`             | `path` \| `content` \| `both`                                     | `path`            |
| Offline HTML   | `--offline`       | `MARKMAP_OFFLINE`                 | `true` \| `false` (CLI only needs `--offline` to enable)          | `false`           |

Command-line arguments take precedence over environment variables; `--output` takes precedence over `MARKMAP_DIR`.

**`--open`:** Bare `--open` is equivalent to `always`; you can also explicitly pass `--open always|never|agent`. Invalid values will cause an error and exit. If the flag is not written, `MARKMAP_OPEN` (default `never`) is used.

**Return Modes:**

| Mode      | Meaning                                                     |
| --------- | ----------------------------------------------------------- |
| `path`    | Only path JSON (`htmlFilePath` + `filePath`)                |
| `content` | Only inline content (raw HTML text, or base64 image block)  |
| `both`    | Path JSON + inline content                                  |

Generated HTML always includes the markmap toolbar, English export button text, and all nodes are expanded by default.

### Example Prompts

- "Organize this design document into a mind map."
- "Convert `./notes/architecture.md` into a mind map."
- "Generate a PNG mind map from the following outline and display it directly in the conversation."

## Available Tools

### `markdown_to_mindmap`Convert Markdown to an interactive mind map (optional image export).

| Parameter   | Type                              | Default | Description                                                                                                                     |
|-------------|-----------------------------------|---------|---------------------------------------------------------------------------------------------------------------------------------|
| `markdown`  | string                            | —       | Markdown content (at least one of `markdown` or `inputPath` must be provided; if both are given, `markdown` takes precedence)    |
| `inputPath` | string                            | —       | Absolute path to the local Markdown file                                                                                        |
| `format`    | `html` \| `png` \| `svg` \| `jpg` | `html`  | Output format; image formats require Playwright                                                                                  |
| `filename`  | string                            | auto    | Output filename (will be sanitized; prefixed with `markmap-` if necessary; overwrites existing files with the same name)         |
| `open`      | boolean                           | `false` | Whether to open the result in a browser. **Only appears in tool arguments when the server's open mode is `agent`** (`--open agent` / `MARKMAP_OPEN=agent`). |

**Return Value (`returnMode=path`):**

```json

{

  "htmlFilePath": "/path/to/markmap-….html",

  "filePath": "/path/to/markmap-….html"

}

```
For image formats, `filePath` is the path to the image, and `htmlFilePath` is still the source HTML file.

**Return Value (`returnMode=content`):** Raw HTML text block, or base64-encoded MCP `image` content block for PNG/JPG/SVG — without path JSON. Falls back to path JSON if HTML size is ≥200KB.

**Return Value (`returnMode=both`):** Path JSON + the above inline content.

> **Note:** Zooming/folding within the page and the "Export PNG/JPG/SVG" button are part of the **HTML preview experience**. If the agent needs to directly obtain images, use the tool parameter `format: png|jpg|svg`.

### `list_mindmaps`

Lists recently generated mind map files in the output directory (newest first). Only includes files whose names start with `markmap`.

| Parameter | Type   | Default | Description                  |
|-----------|--------|---------|------------------------------|
| `limit`   | number | `20`    | Maximum number of items to return (1–200) |

Returns `{outputDir, files: [{name, filePath, size, mtimeMs, mtime}]}`.

### `get_mindmap`

Retrieves a generated mind map file by its absolute path. The path must be within the configured output directory (path traversal is not allowed).

| Parameter  | Type   | Default | Description                              |
|------------|--------|---------|------------------------------------------|
| `filePath` | string | —       | Absolute path to the mind map file (HTML or image) |

Returns JSON `{filePath, mimeType, size}`. For HTML/SVG and less than 200KB, also includes the text content block; for PNG/JPG, only metadata is returned (no image block) — to get pixel data, re-export using `markdown_to_mindmap` with `format=png|jpg`.

### `cleanup_mindmaps`

Cleans up (or empties) mind map files in the output directory based on days.

| Parameter     | Type    | Default | Description                                       |
|-------------- | ------- | ------- | ------------------------------------------------- |
| `maxAgeDays`  | number  | `7`     | Deletes files older than the specified number of days |
| `all`         | boolean | `false` | If true, deletes all mind map files               |
| `dryRun`      | boolean | `false` | If true, only previews the files that would be deleted, without actually deleting them |

### Prompt: `mindmap_from_content`

Helper prompt: First organizes the content into hierarchical Markdown, then calls `markdown_to_mindmap`.

| Parameter | Type   | Default | Description                     |
|-----------|--------|---------|---------------------------------|
| `topic`   | string | —       | The topic or original text to organize into a mind map |

## Related Projects| Project                                                                            | Description                                                                |
| ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **[MarkXMind Online](https://github.com/jinzcdev/markxmind)**                   | Create XMind with Markdown online. [Try it now →](https://markxmind.js.org/) |
| **[Obsidian MarkXMind Plugin](https://github.com/jinzcdev/obsidian-markxmind)** | Render XMindMark mind maps in Obsidian.                             |

## License

This project is licensed under the [MIT](https://github.com/jinzcdev/markmap-mcp-server/blob/HEAD/LICENSE) license.

**Official site: ** [https://github.com/jinzcdev/markmap-mcp-server](https://github.com/jinzcdev/markmap-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `memory`
- Tags: `knowledge and memory`, `mindmap`, `markmap`, `思维导图`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @jinzcdev/markmap-mcp-server`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/jinzcdev-markmap.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
