---
title: "Todoist-MCP 服务器（待办事项自然语言管理工具）"
description: "一个集成了Claude与Todoist的MCP服务器，支持使用自然语言进行任务管理，包括创建、更新、完成和删除任务。"
---

# Todoist-MCP 服务器（待办事项自然语言管理工具）

一个集成了Claude与Todoist的MCP服务器，支持使用自然语言进行任务管理，包括创建、更新、完成和删除任务。

# Todoist MCP 服务器
[Smithery](https://smithery.ai/server/@abhiz123/todoist-mcp-server)

这是一个实现了 MCP（Model Context Protocol）协议的服务器，它将 Claude 与 Todoist 集成在一起，从而实现自然语言任务管理。该服务器允许 Claude 使用日常语言与您的 Todoist 任务进行交互。

  

## 功能

* **自然语言任务管理**：使用日常语言创建、更新、完成和删除任务
* **智能任务搜索**：通过部分名称匹配查找任务
* **灵活的过滤**：按截止日期、优先级和其他属性筛选任务
* **丰富的任务详情**：支持描述、截止日期和优先级级别
* **直观的错误处理**：清晰的反馈以提供更好的用户体验

## 安装

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@abhiz123/todoist-mcp-server) 自动为 Claude 桌面版安装 Todoist MCP 服务器：

```bash
npx -y @smithery/cli install @abhiz123/todoist-mcp-server --client claude
```

### 手动安装
```bash
npm install -g @abhiz123/todoist-mcp-server
```

## 工具

### todoist_create_task
创建具有各种属性的新任务：
* 必填项：内容（任务标题）
* 可选项：描述、截止日期、优先级（1-4）
* 示例：“创建名为'Team Meeting'的任务，描述为'Weekly sync'，截止日期为明天”

### todoist_get_tasks
检索并筛选任务：
* 按截止日期、优先级或项目筛选
* 自然语言日期筛选
* 可选结果限制
* 示例：“显示本周到期的高优先级任务”

### todoist_update_task
使用自然语言搜索更新现有任务：
* 通过部分名称匹配找到任务
* 更新任何任务属性（内容、描述、截止日期、优先级）
* 示例：“将会议任务的截止日期改为下周一”

### todoist_complete_task
使用自然语言搜索标记任务为已完成：
* 通过部分名称匹配找到任务
* 确认完成状态
* 示例：“将文档任务标记为已完成”

### todoist_delete_task
使用自然语言搜索移除任务：
* 通过名称找到并删除任务
* 确认消息
* 示例：“删除 PR 审核任务”

## 设置

### 获取 Todoist API 令牌
1. 登录您的 Todoist 账户
2. 导航到设置 → 集成
3. 在“开发者”下找到您的 API 令牌

### 与 Claude 桌面版一起使用

添加到您的 `claude_desktop_config.json` 文件中：

```json
{
  "mcpServers": {
    "todoist": {
      "command": "npx",
      "args": ["-y", "@abhiz123/todoist-mcp-server"],
      "env": {
        "TODOIST_API_TOKEN": "your_api_token_here"
      }
    }
  }
}
```

## 示例用法

### 创建任务
```
"Create task 'Team Meeting'"
"Add task 'Review PR' due tomorrow at 2pm"
"Create high priority task 'Fix bug' with description 'Critical performance issue'"
```

### 获取任务
```
"Show all my tasks"
"List tasks due today"
"Get high priority tasks"
"Show tasks due this week"
```

### 更新任务
```
"Update documentation task to be due next week"
"Change priority of bug fix task to urgent"
"Add description to team meeting task"
```

### 完成任务
```
"Mark the PR review task as complete"
"Complete the documentation task"
```

### 删除任务
```
"Delete the PR review task"
"Remove meeting prep task"
```

## 开发

### 从源代码构建
```bash
# Clone the repository
git clone https://github.com/abhiz123/todoist-mcp-server.git

# Navigate to directory
cd todoist-mcp-server

# Install dependencies
npm install

# Build the project
npm run build
```

## 贡献
欢迎贡献！随时提交 Pull Request。

## 许可证
本项目根据 MIT 许可证发布 - 详见 [LICENSE](https://github.com/abhiz123/todoist-mcp-server/blob/HEAD/LICENSE) 文件。

## 问题和支持
如果您遇到任何问题或需要支持，请在 [GitHub 仓库](https://github.com/abhiz123/todoist-mcp-server/issues)上提交一个 issue。

**官方网站：** [https://github.com/abhiz123/todoist-mcp-server](https://github.com/abhiz123/todoist-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`productivity`
- 标签：`note taking`, `calendar management`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @abhiz123/todoist-mcp-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/abhiz123-todoist.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
