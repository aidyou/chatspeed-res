---
title: "Figma"
description: "此项目提供了一个模型上下文协议（MCP）服务器，允许像Cursor这样的AI编码工具访问和使用Figma设计数据。它简化了Figma API的响应，仅提供最相关的布局和样式信息，从而提高了AI生成代码的准确性。"
---

# Figma

此项目提供了一个模型上下文协议（MCP）服务器，允许像Cursor这样的AI编码工具访问和使用Figma设计数据。它简化了Figma API的响应，仅提供最相关的布局和样式信息，从而提高了AI生成代码的准确性。

Figma 的 Framelink MCP

  
让您的编码代理访问 Figma 数据。
一次性在任何框架中实现设计。

  

    

  

  

    

  

  

    

  

  

  

    

  

通过这个 [Model Context Protocol](https://modelcontextprotocol.io/introduction) 服务器，让 [Cursor](https://cursor.sh/) 和其他基于 AI 的编码工具能够访问您的 Figma 文件。

当 Cursor 能够访问 Figma 设计数据时，它在一次性准确实现设计方面比粘贴截图等替代方法要好得多。

查看快速入门指南 →

## 演示

[观看使用 Figma 设计数据在 Cursor 中构建 UI 的演示](https://youtu.be/6G9yb-LrEqg)

[Watch video](https://youtu.be/6G9yb-LrEqg)

## 工作原理

1. 打开 IDE 的聊天（例如 Cursor 中的代理模式）。
2. 粘贴一个 Figma 文件、帧或组的链接。
3. 要求 Cursor 对 Figma 文件执行某些操作——例如实现设计。
4. Cursor 将从 Figma 获取相关元数据，并使用这些数据编写代码。

此 MCP 服务器是专门为与 Cursor 一起使用而设计的。在从 [Figma API](https://www.figma.com/developers/api) 响应提供上下文之前，它会简化并翻译响应，以便仅向模型提供最相关的布局和样式信息。

减少提供给模型的上下文数量有助于提高 AI 的准确性，并使响应更加相关。

## 开始使用

许多代码编辑器和其他 AI 客户端使用配置文件来管理 MCP 服务器。

可以通过将以下内容添加到配置文件中来配置 `figma-developer-mcp` 服务器。

> 注意：您需要创建一个 Figma 访问令牌才能使用此服务器。有关如何创建 Figma API 访问令牌的说明，请参阅 [这里](https://help.figma.com/hc/en-us/articles/8085703771159-Manage-personal-access-tokens)。

### MacOS / Linux

```json

{

  "mcpServers": {

    "Framelink MCP for Figma": {

      "command": "npx",

      "args": ["-y", "figma-developer-mcp", "--figma-api-key=YOUR-KEY", "--stdio"]

    }

  }

}

```
### Windows

```json

{

  "mcpServers": {

    "Framelink MCP for Figma": {

      "command": "cmd",

      "args": ["/c", "npx", "-y", "figma-developer-mcp", "--figma-api-key=YOUR-KEY", "--stdio"]

    }

  }

}

```
或者您可以在 `env` 字段中设置 `FIGMA_API_KEY` 和 `PORT`。

如果您需要更多关于如何配置 Figma 的 Framelink MCP 的信息，请参阅 [Framelink 文档](https://www.framelink.ai/docs/quickstart)。

## 星标历史

## 了解更多

Figma 的 Framelink MCP 简单但功能强大。通过访问 [Framelink](https://framelink.ai) 网站了解更多内容，以充分利用它。

**官方网站：** [https://github.com/GLips/Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y figma-developer-mcp --figma-api-key=YOUR_KEY --stdio`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/glips-figma-context.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
