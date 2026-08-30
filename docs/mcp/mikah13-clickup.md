---
title: "ClickUp开发服务"
description: "ClickUp API的MCP服务器，"
---

# ClickUp开发服务

ClickUp API的MCP服务器，

# ClickUp MCP 服务器

[Smithery](https://smithery.ai/server/@mikah13/mcp-clickup)

用于 ClickUp API 的 MCP 服务器，使 Claude 能够与 ClickUp 工作区进行交互。

## 工具

1. `clickup_authenticate`
   - 使用 API 令牌和工作区 ID 对 ClickUp API 进行身份验证
   - 必需的输入：
     - `api_token` (字符串)：用于身份验证的 ClickUp API 令牌
     - `workspace_id` (字符串)：用于身份验证的 ClickUp 工作区 ID
   - 返回：用户信息和身份验证状态

2. `clickup_get_task`
   - 通过任务 ID 从 ClickUp 中检索任务
   - 必需的输入：
     - `api_token` (字符串)：用于身份验证的 ClickUp API 令牌
     - `task_id` (字符串)：要检索的 ClickUp 任务的 ID
   - 返回：包括描述、状态和元数据在内的详细任务信息

3. `clickup_get_task_by_custom_id`
   - 通过自定义 ID 从 ClickUp 中检索任务
   - 必需的输入：
     - `api_token` (字符串)：用于身份验证的 ClickUp API 令牌
     - `custom_id` (字符串)：要检索的 ClickUp 任务的自定义 ID
     - `workspace_id` (字符串)：API 请求所需的工作区 ID
   - 返回：包括描述、状态和元数据在内的详细任务信息

4. `clickup_get_tasks`
   - 通过它们的 ID 从 ClickUp 中检索多个任务
   - 必需的输入：
     - `api_token` (字符串)：用于身份验证的 ClickUp API 令牌
     - `workspace_id` (字符串)：ClickUp 工作区 ID
     - `task_ids` (字符串数组)：要检索的任务 ID 列表
   - 返回：包含完整信息的任务列表

## 设置

1. 获取您的 ClickUp API 令牌：
   - 登录到您的 ClickUp 帐户
   - 转到设置 → 应用程序
   - 点击“生成 API 令牌”
   - 复制您的 API 令牌

2. 获取您的工作区 ID：
   - 在浏览器中打开 ClickUp
   - 工作区 ID 在 URL 中：`https://app.clickup.com/{workspace_id}/home`
   - 它是一个以数字开头的数字

### 与 Claude 桌面版一起使用

将以下内容添加到您的 `claude_desktop_config.json` 文件中：

#### npx

```json
{
  "mcpServers": {
    "clickup": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-clickup"
      ],
      "env": {
        "CLICKUP_API_TOKEN": "your-api-token",
        "CLICKUP_WORKSPACE_ID": "your-workspace-id"
      }
    }
  }
}
```

#### docker

```json
{
  "mcpServers": {
    "clickup": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e",
        "CLICKUP_API_TOKEN",
        "-e",
        "CLICKUP_WORKSPACE_ID",
        "mcp/clickup"
      ],
      "env": {
        "CLICKUP_API_TOKEN": "your-api-token",
        "CLICKUP_WORKSPACE_ID": "your-workspace-id"
      }
    }
  }
}
```

### 故障排除

如果您遇到错误，请验证：
1. 您的 API 令牌有效且未过期
2. 工作区 ID 正确
3. 您在 ClickUp 工作区中有必要的权限
4. 您尝试访问的任务 ID 存在且对您可访问

## 构建

Docker 构建：

```bash
docker build -t mcp/clickup .
```

## 许可证

此 MCP 服务器根据 MIT 许可证许可。这意味着您可以自由使用、修改和分发该软件，但须遵守 MIT 许可证的条款和条件。有关更多详细信息，请参阅项目存储库中的 LICENSE 文件。

**官方网站：** [https://github.com/mikah13/mcp-clickup](https://github.com/mikah13/mcp-clickup)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`communication`
- 标签：`developer tools`, `communication`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y mcp-clickup`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/mikah13-clickup.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
