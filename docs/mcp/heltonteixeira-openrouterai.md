---
title: "OpenRouter.ai 集成平台"
description: "提供了与OpenRouter.ai的集成，允许通过统一接口访问各种AI模型。"
---

# OpenRouter.ai 集成平台

提供了与OpenRouter.ai的集成，允许通过统一接口访问各种AI模型。

# OpenRouter MCP 服务器

[![MCP Server](/mcp-assets/cb56a0889b99f9bc45a0b547b9f87230.svg)](https://github.com/heltonteixeira/openrouterai)
![Version](/mcp-assets/d58b7f6784e65408fe1c317cfc0473dd.svg)
[![TypeScript](/mcp-assets/754e1918c2ab1fa621c9e6e01628f1e0.svg)](https://www.typescriptlang.org/)
![License](/mcp-assets/4159b5048650fda64b541eaec9d81bd1.svg)

这是一个模型上下文协议（MCP）服务器，提供与OpenRouter.ai多样化的模型生态系统的无缝集成。通过统一的、类型安全的接口访问各种AI模型，并内置缓存、速率限制和错误处理功能。

## 功能

- **模型访问**
  - 直接访问所有OpenRouter.ai模型
  - 自动模型验证和能力检查
  - 默认模型配置支持

- **性能优化**
  - 智能模型信息缓存（1小时过期）
  - 自动速率限制管理
  - 对失败请求使用指数退避策略

- **统一响应格式**
  - 所有响应的一致`ToolResult`结构
  - 使用`isError`标志明确识别错误
  - 带有上下文的结构化错误消息

## 安装

```bash
pnpm install @mcpservers/openrouterai
```

## 配置

### 先决条件

1. 从[OpenRouter 密钥](https://openrouter.ai/keys)获取您的OpenRouter API密钥
2. 选择一个默认模型（可选）

### 环境变量
```env
OPENROUTER_API_KEY=your-api-key-here
OPENROUTER_DEFAULT_MODEL=optional-default-model
```

### 设置

将以下内容添加到您的MCP设置配置文件 (`cline_mcp_settings.json` 或 `claude_desktop_config.json`) 中：

```json
{
  "mcpServers": {
    "openrouterai": {
      "command": "npx",
      "args": ["@mcpservers/openrouterai"],
      "env": {
        "OPENROUTER_API_KEY": "your-api-key-here",
        "OPENROUTER_DEFAULT_MODEL": "optional-default-model"
      }
    }
  }
}
```

## 响应格式

所有工具返回的响应都采用标准化结构：

```typescript
interface ToolResult {
  isError: boolean;
  content: Array;
}
```

**成功示例:**
```json
{
  "isError": false,
  "content": [{
    "type": "text",
    "text": "{\"id\": \"gen-123\", ...}"
  }]
}
```

**错误示例:**
```json
{
  "isError": true,
  "content": [{
    "type": "text",
    "text": "Error: Model validation failed - 'invalid-model' not found"
  }]
}
```

## 可用工具

### chat_completion

向OpenRouter.ai模型发送消息：

```typescript
interface ChatCompletionRequest {
  model?: string;
  messages: Array;
  temperature?: number; // 0-2
}

// Response: ToolResult with chat completion data or error
```

### search_models

搜索并筛选可用模型：

```typescript
interface ModelSearchRequest {
  query?: string;
  provider?: string;
  minContextLength?: number;
  capabilities?: {
    functions?: boolean;
    vision?: boolean;
  };
}

// Response: ToolResult with model list or error
```

### get_model_info

获取特定模型的详细信息：

```typescript
{
  model: string;           // Model identifier
}
```

### validate_model

检查模型ID是否有效：

```typescript
interface ModelValidationRequest {
  model: string;
}

// Response: 
// Success: { isError: false, valid: true }
// Error: { isError: true, error: "Model not found" }
```

## 错误处理

服务器提供带有上下文信息的结构化错误：

```typescript
// Error response structure
{
  isError: true,
  content: [{
    type: "text",
    text: "Error: [Category] - Detailed message"
  }]
}
```

**常见错误类别：**
- `Validation Error`: 无效的输入参数
- `API Error`: OpenRouter API通信问题
- `Rate Limit`: 请求限流检测
- `Internal Error`: 服务器端处理失败

**处理响应：**
```typescript
async function handleResponse(result: ToolResult) {
  if (result.isError) {
    const errorMessage = result.content[0].text;
    if (errorMessage.startsWith('Error: Rate Limit')) {
      // Handle rate limiting
    }
    // Other error handling
  } else {
    const data = JSON.parse(result.content[0].text);
    // Process successful response
  }
}
```

## 开发

参见 CONTRIBUTING.md 以获取关于以下方面的详细信息：
- 开发环境设置
- 项目结构
- 功能实现
- 错误处理指南
- 工具使用示例

```bash
# Install dependencies
pnpm install

# Build project
pnpm run build

# Run tests
pnpm test
```

## 更新日志
请参阅 CHANGELOG.md 了解最近的更新，包括：
- 统一响应格式的实现
- 增强的错误处理系统
- 类型安全接口的改进

## 许可证

该项目根据Apache许可证2.0版许可 - 详情请参阅 LICENSE 文件。

**官方网站：** [https://github.com/heltonteixeira/openrouterai](https://github.com/heltonteixeira/openrouterai)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`@mcpservers/openrouterai`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/heltonteixeira-openrouterai.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
