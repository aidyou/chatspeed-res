---
title: "邮件服务"
description: "一个基于 TypeScript 的 MCP 服务器，实现了电子邮件发送系统，允许 Claude 通过 blastengine 服务发送电子邮件。"
---

# 邮件服务

一个基于 TypeScript 的 MCP 服务器，实现了电子邮件发送系统，允许 Claude 通过 blastengine 服务发送电子邮件。

# blastengine-mailer MCP 服务器

这是一个基于模型上下文协议的服务器。

这是一款基于 TypeScript 的 MCP 服务器，实现了发送电子邮件的系统。

## 特性

### 工具
- `send_email` - 发送邮件

## 开发

安装依赖项：
```bash
npm install
```

构建服务器：
```bash
npm run build
```

开发时自动重建：
```bash
npm run watch
```

## 安装

要与 Claude Desktop 一起使用，请添加服务器配置：

在 MacOS 上: `~/Library/Application Support/Claude/claude_desktop_config.json`
在 Windows 上: `%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "blastengine-mailer": {
      "command": "node",
      "env": {
        "BLASTENGINE_USER_ID": "userid-of-blastengine",
        "BLASTENGINE_API_KEY": "apikey-of-blastengine"
      },
      "args": [
        "/path/to/blastengine-mailer/server.js"
      ]
    }
  }
}
```

### 调试

由于 MCP 服务器通过标准输入输出进行通信，调试可能会比较困难。我们推荐使用 [MCP Inspector](https://github.com/modelcontextprotocol/inspector)，它作为一个包脚本可用：

```bash
npm run inspector
```

Inspector 将提供一个 URL，以便您可以在浏览器中访问调试工具。

**官方网站：** [https://github.com/r3-yamauchi/mcp-server-blastengine-mailer](https://github.com/r3-yamauchi/mcp-server-blastengine-mailer)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`communication`
- 标签：`communication`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`/path/to/blastengine-mailer/server.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/r3-yamauchi-blastengine-mailer.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
