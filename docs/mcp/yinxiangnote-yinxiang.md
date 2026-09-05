---
title: "mcp-server-yinxiang"
description: "YXBJ-MCP 印象笔记 MCP 服务器，支持通过 Model Context Protocol 保存笔记到印象笔记"
---

# mcp-server-yinxiang

YXBJ-MCP 印象笔记 MCP 服务器，支持通过 Model Context Protocol 保存笔记到印象笔记

# YXBJ-MCP

> 印象笔记 MCP 服务，支持将文本内容保存到您的印象笔记

## 简介

YXBJ-MCP 是一个 MCP (Model Context Protocol) 服务，可以让您在与 AI 工具（如 Cursor、Claude、Cherry Studio等）聊天交互时，直接将内容保存到印象笔记。

## 功能特性

- ✅ **连接测试** - 测试 MCP 连接状态
- ✅ **保存笔记** - 将内容保存到印象笔记
- ✅ **Markdown 支持** - 支持丰富的文本格式
- ✅ **环境变量配置** - 安全的认证方式

## 安装和使用

### 1. 获取授权Token
- 访问印象笔记OAuth授权页面：https://app.yinxiang.com/third/mcp-oauth/
- 登录印象笔记账号，并获取获取MCP服务授权Token

### 2. 使用 npx 安装

```bash
# 直接运行，无需安装
npx yxbj-mcp
```
### 3. 环境配置
在使用前，需要设置环境变量：
```bash
# 临时设置环境变量并运行
YINXIANG_AUTH_TOKEN="your_token" npx yxbj-mcp
```
> "your_token"替换为获取的授权Token

## 在 Cursor 中使用

1. 在 Cursor 的 MCP 配置中添加：
```json
{
  "mcpServers": {
    "yxbj-mcp": {
      "command": "npx",
      "args": ["yxbj-mcp"],
      "env": {
        "YINXIANG_AUTH_TOKEN": "your_token_here"
      }
    }
  }
}
```
> "your_token_here"替换为获取的授权Token
2. 重启 Cursor，即可在 AI 助手中使用印象笔记功能

## 可用工具

### test-connection
测试 MCP 连接状态，返回系统信息

### save-note
保存笔记到印象笔记
- `title`: 笔记标题
- `content`: 笔记内容（支持 Markdown）

## 开发

```bash
# 安装依赖
npm install

# 开发模式（TypeScript）
npm run build

# 测试
npm test
```

## 许可证

ISC

## 贡献

欢迎提交 Issue 和 Pull Request！

**Official site: ** [https://github.com/yinxiang-team/YXBJ-MCP](https://github.com/yinxiang-team/YXBJ-MCP)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `memory`
- Tags: `knowledge and memory`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `yxbj-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/yinxiangnote-yinxiang.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
