---
title: "bing-cn-mcp-server"
description: "让 AI 助手（如 Claude）能够使用必应搜索引擎实时获取网络信息的工具。 MCP（Model Context Protocol）是一个让 AI 助手能够调用外部工具的协议。这个项目提供了一个必应搜索工具，让 AI 可以帮你搜索网络信息并返回结果。"
---

# bing-cn-mcp-server

让 AI 助手（如 Claude）能够使用必应搜索引擎实时获取网络信息的工具。 MCP（Model Context Protocol）是一个让 AI 助手能够调用外部工具的协议。这个项目提供了一个必应搜索工具，让 AI 可以帮你搜索网络信息并返回结果。

# Bing Chinese Search MCP Server

A tool that enables AI assistants (such as Claude) to fetch real-time web information using the Bing search engine.

## What is an MCP Server?

MCP (Model Context Protocol) is a protocol that allows AI assistants to call external tools. This project provides a Bing search tool, enabling AI to help you search for web information and return results.

## Features

- 🔍 **Real-time Search**: Use the Bing Chinese search engine to get the latest web information
- 📄 **Web Scraping**: Automatically scrape and extract content from search result pages
- 🌐 **Chinese Optimization**: Specifically optimized for Chinese searches, supporting Simplified Chinese results
- 🔒 **No API Key Required**: No need to apply for an API key, ready to use out of the box
- 🚫 **Intelligent Filtering**: Automatically filters out unscrapable websites (Zhihu, WeChat Official Accounts, etc.)

## Quick Start

### Using in Claude Desktop (Recommended)

#### Step 1: Open the Configuration File

Find and open the Claude Desktop configuration file based on your operating system:

**Windows Users**:
plaintext
%APPDATA%\Claude\claude_desktop_config.json

Copy the path above into the address bar of the File Explorer, then open the `claude_desktop_config.json` file with Notepad.

**macOS Users**:
plaintext
~/Library/Application Support/Claude/claude_desktop_config.json

In Finder, press `Cmd + Shift + G`, paste the path above, and then open the file with a text editor.

#### Step 2: Add Configuration

Add the following content to the configuration file (if the file is empty, just paste; if there is existing content, add it to the `mcpServers` section):

json
{
  "mcpServers": [
    {
      "name": "BingSearch",
      "url": "http://localhost:3000"
    }
  ]
}

Note, on Windows, you should configure it like this:

json
{
  "mcpServers": [
    {
      "name": "BingSearch",
      "url": "http://localhost:3000"
    }
  ]
}

If the configuration file already contains other MCP servers, it should look like this:

json
{
  "mcpServers": [
    {
      "name": "ExistingServer",
      "url": "http://existingserver.com"
    },
    {
      "name": "BingSearch",
      "url": "http://localhost:3000"
    }
  ]
}

#### Step 3: Restart Claude Desktop

Fully exit Claude Desktop (not just minimize, but completely close), then reopen it.

#### Step 4: Start Using

In Claude, you can ask questions like:

> "Help me search for the latest developments in artificial intelligence"

> "Search for Python asynchronous programming tutorials"

Claude will automatically call the Bing search tool and return the results.

## Tool Description

This MCP server provides two tools:

### 1. bing_search - Bing Search

Uses the Bing search engine to search for web information.

**Parameter Description**:
- `query` (required): Search keywords, e.g., "artificial intelligence"
- `count` (optional): Number of results to return, default is 10, maximum is 50
- `offset` (optional): The starting index of the results, used for pagination, default is 0

**Return Content**:
The search results include:
- Total number of search results
- Title, link, and summary of each result
- Formatted, readable content

### 2. crawl_webpage - Web Page Scraping

Scrapes and extracts the text content of a webpage (automatically skips inaccessible websites).

**Parameter Description**:
- `url` (required): The URL of the webpage to be scraped

**Return Content**:
- Webpage title
- Cleaned main content (automatically removes ads, navigation bars, etc.)

**Blacklisted Websites** (these sites will be automatically skipped):
- Zhihu (zhihu.com)
- Xiaohongshu (xiaohongshu.com)
- Weibo (weibo.com)
- WeChat Official Accounts (weixin.qq.com)
- Douyin/TikTok (douyin.com, tiktok.com)
- Bilibili (bilibili.com)
- CSDN (csdn.net)

