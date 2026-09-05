---
title: "dify-mcp-server"
description: "Integrates Dify AI API to provide code generation for Ant Design components, supporting both text and image inputs with stream processing capabilities."
---

# dify-mcp-server

Integrates Dify AI API to provide code generation for Ant Design components, supporting both text and image inputs with stream processing capabilities.

# dify-server MCP 服务器

一个集成 Dify AI API 的 Model Context Protocol 服务器

这是一个基于 TypeScript 的 MCP 服务器，通过集成 Dify AI API 来提供 Ant Design 业务组件的代码生成能力。它展示了以下核心 MCP 概念：

- 集成 Dify AI API 实现聊天完成功能
- 支持文本和图片输入
- 流式响应处理

## 功能特性

### Tools

- `antd-component-codegen-mcp-tool` - 生成 Ant Design 业务组件代码
  - 支持文本和可选的图片输入
  - 处理图片文件上传
  - 支持来自 Dify AI API 的流式响应

## 开发指南

安装依赖：

```bash
npm install
```

开发模式（自动重新构建）：

```bash
npm run watch
```

构建服务器：

```bash
npm run build
```

## 安装说明

### 在 Continue 中集成

在`~/.continue/config.json`中添加以下配置：

```json
{
  "experimental": {
    "modelContextProtocolServers": [
      {
        "transport": {
          "type": "stdio",
          "command": "node",
          "args": ["your/path/dify-server/build/index.js"],
          "env": {
            "DIFY_API_KEY": "***"
          }
        }
      }
    ]
  }
}
```

### 在 Cline 中集成

在`your/path/cline_mcp_settings.json`中添加以下配置：

```json
{
  "mcpServers": {
    "dify-server": {
      "command": "node",
      "args": ["your/path/dify-server/build/index.js"],
      "env": {
        "DIFY_API_KEY": "***"
      }
    }
  }
}
```

### 调试

由于 MCP 服务器通过标准输入输出（stdio）进行通信，调试可能会比较困难。我们推荐使用 [MCP Inspector](https://github.com/modelcontextprotocol/inspector)，可通过以下命令启动：

```bash
npm run inspector
```

Inspector 将提供一个可在浏览器中访问的调试工具 URL。

**Official site: ** [https://github.com/AI-FE/dify-mcp-server](https://github.com/AI-FE/dify-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`, `media`
- Tags: `developer tools`, `image and video processing`, `other`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `node`
- Args: `your/path/dify-server/build/index.js`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/ai-fe-dify.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
