---
title: "jenkins-mcp"
description: "Enables managing Jenkins operations like listing jobs, triggering builds, and checking build statuses through a configurable MCP server."
---

# jenkins-mcp

Enables managing Jenkins operations like listing jobs, triggering builds, and checking build statuses through a configurable MCP server.

# Jenkins MCP
[Smithery](https://smithery.ai/server/@kjozsa/jenkins-mcp)
MCP server for managing Jenkins operations.

  

## Installation
### Installing via Smithery

To install Jenkins MCP for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@kjozsa/jenkins-mcp):

```bash
npx -y @smithery/cli install @kjozsa/jenkins-mcp --client claude
```

### Installing Manually
```bash
uvx install jenkins-mcp
```

## Configuration
Add the MCP server using the following JSON configuration snippet:

```json
{
  "mcpServers": {
    "jenkins-mcp": {
      "command": "uvx",
      "args": ["jenkins-mcp"],
      "env": {
        "JENKINS_URL": "https://your-jenkins-server/",
        "JENKINS_USERNAME": "your-username",
        "JENKINS_PASSWORD": "your-password",
        "JENKINS_USE_API_TOKEN": "false"
      }
    }
  }
}
```

## CSRF Crumb Handling

Jenkins implements CSRF protection using "crumbs" - tokens that must be included with POST requests. This MCP server handles CSRF crumbs in two ways:

1. **Default Mode**: Automatically fetches and includes CSRF crumbs with build requests
   - Uses session cookies to maintain the web session
   - Handles all the CSRF protection behind the scenes

2. **API Token Mode**: Uses Jenkins API tokens which are exempt from CSRF protection
   - Set `JENKINS_USE_API_TOKEN=true`
   - Set `JENKINS_PASSWORD` to your API token instead of password
   - Works with Jenkins 2.96+ which doesn't require crumbs for API token auth

You can generate an API token in Jenkins at: User → Configure → API Token → Add new Token

## Features
- List Jenkins jobs
- Trigger builds with optional parameters
- Check build status
- CSRF crumb handling for secure API access

## Development
```bash
# Install dependencies
uv pip install -r requirements.txt

# Run in dev mode with Inspector
mcp dev jenkins_mcp/server.py
```

**Official site: ** [https://github.com/kjozsa/jenkins-mcp](https://github.com/kjozsa/jenkins-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `developer tools`, `os automation`, `monitoring`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `jenkins-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/kjozsa-jenkins.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
