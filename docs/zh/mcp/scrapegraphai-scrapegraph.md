---
title: "网页图AI智搜"
description: "一个生产就绪的模型上下文协议服务器，使语言模型能够利用人工智能驱动的网络爬虫功能，提供将网页转换为Markdown、提取结构化数据以及执行人工智能驱动的网络搜索的工具。"
---

# 网页图AI智搜

一个生产就绪的模型上下文协议服务器，使语言模型能够利用人工智能驱动的网络爬虫功能，提供将网页转换为Markdown、提取结构化数据以及执行人工智能驱动的网络搜索的工具。

# ScrapeGraph MCP 服务器

  

[![许可证: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10](/mcp-assets/9a5462509af74d8a0229903fa0c244e1.svg)](https://www.python.org/downloads/release/python-3100/)
[Smithery](https://smithery.ai/server/@ScrapeGraphAI/scrapegraph-mcp)

一个生产就绪的 [Model Context Protocol](https://modelcontextprotocol.io/introduction) (MCP) 服务器，提供与 [ScapeGraph AI](https://scrapegraphai.com) API 的无缝集成。此服务器使语言模型能够利用具有企业级可靠性的高级 AI 支持的网络抓取功能。

## 可用工具

该服务器提供了以下企业级工具：

- `markdownify(website_url: str)`: 将任何网页转换为干净、结构化的 markdown 格式
- `smartscraper(user_prompt: str, website_url: str)`: 利用 AI 从任何网页中提取结构化数据
- `searchscraper(user_prompt: str)`: 执行具有结构化、可操作结果的 AI 支持的网络搜索

## 设置说明

要使用此服务器，您需要一个 ScapeGraph API 密钥。请按照以下步骤获取：

1. 转到 [ScapeGraph 控制面板](https://dashboard.scrapegraphai.com)
2. 创建账户并生成您的 API 密钥

### 通过 Smithery 自动安装

使用 [Smithery](https://smithery.ai/server/@ScrapeGraphAI/scrapegraph-mcp) 自动安装 ScrapeGraph API 集成服务器：

```bash
npx -y @smithery/cli install @ScrapeGraphAI/scrapegraph-mcp --client claude
```

### Claude 桌面配置

更新您的 Claude 桌面配置文件，添加以下设置（位于光标页面右上角）：

（记得在配置中添加您的 API 密钥）

```json
{
    "mcpServers": {
        "@ScrapeGraphAI-scrapegraph-mcp": {
            "command": "npx",
            "args": [
                "-y",
                "@smithery/cli@latest",
                "run",
                "@ScrapeGraphAI/scrapegraph-mcp",
                "--config",
                "\"{\\\"scrapegraphApiKey\\\":\\\"YOUR-SGAI-API-KEY\\\"}\""
            ]
        }
    }
}
```

配置文件位于：
- Windows: `%APPDATA%/Claude/claude_desktop_config.json`
- macOS: `~/Library/Application\ Support/Claude/claude_desktop_config.json`

### Cursor 集成

在设置中添加 ScrapeGraphAI MCP 服务器：

## 示例用例

该服务器支持复杂的查询，例如：

- "分析并提取 ScapeGraph API 的主要特性"
- "生成 ScapeGraph 主页的结构化 markdown 版本"
- "从 ScapeGraph 网站中提取并分析定价信息"
- "研究并总结 AI 支持的网络抓取领域的最新进展"
- "创建 Python 文档网站的全面摘要"

## 错误处理

该服务器实现了强大的错误处理机制，并为以下情况提供详细且可操作的错误消息：

- API 认证问题
- URL 结构不正确
- 网络连接故障
- 速率限制和配额管理

## 常见问题

### Windows 特定连接

在 Windows 系统上运行时，您可能需要使用以下命令来连接 MCP 服务器：

```bash
C:\Windows\System32\cmd.exe /c npx -y @smithery/cli@latest run @ScrapeGraphAI/scrapegraph-mcp --config "{\"scrapegraphApiKey\":\"YOUR-SGAI-API-KEY\"}"
```

这确保了在 Windows 环境中的正确执行。

## 许可证

本项目遵循 MIT 许可证发布。有关详细的条款和条件，请参阅 LICENSE 文件。

## 致谢

特别感谢 [tomekkorbak](https://github.com/tomekkorbak) 实现的 [oura-mcp-server](https://github.com/tomekkorbak/oura-mcp-server)，它作为本仓库的起点。

由 [ScrapeGraphAI](https://scrapegraphai.com) 团队用心制作 ❤️

**官方网站：** [https://github.com/ScrapeGraphAI/scrapegraph-mcp](https://github.com/ScrapeGraphAI/scrapegraph-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`browser`
- 标签：`browser automation`, `search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @smithery/cli@latest run @ScrapeGraphAI/scrapegraph-mcp --config "{\"scrapegraphApiKey\":\"YOUR-SGAI-API-KEY\"}"`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/scrapegraphai-scrapegraph.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
