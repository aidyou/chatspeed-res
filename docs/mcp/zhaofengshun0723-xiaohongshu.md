---
title: "xiaohongshu-mcp"
description: "A tool for automating Xiaohongshu operations, including login, publishing content, searching, and getting recommendations. Supports the Model Context Protocol (MCP) and can be integrated with multiple…"
---

# xiaohongshu-mcp

A tool for automating Xiaohongshu operations, including login, publishing content, searching, and getting recommendations. Supports the Model Context Protocol (MCP) and can be integrated with multiple…

# xiaohongshu-mcp

MCP for xiaohongshu.com (Little Red Book).

- My blog post: [haha.ai/xiaohongshu-mcp](https://www.haha.ai/xiaohongshu-mcp)

## Star History

[![Star History Chart](/mcp-assets/7ff5ea12648cd650854ef8cf69c6f49e.svg)](https://www.star-history.com/#xpzouying/xiaohongshu-mcp&Timeline)

**Main features**

> Tip: click the feature title below to expand and view the video demo

1. Login and check login status

The first step is mandatory: Xiaohongshu requires login. You can check the current login status.

**Login demo:**

https://github.com/user-attachments/assets/8b05eb42-d437-41b7-9235-e2143f19e8b7

**Check login status demo:**

https://github.com/user-attachments/assets/bd9a9a4a-58cb-4421-b8f3-015f703ce1f9

2. Publish image-text content

Supports publishing image-text content to Xiaohongshu, including title, content description, and images. More publishing features will be supported later.

**Publish image-text post demo:**

https://github.com/user-attachments/assets/8aee0814-eb96-40af-b871-e66e6bbb6b06

3. Search content

Search Xiaohongshu content by keyword.

**Search posts demo:**

https://github.com/user-attachments/assets/03c5077d-6160-4b18-b629-2e40933a1fd3

4. Get the recommended feed

Get the recommended content list from the Xiaohongshu homepage.

**Get feed demo:**

https://github.com/user-attachments/assets/110fc15d-46f2-4cca-bdad-9de5b5b8cc28

5. Get post details (including interaction data and comments)

Get the complete details of a Xiaohongshu post, including:
- Post content (title, description, images, etc.)
- User info
- Interaction data (likes, favorites, shares, comment count)
- Comment list and sub-comments

**Important notes:**
- You need to provide the post ID and xsec_token (both parameters are required)
- These two parameters can be obtained from the feed list or search results
- You must log in before using this feature

**Get post details demo:**

https://github.com/user-attachments/assets/76a26130-a216-4371-a6b3-937b8fda092a

**Basic Xiaohongshu operations knowledge**

- **Title: (very important) Xiaohongshu requires titles of no more than 20 characters**
- Currently only image-text posting is supported: from the recommendation perspective, image-text posts get more traffic than plain text.
- (Low priority) Video and plain text support may be considered. 1. Personally I feel these two greatly increase operational complexity; 2. Their value in my use cases is low.
- Tags: coming soon.
- Based on my own practice, Xiaohongshu's daily posting limit should be **50 posts**.
- **(Very important) The same Xiaohongshu account is not allowed to log in on multiple web browsers** - if you log in with xiaohongshu-mcp, don't log in to the same account elsewhere in a browser, or it will "kick out" the current MCP login. You can use the mobile app to view your current account info.

**Risk notes**

1. This project is open-sourced based on another project of mine; the original project ran stably for over a year without any account bans, only occasional Cookie expiration requiring re-login.
2. I integrated it with Claude Code and ran stable automated operations for several weeks before open-sourcing it after verifying there were no issues.

This project is for learning purposes; all illegal use is prohibited.

**Practical results**

Day one: likes/favorites reached 999+,

Results after about a week

## 1. Usage Tutorial

### 1.1. Login

The first login is manual and saves Xiaohongshu's login state.

Run:

```bash
go run cmd/login/main.go
```

### 1.2. Start the MCP service

Start the xiaohongshu-mcp service.

```bash
# Default: headless mode, no browser UI
go run .

# Non-headless mode, with browser UI
go run . -headless=false
```

## 1.3. Verify MCP

```bash
npx @modelcontextprotocol/inspector
```

After running, open the red-marked link, configure the MCP inspector, enter `http://localhost:18060/mcp`, and click the `Connect` button.

After configuring the MCP inspector as above, click the `List Tools` button to view all Tools.

## 1.4. Publish with MCP

### Check login status

### Publish image-text content

The example uses a random image from https://unsplash.com/ for testing.

### Search content

Use the search feature to search Xiaohongshu content by keyword:

## 2. MCP Client Integration

This service supports the standard Model Context Protocol (MCP) and can be integrated with various MCP-capable AI clients.

### 2.1. Quick start

#### Start the MCP service

```bash
# Start the service (default headless mode)
go run .

# Or with UI mode
go run . -headless=false
```

The service runs at: `http://localhost:18060/mcp`

#### Verify the service status

```bash
# Test the MCP connection
curl -X POST http://localhost:18060/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"initialize","params":{},"id":1}'
```

#### Claude Code CLI integration

```bash
# Add an HTTP MCP server
claude mcp add --transport http xiaohongshu-mcp http://localhost:18060/mcp
```

### 2.2. Supported clients

Claude Code CLI

The official command-line tool, already shown in the quick start section above:

```bash
# Add an HTTP MCP server
claude mcp add --transport http xiaohongshu-mcp http://localhost:18060/mcp
```

Cursor

#### Configuration file approach

Create or edit the MCP config file:

**Project-level configuration** (recommended):
Create `.cursor/mcp.json` in the project root:

```json
{
  "mcpServers": {
    "xiaohongshu-mcp": {
      "url": "http://localhost:18060/mcp",
      "description": "Xiaohongshu content publishing service - MCP Streamable HTTP"
    }
  }
}
```

**Global configuration**:
Create `~/.cursor/mcp.json` in the user directory (same content).

#### Usage steps

1. Make sure the Xiaohongshu MCP service is running
2. After saving the config file, restart Cursor
3. In the Cursor chat, the tools should be automatically available
4. You can view the connected MCP tools via "Available Tools" in the chat UI

**Demo**

Plugin MCP integration:

Calling an MCP tool (e.g. checking login status):

VSCode

#### Method 1: Use the command palette

1. Press `Ctrl/Cmd + Shift + P` to open the command palette
2. Run the `MCP: Add Server` command
3. Choose the `HTTP` method.
4. Enter the address: `http://localhost:18060/mcp`, or change it to the corresponding server address.
5. Enter the MCP name: `xiaohongshu-mcp`.

#### Method 2: Edit the config file directly

**Workspace configuration** (recommended):
Create `.vscode/mcp.json` in the project root:

```json
{
  "servers": {
    "xiaohongshu-mcp": {
      "url": "http://localhost:18060/mcp",
      "type": "http"
    }
  },
  "inputs": []
}
```

**Check the configuration**:

1. Confirm the running status.
2. Check whether `tools` are detected correctly.

**Demo**

Using post content search as an example:

MCP Inspector

A debugging tool for testing MCP connections:

```bash
# Start MCP Inspector
npx @modelcontextprotocol/inspector

# Connect to http://localhost:18060/mcp in the browser
```

Usage steps:
- Use MCP Inspector to test the connection
- Test the Ping Server feature to verify the connection
- Check whether List Tools returns 4 tools

Other clients supporting HTTP MCP

Any client supporting the HTTP MCP protocol can connect to: `http://localhost:18060/mcp`

Basic config template:
```json
{
  "name": "xiaohongshu-mcp",
  "url": "http://localhost:18060/mcp",
  "type": "http"
}
```

### 2.3. Available MCP tools

After connecting, you can use the following MCP tools:

- `check_login_status` - checks the Xiaohongshu login status (no parameters)
- `publish_content` - publishes image-text content to Xiaohongshu (requires: title, content; optional: images, video)
- `list_feeds` - gets the Xiaohongshu homepage feed (no parameters)
- `search_feeds` - searches Xiaohongshu content (requires: keyword)

### 2.4. Usage examples

Publish content to Xiaohongshu with Claude Code:

```
Help me write a post and publish it to Xiaohongshu,
image: https://cn.bing.com/th?id=OHR.MaoriRock_EN-US6499689741_UHD.jpg&w=3840
image caption: "Maori rock carvings at Ngatoroirangi Mine Bay, Lake Taupo, New Zealand (c) Joppi/Getty Images"

Use xiaohongshu-mcp to publish it.
```

**Publish result:**

 alt="xiaohongshu-mcp publish result" width="400">

**Official site: ** [https://github.com/xpzouying/xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `communication`
- Tags: `communication`

## MCP Configuration

- Transport: `http`
- Command: ``
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/zhaofengshun0723-xiaohongshu.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
