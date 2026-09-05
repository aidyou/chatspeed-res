---
title: "promot-share-mcp-npx"
description: "Promot Share MCP Server is a standard MCP (Model Context Protocol) server that provides an AI prompt sharing platform for Cursor IDE, Tongyi Lingma, and Trae."
---

# promot-share-mcp-npx

Promot Share MCP Server is a standard MCP (Model Context Protocol) server that provides an AI prompt sharing platform for Cursor IDE, Tongyi Lingma, and Trae.

# Promot Share MCP Server

🤖 **Promot Share MCP Server** is a standard MCP (Model Context Protocol) server that provides an AI prompt sharing platform for the Cursor IDE.

## ✨ Features

- 🔍 **Intelligent Search** - Match the most relevant prompts based on the requirement description
- 📝 **View Details** - Get complete information of the prompt
- ✨ **Content Creation** - Share high-quality prompts with the community
- 👍 **Interactive Features** - Like, comment, and favorite prompts
- 📂 **Category Management** - 18+ professional category systems
- 🔒 **Security Authentication** - API Key authentication protection

## 🚀 Quick Start
The `api_key` needs to be created after registering and logging in at https://promot-share.zhangyx-v.cn. The registration and login process requires an activation code, which can be obtained by emailing zhangyx-vip@foxmail.com.

## 🔧 Cursor IDE Configuration

### Old Version of Cursor (Cannot Carry Request Headers)

Add the MCP server in the Cursor settings:

json
{
  "mcpServers": {
    "promot-share": {
      "command": "npx",
      "args": ["@zhangyx-v/promot-share-mcp-server"],
      "env": {
        "PROMOT_SHARE_API_URL": "https://promot-share.zhangyx-v.cn",
        "API_KEY": "your_api_key_here"
      }
    }
  }
}

### New Version of Cursor (Supports Request Headers)

You can directly connect to the original server using SSE:

json
{
  "mcpServers": {
    "promot-share": {
      "url": "https://promot-share.zhangyx-v.cn/sse",
      "headers": {
        "Authorization": "Bearer your_api_key_here"
      }
    }
  }
}

## 🛠️ Available Tools

### 🔍 search_prompts - Intelligent Search
Search for the most relevant prompts based on the requirement description

**Parameters:**
- `query` (required) - Search keyword or requirement description
- `category` (optional) - Prompt category
- `limit` (optional) - Number of results to return, default is 10
- `sortBy` (optional) - Sorting method: relevance/popularity/recent

**Example:**
 
Search for prompts related to "writing code comments"

### 📝 get_prompt_detail - Get Details
Get the complete information of a specified prompt

**Parameters:**
- `id` (required) - Prompt ID

### ✨ create_prompt - Create Prompt
Share a new prompt with the platform

**Parameters:**
- `title` (required) - Prompt title
- `chineseDesc` (required) - Chinese prompt content
- `englishDesc` (required) - English prompt content
- `category` (required) - Category
- `tags` (optional) - Array of tags

### 👍 like_prompt - Like/Unlike
Like or unlike a prompt

**Parameters:**
- `promptId` (required) - Prompt ID
- `action` (optional) - like/unlike, default is like

### 💬 comment_prompt - Add Comment
Add a comment and rating to a prompt

**Parameters:**
- `promptId` (required) - Prompt ID
- `content` (required) - Comment content
- `rating` (optional) - Rating from 1 to 5

## 📂 Supported Categories

- 💻 **Programming Development** - `programming`, `cursor`, `product`, `testing`
- ✍️ **Writing and Creativity** - `writing`, `article`, `creative`, `copywriting`
- 🤖 **AI Related** - `ai`, `ai-art`
- 💼 **Business and Workplace** - `business`, `marketing`, `enterprise`, `seo`
- 🎓 **Education and Academia** - `education`, `academic`
- 🧠 **Psychology and Social** - `psychology`, `philosophy`
- 🏠 **Life Scenarios** - `life`
- 🛠️ **Tool Assistance** - `tool`, `game`
- 📊 **Analysis and Evaluation** - `analysis`, `eval`
- 🌐 **Language Translation** - `language`
- 💰 **Finance and Investment** - `finance`, `doctor`
- 🎵 **Creative Entertainment** - `music`, `industry`, `social`

## 🐛 Troubleshooting

### Connection Failure
- Check if `PROMOT_SHARE_API_URL` is correct
- Verify that the API server is running
- Ensure that the network connection is normal

### Authentication Failure
- Check if `API_KEY` is correct
- Confirm that the API Key is valid and not expired
- Verify user permissions

### Timeout Error
- Increase the `REQUEST_TIMEOUT` value
- Check for network latency
- Ensure the server response is normal

## 🔗 Related Links

- [Promot Share WEB Platform Address](https://promot-share.zhangyx-v.cn/promots)

**Official site: ** [https://github.com/ZYX2018/promot-share-mcp-npx?tab=readme-ov-file](https://github.com/ZYX2018/promot-share-mcp-npx?tab=readme-ov-file)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `memory`, `communication`
- Tags: `developer tools`, `search`, `communication`, `knowledge and memory`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `@zhangyx-v/promot-share-mcp-server`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/zhangyx1619-promot-share-npx.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
