---
title: "向量化智能搜索"
description: "为高级检索、私有深度研究、任意文件转Markdown提取和文本分块矢量化MCP服务器。"
---

# 向量化智能搜索

为高级检索、私有深度研究、任意文件转Markdown提取和文本分块矢量化MCP服务器。

# Vectorize MCP 服务器

这是一个与 [Vectorize](https://vectorize.io/) 集成的 Model Context Protocol (MCP) 服务器实现，用于高级向量检索和文本提取。

  

## 安装

### 使用 npx 运行

```bash
export VECTORIZE_ORG_ID=YOUR_ORG_ID
export VECTORIZE_TOKEN=YOUR_TOKEN
export VECTORIZE_PIPELINE_ID=YOUR_PIPELINE_ID

npx -y @vectorize-io/vectorize-mcp-server@latest
```

## 在 Claude/Windsurf/Cursor/Cline 上配置

```json
{
  "mcpServers": {
    "vectorize": {
      "command": "npx",
      "args": ["-y", "@vectorize-io/vectorize-mcp-server@latest"],
      "env": {
        "VECTORIZE_ORG_ID": "your-org-id",
        "VECTORIZE_TOKEN": "your-token",
        "VECTORIZE_PIPELINE_ID": "your-pipeline-id"
      }
    }
  }
}
```

## 工具

### 检索文档

执行向量搜索并检索文档（参见官方 [API](https://docs.vectorize.io/api/api-pipelines/api-retrieval)）：

```json
{
  "name": "retrieve",
  "arguments": {
    "question": "Financial health of the company",
    "k": 5
  }
}
```

### 文本提取和分块（任何文件转为 Markdown 格式）

从文档中提取文本并将其分块为 Markdown 格式（参见官方 [API](https://docs.vectorize.io/api/api-extraction)）：

```json
{
  "name": "extract",
  "arguments": {
    "base64document": "base64-encoded-document",
    "contentType": "application/pdf"
  }
}
```

### 深度研究

从您的管道生成私有深度研究报告（参见官方 [API](https://docs.vectorize.io/api/api-pipelines/api-deep-research)）：

```json
{
  "name": "deep-research",
  "arguments": {
    "query": "Generate a financial status report about the company",
    "webSearch": true
  }
}
```

## 开发

```bash
npm install
npm run dev
```

### 贡献

1. 叉分仓库
2. 创建您的功能分支
3. 提交拉取请求

**官方网站：** [https://github.com/vectorize-io/vectorize-mcp-server](https://github.com/vectorize-io/vectorize-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`search`, `research and data`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @vectorize-io/vectorize-mcp-server@latest`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/vectorize-io-vectorize.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
