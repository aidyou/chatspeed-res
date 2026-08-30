---
title: "Google Workspace MCP Server 无删除日历版"
description: "语言类型：英语  \n翻译结果：  \n派生自 https://github.com/epaproditus/google-workspace-mcp-server  \n由于在保留创建能力的同时没有防止删除的范围，因此已移除 Google 日历中的删除和更新功能。"
---

# Google Workspace MCP Server 无删除日历版

语言类型：英语  
翻译结果：  
派生自 https://github.com/epaproditus/google-workspace-mcp-server  
由于在保留创建能力的同时没有防止删除的范围，因此已移除 Google 日历中的删除和更新功能。

[Smithery](https://smithery.ai/server/@erickva/google-workspace-mcp-server-no-calendar-deletetion)

# Google Workspace MCP 服务器

这是一个提供与 Gmail 和日历 API 交互工具的模型上下文协议（MCP）服务器。通过 MCP 接口，您可以编程方式管理您的电子邮件和日历事件。

## 功能

### Gmail 工具
- `list_emails`: 列出收件箱中的最近邮件，可选过滤条件
- `search_emails`: 使用 Gmail 查询语法进行高级邮件搜索
- `send_email`: 发送新邮件，支持抄送和密送
- `modify_email`: 修改邮件标签（存档、移到垃圾箱、标记为已读/未读）

### 日历工具
- `list_events`: 按日期范围筛选列出即将到来的日历事件
- `create_event`: 创建带有参与者的新的日历事件
- 由于 Google Cloud Calendar API 没有允许创建但禁止删除或更新的作用域，出于安全考虑，以下功能已从本服务器移除。
- `update_event`: 更新现有的日历事件
- `delete_event`: 删除日历事件

## 前提条件

1. **Node.js**: 安装 Node.js 版本 14 或更高版本
2. **Google Cloud 控制台设置**：
   - 访问 [Google Cloud 控制台](https://console.cloud.google.com/)
   - 创建一个新项目或选择现有项目
   - 启用 Gmail API 和 Google 日历 API：
     1. 转到 "API和服务" > "库"
     2. 搜索并启用 "Gmail API"
     3. 搜索并启用 "Google 日历 API"
   - 设置 OAuth 2.0 凭证：
     1. 转到 "API和服务" > "凭证"
     2. 点击 "创建凭证" > "OAuth 客户端 ID"
     3. 选择 "Web 应用程序"
     4. 将 "授权重定向 URI" 设置为包括: `http://localhost:4100/code`
     5. 记录客户端 ID 和客户端密钥

## 设置说明

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@erickva/google-workspace-mcp-server-no-calendar-deletetion) 自动为 Claude Desktop 安装不带日历删除功能的 Google Workspace 服务器：

```bash
npx -y @smithery/cli install @erickva/google-workspace-mcp-server-no-calendar-deletetion --client claude
```

### 手动安装

（此处根据实际需要补充手动安装的具体步骤）

1. **克隆并安装**:
```bash
   git clone https://github.com/epaproditus/google-workspace-mcp-server.git
   cd google-workspace-mcp-server
   npm install
```

2. **创建OAuth凭证**:
   在根目录下创建一个 `credentials.json` 文件:
```json
   {
       "web": {
           "client_id": "YOUR_CLIENT_ID",
           "client_secret": "YOUR_CLIENT_SECRET",
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
   这将:
   - 打开您的浏览器进行Google OAuth身份验证
   - 请求以下权限:
     - `https://www.googleapis.com/auth/gmail.modify`
     - `https://www.googleapis.com/auth/calendar`
     - `https://www.googleapis.com/auth/gmail.send`
   - 将凭证保存到 `token.json`
   - 在控制台中显示刷新令牌

4. **配置MCP设置**:
   将服务器配置添加到您的MCP设置文件中:
   - 对于VSCode Claude扩展: `~/Library/Application Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`
   - 对于Claude桌面应用程序: `~/Library/Application Support/Claude/claude_desktop_config.json`

   在 `mcpServers` 对象中添加以下内容:
```json
   {
     "mcpServers": {
       "google-workspace": {
         "command": "node",
         "args": ["/path/to/google-workspace-server/build/index.js"],
         "env": {
           "GOOGLE_CLIENT_ID": "your_client_id",
           "GOOGLE_CLIENT_SECRET": "your_client_secret",
           "GOOGLE_REFRESH_TOKEN": "your_refresh_token"
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

### Gmail操作

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
     "body": "Message content",
     "cc": "cc@example.com",
     "bcc": "bcc@example.com"
   }
```

4. **修改邮件**:
```json
   {
     "id": "message_id",
     "addLabels": ["UNREAD"],
     "removeLabels": ["INBOX"]
   }
```

### 日历操作

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
     "summary": "Team Meeting",
     "location": "Conference Room",
     "description": "Weekly sync-up",
     "start": "2024-01-24T10:00:00Z",
     "end": "2024-01-24T11:00:00Z",
     "attendees": ["colleague@example.com"]
   }
```

3. **更新事件**:
```json
   {
     "eventId": "event_id",
     "summary": "Updated Meeting Title",
     "location": "Virtual",
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

1. **认证问题**：
   - 确保所有必需的OAuth范围已授予
   - 验证客户端ID和密钥是否正确
   - 检查刷新令牌是否有效

2. **API错误**：
   - 在Google Cloud Console中检查API配额和限制
   - 确保您的项目已启用API
   - 验证请求参数是否符合所需格式

## 许可证

本项目根据MIT许可证发布。

**官方网站：** [https://github.com/erickva/google-workspace-mcp-server-no-calendar-deletetion](https://github.com/erickva/google-workspace-mcp-server-no-calendar-deletetion)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`productivity`
- 标签：`calendar management`, `communication`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`/path/to/google-workspace-server/build/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/erickva-google-workspace-no-calendar-deletetion.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
