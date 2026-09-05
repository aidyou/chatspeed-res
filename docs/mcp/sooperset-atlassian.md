---
title: "mcp-atlassian"
description: "Model Context Protocol (MCP) server for Atlassian Cloud products (Confluence and Jira). This integration is designed specifically for Atlassian Cloud instances and does not support Atlassian Server or…"
---

# mcp-atlassian

Model Context Protocol (MCP) server for Atlassian Cloud products (Confluence and Jira). This integration is designed specifically for Atlassian Cloud instances and does not support Atlassian Server or…

# MCP Atlassian

![PyPI Version](/mcp-assets/70c34732cb7c08d25b33412d96c854c2.svg)
![PyPI - Downloads](/mcp-assets/534c417bc36a0e78ef942b38b8523bb4.svg)
![PePy - Total Downloads](/mcp-assets/31d34999f0b703a47ffbb660990b858b.svg)
![License](/mcp-assets/5816f652aa1f0cc4eedb21a2f733e09e.svg)

Model Context Protocol (MCP) server for Atlassian products (Confluence and Jira). This integration supports both Confluence & Jira Cloud and Server/Data Center deployments.

### Feature Demo
![Jira Demo](/mcp-assets/61dba7a150323888b4ffffc9a9d3734d.gif)

Confluence Demo

![Confluence Demo](/mcp-assets/44e49275d5a90aaad801912c27834211.gif)

### Compatibility

| Product | Deployment Type | Support Status              |
|---------|----------------|-----------------------------|
| **Confluence** | Cloud | ✅ Fully supported           |
| **Confluence** | Server/Data Center | ✅ Supported (version 7.9+)  |
| **Jira** | Cloud | ✅ Fully supported           |
| **Jira** | Server/Data Center | ✅ Supported (version 8.14+) |

## Setup Guide

### 1. Authentication Setup

First, generate the necessary authentication tokens for Confluence & Jira:

#### For Cloud
1. Go to https://id.atlassian.com/manage-profile/security/api-tokens
2. Click **Create API token**, name it
3. Copy the token immediately

#### For Server/Data Center
1. Go to your profile (avatar) → **Profile** → **Personal Access Tokens**
2. Click **Create token**, name it, set expiry
3. Copy the token immediately

### 2. Installation

Choose one of these installation methods:

```bash
# Using uv (recommended)
brew install uv
uvx mcp-atlassian

# Using pip
pip install mcp-atlassian

# Using Docker
git clone https://github.com/sooperset/mcp-atlassian.git
cd mcp-atlassian
docker build -t mcp/atlassian .
```

### 3. Configuration and Usage

You can configure the MCP server using command line arguments. The server supports using either Confluence, Jira, or both services - include only the arguments needed for your use case.

#### Required Arguments

For Cloud:
```bash
uvx mcp-atlassian \n  --confluence-url https://your-company.atlassian.net/wiki \n  --confluence-username your.email@company.com \n  --confluence-token your_api_token \n  --jira-url https://your-company.atlassian.net \n  --jira-username your.email@company.com \n  --jira-token your_api_token
```

For Server/Data Center:
```bash
uvx mcp-atlassian \n  --confluence-url https://confluence.your-company.com \n  --confluence-personal-token your_token \n  --jira-url https://jira.your-company.com \n  --jira-personal-token your_token
```

> **Note:** You can configure just Confluence, just Jira, or both services. Simply include only the arguments for the service(s) you want to use. For example, to use only Confluence Cloud, you would only need `--confluence-url`, `--confluence-username`, and `--confluence-token`.

#### Optional Arguments

- `--transport`: Choose transport type (`stdio` [default] or `sse`)
- `--port`: Port number for SSE transport (default: 8000)
- `--[no-]confluence-ssl-verify`: Toggle SSL verification for Confluence Server/DC
- `--[no-]jira-ssl-verify`: Toggle SSL verification for Jira Server/DC
- `--confluence-spaces-filter`: Comma-separated list of space keys to filter Confluence search results (e.g., "DEV,TEAM,DOC")
- `--jira-projects-filter`: Comma-separated list of project keys to filter Jira search results (e.g., "PROJ,DEV,SUPPORT")
- `--read-only`: Run in read-only mode (disables all write operations)
- `--verbose`: Increase logging verbosity (can be used multiple times, default is WARNING level)
  - `-v` or `--verbose`: Set logging to INFO level
  - `-vv` or `--verbose --verbose`: Set logging to DEBUG level

