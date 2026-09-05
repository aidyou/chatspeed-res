---
title: "Terraform MCP 服务"
description: "通过 MCP 将 AI 模型连接到 Terraform 注册表，启用提供程序查找、资源使用示例和模块推荐，从而简化 Terraform 工作流。"
---

# Terraform MCP 服务

通过 MCP 将 AI 模型连接到 Terraform 注册表，启用提供程序查找、资源使用示例和模块推荐，从而简化 Terraform 工作流。

# Terraform Registry MCP 服务器

这是一个提供与 Terraform Registry API 交互工具的 Model Context Protocol (MCP) 服务器。该服务器使 AI 代理能够查询提供商信息、资源详情和模块元数据。

## 安装

### 在 Cursor 中安装

要在 [Cursor](https://cursor.sh/) 中安装并使用此 MCP 服务器：

1. 在 Cursor 中，打开设置（⌘+,）并导航到“MCP”选项卡。
   
2. 点击“+ 添加新的 MCP 服务器”。
   
3. 输入以下内容：
   - 名称：terraform-registry
   - 类型：command
   - 命令：npx -y terraform-mcp-server
   
4. 点击“添加”，然后滚动到服务器并点击“禁用”以启用服务器。

5. 如果需要，请重启 Cursor 以确保 MCP 服务器正确加载。

![terraform-registry MCP 设置 for Cursor](/mcp-assets/af879626225c9e8d31e9162616004abf.png)

### 在 Claude Desktop 中安装

要在 Claude Desktop 中安装并使用此 MCP 服务器：

1. 在 Claude Desktop 中，打开设置（⌘+,）并导航到“开发者”选项卡。

2. 点击窗口底部的“编辑配置”。

3. 编辑文件（`~/Library/Application Support/Claude/claude_desktop_config.json`）以添加以下代码，然后保存文件。

```json
{
  "mcpServers": {
    "terraform-registry": {
      "command": "npx",
      "args": ["-y", "terraform-mcp-server"]
    }
  }
}
```

4. 重启 Claude Desktop 以确保 MCP 服务器正确加载。

## 工具

此 MCP 服务器中提供了以下工具：

### 核心注册表工具

| 工具 | 描述 |
|------|-------------|
| `providerDetails` | 获取关于 Terraform 提供商的详细信息 |
| `resourceUsage` | 获取 Terraform 资源及其相关资源的示例用法 |
| `moduleSearch` | 根据查询搜索并推荐 Terraform 模块 |
| `listDataSources` | 列出提供商的所有可用数据源及其基本信息 |
| `resourceArgumentDetails` | 获取资源类型的参数的全面详细信息 |
| `moduleDetails` | 获取 Terraform 模块的详细元数据 |
| `functionDetails` | 获取关于 Terraform 提供商函数的详细信息 |
| `providerGuides` | 列出并查看特定于提供商的指南和文档 |
| `policySearch` | 在 Terraform 注册表中搜索策略库 |
| `policyDetails` | 获取特定策略库的详细信息 |

### Terraform Cloud 工具

这些工具需要一个 Terraform Cloud API 令牌 (`TFC_TOKEN`)：

| 工具 | 描述 |
|------|-------------|
| `listOrganizations` | 列出经过身份验证的用户有权访问的所有组织 |
| `privateModuleSearch` | 在组织中搜索私有模块 |
| `privateModuleDetails` | 获取关于私有模块的详细信息 |
| `explorerQuery` | 查询 Terraform Cloud Explorer API 以分析数据 |
| `listWorkspaces` | 列出组织中的工作区 |
| `workspaceDetails` | 获取特定工作区的详细信息 |
| `lockWorkspace` | 锁定工作区以防止运行 |
| `unlockWorkspace` | 解锁工作区以允许运行 |
| `listRuns` | 列出工作区的运行 |
| `runDetails` | 获取特定运行的详细信息 |
| `createRun` | 为工作区创建新的运行 |
| `applyRun` | 应用已计划的运行 |
| `cancelRun` | 取消正在进行的运行 |
| `listWorkspaceResources` | 列出工作区中的资源 |

## 资源

MCP 服务器通过 `resources/*` 方法支持以下用于列出和读取的资源 URI：

| 资源类型 | 示例 URI(s) | 描述 |
|---------------|----------------|-------------|
| **提供者** | `terraform:providers` | 列出所有命名空间/提供者 |
|               | `terraform:provider:/` | 获取特定提供者的详细信息 |
| **提供者版本** | `terraform:provider://versions` | 列出提供者的可用版本 |
| **提供者资源** | `terraform:provider://resources` | 列出提供者的资源 |
|                 | `terraform:resource://` | 获取特定资源类型的详细信息 |
| **提供者数据源** | `terraform:provider://dataSources` | 列出提供者的数据源 |
|                       | `terraform:dataSource://` | 获取特定数据源的详细信息 |
| **提供者函数** | `terraform:provider://functions` | 列出提供者的函数 |
|                      | `terraform:function://` | 获取特定函数的详细信息 |

服务器还支持 `resources/templates/list` 以提供创建以下项的模板：
- `terraform:provider`
- `terraform:resource`
- `terraform:dataSource`

## 提示

以下提示可用于生成上下文响应：

| 提示 | 描述 | 必需参数 |
|--------|-------------|-------------------|
| `migrate-clouds` | 生成 Terraform 代码以在云服务提供商之间迁移基础设施 | `sourceCloud`, `targetCloud`, `terraformCode` |
| `generate-resource-skeleton` | 帮助用户快速使用最佳实践搭建新的 Terraform 资源 | `resourceType` |
| `optimize-terraform-module` | 提供改进 Terraform 代码的具体建议 | `terraformCode` |
| `migrate-provider-version` | 协助进行提供者版本升级和处理破坏性变更 | `providerName`, `currentVersion`, `targetVersion`, `terraformCode` (可选) |
| `analyze-workspace-runs` | 分析最近的运行失败并为 Terraform Cloud 工作区提供故障排除指导 | `workspaceId`, `runsToAnalyze` (可选，默认: 5) |

### 提示已知问题

**注意**：`getPrompt` 功能存在一个已知问题，可能会导致服务器崩溃。服务器可以正确注册提示并列出它们，但直接使用 `getPrompt` 方法可能引起连接问题。此问题正在调查中，可能与 SDK 兼容性或实现细节有关。在解决之前，请使用 `listPrompts` 查看可用提示，但避免直接调用 `getPrompt`。

## 运行服务器

服务器使用 stdio 传输进行 MCP 通信：

```bash
npm install
npm start
```

### 使用环境变量配置

可以通过环境变量来配置服务器：

| 环境变量 | 描述 | 默认值 |
|---------------------|-------------|---------------|
| `TERRAFORM_REGISTRY_URL` | Terraform 注册表 API 的基础 URL | https://registry.terraform.io |
| `DEFAULT_PROVIDER_NAMESPACE` | 提供者的默认命名空间 | hashicorp |
| `LOG_LEVEL` | 日志级别（错误、警告、信息、调试） | info |
| `REQUEST_TIMEOUT_MS` | API 请求的超时时间（毫秒） | 10000 |
| `RATE_LIMIT_ENABLED` | 启用 API 请求的速率限制 | false |
| `RATE_LIMIT_REQUESTS` | 时间窗口内允许的请求数量 | 60 |
| `RATE_LIMIT_WINDOW_MS` | 速率限制的时间窗口（毫秒） | 60000 |
| `TFC_TOKEN` | 访问私有注册表的 Terraform Cloud API 令牌（可选） | |

使用环境变量的示例：

```bash
# Set environment variables
export LOG_LEVEL="debug"
export REQUEST_TIMEOUT_MS="15000"
export TFC_TOKEN="your-terraform-cloud-token"

# Run the server
npm start
```

## 测试

关于本项目的测试信息，请参阅 [TESTS.md](https://github.com/thrashr888/terraform-mcp-server/blob/HEAD/TESTS.md) 文件。

**官方网站：** [https://github.com/thrashr888/terraform-mcp-server](https://github.com/thrashr888/terraform-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`, `development`
- 标签：`cloud platforms`, `developer tools`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y terraform-mcp-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/thrashr888-terraform.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
