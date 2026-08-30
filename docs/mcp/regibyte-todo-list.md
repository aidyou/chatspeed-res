---
title: "MCP任务清单"
description: "一个模型上下文协议（MCP）服务器，提供管理待办事项的工具，包括创建、更新、完成、删除、搜索和汇总任务。"
---

# MCP任务清单

一个模型上下文协议（MCP）服务器，提供管理待办事项的工具，包括创建、更新、完成、删除、搜索和汇总任务。

# 待办事项 MCP 服务器

这是一个提供全面 API 的 Model Context Protocol (MCP) 服务器，用于管理待办事项。

  

> **📚 学习资源**：此项目设计为 MCP 实现的教育示例。请参阅 [GUIDE.md](https://github.com/RegiByte/todo-list-mcp/blob/HEAD/GUIDE.md) 以了解项目的详细工作原理及其实现方式。

## 功能

- **创建待办事项**：添加带有标题和 Markdown 描述的新任务
- **更新待办事项**：修改现有任务
- **完成待办事项**：标记任务为已完成
- **删除待办事项**：从列表中移除任务
- **搜索待办事项**：按标题或创建日期查找任务
- **总结待办事项**：快速概览活动任务

## 工具

此 MCP 服务器提供了以下工具：

1. `create-todo`：创建一个新的待办事项
2. `list-todos`：列出所有待办事项
3. `get-todo`：通过 ID 获取特定的待办事项
4. `update-todo`：更新待办事项的标题或描述
5. `complete-todo`：标记待办事项为已完成
6. `delete-todo`：删除一个待办事项
7. `search-todos-by-title`：按标题搜索待办事项（不区分大小写的部分匹配）
8. `search-todos-by-date`：按创建日期搜索待办事项（格式：YYYY-MM-DD）
9. `list-active-todos`：列出所有未完成的待办事项
10. `summarize-active-todos`：生成所有活动（未完成）待办事项的摘要

## 安装

```bash
# Clone the repository
git clone https://github.com/RegiByte/todo-list-mcp.git
cd todo-list-mcp

# Install dependencies
npm install

# Build the project
npm run build
```

## 使用方法

### 启动服务器

```bash
npm start
```

### 与 Claude 桌面版配置

#### Claude 桌面版

将以下内容添加到您的 `claude_desktop_config.json` 中：

```json
{
  "mcpServers": {
    "todo": {
      "command": "node",
      "args": ["/absolute/path/to/todo-list-mcp/dist/index.js"]
    }
  }
}
```

#### Cursor

- 前往“光标设置” -> MCP
- 添加一个新的命令类型的 MCP 服务器
- 添加服务器的绝对路径并使用 node 运行
- 示例：node /absolute/path/to/todo-list-mcp/dist/index.js

### 示例命令

当与 Claude 桌面版或 Cursor 一起使用时，您可以尝试：

- “创建一个学习 MCP 的待办事项，并附上说明为什么 MCP 是有用的描述”
- “列出我所有的活动待办事项”
- “为明天的会议创建一个待办事项，并在 Markdown 中包含议程详情”
- “将我的学习 MCP 待办事项标记为已完成”
- “总结我所有的活动待办事项”

## 项目结构

此项目遵循清晰的关注点分离原则，使代码易于理解：

```
src/
├── models/       # Data structures and validation schemas
├── services/     # Business logic and database operations
├── utils/        # Helper functions and formatters
├── config.ts     # Configuration settings
├── client.ts     # Test client for local testing
└── index.ts      # Main entry point with MCP tool definitions
```

## 从此项目中学习

此项目设计为教育资源。为了最大限度地利用它：

1. 阅读 [GUIDE.md](https://github.com/RegiByte/todo-list-mcp/blob/HEAD/GUIDE.md) 以获得设计的全面解释
2. 研究源代码中的注释以了解实现细节
3. 使用测试客户端查看服务器的实际运行情况
4. 尝试添加自己的工具或扩展现有工具

## 开发

### 构建

```bash
npm run build
```

### 以开发模式运行

```bash
npm run dev
```

## 许可证

MIT

**官方网站：** [https://github.com/RegiByte/todo-list-mcp](https://github.com/RegiByte/todo-list-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`memory`
- 标签：`note taking`, `knowledge and memory`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`/absolute/path/to/todo-list-mcp/dist/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/regibyte-todo-list.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
