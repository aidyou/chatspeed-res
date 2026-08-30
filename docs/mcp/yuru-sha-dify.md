---
title: "Dify对话服务"
description: "启用大型语言模型与Dify AI的聊天补全API进行交互，包括对话上下文支持和餐厅推荐工具。"
---

# Dify对话服务

启用大型语言模型与Dify AI的聊天补全API进行交互，包括对话上下文支持和餐厅推荐工具。

# mcp-server-dify
[![CI Status](/mcp-assets/90f677fd1e0f984b06982d3cb0c83958.svg)](https://github.com/yuru-sha/mcp-server-dify/actions)

用于Dify AI的模型上下文协议服务器。此服务器通过标准化协议使LLMs能够与Dify AI的聊天完成功能进行交互。

## 特性

- 与Dify AI聊天完成API集成
- 餐厅推荐工具（meshi-doko）
- 支持对话上下文
- 支持流式响应
- 使用TypeScript实现

## 安装

### 使用Docker

```bash
# Build the Docker image
make docker

# Run with Docker
docker run -i --rm mcp/dify https://your-dify-api-endpoint your-dify-api-key
```

## 使用方法

### 与Claude Desktop一起使用

在您的`claude_desktop_config.json`中添加以下配置：

```json
{
  "mcpServers": {
    "dify": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-dify",
        "https://your-dify-api-endpoint",
        "your-dify-api-key"
      ]
    }
  }
}
```

将`your-dify-api-endpoint`和`your-dify-api-key`替换为您实际的Dify API凭据。

### 工具

#### meshi-doko

一个与Dify AI接口的餐厅推荐工具：

参数：
- `LOCATION` (字符串)：餐厅位置
- `BUDGET` (字符串)：预算限制
- `query` (字符串)：发送给Dify AI的查询
- `conversation_id` (字符串, 可选)：用于维护聊天上下文

## 开发

```bash
# Initial setup
make setup

# Build the project
make build

# Format code
make format

# Run linter
make lint
```

## 许可证

本项目根据[MIT许可证](https://github.com/yuru-sha/mcp-server-dify/blob/HEAD/LICENSE)发布。

## 安全

该服务器使用您提供的API密钥与Dify AI互动。请确保：
- 保持您的API凭证安全
- 对API端点使用HTTPS
- 永远不要将API密钥提交到版本控制系统

## 贡献

欢迎贡献！请随时提交Pull Request。

**官方网站：** [https://github.com/yuru-sha/mcp-server-dify](https://github.com/yuru-sha/mcp-server-dify)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`
- 标签：`search`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @modelcontextprotocol/server-dify https://your-dify-api-endpoint your-dify-api-key`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/yuru-sha-dify.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
