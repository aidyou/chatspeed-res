---
title: "folderr助手服务"
description: "一个模型上下文协议（MCP）服务器，提供与Folderr API交互的工具，专门用于管理和与Folderr助手进行通信。"
---

# folderr助手服务

一个模型上下文协议（MCP）服务器，提供与Folderr API交互的工具，专门用于管理和与Folderr助手进行通信。

# Folderr MCP 服务器

一个模型上下文协议 (MCP) 服务器，提供了与 Folderr 的 API 进行交互的工具，特别是用于管理和与 Folderr 助手进行通信。

## 安装

将以下内容添加到您的 MCP 设置中

```
{
  "mcpServers": {
    "folderr": {
      "command": "npx",
      "args": ["-y", "@folderr/folderr-mcp-server"]
    }
  }
}
```

## 功能

该服务器提供以下工具：

### 身份验证

支持两种身份验证方法：

1. **使用邮箱/密码登录**
```typescript
   {
     "name": "login",
     "arguments": {
       "email": "user@example.com",
       "password": "your-password"
     }
   }
```

2. **API 令牌身份验证**
```typescript
   {
     "name": "set_api_token",
     "arguments": {
       "token": "your-api-token"
     }
   }
```
   可以从 Folderr 开发者部分生成 API 令牌。此方法推荐用于自动化或长时间运行的过程。

### 助手管理

1. **列出助手**
```typescript
   {
     "name": "list_assistants",
     "arguments": {}
   }
```
   返回经过身份验证用户的所有可用助手列表。

2. **询问助手**
```typescript
   {
     "name": "ask_assistant",
     "arguments": {
       "assistant_id": "assistant-id",
       "question": "您的问题"
     }
   }
```
   向特定助手发送问题并接收其响应。

## 配置

服务器将其配置存储在 `config.json` 文件中，包括：
- Folderr API 的基础 URL
- 身份验证令牌（来自登录或 API 密钥）

## 错误处理

服务器为常见场景提供详细的错误消息：
- 身份验证失败
- 无效请求
- API 错误
- 网络问题

## 开发

要构建服务器，请执行：
```bash
npm install
npm run build
```

## 在 MCP 设置中的使用

将以下内容添加到您的 MCP 设置配置中：
```json
{
  "mcpServers": {
    "folderr": {
      "command": "node",
      "args": ["/path/to/folderr-server/build/index.js"]
    }
  }
}
```

## 身份验证流程

1. 任选一种：
   - 使用带有邮箱和密码的 `login` 工具
   - 使用从 Folderr 开发者部分获取的 API 令牌的 `set_api_token` 工具
2. 身份验证令牌会自动保存，并用于后续请求
3. 所有助手相关的工具都需要在使用前进行身份验证

## 错误消息

常见的错误消息及其含义：
- "未登录"：未设置身份验证令牌
- "登录失败"：凭证无效
- "无法列出助手"：检索助手列表时出错
- "无法向助手提问"：向助手发送问题时出错

**官方网站：** [https://github.com/folderr-tech/folderr-mcp-server](https://github.com/folderr-tech/folderr-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`communication`
- 标签：`communication`, `developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @folderr/folderr-mcp-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/folderr-tech-folderr.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
