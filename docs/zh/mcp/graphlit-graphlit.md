---
title: "图灵知识桥"
description: "模型上下文协议（MCP）服务器实现了MCP客户端与Graphlit服务之间的集成。 将从Slack到Gmail再到播客订阅源的内容，以及网络爬虫获取的内容，全部导入到Graphlit项目中——然后通过MCP客户端检索相关的内容。"
---

# 图灵知识桥

模型上下文协议（MCP）服务器实现了MCP客户端与Graphlit服务之间的集成。 将从Slack到Gmail再到播客订阅源的内容，以及网络爬虫获取的内容，全部导入到Graphlit项目中——然后通过MCP客户端检索相关的内容。

[![npm version](/mcp-assets/75a1729d773d8f5a7b9ad62669fc1b8d.svg)](https://badge.fury.io/js/graphlit-mcp-server)
[Smithery](https://smithery.ai/server/@graphlit/graphlit-mcp-server)

# Graphlit 平台的 Model Context Protocol (MCP) 服务器

## 概述

Model Context Protocol (MCP) 服务器实现了 MCP 客户端与 Graphlit 服务之间的集成。本文档概述了设置过程，并提供了使用客户端的基本示例。

您可以从 Slack、Discord、网站、Google Drive、电子邮件、Jira、Linear 或 GitHub 中导入任何内容到 Graphlit 项目中，然后在像 Cursor、Windsurf 或 Cline 这样的 MCP 客户端中搜索和检索相关知识。

文档（PDF、DOCX、PPTX 等）和 HTML 网页将在导入时被提取为 Markdown 格式。

音频和视频文件将在导入时转录。

Web 爬虫和网络搜索作为 MCP 工具内置，无需单独集成如 Firecrawl、Exa 等其他工具。

您可以在我们的 [博客](https://www.graphlit.com/blog/graphlit-mcp-server) 上了解更多关于 MCP 服务器用例和功能的信息。

  

## 工具

### 检索

- 查询内容
- 查询集合
- 检索相关源
- 检索相似图片
- 图片视觉描述

### 提取

- 从文本中提取结构化的 JSON

### 导入

- 文件
- 网页
- 消息
- 帖子
- 电子邮件
- 问题
- 文本

### 数据连接器
- Microsoft Outlook 电子邮件
- Google Mail
- Notion
- Reddit
- Linear
- Jira
- GitHub Issues
- Google Drive
- OneDrive
- SharePoint
- Dropbox
- Box
- GitHub
- Slack
- Microsoft Teams
- Discord
- Twitter/X
- 播客 (RSS)

### Web
- Web 爬虫
- Web 搜索（包括播客搜索）
- Web 映射
- 截图页面

### 通知
- Slack
- 电子邮件
- Webhook

### 操作

- 配置项目
- 创建集合
- 向集合添加内容
- 从集合中移除内容
- 删除集合
- 删除订阅
- 删除内容
- 订阅完成了吗？
- 内容完成了吗？

### 枚举

- 列出 Slack 频道
- 列出 Microsoft Teams 团队
- 列出 Microsoft Teams 频道
- 列出 SharePoint 库
- 列出 SharePoint 文件夹
- 列出 Linear 项目

## 资源

- 项目
- 内容
- 订阅
- 内容集合
- 工作流
- 规范

## 前提条件

在开始之前，请确保您具备以下条件：

- 您的系统上安装了 Node.js（建议版本 18.x 或更高）。
- 在 [Graphlit 平台](https://portal.graphlit.dev) 上拥有一个活跃帐户，并可以访问 API 设置仪表板。

## 配置

Graphlit MCP 服务器支持通过设置环境变量来进行身份验证和配置：

- `GRAPHLIT_ENVIRONMENT_ID`：您的环境 ID。
- `GRAPHLIT_ORGANIZATION_ID`：您的组织 ID。
- `GRAPHLIT_JWT_SECRET`：用于签署 JWT 令牌的 JWT 密钥。

你可以在 [Graphlit 平台](https://portal.graphlit.dev) 的 API 设置仪表板中找到这些值。

## 安装

### 通过 Windsurf 安装

要在 Windsurf IDE 应用程序中安装 graphlit-mcp-server，Cline 应该使用 NPX：

```bash
npx -y graphlit-mcp-server
```

你的 mcp_config.json 文件应该配置如下：

```
{
    "mcpServers": {
        "graphlit-mcp-server": {
            "command": "npx",
            "args": [
                "-y",
                "graphlit-mcp-server"
            ],
            "env": {
                "GRAPHLIT_ORGANIZATION_ID": "your-organization-id",
                "GRAPHLIT_ENVIRONMENT_ID": "your-environment-id",
                "GRAPHLIT_JWT_SECRET": "your-jwt-secret",
            }
        }
    }
}
```

### 通过 Cline 安装

要在 Cline IDE 应用程序中安装 graphlit-mcp-server，Cline 应该使用 NPX：

```bash
npx -y graphlit-mcp-server
```

你的 cline_mcp_settings.json 文件应该配置如下：

```
{
    "mcpServers": {
        "graphlit-mcp-server": {
            "command": "npx",
            "args": [
                "-y",
                "graphlit-mcp-server"
            ],
            "env": {
                "GRAPHLIT_ORGANIZATION_ID": "your-organization-id",
                "GRAPHLIT_ENVIRONMENT_ID": "your-environment-id",
                "GRAPHLIT_JWT_SECRET": "your-jwt-secret",
            }
        }
    }
}
```

### 通过 Cursor 安装

要在 Cursor IDE 应用程序中安装 graphlit-mcp-server，Cline 应该使用 NPX：

```bash
npx -y graphlit-mcp-server
```

你的 mcp.json 文件应该配置如下：

```
{
    "mcpServers": {
        "graphlit-mcp-server": {
            "command": "npx",
            "args": [
                "-y",
                "graphlit-mcp-server"
            ],
            "env": {
                "GRAPHLIT_ORGANIZATION_ID": "your-organization-id",
                "GRAPHLIT_ENVIRONMENT_ID": "your-environment-id",
                "GRAPHLIT_JWT_SECRET": "your-jwt-secret",
            }
        }
    }
}
```

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@graphlit/graphlit-mcp-server) 自动为 Claude 桌面版安装 graphlit-mcp-server：

```bash
npx -y @smithery/cli install @graphlit/graphlit-mcp-server --client claude
```

### 手动安装

要在任何 MCP 客户端应用程序中使用 Graphlit MCP Server，请使用：

```
{
    "mcpServers": {
        "graphlit-mcp-server": {
            "command": "npx",
            "args": [
                "-y",
                "graphlit-mcp-server"
            ],
            "env": {
                "GRAPHLIT_ORGANIZATION_ID": "your-organization-id",
                "GRAPHLIT_ENVIRONMENT_ID": "your-environment-id",
                "GRAPHLIT_JWT_SECRET": "your-jwt-secret",
            }
        }
    }
}
```

可选地，你可以配置数据连接器的凭证，如 Slack、Google 邮件和 Notion。仅需要 GRAPHLIT_ORGANIZATION_ID、GRAPHLIT_ENVIRONMENT_ID 和 GRAPHLIT_JWT_SECRET。

```
{
    "mcpServers": {
        "graphlit-mcp-server": {
            "command": "npx",
            "args": [
                "-y",
                "graphlit-mcp-server"
            ],
            "env": {
                "GRAPHLIT_ORGANIZATION_ID": "your-organization-id",
                "GRAPHLIT_ENVIRONMENT_ID": "your-environment-id",
                "GRAPHLIT_JWT_SECRET": "your-jwt-secret",
                "SLACK_BOT_TOKEN": "your-slack-bot-token",
                "DISCORD_BOT_TOKEN": "your-discord-bot-token",
                "TWITTER_TOKEN": "your-twitter-token",
                "GOOGLE_EMAIL_REFRESH_TOKEN": "your-google-refresh-token",
                "GOOGLE_EMAIL_CLIENT_ID": "your-google-client-id",
                "GOOGLE_EMAIL_CLIENT_SECRET": "your-google-client-secret",
                "LINEAR_API_KEY": "your-linear-api-key",
                "GITHUB_PERSONAL_ACCESS_TOKEN": "your-github-pat",
                "JIRA_EMAIL": "your-jira-email",
                "JIRA_TOKEN": "your-jira-token",
                "NOTION_API_KEY": "your-notion-api-key",
                "NOTION_DATABASE_ID": "your-notion-database-id"
            }
        }
    }
}
```

## 支持

请参考 [Graphlit API 文档](https://docs.graphlit.dev/)。

对于 Graphlit MCP Server 的支持，请提交一个 [GitHub Issue](https://github.com/graphlit/graphlit-mcp-server/issues)。

对于 Graphlit 平台的进一步支持，请加入我们的 [Discord](https://discord.gg/ygFmfjy3Qx) 社区。

**官方网站：** [https://github.com/graphlit/graphlit-mcp-server](https://github.com/graphlit/graphlit-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`memory`, `communication`
- 标签：`knowledge and memory`, `communication`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y graphlit-mcp-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/graphlit-graphlit.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
