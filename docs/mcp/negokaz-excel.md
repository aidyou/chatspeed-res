---
title: "excel-mcp-server"
description: "A Model Context Protocol server that enables AI assistants to read from and write to Microsoft Excel files, supporting formats like xlsx, xlsm, xltx, and xltm."
---

# excel-mcp-server

A Model Context Protocol server that enables AI assistants to read from and write to Microsoft Excel files, supporting formats like xlsx, xlsm, xltx, and xltm.

# Excel MCP Server

 width="128">

[![NPM Version](/mcp-assets/2676ce9d04906ee62bf588f55bb53df6.svg)](https://www.npmjs.com/package/@negokaz/excel-mcp-server)
[Smithery](https://smithery.ai/server/@negokaz/excel-mcp-server)

A Model Context Protocol (MCP) server that reads and writes MS Excel data.

## Features

- Read text values from MS Excel file
- Write text values to MS Excel file
- Read formulas from MS Excel file
- Write formulas to MS Excel file
- Capture screen image from MS Excel file (Windows only)

For more details, see the [tools](#tools) section.

## Requirements

- Node.js 20.x or later

## Supported file formats

- xlsx (Excel book)
- xlsm (Excel macro-enabled book)
- xltx (Excel template)
- xltm (Excel macro-enabled template)

## Installation

### Installing via NPM

excel-mcp-server is automatically installed by adding the following configuration to the MCP servers configuration.

For Windows:
```json
{
    "mcpServers": {
        "excel": {
            "command": "cmd",
            "args": ["/c", "npx", "--yes", "@negokaz/excel-mcp-server"],
            "env": {
                "EXCEL_MCP_PAGING_CELLS_LIMIT": "4000"
            }
        }
    }
}
```

For other platforms:
```json
{
    "mcpServers": {
        "excel": {
            "command": "npx",
            "args": ["--yes", "@negokaz/excel-mcp-server"],
            "env": {
                "EXCEL_MCP_PAGING_CELLS_LIMIT": "4000"
            }
        }
    }
}
```

### Installing via Smithery

To install Excel MCP Server for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@negokaz/excel-mcp-server):

```bash
npx -y @smithery/cli install @negokaz/excel-mcp-server --client claude
```

Tools

### `read_sheet_names`

List all sheet names in an Excel file.

**Arguments:**
- `fileAbsolutePath`
    - Absolute path to the Excel file

### `read_sheet_data`

Read data from Excel sheet with pagination.

**Arguments:**
- `fileAbsolutePath`
    - Absolute path to the Excel file
- `sheetName`
    - Sheet name in the Excel file
- `range`
    - Range of cells to read in the Excel sheet (e.g., "A1:C10"). [default: first paging range]
- `knownPagingRanges`
    - List of already read paging ranges

### `read_sheet_formula`

Read formulas from Excel sheet with pagination.

**Arguments:**
- `fileAbsolutePath`
    - Absolute path to the Excel file
- `sheetName`
    - Sheet name in the Excel file
- `range`
    - Range of cells to read in the Excel sheet (e.g., "A1:C10"). [default: first paging range]
- `knownPagingRanges`
    - List of already read paging ranges

### `read_sheet_image`

**[Windows only]** Read data as an image from the Excel sheet with pagination.

**Arguments:**
- `fileAbsolutePath`
    - Absolute path to the Excel file
- `sheetName`
    - Sheet name in the Excel file
- `range`
    - Range of cells to read in the Excel sheet (e.g., "A1:C10"). [default: first paging range]
- `knownPagingRanges`
    - List of already read paging ranges

### `write_sheet_data`

Write data to the Excel sheet.

**Arguments:**
- `fileAbsolutePath`
    - Absolute path to the Excel file
- `sheetName`
    - Sheet name in the Excel file
- `range`
    - Range of cells to read in the Excel sheet (e.g., "A1:C10").
- `data`
    - Data to write to the Excel sheet

### `write_sheet_formula`

Write formulas to the Excel sheet.

**Arguments:**
- `fileAbsolutePath`
    - Absolute path to the Excel file
- `sheetName`
    - Sheet name in the Excel file
- `range`
    - Range of cells to read in the Excel sheet (e.g., "A1:C10").
- `formulas`
    - Formulas to write to the Excel sheet (e.g., "=A1+B1")

Configuration

You can change the MCP Server behaviors by the following environment variables:

### `EXCEL_MCP_PAGING_CELLS_LIMIT`

The maximum number of cells to read in a single paging operation.  
[default: 4000]

## License

Copyright (c) 2025 Kazuki Negoro

excel-mcp-server is released under the [MIT License](https://github.com/negokaz/excel-mcp-server/blob/HEAD/LICENSE)

**Official site: ** [https://github.com/negokaz/excel-mcp-server](https://github.com/negokaz/excel-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `files`
- Tags: `file systems`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `--yes @negokaz/excel-mcp-server`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/negokaz-excel.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
