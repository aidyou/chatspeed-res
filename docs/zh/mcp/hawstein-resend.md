---
title: "Resend邮件工具"
description: "一种工具集成，使 Claude 能够通过 Resend API 撰写和发送电子邮件，支持定时发送和文件附件等功能。"
---

# Resend邮件工具

一种工具集成，使 Claude 能够通过 Resend API 撰写和发送电子邮件，支持定时发送和文件附件等功能。

# MCP Server Resend

用于 Resend API 的 MCP 服务器。让大语言模型为您撰写和发送电子邮件。

## 环境变量

- `RESEND_API_KEY` (字符串，必填)：您的 Resend API 密钥
- `SENDER_EMAIL_ADDRESS` (字符串，必填)：发件人电子邮件地址
- `REPLY_TO_EMAIL_ADDRESSES` (字符串，可选)：逗号分隔的回复至电子邮件地址列表

## 可用工具

- `send_email` - 使用 Resend API 发送电子邮件
  - 输入：
    - `to` (字符串)：收件人电子邮件地址
    - `subject` (字符串)：邮件主题行
    - `content` (字符串)：纯文本邮件内容
    - `from` (字符串，可选)：发件人电子邮件地址（如果未提供则使用 SENDER_EMAIL_ADDRESS）
    - `replyTo` (数组，可选)：回复至电子邮件地址（如果未提供则使用 REPLY_TO_EMAIL_ADDRESSES）
    - `scheduledAt` (字符串，可选)：预定邮件发送时间
    - `attachments` (数组，可选)：附件列表，每个附件必须包含：
      - `filename` (字符串)：附件文件名
      - `localPath` (字符串)：用户计算机上的本地文件绝对路径（如果未提供 remoteUrl 则为必填项）
      - `remoteUrl` (字符串)：互联网上的文件 URL（如果未提供 localPath 则为必填项）

## 获取 API 密钥

1. 注册 [Resend 账户](https://resend.com/)
2. 从 [Resend 控制台](https://resend.com/api-keys) 生成您的 API 密钥

**注意：免费层级每月可用 3000 封邮件。**

## 安装

### 使用 [ClaudeMind](https://claudemind.com/) (推荐)

使用 Resend MCP 服务器最简单的方法是通过 ClaudeMind 桌面应用程序。只需下载并安装 ClaudeMind，然后：

1. 打开 ClaudeMind 应用程序
2. 导航到 Servers 页面
3. 找到 resend-mcp 并点击 Install

就这样！无需任何技术知识 - ClaudeMind 无缝地为您处理所有安装和配置。

### 使用 Claude Desktop

将以下内容添加到您的 `claude_desktop_config.json` 文件中：

```json
{
  "mcpServers": {
    "resend-mcp": {
      "command": "npx",
      "args": [
        "-y",
        "resend-mcp"
      ],
      "env": {
        "RESEND_API_KEY": "YOUR_RESEND_API_KEY_HERE (string, required)",
        "SENDER_EMAIL_ADDRESS": "YOUR_SENDER_EMAIL_ADDRESS_HERE (string, required)",
        "REPLY_TO_EMAIL_ADDRESSES": "YOUR_REPLY_TO_EMAIL_ADDRESSES_HERE (string, optional, comma delimited)"
      }
    }
  }
}
```

## 许可证

此 MCP 服务器根据 MIT 许可证授权。这意味着您可以在遵守 MIT 许可证条款和条件的前提下自由使用、修改和分发该软件。更多详情，请参见项目仓库中的 LICENSE 文件。

**官方网站：** [https://github.com/hawstein/resend-mcp](https://github.com/hawstein/resend-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`communication`
- 标签：`communication`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y resend-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/hawstein-resend.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
