---
title: "MCP文档增强"
description: "一种MCP服务器实现，它提供了通过向量搜索检索和处理文档的工具，使人工智能助手能够用相关的文档上下文来增强其响应。"
---

# MCP文档增强

一种MCP服务器实现，它提供了通过向量搜索检索和处理文档的工具，使人工智能助手能够用相关的文档上下文来增强其响应。

# RAG 文档 MCP 服务器

一个MCP服务器实现，提供通过向量搜索检索和处理文档的工具，使AI助手能够利用相关文档上下文增强其响应。

## 功能

- 基于向量的文档搜索和检索
- 支持多个文档源
- 语义搜索能力
- 自动化文档处理
- 实时为LLM提供上下文增强

## 工具

### search_documentation
使用自然语言查询搜索存储的文档。返回按相关性排序的带有上下文的匹配摘录。

**输入:**
- `query` (字符串): 在文档中搜索的文本。可以是自然语言查询、特定术语或代码片段。
- `limit` (数字, 可选): 返回的最大结果数量（1-20，默认：5）。较高的限制提供了更全面的结果，但可能需要更长的处理时间。

### list_sources
列出系统中当前存储的所有文档源。返回所有已索引文档的综合列表，包括来源URL、标题和最后更新时间。使用此功能来了解可搜索的文档有哪些，或者验证特定来源是否已被索引。

### extract_urls
从给定网页提取并分析所有URL。该工具会爬取指定的网页，识别所有超链接，并可以选择将它们添加到处理队列中。

**输入:**
- `url` (字符串): 要分析的网页的完整URL（必须包含协议，例如https://）。页面必须是公开可访问的。
- `add_to_queue` (布尔值, 可选): 如果为true，则自动将提取的URL添加到处理队列以供稍后索引。对于大型站点，请谨慎使用以避免过度排队。

### remove_documentation
通过其URL从系统中删除特定的文档源。移除是永久性的，并将影响未来的搜索结果。

**输入:**
- `urls` (字符串数组): 要从数据库中删除的URL数组。每个URL必须与添加文档时使用的URL完全匹配。

### list_queue
列出当前等待在文档处理队列中的所有URL。显示将在调用run_queue时被处理的待处理文档源。使用此功能监控队列状态，验证URL是否正确添加，或检查处理积压情况。

### run_queue
处理并索引文档队列中的所有URL。每个URL按顺序处理，具有适当的错误处理和重试逻辑。处理过程中提供进度更新。长时间运行的操作将持续处理直到队列为空或发生无法恢复的错误为止。

### clear_queue
从文档处理队列中移除所有待处理的URL。当您想要重新开始、移除不需要的URL或取消待处理的处理时，使用此功能。此操作立即生效且不可逆——如果您希望以后再处理这些URL，需要重新添加。

## 使用说明

请注意，原文档在这里结束，并没有进一步提供具体的使用示例或指南。如果需要关于如何配置或具体命令行参数等信息，请参照相关章节或联系支持团队获取更多帮助。

RAG 文档工具旨在实现以下功能：

- 通过相关文档增强 AI 响应
- 构建具有文档意识的 AI 助手
- 为开发者创建上下文感知工具
- 实现语义文档搜索
- 增强现有知识库

## 配置

### 在 Claude Desktop 中使用

将以下内容添加到您的 `claude_desktop_config.json` 文件中：

```json
{
  "mcpServers": {
    "rag-docs": {
      "command": "npx",
      "args": [
        "-y",
        "@hannesrudolph/mcp-ragdocs"
      ],
      "env": {
        "OPENAI_API_KEY": "",
        "QDRANT_URL": "",
        "QDRANT_API_KEY": ""
      }
    }
  }
}
```

您需要为以下环境变量提供值：
- `OPENAI_API_KEY`：用于生成嵌入的 OpenAI API 密钥
- `QDRANT_URL`：您的 Qdrant 向量数据库实例的 URL
- `QDRANT_API_KEY`：与 Qdrant 认证的 API 密钥

## 许可证

此 MCP 服务器采用 MIT 许可证。这意味着您可以自由地使用、修改和分发该软件，但需遵守 MIT 许可证的条款和条件。更多详情，请参阅项目仓库中的 LICENSE 文件。

## 致谢

该项目是 [qpd-v/mcp-ragdocs](https://github.com/qpd-v/mcp-ragdocs) 的一个分支，最初由 qpd-v 开发。原项目为此实现提供了基础。

**官方网站：** [https://github.com/hannesrudolph/mcp-ragdocs](https://github.com/hannesrudolph/mcp-ragdocs)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`, `search`, `memory`
- 标签：`search`, `knowledge and memory`, `developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @hannesrudolph/mcp-ragdocs`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/hannesrudolph-ragdocs.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
