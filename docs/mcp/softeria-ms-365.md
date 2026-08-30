---
title: "微软365 MCP 服务器"
description: "一种模型上下文协议服务器，通过 Graph API 实现与 Microsoft 365 服务（Excel、日历、邮件、OneDrive、Teams 等）的交互，使人工智能助手能够通过自然语言管理 Microsoft 365 资源。"
---

# 微软365 MCP 服务器

一种模型上下文协议服务器，通过 Graph API 实现与 Microsoft 365 服务（Excel、日历、邮件、OneDrive、Teams 等）的交互，使人工智能助手能够通过自然语言管理 Microsoft 365 资源。

# ms-365-mcp-server

![npm version](/mcp-assets/a31704b4715177030b77326640272691.svg) ![build status](/mcp-assets/a360cf14c31b446d557b2bc79fbedc72.svg) ![license](/mcp-assets/d177f30277cff66d9af1e3c6409e24dc.svg)

Microsoft 365 MCP Server

A Model Context Protocol (MCP) server for interacting with Microsoft 365 services through the Graph API.

## Prerequisites

- Node.js >= 14

## Features

- Authentication via Microsoft Authentication Library (MSAL)
- Excel file operations
- Calendar event management
- Mail operations
- OneDrive file management
- OneNote notebooks and pages
- To Do tasks and task lists
- Planner plans and tasks
- Outlook contacts
- User management
- Dynamic tools powered by Microsoft Graph OpenAPI spec
- Built on the Model Context Protocol

## Quick Start Example

Test login in Claude Desktop:

## Examples

## Integration

### Claude Desktop

To add this MCP server to Claude Desktop:

Edit the config file under Settings > Developer:

```json
{
  "mcpServers": {
    "ms365": {
      "command": "npx",
      "args": [
        "-y",
        "@softeria/ms-365-mcp-server"
      ]
    }
  }
}
```

### Claude Code CLI

```bash
claude mcp add ms365 -- npx -y @softeria/ms-365-mcp-server
```

For other interfaces that support MCPs, please refer to their respective documentation for the correct
integration method.

### Authentication

> ⚠️ You must authenticate before using tools.

1. **MCP client login**:
    - Call the `login` tool (auto-checks existing token)
    - If needed, get URL+code, visit in browser
    - Use `verify-login` tool to confirm
2. **Optional CLI login**:
```bash
   npx @softeria/ms-365-mcp-server --login
```
   Follow the URL and code prompt in the terminal.

Tokens are cached securely in your OS credential store (fallback to file).

## License

MIT © 2025 Softeria

**官方网站：** [https://github.com/softeria/ms-365-mcp-server](https://github.com/softeria/ms-365-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`productivity`
- 标签：`app automation`, `cloud platforms`, `calendar management`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @softeria/ms-365-mcp-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/softeria-ms-365.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
