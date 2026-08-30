---
title: "Resend邮件"
description: "一个简单的MCP服务器，允许用户通过Resend的API发送电子邮件，并与Cursor和Claude Desktop等工具集成，实现无缝的邮件撰写和发送。"
---

# Resend邮件

一个简单的MCP服务器，允许用户通过Resend的API发送电子邮件，并与Cursor和Claude Desktop等工具集成，实现无缝的邮件撰写和发送。

# 邮件发送 MCP 💌

[Smithery](https://smithery.ai/server/@ykhli/mcp-send-email)

这是一个使用 Resend 的 API 发送邮件的简单 MCP 服务器。为什么？现在你可以让 Cursor 或 Claude Desktop 为你撰写邮件，并立即发送，而无需复制粘贴邮件内容。

构建工具：

- [Resend](https://resend.com/)
- [Anthropic MCP](https://docs.anthropic.com/en/docs/agents-and-tools/mcp)
- [Cursor](https://cursor.so/)

## 功能

- 发送纯文本和 HTML 邮件
- 安排未来发送的邮件
- 添加抄送（CC）和密送（BCC）收件人
- 配置回复地址
- 可自定义发件人邮箱（需要验证）

**演示**

[https://github.com/user-attachments/assets/8c05cbf0-1664-4b3b-afb1-663b46af3464](https://github.com/user-attachments/assets/8c05cbf0-1664-4b3b-afb1-663b46af3464)

**Cursor**

1. 首先，你需要授权 Resend 从你的域名或邮箱发送邮件。按照[这里](https://resend.com/docs/send-with-nodejs)的步骤进行设置并获取一个 Resend API 密钥。
2. 在本地克隆此项目。编辑 `index.ts` 文件并将 `me@yoko.dev` 替换为你要用来发送邮件的电子邮件地址。
3. 在项目目录下运行 `npm install` 和 `npm run build`。你应该会看到生成了一个 `/build/index.js` 文件 - 这就是 MCP 服务器脚本！

然后进入 Cursor 设置 -> MCP -> 添加新的 MCP 服务器

- 名称 = [选择你自己的名称]
- 类型 = 命令
- 命令: `node ABSOLUTE_PATH_TO_MCP_SERVER/build/index.js --key=YOUR_RESEND_API_KEY --sender=OPTIONAL_SENDER_EMAIL_ADDRESS --reply-to=OPTIONAL_REPLY_TO_EMAIL_ADDRESS_ONE --reply-to=OPTIONAL_REPLY_TO_EMAIL_ADDRESS_TWO`

你可以在这里获取 Resend API 密钥: [https://resend.com/](https://resend.com/)

现在你可以通过转到 `email.md`，替换 `to:` 邮件地址，选中邮件 md 中的所有内容，并按下 cmd+l 来测试发送邮件。确保 Cursor 聊天处于代理模式，方法是在左下角下拉菜单中选择“Agent”。

**Claude 桌面版**

与上述相同的设置，然后添加以下 MCP 配置

```
{
  "mcpServers": {
    "resend": {
      "command": "node",
      "args": ["ABSOLUTE_PATH_TO_MCP_SERVER/build/index.js"],
      "env": {
        "RESEND_API_KEY": [YOUR_API_KEY],
        "SENDER_EMAIL_ADDRESS": [OPTIONAL_SENDER_EMAIL_ADDRESS],
        "REPLY_TO_EMAIL_ADDRESSES": [OPTIONAL_REPLY_TO_EMAIL_ADDRESSES_COMMA_DELIMITED]
      }
    }
  }
}
```

**开发**

`npm install`
`npm run build`

**官方网站：** [https://github.com/ykhli/mcp-send-email](https://github.com/ykhli/mcp-send-email)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`communication`
- 标签：`communication`, `developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node ABSOLUTE_PATH_TO_MCP_SEND_EMAIL_PROJECT/build/index.js --key=YOUR_RESEND_API_KEY`
- 参数：无

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/resend-send-email.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
