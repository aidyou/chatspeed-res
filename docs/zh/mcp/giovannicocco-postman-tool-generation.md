---
title: "Postman AI工具生成器"
description: "一个MCP服务器，可以从Postman集合和请求生成AI代理工具。该服务器与Postman API集成，将API端点转换为类型安全的代码，这些代码可以与各种AI框架一起使用。"
---

# Postman AI工具生成器

一个MCP服务器，可以从Postman集合和请求生成AI代理工具。该服务器与Postman API集成，将API端点转换为类型安全的代码，这些代码可以与各种AI框架一起使用。

# Postman 工具生成 MCP 服务器

一个从 Postman 集合和请求生成 AI 代理工具的 MCP 服务器。此服务器与 Postman API 集成，将 API 端点转换为类型安全的代码，可以与各种 AI 框架一起使用。

模型上下文协议 (MCP) 是一种用于管理大型语言模型 (LLMs) 和外部系统之间上下文的[新标准化协议](https://modelcontextprotocol.io/introduction)。在此仓库中，我们提供了一个安装程序以及一个针对 [Postman 工具生成 API](https://api.getpostman.com/postbot/generations/tool) 的 MCP 服务器。

这使您可以使用 [Claude Desktop](https://claude.ai/download)，或任何像 [Cline](https://github.com/cline/cline) 这样的 MCP 客户端，通过自然语言在您的 Postman 账户上完成任务，例如：

* `为以下内容创建 AI 工具：
collectionID: 12345-abcde
requestID: 67890-fghij
typescript
openai`

## 特性

- 从 Postman 集合生成 TypeScript/JavaScript 代码
- 支持多个 AI 框架（OpenAI, Mistral, Gemini, Anthropic, LangChain, AutoGen）
- 类型安全的代码生成
- 错误处理和响应验证

## 演示

  

     alt="演示新发布的 MCP 服务器以探索 Postman 工具生成 API" width="600"/>
  

## 设置

1. 安装依赖项：
```bash
npm install
```

2. 构建服务器：
```bash
npm run build
```

3. 通过向您的 Claude 设置文件 (`cline_mcp_settings.json`) 添加以下内容来配置 MCP 设置：
```json
{
  "mcpServers": {
    "postman-ai-tools": {
      "command": "node",
      "args": [
        "/path/to/postman-tool-generation-server/build/index.js"
      ],
      "env": {
        "POSTMAN_API_KEY": "your-postman-api-key"
      },
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

## 使用

服务器提供了一个名为 `generate_ai_tool` 的工具，具有以下参数：

```typescript
{
  collectionId: string;    // The Public API Network collection ID
  requestId: string;       // The public request ID
  language: "javascript" | "typescript";  // Programming language to use
  agentFramework: "openai" | "mistral" | "gemini" | "anthropic" | "langchain" | "autogen";  // AI framework
}
```

### 示例

```typescript
// Using the tool through MCP
const result = await use_mcp_tool({
  server_name: "postman-ai-tools",
  tool_name: "generate_ai_tool",
  arguments: {
    collectionId: "your-collection-id",
    requestId: "your-request-id",
    language: "typescript",
    agentFramework: "openai"
  }
});
```

### 生成的代码

该工具生成的类型安全代码包括：

- 请求/响应的类型定义
- 错误处理
- API 集成
- OpenAI 函数定义
- 文档和示例

## 开发

1. 安装依赖项：
```bash
npm install
```

2. 对 `src/index.ts` 进行更改

3. 构建服务器：
```bash
npm run build
```

4. 重启 Claude 应用程序以加载更新后的服务器

## 环境变量

- `POSTMAN_API_KEY`: 您的 Postman API 密钥（必需）

## 错误处理

服务器包括以下方面的全面错误处理：
- 无效参数
- API 失败
- JSON 解析错误
- 网络问题

错误响应包含详细的错误信息，以帮助诊断问题。

## 贡献

欢迎贡献！请随时提交 Pull Request。

## 许可证

MIT 许可证

**官方网站：** [https://github.com/giovannicocco/mcp-server-postman-tool-generation](https://github.com/giovannicocco/mcp-server-postman-tool-generation)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`/path/to/postman-tool-generation-server/build/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/giovannicocco-postman-tool-generation.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