## Usage Examples

### Example 1: Basic Search

**Question**: "Search for TypeScript tutorials"

**AI will call**: `bing_search` with parameters `{ "query": "TypeScript 教程" }`

**Returned Results**:
json
{
  "totalResults": 10,
  "results": [
    {
      "title": "TypeScript Tutorial - W3Schools",
      "link": "https://www.w3schools.com/typescript/",
      "summary": "Learn TypeScript with our comprehensive tutorial. Start from the basics and go all the way to advanced topics."
    },
    ...
  ]
}

### Example 2: Custom Result Count

**Question**: "Search for Node.js performance optimization, give me 20 results"

**AI will call**: `bing_search` with parameters `{ "query": "Node.js 性能优化", "count": 20 }`

### Example 3: Paginated Search

**Question**: "Search for React Hooks tutorials, start displaying from the 11th result"

**AI will call**: `bing_search` with parameters `{ "query": "React Hooks 教程", "offset": 10 }`

### Example 4: Scrape Web Page Content

**Question**: "Help me scrape the content of this webpage https://example.com/article"

**AI will call**: `crawl_webpage` with parameters `{ "url": "https://example.com/article" }`

## Technical Implementation

This project is built using the following technology stack:

- **MCP SDK** (`@modelcontextprotocol/sdk`): Implements the MCP protocol
- **Axios**: Sends HTTP requests
- **Cheerio**: Parses HTML pages- **Zod**: Parameter validation
- **TypeScript**: Type-safe development

### Project Structure

```

bingcnmcp/

├── src/

│   ├── index.ts         # MCP 服务器入口

│   ├── bingSearch.ts    # 必应搜索实现

│   ├── crawler.ts       # 网页抓取实现

│   ├── parser.ts        # HTML 解析器

│   ├── blacklist.ts     # 黑名单配置

│   └── types.ts         # 类型定义

├── build/               # 编译输出

├── package.json

└── tsconfig.json

```
## Frequently Asked Questions

### Why are the search results empty?

1. **Network Issues**: Check if you can access cn.bing.com normally.
2. **Keyword Issues**: Try using a different keyword or a more specific search term.
3. **Rate Limiting**: Searching too many times in a short period may result in being rate-limited by Bing. Wait a few minutes and try again.

### What if Claude does not call the search tool?

1. Ensure that the configuration file is correctly formatted (JSON format).
2. Make sure you have fully restarted Claude Desktop.
3. Try explicitly asking Claude to use the search: "Use the Bing search tool to find..."

### Some websites cannot be scraped for content

This is normal. Some websites (such as Zhihu, Xiaohongshu, etc.) are blacklisted due to access restrictions or anti-scraping mechanisms. The links to these websites will appear in the search results, but their content will not be automatically scraped.

### Windows system prompts that the npx command is not found

Ensure that Node.js (version 18 or higher recommended) is installed. After installation, restart your computer or the command line window.

Download Node.js: https://nodejs.org/

## Notes

1. **Network Requirements**: You need to be able to access `cn.bing.com`.
2. **Usage Frequency**: Do not search too frequently; it is recommended to wait at least 1-2 seconds between searches.
3. **Privacy Protection**: Search requests are sent directly to Bing, and this server does not store any search records.
4. **Stateless Design**: Each request is independent, and no cookies or session information are saved.
5. **For Reference Only**: This project is for learning and reference purposes only. Do not use it for illegal activities.
6. **Incorrect Results**: If the search results are incorrect, it might be due to triggering anti-scraping measures. For more stable needs, [tavily-mcp](https://github.com/tavily-ai/tavily-mcp) is recommended.

## License

[MIT](https://github.com/yan5236/bing-cn-mcp-server/blob/HEAD/LICENSE)

## Contributions

Feel free to submit bug reports and suggestions for improvements!

**Official site: ** [https://github.com/yan5236/bing-cn-mcp-server](https://github.com/yan5236/bing-cn-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `search`
- Tags: `search`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y bing-cn-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/slcatwujian-bing-cn.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
