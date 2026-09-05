---
title: "datagov-mcp-server"
description: "An MCP server that provides access to government datasets from Data.gov, enabling users to search packages, view dataset details, list groups and tags, and access resources by URL."
---

# datagov-mcp-server

An MCP server that provides access to government datasets from Data.gov, enabling users to search packages, view dataset details, list groups and tags, and access resources by URL.

# Data.gov MCP Server

An MCP server for accessing data from Data.gov, providing tools and resources for interacting with government datasets.

  

## Installation

1.  **Install the package globally:**

```bash
    npm install -g @melaodoidao/datagov-mcp-server
```

2. **Configure the MCP Server:**

   - Add the following entry to your `cline_mcp_settings.json` file (usually located in `~/Library/Application Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings/` on macOS):

```json
      {
        "mcpServers": {
          "datagov": {
            "command": "datagov-mcp-server",
            "args": [],
            "env": {}
          }
        }
      }
```
    - If you are using the Claude Desktop app, add the entry to `~/Library/Application Support/Claude/claude_desktop_config.json` instead.

## Usage

This server provides the following tools:

*   `package_search`: Search for packages (datasets) on Data.gov.
*   `package_show`: Get details for a specific package (dataset).
*   `group_list`: List groups on Data.gov.
*   `tag_list`: List tags on Data.gov.

It also provides the following resource template:

*   `datagov://resource/{url}`: Access a Data.gov resource by its URL.

You can use these tools and resources with Cline by specifying the server name (`datagov-mcp-server`) and the tool/resource name.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

MIT License

**Official site: ** [https://github.com/melaodoidao/datagov-mcp-server](https://github.com/melaodoidao/datagov-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `research and data`, `search`, `databases`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `datagov-mcp-server`
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/melaodoidao-datagov.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
