---
title: "知识搜索"
description: "一个模型上下文协议服务器，使像 Claude 这样的人工智能助手能够访问和搜索 Atlassian Confluence 内容，从而实现与您组织的知识库的集成。"
---

# 知识搜索

一个模型上下文协议服务器，使像 Claude 这样的人工智能助手能够访问和搜索 Atlassian Confluence 内容，从而实现与您组织的知识库的集成。

# Atlassian Confluence MCP 服务器

该项目提供了一个模型上下文协议（MCP）服务器，作为AI助手（如Anthropic的Claude、Cursor AI或其他MCP兼容客户端）和您的Atlassian Confluence实例之间的桥梁。它允许AI实时安全地访问和与您的Confluence空间和页面进行交互。

## 什么是MCP以及为什么要使用此服务器？

模型上下文协议（MCP）是一个开放标准，使AI模型能够安全地连接到外部工具和数据源。此服务器专门为Confluence实现了MCP。

**优势：**

- **实时访问：** 您的AI助手可以直接访问最新的Confluence内容。
- **消除复制/粘贴：** 无需手动在Confluence和您的AI助手之间传输信息。
- **增强的AI功能：** 使AI能够搜索、总结、分析并引用您的Confluence文档中的内容。
- **安全性：** 您可以通过API令牌控制访问权限。AI通过服务器进行交互，敏感操作被限制在服务器内。

## 可用工具

此MCP服务器为您的AI助手提供了以下工具：

```markdown
- **Page Search:** Allows the AI to search for specific pages within your Confluence instance.
- **Page Content Retrieval:** Enables the AI to fetch the content of a specific page.
- **Page Creation and Editing:** The AI can create new pages or edit existing ones.
- **Space Management:** The AI can list, create, and manage spaces in your Confluence instance.
```

请根据实际需求继续添加更多工具及其描述。

- **列出空间 (`list-spaces`)**

    - **目的：** 发现可用的 Confluence 空间并找到它们的“键”（唯一标识符）。
    - **使用时机：** 当你需要知道存在哪些空间、查找某个空间的键，或者按类型/状态过滤空间时。
    - **对话示例：** “显示所有的 Confluence 空间。”
    - **参数示例：** `{}` （基本列表不需要参数）或 `{ type: "global", status: "current" }` （用于过滤）。

- **获取空间 (`get-space`)**

    - **目的：** 使用其键检索关于特定空间的详细信息。包括主页内容片段。
    - **使用时机：** 当你知道空间键（例如，“DEV”）并且需要其完整详细信息、标签或主页概览时。
    - **对话示例：** “告诉我 Confluence 中 'DEV' 空间的详情。”
    - **参数示例：** `{ spaceKey: "DEV" }`

- **列出页面 (`list-pages`)**

    - **目的：** 列出特定空间内的页面（使用数字空间 ID），或者在整个实例中列出页面，并提供过滤选项。
    - **使用时机：** 当你需要在已知空间中查找页面（需要数字 ID）、按状态过滤，或者对标题/标签进行简单的文本搜索时。
    - **对话示例：** “显示空间 ID 123456 中当前的页面。”（如果你只知道键，请先使用 `list-spaces`）。
    - **参数示例：** `{ spaceId: ["123456"] }` 或 `{ status: ["archived"], query: "Meeting Notes" }`。

- **获取页面 (`get-page`)**

    - **目的：** 使用页面的数字 ID 检索特定页面的完整内容（以 Markdown 格式）和元数据。
    - **使用时机：** 当你知道页面的数字 ID（通过 `list-pages` 或 `search` 找到）并且需要阅读、分析或总结其内容时。
    - **对话示例：** “获取 Confluence 页面 ID 12345678 的内容。”
    - **参数示例：** `{ pageId: "12345678" }`

