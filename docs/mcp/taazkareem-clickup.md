---
title: "ClickUp 任务管理 AI 推荐"
description: "启用与 ClickUp 任务的 AI 集成，支持资源管理、任务操作、工作区组织以及通过标准化协议进行的 AI 驱动的任务推荐。"
---

# ClickUp 任务管理 AI 推荐

启用与 ClickUp 任务的 AI 集成，支持资源管理、任务操作、工作区组织以及通过标准化协议进行的 AI 驱动的任务推荐。

alt="ClickUp MCP Server" width="100%">

[![GitHub Stars](/mcp-assets/c8ab93d8df15924ea3f3648c84d5a38e.svg)](https://github.com/TaazKareem/clickup-mcp-server/stargazers)
[![Maintenance](/mcp-assets/c7778e30c5b75ad6bdf042640f8a94d9.svg)](https://github.com/TaazKareem/clickup-mcp-server/graphs/commit-activity)

一个用于将 ClickUp 任务与 AI 应用程序集成的 Model Context Protocol (MCP) 服务器。此服务器允许 AI 代理通过标准化协议与 ClickUp 任务、空间、列表和文件夹进行交互。

> 🚧 **状态更新：** 推出 v0.6.8 版本将增加全局任务查找功能（智能消歧）、支持使用自然语言表达的任务开始日期、完整的标签支持（包括自然语言标签颜色命令）、子任务支持、自定义 ID 支持以及日志修复

## 设置

1. 获取您的凭据：
   - 从 [ClickUp 设置](https://app.clickup.com/settings/apps) 中获取 ClickUp API 密钥
   - 从您的 ClickUp 工作区 URL 中获取团队 ID
2. 选择托管安装（发送 Webhook）或 NPX 安装（下载到本地路径并安装依赖项）
3. 使用自然语言管理您的工作区！

## Smithery 安装（快速启动）

[Smithery](https://smithery.ai/server/@TaazKareem/clickup-mcp-server)

该服务器托管在 [Smithery](https://smithery.ai/server/@taazkareem/clickup-mcp-server) 上。在那里，您可以预览可用工具或复制要在特定客户端应用程序上运行的命令。

## NPX 安装

[![NPM Version](/mcp-assets/63a09ba3381401ee3ab91cb41b16156b.svg)](https://www.npmjs.com/package/@taazkareem/clickup-mcp-server)
[![Dependency Status](/mcp-assets/80a22720777445f6d9736d2023c537c2.svg)](https://github.com/TaazKareem/clickup-mcp-server/blob/main/package.json)
[![NPM Downloads](/mcp-assets/b5f06d7741a799aa895607d5a3ccc7bd.svg)](https://npmcharts.com/compare/@taazkareem/clickup-mcp-server?minimal=true)

将此条目添加到您的客户端 MCP 设置 JSON 文件中：

```json
{
  "mcpServers": {
    "ClickUp": {
      "command": "npx",
      "args": [
        "-y",
        "@taazkareem/clickup-mcp-server@latest"
      ],
      "env": {
        "CLICKUP_API_KEY": "your-api-key",
        "CLICKUP_TEAM_ID": "your-team-id"
      }
    }
  }
}
```

或者使用此 npx 命令：

`npx -y @taazkareem/clickup-mcp-server@latest --env CLICKUP_API_KEY=your-api-key --env CLICKUP_TEAM_ID=your-team-id`

## 功能

| 📝 任务管理 | 🏷️ 标签管理 |
|----------------------------|----------------------------|
| • 创建、更新和删除任务
• 在任何地方移动和复制任务
• 支持单个和批量操作
• 使用自然语言设置开始/截止日期
• 创建和管理子任务
• 添加评论和附件 | • 创建、更新和删除空间标签
• 向任务添加或移除标签
• 使用自然语言颜色命令
• 自动对比前景色
• 查看所有空间标签
• 基于标签的任务组织跨越工作区 |

| 🌳 **工作区组织** | ⚡ **集成特性** |
| • 导航空间、文件夹和列表
• 创建和管理文件夹
• 在空间内组织列表
• 在文件夹中创建列表
• 查看工作区层次结构
• 高效路径导航 | • 全局名称或基于ID的查找
• 不区分大小写的匹配
• Markdown格式支持
• 内置速率限制
• 错误处理和验证
• 全面的API覆盖 |

## 可用工具

| Tool | Description | Required Parameters |
|------|-------------|-------------------|
| get_workspace_hierarchy | Get workspace structure | None |
| create_task | Create a task | `name`, (`listId`/`listName`) |
| create_bulk_tasks | Create multiple tasks | `tasks[]` |
| update_task | Modify task | `taskId`/`taskName` |
| update_bulk_tasks | Update multiple tasks | `tasks[]` with IDs or names |
| get_tasks | Get tasks from list | `listId`/`listName` |
| get_task | Get single task details | `taskId`/`taskName` (with smart disambiguation) |
| get_workspace_tasks | Get tasks with filtering | At least one filter (tags, list_ids, space_ids, etc.) |
| get_task_comments | Get comments on a task | `taskId`/`taskName` |
| create_task_comment | Add a comment to a task | `commentText`, (`taskId`/(`taskName`+`listName`)) |
| attach_task_file | Attach file to a task | `taskId`/`taskName`, (`file_data` or `file_url`) |
| delete_task | Remove task | `taskId`/`taskName` |
| delete_bulk_tasks | Remove multiple tasks | `tasks[]` with IDs or names |
| move_task | Move task | `taskId`/`taskName`, `listId`/`listName` |
| move_bulk_tasks | Move multiple tasks | `tasks[]` with IDs or names, target list |
| duplicate_task | Copy task | `taskId`/`taskName`, `listId`/`listName` |
| create_list | Create list in space | `name`, `spaceId`/`spaceName` |
| create_folder | Create folder | `name`, `spaceId`/`spaceName` |
| create_list_in_folder | Create list in folder | `name`, `folderId`/`folderName` |
| get_folder | Get folder details | `folderId`/`folderName` |
| update_folder | Update folder properties | `folderId`/`folderName` |
| delete_folder | Delete folder | `folderId`/`folderName` |
| get_list | Get list details | `listId`/`listName` |
| update_list | Update list properties | `listId`/`listName` |
| delete_list | Delete list | `listId`/`listName` |
| get_space_tags | Get space tags | `spaceId`/`spaceName` |
| create_space_tag | Create tag | `tagName`, `spaceId`/`spaceName` |
| update_space_tag | Update tag | `tagName`, `spaceId`/`spaceName` |
| delete_space_tag | Delete tag | `tagName`, `spaceId`/`spaceName` |
| add_tag_to_task | Add tag to task | `tagName`, `taskId`/(`taskName`+`listName`) |
| remove_tag_from_task | Remove tag from task | `tagName`, `taskId`/(`taskName`+`listName`) |

请参阅完整文档以获取可选参数和高级用法。

## 提示
尚未实现，并且不是所有客户端应用程序都支持。请求一个对您的工作流程最有益的提示实现（不要太具体）。示例：

| 提示 | 目的 | 功能 |
|--------|---------|----------|
| summarize_tasks | 任务概览 | 状态总结、优先级、关系 |
| analyze_priorities | 优先级优化 | 分布分析、排序 |
| generate_description | 任务描述创建 | 目标、标准、依赖 |

## 错误处理

服务器为以下情况提供清晰的错误消息：
- 缺少必需参数
- 无效的ID或名称
- 项目未找到
- 权限问题
- API错误
- 速率限制

可以通过设置`LOG_LEVEL`环境变量来控制服务器日志的详细程度。有效值包括 `trace`, `debug`, `info`, `warn`, 和 `error`（默认）。
这也可以通过命令行指定，例如 `--env LOG_LEVEL=info`。

## 支持开发者

在使用此服务器时，您可能会偶尔看到一个小赞助信息，其中包含工具响应中的指向本仓库的链接。希望您可以支持该项目！
如果您认为这个项目有用，请考虑支持：

[![Sponsor TaazKareem](/mcp-assets/76fc25891c633e752edf4505b06e8874.svg)](https://github.com/sponsors/TaazKareem)

  

## 致谢

特别感谢[ClickUp](https://clickup.com)提供的优秀API和服务，使这一集成成为可能。

## 贡献

欢迎贡献！请阅读我们的贡献指南了解详情。

## 许可证

[![License: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://opensource.org/licenses/MIT)

本项目采用MIT许可证 - 详情请见[LICENSE](https://github.com/TaazKareem/clickup-mcp-server/blob/HEAD/LICENSE)文件。

## 免责声明

本软件使用了第三方API，并可能引用第三方拥有的商标或品牌。使用这些API或引用并不意味着与相关公司有任何关联或得到其认可。所有商标和品牌名称均为各自所有者的财产。此项目是独立作品，与文中提及的任何第三方公司无官方关联或赞助。

**官方网站：** [https://github.com/TaazKareem/clickup-mcp-server](https://github.com/TaazKareem/clickup-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`, `browser`
- 标签：`developer tools`, `os automation`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @taazkareem/clickup-mcp-server@latest`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/taazkareem-clickup.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
