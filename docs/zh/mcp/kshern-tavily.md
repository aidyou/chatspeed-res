---
title: "MCP内容搜索"
description: "一个支持使用Tavily API进行高级搜索和内容提取的模型上下文协议服务器，具有丰富的定制和集成选项。"
---

# MCP内容搜索

一个支持使用Tavily API进行高级搜索和内容提取的模型上下文协议服务器，具有丰富的定制和集成选项。

# MCP Tavily

[Smithery](https://smithery.ai/server/@kshern/mcp-tavily)

[中文文档](https://github.com/kshern/mcp-tavily/blob/HEAD/readme.zh-CN.md)

一个为 Tavily API 实现的 Model Context Protocol (MCP) 服务器，提供高级搜索和内容提取功能。

## 功能

- **多种搜索工具**：
  - `search`：具有可定制选项的基本搜索功能
  - `searchContext`：上下文感知搜索以提高相关性
  - `searchQNA`：专注于问答的搜索
- **内容提取**：从 URL 中提取内容，并支持配置选项
- **丰富的配置选项**：广泛的搜索深度、过滤和内容包含选项

### 使用 MCP

将 Tavily MCP 服务器添加到您的 MCP 配置中：

```json
{
  "mcpServers": {
    "tavily": {
      "command": "npx",
      "args": ["-y", "@mcptools/mcp-tavily"],
      "env": {
        "TAVILY_API_KEY": "your-api-key"
      }
    }
  }
}
```

> 注意：请确保将 `your-api-key` 替换为您实际的 Tavily API 密钥。您也可以在运行服务器之前将其设置为环境变量 `TAVILY_API_KEY`。

## API 参考

### 搜索工具

服务器通过 MCP 提供了三个可以调用的搜索工具：

#### 1. 基本搜索
```typescript
// Tool name: search
{
  query: "artificial intelligence",
  options: {
    searchDepth: "advanced",
    topic: "news",
    maxResults: 10
  }
}
```

#### 2. 上下文搜索
```typescript
// Tool name: searchContext
{
  query: "latest developments in AI",
  options: {
    topic: "news",
    timeRange: "week"
  }
}
```

#### 3. 问答搜索
```typescript
// Tool name: searchQNA
{
  query: "What is quantum computing?",
  options: {
    includeAnswer: true,
    maxResults: 5
  }
}
```

### 提取工具

```typescript
// Tool name: extract
{
  urls: ["https://example.com/article1", "https://example.com/article2"],
  options: {
    extractDepth: "advanced",
    includeImages: true
  }
}
```

### 搜索选项

所有搜索工具共享以下选项：

```typescript
interface SearchOptions {
  searchDepth?: "basic" | "advanced";    // Search depth level
  topic?: "general" | "news" | "finance"; // Search topic category
  days?: number;                         // Number of days to search
  maxResults?: number;                   // Maximum number of results
  includeImages?: boolean;               // Include images in results
  includeImageDescriptions?: boolean;    // Include image descriptions
  includeAnswer?: boolean;               // Include answer in results
  includeRawContent?: boolean;           // Include raw content
  includeDomains?: string[];            // List of domains to include
  excludeDomains?: string[];            // List of domains to exclude
  maxTokens?: number;                    // Maximum number of tokens
  timeRange?: "year" | "month" | "week" | "day" | "y" | "m" | "w" | "d"; // Time range for search
}
```

### 提取选项

```typescript
interface ExtractOptions {
  extractDepth?: "basic" | "advanced";   // Extraction depth level
  includeImages?: boolean;               // Include images in results
}
```

## 响应格式

所有工具返回的响应格式如下：

```typescript
{
  content: Array
}
```

对于搜索结果，每个条目包括：
- 标题
- 内容
- URL

对于提取的内容，每个条目包括：
- URL
- 原始内容
- 失败的 URL 列表（如果有）

## 错误处理

所有工具都包含适当的错误处理，并在出现问题时抛出描述性的错误消息。

## 安装

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@kshern/mcp-tavily) 自动安装适用于 Claude Desktop 的 Tavily API 服务器：

```bash
npx -y @smithery/cli install @kshern/mcp-tavily --client claude
```

### 手动安装
```bash
npm install @mcptools/mcp-tavily
```

或者直接使用 npx：

```bash
npx @mcptools/mcp-tavily
```

### 先决条件

- Node.js 16 或更高版本
- npm 或 yarn
- Tavily API 密钥（从 [Tavily](https://tavily.com) 获取）

### 设置

1. 克隆仓库
2. 安装依赖项：
```bash
npm install
```
3. 设置您的 Tavily API 密钥：
```bash
export TAVILY_API_KEY=your_api_key
```

### 构建

```bash
npm run build
```

## 使用 MCP Inspector 调试

对于开发和调试，我们推荐使用 [MCP Inspector](https://github.com/modelcontextprotocol/inspector)，这是一个强大的 MCP 服务器开发工具。

Inspector 提供了一个用户界面用于：
- 测试工具调用
- 查看服务器响应
- 调试工具执行
- 监控服务器状态

## 贡献

欢迎贡献！请随时提交 Pull Request。

1. 分叉仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

## 许可证

此项目根据 MIT 许可证发布。

## 支持

对于任何问题或问题：

- Tavily API: 请参考[Tavily文档](https://docs.tavily.com/)
- MCP集成: 请参考[MCP文档](https://modelcontextprotocol.io//)

**官方网站：** [https://github.com/kshern/mcp-tavily](https://github.com/kshern/mcp-tavily)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`browser`
- 标签：`search`, `browser automation`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @mcptools/mcp-tavily`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/kshern-tavily.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
