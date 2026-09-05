---
title: "tavily-mcp"
description: "This server enables AI systems to integrate with Tavily's search and data extraction tools, providing real-time web information access and domain-specific searches."
---

# tavily-mcp

This server enables AI systems to integrate with Tavily's search and data extraction tools, providing real-time web information access and domain-specific searches.

# Tavily MCP Server

![GitHub Repo stars](/mcp-assets/2c43d86a5c7e70011ed1d24ae527b2d6.svg)
![npm](/mcp-assets/aafae7ed7f5b12a9b3239f7ddfe732e5.svg)

> **Compatible with [Cline](https://github.com/cline/cline), [Cursor](https://cursor.sh), [Claude Desktop](https://claude.ai/desktop), and any other MCP client!**
>
> Tavily MCP is also compatible with any MCP client.
>
> Tutorial on [integrating Tavily MCP with the Neo4j MCP server](https://medium.com/@dustin_36183/building-a-knowledge-graph-assistant-combining-tavily-and-neo4j-mcp-servers-with-claude-db92de075df9)!
>
> [Tutorial](https://medium.com/@dustin_36183/connect-your-coding-assistant-to-the-web-integrating-tavily-mcp-with-cline-in-vs-code-5f923a4983d1) for integrating Tavily MCP with Cline in VS Code (demo + example use cases)

The Model Context Protocol (MCP) is an open standard that enables AI systems to interact seamlessly with a variety of data sources and tools, facilitating secure bidirectional connections.

Developed by Anthropic, the Model Context Protocol (MCP) allows AI assistants like Claude to seamlessly integrate Tavily's advanced search and data extraction capabilities. This integration provides real-time access to web information, with sophisticated filtering options and domain-specific search functionalities.

Tavily MCP Server offers:
- Seamless interaction with the tavily-search and tavily-extract tools
- Real-time web search capabilities via the tavily-search tool
- Intelligent data extraction from web pages using the tavily-extract tool

## Prerequisites

Before you begin, make sure you have the following:

- [Tavily API key](https://app.tavily.com/home)
  - If you don't have a Tavily API key yet, you can sign up for a free account [here](https://app.tavily.com/home)
- [Claude Desktop](https://claude.ai/download) or [Cursor](https://cursor.sh)
- [Node.js](https://nodejs.org/) (v20 or higher)
  - You can verify your Node.js installation by running the following command:
    - `node --version`
- [Git](https://git-scm.com/downloads) installed (only required if using the Git installation method)
  - On macOS: `brew install git`
  - On Linux:
    - Debian/Ubuntu: `sudo apt install git`
    - RedHat/CentOS: `sudo yum install git`
  - On Windows: Download [Git for Windows](https://git-scm.com/download/win)

## Tavily MCP Server Installation

### Run with NPX

```bash
npx -y tavily-mcp@0.1.4
```

### Install via Smithery

To automatically install the Tavily MCP Server for Claude Desktop via [Smithery](https://smithery.ai/server/@tavily-ai/tavily-mcp):

```bash
npx -y @smithery/cli install @tavily-ai/tavily-mcp --client claude
```

While you can start the server standalone, it is not particularly useful in isolation. Instead, you should integrate it into an MCP client. Below is an example of how to configure the Claude Desktop application to work with the tavily-mcp server.

## Configure MCP Client

This repository explains how to configure [Cursor](https://cursor.sh) and [Claude Desktop](https://claude.ai/desktop) to work with the tavily-mcp server.

### Configure Cline

The easiest way to set up the Tavily MCP Server in Cline is through a one-click install from the marketplace:

1. Open Cline in VS Code
2. Click on the Cline icon in the sidebar
3. Navigate to the "MCP Servers" tab (icon with four squares)
4. Search for "Tavily" and click "Install"
5. When prompted, enter your Tavily API key

Alternatively, you can manually set up the Tavily MCP Server in Cline:

1. Open the Cline MCP settings file:

   ### For macOS:
```bash
   # Using Visual Studio Code
   code ~/Library/Application\ Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json

   # Or using TextEdit
   open -e ~/Library/Application\ Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json
```

   ### For Windows:
```bash
   code %APPDATA%\Code\User\globalStorage\saoudrizwan.claude-dev\settings\cline_mcp_settings.json
```

2. Add the Tavily server configuration to the file:

   Replace `your-api-key-here` with your actual [Tavily API key](https://tavily.com/api-keys).

```json
   {
     "mcpServers": {
       "tavily-mcp": {
         "command": "npx",
         "args": ["-y", "tavily-mcp@0.1.4"],
         "env": {
           "TAVILY_API_KEY": "your-api-key-here"
         },
         "disabled": false,
         "autoApprove": []
       }
     }
   }
```

3. Save the file. If Cline is already running, restart it.

4. When using Cline, you can now access the Tavily MCP tools. You can directly ask Cline to use the tavily-search and tavily-extract tools in the conversation.

### Configure Cursor

> **Note**: Requires Cursor version 0.45.6 or higher

To set up the Tavily MCP Server in Cursor:

1. Open Cursor settings
2. Navigate to Features > MCP Servers
3. Click the "+ Add New MCP Server" button
4. Fill in the following information:
   - **Name**: Enter a nickname for the server (e.g., "tavily-mcp")
   - **Type**: Select "command" as the type
   - **Command**: Enter the command to run the server:
```bash
     env TAVILY_API_KEY=your-api-key npx -y tavily-mcp@0.1.4
```
     > **Important**: Replace `your-api-key` with your Tavily API key. You can get one at [app.tavily.com/home](https://app.tavily.com/home).

After adding the server, it should appear in the MCP server list. You may need to manually click the refresh button in the upper right corner of the MCP server to populate the tool list.

The Composer Agent will automatically use the Tavily MCP tools based on your query. It's best to explicitly request the use of these tools by describing what you want to do (e.g., "Use tavily-search to find the latest news about AI"). On a Mac, press command + L to open the chat interface, select the composer option at the top of the screen, then select agent next to the submit button and submit your query when ready.

### Configuring the Claude Desktop App

### For macOS:

```bash
# Create the config file if it doesn't exist
touch "$HOME/Library/Application Support/Claude/claude_desktop_config.json"

# Opens the config file in TextEdit
open -e "$HOME/Library/Application Support/Claude/claude_desktop_config.json"

# Alternative method using Visual Studio Code (requires VS Code to be installed)
code "$HOME/Library/Application Support/Claude/claude_desktop_config.json"
```

### For Windows:
```bash
code %APPDATA%\Claude\claude_desktop_config.json
```

### Adding Tavily Server Configuration:

Replace `your-api-key-here` with your actual [Tavily API key](https://tavily.com/api-keys).

```json
{
  "mcpServers": {
    "tavily-mcp": {
      "command": "npx",
      "args": ["-y", "tavily-mcp@0.1.2"],
      "env": {
        "TAVILY_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

### 2. Git Installation

1. Clone the repository:
```bash
git clone https://github.com/tavily-ai/tavily-mcp.git
cd tavily-mcp
```

2. Install dependencies:
```bash
npm install
```

3. Build the project:
```bash
npm run build
```

### Configuring the Claude Desktop App

Follow the configuration steps outlined in the [Configuring the Claude Desktop App](#configuring-the-claude-desktop-app) section above, using the JSON configuration below.

Replace `your-api-key-here` with your actual [Tavily API key](https://tavily.com/api-keys), and replace `/path/to/tavily-mcp` with the actual path where you cloned the repository on your system.

```json
{
  "mcpServers": {
    "tavily": {
      "command": "npx",
      "args": ["/path/to/tavily-mcp/build/index.js"],
      "env": {
        "TAVILY_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

## Usage in the Claude Desktop App

After installation and configuring the Claude Desktop App, you must fully close and reopen the Claude Desktop App to see the tavily-mcp server. You should see a hammer icon in the lower left corner of the app, indicating available MCP tools; you can click the hammer icon for more information about the tavily-search and tavily-extract tools.

Now, Claude will have full access to the tavily-mcp server, including the tavily-search and tavily-extract tools. If you insert the following example into the Claude Desktop App, you should be able to see the effect of the tavily-mcp server tools.

### Tavily Search Examples

1. **General Web Search**:
```
Can you search for recent developments in quantum computing?
```

2. **News Search**:
```
Search for news articles about AI startups from the last 7 days.
```

3. **Domain-Specific Search**:
```
Search for climate change research on nature.com and sciencedirect.com
```

### Tavily Extraction Examples

1. **Extract Article Content**:
```
Extract the main content from this article: https://example.com/article
```

### Combining Search and Extraction

You can also combine the use of the tavily-search and tavily-extract tools to perform more complex tasks.

```
Search for news articles about AI startups from the last 7 days and extract the main content from each article to generate a detailed report.
```

## Troubleshooting

### Common Issues

1. **Server Not Found**
   - Verify npm installation by running `npm --version`.
   - Check the Claude Desktop configuration syntax by running `code ~/Library/Application\ Support/Claude/claude_desktop_config.json`.
   - Ensure Node.js is correctly installed by running `node --version`.

2. **NPX Related Issues**
  - If you encounter errors related to `npx`, you might need to use the full path to the npx executable.
  - You can find this path by running `which npx` in the terminal, then replace the line `"command": "npx"` in the configuration with `"command": "/full/path/to/npx"`.

3. **API Key Issues**
   - Confirm that your Tavily API key is valid.
   - Check that the API key is set correctly in the configuration.
   - Ensure there are no spaces or quotes around the API key.

## Acknowledgements

- [Model Context Protocol](https://modelcontextprotocol.io) provided the MCP specification.
- [Anthropic](https://anthropic.com) provided the Claude Desktop.

**Official site: ** [https://github.com/tavily-ai/tavily-mcp](https://github.com/tavily-ai/tavily-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `search`, `browser`
- Tags: `search`, `browser automation`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y tavily-mcp@0.1.4`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/tavily-ai-tavily.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
