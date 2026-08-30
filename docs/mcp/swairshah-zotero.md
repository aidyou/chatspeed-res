---
title: "Zotero MCP 服务端"
description: "一个服务器，它使像Anthropic Claude App这样的MCP客户端能够与本地Zotero图书馆互动，允许用户通过自然语言搜索论文、管理笔记和访问研究资料。"
---

# Zotero MCP 服务端

一个服务器，它使像Anthropic Claude App这样的MCP客户端能够与本地Zotero图书馆互动，允许用户通过自然语言搜索论文、管理笔记和访问研究资料。

# Zotero MCP 服务器

一个MCP（模型上下文协议）服务器，可以让您的MCP客户端（例如Anthropic Claude应用程序、Goose，可能还包括vscode Cline）与您的本地Zotero库进行交互。此服务器允许程序化访问您的Zotero图书馆，使您能够搜索论文、管理笔记等。

## 设置

1. 安装依赖项：
```bash
pip install -e .
```

2. 在根目录下创建一个包含您的Zotero凭据的`.env`文件：
```bash
ZOTERO_API_KEY=your_api_key_here
ZOTERO_USER_ID=your_user_id_here
```

您可以从[Zotero的设置页面](https://www.zotero.org/settings/keys)获取您的Zotero API密钥和用户ID。

## 与Anthropic桌面应用集成

要与Anthropic桌面应用程序集成，请将以下配置添加到`~/Library/Application Support/Claude/claude_desktop_config.json`：

```json
{
  "mcpServers": {
    "zotero-mcp-server": {
      "command": "uv",
      "args": [
        "--directory",
        "/Users/swairshah/work/research/zotero-mcp",
        "run",
        "python",
        "-m",
        "zotero_mcp.server"
      ]
    }
  }
}
```
如果这导致错误如
```
{"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"claude-ai","version":"0.1.0"}},"jsonrpc":"2.0","id":0}
  error: unexpected argument '--directory' found
```
则使用下面的配置，并确保执行 `uv venv`; `source .venv/bin/activate`; `uv pip install ".[dev]"` 来确保服务器能够在安装所有依赖的情况下运行。

```json
{
   "mcpServers": {
      "zotero-mcp-server": {
        "command": "bash",
        "args": [
          "-c",
          "cd /Users/shahswai/personal/zotero-mcp-server && source .venv/bin/activate && python -m zotero_mcp.server"
        ]
      }
    }
  }
```

## 示例用法

该服务器允许您：
- 按标签搜索论文
- 获取论文详情及附带的笔记
- 向论文添加笔记
- 请求论文摘要

**官方网站：** [https://github.com/swairshah/zotero-mcp-server](https://github.com/swairshah/zotero-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`research and data`, `note taking`, `search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`--directory /Users/swairshah/work/research/zotero-mcp run python -m zotero_mcp.server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/swairshah-zotero.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
