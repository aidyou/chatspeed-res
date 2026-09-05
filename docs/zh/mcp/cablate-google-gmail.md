---
title: "Google Gmail 邮件助手"
description: "提供了与Gmail的全面集成，并具备LLM处理能力，允许用户通过模型上下文协议阅读、搜索、过滤电子邮件和处理附件。"
---

# Google Gmail 邮件助手

提供了与Gmail的全面集成，并具备LLM处理能力，允许用户通过模型上下文协议阅读、搜索、过滤电子邮件和处理附件。

# Gmail MCP 服务器

一个强大的模型上下文协议 (MCP) 服务器，提供全面的 Gmail 集成和 LLM 处理能力。

## 功能

### 邮件管理

- 读取和搜索邮件
- 以各种格式处理邮件内容
- 高级邮件过滤
- 附件处理

## 在 Dive Desktop 上的演示

## 安装

### 手动安装

```bash
npm install -g @cablate/mcp-gmail
```

## 使用

### 命令行界面 (CLI)

```bash
map-gmail
```

### 与 [Dive Desktop](https://github.com/OpenAgentPlatform/Dive) 一起使用

1. 在 Dive Desktop 中点击 "+ 添加 MCP 服务器"
2. 复制并粘贴此配置：

```json
{
  "mcpServers": {
    "gmail": {
      "command": "npx",
      "args": ["-y", "@cablate/mcp-gmail"],
      "env": {
        "GMAIL_CLIENT_ID": "your_client_id",
        "GMAIL_CLIENT_SECRET": "your_client_secret",
        "GMAIL_REFRESH_TOKEN": "your_refresh_token"
      },
      "enabled": true
    }
  }
}
```

3. 点击“保存”以安装 MCP 服务器

## Gmail API 认证设置

有关设置 Gmail API 认证和获取必要凭证的详细说明，请参阅我们的 [Gmail API 设置指南](https://github.com/cablate/mcp-google-gmail/blob/HEAD/guide.md)。

## 许可证

MIT

## 贡献

欢迎社区参与和贡献！以下是贡献的方式：

- ⭐️ 如果你觉得项目有用，请给项目加星标
- 🐛 提交问题：报告问题或提供建议
- 🔧 创建拉取请求：提交代码改进

## 联系

如果你有任何问题或建议，欢迎联系我们：

- 📧 电子邮件: [reahtuoo310109@gmail.com](mailto:reahtuoo310109@gmail.com)
- 📧 GitHub: [CabLate](https://github.com/cablate/)
- 🤝 合作：欢迎讨论项目合作
- 📚 技术指导：真诚欢迎提出建议和技术指导

**官方网站：** [https://github.com/cablate/mcp-google-gmail](https://github.com/cablate/mcp-google-gmail)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`communication`
- 标签：`communication`, `search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @cablate/mcp-gmail`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/cablate-google-gmail.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