> **Note:** All configuration options can also be set via environment variables. See the `.env.example` file in the repository for the full list of available environment variables.

## IDE Integration

### Claude Desktop Setup

Using uvx (recommended) - Cloud:

```json
{
  "mcpServers": {
    "mcp-atlassian": {
      "command": "uvx",
      "args": [
        "mcp-atlassian",
        "--confluence-url=https://your-company.atlassian.net/wiki",
        "--confluence-username=your.email@company.com",
        "--confluence-token=your_api_token",
        "--jira-url=https://your-company.atlassian.net",
        "--jira-username=your.email@company.com",
        "--jira-token=your_api_token"
      ]
    }
  }
}
```

Using uvx (recommended) - Server/Data Center 

```json
{
  "mcpServers": {
    "mcp-atlassian": {
      "command": "uvx",
      "args": [
        "mcp-atlassian",
        "--confluence-url=https://confluence.your-company.com",
        "--confluence-personal-token=your_token",
        "--jira-url=https://jira.your-company.com",
        "--jira-personal-token=your_token"
      ]
    }
  }
}
```

Using pip

> Note: Examples below use Cloud configuration. For Server/Data Center, use the corresponding arguments (--confluence-personal-token, --jira-personal-token) as shown in the Configuration section above.

```json
{
  "mcpServers": {
    "mcp-atlassian": {
      "command": "python",
      "args": [
        "-m",
        "mcp-atlassian",
        "--confluence-url=https://your-company.atlassian.net/wiki",
        "--confluence-username=your.email@company.com",
        "--confluence-token=your_api_token",
        "--jira-url=https://your-company.atlassian.net",
        "--jira-username=your.email@company.com",
        "--jira-token=your_api_token"
      ]
    }
  }
}
```

Using docker

> Note: Examples below use Cloud configuration. For Server/Data Center, use the corresponding arguments (--confluence-personal-token, --jira-personal-token) as shown in the Configuration section above.

There are two ways to configure the Docker environment:

1. Using cli arguments directly in the config:
```json
{
  "mcpServers": {
    "mcp-atlassian": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "mcp/atlassian",
        "--confluence-url=https://your-company.atlassian.net/wiki",
        "--confluence-username=your.email@company.com",
        "--confluence-token=your_api_token",
        "--jira-url=https://your-company.atlassian.net",
        "--jira-username=your.email@company.com",
        "--jira-token=your_api_token"
      ]
    }
  }
}
```

2. Using an environment file:
```json
{
  "mcpServers": {
    "mcp-atlassian": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "--env-file",
        "/path/to/your/.env",
        "mcp/atlassian"
      ]
    }
  }
}
```

### Cursor IDE Setup

1. Open Cursor Settings
2. Navigate to `Features` > `MCP Servers` (or directly to `MCP`)
3. Click `+ Add new global MCP server`

This will create or edit the `~/.cursor/mcp.json` file with your MCP server configuration.

![Cursor MCP Configuration](/mcp-assets/7454e87ad13115092aae5c745861c7fb.png)

#### JSON Configuration for stdio Transport

For Cloud:
```json
{
  "mcpServers": {
    "mcp-atlassian": {
      "command": "uvx",
      "args": [
        "mcp-atlassian",
        "--confluence-url=https://your-company.atlassian.net/wiki",
        "--confluence-username=your.email@company.com",
        "--confluence-token=your_api_token",
        "--jira-url=https://your-company.atlassian.net",
        "--jira-username=your.email@company.com",
        "--jira-token=your_api_token"
      ]
    }
  }
}
```

Server/Data Center Configuration

```json
{
  "mcpServers": {
    "mcp-atlassian": {
      "command": "uvx",
      "args": [
        "mcp-atlassian",
        "--confluence-url=https://confluence.your-company.com",
        "--confluence-personal-token=your_token",
        "--jira-url=https://jira.your-company.com",
        "--jira-personal-token=your_token"
      ]
    }
  }
}
```

