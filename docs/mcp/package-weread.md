---
title: "mcp-server-weread"
description: "A tool that provides MCP (Model Context Protocol) services for WeChat Reading, enabling the sharing of books, notes, and highlighted text from WeChat Reading with large language model clients that sup…"
---

# mcp-server-weread

A tool that provides MCP (Model Context Protocol) services for WeChat Reading, enabling the sharing of books, notes, and highlighted text from WeChat Reading with large language model clients that sup…

# WeChat Reading MCP Server

A tool that provides MCP (Model Context Protocol) services for WeChat Reading, enabling you to share books, notes, and highlights from WeChat Reading with MCP-capable LLM clients such as Claude Desktop.

## Features

- Get bookshelf information from WeChat Reading
- Search books in the bookshelf
- Get notes and highlights for a book
- Organize notes and highlights by chapter
- Seamless integration with MCP-capable LLM clients

## Main Tools

1. **get_bookshelf** - Get all books on the user's bookshelf
   - Returns basic book info including title, author, translator, and category

2. **search_books** - Search the user's bookshelf by keyword
   - Supports fuzzy and exact matching
   - Optionally includes detailed info
   - Configurable maximum result count

3. **get_book_notes_and_highlights** - Get all highlights and notes for a specific book
   - Supports organizing results by chapter
   - Supports filtering by highlight style
   - Returns structured data for easy LLM understanding

## Installation & Usage

### Prerequisites

- Node.js 16.x or later
- A WeChat Reading account with a valid Cookie

### Installation Guide

See: [Weread MCP Server Usage Guide](https://chenge.ink/article/post20250505)

### Integration with Claude Desktop

There are several ways to integrate with Claude Desktop:

#### Method 1: Via npx (simplest, recommended)
1. Open Claude Desktop
2. Go to Settings -> MCP Configuration
3. Add a tool using the following JSON config:
```json
   {
     "mcpServers": {
       "mcp-server-weread": {
         "command": "npx",
         "args": ["-y", "mcp-server-weread"],
         "env": {
           // Method 1: Use Cookie Cloud (recommended)
           "CC_URL": "https://cc.chenge.ink",  // Cookie Cloud URL
           "CC_ID": "YOUR_ID",                 // Cookie Cloud ID
           "CC_PASSWORD": "YOUR_PASSWORD"      // Cookie Cloud password

           // Or Method 2: Provide the cookie directly
           // "WEREAD_COOKIE": "YOUR_WEREAD_COOKIE"
         }
       }
     }
   }
```

#### Method 2: Global install

1. Install the package globally:
```bash
   npm install -g mcp-server-weread
```

2. Use it in the Claude config:
```json
   {
     "mcpServers": {
       "mcp-server-weread": {
         "command": "mcp-server-weread",
         "env": {
           // Configure the environment variables as above
         }
       }
     }
   }
```

> Tip: providing environment variables directly in the Claude config is more convenient - no .env file is needed. Recommended.

## CookieCloud Configuration
To avoid cookies expiring frequently and needing to re-fetch and update environment variables, this project supports the [CookieCloud](https://github.com/easychen/CookieCloud) service to sync and update cookies automatically. CookieCloud is an open-source cross-browser cookie sync tool that supports self-hosted servers.

### Configuration steps:
Install the browser extension
Edge Store: [CookieCloud for Edge](https://microsoftedge.microsoft.com/addons/detail/cookiecloud/bffenpfpjikaeocaihdonmgnjjdpjkeo)
Chrome Web Store: [CookieCloud for Chrome](https://chromewebstore.google.com/detail/cookiecloud/ffjiejobkoibkjlhjnlgmcnnigeelbdl)

### Configure the CookieCloud extension
Server address: use the default server https://cc.chenge.ink or enter your self-hosted server address
Click "Auto-generate password"
Enter "weread" in the sync domain keywords field
Click "Save", then click "Manual sync" to make sure the configuration takes effect
[Optional] To keep the extension alive automatically, you can enter https://weread.qq.com in the keepalive field; the extension will refresh the cookies automatically

Configure the CookieCloud variables in the MCP JSON:
CC_URL=your CookieCloud server address (or use the default server address https://cc.chenge.ink)
CC_ID=your CookieCloud user UUID
CC_PASSWORD=your CookieCloud password
Note: after configuring CookieCloud, the system will prefer getting the cookie from CookieCloud; it only falls back to the WEREAD_COOKIE environment variable if that fails.

## How to get the Cookie
You can get your WeChat Reading cookie as follows:
1. Log in to the [WeChat Reading web version](https://weread.qq.com/) in Chrome
2. Press F12 to open the developer tools and switch to the Network tab
3. Refresh the page and find a request to weread.qq.com in the request list
4. Find the Cookie field in Headers and copy its full content
5. Add the copied content to the WEREAD_COOKIE variable in the MCP JSON or .env file

## Usage Examples
Here are some example LLM conversations:

**Get bookshelf info**
```
User: Help me view my WeChat Reading bookshelf
LLM: I will fetch your WeChat Reading bookshelf info.
[LLM calls the get_bookshelf tool]
I retrieved 208 books from your WeChat Reading bookshelf. Here are some of them:
1. The Hidden Self - David Eagleman
2. Thinking, Fast and Slow - Daniel Kahneman
3. Sapiens: A Brief History of Humankind - Yuval Noah Harari
...
```

**Search for a specific book**
```
User: Help me find books about psychology
LLM: I will search your bookshelf for psychology-related books.
[LLM calls the search_books tool with keyword="psychology"]
I found 3 psychology-related books on your bookshelf:
1. Thinking, Fast and Slow - Daniel Kahneman (progress: 75%)
2. The Crowd - Gustave Le Bon (progress: 50%)
3. Psychology and Life - Richard Gerrig (progress: 30%)
Which book would you like to learn more about?
```

**Get notes and highlights**
```
User: Help me organize my notes on Thinking, Fast and Slow
LLM: I will get the notes and highlights for Thinking, Fast and Slow.
[LLM calls the search_books tool and finds the book ID]
[LLM calls the get_book_notes_and_highlights tool]
Here are your notes and highlights in Thinking, Fast and Slow (organized by chapter):

Chapter 1: Two Systems
- Highlight: "System 1 operates automatically and quickly, with little or no effort and no sense of voluntary control."
- Your note: "System 1 handles intuition and fast judgments; System 2 handles slow, deliberate reasoning."

Chapter 3: Anchoring Effect
- Highlight: "The anchoring effect refers to the tendency to rely too heavily on an initial piece of information when making estimates in uncertain situations."
...
```

## License

MIT

## Contributing

Pull requests and issues are welcome to improve this project.

**Official site: ** [https://www.npmjs.com/package/mcp-server-weread?activeTab=readme](https://www.npmjs.com/package/mcp-server-weread?activeTab=readme)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `memory`
- Tags: `knowledge and memory`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y mcp-server-weread`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/package-weread.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
