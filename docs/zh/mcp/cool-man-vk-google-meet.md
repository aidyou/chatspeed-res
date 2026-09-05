---
title: "Google Meet MCP 服务器"
description: "Google Meet MCP服务器允许AI代理创建、管理和检索Google Meet会议。它基于模型上下文协议构建，提供了用于安排、更新和删除会议的工具，使得集成Google Meet功能变得轻松容易。"
---

# Google Meet MCP 服务器

Google Meet MCP服务器允许AI代理创建、管理和检索Google Meet会议。它基于模型上下文协议构建，提供了用于安排、更新和删除会议的工具，使得集成Google Meet功能变得轻松容易。

# Google Meet MCP 服务器

[Smithery](https://smithery.ai/server/@cool-man-vk/google-meet-mcp-server)

这是一个通过 Google 日历 API 与 Google Meet 进行交互的 Model Context Protocol (MCP) 服务器。该服务器提供了用于以编程方式创建和管理 Google Meet 会议的工具。

## 描述

此项目实现了一个 MCP 服务器，允许 AI 代理通过 Google 日历 API 创建、检索和管理会议来与 Google Meet 进行交互。它利用了 MCP（Model Context Protocol）规范将这些功能作为工具暴露出来，可以被兼容的 AI 系统使用。

## 安装

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@cool-man-vk/google-meet-mcp-server) 自动为 Claude 桌面版安装 Google Meet MCP 服务器：

```bash
npx -y @smithery/cli install @cool-man-vk/google-meet-mcp-server --client claude
```

### 手动安装
```bash
# Clone the repository
git clone https://github.com/yourusername/google-meet-mcp.git

# Navigate to the project directory
cd google-meet-mcp

# Install dependencies
npm install
```

## 设置

在使用 Google Meet MCP 服务器之前，您需要设置您的 Google API 凭证：

1. 访问 [Google Cloud 控制台](https://console.cloud.google.com/)
2. 创建一个新项目或选择现有项目
3. 启用 Google 日历 API
4. 创建 OAuth 2.0 凭证（桌面应用程序）
5. 下载凭证 JSON 文件并将其保存为 `credentials.json` 在项目根目录中
6. 运行设置脚本进行身份验证并生成令牌：

```bash
npm run setup
```

这将打开一个浏览器窗口，您可以在其中授权应用程序访问您的 Google 日历。

## 使用

设置完成后，您可以启动 MCP 服务器：

```bash
npm run start
```

服务器将运行并提供以下工具：

- `create-meeting`: 创建一个新的 Google Meet 会议
- `list-meetings`: 列出即将到来的 Google Meet 会议
- `get-meeting-details`: 获取特定会议的详细信息
- `update-meeting`: 更新现有的会议
- `delete-meeting`: 删除会议

## MCP 配置

要与支持 MCP 的系统一起使用此服务器，请将以下内容添加到您的 MCP 设置配置文件中：

```json
{
  "mcpServers": {
    "google-meet": {
      "command": "node",
      "args": ["path/to/google-meet-mcp/src/index.js"],
      "env": {},
      "disabled": false
    }
  }
}
```

## 功能

- 用自定义设置创建 Google Meet 会议
- 检索包括加入链接在内的会议详情
- 更新现有会议
- 删除会议
- 列出即将召开的会议

**官方网站：** [https://github.com/cool-man-vk/google-meet-mcp-server](https://github.com/cool-man-vk/google-meet-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`productivity`
- 标签：`calendar management`, `communication`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`path/to/google-meet-mcp/src/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/cool-man-vk-google-meet.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
