---
title: "Google 工作区邮件日历服务器"
description: "提供了与Gmail和日历API交互的工具。通过MCP界面，此服务器使您能够以编程方式管理电子邮件和日历事件。"
---

# Google 工作区邮件日历服务器

提供了与Gmail和日历API交互的工具。通过MCP界面，此服务器使您能够以编程方式管理电子邮件和日历事件。

# Google Workspace MCP 服务器

这是一个提供与 Gmail 和日历 API 交互工具的模型上下文协议 (MCP) 服务器。通过 MCP 接口，该服务器使您能够以编程方式管理您的电子邮件和日历事件。

## 功能

### Gmail 工具
- `list_emails`: 列出收件箱中的最近邮件，并可选择性过滤
- `search_emails`: 使用 Gmail 查询语法进行高级邮件搜索
- `send_email`: 发送新邮件，支持抄送 (CC) 和密送 (BCC)
- `modify_email`: 修改邮件标签（归档、移至垃圾箱、标记为已读/未读）

### 日历工具
- `list_events`: 列出即将到来的日历事件，并可按日期范围过滤
- `create_event`: 创建带有参与者的新的日历事件
- `update_event`: 更新现有的日历事件
- `delete_event`: 删除日历事件

## 前提条件

1. **Node.js**: 安装 Node.js 版本 14 或更高版本
2. **Google Cloud 控制台设置**:
   - 访问 [Google Cloud 控制台](https://console.cloud.google.com/)
   - 创建一个新项目或选择一个现有项目
   - 启用 Gmail API 和 Google 日历 API：
     1. 转到“API和服务” > “库”
     2. 搜索并启用“Gmail API”
     3. 搜索并启用“Google 日历 API”
   - 设置 OAuth 2.0 凭据：
     1. 转到“API和服务” > “凭据”
     2. 点击“创建凭据” > “OAuth 客户端 ID”
     3. 选择“Web 应用程序”
     4. 将“授权重定向 URI”设置为包括：`http://localhost:4100/code`
     5. 记下客户端 ID 和客户端密钥

## 设置说明

（此处原文没有更多内容，请根据实际文档继续添加具体的设置步骤）

1. **克隆并安装**:
```bash
   git clone https://github.com/epaproditus/google-workspace-mcp-server.git
   cd google-workspace-mcp-server
   npm install
```

2. **创建 OAuth 凭证**:
   在根目录下创建一个 `credentials.json` 文件：
```json
   {
       "web": {
           "client_id": "您的客户端ID",
           "client_secret": "您的客户端密钥",
           "redirect_uris": ["http://localhost:4100/code"],
           "auth_uri": "https://accounts.google.com/o/oauth2/auth",
           "token_uri": "https://oauth2.googleapis.com/token"
       }
   }
```

3. **获取刷新令牌**:
```bash
   node get-refresh-token.js
```
   这将：
   - 打开浏览器进行 Google OAuth 认证
   - 请求以下权限：
     - `https://www.googleapis.com/auth/gmail.modify`
     - `https://www.googleapis.com/auth/calendar`
     - `https://www.googleapis.com/auth/gmail.send`
   - 将凭证保存到 `token.json`
   - 在控制台中显示刷新令牌

4. **配置 MCP 设置**:
   在您的 MCP 设置文件中添加服务器配置：
   - 对于 VSCode Claude 扩展：`~/Library/Application Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`
   - 对于 Claude 桌面应用：`~/Library/Application Support/Claude/claude_desktop_config.json`

   在 `mcpServers` 对象中添加以下内容：
```json
   {
     "mcpServers": {
       "google-workspace": {
         "command": "node",
         "args": ["/path/to/google-workspace-server/build/index.js"],
         "env": {
           "GOOGLE_CLIENT_ID": "您的客户端ID",
           "GOOGLE_CLIENT_SECRET": "您的客户端密钥",
           "GOOGLE_REFRESH_TOKEN": "您的刷新令牌"
         }
       }
     }
   }
```

5. **构建并运行**:
```bash
   npm run build
```

## 使用示例

### Gmail 操作

1. **列出最近的邮件**:
```json
   {
     "maxResults": 5,
     "query": "is:unread"
   }
```

2. **搜索邮件**:
```json
   {
     "query": "from:example@gmail.com has:attachment",
     "maxResults": 10
   }
```

3. **发送邮件**:
```json
   {
     "to": "recipient@example.com",
     "subject": "Hello",
     "body": "邮件内容",
     "cc": "cc@example.com",
     "bcc": "bcc@example.com"
   }
```

4. **修改邮件**:
```json
   {
     "id": "邮件ID",
     "addLabels": ["UNREAD"],
     "removeLabels": ["INBOX"]
   }
```

### 日历操作

（原文档在此处结束，没有提供日历操作的具体示例。）

1. **列出事件**:
```json
   {
     "maxResults": 10,
     "timeMin": "2024-01-01T00:00:00Z",
     "timeMax": "2024-12-31T23:59:59Z"
   }
```

2. **创建事件**:
```json
   {
     "summary": "团队会议",
     "location": "会议室",
     "description": "每周同步",
     "start": "2024-01-24T10:00:00Z",
     "end": "2024-01-24T11:00:00Z",
     "attendees": ["colleague@example.com"]
   }
```

3. **更新事件**:
```json
   {
     "eventId": "event_id",
     "summary": "更新后的会议标题",
     "location": "虚拟",
     "start": "2024-01-24T11:00:00Z",
     "end": "2024-01-24T12:00:00Z"
   }
```

4. **删除事件**:
```json
   {
     "eventId": "event_id"
   }
```

## 故障排除

1. **认证问题**:
   - 确保授予了所有必需的OAuth范围
   - 验证客户端ID和密钥是否正确
   - 检查刷新令牌是否有效

2. **API错误**:
   - 在Google Cloud控制台中检查API配额和限制
   - 确保为您的项目启用了API
   - 验证请求参数与所需格式匹配

## 许可证

本项目根据MIT许可证发布。

**官方网站：** [https://github.com/epaproditus/google-workspace-mcp-server](https://github.com/epaproditus/google-workspace-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`productivity`
- 标签：`communication`, `calendar management`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`/path/to/google-workspace-server/build/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/epaproditus-google-workspace.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
