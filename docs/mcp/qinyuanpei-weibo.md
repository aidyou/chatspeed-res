---
title: "mcp-server微博抓取器"
description: "一种用于抓取微博用户信息、动态和搜索功能的模型上下文协议服务器。它有助于获取详细的用户资料、时间线内容，并在微博上执行用户搜索。"
---

# mcp-server微博抓取器

一种用于抓取微博用户信息、动态和搜索功能的模型上下文协议服务器。它有助于获取详细的用户资料、时间线内容，并在微博上执行用户搜索。

# 微博 MCP 服务器

这是一个基于 [Model Context Protocol](https://modelcontextprotocol.io) 的服务器，用于抓取微博用户信息、动态和搜索功能。该服务器可以帮助获取微博用户的详细信息、动态内容以及进行用户搜索。

## 安装

从源代码安装：

```json
{
    "mcpServers": {
        "weibo": {
            "command": "uvx",
            "args": [
                "--from",
                "git+https://github.com/qinyuanpei/mcp-server-weibo.git",
                "mcp-server-weibo"
            ]
        }
    }
}
```

从包管理器安装：

```json
{
    "mcpServers": {
        "weibo": {
            "command": "uvx",
            "args": ["mcp-server-weibo"],
        }
    }
}
```

## 组件

### 工具

- `search_users(keyword, limit)`: 用于搜索微博用户
- `get_profile(uid)`: 获取用户详细信息
- `get_feeds(uid, limit)`: 获取用户动态

### 资源   

无

### 提示

无

## 依赖要求

- Python >= 3.10
- httpx >= 0.24.0

## 许可证

MIT 许可证 - 详见 [LICENSE](https://github.com/qinyuanpei/mcp-server-weibo/blob/HEAD/LICENSE) 文件

## 免责声明

本项目与微博官方无关，仅用于学习和研究目的。

**官方网站：** [https://github.com/qinyuanpei/mcp-server-weibo](https://github.com/qinyuanpei/mcp-server-weibo)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`browser`
- 标签：`browser automation`, `social media`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`--from git+https://github.com/qinyuanpei/mcp-server-weibo.git mcp-server-weibo`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/qinyuanpei-weibo.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
