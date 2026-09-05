---
title: "clickup-mcp-server"
description: "Enables AI integrations with ClickUp tasks, supporting resource management, task operations, workspace organization, and AI-powered task recommendations through a standardized protocol."
---

# clickup-mcp-server

Enables AI integrations with ClickUp tasks, supporting resource management, task operations, workspace organization, and AI-powered task recommendations through a standardized protocol.

alt="ClickUp MCP Server" width="100%">

[![GitHub Stars](/mcp-assets/c8ab93d8df15924ea3f3648c84d5a38e.svg)](https://github.com/TaazKareem/clickup-mcp-server/stargazers)
[![Maintenance](/mcp-assets/c7778e30c5b75ad6bdf042640f8a94d9.svg)](https://github.com/TaazKareem/clickup-mcp-server/graphs/commit-activity)

A Model Context Protocol (MCP) server for integrating ClickUp tasks with AI applications. This server allows AI agents to interact with ClickUp tasks, spaces, lists, and folders through a standardized protocol.

> 🚧 **Status Update:** Rolling out v0.6.8 will add Global Task Lookup with smart disambiguation, Start Date Support for tasks with natural language expressions, Complete Tag Support including natural language tag color commands, Subtasks Support, Custom ID Support, and Logging Fixes

## Setup

1. Get your credentials:
   - ClickUp API key from [ClickUp Settings](https://app.clickup.com/settings/apps)
   - Team ID from your ClickUp workspace URL
2. Choose either hosted installation (sends webhooks) or NPX installation (downloads to local path and installs dependencies)
3. Use natural language to manage your workspace!

## Smithery Installation (Quick Start)

[Smithery](https://smithery.ai/server/@TaazKareem/clickup-mcp-server)

The server is hosted on [Smithery](https://smithery.ai/server/@taazkareem/clickup-mcp-server). There, you can preview the available tools or copy the commands to run on your specific client app. 

## NPX Installation

[![NPM Version](/mcp-assets/63a09ba3381401ee3ab91cb41b16156b.svg)](https://www.npmjs.com/package/@taazkareem/clickup-mcp-server)
[![Dependency Status](/mcp-assets/80a22720777445f6d9736d2023c537c2.svg)](https://github.com/TaazKareem/clickup-mcp-server/blob/main/package.json)
[![NPM Downloads](/mcp-assets/b5f06d7741a799aa895607d5a3ccc7bd.svg)](https://npmcharts.com/compare/@taazkareem/clickup-mcp-server?minimal=true)

Add this entry to your client's MCP settings JSON file:

```json
{
  "mcpServers": {
    "ClickUp": {
      "command": "npx",
      "args": [
        "-y",
        "@taazkareem/clickup-mcp-server@latest"
      ],
      "env": {
        "CLICKUP_API_KEY": "your-api-key",
        "CLICKUP_TEAM_ID": "your-team-id"
      }
    }
  }
}
```

Or use this npx command:

`npx -y @taazkareem/clickup-mcp-server@latest --env CLICKUP_API_KEY=your-api-key --env CLICKUP_TEAM_ID=your-team-id`

## Features

| 📝 Task Management | 🏷️ Tag Management |
|----------------------------|----------------------------|
| • Create, update, and delete tasks
• Move and duplicate tasks anywhere
• Support for single and bulk operations
• Set start/due dates with natural language
• Create and manage subtasks
• Add comments and attachments | • Create, update, and delete space tags
• Add and remove tags from tasks
• Use natural language color commands
• Automatic contrasting foreground colors
• View all space tags
• Tag-based task organization across workspace |
| 🌳 **Workspace Organization** | ⚡ **Integration Features** |
| • Navigate spaces, folders, and lists
• Create and manage folders
• Organize lists within spaces
• Create lists in folders
• View workspace hierarchy
• Efficient path navigation | • Global name or ID-based lookups
• Case-insensitive matching
• Markdown formatting support
• Built-in rate limiting
• Error handling and validation
• Comprehensive API coverage |

## Available Tools

| Tool | Description | Required Parameters |
|------|-------------|-------------------|
| get_workspace_hierarchy | Get workspace structure | None |
| create_task | Create a task | `name`, (`listId`/`listName`) |
| create_bulk_tasks | Create multiple tasks | `tasks[]` |
| update_task | Modify task | `taskId`/`taskName` |
| update_bulk_tasks | Update multiple tasks | `tasks[]` with IDs or names |
| get_tasks | Get tasks from list | `listId`/`listName` |
| get_task | Get single task details | `taskId`/`taskName` (with smart disambiguation) |
| get_workspace_tasks | Get tasks with filtering | At least one filter (tags, list_ids, space_ids, etc.) |
| get_task_comments | Get comments on a task | `taskId`/`taskName` |
| create_task_comment | Add a comment to a task | `commentText`, (`taskId`/(`taskName`+`listName`)) |
| attach_task_file | Attach file to a task | `taskId`/`taskName`, (`file_data` or `file_url`) |
| delete_task | Remove task | `taskId`/`taskName` |
| delete_bulk_tasks | Remove multiple tasks | `tasks[]` with IDs or names |
| move_task | Move task | `taskId`/`taskName`, `listId`/`listName` |
| move_bulk_tasks | Move multiple tasks | `tasks[]` with IDs or names, target list |
| duplicate_task | Copy task | `taskId`/`taskName`, `listId`/`listName` |
| create_list | Create list in space | `name`, `spaceId`/`spaceName` |
| create_folder | Create folder | `name`, `spaceId`/`spaceName` |
| create_list_in_folder | Create list in folder | `name`, `folderId`/`folderName` |
| get_folder | Get folder details | `folderId`/`folderName` |
| update_folder | Update folder properties | `folderId`/`folderName` |
| delete_folder | Delete folder | `folderId`/`folderName` |
| get_list | Get list details | `listId`/`listName` |
| update_list | Update list properties | `listId`/`listName` |
| delete_list | Delete list | `listId`/`listName` |
| get_space_tags | Get space tags | `spaceId`/`spaceName` |
| create_space_tag | Create tag | `tagName`, `spaceId`/`spaceName` |
| update_space_tag | Update tag | `tagName`, `spaceId`/`spaceName` |
| delete_space_tag | Delete tag | `tagName`, `spaceId`/`spaceName` |
| add_tag_to_task | Add tag to task | `tagName`, `taskId`/(`taskName`+`listName`) |
| remove_tag_from_task | Remove tag from task | `tagName`, `taskId`/(`taskName`+`listName`) |

See full documentation for optional parameters and advanced usage.

## Prompts
Not yet implemented and not supported by all client apps. Request a feature for a Prompt implementation that would be most beneficial for your workflow (without it being too specific). Examples:

| Prompt | Purpose | Features |
|--------|---------|----------|
| summarize_tasks | Task overview | Status summary, priorities, relationships |
| analyze_priorities | Priority optimization | Distribution analysis, sequencing |
| generate_description | Task description creation | Objectives, criteria, dependencies |

## Error Handling

The server provides clear error messages for:
- Missing required parameters
- Invalid IDs or names
- Items not found
- Permission issues
- API errors
- Rate limiting

The `LOG_LEVEL` environment variable can be specified to control the verbosity of server logs. Valid values are `trace`, `debug`, `info`, `warn`, and `error` (default).
This can be also be specified on the command line as, e.g. `--env LOG_LEVEL=info`.

## Support the Developer

When using this server, you may occasionally see a small sponsor message with a link to this repository included in tool responses. I hope you can support the project!
If you find this project useful, please consider supporting:

[![Sponsor TaazKareem](/mcp-assets/76fc25891c633e752edf4505b06e8874.svg)](https://github.com/sponsors/TaazKareem)

  

## Acknowledgements

Special thanks to [ClickUp](https://clickup.com) for their excellent API and services that make this integration possible.

## Contributing

Contributions are welcome! Please read our Contributing Guide for details.

## License

[![License: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](https://github.com/TaazKareem/clickup-mcp-server/blob/HEAD/LICENSE) file for details.

## Disclaimer

This software makes use of third-party APIs and may reference trademarks
or brands owned by third parties. The use of such APIs or references does not imply 
any affiliation with or endorsement by the respective companies. All trademarks and 
brand names are the property of their respective owners. This project is an independent
work and is not officially associated with or sponsored by any third-party company mentioned.

**Official site: ** [https://github.com/TaazKareem/clickup-mcp-server](https://github.com/TaazKareem/clickup-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`, `browser`
- Tags: `developer tools`, `os automation`, `other`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @taazkareem/clickup-mcp-server@latest`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/taazkareem-clickup.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
