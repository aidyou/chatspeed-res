---
title: "模型上下文协议股票工具"
description: "一种模型上下文协议服务器，提供与雅虎财经互动的工具，允许用户检索股票价格、公司信息并进行财务数据比较。"
---

# 模型上下文协议股票工具

一种模型上下文协议服务器，提供与雅虎财经互动的工具，允许用户检索股票价格、公司信息并进行财务数据比较。

# MCP Yahoo Finance

A [Model Context Protocol](https://modelcontextprotocol.io) (MCP) server for Yahoo Finance interaction. This server provides tools to get pricing, company information and more.

> Please note that `mcp-yahoo-finance` is currently in early development. The functionality and available tools are subject to change and expansion as I continue to develop and improve the server.

## Installation

You don t need to manually install `mcp-yahoo-finance` if you use [`uv`](https://docs.astral.sh/uv/). We ll use [`uvx`](https://docs.astral.sh/uv/guides/tools/) to directly run `mcp-yahoo-finance`.

I would recommend using this method if you simply want to use the MCP server.

### Using pip

Using `pip`.

```sh
pip install mcp-yahoo-finance
```

### Using Git

You can also install the package after cloning the repository to your machine.

```sh
git clone git@github.com:maxscheijen/mcp-yahoo-finance.git
cd mcp-yahoo-finance
uv sync
```

## Configuration

### Claude Desktop

Add this to your `claude_desktop_config.json`:

```json
{
    "mcpServers": {
        "yahoo-finance": {
            "command": "uvx",
            "args": ["mcp-yahoo-finance"]
        }
    }
}
```
You can also use docker:

```json
{
    "mcpServers": {
        "yahoo-finance": {
            "command": "docker",
            "args": ["run", "-i", "--rm", "IMAGE"]
        }
    }
}
```

### VSCode

Add this to your `.vscode/mcp.json`:

```json
{
    "servers": {
        "yahoo-finance": {
            "command": "uvx",
            "args": ["mcp-yahoo-finance"]
        }
    }
}
```

## Examples of Questions

1. "What is the stock price of Apple?"
2. "What is the difference in stock price between Apple and Google?"
3. "How much did the stock price of Apple change between 2024-01-01 and 2025-01-01?"

## Build

Docker:

```sh
docker build -t [IMAGE] .
```

## Test with MCP Inspector

```sh
npx @modelcontextprotocol/inspector uv run mcp-yahoo-finance
```
## Acknowledgements

- Original project by [Max Scheijen](https://github.com/maxscheijen)

**官方网站：** [https://github.com/marckwei/no-use-tools](https://github.com/marckwei/no-use-tools)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`finance`
- 标签：`finance`, `search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`mcp-yahoo-finance`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/marckwei-no-use-tools.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
