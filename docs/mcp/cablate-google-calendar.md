---
title: "MCP Google日历管理器"
description: "启用全面的日历管理功能，可以通过与Google日历集成的Model Context Protocol服务器创建、列出、更新和删除事件。"
---

# MCP Google日历管理器

启用全面的日历管理功能，可以通过与Google日历集成的Model Context Protocol服务器创建、列出、更新和删除事件。

# Calendar Tools MCP 服务器

一个强大的模型上下文协议（MCP）服务器，提供全面的日历管理功能。

## 功能

### 日历管理

- 创建日历事件
- 列出日历事件
- 更新现有事件
- 删除事件

## 在 Dive Desktop 上的演示

## 安装

### 手动安装

```bash
npm install -g @cablate/mcp-google-calendar
```

## 使用方法

### 命令行界面 (CLI)

```bash
mcp-google-calendar
```

### 使用 [Dive Desktop](https://github.com/OpenAgentPlatform/Dive)

1. 在 Dive Desktop 中点击 "+ 添加 MCP 服务器"
2. 复制并粘贴以下配置：

```json
{
  "mcpServers": {
    "calendar": {
      "command": "npx",
      "args": ["-y", "@cablate/mcp-google-calendar"],
      "env": {
        "GOOGLE_CALENDAR_ID": "your_calendar_id",
        "GOOGLE_TIME_ZONE": "your_time_zone",
        "GOOGLE_CREDENTIALS_PATH": "your_credentials_path"
      },
      "enabled": true
    }
  }
}
```

3. 点击“保存”以安装 MCP 服务器

## Google 服务账号和凭证

以下是创建 Google 服务账号和凭证的简单步骤：

1. 前往 [Google Cloud 控制台](https://console.cloud.google.com/)
2. 创建新项目或选择现有项目
3. 导航到 "IAM & Admin" 部分
4. 点击 "Service Accounts"
5. 点击 "Create Service Account"
6. 为服务账号输入名称（例如，“MCP Google Calendar”）
7. 点击 "Create"
8. 点击 "Create Key"
9. 选择 "JSON" 作为密钥类型
10. 点击 "Create"
11. 下载 JSON 文件并将其保存为 `credentials.json`

如果还有任何问题，请自行搜索答案。

## 许可证

MIT

## 贡献

欢迎社区参与和贡献！以下是贡献方式：

- ⭐️ 如果您觉得该项目有帮助，请给它点个星
- 🐛 提交问题：报告问题或提供建议
- 🔧 创建 Pull Requests：提交代码改进

## 联系

如果您有任何问题或建议，请随时联系我们：

- 📧 电子邮件: [reahtuoo310109@gmail.com](mailto:reahtuoo310109@gmail.com)
- 📧 GitHub: [CabLate](https://github.com/cablate/)
- 🤝 合作: 欢迎讨论项目合作事宜
- 📚 技术指导: 欢迎提出建议和指导

**官方网站：** [https://github.com/cablate/mcp-google-calendar](https://github.com/cablate/mcp-google-calendar)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`productivity`
- 标签：`calendar management`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @cablate/mcp-google-calendar`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/cablate-google-calendar.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
