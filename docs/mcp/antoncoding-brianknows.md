---
title: "mcp-brianknows区块链知识库服务器"
description: "一个MCP服务器，它将克劳德连接到布莱恩诺尔斯的区块链知识库，允许用户搜索区块链/DeFi信息，并与跨多个知识库的专业代理进行交互。"
---

# mcp-brianknows区块链知识库服务器

一个MCP服务器，它将克劳德连接到布莱恩诺尔斯的区块链知识库，允许用户搜索区块链/DeFi信息，并与跨多个知识库的专业代理进行交互。

# BrianKnows MCP 服务器
[Smithery](https://smithery.ai/server/@antoncoding/mcp-brianknows)

这是一个 Model Context Protocol (MCP) 服务器，它将 Claude 连接到 BrianKnows 的区块链知识库。

  

## 什么是 MCP？🤔

Model Context Protocol (MCP) 允许像 Claude Desktop 这样的 AI 助手以安全的方式连接到外部工具和数据源，同时保持用户控制。

## 这个服务器做什么？🚀

BrianKnows MCP 服务器提供了三个主要工具：

1. **Ping 工具**：检查 BrianKnows API 服务器是否响应
2. **搜索工具**：查询 BrianKnows 知识引擎以获取区块链和 DeFi 信息
3. **代理工具**：与 BrianKnows 代理聊天关于 DeFi 协议的信息

支持的知识库包括：
- public-knowledge-box（默认）
- circle_kb, lido_kb, Polygon_kb, taiko_kb
- near_kb, clave_kb, starknet_kb, consensys_kb

服务器会缓存您最近的 5 次搜索，以便快速参考。

## 前提条件 📋

- [Node.js](https://nodejs.org/)（v18 或更高版本）
- [Claude Desktop](https://claude.ai/download)
- 一个 [BrianKnows API 密钥](https://docs.brianknows.org/)

## 配置 ⚙️

在您的 Claude Desktop 配置文件（通过开发者设置访问）中添加以下内容：

```json
{
  "mcpServers": {
    "brianknows": {
      "command": "npx",
      "args": ["mcp-brianknows"],
      "env": {
        "BRIAN_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

将 `your-api-key-here` 替换为您的实际 BrianKnows API 密钥。

## 示例用法 🎯

```
Can you check if the BrianKnows API is online?

Use BrianKnows to search for information about Ethereum's Layer 2 solutions.

Ask the BrianKnows agent to explain how Uniswap V3 works.
```

## 特性 ✨

* **多个知识库**：访问不同区块链协议的专业知识
* **缓存搜索**：快速访问您最近的 5 次搜索
* **错误处理**：用户友好的错误消息
* **类型安全**：完整的 TypeScript 实现

## 致谢 🙏

* [BrianKnows](https://brianknows.org) 提供他们的区块链知识 API
* [Model Context Protocol](https://modelcontextprotocol.io)
* [Anthropic](https://anthropic.com) 提供 Claude Desktop

**官方网站：** [https://github.com/antoncoding/mcp-brianknows](https://github.com/antoncoding/mcp-brianknows)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`finance`
- 标签：`search`, `knowledge and memory`, `finance`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`mcp-brianknows`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/antoncoding-brianknows.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
