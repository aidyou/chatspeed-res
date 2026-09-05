---
title: "Verge新闻获取器"
description: "提供从The Verge的RSS源获取和搜索新闻的工具，允许用户获取当天的新闻、检索过去一周的随机文章以及在近期的Verge内容中搜索特定关键词。"
---

# Verge新闻获取器

提供从The Verge的RSS源获取和搜索新闻的工具，允许用户获取当天的新闻、检索过去一周的随机文章以及在近期的Verge内容中搜索特定关键词。

# The Verge News MCP 服务器

[Smithery](https://smithery.ai/server/@manimohans/verge-news-mcp)

一个提供从 The Verge 的 RSS 源获取和搜索新闻的工具的 MCP 服务器。

  

## 功能

- 从 The Verge 获取今日新闻
- 从 The Verge 过去一周中随机选择一些新闻
- 通过关键词搜索新闻文章

## 安装

```bash
# Clone the repository
git clone https://github.com/manimohans/verge-news-mcp.git
cd verge-news-mcp

# Install dependencies
npm install

# Build the project
npm run build
```

## 使用方法

### 运行服务器

```bash
npm start
```

### 与 Claude for Desktop 一起使用

1. 安装 [Claude for Desktop](https://claude.ai/download)
2. 打开你的 Claude for Desktop 应用配置文件：
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`

3. 添加以下配置：

```json
{
  "mcpServers": {
    "verge-news": {
      "command": "node",
      "args": ["/absolute/path/to/verge-news-mcp/build/index.js"]
    }
  }
}
```

4. 重启 Claude for Desktop

### 与 Smithery 一起使用

你也可以将此 MCP 服务器与 [Smithery](https://smithery.dev/) 一起使用，这允许你轻松地共享和使用 MCP 服务器：

1. 确保已安装 Smithery：
```bash
npm install -g @anthropic-ai/smithery
```

2. 要通过 Smithery 使用此服务器，请运行：
```bash
smithery use https://github.com/manimohans/verge-news-mcp
```

3. 安装完成后，你可以将其与 Claude 或任何其他支持 MCP 的应用程序一起使用。

#### Smithery 配置

此仓库包括了 Smithery 所需的配置文件：

- `Dockerfile`：定义如何为 MCP 服务器构建 Docker 容器
- `smithery.yaml`：为 Smithery 配置 MCP 服务器，包括其功能

有关 Smithery 配置的更多信息，请参阅 [Smithery 文档](https://smithery.ai/docs/config)。

### 可用工具

#### get-daily-news

从 The Verge 获取过去 24 小时内发布的最新新闻文章。

示例查询：“今天 The Verge 有什么新闻？”

#### get-weekly-news

从 The Verge 获取过去 7 天内发布的新闻文章。

示例查询：“显示 The Verge 过去一周的新闻。”

**注意：** 此工具会从过去一周中随机选择 10 条新闻，每次使用时都会有所不同。

#### search-news

搜索包含特定关键词的新闻文章。

参数：
- `keyword`：要搜索的术语
- `days`（可选）：回溯的天数（默认：30）

示例查询：“查找 The Verge 关于 AI 的新闻文章。”

## 开发

```bash
# Run in development mode
npm run dev
```

## 许可证

ISC

**官方网站：** [https://github.com/manimohans/verge-news-mcp](https://github.com/manimohans/verge-news-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`, `browser`, `media`
- 标签：`search`, `browser automation`, `entertainment and media`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`/absolute/path/to/verge-news-mcp/build/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/manimohans-verge-news.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
