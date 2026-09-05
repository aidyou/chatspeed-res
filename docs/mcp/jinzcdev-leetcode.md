---
title: "leetcode-mcp-server"
description: "LeetCode MCP server implementation for LeetCode API integration, enabling automated access to programming problems, user data, and contest information."
---

# leetcode-mcp-server

LeetCode MCP server implementation for LeetCode API integration, enabling automated access to programming problems, user data, and contest information.

# LeetCode MCP Server

[![NPM Version](/mcp-assets/57a43fd7978f102acad680227fbc0de3.svg)](https://www.npmjs.com/package/@jinzcdev/leetcode-mcp-server)
![English Doc](/mcp-assets/68c24c85add4de7cbad6d30f3eb783c6.svg)
[![NPM Downloads](/mcp-assets/de068c911d55aa9481bcfb2a2762f749.svg)](https://www.npmjs.com/package/@jinzcdev/leetcode-mcp-server)
![GitHub License](/mcp-assets/5816f652aa1f0cc4eedb21a2f733e09e.svg)
[![LeetCode MCP Server on Glama](/mcp-assets/28e1437ec27d2d1ef1d07333e1207ff8.svg)](https://glama.ai/mcp/servers/jinzcdev/leetcode-mcp-server)
[![Stars](/mcp-assets/174c2aade82e203ccf84fe481136977d.svg)](https://github.com/jinzcdev/leetcode-mcp-server)

LeetCode MCP Server is a service based on the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction), providing seamless integration with the LeetCode API for advanced automation and intelligent interaction with LeetCode programming problems, contests, solutions, and user data.

## Features

- 🌐 **Multi-site Support**: Supports both leetcode.com (global) and leetcode.cn (China) sites
- 🔌 **Dual Transport Modes**: Runs by default as a stdio process or in [Streamable HTTP](https://modelcontextprotocol.io/docs/concepts/transports) server mode, suitable for web integration scenarios
- 📊 **Problem Data Retrieval**: Fetches detailed problem descriptions, constraints, examples, official solutions, and user-submitted solutions
- 👤 **User Data Access**: Retrieves user profiles, submission history, and contest performance
- 🔒 **Private Data Access**: Creates and queries user notes, tracks problem-solving progress, and analyzes submission details (AC/WA reports)
- 🔍 **Advanced Search Functionality**: Filters problems by tags, difficulty levels, categories, and keywords
- 📅 **Daily Problem Access**: Easy access to the daily problem

## Prerequisites

1. Node.js (v20.x or higher)
2. (Optional) LeetCode session cookie for authorized API access

## Installation

```bash

# 从 npm 安装

npm install @jinzcdev/leetcode-mcp-server -g

# 使用中国站点配置运行（stdio 传输，默认）

npx -y @jinzcdev/leetcode-mcp-server --site cn

# 使用认证运行（访问私有数据）

npx -y @jinzcdev/leetcode-mcp-server --site cn --session 

# 以 Streamable HTTP 服务器模式运行

npx -y @jinzcdev/leetcode-mcp-server --transport http --port 3000 --site cn

```
Alternatively, you can clone the repository and run it locally:

```bash

# 克隆仓库

git clone https://github.com/jinzcdev/leetcode-mcp-server.git

# 导航到项目目录

cd leetcode-mcp-server

# 构建项目

npm install && npm run build

# 运行服务器（stdio 传输）

node build/index.js --site cn

# 或以 Streamable HTTP 服务器模式运行

node build/index.js --transport http --port 3000 --site cn

```
## Usage

The server supports two transport modes:

| Transport Mode | Description                                                                                                        |
| -------------- | ------------------------------------------------------------------------------------------------------------------ |
| `stdio` (default) | Standard input/output transport, suitable for local MCP clients                                                    |
| `http`         | [Streamable HTTP](https://modelcontextprotocol.io/docs/concepts/transports) transport, suitable for web integration and remote access                     |

### Command Line Arguments

| Argument      | Alias | Default Value | Description                                                              |
| ------------- | ------ | ------------- | ------------------------------------------------------------------------ |
| `--site`      | `-s`   | `global`      | LeetCode API site: `global` (leetcode.com) or `cn` (leetcode.cn)         |
| `--session`   | `-c`   | —             | LeetCode session cookie for authorized access                            |
| `--transport` | `-t`   | `stdio`       | Transport mode: `stdio` or `http`                                        |
| `--port`      | —      | `3000`        | HTTP service port (for Streamable HTTP only)                             |
| `--host`      | —      | `127.0.0.1`   | HTTP service host (for Streamable HTTP only)                             |
| `--endpoint`  | —      | `/mcp`        | HTTP endpoint path (for Streamable HTTP only)                            |

### MCP Client Configuration (stdio)

Add the following server configuration to your MCP client's configuration file:

#### Method 1: Using Environment Variables

```json

{

  "mcpServers": {

    "leetcode": {

      "command": "npx",

      "args": ["-y", "@jinzcdev/leetcode-mcp-server"],

      "env": {

        "LEETCODE_SITE": "cn",

        "LEETCODE_SESSION": ""

      }

    }

  }

}

```
#### Method 2: Using Command Line Arguments

```json

{

  "mcpServers": {

    "leetcode": {

      "command": "npx",

      "args": [

        "-y",

        "@jinzcdev/leetcode-mcp-server",

        "--site",

        "cn",

        "--session",

        ""

      ]

    }

  }

}

```
For the global LeetCode site, change the `--site` parameter to `global`.

> [!NOTE]
>
> The location and JSON structure of the configuration file may vary among different MCP clients. Some clients use an `mcp.servers` wrapper or a `type` field. Please refer to the documentation of the client you are using and adjust the example accordingly.

### MCP Client Configuration (Streamable HTTP)

First, start the server in HTTP mode:

```bash

npx -y @jinzcdev/leetcode-mcp-server --transport http --port 3000 --site cn

```
Then, connect to the server in your MCP client:

PLACEHOLDER_CODE_5To access authenticated APIs, pass the session cookie when starting the server:

```bash

npx -y @jinzcdev/leetcode-mcp-server --transport http --port 3000 --site cn --session 

```
> [!NOTE]
> Some MCP clients require specifying `"type": "http"` or `"type": "streamableHttp"` in addition to the `url` field. Please refer to the documentation of the client you are using for the correct HTTP transport configuration format.

> [!TIP]
>
> The service supports the following optional environment variables:
>
> - `LEETCODE_SITE`: LeetCode API endpoint (`global` or `cn`, default is `global`)
> - `LEETCODE_SESSION`: LeetCode session cookie for authorizing API access (default is empty)
> - `LEETCODE_TRANSPORT`: Transport mode (`stdio` or `http`, default is `stdio`)
> - `LEETCODE_HTTP_PORT`: Streamable HTTP service port (default is `3000`)
> - `LEETCODE_HTTP_HOST`: Streamable HTTP service host (default is `127.0.0.1`)
> - `LEETCODE_HTTP_ENDPOINT`: Streamable HTTP endpoint path (default is `/mcp`)
>
> **Priority Explanation**:
>
> When both command-line arguments and environment variables are specified, command-line arguments take precedence. For example:
>
> - If `LEETCODE_SITE=cn` is set but you run `leetcode-mcp-server --site global`, the server will use `global`.
> - If `LEETCODE_SESSION` exists but you provide `--session "new_cookie"`, the value from the command line will be used.

## Available Tools

### Problems

| Tool                     | Global | China | Requires Auth | Description                               |
| ------------------------ | :----: | :---: | :----------: | ----------------------------------------- |
| **get_daily_challenge**  |   ✅   |   ✅  |      ❌       | Get today's LeetCode daily challenge      |
| **get_problem**          |   ✅   |   ✅  |      ❌       | Get details of a specific LeetCode problem|
| **search_problems**      |   ✅   |   ✅  |      ❌       | Search LeetCode problems with filters     |

### User

| Tool                           | Global | China | Requires Auth | Description                         |
| ------------------------------ | :----: | :---: | :----------: | ----------------------------------- |
| **get_user_profile**           |   ✅   |   ✅  |      ❌       | Get LeetCode user profile information|
| **get_user_contest_ranking**   |   ✅   |   ✅  |      ❌       | Get user's contest ranking statistics|
| **get_recent_ac_submissions**  |   ✅   |   ✅  |      ❌       | Get user's recent accepted submissions|
| **get_recent_submissions**     |   ✅   |   ❌  |      ❌       | Get user's recent submission history |
| **get_user_status**            |   ✅   |   ✅  |      ✅       | Get user's current status           |
| **get_problem_submission_report** |   ✅   |   ✅  |      ✅       | Provide detailed submission analysis |
| **get_problem_progress**       |   ✅   |   ✅  |      ✅       | Get user's problem solving progress  |
| **get_all_submissions**        |   ✅   |   ✅  |      ✅       | Get paginated list of user submissions|

### Submission / Run

| Tool                | Global | China | Requires Auth | Description                              |
| ------------------- | :----: | :---: | :----------: | --------------------------------------- |
| **run_code**        |   ✅   |   ✅  |      ✅       | Run code and poll `/check/` until completion |
| **submit_solution** |   ✅   |   ✅  |      ✅       | Submit code and poll `/check/` until completion |

### Notes

| Tool             | Global | China | Requires Auth | Description                           |
| ---------------- | :----: | :---: | :----------: | ------------------------------------ |
| **search_notes** |   ❌   |   ✅  |      ✅       | Search user notes with filters       |
| **get_note**     |   ❌   |   ✅  |      ✅       | Get note for a specific problem by ID|
| **create_note**  |   ❌   |   ✅  |      ✅       | Create a new note for a specific problem |
| **update_note**  |   ❌   |   ✅  |      ✅       | Update an existing note with new content |

### Solutions| Tool                       | Global Site | China Site | Requires Authentication | Description                           |
| -------------------------- | :---------: | :--------: | :---------------------: | ------------------------------------ |
| **list_problem_solutions** |      ✅     |      ✅    |           ❌            | Get a list of community solution articles for a specific problem |
| **get_problem_solution**   |      ✅     |      ✅    |           ❌            | Get the full content of a specific solution article               |

## Tool Parameters

### Problems

- **get_daily_challenge** - Get today's LeetCode daily challenge and full details

  - No parameters required

- **get_problem** - Get details of a specific LeetCode problem

  - `titleSlug`: URL identifier of the problem (string, required)

- **search_problems** - Search LeetCode problems based on multiple filters
  - `category`: Problem category filter (string, optional, default: "all-code-essentials")
  - `tags`: List of topic tags to filter problems (array of strings, optional)
  - `difficulty`: Difficulty level filter (enum: "EASY", "MEDIUM", "HARD", optional)
  - `searchKeywords`: Keywords to search in the problem title and description (string, optional)
  - `limit`: Maximum number of problems to return (number, optional, default: 10)
  - `offset`: Number of problems to skip (number, optional)

### Users

- **get_user_profile** - Get profile information of a LeetCode user

  - `username`: LeetCode username (string, required)

- **get_user_contest_ranking** - Get contest ranking information of a user

  - `username`: LeetCode username (string, required)
  - `attended`: Whether to include only contests the user has attended (boolean, optional, default: true)

- **get_recent_submissions** - Get recent submissions of a user on the global LeetCode site

  - `username`: LeetCode username (string, required)
  - `limit`: Maximum number of submissions to return (number, optional, default: 10)

- **get_recent_ac_submissions** - Get recent accepted submissions of a user

  - `username`: LeetCode username (string, required)
  - `limit`: Maximum number of submissions to return (number, optional, default: 10)

- **get_user_status** - Get the status of the currently authenticated user

  - No parameters required

- **get_problem_submission_report** - Get detailed information about a specific submission

  - `id`: Numeric ID of the submission (number, required)

- **get_problem_progress** - Get the problem-solving status of the authenticated user

  - `offset`: Number of problems to skip (number, optional, default: 0)
  - `limit`: Maximum number of problems to return (number, optional, default: 100)
  - `questionStatus`: Filter by problem status (enum: "ATTEMPTED", "SOLVED", optional)
  - `difficulty`: Filter by difficulty levels (array of strings, optional)

- **get_all_submissions** - Get a paginated list of user submissions
  - `limit`: Maximum number of submissions to return (number, default: 20)
  - `offset`: Number of submissions to skip (number, default: 0)
  - `questionSlug`: Optional question identifier (string, optional)
  - `lang`: Programming language filter (string, optional, China site only)
  - `status`: Submission status filter (enum: "AC", "WA", optional, China site only)
  - `lastKey`: Pagination token for retrieving the next page (string, optional, China site only)

### Submissions / Runs

- **run_code** - Run code for a specified problem and wait for completion (requires authentication)

  - `titleSlug`: URL identifier of the problem (string, required)
  - `lang`: Programming language (string enum, required)
  - `typedCode`: Source code to run (string, required)
  - `dataInput`: Custom input for the run (string, optional)
  - `timeoutMs`: Polling timeout in milliseconds (number, optional, default: 120000)
  - `pollIntervalMs`: Polling interval in milliseconds (number, optional, default: 1500)

- **submit_solution** - Submit code for a specified problem and wait for completion (requires authentication)

  - `titleSlug`: URL identifier of the problem (string, required)
  - `lang`: Programming language (string enum, required)
  - `typedCode`: Source code to submit (string, required)- `timeoutMs`: Polling timeout in milliseconds (number, optional, default: 120000)
- `pollIntervalMs`: Polling interval in milliseconds (number, optional, default: 1500)

### Notes

- **search_notes** - Search for user notes on LeetCode China

  - `keyword`: Keyword to filter the notes (string, optional)
  - `limit`: Maximum number of notes to return (number, optional, default: 10)
  - `skip`: Number of notes to skip (number, optional, default: 0)
  - `orderBy`: Order in which to return the notes (enum: "ASCENDING", "DESCENDING", optional, default: "DESCENDING")

- **get_note** - Get user notes for a specific LeetCode problem

  - `questionId`: The ID of the LeetCode problem (string, required)
  - `limit`: Maximum number of notes to return (number, optional, default: 10)
  - `skip`: Number of notes to skip (number, optional, default: 0)

- **create_note** - Create a new note for a specific LeetCode problem

  - `questionId`: The ID of the LeetCode problem (string, required)
  - `content`: Note content, supports markdown format (string, required)
  - `summary`: Optional short summary or title for the note (string, optional)

- **update_note** - Update an existing note with new content or summary
  - `noteId`: The ID of the note to update (string, required)
  - `content`: New content for the note, supports markdown format (string, required)
  - `summary`: Optional new short summary or title (string, optional)

### Solutions

- **list_problem_solutions** - Get a list of community solution articles for a specific problem

  - `questionSlug`: URL identifier of the problem (string, required)
  - `limit`: Maximum number of solution articles to return (number, optional, default: 10)
  - `skip`: Number of solution articles to skip (number, optional)
  - `userInput`: Keyword to filter the solution articles (string, optional)
  - `tagSlugs`: Array of tag identifiers to filter the solution articles (array of strings, optional, default: [])
  - `orderBy`: Sorting condition for the solution articles
    - Global site: enum: "HOT", "MOST_RECENT", "MOST_VOTES", optional, default: "HOT"
    - China site: enum: "DEFAULT", "MOST_UPVOTE", "HOT", "NEWEST_TO_OLDEST", "OLDEST_TO_NEWEST", optional, default: "DEFAULT"

- **get_problem_solution** - Get the full content of a specific solution article
  - `topicId`: Unique topic ID of the solution article (string, required, global site only)
  - `slug`: Unique identifier of the solution article (string, required, China site only)

## Available Resources

| Resource Name          | Global Site | China Site | Requires Authentication | Description                           |
| ---------------------- | :---------: | :--------: | :--------------------: | ------------------------------------- |
| **problem-categories** |      ✅     |      ✅    |           ❌            | List of all problem category types    |
| **problem-tags**       |      ✅     |      ✅    |           ❌            | Detailed collection of algorithm and data structure tags |
| **problem-langs**      |      ✅     |      ✅    |           ❌            | Complete list of supported programming languages |
| **problem-detail**     |      ✅     |      ✅    |           ❌            | Provides details for a specific problem |
| **problem-solution**   |      ✅     |      ✅    |           ❌            | Provides the full content of a specific solution article |

## Resource URIs

- **problem-categories** - List of all problem category types

  - URI: `categories://problems/all`

- **problem-tags** - Detailed collection of algorithm and data structure tags

  - URI: `tags://problems/all`

- **problem-langs** - Complete list of all programming languages supported by LeetCode

  - URI: `langs://problems/all`

- **problem-detail** - Provides details for a specific LeetCode problem

  - URI: `problem://{titleSlug}`
  - Parameters:
    - `titleSlug`: Identifier of the problem as shown in the LeetCode URL

- **problem-solution** - Provides the full content of a specific solution article
  - Global site URI: `solution://{topicId}`
    - Parameters:
      - `topicId`: Unique topic ID of the solution article
  - China site URI: `solution://{slug}`
    - Parameters:
      - `slug`: Unique identifier of the solution article

## Authentication

Access to user-specific data requires LeetCode session authentication:1. Log in to LeetCode ([Global Site](https://leetcode.com) or [China Site](https://leetcode.cn))
2. Extract the `LEETCODE_SESSION` cookie from the browser developer tools
3. Configure the server using the `--session` flag or the `LEETCODE_SESSION` environment variable

## Response Format

All tools return a JSON formatted response with the following structure:

json
```json
{
  "content": [
    {
      "type": "text",
      "text": "JSON_DATA_STRING"
    }
  ]
}
```
`JSON_DATA_STRING` contains the requested data or an error message for failed requests.

## License

This project is licensed under the MIT License.

**Official site: ** [https://github.com/jinzcdev/leetcode-mcp-server](https://github.com/jinzcdev/leetcode-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`, `memory`, `data`
- Tags: `research and data`, `knowledge and memory`, `developer tools`, `leetcode`, `编程`, `力扣`, `算法`, `数据结构`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @jinzcdev/leetcode-mcp-server --site cn`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/jinzcdev-leetcode.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
