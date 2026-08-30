---
title: "MCP上下文管理总结功能"
description: "通过一个清晰且可扩展的架构提供智能摘要功能。主要构建用于解决大型存储库中的人工智能代理问题，因为在大型存储库中，大文件可能会占用上下文窗口。"
---

# MCP上下文管理总结功能

通过一个清晰且可扩展的架构提供智能摘要功能。主要构建用于解决大型存储库中的人工智能代理问题，因为在大型存储库中，大文件可能会占用上下文窗口。

# 摘要功能

### 为 Model Context Protocol 提供智能文本摘要

[功能](#features) •
[AI 代理集成](#ai-agent-integration) •
[安装](#installation) •
[使用](#usage)

[Smithery](https://smithery.ai/server/mcp-summarization-functions)
[![npm 版本](/mcp-assets/b583c5f3726f8d2d2e609ea4aeba1926.svg)](https://www.npmjs.com/package/mcp-summarization-functions)

---

## 概述

一个强大的 MCP 服务器，通过简洁、可扩展的架构提供智能摘要功能。使用现代 TypeScript 构建，并设计用于与 AI 工作流无缝集成。

## 安装

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/mcp-summarization-functions) 自动安装 Claude Desktop 的摘要功能：

```bash
npx -y @smithery/cli install mcp-summarization-functions --client claude
```

```bash
npm i mcp-summarization-functions
```

## AI 代理集成

此 MCP 服务器主要开发用于增强像 Roo Cline 和 Cline 这样的 AI 代理的性能和可靠性。它解决了 AI 代理操作中的一个关键挑战：上下文窗口管理。

### 上下文窗口优化

AI 代理经常遇到其上下文窗口被以下内容迅速填满的情况：
- 命令执行结果
- 文件内容读取
- 目录列表
- API 响应
- 错误消息和堆栈跟踪

该服务器通过以下方式帮助维持高效的上下文使用：
1. 提供简洁的相关摘要而不是完整内容
2. 存储完整内容以备需要时参考
3. 根据具体需求（安全、API 表面等）提供专注的分析
4. 支持多种输出格式以优化上下文利用

### 对 AI 代理的好处

- **降低失败率**：通过防止上下文窗口溢出
- **提高响应质量**：通过专注的相关摘要
- **提高效率**：在减少噪音的同时保持重要上下文
- **更好的资源管理**：通过智能内容缓存和检索
- **灵活集成**：支持多个 AI 提供商和配置选项

### 推荐的 AI 代理提示

在与 AI 代理集成时，请在代理的指令中包含以下内容：

```
# CONTEXT MANAGEMENT

You have access to summarization functions through the MCP server. These functions are NOT optional - you MUST use them for ALL potentially large outputs to prevent context overflow:

MANDATORY SUMMARIZATION:
- You MUST ALWAYS use summarization functions for:
    - ANY first time file reading operations (unless you are CERTAIN its small and you are going to edit it)
    - ALL command execution outputs
    - EVERY directory analysis
    - ANY API responses or error logs
    - ANY output that could be large

NEVER attempt to process raw output directly - ALWAYS use the appropriate summarization function:
• For commands: summarize_command
• For files: summarize_files
• For directories: summarize_directory
• For other text: summarize_text

ALWAYS utilize available features:
• Specify hints for focused analysis
• Choose appropriate output formats
• Use content IDs to access full details only when absolutely necessary

There is NO NEED to process perfect or complete output. Summarized content is ALWAYS preferred over raw data. When in doubt, use summarization.
```

在 Ollama 仓库中实际应用摘要功能（Gemini 2.0 Flash 摘要，Claude 3.5 代理）

## 功能

- **命令输出摘要**  
  执行命令并获取其输出的简洁摘要

- **文件内容分析**  
  在保持技术准确性的同时，总结单个或多个文件

- **目录结构理解**  
  获取复杂目录结构的清晰概览

- **灵活的模型支持**
  使用来自不同提供商的模型

- **AI 代理上下文优化**
  通过智能摘要防止上下文窗口溢出并提高 AI 代理性能

## 配置

服务器通过环境变量支持多个 AI 提供商：

### 必需的环境变量

- `PROVIDER`: 要使用的AI提供商。支持的值：
        - `ANTHROPIC` - 来自Anthropic的Claude模型
        - `OPENAI` - 来自OpenAI的GPT模型
        - `OPENAI-COMPATIBLE` - 与OpenAI兼容的API（例如Azure）
        - `GOOGLE` - 来自Google的Gemini模型
- `API_KEY`: 所选提供商的API密钥

### 可选环境变量

- `MODEL_ID`: 使用的具体模型（默认为提供商的标准模型）
- `PROVIDER_BASE_URL`: 用于与OpenAI兼容提供商的自定义API端点
- `MAX_TOKENS`: 模型响应的最大令牌数（默认：1024）
- `SUMMARIZATION_CHAR_THRESHOLD`: 当需要总结时的字符计数阈值（默认：512）
- `SUMMARIZATION_CACHE_MAX_AGE`: 缓存持续时间，以毫秒为单位（默认：3600000 - 1小时）
- `MCP_WORKING_DIR` - 作为回退目录，尝试从中查找具有相对路径的文件

### 示例配置

```bash
# Anthropic Configuration
PROVIDER=ANTHROPIC
API_KEY=your-anthropic-key
MODEL_ID=claude-3-5-sonnet-20241022

# OpenAI Configuration
PROVIDER=OPENAI
API_KEY=your-openai-key
MODEL_ID=gpt-4-turbo-preview

# Azure OpenAI Configuration
PROVIDER=OPENAI-COMPATIBLE
API_KEY=your-azure-key
PROVIDER_BASE_URL=https://your-resource.openai.azure.com
MODEL_ID=your-deployment-name

# Google Configuration
PROVIDER=GOOGLE
API_KEY=your-google-key
MODEL_ID=gemini-2.0-flash-exp
```

## 使用方法

将服务器添加到您的MCP配置文件中：

```json
{
        "mcpServers": {
                "MUST_USE_summarization": {
                        "command": "node",
                        "args": ["path/to/summarization-functions/build/index.js"],
                        "env": {
                                "PROVIDER": "ANTHROPIC",
                                "API_KEY": "your-api-key",
                                "MODEL_ID": "claude-3-5-sonnet-20241022",
                "MCP_WORKING_DIR": "default_working_directory"
                        }
                }
        }
}
```

### 可用功能

该服务器提供以下摘要工具：

#### `summarize_command`
执行并总结命令输出。
```typescript
{
  // Required
  command: string,    // Command to execute
  cwd: string,       // Working directory for command execution
  
  // Optional
  hint?: string,      // Focus area: "security_analysis" | "api_surface" | "error_handling" | "dependencies" | "type_definitions"
  output_format?: string  // Format: "text" | "json" | "markdown" | "outline" (default: "text")
}
```

#### `summarize_files`
总结文件内容。
```typescript
{
  // Required
  paths: string[],    // Array of file paths to summarize (relative to cwd)
  cwd: string,       // Working directory for resolving file paths
  
  // Optional
  hint?: string,      // Focus area: "security_analysis" | "api_surface" | "error_handling" | "dependencies" | "type_definitions"
  output_format?: string  // Format: "text" | "json" | "markdown" | "outline" (default: "text")
}
```

#### `summarize_directory`
获取目录结构概览。
```typescript
{
  // Required
  path: string,       // Directory path to summarize (relative to cwd)
  cwd: string,       // Working directory for resolving directory path
  
  // Optional
  recursive?: boolean,  // Whether to include subdirectories. Safe for deep directories
  hint?: string,       // Focus area: "security_analysis" | "api_surface" | "error_handling" | "dependencies" | "type_definitions"
  output_format?: string   // Format: "text" | "json" | "markdown" | "outline" (default: "text")
}
```

#### `summarize_text`
总结任意文本内容。
```typescript
{
  // Required
  content: string,    // Text content to summarize
  type: string,       // Type of content (e.g., "log output", "API response")
  
  // Optional
  hint?: string,      // Focus area: "security_analysis" | "api_surface" | "error_handling" | "dependencies" | "type_definitions"
  output_format?: string  // Format: "text" | "json" | "markdown" | "outline" (default: "text")
}
```

#### `get_full_content`
根据给定的摘要ID检索完整内容。
```typescript
{
  // Required
  id: string         // ID of the stored content
}
```

## 许可证

MIT

**官方网站：** [https://github.com/Braffolk/MCP-summarization-functions](https://github.com/Braffolk/MCP-summarization-functions)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`memory`, `data`
- 标签：`research and data`, `developer tools`, `knowledge and memory`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`path/to/summarization-functions/build/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/braffolk-summarization-functions.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
