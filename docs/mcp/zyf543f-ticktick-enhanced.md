---
title: "ticktick-mcp-enhanced"
description: "TickTick MCP Enhanced Version A Model Context Protocol (MCP) server that allows large language models to manage your TickTick to-do items. 🔗 API Documentation: TickTick Official OpenAPI --- 🛠️ Prerequ…"
---

# ticktick-mcp-enhanced

TickTick MCP Enhanced Version A Model Context Protocol (MCP) server that allows large language models to manage your TickTick to-do items. 🔗 API Documentation: TickTick Official OpenAPI --- 🛠️ Prerequ…

# TickTick MCP Enhanced Version

[![Python 3.10+](/mcp-assets/405b7b46d001e379991916d79670861b.svg)](https://www.python.org/downloads/) [![License: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://opensource.org/licenses/MIT)

A [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server that allows large language models to manage your TickTick to-do items.

🔗 **API Documentation**: [TickTick Official OpenAPI](https://developer.dida365.com/docs#/openapi)

---

## 🛠️ Prerequisites

- **Python 3.10+**
- [**uv**](https://github.com/astral-sh/uv) installed (recommended)
- A TickTick or TickTick account
- API credentials (Client ID, Client Secret)

## 🔑 Authentication Setup

Register an application at the [TickTick Developer Center](https://developer.dida365.com/manage) (for domestic users) or [TickTick Developer Center](https://developer.ticktick.com/manage).

1. Click on **"New App"**.
2. Save your **Client ID** and **Client Secret**.
3. Set up the **Redirect URI**:
   - **Recommended**: `http://localhost:8000/callback`.
   - _Custom_: If you change this, set the `TICKTICK_REDIRECT_URI` environment variable accordingly.

## 🚀 Quick Start

### 1. Clone the Repository

```bash

git clone https://github.com/Code-MonkeyZhang/ticktick-mcp-enhanced

cd ticktick-mcp-enhanced

```
### 2. Configure the MCP Client

Using **Claude Desktop** (`claude_desktop_config.json`) as an example:

```json

{

  "mcpServers": {

    "ticktick": {

      "command": "/path/to/uv",

      "args": [

        "run",

        "--directory",

        "/项目/的/绝对路径/ticktick-mcp-enhanced",

        "ticktick-mcp",

        "run"

      ],

      "env": {

        "TICKTICK_ACCOUNT_TYPE": "china", // "china" 或 "global" 选择你滴答清单账户的区域

        "TICKTICK_CLIENT_ID": "你的_client_id",

        "TICKTICK_CLIENT_SECRET": "你的_client_secret",

        "TICKTICK_REDIRECT_URI": "http://localhost:8000/callback", // 这里填写上一步中你在开发者平台注册的URL

        "MCP_LOG_ENABLE": "false" // 可选：开启MCP日志记录功能

      }

    }

  }

}

```
### 3. Authorize and Use

1. Restart your MCP client.
2. Ask the AI: "Show me my tasks for today."
3. **First-time authorization**: The AI will provide an authorization link. Click the link -> log in -> a page will pop up showing that the authorization is complete.
4. You can return to the LLM client and use this MCP to access TickTick.

> Your authorization token will be stored in `.ticktick_token.json` within the project folder.

## 🧰 Available Tools

This MCP exposes the following tools to your LLM client.

| Category  | Tool Name               | Function Description                           |
| :-------- | :--------------------- | :--------------------------------------------- |
| **Auth**  | `ticktick_status`      | Check the current connection and authorization status. |
|           | `start_authentication` | Generate a login link and start local callback listening. |
| **Lists** | `get_all_projects`     | Get all list items.                            |
|           | `get_project_info`     | View specific lists and their tasks.           |
|           | `create_project`       | Create a new project.                          |
|           | `delete_projects`      | Delete projects.                               |
| **Tasks** | `create_tasks`         | Create tasks (supports smart time recognition).|
|           | `update_tasks`         | Modify task title, content, date, or priority. |
|           | `complete_tasks`       | Mark tasks as completed.                       |
|           | `delete_tasks`         | Batch delete tasks.                            |
|           | `create_subtasks`      | Add subtasks to a task.                        |
| **Query** | `query_tasks`          | Advanced list query (supports date range, priority, search terms). |

## 📂 Project Structure

```text

ticktick-mcp-enhanced/

├── ticktick_mcp/

│   ├── src/

│   │   ├── server.py          # MCP 服务入口

│   │   ├── auth.py            # OAuth 逻辑与回调服务器

│   │   ├── tools/             # 各类工具实现

│   │   └── utils/             # 格式化与校验工具

│   └── __main__.py            # CLI 启动项

├── pyproject.toml             # 项目配置与依赖

└── README_en.md               # 英文文档

```

**Official site: ** [https://github.com/Code-MonkeyZhang/ticktick-mcp-enhanced](https://github.com/Code-MonkeyZhang/ticktick-mcp-enhanced)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `productivity`
- Tags: `calendar management`, `滴答清单`, `日程管理`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `/path/to/uv`
- Args: `run --directory /项目/的/绝对路径/ticktick-mcp-enhanced ticktick-mcp run`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/zyf543f-ticktick-enhanced.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
