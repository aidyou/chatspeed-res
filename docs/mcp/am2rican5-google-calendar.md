---
title: "MCP日历助手"
description: "通过模型上下文协议将 Google 日历与人工智能助手集成，使用户能够通过自然语言交互查看和管理日历事件。"
---

# MCP日历助手

通过模型上下文协议将 Google 日历与人工智能助手集成，使用户能够通过自然语言交互查看和管理日历事件。

# Google Calendar MCP 服务器

一个与 Google 日历集成的模型上下文协议 (MCP) 服务器，使用 TypeScript 构建。

## 功能

- 无缝集成 Google 日历并使用 OAuth 2.0 身份验证
- 持久化令牌存储以实现自动身份验证
- 列出和管理日历，并提供全面的事件操作
- 创建、读取、更新和删除日历事件
- 获取指定日期范围内的日历事件
- 支持 Server-Sent Events (SSE) 传输选项以实现实时更新
- 简单集成 Claude 和其他兼容 MCP 的 AI 助手

## 安装

```bash
npm install -g mcp-google-calendar
```

或者直接运行：

```bash
npx -y mcp-google-calendar
```

## 先决条件

1. Node.js（v16 或更高版本）
2. Google Cloud Platform 账户
3. 启用 Google 日历 API
4. OAuth 2.0 凭证

## 设置

### 1. Google Cloud 配置

1. 前往 [Google Cloud 控制台](https://console.cloud.google.com/)
2. 创建一个新项目或选择现有项目
3. 启用 Google 日历 API：
   - 导航到 "APIs & Services" > "Library"
   - 搜索 "Google Calendar API"
   - 单击 "启用"
4. 配置 OAuth 同意屏幕：
   - 前往 "APIs & Services" > "OAuth consent screen"
   - 选择 "外部" 用户类型（或 "内部" 对于 Google Workspace）
   - 填写必填信息：
     - 应用名称: mcp-calendar
     - 用户支持邮箱: (你的邮箱)
     - 开发者联系信息: (你的邮箱)
   - 添加权限范围：
     - 单击 "添加或移除权限范围"
     - 查找并选择 "https://www.googleapis.com/auth/calendar.events"
     - 将你的邮箱添加为测试用户
   - 完成设置
5. 创建 OAuth 凭证：
   - 前往 "Credentials"
   - 单击 "创建凭证" > "OAuth Client ID"
   - 选择 "桌面应用" 作为应用程序类型
   - 命名它（例如 "MCP Calendar Desktop Client"）
   - 下载 JSON 文件并保存为 `credentials.json` 在你的项目目录中

### 2. 环境配置

在你的项目根目录中创建一个 `.env` 文件：

```
# Server configuration
PORT=3420

# Google Calendar API configuration
CREDENTIALS_PATH=./credentials.json
```

## 使用

### 启动服务器

使用标准 WebSockets 启动：
```bash
npx -y mcp-google-calendar
```

使用 Server-Sent Events (SSE) 启动：
```bash
npx -y mcp-google-calendar --sse
```

### 与 Claude 桌面版一起使用

将以下内容添加到你的 `claude_desktop_config.json` 中：
```json
{
   "mcpServers": {
      "mcp-google-calendar": {
         "command": "npx",
         "args": ["-y", "mcp-google-calendar"],
         "env": {
            "CREDENTIALS_PATH": "/path/to/your/credentials.json"
         }
      }
   }
}
```

### 身份验证过程

首次运行服务器时：
1. 浏览器窗口将自动打开
2. 使用你的 Google 账户登录
3. 授权请求的日历权限
4. 认证令牌将保存到 `token.json`

后续启动时：
- 服务器会自动使用保存的令牌
- 除非令牌过期，否则无需浏览器交互

## 可用工具

| 工具 | 描述 |
|------|-------------|
| `list_calendars` | 获取所有可用日历 |
| `list_calendar_events` | 检索指定日期之间的事件 |
| `create_calendar_event` | 向你的日历添加新事件 |
| `get_calendar_event` | 获取特定事件的详细信息 |
| `edit_calendar_event` | 修改现有的日历事件 |
| `delete_calendar_event` | 从你的日历中删除事件 |

## 开发

克隆并设置项目：
```bash
git clone https://github.com/am2rican5/mcp-google-calendar.git
cd mcp-google-calendar
npm install
```

构建项目：
```bash
npm run build
```

以开发模式运行：
```bash
npm start
```

## 安全注意事项

⚠️ **重要安全警告** ⚠️

- `credentials.json` 和 `token.json` 包含敏感的认证信息
- 请勿将这些文件提交到版本控制系统或公开分享
- 每个用户应创建自己的 OAuth 凭据
- 如果您怀疑凭据被泄露，请立即在 Google Cloud Console 中撤销它们
- 令牌授予访问您的 Google 日历数据的权限

## 许可证

本项目采用 MIT 许可证 - 详情请参阅 [LICENSE](https://github.com/am2rican5/mcp-google-calendar/blob/HEAD/LICENSE) 文件。

## 贡献

欢迎贡献！请随时提交 Pull Request。

1. 叉分仓库
2. 创建您的功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交您的更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到该分支 (`git push origin feature/amazing-feature`)
5. 打开一个 Pull Request

**官方网站：** [https://github.com/am2rican5/mcp-google-calendar](https://github.com/am2rican5/mcp-google-calendar)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`productivity`
- 标签：`calendar management`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y mcp-google-calendar`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/am2rican5-google-calendar.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
