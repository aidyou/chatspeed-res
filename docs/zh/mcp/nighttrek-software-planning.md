---
title: "MCP软件规划工具"
description: "通过管理任务、跟踪进度以及通过模型上下文协议创建详细的实施计划，促进交互式软件开发规划。"
---

# MCP软件规划工具

通过管理任务、跟踪进度以及通过模型上下文协议创建详细的实施计划，促进交互式软件开发规划。

# 软件规划工具 🚀
[Smithery](https://smithery.ai/server/@NightTrek/Software-planning-mcp)

这是一个设计用于通过交互式、结构化方法促进软件开发规划的模型上下文协议（MCP）服务器。此工具帮助将复杂的软件项目分解为可管理的任务，跟踪实施进度，并维护详细的开发计划。

  

## 功能 ✨

- **交互式规划会话**：启动和管理开发规划会话
- **待办事项管理**：创建、更新并跟踪开发任务
- **复杂度评分**：为任务分配复杂度分数以进行更好的估算
- **代码示例**：在任务描述中包含相关的代码片段
- **实施计划**：保存和管理详细的实施计划

## 安装 🛠️

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@NightTrek/Software-planning-mcp) 自动安装适用于 Claude 桌面版的软件规划工具：

```bash
npx -y @smithery/cli install @NightTrek/Software-planning-mcp --client claude
```

### 手动安装
1. 克隆仓库
2. 安装依赖项：
```bash
pnpm install
```
3. 构建项目：
```bash
pnpm run build
```
4. 添加到您的 MCP 设置配置文件中（通常位于 `~/Library/Application Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`）：
```json
{
  "mcpServers": {
    "software-planning-tool": {
      "command": "node",
      "args": [
        "/path/to/software-planning-tool/build/index.js"
      ],
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

## 可用工具 🔧

### start_planning
以特定目标开始新的规划会话。
```typescript
{
  goal: string  // The software development goal to plan
}
```

### add_todo
向当前计划添加一个新的待办事项。
```typescript
{
  title: string,         // Title of the todo item
  description: string,   // Detailed description
  complexity: number,    // Complexity score (0-10)
  codeExample?: string  // Optional code example
}
```

### get_todos
检索当前计划中的所有待办事项。
```typescript
// No parameters required
```

### update_todo_status
更新待办事项的完成状态。
```typescript
{
  todoId: string,     // ID of the todo item
  isComplete: boolean // New completion status
}
```

### save_plan
保存当前的实施计划。
```typescript
{
  plan: string  // The implementation plan text
}
```

### remove_todo
从当前计划中移除一个待办事项。
```typescript
{
  todoId: string  // ID of the todo item to remove
}
```

## 使用示例 📝

这里是一个使用软件规划工具的完整示例：

1. 开始一个规划会话：
```typescript
await client.callTool("software-planning-tool", "start_planning", {
  goal: "Create a React-based dashboard application"
});
```

2. 添加一个待办事项：
```typescript
const todo = await client.callTool("software-planning-tool", "add_todo", {
  title: "Set up project structure",
  description: "Initialize React project with necessary dependencies",
  complexity: 3,
  codeExample: `
npx create-react-app dashboard
cd dashboard
npm install @material-ui/core @material-ui/icons
  `
});
```

3. 更新待办事项状态：
```typescript
await client.callTool("software-planning-tool", "update_todo_status", {
  todoId: todo.id,
  isComplete: true
});
```

4. 保存实施计划：
```typescript
await client.callTool("software-planning-tool", "save_plan", {
  plan: `
# Dashboard Implementation Plan

## Phase 1: Setup (Complexity: 3)
- Initialize React project
- Install dependencies
- Set up routing

## Phase 2: Core Features (Complexity: 5)
- Implement authentication
- Create dashboard layout
- Add data visualization components
  `
});
```

## 开发 🔨

### 项目结构
```
software-planning-tool/
  ├── src/
  │   ├── index.ts        # Main server implementation
  │   ├── prompts.ts      # Planning prompts and templates
  │   ├── storage.ts      # Data persistence
  │   └── types.ts        # TypeScript type definitions
  ├── build/              # Compiled JavaScript
  ├── package.json
  └── tsconfig.json
```

### 构建
```bash
pnpm run build
```

### 测试
使用 MCP 检查器测试所有功能：
```bash
pnpm run inspector
```

## 许可证 📄

MIT

---

使用 Model Context Protocol 以 ❤️ 制作

**官方网站：** [https://github.com/NightTrek/Software-planning-mcp](https://github.com/NightTrek/Software-planning-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`/path/to/software-planning-tool/build/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/nighttrek-software-planning.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
