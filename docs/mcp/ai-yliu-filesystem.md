---
title: "filesystem-mcp-server"
description: "An MCP server that allows Claude AI to perform filesystem operations including reading, writing, listing, moving files, and searching directories within specified allowed paths."
---

# filesystem-mcp-server

An MCP server that allows Claude AI to perform filesystem operations including reading, writing, listing, moving files, and searching directories within specified allowed paths.

# Filesystem MCP Server

A Model Context Protocol (MCP) server that provides filesystem operations for Claude AI.

## Features

This MCP server provides the following filesystem operations:

1. **read_file**: Read complete contents of a file
   - Input: `path` (string)
   - Reads complete file contents with UTF-8 encoding

2. **read_multiple_files**: Read multiple files simultaneously
   - Input: `paths` (string[])
   - Failed reads Will not  stop the entire operation

3. **write_file**: Create new file or overwrite existing 
   - Inputs:
     - `path` (string): File location
     - `content` (string): File content

4. **create_directory**: Create new directory or ensure it exists
   - Input: `path` (string)
   - Creates parent directories if needed
   - Succeeds silently if directory exists

5. **list_directory**: List directory contents with [FILE] or [DIR] prefixes
   - Input: `path` (string)

6. **move_file**: Move or rename files and directories
   - Inputs:
     - `source` (string)
     - `destination` (string)
   - Fails if destination exists

7. **search_files**: Recursively search for files/directories
   - Inputs:
     - `path` (string): Starting directory
     - `pattern` (string): Search pattern
   - Case-insensitive matching
   - Returns full paths to matches

8. **get_file_info**: Get detailed file/directory metadata
   - Input: `path` (string)
   - Returns:
     - Size
     - Creation time
     - Modified time
     - Access time
     - Type (file/directory)
     - Permissions

9. **list_allowed_directories**: List all directories the server is allowed to access
   - No input required
   - Returns directories that this server can read/write from

## Security

The server only allows operations within directories specified via command-line arguments.

## Installation

1. Clone this repository
2. Install dependencies: `npm install`
3. Build the project: `npm run build`

## Usage

Run the server with one or more allowed directories:

```bash
node build/index.js /path/to/allowed/dir1 /path/to/allowed/dir2
```

## MCP Configuration

Add the server to your MCP configuration file:

```json
{
  "mcpServers": {
    "filesystem-server": {
      "command": "node",
      "args": [
        "/path/to/filesystem-server/build/index.js",
        "/path/to/allowed/dir1",
        "/path/to/allowed/dir2"
      ],
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

## License

ISC

**Official site: ** [https://github.com/ai-yliu/filesystem-mcp-server](https://github.com/ai-yliu/filesystem-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `files`
- Tags: `file systems`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `node`
- Args: `/path/to/filesystem-server/build/index.js /path/to/allowed/dir1 /path/to/allowed/dir2`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/ai-yliu-filesystem.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
