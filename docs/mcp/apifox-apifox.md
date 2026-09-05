---
title: "apifox-mcp-server"
description: "A server that connects AI coding assistants like Cursor and Cline to Apifox API definitions, allowing developers to implement API interfaces through natural language commands."
---

# apifox-mcp-server

A server that connects AI coding assistants like Cursor and Cline to Apifox API definitions, allowing developers to implement API interfaces through natural language commands.

# Apifox MCP Server

With the Apifox MCP Server, you can use the API docs in your Apifox project as a data source for AI-coding IDE tools such as Cursor, so the AI can directly access the API documentation data of the corresponding project.

Developers can use the AI assistant to: generate or modify code based on API docs, search API doc content, and more. As for what bigger and more powerful things this API doc data can let the AI do, use your and your team's imagination :)

## How to Use

After installing and configuring the MCP, the Apifox MCP Server automatically reads the data of all API docs in the entire Apifox project and caches it locally. The AI can read the API documentation data of all endpoints in the project through MCP.

Just tell the AI what you want to do with the API docs, for example:

1. "Get the API docs via MCP, then generate the definition code for Product and its related models"
2. "Based on the API docs, add the few new fields from the API docs to the Product DTO"
3. "Add comments to every field of the Product class based on the API docs"
4. "Based on the API docs, generate all MVC code related to the /users endpoint"

Note: the API doc data is cached locally by default. If the data in Apifox has been updated, tell the AI to refresh the API doc data, otherwise the AI may not read the latest data.

## Installation

### Prerequisites

- Node.js environment installed (version >= 18; we recommend the latest LTS)
- Any MCP-capable IDE:
  - Cursor
  - VSCode + Cline plugin

### Installation steps

1. **Generate an Access Token in Apifox**
   a. Open Apifox, hover over the avatar in the top-right corner, and click "Account Settings -> API Access Token"
   b. Create a new API access token (see the help docs for details)
   c. Copy the API access token and replace the `YOUR_APIFOX_ACCESS_TOKEN` placeholder in the config below

2. **Get the Apifox project ID**
   a. Open the corresponding project in Apifox
   b. Click "Project Settings" in the left sidebar and copy the project ID on the "Basic Settings" page
   c. Copy the project ID and replace the `YOUR_PROJECT_ID` placeholder in the config below

3. **Configure the IDE**

Add the following JSON config to the IDE's MCP config file:

```json
{
  "mcpServers": {
    "API Docs": {
      "command": "npx",
      "args": [
        "-y",
        "apifox-mcp-server@latest",
        "--project-id=YOUR_PROJECT_ID"
      ],
      "env": {
        "APIFOX_ACCESS_TOKEN": "YOUR_APIFOX_ACCESS_TOKEN"
      }
    }
  }
}
```

If you are on Windows and the config above does not work, use the following:

```json
{
  "mcpServers": {
    "API Docs": {
      "command": "cmd",
      "args": [
        "/c",
        "npx",
        "-y",
        "apifox-mcp-server@latest",
        "--project-id=YOUR_PROJECT_ID"
      ],
      "env": {
        "APIFOX_ACCESS_TOKEN": "YOUR_APIFOX_ACCESS_TOKEN"
      }
    }
  }
}
```

- Cursor: add it to the global `~/.cursor/mcp.json` or the project-level `.cursor/mcp.json`
- Cline: open the Cline panel > MCP Server > Configure MCP Server

**Notes:**
1. Replace `YOUR_PROJECT_ID` and `YOUR_APIFOX_ACCESS_TOKEN` with your personal Apifox API access token and project ID.
2. It is recommended to name the MCP Server something containing "API Docs", like "API Docs" or "xxx API Docs", so the AI can more easily recognize the purpose of this MCP server. Names like "Apifox" or "Apifox MCP" are not recommended, as the AI has a harder time recognizing their purpose.
3. To use API docs from multiple projects, add multiple MCP Server entries in the config file (each with a different `YOUR_PROJECT_ID`), and name them "xxx API Docs".
4. If your team syncs the MCP config file to the code repository, we recommend removing `"APIFOX_ACCESS_TOKEN": "YOUR_APIFOX_ACCESS_TOKEN"` from the config and having each member configure an environment variable named APIFOX_ACCESS_TOKEN on their own machine, to avoid token leakage.
5. For users of the private deployment version, add the parameter `--apifox-api-base-url= ` to the IDE's MCP config file. Also, make sure the network can reach `www.npm.com` normally.
6. Besides Apifox projects, reading Swagger/OAS files directly is also supported: remove the `--project-id=YOUR_PROJECT_ID` parameter and add the `--oas= ` parameter. For example: `npx apifox-mcp-server --oas https://petstore.swagger.io/v2/swagger.json` or `npx apifox-mcp-server --oas ~/data/petstore/swagger.json`

## Help & Support

The Apifox MCP Server is still in beta. We welcome your suggestions and ideas. Join the beta group:

![QR Code](/mcp-assets/bf2b2189dfdd5ebdff711874b2ee0807.png)

**Official site: ** [https://github.com/apifox/apifox-mcp-server](https://github.com/apifox/apifox-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`, `browser`
- Tags: `developer tools`, `browser automation`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y apifox-mcp-server@latest --project-id=<project-id>`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/apifox-apifox.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
