---
title: "WebSearch-MCP网络搜索服务器"
description: "一种模型上下文协议服务器，使人工智能助手能够进行实时网络搜索，通过爬虫API从互联网检索最新信息。"
---

# WebSearch-MCP网络搜索服务器

一种模型上下文协议服务器，使人工智能助手能够进行实时网络搜索，通过爬虫API从互联网检索最新信息。

# WebSearch-MCP

[Smithery](https://smithery.ai/server/@mnhlt/WebSearch-MCP)

这是一个通过标准输入输出传输提供网络搜索功能的 Model Context Protocol (MCP) 服务器实现。该服务器与 WebSearch 爬虫 API 集成以检索搜索结果。

## 目录

- [关于](#关于)
- [安装](#安装)
- [配置](#配置)
- [设置与集成](#设置与集成)
  - [设置爬虫服务](#设置爬虫服务)
    - [先决条件](#先决条件)
    - [启动爬虫服务](#启动爬虫服务)
    - [测试爬虫 API](#测试爬虫-api)
    - [自定义配置](#自定义配置)
  - [与 MCP 客户端集成](#与-mcp-客户端集成)
    - [快速参考：MCP 配置](#快速参考-mcp-配置)
    - [Claude Desktop](#claude-desktop)
    - [Cursor IDE](#cursor-ide)
    - [Cline](#cline-命令行接口-for-claude)
- [使用](#使用)
  - [参数](#参数)
  - [示例搜索响应](#示例搜索响应)
  - [本地测试](#本地测试)
  - [作为库使用](#作为库使用)
- [故障排除](#故障排除)
  - [爬虫服务问题](#爬虫服务问题)
  - [MCP 服务器问题](#mcp-服务器问题)
- [开发](#开发)
  - [项目结构](#项目结构)
  - [发布到 npm](#发布到-npm)
- [贡献](#贡献)
- [许可证](#许可证)

## 关于

WebSearch-MCP 是一个 Model Context Protocol 服务器，为支持 MCP 的 AI 助手提供网络搜索功能。它允许像 Claude 这样的 AI 模型实时搜索网络，获取任何主题的最新信息。

该服务器与处理实际网络搜索的爬虫 API 服务集成，并使用标准化的 Model Context Protocol 与 AI 助手通信。

## 安装

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@mnhlt/WebSearch-MCP) 自动为 Claude Desktop 安装 WebSearch：

```bash
npx -y @smithery/cli install @mnhlt/WebSearch-MCP --client claude
```

### 手动安装
```bash
npm install -g websearch-mcp
```

或者不安装直接使用：

```bash
npx websearch-mcp
```

## 配置

WebSearch MCP 服务器可以使用环境变量进行配置：

- `API_URL`：WebSearch 爬虫 API 的 URL（默认：`http://localhost:3001`）
- `MAX_SEARCH_RESULT`：未在请求中指定时返回的最大搜索结果数量（默认：`5`）

示例：
```bash
# Configure API URL
API_URL=https://crawler.example.com npx websearch-mcp

# Configure maximum search results
MAX_SEARCH_RESULT=10 npx websearch-mcp

# Configure both
API_URL=https://crawler.example.com MAX_SEARCH_RESULT=10 npx websearch-mcp
```

## 设置与集成

设置 WebSearch-MCP 包括两个主要部分：配置执行实际网络搜索的爬虫服务，以及将 MCP 服务器与您的 AI 客户端应用程序集成。

### 设置爬虫服务

WebSearch MCP 服务器需要一个爬虫服务来执行实际的网络搜索。您可以使用 Docker Compose 轻松设置爬虫服务。

### 先决条件

- [Docker](https://www.docker.com/get-started) 和 [Docker Compose](https://docs.docker.com/compose/install/)

### 启动爬虫服务

1. 创建一个名为 `docker-compose.yml` 的文件，内容如下：

```yaml
version: '3.8'

services:
  crawler:
    image: laituanmanh/websearch-crawler:latest
    container_name: websearch-api
    restart: unless-stopped
    ports:
      - "3001:3001"
    environment:
      - NODE_ENV=production
      - PORT=3001
      - LOG_LEVEL=info
      - FLARESOLVERR_URL=http://flaresolverr:8191/v1
    depends_on:
      - flaresolverr
    volumes:
      - crawler_storage:/app/storage

  flaresolverr:
    image: 21hsmw/flaresolverr:nodriver
    container_name: flaresolverr
    restart: unless-stopped
    environment:
      - LOG_LEVEL=info
      - TZ=UTC

volumes:
  crawler_storage:
```
针对 Mac Apple Silicon 的解决方法
```
version: '3.8'

services:
  crawler:
    image: laituanmanh/websearch-crawler:latest
    container_name: websearch-api
    platform: "linux/amd64"
    restart: unless-stopped
    ports:
      - "3001:3001"
    environment:
      - NODE_ENV=production
      - PORT=3001
      - LOG_LEVEL=info
      - FLARESOLVERR_URL=http://flaresolverr:8191/v1
    depends_on:
      - flaresolverr
    volumes:
      - crawler_storage:/app/storage

  flaresolverr:
    image: 21hsmw/flaresolverr:nodriver
    platform: "linux/arm64"
    container_name: flaresolverr
    restart: unless-stopped
    environment:
      - LOG_LEVEL=info
      - TZ=UTC

volumes:
  crawler_storage:
```

2. 启动服务：

```bash
docker-compose up -d
```

3. 验证服务是否正在运行：

```bash
docker-compose ps
```

4. 测试爬虫 API 健康端点：

```bash
curl http://localhost:3001/health
```

预期响应：
```json
{
  "status": "ok",
  "details": {
    "status": "ok",
    "flaresolverr": true,
    "google": true,
    "message": null
  }
}
```

爬虫 API 将在 `http://localhost:3001` 上可用。

### 测试爬虫 API

你可以直接使用 curl 来测试爬虫 API：

```bash
curl -X POST http://localhost:3001/crawl \
  -H "Content-Type: application/json" \
  -d '{
    "query": "typescript best practices",
    "numResults": 2,
    "language": "en",
    "filters": {
      "excludeDomains": ["youtube.com"],
      "resultType": "all" 
    }
  }'
```

### 自定义配置

你可以在 `docker-compose.yml` 文件中通过修改环境变量来自定义爬虫服务：

- `PORT`: 爬虫 API 监听的端口（默认：3001）
- `LOG_LEVEL`: 日志级别（选项：debug, info, warn, error）
- `FLARESOLVERR_URL`: FlareSolverr 服务的 URL（用于绕过 Cloudflare 保护）

## 与 MCP 客户端集成

### 快速参考：MCP 配置

以下是不同客户端的 MCP 配置快速参考：

```json
{
    "mcpServers": {
        "websearch": {
            "command": "npx",
            "args": [
                "websearch-mcp"
            ],
            "environment": {
                "API_URL": "http://localhost:3001",
                "MAX_SEARCH_RESULT": "5" // reduce to save your tokens, increase for wider information gain
            }
        }
    }
}
```

针对 Windows 的解决方法，由于 [问题](https://github.com/smithery-ai/mcp-obsidian/issues/19)
```
{
    "mcpServers": {
      "websearch": {
            "command": "cmd",
            "args": [
                "/c",
                "npx",
                "websearch-mcp"
            ],
            "environment": {
                "API_URL": "http://localhost:3001",
                "MAX_SEARCH_RESULT": "1"
            }
        }
    }
  }
```

## 使用

此包实现了一个使用 stdio 传输的 MCP 服务器，并暴露了一个带有以下参数的 `web_search` 工具：

### 参数

- `query` (必需): 要查找的搜索查询
- `numResults` (可选): 返回的结果数量（默认：5）
- `language` (可选): 搜索结果的语言代码（例如 'en'）
- `region` (可选): 搜索结果的地区代码（例如 'us'）
- `excludeDomains` (可选): 从结果中排除的域名
- `includeDomains` (可选): 结果中仅包含这些域名
- `excludeTerms` (可选): 从结果中排除的术语
- `resultType` (可选): 返回的结果类型 ('all', 'news', 或 'blogs')

### 示例搜索响应

这里是一个搜索响应示例：

```json
{
  "query": "machine learning trends",
  "results": [
    {
      "title": "Top Machine Learning Trends in 2025",
      "snippet": "The key machine learning trends for 2025 include multimodal AI, generative models, and quantum machine learning applications in enterprise...",
      "url": "https://example.com/machine-learning-trends-2025",
      "siteName": "AI Research Today",
      "byline": "Dr. Jane Smith"
    },
    {
      "title": "The Evolution of Machine Learning: 2020-2025",
      "snippet": "Over the past five years, machine learning has evolved from primarily supervised learning approaches to more sophisticated self-supervised and reinforcement learning paradigms...",
      "url": "https://example.com/ml-evolution",
      "siteName": "Tech Insights",
      "byline": "John Doe"
    }
  ]
}
```

### 本地测试

要本地测试 WebSearch MCP 服务器，你可以使用附带的测试客户端：

```bash
npm run test-client
```

这将启动 MCP 服务器和一个简单的命令行界面，允许你输入搜索查询并查看结果。

你还可以为测试客户端配置 API_URL：

```bash
API_URL=https://crawler.example.com npm run test-client
```

### 作为库使用

你可以以编程方式使用此包：

```typescript
import { createMCPClient } from '@modelcontextprotocol/sdk';

// Create an MCP client
const client = createMCPClient({
  transport: { type: 'subprocess', command: 'npx websearch-mcp' }
});

// Execute a web search
const response = await client.request({
  method: 'call_tool',
  params: {
    name: 'web_search',
    arguments: {
      query: 'your search query',
      numResults: 5,
      language: 'en'
    }
  }
});

console.log(response.result);
```

## 故障排除

### 爬虫服务问题

- **API 不可达**：确保爬虫服务正在运行并在配置的 API_URL 上可访问。
- **搜索结果不可用**：检查爬虫服务的日志以查看是否有任何错误：
```bash
  docker-compose logs crawler
```
- **FlareSolverr 问题**：一些网站使用了 Cloudflare 保护。如果看到与此相关的错误，请检查 FlareSolverr 是否工作正常：
```bash
  docker-compose logs flaresolverr
```

### MCP 服务器问题

- **导入错误**：确保您已安装最新版本的 MCP SDK：
```bash
  npm install -g @modelcontextprotocol/sdk@latest
```
- **连接问题**：确保您的客户端正确配置了 stdio 传输。

## 开发

要在这个项目上工作：

1. 克隆仓库
2. 安装依赖项：`npm install`
3. 构建项目：`npm run build`
4. 以开发模式运行：`npm run dev`

服务器期望一个如 swagger.json 文件中定义的 WebSearch Crawler API。请确保该 API 在配置的 API_URL 上运行。

### 项目结构

- `.gitignore`：指定 Git 应忽略的文件（如 node_modules、dist、logs 等）
- `.npmignore`：指定在发布到 npm 时不包含的文件
- `package.json`：项目元数据和依赖项
- `src/`：源 TypeScript 文件
- `dist/`：编译后的 JavaScript 文件（构建时生成）

### 发布到 npm

要将此包发布到 npm：

1. 确保您有 npm 账户并已登录 (`npm login`)
2. 更新 package.json 中的版本 (`npm version patch|minor|major`)
3. 运行 `npm publish`

`.npmignore` 文件确保只有必要的文件被包含在发布的包中：
- 编译后的代码在 `dist/` 目录下
- README.md 和 LICENSE 文件
- package.json

## 贡献

欢迎贡献！请随时提交 Pull Request。

## 许可证

ISC

**官方网站：** [https://github.com/mnhlt/WebSearch-MCP](https://github.com/mnhlt/WebSearch-MCP)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`browser`
- 标签：`search`, `browser automation`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`cmd`
- 参数：`/c npx websearch-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/mnhlt-websearch.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
