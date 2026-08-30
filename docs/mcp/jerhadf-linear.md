---
title: "Linear协作工具"
description: "一个集成了Linear问题跟踪系统的模型上下文协议服务器，允许大型语言模型通过自然语言交互创建、更新、搜索和评论Linear问题。"
---

# Linear协作工具

一个集成了Linear问题跟踪系统的模型上下文协议服务器，允许大型语言模型通过自然语言交互创建、更新、搜索和评论Linear问题。

# Linear MCP 服务器

[![npm version](/mcp-assets/d7ee6b6f2c88f845cdef2e7b8e71abb0.svg)](https://www.npmjs.com/package/linear-mcp-server) [Smithery](https://smithery.ai/server/linear-mcp-server)

这是一个用于 [Linear API](https://developers.linear.app/docs/graphql/working-with-the-graphql-api) 的 [Model Context Protocol](https://github.com/modelcontextprotocol) 服务器。

该服务器通过 MCP 提供与 Linear 问题跟踪系统的集成，允许 LLM 与 Linear 问题进行交互。

## 安装

### 自动安装

要通过 [Smithery](https://smithery.ai/protocol/linear-mcp-server) 自动为 Claude Desktop 安装 Linear MCP 服务器：

```bash
npx @smithery/cli install linear-mcp-server --client claude
```

### 手动安装

1. 为您的团队创建或获取一个 Linear API 密钥：[https://linear.app/YOUR-TEAM/settings/api](https://linear.app/YOUR-TEAM/settings/api)

2. 将服务器配置添加到 Claude Desktop 中：
   - MacOS: `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "linear": {
      "command": "npx",
      "args": [
        "-y",
        "linear-mcp-server"
      ],
      "env": {
        "LINEAR_API_KEY": "your_linear_api_key_here"
      }
    }
  }
}
```

## 组件

### 工具

1. **`linear_create_issue`**: 创建新的 Linear 问题
   - 必需输入:
     - `title` (字符串): 问题标题
     - `teamId` (字符串): 创建问题的团队 ID
   - 可选输入:
     - `description` (字符串): 问题描述（支持 markdown）
     - `priority` (数字, 0-4): 优先级（1=紧急, 4=低）
     - `status` (字符串): 初始状态名称

2. **`linear_update_issue`**: 更新现有问题
   - 必需输入:
     - `id` (字符串): 要更新的问题 ID
   - 可选输入:
     - `title` (字符串): 新标题
     - `description` (字符串): 新描述
     - `priority` (数字, 0-4): 新优先级
     - `status` (字符串): 新状态名称

3. **`linear_search_issues`**: 使用灵活过滤搜索问题
   - 可选输入:
     - `query` (字符串): 在标题/描述中搜索文本
     - `teamId` (字符串): 按团队筛选
     - `status` (字符串): 按状态筛选
     - `assigneeId` (字符串): 按指派者筛选
     - `labels` (字符串数组): 按标签筛选
     - `priority` (数字): 按优先级筛选
     - `limit` (数字, 默认: 10): 最大结果数

4. **`linear_get_user_issues`**: 获取分配给用户的问题
   - 可选输入:
     - `userId` (字符串): 用户 ID（省略则使用已认证用户）
     - `includeArchived` (布尔值): 包含归档问题
     - `limit` (数字, 默认: 50): 最大结果数

5. **`linear_add_comment`**: 向问题添加评论
   - 必需输入:
     - `issueId` (字符串): 要评论的问题 ID
     - `body` (字符串): 评论文本（支持 markdown）
   - 可选输入:
     - `createAsUser` (字符串): 自定义用户名
     - `displayIconUrl` (字符串): 自定义头像 URL

### 资源

- `linear-issue:///{issueId}` - 查看单个问题详情
- `linear-team:///{teamId}/issues` - 查看团队问题
- `linear-user:///{userId}/assigned` - 查看用户的分配问题
- `linear-organization:` - 查看组织信息
- `linear-viewer:` - 查看当前用户上下文

## 使用示例

一些您可以与 Claude Desktop 一起使用的示例提示以与 Linear 互动：

1. "显示我所有高**优先级**的问题" → 执行 `search_issues` 工具和/或 `linear-user:///{userId}/assigned` 以查找分配给你的优先级为1的问题

2. "根据我已经告诉你的关于这个错误的信息，为认证系统创建一个错误报告" → 使用 `create_issue` 创建一个新的高优先级问题，并附上适当的信息和状态跟踪

3. "找到所有正在进行中的前端任务" → 使用 `search_issues` 定位与前端相关的、状态为进行中的任务

4. "给我一份关于移动应用开发问题的最新更新摘要" → 使用 `search_issues` 确定相关问题，然后通过 `linear-issue:///{issueId}` 获取问题详情并展示最近的活动和评论

5. "移动团队当前的工作量是多少？" → 结合使用 `linear-team:///{teamId}/issues` 和 `search_issues` 来分析移动团队中问题的分布情况及优先级

## 开发

1. 安装依赖项：

```bash
npm install
```

1. 在`.env`中配置Linear API密钥：

```bash
LINEAR_API_KEY=your_api_key_here
```

1. 构建服务器：

```bash
npm run build
```

对于带有自动重建功能的开发：

```bash
npm run watch
```

## 许可证

此MCP服务器依据MIT许可证发布。这意味着你可以在遵守MIT许可证条款和条件的前提下自由地使用、修改和分发该软件。更多详情，请参阅项目仓库中的LICENSE文件。

**官方网站：** [https://github.com/jerhadf/linear-mcp-server](https://github.com/jerhadf/linear-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`communication`
- 标签：`developer tools`, `communication`, `version control`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y linear-mcp-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/jerhadf-linear.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
