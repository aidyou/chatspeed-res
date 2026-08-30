---
title: "MCP骰子服务器"
description: "一个启用LLM掷骰子的MCP服务器"
---

# MCP骰子服务器

一个启用LLM掷骰子的MCP服务器

# mcp-dice: 一个用于掷骰子的 MCP 服务器

[Smithery](https://smithery.ai/protocol/mcp-dice)
![截图](/mcp-assets/1b3508a9a643e1818fcec12c9672299d.png)

这是一个模型上下文协议 (MCP) 服务器，它使大型语言模型 (LLMs) 能够掷骰子。它接受标准的骰子表示法（例如 `1d20`），并返回单次掷骰的结果及其总和。

## 特性

- 支持标准骰子表示法（例如 `1d20`, `3d6`, `2d8+1`）
- 返回单次掷骰结果及总和
- 易于与 Claude Desktop 集成
- 兼容 MCP Inspector 以便调试

## 安装

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/protocol/mcp-dice) 自动为 Claude Desktop 安装 Dice Roller：

```bash
npx @smithery/cli install mcp-dice --client claude
```

使 `uv` 可用：[https://docs.astral.sh/uv/getting-started/installation/](https://docs.astral.sh/uv/getting-started/installation/)

## 使用方法

### 基本命令行使用

```shell
# Using uvx
uvx mcp-dice
```

### 输入格式

服务器接受带有 `notation` 字段的 JSON 对象：
```json
{
  "notation": "2d6+3"
}
```

示例响应：
```json
{
  "rolls": [
    3,
    1
  ],
  "sum": 4,
  "modifier": 3,
  "total": 7,
  "notation": "2d6+3",
  "timestamp": "2024-12-03T16:36:38.926452"
}
```

## Claude Desktop 配置

### 位置
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%/Claude/claude_desktop_config.json`

### 示例

macOS 配置

```json
{
  "mcpServers": {
    "dice": {
      "command": "uvx",
      "args": ["mcp-dice"]
    }
  }
}
```

WSL 配置

```json
{
  "mcpServers": {
    "dice": {
      "command": "wsl",
      "args": [
        "-e",
        "zsh",
        "-lc",
        "uvx mcp-dice"
      ]
    }
  }
}
```

注意：将 `zsh` 替换为您的登录 shell。

## 开发与调试

### 安装开发依赖项

```shell
# Clone the repository
git clone https://github.com/yourusername/mcp-dice
cd mcp-dice

# Install development dependencies
uv pip install -e ".[dev]"
```

### 运行测试

```shell
uv run pytest
```

### 使用 MCP Inspector

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) 是一个有用的工具，可用于调试您的 MCP 服务器。使用 npm 安装并运行它：

```shell
npx @modelcontextprotocol/inspector uvx mcp-dice
```

### 用于开发的 Claude Desktop 配置

macOS 配置（本地开发）

```json
{
  "mcpServers": {
    "dice": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "path/to/mcp-dice-repo",
        "mcp-dice"
      ]
    }
  }
}
```

注意：将 `path/to/mcp-dice-repo` 替换为您文件系统中仓库的实际路径。

Windows (WSL) 配置（本地开发）

```json
{
  "mcpServers": {
    "dice": {
      "command": "wsl",
      "args": [
        "-e",
        "zsh",
        "-lc",
        "uv run --directory path/to/mcp-dice-repo mcp-dice"
      ]
    }
  }
}
```

注意：将 `zsh` 替换为您的登录 shell。同时，将 `path/to/mcp-dice-repo` 替换为您 WSL 文件系统中仓库的实际路径。

**官方网站：** [https://github.com/yamaton/mcp-dice](https://github.com/yamaton/mcp-dice)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`productivity`
- 标签：`other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`wsl`
- 参数：`-e zsh -lc uvx mcp-dice`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/yamaton-dice.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
