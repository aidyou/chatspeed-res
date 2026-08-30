---
title: "GitHub趋势MCP"
description: "一个MCP服务器，通过简单的API接口提供对GitHub热门仓库和开发者数据的访问。"
---

# GitHub趋势MCP

一个MCP服务器，通过简单的API接口提供对GitHub热门仓库和开发者数据的访问。

# mcp-github-trending MCP Server

一个通过简单API接口提供GitHub热门仓库和开发者数据的MCP服务器。

[Smithery](https://smithery.ai/server/@hetaoBackend/github-trending-mcp-server)

## 功能

- 访问GitHub热门仓库和开发者数据
- 按编程语言筛选
- 按时间周期（每日、每周、每月）筛选
- 按自然语言筛选
- 返回格式良好的JSON响应

## 工具

该服务器实现了以下工具：

### get_github_trending_repositories

从GitHub获取热门仓库，参数如下：

- `language` (可选): 用于筛选仓库的编程语言（例如 "python", "javascript"）
- `since` (可选): 用于筛选仓库的时间周期 ("daily", "weekly", "monthly")。默认为 "daily"
- `spoken_language` (可选): 用于筛选仓库的自然语言

示例响应：
```json
[
  {
    "name": "repository-name",
    "fullname": "owner/repository-name",
    "url": "https://github.com/owner/repository-name",
    "description": "Repository description",
    "language": "Python",
    "stars": 1000,
    "forks": 100,
    "current_period_stars": 50
  }
]
```

### get_github_trending_developers

从GitHub获取热门开发者，参数如下：

- `language` (可选): 用于筛选开发者的编程语言（例如 "python", "javascript"）
- `since` (可选): 用于筛选开发者的时间周期 ("daily", "weekly", "monthly")。默认为 "daily"

示例响应：
```json
[
  {
    "username": "developer",
    "name": "Developer Name",
    "url": "https://github.com/developer",
    "avatar": "https://avatars.githubusercontent.com/u/123456",
    "repo": {
      "name": "repository-name",
      "description": "Repository description",
      "url": "https://github.com/developer/repository-name"
    }
  }
]
```

## 安装

### 前提条件

- Python 3.12

### 安装步骤

安装包：
```bash
pip install mcp-github-trending
```

### Claude Desktop 配置

在MacOS上：
```bash
~/Library/Application\ Support/Claude/claude_desktop_config.json
```

在Windows上：
```bash
%APPDATA%/Claude/claude_desktop_config.json
```

 开发/未发布服务器配置

```json
{
  "mcpServers": {
    "mcp-github-trending": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/mcp-github-trending",
        "run",
        "mcp-github-trending"
      ]
    }
  }
}
```

 已发布服务器配置

```json
{
  "mcpServers": {
    "mcp-github-trending": {
      "command": "uvx",
      "args": [
        "mcp-github-trending"
      ]
    }
  }
}
```

## 开发

### 构建和发布

1. 同步依赖并更新锁文件：
```bash
uv sync
```

2. 构建包分发：
```bash
uv build
```

3. 发布到PyPI：
```bash
uv publish
```

注意：通过环境变量或命令标志设置PyPI凭据：
- Token: `--token` 或 `UV_PUBLISH_TOKEN`
- 用户名/密码: `--username`/`UV_PUBLISH_USERNAME` 和 `--password`/`UV_PUBLISH_PASSWORD`

### 调试

为了获得最佳调试体验，请使用 [MCP Inspector](https://github.com/modelcontextprotocol/inspector)。

通过[npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)启动MCP Inspector：

```bash
npx @modelcontextprotocol/inspector uv --directory /path/to/mcp-github-trending run mcp-github-trending
```

Inspector将显示一个URL，您可以在浏览器中访问它以开始调试。

## 许可证

本项目根据MIT许可证许可 - 详情请参阅LICENSE文件。

**官方网站：** [https://github.com/hetaoBackend/mcp-github-trending](https://github.com/hetaoBackend/mcp-github-trending)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`version control`, `developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`mcp-github-trending`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/hetaobackend-github-trending.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
