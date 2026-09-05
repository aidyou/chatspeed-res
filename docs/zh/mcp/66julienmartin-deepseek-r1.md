---
title: "MCP-Deepseek R1推理服务"
description: "用于Deepseek R1语言模型的Node.js/TypeScript实现的模型上下文协议服务器，针对具有大上下文窗口的推理任务进行了优化，并与Claude Desktop完全集成。"
---

# MCP-Deepseek R1推理服务

用于Deepseek R1语言模型的Node.js/TypeScript实现的模型上下文协议服务器，针对具有大上下文窗口的推理任务进行了优化，并与Claude Desktop完全集成。

# Deepseek R1 MCP 服务器

这是一个为 Deepseek R1 语言模型实现的模型上下文协议（MCP）服务器。Deepseek R1 是一个强大的语言模型，针对推理任务进行了优化，具有 8192 个令牌的上下文窗口。

为什么选择 Node.js？
这个实现使用了 Node.js/TypeScript，因为它提供了与 MCP 服务器最稳定的集成。Node.js SDK 提供了更好的类型安全性、错误处理以及与 Claude Desktop 的兼容性。

## 快速开始

### 手动安装
```bash
# Clone and install
git clone https://github.com/66julienmartin/MCP-server-Deepseek_R1.git
cd deepseek-r1-mcp
npm install

# Set up environment
cp .env.example .env  # Then add your API key

# Build and run
npm run build
```

## 前提条件

- Node.js (v18 或更高版本)
- npm
- Claude Desktop
- Deepseek API 密钥

## 模型选择

默认情况下，此服务器使用 **deepseek-R1** 模型。如果你想改用 **DeepSeek-V3**，请在 `src/index.ts` 中修改模型名称：

```typescript
// For DeepSeek-R1 (default)
model: "deepseek-reasoner"

// For DeepSeek-V3
model: "deepseek-chat"
```

## 项目结构

```
deepseek-r1-mcp/
├── src/
│   ├── index.ts             # Main server implementation
├── build/                   # Compiled files
│   ├── index.js
├── LICENSE
├── README.md
├── package.json
├── package-lock.json
└── tsconfig.json
```

## 配置

1. 创建一个 `.env` 文件：
```
DEEPSEEK_API_KEY=your-api-key-here
```

2. 更新 Claude Desktop 配置：
```json
{
  "mcpServers": {
    "deepseek_r1": {
      "command": "node",
      "args": ["/path/to/deepseek-r1-mcp/build/index.js"],
      "env": {
        "DEEPSEEK_API_KEY": "your-api-key"
      }
    }
  }
}
```

## 开发

```bash
npm run dev     # Watch mode
npm run build   # Build for production
```

## 特性

- 使用 Deepseek R1 进行高级文本生成（8192 个令牌的上下文窗口）
- 可配置参数（max_tokens, temperature）
- 具有详细错误信息的强大错误处理
- 完全支持 MCP 协议
- Claude Desktop 集成
- 支持 DeepSeek-R1 和 DeepSeek-V3 模型

## API 使用

```typescript
{
  "name": "deepseek_r1",
  "arguments": {
    "prompt": "Your prompt here",
    "max_tokens": 8192,    // Maximum tokens to generate
    "temperature": 0.2     // Controls randomness
  }
}
```

## 温度参数

`temperature` 的默认值是 0.2。

Deepseek 建议根据您的具体使用情况设置 `temperature`：

| 使用场景 | 温度 | 示例 |
|----------|-------------|---------|
| 编程 / 数学 | 0.0 | 代码生成，数学计算 |
| 数据清理 / 数据分析 | 1.0 | 数据处理任务 |
| 一般对话 | 1.3 | 聊天和对话 |
| 翻译 | 1.3 | 语言翻译 |
| 创意写作 / 诗歌 | 1.5 | 故事写作，诗歌生成 |

## 错误处理

服务器为常见问题提供详细的错误信息：
- API 认证错误
- 无效参数
- 速率限制
- 网络问题

## 贡献

欢迎贡献！请随时提交 Pull Request。

## 许可证

MIT

**官方网站：** [https://github.com/66julienmartin/MCP-server-Deepseek_R1](https://github.com/66julienmartin/MCP-server-Deepseek_R1)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`/path/to/deepseek-r1-mcp/build/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/66julienmartin-deepseek-r1.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
