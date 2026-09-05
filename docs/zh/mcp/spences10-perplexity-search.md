---
title: "Perplexity 智能搜索"
description: "启用 Perplexity 的 AI API 与大语言模型的集成，通过使用专门的提示模板来实现高级聊天补全，适用于技术文档、代码审查和 API 文档等任务。"
---

# Perplexity 智能搜索

启用 Perplexity 的 AI API 与大语言模型的集成，通过使用专门的提示模板来实现高级聊天补全，适用于技术文档、代码审查和 API 文档等任务。

# mcp-perplexity-search

---

## ⚠️ 通知

**此仓库不再维护。**

该工具的功能现已整合到 [mcp-omnisearch](https://github.com/spences10/mcp-omnisearch) 中，后者将多个 MCP 工具合并为一个统一的包。

请改用 [mcp-omnisearch](https://github.com/spences10/mcp-omnisearch)。

---

这是一个用于将 Perplexity 的 AI API 与大型语言模型 (LLMs) 集成的 Model Context Protocol (MCP) 服务器。该服务器提供了先进的聊天完成能力，并为各种使用场景提供了专门的提示模板。

  

## 特性

- 🤖 使用 Perplexity 的 AI 模型进行高级聊天完成
- 📝 常见场景预定义提示模板：
  - 技术文档生成
  - 安全最佳实践分析
  - 代码审查和改进
  - 结构化格式的 API 文档
- 🎯 支持自定义模板以满足特定需求
- 📊 多种输出格式（文本、Markdown、JSON）
- 🔍 可选在响应中包含源 URL
- ⚙️ 可配置的模型参数（温度、最大令牌数）
- 🚀 支持多种 Perplexity 模型，包括 Sonar 和 LLaMA

## 配置

此服务器需要通过您的 MCP 客户端进行配置。以下是不同环境下的示例：

### Cline 配置

将以下内容添加到您的 Cline MCP 设置中：

```json
{
    "mcpServers": {
        "mcp-perplexity-search": {
            "command": "npx",
            "args": ["-y", "mcp-perplexity-search"],
            "env": {
                "PERPLEXITY_API_KEY": "your-perplexity-api-key"
            }
        }
    }
}
```

### Claude Desktop with WSL 配置

对于 WSL 环境，请将以下内容添加到您的 Claude Desktop 配置中：

```json
{
    "mcpServers": {
        "mcp-perplexity-search": {
            "command": "wsl.exe",
            "args": [
                "bash",
                "-c",
                "source ~/.nvm/nvm.sh && PERPLEXITY_API_KEY=your-perplexity-api-key /home/username/.nvm/versions/node/v20.12.1/bin/npx mcp-perplexity-search"
            ]
        }
    }
}
```

### 环境变量

服务器需要以下环境变量：

- `PERPLEXITY_API_KEY`: 您的 Perplexity API 密钥（必需）

## API

服务器实现了一个带有可配置参数的单个 MCP 工具：

### chat_completion

使用 Perplexity API 生成聊天完成，并支持专门的提示模板。

参数：

- `messages` (数组, 必需): 包含消息对象的数组，每个对象包含：
  - `role` (字符串): 'system', 'user', 或 'assistant'
  - `content` (字符串): 消息内容
- `prompt_template` (字符串, 可选): 要使用的预定义模板：
  - `technical_docs`: 带有代码示例的技术文档
  - `security_practices`: 安全实施指南
  - `code_review`: 代码分析和改进
  - `api_docs`: JSON 格式的 API 文档
- `custom_template` (对象, 可选): 自定义提示模板，包含：
  - `system` (字符串): 助手行为的系统消息
  - `format` (字符串): 输出格式偏好
  - `include_sources` (布尔值): 是否包含来源
- `format` (字符串, 可选): 'text', 'markdown', 或 'json' (默认: 'text')
- `include_sources` (布尔值, 可选): 包含源 URL (默认: false)
- `model` (字符串, 可选): 要使用的 Perplexity 模型 (默认: 'sonar')
- `temperature` (数字, 可选): 输出随机性 (0-1, 默认: 0.7)
- `max_tokens` (数字, 可选): 最大响应长度 (默认: 1024)

## 开发

### 设置

1. 克隆仓库
2. 安装依赖项：

```bash
pnpm install
```

3. 构建项目：

```bash
pnpm build
```

4. 以开发模式运行：

```bash
pnpm dev
```

### 发布

该项目使用 changesets 进行版本管理。要发布，请执行以下步骤：

1. 创建一个 changeset：

```bash
pnpm changeset
```

2. 对包进行版本控制：

```bash
pnpm changeset version
```

3. 发布到 npm：

```bash
pnpm release
```

## 贡献

欢迎贡献！请随时提交 Pull Request。

## 许可证

MIT 许可证 - 详情请参阅 [LICENSE](https://github.com/spences10/mcp-perplexity-search/blob/HEAD/LICENSE) 文件。

## 致谢

- 基于 [Model Context Protocol](https://github.com/modelcontextprotocol)
- 由 [Perplexity SONAR](https://docs.perplexity.ai/api-reference/chat-completions) 提供支持

**官方网站：** [https://github.com/spences10/mcp-perplexity-search](https://github.com/spences10/mcp-perplexity-search)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`, `development`
- 标签：`search`, `developer tools`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y mcp-perplexity-search`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/spences10-perplexity-search.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
