---
title: "MCP消息网关"
description: "启用通过 MCP 协议向网络钩子端点发送消息的功能，支持自定义内容、显示名称和头像 URL。"
---

# MCP消息网关

启用通过 MCP 协议向网络钩子端点发送消息的功能，支持自定义内容、显示名称和头像 URL。

# MCP Webhook Server

一个与webhooks集成的MCP服务器实现，提供消息发送功能。

## 特性

* **通用Webhook支持**：向任意webhook端点发送消息
* **自定义用户名**：为消息设置自定义显示名称
* **头像支持**：自定义消息头像
* **MCP集成**：与Dive及其他兼容MCP的LLM一起工作

## 安装

```bash
npm install @kevinwatt/mcp-webhook
```

## 与[Dive Desktop](https://github.com/OpenAgentPlatform/Dive)配置

1. 在Dive Desktop中点击“+ 添加MCP服务器”
2. 复制并粘贴此配置：

```json
{
  "mcpServers": {
    "webhook": {
      "command": "npx",
      "args": [
        "-y",
        "@kevinwatt/mcp-webhook"
      ],
      "env": {
        "WEBHOOK_URL": "your-webhook-url"
      },
      "alwaysAllow": [
        "send_message"
      ]
    }
  }
}
```

3. 点击“保存”以安装MCP服务器

## 工具文档

* **send_message**
  * 向webhook端点发送消息
  * 输入参数：
    * `content` (字符串, 必填): 要发送的消息内容
    * `username` (字符串, 可选): 显示名称
    * `avatar_url` (字符串, 可选): 头像URL

## 使用示例

让您的LLM执行以下操作：
```
"Send a message to webhook: Hello World!"
"Send a message with custom name: content='Testing', username='Bot'"
```

## 手动启动

如果需要，可以手动启动服务器：

```bash
npx @kevinwatt/mcp-webhook
```

## 需求

* Node.js 18+
* 兼容MCP的LLM服务

## 许可证

MIT

## 作者

kevinwatt

## 关键词

* mcp
* webhook
* chat
* dive
* llm
* automation

**官方网站：** [https://github.com/kevinwatt/mcp-webhook](https://github.com/kevinwatt/mcp-webhook)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`communication`
- 标签：`communication`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @kevinwatt/mcp-webhook`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/kevinwatt-webhook.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
