---
title: "MCP文档增强服务器"
description: "一种MCP服务器实现，它提供了通过向量搜索检索和处理文档的工具，使AI助手能够用相关的文档上下文来增强其响应。\n\n使用Ollama或OpenAI生成嵌入式内容。\n\n包含Docker文件。"
---

# MCP文档增强服务器

一种MCP服务器实现，它提供了通过向量搜索检索和处理文档的工具，使AI助手能够用相关的文档上下文来增强其响应。

使用Ollama或OpenAI生成嵌入式内容。

包含Docker文件。

# MCP-server-ragdocs
[![Node.js Package](/mcp-assets/d5ccd5c5c7571857b94be33d0359c687.svg)](https://github.com/sanderkooger/mcp-server-ragdocs/actions/workflows/release.yml)
![NPM Downloads](/mcp-assets/cb523f59e75b4645e3362a2099f9f779.svg)
[![Version](/mcp-assets/d10c105fa0829d402828249bd43e2c0c.svg)](https://npmjs.com/package/@sanderkooger/mcp-server-ragdocs)
[![codecov](/mcp-assets/1a234f4d2d89ec3ce218d06c6d518c8b.svg)](https://codecov.io/gh/sanderkooger/mcp-server-ragdocs)
[![License: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://opensource.org/licenses/MIT)

这是一个MCP服务器实现，它提供了通过向量搜索检索和处理文档的工具，使AI助手能够利用相关的文档上下文来增强其响应。

## 目录

- [使用](#usage)
- [特性](#features)
- [配置](#configuration)
- [部署](#deployment)
  - [本地开发](#local-development)
  - [云部署](#cloud-deployment)
- [工具](#tools)
- [项目结构](#project-structure)
- [使用Ollama嵌入](#using-ollama-embeddings)
- [许可证](#license)
- [开发工作流程](#development-workflow)
- [贡献](#contributing)
- [Forkception致谢](#forkception-acknowledgments)

## 使用

RAG文档工具设计用于：

- 用相关文档增强AI响应
- 构建具有文档意识的AI助手
- 为开发者创建上下文感知的工具
- 实现语义文档搜索
- 增强现有的知识库

## 特性

- 基于向量的文档搜索和检索
- 支持多种文档来源
- 支持本地（Ollama）嵌入生成或OPENAI
- 语义搜索功能
- 自动化文档处理
- 为LLMs提供实时上下文增强

## 配置

```json
{
  "mcpServers": {
    "rag-docs": {
      "command": "npx",
      "args": ["-y", "@sanderkooger/mcp-server-ragdocs"],
      "env": {
        "EMBEDDINGS_PROVIDER": "ollama",
        "QDRANT_URL": "your-qdrant-url",
        "QDRANT_API_KEY": "your-qdrant-key" # if applicable
      }
    }
  }
}
```

### 与Claude Desktop一起使用

在你的`claude_desktop_config.json`中添加以下内容：

### OpenAI配置

```json
{
  "mcpServers": {
    "rag-docs-openai": {
      "command": "npx",
      "args": ["-y", "@sanderkooger/mcp-server-ragdocs"],
      "env": {
        "EMBEDDINGS_PROVIDER": "openai",
        "OPENAI_API_KEY": "your-openai-key-here",
        "QDRANT_URL": "your-qdrant-url",
        "QDRANT_API_KEY": "your-qdrant-key"
      }
    }
  }
}
```

### Ollama配置

```json
{
  "mcpServers": {
    "rag-docs-ollama": {
      "command": "npx",
      "args": ["-y", "@sanderkooger/mcp-server-ragdocs"],
      "env": {
        "EMBEDDINGS_PROVIDER": "ollama",
        "OLLAMA_BASE_URL": "http://localhost:11434",
        "QDRANT_URL": "your-qdrant-url",
        "QDRANT_API_KEY": "your-qdrant-key"
      }
    }
  }
}
```

### 从这个代码库运行Ollama
```
"ragdocs-mcp": {
      "command": "node",
      "args": [
        "/home/sander/code/mcp-server-ragdocs/build/index.js"
      ],
      "env": {
        "QDRANT_URL": "http://127.0.0.1:6333",
        "EMBEDDINGS_PROVIDER": "ollama",
        "OLLAMA_URL": "http://localhost:11434"
      },
      "alwaysAllow": [
        "run_queue",
        "list_queue",
        "list_sources",
        "search_documentation",
        "clear_queue",
        "remove_documentation",
        "extract_urls"
      ],
      "timeout": 3600
    }
```

## 环境变量参考

| 变量                | 必需项  | 默认值                  | 备注                       |
|-------------------------|---------------|--------------------------|-------------------------------|
| `EMBEDDINGS_PROVIDER`   | 所有           | `ollama`                 | "openai" 或 "ollama"          |
| `OPENAI_API_KEY`        | OpenAI        | -                        | 从OpenAI仪表板获取           |
| `OLLAMA_BASE_URL`       | Ollama        | `http://localhost:11434` | 本地Ollama服务器URL         |
| `QDRANT_URL`            | 所有           | `http://localhost:6333`  | Qdrant端点URL               |
| `QDRANT_API_KEY`        | 云Qdrant      | -                        | 从Qdrant Cloud控制台获得     |

### 本地部署

仓库包含了用于本地开发的Docker Compose配置文件：

[Docker Compose 下载](https://raw.githubusercontent.com/sanderkooger/mcp-server-ragdocs/main/docker-compose.yml)

```bash
docker compose up -d
```

这将启动：

- Qdrant 向量数据库在 6333 端口
- Ollama LLM 服务在 11434 端口

访问端点：

- Qdrant: http://localhost:6333
- Ollama: http://localhost:11434

### 云部署

对于生产环境部署：

1. 使用托管的 Qdrant Cloud 服务
2. 设置以下环境变量：

```bash
QDRANT_URL=your-cloud-cluster-url
QDRANT_API_KEY=your-cloud-api-key
```

## 工具

### search_documentation

使用自然语言查询搜索存储的文档。返回带有上下文的相关摘录，并按相关性排序。

**输入：**

- `query` (字符串)：要在文档中搜索的文本。可以是自然语言查询、特定术语或代码片段。
- `limit` (数字，可选)：要返回的最大结果数量（1-20，默认为 5）。较高的限制提供更全面的结果，但处理时间可能更长。

### list_sources

列出系统中当前存储的所有文档源。返回所有已索引文档的综合列表，包括源 URL、标题和最后更新时间。使用此功能可以了解可用于搜索的文档，或验证特定源是否已被索引。

### extract_urls

从给定网页中提取并分析所有 URL。此工具会爬取指定网页，识别所有超链接，并可选择将它们添加到处理队列中。

**输入：**

- `url` (字符串)：要分析的网页的完整 URL（必须包含协议，例如 https://）。页面必须是公开可访问的。
- `add_to_queue` (布尔值，可选)：如果为 true，则自动将提取的 URL 添加到处理队列以供稍后索引。在大型站点上使用时需谨慎，以免过度排队。

### remove_documentation

通过其 URL 从系统中删除特定的文档源。删除是永久性的，会影响未来的搜索结果。

**输入：**

- `urls` (字符串数组)：要从数据库中删除的 URL 数组。每个 URL 必须与添加文档时使用的 URL 完全匹配。

### list_queue

列出当前在文档处理队列中等待的所有 URL。显示将在调用 run_queue 时处理的待处理文档源。使用此功能来监控队列状态、验证 URL 是否正确添加或检查处理积压情况。

### run_queue

处理并索引文档队列中的所有 URL。每个 URL 依次处理，具有适当的错误处理和重试逻辑。处理过程中会提供进度更新。长时间运行的操作将一直处理直到队列为空或发生无法恢复的错误为止。

### clear_queue

从文档处理队列中移除所有待处理的 URL。当您想重新开始、删除不需要的 URL 或取消待处理的处理时，请使用此功能。此操作是立即且永久的——如果以后需要处理这些 URL，则需要重新添加。

## 项目结构

该包遵循模块化架构，核心组件和MCP协议处理器之间有明确的分离。有关详细的结构文档和设计决策，请参阅[ARCHITECTURE.md](https://github.com/sanderkooger/mcp-server-ragdocs/blob/HEAD/ARCHITECTURE.md)。

## 不使用Docker运行Ollama Embeddings

1. 安装Ollama：

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

2. 下载nomic-embed-text模型：

```bash
ollama pull nomic-embed-text
```

3. 验证安装：

```bash
ollama list
```

## 许可证

此MCP服务器根据MIT许可证授权。这意味着您可以自由地使用、修改和分发软件，但必须遵守MIT许可证的条款和条件。更多详情，请参见项目仓库中的LICENSE文件。

## 贡献

我们欢迎贡献！请参阅我们的[CONTRIBUTING.md](https://github.com/sanderkooger/mcp-server-ragdocs/blob/HEAD/CONTRIBUTING.md)以获取详细指南，以下是基本步骤：

1. Fork仓库
2. 安装依赖项：`npm install`
3. 创建特性分支：`git checkout -b feat/your-feature`
4. 使用`npm run commit`提交更改，以确保符合[Conventional Commits](https://www.conventionalcommits.org)规范
5. 将更改推送到您的Fork并打开一个PR

## Forkception致谢

本项目基于[hannesrudolph/mcp-ragdocs](https://github.com/hannesrudolph/mcp-ragdocs)的一个分支，而后者又从[qpd-v/mcp-ragdocs](https://github.com/qpd-v/mcp-ragdocs)的原始工作分叉而来。原项目为这个实现提供了基础。

**官方网站：** [https://github.com/sanderkooger/mcp-server-ragdocs](https://github.com/sanderkooger/mcp-server-ragdocs)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`knowledge and memory`, `search`, `research and data`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @sanderkooger/mcp-server-ragdocs`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/sanderkooger-ragdocs.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
