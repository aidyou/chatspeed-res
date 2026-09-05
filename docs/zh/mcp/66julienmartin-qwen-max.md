---
title: "MCP服务端-Qwen大模型"
description: "通过模型上下文协议（MCP），启用使用Qwen Max语言模型生成文本，该模型具有可配置参数，并与克劳德桌面无缝集成。"
---

# MCP服务端-Qwen大模型

通过模型上下文协议（MCP），启用使用Qwen Max语言模型生成文本，该模型具有可配置参数，并与克劳德桌面无缝集成。

# Qwen Max MCP 服务器

Qwen Max 语言模型的 Model Context Protocol (MCP) 服务器实现。

[Smithery](https://smithery.ai/server/@66julienmartin/mcp-server-qwen_max)

为什么选择 Node.js？
此实现使用了 Node.js/TypeScript，因为它目前提供了与 MCP 服务器相比其他语言（如 Python）更为稳定和可靠的集成。Node.js 的 MCP SDK 提供了更好的类型安全性、错误处理以及与 Claude Desktop 的兼容性。

## 前提条件

- Node.js (v18 或更高版本)
- npm
- Claude Desktop
- Dashscope API 密钥

## 安装

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@66julienmartin/mcp-server-qwen_max) 自动为 Claude Desktop 安装 Qwen Max MCP 服务器：

```bash
npx -y @smithery/cli install @66julienmartin/mcp-server-qwen_max --client claude
```

### 手动安装
```bash
git clone https://github.com/66julienmartin/mcp-server-qwen-max.git
cd Qwen_Max
npm install
```

## 模型选择
默认情况下，此服务器使用 Qwen-Max 模型。
Qwen 系列提供了几个具有不同功能的商业模型：

### Qwen-Max
提供最佳推理性能，特别是对于复杂和多步骤的任务。

上下文窗口：32,768 个令牌
- 最大输入：30,720 个令牌
- 最大输出：8,192 个令牌
- 价格：$0.0016/1K 令牌（输入），$0.0064/1K 令牌（输出）
- 免费配额：1 百万个令牌

可用版本：

- qwen-max (稳定版)
- qwen-max-latest (最新版)
- qwen-max-2025-01-25 (快照，也称为 qwen-max-0125 或 Qwen2.5-Max)

### Qwen-Plus
在性能、速度和成本之间取得平衡，适用于中等复杂度的任务。

上下文窗口：131,072 个令牌
- 最大输入：129,024 个令牌
- 最大输出：8,192 个令牌
- 价格：$0.0004/1K 令牌（输入），$0.0012/1K 令牌（输出）
- 免费配额：1 百万个令牌

可用版本：

- qwen-plus (稳定版)
- qwen-plus-latest (最新版)
- qwen-plus-2025-01-25 (快照，也称为 qwen-plus-0125)

### Qwen-Turbo
速度快且成本低，适合简单任务。

- 上下文窗口：1,000,000 个令牌
- 最大输入：1,000,000 个令牌
- 最大输出：8,192 个令牌
- 价格：$0.00005/1K 令牌（输入），$0.0002/1K 令牌（输出）
- 免费配额：1 百万个令牌

可用版本：

- qwen-turbo (稳定版)
- qwen-turbo-latest (最新版)
- qwen-turbo-2024-11-01 (快照，也称为 qwen-turbo-1101)

要修改模型，请在 `src/index.ts` 中更新模型名称：

```typescript
// For Qwen-Max (default)
model: "qwen-max"

// For Qwen-Plus
model: "qwen-plus"

// For Qwen-Turbo
model: "qwen-turbo"
```

有关可用模型的更多详细信息，请访问 Alibaba Cloud 模型文档 [https://www.alibabacloud.com/help/en/model-studio/getting-started/models?spm=a3c0i.23458820.2359477120.1.446c7d3f9LT0FY](https://www.alibabacloud.com/help/en/model-studio/getting-started/models?spm=a3c0i.23458820.2359477120.1.446c7d3f9LT0FY)。

## 项目结构
```
qwen-max-mcp/
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

1. 在项目根目录中创建一个 `.env` 文件：
```
DASHSCOPE_API_KEY=your-api-key-here
```

2. 更新 Claude Desktop 配置：
```json
{
  "mcpServers": {
    "qwen_max": {
      "command": "node",
      "args": ["/path/to/Qwen_Max/build/index.js"],
      "env": {
        "DASHSCOPE_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

## 开发

```bash
npm run dev     # Watch mode
npm run build   # Build
npm run start   # Start server
```

## 功能

- 使用 Qwen 模型生成文本
- 可配置参数（max_tokens, temperature）
- 错误处理
- 支持 MCP 协议
- Claude Desktop 集成
- 支持所有 Qwen 商业模型（Max, Plus, Turbo）
- 广泛的 token 上下文窗口

## API 使用

```typescript
// Example tool call
{
  "name": "qwen_max",
  "arguments": {
    "prompt": "Your prompt here",
    "max_tokens": 8192,
    "temperature": 0.7
  }
}
```
## 温度参数

温度参数控制模型输出的随机性：

较低值 (0.0-0.7)：更集中和确定性的输出
较高值 (0.7-1.0)：更具创造性和多样性的输出

按任务推荐的温度设置：

代码生成：0.0-0.3
技术写作：0.3-0.5
一般任务：0.7（默认）
创意写作：0.8-1.0

## 错误处理

服务器为常见问题提供了详细的错误信息：

API 认证错误
无效参数
速率限制
网络问题
超出 token 限制
模型可用性问题

## 贡献
欢迎贡献！请随时提交 Pull Request。

## 许可证
MIT

**官方网站：** [https://github.com/66julienmartin/MCP-server-Qwen_Max](https://github.com/66julienmartin/MCP-server-Qwen_Max)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`productivity`
- 标签：`other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`/path/to/Qwen_Max/build/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/66julienmartin-qwen-max.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
