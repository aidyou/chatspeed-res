---
title: "mcp-server-weibo"
description: "A Model Context Protocol server for scraping Weibo user information, feeds, and search functionality. It helps retrieve detailed user profiles, timeline content, and perform user searches on Weibo."
---

# mcp-server-weibo

A Model Context Protocol server for scraping Weibo user information, feeds, and search functionality. It helps retrieve detailed user profiles, timeline content, and perform user searches on Weibo.

# Weibo MCP Server

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

**Official site: ** [https://github.com/qinyuanpei/mcp-server-weibo](https://github.com/qinyuanpei/mcp-server-weibo)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `browser`
- Tags: `browser automation`, `social media`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `--from git+https://github.com/qinyuanpei/mcp-server-weibo.git mcp-server-weibo`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/qinyuanpei-weibo.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
