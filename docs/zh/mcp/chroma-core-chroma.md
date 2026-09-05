---
title: "Chroma MCP"
description: "Chroma - the open-source embedding database . The fastest way to build Python or JavaScript LLM apps with memory! Docs Homepage Chroma MCP Server The Model Context Protocol (MCP) is an open protocol d…"
---

# Chroma MCP

Chroma - the open-source embedding database . The fastest way to build Python or JavaScript LLM apps with memory! Docs Homepage Chroma MCP Server The Model Context Protocol (MCP) is an open protocol d…

Chroma - the open-source embedding database
. 

    The fastest way to build Python or JavaScript LLM apps with memory!

  

      

  
 |
  

      

  
 |
  

      Docs
  
 |
  

      Homepage
  

# Chroma MCP Server


[The Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) is an open protocol designed for effortless integration between LLM applications and external data sources or tools, offering a standardized framework to seamlessly provide LLMs with the context they require.

This server provides data retrieval capabilities powered by Chroma, enabling AI models to create collections over generated data and user inputs, and retrieve that data using vector search, full text search, metadata filtering, and more.

This is a MCP server for self-hosting your access to Chroma. If you are looking for [Package Search](https://www.trychroma.com/package-search) you can find the repository for that [here](https://github.com/chroma-core/package-search).

## Features

- **Flexible Client Types**
  - Ephemeral (in-memory) for testing and development
  - Persistent for file-based storage
  - HTTP client for self-hosted Chroma instances
  - Cloud client for Chroma Cloud integration (automatically connects to api.trychroma.com)

- **Collection Management**
  - Create, modify, and delete collections
  - List all collections with pagination support
  - Get collection information and statistics
  - Configure HNSW parameters for optimized vector search
  - Select embedding functions when creating collections

- **Document Operations**
  - Add documents with optional metadata and custom IDs
  - Query documents using semantic search
  - Advanced filtering using metadata and document content
  - Retrieve documents by IDs or filters
  - Full text search capabilities

### Supported Tools

- `chroma_list_collections` - List all collections with pagination support
- `chroma_create_collection` - Create a new collection with optional HNSW configuration
- `chroma_peek_collection` - View a sample of documents in a collection
- `chroma_get_collection_info` - Get detailed information about a collection
- `chroma_get_collection_count` - Get the number of documents in a collection
- `chroma_modify_collection` - Update a collection's name or metadata
- `chroma_delete_collection` - Delete a collection
- `chroma_add_documents` - Add documents with optional metadata and custom IDs
- `chroma_query_documents` - Query documents using semantic search with advanced filtering
- `chroma_get_documents` - Retrieve documents by IDs or filters with pagination
- `chroma_update_documents` - Update existing documents' content, metadata, or embeddings
- `chroma_delete_documents` - Delete specific documents from a collection

### Embedding Functions
Chroma MCP supports several embedding functions: `default`, `cohere`, `openai`, `jina`, `voyageai`, and `roboflow`.

The embedding functions utilize Chroma's collection configuration, which persists the selected embedding function of a collection for retrieval. Once a collection is created using the collection configuration, on retrieval for future queries and inserts, the same embedding function will be used, without needing to specify the embedding function again. Embedding function persistance was added in v1.0.0 of Chroma, so if you created a collection using version _API_KEY=""`.
So to set a Cohere API key, set the environment variable `CHROMA_COHERE_API_KEY=""`. We recommend adding this to a .env file somewhere and using the `CHROMA_DOTENV_PATH` environment variable or `--dotenv-path` flag to set that location for safekeeping.

**官方网站：** [https://github.com/chroma-core/chroma-mcp](https://github.com/chroma-core/chroma-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`, `memory`
- 标签：`vector database`, `chroma`, `memory`, `rag`, `official`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`mcp-server-chroma`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/chroma-core-chroma.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