#### SSE Transport Configuration

For SSE transport, first start the server:
```bash
uvx mcp-atlassian --transport sse --port 9000
```

Then configure in Cursor:
```json
{
  "mcpServers": {
    "mcp-atlassian-sse": {
      "url": "http://localhost:9000/sse",
      "env": {
        "CONFLUENCE_URL": "https://your-company.atlassian.net/wiki",
        "CONFLUENCE_USERNAME": "your.email@company.com",
        "CONFLUENCE_API_TOKEN": "your_api_token",
        "JIRA_URL": "https://your-company.atlassian.net",
        "JIRA_USERNAME": "your.email@company.com",
        "JIRA_API_TOKEN": "your_api_token"
      }
    }
  }
}
```

## Resources

> **Note:** The MCP server filters resources to only show Confluence spaces and Jira projects that the user is actively interacting with, based on their contributions and assignments.

- `confluence://{space_key}`: Access Confluence spaces
- `jira://{project_key}`: Access Jira projects

## Available Tools

| Tool | Description |
|------|-------------|
| `confluence_search` | Search Confluence content using CQL |
| `confluence_get_page` | Get content of a specific Confluence page |
| `confluence_get_page_children` | Get child pages of a specific Confluence page |
| `confluence_get_page_ancestors` | Get parent pages of a specific Confluence page |
| `confluence_get_comments` | Get comments for a specific Confluence page |
| `confluence_create_page` | Create a new Confluence page |
| `confluence_update_page` | Update an existing Confluence page |
| `confluence_delete_page` | Delete an existing Confluence page |
| `jira_get_issue` | Get details of a specific Jira issue |
| `jira_search` | Search Jira issues using JQL |
| `jira_get_project_issues` | Get all issues for a specific Jira project |
| `jira_create_issue` | Create a new issue in Jira |
| `jira_update_issue` | Update an existing Jira issue |
| `jira_delete_issue` | Delete an existing Jira issue |
| `jira_get_transitions` | Get available status transitions for a Jira issue |
| `jira_transition_issue` | Transition a Jira issue to a new status |
| `jira_add_worklog` | Add a worklog entry to a Jira issue |
| `jira_get_worklog` | Get worklog entries for a Jira issue |
| `jira_link_to_epic` | Link an issue to an Epic |
| `jira_get_epic_issues` | Get all issues linked to a specific Epic |

## Development & Debugging

### Local Development Setup

If you've cloned the repository and want to run a local version:

For Cloud:
```json
{
  "mcpServers": {
    "mcp-atlassian": {
      "command": "uv",
      "args": [
        "--directory", "/path/to/your/mcp-atlassian",
        "run", "mcp-atlassian",
        "--confluence-url=https://your-domain.atlassian.net/wiki",
        "--confluence-username=your.email@domain.com",
        "--confluence-token=your_api_token",
        "--jira-url=https://your-domain.atlassian.net",
        "--jira-username=your.email@domain.com",
        "--jira-token=your_api_token"
      ]
    }
  }
}
```

### Debugging Tools

```bash
# Using MCP Inspector
# For installed package
npx @modelcontextprotocol/inspector uvx mcp-atlassian ...

# For local development version
npx @modelcontextprotocol/inspector uv --directory /path/to/your/mcp-atlassian run mcp-atlassian ...

# View logs
tail -n 20 -f ~/Library/Logs/Claude/mcp*.log
```

## Security

- Never share API tokens
- Keep .env files secure and private
- See [SECURITY.md](https://github.com/sooperset/mcp-atlassian/blob/HEAD/SECURITY.md) for best practices

## License

Licensed under MIT - see [LICENSE](https://github.com/sooperset/mcp-atlassian/blob/HEAD/LICENSE) file. This is not an official Atlassian product.

**Official site: ** [https://github.com/sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `communication`
- Tags: `communication`, `developer tools`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `mcp-atlassian --confluence-url=https://your-company.atlassian.net/wiki --confluence-username=your.email@company.com --confluence-token=your_api_token --jira-url=https://your-company.atlassian.net --jira-username=your.email@company.com --jira-token=your_api_token`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/sooperset-atlassian.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