- **搜索 (`search`)**
    - **目的：** 使用 CQL（Confluence 查询语言）对 Confluence 内容（页面、博客、附件）执行强大的搜索。
    - **使用时机：** 当你需要涉及多个条件的复杂搜索、全文搜索或按标签、日期、贡献者等进行过滤时。
    - **对话示例：** “搜索上周创建的带有 'meeting-notes' 标签的 Confluence 页面。”
    - **参数示例：** `{ cql: "label = meeting-notes AND created > -7d" }`

## 接口理念：简单输入，丰富输出

该服务器遵循“最小接口，最大细节”的方法：

1.  **简单工具：** 只请求必要的标识符或过滤器（如 `pageId`、`spaceKey`、`cql`）。
2.  **丰富细节：** 当你请求特定项目（如 `get-page`）时，服务器默认提供所有相关信息（内容、标签、链接等），而无需额外的标志。

## 前提条件

- **Node.js 和 npm：** 确保已安装 Node.js（包含 npm）。从 [nodejs.org](https://nodejs.org/) 下载。
- **Atlassian 账户：** 一个可以访问你想连接的 Confluence 实例的有效 Atlassian 账户。

## 快速入门指南

按照以下步骤将您的 AI 助手连接到 Confluence：

### 第 1 步：获取您的 Atlassian API 令牌

**重要提示：**请像对待密码一样对待您的 API 令牌。不要与他人共享，也不要将其提交到版本控制系统中。

1.  前往您的 Atlassian API 令牌管理页面：
    [https://id.atlassian.com/manage-profile/security/api-tokens](https://id.atlassian.com/manage-profile/security/api-tokens)
2.  点击 **创建 API 令牌**。
3.  给它一个描述性的**标签**（例如，`mcp-confluence-access`）。
4.  点击 **创建**。
5.  **立即复制生成的 API 令牌。** 您之后无法再次查看该令牌。请安全地保存它。

### 第 2 步：配置服务器凭据

请选择以下方法中的**一种**：

#### 方法 A：全局 MCP 配置文件（推荐）

这种方式可以让凭据分开且有组织。

1.  **创建目录**（如果需要的话）：`~/.mcp/`
2.  **创建/编辑文件：** `~/.mcp/configs.json`
3.  **添加配置：** 复制以下 JSON 结构并替换占位符：

```json
    {
        "@aashari/mcp-server-atlassian-confluence": {
            "environments": {
                "ATLASSIAN_SITE_NAME": "",
                "ATLASSIAN_USER_EMAIL": "",
                "ATLASSIAN_API_TOKEN": ""
            }
        }
        // 如果需要，此处可添加其他服务器
    }
```

    - ``: 您的 Confluence 站点名称（例如，对于 `mycompany.atlassian.net` 使用 `mycompany`）。
    - ``: 您的 Atlassian 账户邮箱。
    - ``: 从第 1 步复制的 API 令牌。

#### 方法 B：环境变量（替代方案）

在运行服务器时设置环境变量。

```bash
ATLASSIAN_SITE_NAME="" \
ATLASSIAN_USER_EMAIL="" \
ATLASSIAN_API_TOKEN="" \
npx -y @aashari/mcp-server-atlassian-confluence
```

### 第 3 步：连接您的 AI 助手

配置您的 MCP 客户端（如 Claude Desktop, Cursor 等）以运行此服务器。

#### Claude Desktop

1.  打开设置（齿轮图标）> 编辑配置。
2.  添加或合并到 `mcpServers` 中：

```json
    {
        "mcpServers": {
            "aashari/mcp-server-atlassian-confluence": {
                "command": "npx",
                "args": ["-y", "@aashari/mcp-server-atlassian-confluence"]
            }
            // ... 其他服务器
        }
    }
```

3.  保存并**重启 Claude Desktop**。
4.  **验证：** 点击“工具”（锤子图标）；Confluence 工具应被列出。

#### Cursor AI

1.  命令面板 (`Cmd+Shift+P` / `Ctrl+Shift+P`) > **Cursor 设置 > MCP**。
2.  点击 **+ 添加新的 MCP 服务器**。
3.  输入：
    - 名称: `aashari/mcp-server-atlassian-confluence`
    - 类型: `command`
    - 命令: `npx -y @aashari/mcp-server-atlassian-confluence`
4.  点击 **添加**。
5.  **验证：** 等待服务器名称旁边的指示器变为绿色。

### 第 4 步：使用工具

现在您可以向您的 AI 助手询问有关您的 Confluence 实例的问题了：

- "列出 Confluence 空间。"
- "使用 CQL 搜索 Confluence: `label = meeting-notes AND created > -7d`"
- "获取 Confluence 页面 ID 12345678 的内容。"
- "总结 DEV 空间中的 'API Guidelines' 页面。"（你可能需要先使用 `search` 或 `list-pages` 来找到页面 ID）。

## 作为命令行工具 (CLI) 使用

你也可以直接从终端使用此包。请确保首先设置好凭证（上面的方法 A 或 B）。

#### 使用 `npx` 快速使用

```bash
npx -y @aashari/mcp-server-atlassian-confluence list-spaces
npx -y @aashari/mcp-server-atlassian-confluence get-page --page 123456
npx -y @aashari/mcp-server-atlassian-confluence search --cql "type=page AND text~API" --limit 10
```

#### 全局安装（可选）

1.  `npm install -g @aashari/mcp-server-atlassian-confluence`
2.  使用 `mcp-atlassian-confluence` 命令：

```bash
mcp-atlassian-confluence list-spaces --limit 5
mcp-atlassian-confluence get-space --space DEV
mcp-atlassian-confluence list-pages --space-id 12345 --status archived
mcp-atlassian-confluence --help # See all commands
```

## 故障排除

- **认证错误 (401/403):**
    - 检查 `~/.mcp/configs.json` 或环境变量中的 `ATLASSIAN_SITE_NAME`、`ATLASSIAN_USER_EMAIL` 和 `ATLASSIAN_API_TOKEN`。
    - 确保证书是正确的、有效的，并且未被撤销。
    - 确认您的用户帐户有权访问 Confluence 实例和相关空间/页面。
- **服务器无法连接（在 AI 客户端中）:**
    - 确保客户端配置中的命令 (`npx ...`) 是正确的。
    - 检查 Node.js/npm 安装和 PATH。
    - 在终端中直接运行 `npx` 命令以查看错误信息。
- **资源未找到 (404):**
    - 验证 `pageId`（必须是数字）或 `spaceKey` 是否正确。
    - 检查您对特定页面或空间的权限。
- **CQL 查询错误 (400):**
    - 仔细检查 CQL 语法。参考 [Confluence CQL 文档](https://developer.atlassian.com/cloud/confluence/advanced-searching-using-cql/)。
    - 确认字段名称和值有效。
- **启用调试日志:** 设置 `DEBUG=true` 环境变量（例如，在 `configs.json` 中添加 `"DEBUG": "true"` 或运行 `DEBUG=true npx ...`）。

## 对开发者：贡献

欢迎贡献！如果你想参与贡献：

- **架构:** 该服务器采用了分层方法（CLI/工具 -> 控制器 -> 服务）。详情请参见 `.cursorrules` 或代码注释。
- **设置:** 克隆仓库，`npm install`。使用 `npm run dev:server` 或 `npm run dev:cli -- `。
- **代码风格:** 使用 `npm run lint` 和 `npm run format`。
- **测试:** 通过 `npm test` 添加测试。
- **一致性:** 遵循现有的模式和“最小接口，最大细节”的理念。

## 版本说明

此项目 (`@aashari/mcp-server-atlassian-confluence`) 遵循语义化版本控制，并独立于其他 `@aashari/mcp-server-*` 包进行版本管理。

## 许可证

[ISC](https://opensource.org/licenses/ISC)

**官方网站：** [https://github.com/aashari/mcp-server-atlassian-confluence](https://github.com/aashari/mcp-server-atlassian-confluence)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`, `memory`
- 标签：`search`, `knowledge and memory`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @aashari/mcp-server-atlassian-confluence`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/aashari-atlassian-confluence.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
