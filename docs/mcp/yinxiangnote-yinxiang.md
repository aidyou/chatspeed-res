---
title: "印象笔记MCP"
description: "YXBJ-MCP 是一个 MCP (Model Context Protocol) 服务器，可以让 AI 助手（如 Cursor）直接与印象笔记进行交互，实现笔记的创建和保存功能。它支持连接测试、保存笔记、Markdown 格式以及通过环境变量进行安全认证。"
---

# 印象笔记MCP

YXBJ-MCP 是一个 MCP (Model Context Protocol) 服务器，可以让 AI 助手（如 Cursor）直接与印象笔记进行交互，实现笔记的创建和保存功能。它支持连接测试、保存笔记、Markdown 格式以及通过环境变量进行安全认证。

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

**官方网站：** [https://github.com/yinxiang-team/YXBJ-MCP](https://github.com/yinxiang-team/YXBJ-MCP)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`memory`
- 标签：`knowledge and memory`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`yxbj-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/yinxiangnote-yinxiang.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
