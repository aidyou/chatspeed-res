---
title: "FireCrawl网络抓取服务器"
description: "一个模型上下文协议（MCP）服务器实现，它与FireCrawl集成以实现高级网络爬取功能。"
---

# FireCrawl网络抓取服务器

一个模型上下文协议（MCP）服务器实现，它与FireCrawl集成以实现高级网络爬取功能。

# Firecrawl MCP 服务器

一个与 [Firecrawl](https://github.com/mendableai/firecrawl) 集成的模型上下文协议 (MCP) 服务器实现，用于网络爬虫功能。

特别感谢 [@vrknetha](https://github.com/vrknetha) 和 [@cawstudios](https://caw.tech) 的初始实现！

## 功能

- 支持抓取、爬行、搜索、提取、深度研究和批量抓取
- 带有 JS 渲染的网页抓取
- URL 发现和爬行
- 带内容提取的网页搜索
- 指数退避自动重试
- - 内置限流的高效批量处理
- 云 API 使用额度监控
- 全面的日志系统
- 支持云托管和自托管的 FireCrawl 实例
- 移动/桌面视口支持
- 智能内容过滤，包括标签包含/排除

## 安装

### 使用 npx 运行

```bash
env FIRECRAWL_API_KEY=fc-YOUR_API_KEY npx -y firecrawl-mcp
```

### 手动安装

```bash
npm install -g firecrawl-mcp
```

### 在 Cursor 上运行

配置 Cursor 🖥️
注意：需要 Cursor 版本 0.45.6+

要在 Cursor 中配置 FireCrawl MCP：

1. 打开 Cursor 设置
2. 转到功能 > MCP 服务器
3. 点击 "+ 添加新的 MCP 服务器"
4. 输入以下内容：
   - 名称: "firecrawl-mcp"（或您喜欢的名称）
   - 类型: "命令"
   - 命令: `env FIRECRAWL_API_KEY=your-api-key npx -y firecrawl-mcp`

> 如果您使用的是 Windows 并遇到问题，请尝试 `cmd /c "set FIRECRAWL_API_KEY=your-api-key && npx -y firecrawl-mcp"`

将 `your-api-key` 替换为您的 FireCrawl API 密钥。

添加后，刷新 MCP 服务器列表以查看新工具。作曲家代理将在适当的时候自动使用 FireCrawl MCP，但您也可以通过描述您的网络抓取需求来明确请求它。通过 Command+L（Mac）访问作曲家，在提交按钮旁边的“代理”中选择，并输入您的查询。

### 在 Windsurf 上运行

将以下内容添加到您的 `./codeium/windsurf/model_config.json` 文件中：

```json
{
  "mcpServers": {
    "mcp-server-firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "YOUR_API_KEY_HERE"
      }
    }
  }
}
```

### 通过 Smithery（旧版）安装

要通过 [Smithery](https://smithery.ai/server/@mendableai/mcp-server-firecrawl) 自动安装 Claude Desktop 的 FireCrawl：

```bash
npx -y @smithery/cli install @mendableai/mcp-server-firecrawl --client claude
```

## 配置

### 环境变量

#### 云 API 必需

- `FIRECRAWL_API_KEY`: 您的 FireCrawl API 密钥
  - 使用云 API 时必需（默认）
  - 当使用带有 `FIRECRAWL_API_URL` 的自托管实例时可选
- `FIRECRAWL_API_URL`（可选）: 自托管实例的自定义 API 端点
  - 例如: `https://firecrawl.your-domain.com`
  - 如果未提供，则将使用云 API（需要 API 密钥）

#### 可选配置

##### 重试配置

- `FIRECRAWL_RETRY_MAX_ATTEMPTS`: 最大重试次数（默认: 3）
- `FIRECRAWL_RETRY_INITIAL_DELAY`: 第一次重试前的初始延迟（毫秒，默认: 1000）
- `FIRECRAWL_RETRY_MAX_DELAY`: 重试之间的最大延迟（毫秒，默认: 10000）
- `FIRECRAWL_RETRY_BACKOFF_FACTOR`: 指数退避乘数（默认: 2）

##### 使用额度监控

- `FIRECRAWL_CREDIT_WARNING_THRESHOLD`: 信用使用警告阈值（默认：1000）
- `FIRECRAWL_CREDIT_CRITICAL_THRESHOLD`: 信用使用严重阈值（默认：100）

### 配置示例

对于使用自定义重试和信用监控的云 API：

```bash
# Required for cloud API
export FIRECRAWL_API_KEY=your-api-key

# Optional retry configuration
export FIRECRAWL_RETRY_MAX_ATTEMPTS=5        # Increase max retry attempts
export FIRECRAWL_RETRY_INITIAL_DELAY=2000    # Start with 2s delay
export FIRECRAWL_RETRY_MAX_DELAY=30000       # Maximum 30s delay
export FIRECRAWL_RETRY_BACKOFF_FACTOR=3      # More aggressive backoff

# Optional credit monitoring
export FIRECRAWL_CREDIT_WARNING_THRESHOLD=2000    # Warning at 2000 credits
export FIRECRAWL_CREDIT_CRITICAL_THRESHOLD=500    # Critical at 500 credits
```

对于自托管实例：

```bash
# Required for self-hosted
export FIRECRAWL_API_URL=https://firecrawl.your-domain.com

# Optional authentication for self-hosted
export FIRECRAWL_API_KEY=your-api-key  # If your instance requires auth

# Custom retry configuration
export FIRECRAWL_RETRY_MAX_ATTEMPTS=10
export FIRECRAWL_RETRY_INITIAL_DELAY=500     # Start with faster retries
```

### 与 Claude Desktop 一起使用

将以下内容添加到您的 `claude_desktop_config.json` 中：

```json
{
  "mcpServers": {
    "mcp-server-firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "YOUR_API_KEY_HERE",

        "FIRECRAWL_RETRY_MAX_ATTEMPTS": "5",
        "FIRECRAWL_RETRY_INITIAL_DELAY": "2000",
        "FIRECRAWL_RETRY_MAX_DELAY": "30000",
        "FIRECRAWL_RETRY_BACKOFF_FACTOR": "3",

        "FIRECRAWL_CREDIT_WARNING_THRESHOLD": "2000",
        "FIRECRAWL_CREDIT_CRITICAL_THRESHOLD": "500"
      }
    }
  }
}
```

### 系统配置

服务器包括几个可通过环境变量设置的可配置参数。如果未配置，以下是默认值：

```typescript
const CONFIG = {
  retry: {
    maxAttempts: 3, // Number of retry attempts for rate-limited requests
    initialDelay: 1000, // Initial delay before first retry (in milliseconds)
    maxDelay: 10000, // Maximum delay between retries (in milliseconds)
    backoffFactor: 2, // Multiplier for exponential backoff
  },
  credit: {
    warningThreshold: 1000, // Warn when credit usage reaches this level
    criticalThreshold: 100, // Critical alert when credit usage reaches this level
  },
};
```

这些配置控制：

1. **重试行为**

   - 自动重试因速率限制而失败的请求
   - 使用指数退避以避免对 API 造成过大压力
   - 示例：使用默认设置时，重试将在以下时间进行：
     - 第一次重试：延迟1秒
     - 第二次重试：延迟2秒
     - 第三次重试：延迟4秒（最大延迟为 maxDelay）

2. **信用使用监控**
   - 跟踪云 API 使用情况下的 API 信用消耗
   - 在指定阈值处提供警告
   - 帮助防止意外服务中断
   - 示例：使用默认设置时：
     - 当剩余信用为1000时发出警告
     - 当剩余信用为100时发出严重警报

### 速率限制和批量处理

服务器利用 FireCrawl 的内置速率限制和批量处理功能：

- 自动处理速率限制，并采用指数退避
- 对批量操作进行高效的并行处理
- 智能请求排队和节流
- 对瞬态错误自动重试

## 可用工具

### 1. 抓取工具 (`firecrawl_scrape`)

从单个 URL 抓取内容，并具有高级选项。

```json
{
  "name": "firecrawl_scrape",
  "arguments": {
    "url": "https://example.com",
    "formats": ["markdown"],
    "onlyMainContent": true,
    "waitFor": 1000,
    "timeout": 30000,
    "mobile": false,
    "includeTags": ["article", "main"],
    "excludeTags": ["nav", "footer"],
    "skipTlsVerification": false
  }
}
```

### 2. 批量抓取工具 (`firecrawl_batch_scrape`)

使用内置速率限制和并行处理高效地抓取多个 URL。

```json
{
  "name": "firecrawl_batch_scrape",
  "arguments": {
    "urls": ["https://example1.com", "https://example2.com"],
    "options": {
      "formats": ["markdown"],
      "onlyMainContent": true
    }
  }
}
```

响应中包含用于状态检查的操作 ID：

```json
{
  "content": [
    {
      "type": "text",
      "text": "Batch operation queued with ID: batch_1. Use firecrawl_check_batch_status to check progress."
    }
  ],
  "isError": false
}
```

### 3. 检查批量状态 (`firecrawl_check_batch_status`)

检查批量操作的状态。

```json
{
  "name": "firecrawl_check_batch_status",
  "arguments": {
    "id": "batch_1"
  }
}
```

### 4. 搜索工具 (`firecrawl_search`)

搜索网络并可选地从搜索结果中提取内容。

```json
{
  "name": "firecrawl_search",
  "arguments": {
    "query": "your search query",
    "limit": 5,
    "lang": "en",
    "country": "us",
    "scrapeOptions": {
      "formats": ["markdown"],
      "onlyMainContent": true
    }
  }
}
```

### 5. 爬取工具 (`firecrawl_crawl`)

开始一个带有高级选项的异步爬取。

```json
{
  "name": "firecrawl_crawl",
  "arguments": {
    "url": "https://example.com",
    "maxDepth": 2,
    "limit": 100,
    "allowExternalLinks": false,
    "deduplicateSimilarURLs": true
  }
}
```

### 6. 提取工具 (`firecrawl_extract`)

使用 LLM 功能从网页中提取结构化信息。支持云端 AI 和自托管 LLM 提取。

```json
{
  "name": "firecrawl_extract",
  "arguments": {
    "urls": ["https://example.com/page1", "https://example.com/page2"],
    "prompt": "Extract product information including name, price, and description",
    "systemPrompt": "You are a helpful assistant that extracts product information",
    "schema": {
      "type": "object",
      "properties": {
        "name": { "type": "string" },
        "price": { "type": "number" },
        "description": { "type": "string" }
      },
      "required": ["name", "price"]
    },
    "allowExternalLinks": false,
    "enableWebSearch": false,
    "includeSubdomains": false
  }
}
```

示例响应：

```json
{
  "content": [
    {
      "type": "text",
      "text": {
        "name": "Example Product",
        "price": 99.99,
        "description": "This is an example product description"
      }
    }
  ],
  "isError": false
}
```

#### 提取工具选项：

- `urls`: 要从中提取信息的 URL 数组
- `prompt`: 用于 LLM 提取的自定义提示
- `systemPrompt`: 引导 LLM 的系统提示
- `schema`: 结构化数据提取的 JSON 模式
- `allowExternalLinks`: 允许从外部链接提取
- `enableWebSearch`: 启用网络搜索以获取额外上下文
- `includeSubdomains`: 在提取中包含子域

当使用自托管实例时，提取将使用您配置的LLM。对于云API，它使用FireCrawl管理的LLM服务。

### 7. 深度研究工具 (firecrawl_deep_research)
利用智能爬取、搜索和LLM分析对查询进行深度网络研究。

```json
{
  "name": "firecrawl_deep_research",
  "arguments": {
    "query": "how does carbon capture technology work?",
    "maxDepth": 3,
    "timeLimit": 120,
    "maxUrls": 50
  }
}
```

参数：
- query (字符串, 必需): 要探索的研究问题或主题。
- maxDepth (数字, 可选): 爬取/搜索的最大递归深度（默认：3）。
- timeLimit (数字, 可选): 研究会话的时间限制（秒，默认：120）。
- maxUrls (数字, 可选): 分析的最大URL数量（默认：50）。

返回：

- 基于研究生成的最终分析。(data.finalAnalysis)
- 还可能包括研究过程中使用的结构化活动和来源。

### 8. 生成 LLMs.txt 工具 (firecrawl_generate_llmstxt)
为给定域名生成标准化的llms.txt文件（可选地还包括llms-full.txt）。此文件定义了大型语言模型应如何与站点交互。

```json
{
  "name": "firecrawl_generate_llmstxt",
  "arguments": {
    "url": "https://example.com",
    "maxUrls": 20,
    "showFullText": true
  }
}
```

参数：

- url (字符串, 必需): 要分析网站的基础URL。
- maxUrls (数字, 可选): 包含的最大URL数量（默认：10）。
- showFullText (布尔值, 可选): 是否在响应中包含llms-full.txt内容。

返回：
- 生成的llms.txt文件内容，可选地还包括llms-full.txt (data.llmstxt 和/或 data.llmsfulltxt)

## 日志系统

服务器包含了全面的日志记录：

- 操作状态和进度
- 性能指标
- 信用使用监控
- 速率限制跟踪
- 错误条件

示例日志消息：

```
[INFO] FireCrawl MCP Server initialized successfully
[INFO] Starting scrape for URL: https://example.com
[INFO] Batch operation queued with ID: batch_1
[WARNING] Credit usage has reached warning threshold
[ERROR] Rate limit exceeded, retrying in 2s...
```

## 错误处理

服务器提供了强大的错误处理机制：

- 对瞬态错误自动重试
- 采用退避策略处理速率限制
- 详细的错误信息
- 信用使用警告
- 网络弹性

示例错误响应：

```json
{
  "content": [
    {
      "type": "text",
      "text": "Error: Rate limit exceeded. Retrying in 2 seconds..."
    }
  ],
  "isError": true
}
```

## 开发

```bash
# Install dependencies
npm install

# Build
npm run build

# Run tests
npm test
```

### 贡献指南

1. Fork仓库
2. 创建你的特性分支
3. 运行测试: `npm test`
4. 提交Pull Request

## 许可证

MIT许可证 - 详情请参阅LICENSE文件

**官方网站：** [https://github.com/vrknetha/mcp-server-firecrawl](https://github.com/vrknetha/mcp-server-firecrawl)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`browser`
- 标签：`browser automation`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y firecrawl-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/mendableai-firecrawl.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
