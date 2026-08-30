---
title: "mcp RSS爬虫"
description: "一种MCP服务器，它获取RSS源并将其与大型语言模型共享，使人工智能助手能够访问并呈现来自已配置源的最新新闻和文章。"
---

# mcp RSS爬虫

一种MCP服务器，它获取RSS源并将其与大型语言模型共享，使人工智能助手能够访问并呈现来自已配置源的最新新闻和文章。

# MCP-RSS-Crawler

一个MCP（消息链协议）服务器，用于抓取RSS源并与LLMs共享。

## 特性

- 抓取和缓存RSS源（SQLite数据库）
- 实现MCP协议以无缝集成LLM
- 支持按类别、来源或关键词过滤源
- 全面的API端点用于管理源
  - 添加、更新和删除源
- 支持从Firecrawl获取文章

## 需求

- Bun
- Firecrawl API密钥
- Claude Desktop或其他MCP客户端

## 设置为MCP服务器

1. 克隆此仓库
2. 根据`claude_desktop_config.json.example`创建一个`claude_desktop_config.json`文件，并根据你的配置进行修改

```json
{
  "mcpServers": {
    "rss-crawler": {
      "command": "/path/to/bun",
      "args": ["run", "/path/to/mcp-rss-crawler/apps/mcp-server/src/mcp-cli.ts"],
      "cwd": "/path/to/mcp-rss-crawler",
      "env": {
        "PORT": "5556",
        "DB_DIR": "/path/to/mcp-rss-crawler",
        "FIRECRAWL_API_KEY": "fc-"
      }
    }
  }
}
```

3. 安装依赖项：
```
   bun install
```
4. 启动Claude Desktop：

## MCP协议

该服务器实现了消息链协议(MCP)，允许LLMs访问你最新的RSS源。MCP端点接受包含消息数组的JSON体的POST请求，并返回包含最新源项目的响应。

示例请求：
```json
{
  "messages": [
    {
      "role": "user",
      "content": "What are the latest news from my RSS feeds?"
    }
  ]
}
```

示例响应：
```json
{
  "messages": [
    {
      "role": "assistant",
      "content": "Here are the latest articles from your RSS feeds:",
      "name": "rss-mcp"
    },
    {
      "role": "tool",
      "content": "[{\"title\":\"Article Title\",\"summary\":\"Article summary...\",\"published\":\"2025-03-16T04:30:00.000Z\",\"origin\":\"Feed Name\",\"link\":\"https://example.com/article\"}]",
      "name": "rss-feeds"
    }
  ]
}
```

## 配置选项

可以通过环境变量或`.env`文件来配置服务器：

- `PORT` - 服务器端口（默认：5556）
- `FIRECRAWL_API_KEY` - Firecrawl API密钥
- `DB_DIR` - 数据库目录（默认：`~/.mcp-rss-crawler`）

## 故障排除

- 对于连接问题，请检查您的网络设置和防火墙配置
- 日志可以在控制台中查看，可用于诊断问题
- 更详细的日志记录，设置环境变量`DEBUG=mcp-rss:*`

**官方网站：** [https://github.com/mshk/mcp-rss-crawler](https://github.com/mshk/mcp-rss-crawler)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`communication`
- 标签：`search`, `communication`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`/path/to/bun`
- 参数：`run /path/to/mcp-rss-crawler/apps/mcp-server/src/mcp-cli.ts`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/mshk-rss-crawler.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
