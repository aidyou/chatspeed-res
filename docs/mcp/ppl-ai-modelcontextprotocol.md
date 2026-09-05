---
title: "modelcontextprotocol"
description: "A MCP server implementation that integrates the Sonar API, providing Claude with unparalleled real-time, full-network research capabilities."
---

# modelcontextprotocol

A MCP server implementation that integrates the Sonar API, providing Claude with unparalleled real-time, full-network research capabilities.

# Perplexity Ask MCP Server

An MCP server implementation that integrates with the Sonar API, providing unparalleled real-time web research capabilities for Claude.

## Tools

- **perplexity_ask**
  - Performs real-time web searches by conversing with the Sonar API.
  - **Inputs:**
    - `messages` (array): An array of conversation messages.
      - Each message must include:
        - `role` (string): The role of the message (e.g., `system`, `user`, `assistant`).
        - `content` (string): The content of the message.

## Configuration

### Step One: 

Clone this repository:

```bash

git clone git@github.com:ppl-ai/modelcontextprotocol.git

```
Navigate to the `perplexity-ask` directory and install the necessary dependencies:

```bash

cd modelcontextprotocol/perplexity-ask && npm install

```
### Step Two: Obtain a Sonar API Key

1. Register for a [Sonar API account](https://docs.perplexity.ai/guides/getting-started).
2. Follow the account setup instructions to generate your API key from the developer dashboard.
3. Set the API key as `PERPLEXITY_API_KEY` in your environment variables.

### Step Three: Configure Claude Desktop

1. Download Claude Desktop [here](https://claude.ai/download).

2. Add the following to your `claude_desktop_config.json` file:

```json

{

  "mcpServers": {

    "perplexity-ask": {

      "command": "docker",

      "args": [

        "run",

        "-i",

        "--rm",

        "-e",

        "PERPLEXITY_API_KEY",

        "mcp/perplexity-ask"

      ],

      "env": {

        "PERPLEXITY_API_KEY": "YOUR_API_KEY_HERE"

      }

    }

  }

}

```
### NPX

```json

{

  "mcpServers": {

    "perplexity-ask": {

      "command": "npx",

      "args": [

        "-y",

        "server-perplexity-ask"

      ],

      "env": {

        "PERPLEXITY_API_KEY": "YOUR_API_KEY_HERE"

      }

    }

  }

}

```
You can access the file using the following command:

```bash

vim ~/Library/Application\ Support/Claude/claude_desktop_config.json

```
### Step Four: Build Docker Image

Docker build command:

```bash

docker build -t mcp/perplexity-ask:latest -f Dockerfile .

```
### Step Five: Testing

Let's make sure that Claude Desktop has recognized the two tools we exposed in the `perplexity-ask` server. You can confirm this by looking for the hammer icon:

After clicking on the hammer icon, you should see the tools provided by the Filesystem MCP server:

If you see these two tools, it means the integration is active. Congratulations! This means Claude can now use Perplexity. You can then use it just like the Perplexity web application.

### Step Six: Advanced Parameters

The search parameters currently in use are the defaults. You can modify any of the search parameters directly in the API call within the `index.ts` script. For this, refer to the official [API documentation](https://docs.perplexity.ai/api-reference/chat-completions).

### Troubleshooting

The Claude documentation provides an excellent [troubleshooting guide](https://modelcontextprotocol.io/docs/tools/debugging) that you can refer to. However, if you need additional support or to [report a bug](https://github.com/ppl-ai/api-discussion/issues), you can still reach out to us at api@perplexity.ai.

## License

This MCP server is released under the MIT License. This means you are free to use, modify, and distribute the software, subject to the terms and conditions of the MIT License. For more details, please see the LICENSE file in the project repository.

**Official site: ** [https://github.com/ppl-ai/modelcontextprotocol](https://github.com/ppl-ai/modelcontextprotocol)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `search`
- Tags: `search`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y server-perplexity-ask`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/ppl-ai-modelcontextprotocol.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
