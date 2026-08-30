---
title: "MCP Yahoo Finance 股票数据工具"
description: "一种模型上下文协议服务器，可通过自然语言查询与雅虎财经互动，以获取股票价格、公司信息和历史财务数据。"
---

# MCP Yahoo Finance 股票数据工具

一种模型上下文协议服务器，可通过自然语言查询与雅虎财经互动，以获取股票价格、公司信息和历史财务数据。

# MCP Yahoo Finance

一个用于与Yahoo Finance交互的[Model Context Protocol](https://modelcontextprotocol.io) (MCP) 服务器。该服务器提供了获取定价、公司信息等功能。

> 请注意，`mcp-yahoo-finance` 目前正处于早期开发阶段。随着我继续开发和改进服务器，其功能和可用工具可能会发生变化和扩展。

## 安装

如果你使用的是[`uv`](https://docs.astral.sh/uv/)，则无需手动安装`mcp-yahoo-finance`。我们将使用[`uvx`](https://docs.astral.sh/uv/guides/tools/)直接运行`mcp-yahoo-finance`。

如果你只是想使用MCP服务器，我建议你采用这种方法。

### 使用pip

使用`pip`。

```sh
pip install mcp-yahoo-finance
```

### 使用Git

您也可以在将仓库克隆到您的机器后安装该软件包。

```sh
git clone git@github.com:maxscheijen/mcp-yahoo-finance.git
cd mcp-yahoo-finance
uv sync
```

## 配置

### Claude Desktop

在你的`claude_desktop_config.json`中添加以下内容：

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
您还可以使用docker：

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

在你的`.vscode/mcp.json`中添加以下内容：

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

## 示例问题

1. "苹果公司的股价是多少？"
2. "苹果和谷歌之间的股价差额是多少？"
3. "从2024-01-01到2025-01-01，苹果公司的股价变化了多少？"

## 构建

Docker:

```sh
docker build -t [IMAGE] .
```

## 使用MCP Inspector测试

```sh
npx @modelcontextprotocol/inspector uv run mcp-yahoo-finance
```

**官方网站：** [https://github.com/maxscheijen/mcp-yahoo-finance](https://github.com/maxscheijen/mcp-yahoo-finance)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`finance`
- 标签：`finance`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`mcp-yahoo-finance`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/maxscheijen-yahoo-finance.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
