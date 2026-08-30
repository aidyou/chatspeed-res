---
title: "RAG文档管理工具"
description: "为语义文档搜索提供RAG功能，使用Qdrant向量数据库和Ollama/OpenAI嵌入式服务，允许用户添加、搜索、列出和删除带有元数据支持的文档。"
---

# RAG文档管理工具

为语义文档搜索提供RAG功能，使用Qdrant向量数据库和Ollama/OpenAI嵌入式服务，允许用户添加、搜索、列出和删除带有元数据支持的文档。

# RagDocs MCP 服务器

一个使用 Qdrant 向量数据库和 Ollama/OpenAI 嵌入的模型上下文协议 (MCP) 服务器，提供 RAG（检索增强生成）功能。该服务器通过向量相似性实现文档的语义搜索和管理。

## 功能

- 添加带有元数据的文档
- 通过文档进行语义搜索
- 列出并组织文档
- 删除文档
- 支持 Ollama（免费）和 OpenAI（付费）嵌入
- 自动文本分块和嵌入生成
- 使用 Qdrant 进行向量存储

## 先决条件

- Node.js 16 或更高版本
- 以下 Qdrant 设置之一：
  - 使用 Docker 的本地实例（免费）
  - 拥有 API 密钥的 Qdrant Cloud 账户（托管服务）
- 以下嵌入选项之一：
  - 本地运行的 Ollama（默认，免费）
  - OpenAI API 密钥（可选，付费）

## 可用工具

### 1. add_document
将文档添加到 RAG 系统中。

参数：
- `url`（必填）：文档 URL/标识符
- `content`（必填）：文档内容
- `metadata`（可选）：文档元数据
  - `title`：文档标题
  - `contentType`：内容类型（例如："text/markdown"）

### 2. search_documents
使用语义相似性搜索已存储的文档。

参数：
- `query`（必填）：自然语言搜索查询
- `options`（可选）：
  - `limit`：最大结果数（1-20，默认：5）
  - `scoreThreshold`：最小相似度分数（0-1，默认：0.7）
  - `filters`：
    - `domain`：按领域过滤
    - `hasCode`：过滤包含代码的文档
    - `after`：按日期之后过滤（ISO 格式）
    - `before`：按日期之前过滤（ISO 格式）

### 3. list_documents
列出所有存储的文档，并提供分页和分组选项。

参数（全部可选）：
- `page`：页码（默认：1）
- `pageSize`：每页文档数量（1-100，默认：20）
- `groupByDomain`：按领域分组文档（默认：false）
- `sortBy`：排序字段（"timestamp"、"title" 或 "domain"）
- `sortOrder`：排序顺序（"asc" 或 "desc"）

### 4. delete_document
从 RAG 系统中删除文档。

参数：
- `url`（必填）：要删除的文档的 URL

## 安装

```bash
npm install -g @mcpservers/ragdocs
```

## MCP 服务器配置

```json
{
  "mcpServers": {
    "ragdocs": {
      "command": "node",
      "args": ["@mcpservers/ragdocs"],
      "env": {
        "QDRANT_URL": "http://127.0.0.1:6333",
        "EMBEDDING_PROVIDER": "ollama"
      }
    }
  }
}
```

使用 Qdrant Cloud:
```json
{
  "mcpServers": {
    "ragdocs": {
      "command": "node",
      "args": ["@mcpservers/ragdocs"],
      "env": {
        "QDRANT_URL": "https://your-cluster-url.qdrant.tech",
        "QDRANT_API_KEY": "your-qdrant-api-key",
        "EMBEDDING_PROVIDER": "ollama"
      }
    }
  }
}
```

使用 OpenAI:
```json
{
  "mcpServers": {
    "ragdocs": {
      "command": "node",
      "args": ["@mcpservers/ragdocs"],
      "env": {
        "QDRANT_URL": "http://127.0.0.1:6333",
        "EMBEDDING_PROVIDER": "openai",
        "OPENAI_API_KEY": "your-api-key"
      }
    }
  }
}
```

## 本地 Qdrant 与 Docker

```bash
docker run -d --name qdrant -p 6333:6333 -p 6334:6334 qdrant/qdrant
```

## 环境变量

- `QDRANT_URL`：您的 Qdrant 实例的 URL
  - 对于本地："http://127.0.0.1:6333"（默认）
  - 对于云："https://your-cluster-url.qdrant.tech"
- `QDRANT_API_KEY`：Qdrant Cloud 的 API 密钥（使用云实例时必需）
- `EMBEDDING_PROVIDER`：选择嵌入提供者（"ollama" 或 "openai"，默认："ollama"）
- `OPENAI_API_KEY`：OpenAI API 密钥（如果使用 OpenAI 则必需）
- `EMBEDDING_MODEL`：用于嵌入的模型
  - 对于 Ollama：默认为 "nomic-embed-text"
  - 对于 OpenAI：默认为 "text-embedding-3-small"

## 许可证

Apache License 2.0

**官方网站：** [https://github.com/heltonteixeira/ragdocs](https://github.com/heltonteixeira/ragdocs)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`memory`
- 标签：`knowledge and memory`, `search`, `databases`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`@mcpservers/ragdocs`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/heltonteixeira-ragdocs.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
