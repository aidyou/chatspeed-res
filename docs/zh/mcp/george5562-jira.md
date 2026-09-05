---
title: "Jira MCP Server助手"
description: "通过模型上下文协议启用与 Jira 的自然语言交互，以便通过 Claude Desktop 管理项目、问题、任务和工作流，从而允许用户委托项目管理任务。"
---

# Jira MCP Server助手

通过模型上下文协议启用与 Jira 的自然语言交互，以便通过 Claude Desktop 管理项目、问题、任务和工作流，从而允许用户委托项目管理任务。

# Jira MCP 服务器

使用自然语言与 Jira 对话，以获取项目信息并进行修改。结合自定义的 README（其中包含项目信息）和 Claude Desktop 使用，这样您可以委托 PM 任务（例如，根据您的团队成员及其专长列表，将任何新问题分配给最相关的人）。

该服务器基于 [Model Context Protocol](https://github.com/modelcontextprotocol) 构建。

服务器支持以下功能：

- 项目创建和配置
- 问题和子任务管理
- 问题链接和依赖关系
- 自动化问题工作流

## 配置

必需的环境变量：

- `JIRA_HOST`：您的 Jira 实例主机名
- `JIRA_EMAIL`：您的 Jira 账户邮箱
- `JIRA_API_TOKEN`：来自 https://id.atlassian.com/manage-profile/security/api-tokens 的 API 令牌

## 可用工具

### 1. 用户管理

```typescript
// Get user's account ID by email
{
  email: "user@example.com";
}
```

### 2. 问题类型管理

```typescript
// List all available issue types
// Returns: id, name, description, subtask status
// No parameters required
```

### 3. 问题链接类型

```typescript
// List all available issue link types
// Returns: id, name, inward/outward descriptions
// No parameters required
```

### 4. 问题管理

#### 获取问题

```typescript
// Get all issues in a project
{
  projectKey: "PROJECT"
}

// Get issues with JQL filtering
{
  projectKey: "PROJECT",
  jql: "status = 'In Progress' AND assignee = currentUser()"
}

// Get issues assigned to user
{
  projectKey: "PROJECT",
  jql: "assignee = 'user@example.com' ORDER BY created DESC"
}
```

#### 创建问题

```typescript
// Create a standard issue
{
  projectKey: "PROJECT",
  summary: "Issue title",
  issueType: "Task",  // or "Story", "Bug", etc.
  description: "Detailed description",
  assignee: "accountId",  // from get_user tool
  labels: ["frontend", "urgent"],
  components: ["ui", "api"],
  priority: "High"
}

// Create a subtask
{
  parent: "PROJECT-123",
  projectKey: "PROJECT",
  summary: "Subtask title",
  issueType: "Subtask",
  description: "Subtask details",
  assignee: "accountId"
}
```

#### 更新问题

```typescript
// Update issue fields
{
  issueKey: "PROJECT-123",
  summary: "Updated title",
  description: "New description",
  assignee: "accountId",
  status: "In Progress",
  priority: "High"
}
```

#### 问题依赖

```typescript
// Create issue link
{
  linkType: "Blocks",  // from list_link_types
  inwardIssueKey: "PROJECT-124",  // blocked issue
  outwardIssueKey: "PROJECT-123"  // blocking issue
}
```

#### 删除问题

```typescript
// Delete single issue
{
  issueKey: "PROJECT-123"
}

// Delete issue with subtasks
{
  issueKey: "PROJECT-123",
  deleteSubtasks: true
}

// Delete multiple issues
{
  issueKeys: ["PROJECT-123", "PROJECT-124"]
}
```

## 字段格式

### 描述字段

描述字段支持 Markdown 样式的格式：

- 段落之间使用空行
- 使用 "- " 表示项目符号列表
- 使用 "1. " 表示编号列表
- 使用以 ":" 结尾的标题（后跟空行）

示例：

```
Task Overview:

This task involves implementing new features:
- Feature A implementation
- Feature B testing

Steps:
1. Design component
2. Implement logic
3. Add tests

Acceptance Criteria:
- All tests passing
- Documentation updated
```

## 错误处理

服务器提供详细的错误消息，包括：

- 无效的问题键
- 缺少必填字段
- 权限问题
- API 速率限制

## 设置说明

1. 克隆仓库：

```bash
   git clone https://github.com/George5562/Jira-MCP-Server.git
   cd Jira-MCP-Server
```

2. 安装依赖项：

```bash
   npm install
```

3. 配置环境变量：
   在根目录下创建一个 `.env` 文件：

```bash
   JIRA_HOST=your-instance.atlassian.net
   JIRA_EMAIL=your-email@example.com
   JIRA_API_TOKEN=your-api-token
```

4. 构建项目：

```bash
   npm run build
```

5. 启动服务器：
```bash
   npm start
```

## 配置 Claude Desktop

要将此 MCP 服务器与 Claude Desktop 一起使用，请执行以下步骤：

1. 找到您的 Claude Desktop 配置文件：

   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%/Claude/claude_desktop_config.json`
   - Linux: `~/.config/Claude/claude_desktop_config.json`

2. 将 Jira MCP 服务器添加到您的配置中：

```json
   {
     "mcp_servers": [
       {
         "name": "jira-server",
         "command": "npm start",
         "cwd": "/path/to/jira-server",
         "env": {
           "JIRA_HOST": "your-instance.atlassian.net",
           "JIRA_EMAIL": "your-email@example.com",
           "JIRA_API_TOKEN": "your-api-token"
         }
       }
     ]
   }
```

   将 `/path/to/jira-server` 替换为克隆仓库的绝对路径。

3. 重启 Claude Desktop 以应用更改。

## 参考资料

- [Model Context Protocol](https://github.com/modelcontextprotocol)
- [Jira REST API 文档](https://docs.atlassian.com/software/jira/docs/api/REST/7.12.0)
- [Jira REST API 示例](https://developer.atlassian.com/server/jira/platform/jira-rest-api-examples/)

**官方网站：** [https://github.com/George5562/Jira-MCP-Server](https://github.com/George5562/Jira-MCP-Server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`communication`
- 标签：`developer tools`, `communication`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`/path/to/node`
- 参数：`/path/to/jira-server/build/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/george5562-jira.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
