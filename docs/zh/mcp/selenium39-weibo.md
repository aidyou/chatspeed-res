---
title: "mcp微博服务器"
description: "一个用于抓取微博的模型上下文协议服务器，提供搜索用户、获取详细用户资料和提取用户动态的工具。"
---

# mcp微博服务器

一个用于抓取微博的模型上下文协议服务器，提供搜索用户、获取详细用户资料和提取用户动态的工具。

# 微博 MCP 服务器 (TypeScript 版本)

这是一个基于 [Model Context Protocol](https://modelcontextprotocol.io) 的服务器，用于抓取微博用户信息、动态和搜索功能。该服务器可以帮助获取关于微博用户的详细信息、动态内容以及执行用户搜索。

  

## 安装

从源代码安装：

```json
{
    "mcpServers": {
        "weibo": {
            "command": "npx",
            "args": [
                "--from",
                "git+https://github.com/Selenium39/mcp-server-weibo.git",
                "mcp-server-weibo"
            ]
        }
    }
}
```

通过包管理器安装：

```json
{
    "mcpServers": {
        "weibo": {
            "command": "npx",
            "args": ["mcp-server-weibo"],
        }
    }
}
```

## 组件

### 工具

- `search_users(keyword, limit)`: 根据关键词搜索微博用户
- `get_profile(uid)`: 获取用户详细资料信息
- `get_feeds(uid, limit)`: 获取用户微博动态
- `get_hot_search(limit)`: 获取微博热搜榜
- `search_content(keyword, limit, page?)`: 根据关键词搜索微博内容

### 资源

无

### 提示词

无

## 要求

- Node.js >= 18.0.0

## 许可证

MIT 许可证

## 免责声明

此项目与微博无关，仅供学习和研究用途。

**官方网站：** [https://github.com/Selenium39/mcp-server-weibo](https://github.com/Selenium39/mcp-server-weibo)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`browser`
- 标签：`browser automation`, `social media`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`--from git+https://github.com/Selenium39/mcp-server-weibo.git mcp-server-weibo`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/selenium39-weibo.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
