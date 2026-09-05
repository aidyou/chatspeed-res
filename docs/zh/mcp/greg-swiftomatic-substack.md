---
title: "Greg-Swiftomatic"
description: "Substack MCP 一个用于将Substack API与Claude及其他AI助手集成的MCP（Model Context Protocol）服务器。 概述 本项目实现了一个模型上下文协议（MCP）服务器，使像Claude这样的AI助手能够通过标准化接口与Substack的通讯、帖子和作者进行交互。它利用了Substack API库，并通过MCP提供其功能。 借助这个MCP服务器，Claud…"
---

# Greg-Swiftomatic

Substack MCP 一个用于将Substack API与Claude及其他AI助手集成的MCP（Model Context Protocol）服务器。 概述 本项目实现了一个模型上下文协议（MCP）服务器，使像Claude这样的AI助手能够通过标准化接口与Substack的通讯、帖子和作者进行交互。它利用了Substack API库，并通过MCP提供其功能。 借助这个MCP服务器，Claud…

# Substack MCP

An MCP (Model Context Protocol) server for Substack API integration with Claude and other AI assistants.

## Overview

This project implements a Model Context Protocol (MCP) server that enables AI assistants like Claude to interact with Substack newsletters, posts, and authors through a standardized interface. It leverages the [Substack API library](https://github.com/NHagar/substack_api) and makes its functionality available through MCP.

With this MCP server, Claude can:
- Retrieve newsletter posts, podcasts, and recommendations
- Get post content and metadata
- Search for posts within newsletters
- Get user profile information and subscriptions

## Installation

### Prerequisites

- Python 3.10 or higher
- [Claude for Desktop](https://claude.ai/download) (for testing)

### Setup

1. Clone this repository:
```bash
   git clone https://github.com/Greg-Swiftomatic/substack-mcp.git
   cd substack-mcp
```

2. Set up a virtual environment using `uv`:
```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh  # Install uv if not already installed
   uv init .
   uv venv
   source .venv/bin/activate  # On Windows: .venvScriptsactivate
```

3. Install dependencies:
```bash
   uv add "mcp[cli]" substack-api
```

## Usage

### Running the Server

Run the MCP server:

```bash
python substack_mcp.py
```

### Configuring Claude for Desktop

1. Open Claude for Desktop s configuration file:
   - **macOS/Linux**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%Claudeclaude_desktop_config.json`

2. Add your server configuration:
```json
   {
       "mcpServers": {
           "substack": {
               "command": "uv",
               "args": [
                   "--directory",
                   "/ABSOLUTE/PATH/TO/substack-mcp",
                   "run",
                   "substack_mcp.py"
               ]
           }
       }
   }
```

3. Restart Claude for Desktop.

### Example Queries

Once configured, you can ask Claude questions like:
- "Show me recent posts from https://stratechery.com/"
- "What s the content of this post: https://stratechery.com/2023/the-ai-unbundling/"
- "Search for  AI  on https://stratechery.com/"
- "Who are the authors of https://stratechery.com/?"

## Available Tools

The server provides the following MCP tools:

| Tool | Description |
|------|-------------|
| `get_newsletter_posts` | Retrieves recent posts from a Substack newsletter |
| `get_post_content` | Gets the full content of a specific Substack post |
| `search_newsletter` | Searches for posts within a newsletter |
| `get_author_info` | Gets information about a Substack author |
| `get_newsletter_recommendations` | Gets recommended newsletters for a Substack publication |
| `get_newsletter_authors` | Gets authors of a Substack newsletter |

## Project Structure

- `substack_mcp.py` - The main MCP server implementation
- `examples/` - Example queries and responses
- `docker/` - Docker configuration for containerized deployment

## Development

To contribute to this project:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m  Add some amazing feature `)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Troubleshooting

If you encounter issues:

1. Check Claude s logs for errors:
```bash
   # macOS/Linux
   tail -n 20 -f ~/Library/Logs/Claude/mcp*.log
   
   # Windows
   type %APPDATA%ClaudeLogsmcp*.log
```

2. Verify your server builds and runs without errors:
```bash
   python substack_mcp.py
```

3. Make sure your `claude_desktop_config.json` file has the correct paths and syntax.

4. Try restarting Claude for Desktop completely.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Substack API](https://github.com/NHagar/substack_api) - The underlying library for Substack interactions
- [Model Context Protocol](https://modelcontextprotocol.io/) - Anthropic s protocol for standardized LLM integrations

**官方网站：** [https://github.com/greg-swiftomatic/substack-mcp](https://github.com/greg-swiftomatic/substack-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`art and culture`, `content management systems`, `search`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`--directory /ABSOLUTE/PATH/TO/substack-mcp run substack_mcp.py`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/greg-swiftomatic-substack.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
