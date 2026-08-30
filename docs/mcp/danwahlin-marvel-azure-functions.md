---
title: "Marvel MCP Azure Functions 服务器"
description: "一个基于 Azure Functions 的 MCP 服务器，通过官方的 Marvel Developer API 实现与漫威角色和漫画数据的交互。"
---

# Marvel MCP Azure Functions 服务器

一个基于 Azure Functions 的 MCP 服务器，通过官方的 Marvel Developer API 实现与漫威角色和漫画数据的交互。

alt="" align="center" height="96" />

# 使用 Azure Functions 的 Marvel MCP 服务器

[![在 GitHub Codespaces 中打开项目](/mcp-assets/e29451ff7eaeb8ab1950f61923a2a51f.svg)](https://codespaces.new/danwahlin/marvel-mcp?hide_repo_select=true&ref=main&quickstart=true)

![许可证](/mcp-assets/e7774bdc19bec59b68324eb77825eb99.svg)

[功能](#features) • [工具](#tools) • [设置](#setup) • [配置 MCP 主机](#configuring-an-mcp-host)

用于 [Marvel Developer API](https://developer.marvel.com/documentation/getting_started) 的 MCP 服务器，支持与角色和漫画数据进行交互。*该项目的主要目标是展示如何使用 Azure Functions 托管的 MCP 服务器与 API 进行交互。*

> **注意**：此 MCP 服务器使用的所有数据均从 [官方 Marvel API](https://developer.marvel.com/documentation/getting_started) 获取，并归 Marvel 所有。本项目与 Marvel 没有任何关联。

## 🔧 功能

- **列出 Marvel 角色**：支持 `nameStartsWith`、`limit`、`comics`、`series` 等过滤器。
- **通过 ID 获取 Marvel 角色**：使用 `characterId` 获取任何角色的详细信息。
- **获取角色的漫画**：获取包含特定角色的漫画列表，并支持 `format`、`dateRange` 等各种过滤器。
- **基于工具的 MCP 集成**：将此服务器注册到 Model Context Protocol (MCP) 工具（如 VS Code、Claude 等）。
- **环境配置**：使用 `.env` 文件管理环境变量，如 `MARVEL_PUBLIC_KEY`、`MARVEL_PRIVATE_KEY` 和 `MARVEL_API_BASE`。

## 🧰 工具

### 1. `get_characters` 🔍🦸‍♂️
- **描述**：使用可选过滤器获取 Marvel 角色。
- **输入**：
  - `name` (可选字符串)：完整的角色名称。
  - `nameStartsWith` (可选字符串)：名称以指定字符串开头的角色。
  - `modifiedSince` (可选字符串)：ISO 8601 日期字符串，用于筛选自该日期以来修改过的角色。
  - `comics`, `series`, `events`, `stories` (可选字符串)：逗号分隔的 ID 列表，用于按相关实体过滤。
  - `orderBy` (可选字符串)：结果排序字段，例如 `name` 或 `-modified`。
  - `limit` (可选数字)：返回的最大结果数 (1–100)。
  - `offset` (可选数字)：分页时跳过的结果数。
- **返回**：包含匹配角色的 JSON 响应。详情请参见 `src/schemas.ts` 中的 `CharacterDataWrapperSchema`。

### 2. `get_character_by_id` 🆔🧑‍🎤
- **描述**：通过其唯一 ID 获取 Marvel 角色。
- **输入**：
  - `characterId` (数字)：角色的唯一 ID。
- **返回**：包含角色详细信息的 JSON 响应。详情请参见 `src/schemas.ts` 中的 `CharacterDataWrapperSchema`。

### 3. `get_comics_for_character` 📚🎭

- **描述**: 获取包含特定角色的漫画，可选过滤条件。
- **输入**:
  - `characterId` (数字): 角色的唯一ID。
  - 可选过滤条件:
    - `format`, `formatType` (字符串): 按漫画格式过滤（例如，`comic`, `hardcover`）。
    - `noVariants`, `hasDigitalIssue` (布尔值): 排除变体或仅包括数字版的标志。
    - `dateDescriptor` (字符串): 预定义的日期范围，如 `thisWeek`, `nextWeek`。
    - `dateRange` (字符串): 自定义日期范围，格式为 `YYYY-MM-DD,YYYY-MM-DD`。
    - `title`, `titleStartsWith` (字符串): 按标题或标题前缀过滤。
    - `startYear`, `issueNumber`, `digitalId` (数字): 数字过滤器。
    - `diamondCode`, `upc`, `isbn`, `ean`, `issn` (字符串): 标识符过滤器。
    - `creators`, `series`, `events`, `stories`, `sharedAppearances`, `collaborators` (字符串): 相关实体ID的逗号分隔列表。
    - `orderBy` (字符串): 用于排序结果的字段，例如 `title` 或 `-modified`。
    - `limit`, `offset` (数字): 分页选项。
- **返回**: 包含指定角色的漫画的JSON响应。详情请参见 `src/schemas.ts` 中的 `ComicDataWrapperSchema`。

### 4. `get_comics` 📖🕵️‍♂️

- **描述**: 获取带有可选过滤器的漫威漫画列表。
- **输入**:
  - `format` (可选字符串): 按发行格式过滤（例如，`comic`, `digital comic`, `hardcover`）。
  - `formatType` (可选字符串): 按发行格式类型过滤 (`comic` 或 `collection`)。
  - `noVariants` (可选布尔值): 从结果集中排除变体（替代封面、二次印刷、导演剪辑等）。
  - `dateDescriptor` (可选字符串): 返回预定义日期范围内的漫画 (`lastWeek`, `thisWeek`, `nextWeek`, `thisMonth`)。
  - `dateRange` (可选字符串): 返回自定义日期范围内的漫画。日期必须指定为 `YYYY-MM-DD,YYYY-MM-DD` 格式。
  - `title` (可选字符串): 仅返回标题与输入匹配的系列中的期数。
  - `titleStartsWith` (可选字符串): 仅返回标题以输入开头的系列中的期数。
  - `startYear` (可选数字): 仅返回开始年份与输入匹配的系列中的期数。
  - `issueNumber` (可选数字): 仅返回期数与输入匹配的系列中的期数。
  - `diamondCode`, `digitalId`, `upc`, `isbn`, `ean`, `issn` (可选字符串): 按各种标识符过滤。
  - `hasDigitalIssue` (可选布尔值): 仅包括可以数字化获取的结果。
  - `modifiedSince` (可选字符串): 仅返回自指定日期以来修改过的漫画（ISO 8601 格式）。
  - `creators`, `characters`, `series`, `events`, `stories`, `sharedAppearances`, `collaborators` (可选字符串): 通过相关实体的ID列表进行过滤，用逗号分隔。
  - `orderBy` (可选字符串): 按字段或多个字段对结果集排序。在值前加"-"表示降序排列（例如，`title`, `-modified`）。
  - `limit` (可选数字): 将结果集限制为指定数量的资源（默认：20，最大：100）。
  - `offset` (可选数字): 在结果集中跳过指定数量的资源。
- **返回**: 匹配的漫画的JSON响应。详情见 `src/schemas.ts` 中的 `ComicDataWrapperSchema`。

### 5. `get_comic_by_id` 🆔📘
- **描述**: 通过唯一的ID获取单个漫威漫画。
- **输入**:
  - `comicId` (数字): 漫画的唯一ID。
- **返回**: 漫画详情的JSON响应。详情见 `src/schemas.ts` 中的 `ComicDataWrapperSchema`。

### 6. `get_characters_for_comic` 🦸‍♀️📖

- **描述**: 获取出现在特定漫画中的 Marvel 角色。
- **输入**:
  - `comicId` (数字): 漫画的唯一 ID。
  - 可选过滤器:
    - `name` (可选字符串): 按全名过滤角色。
    - `nameStartsWith` (可选字符串): 按名称以指定字符串开头的角色进行过滤。
    - `modifiedSince` (可选字符串): ISO 8601 日期字符串，用于过滤自该日期以来修改过的角色。
    - `series`, `events`, `stories` (可选字符串): 逗号分隔的相关实体 ID 列表，用于过滤。
    - `orderBy` (可选字符串): 用于对结果进行排序的字段，例如 `name` 或 `-modified`。
    - `limit` (可选数字): 返回的最大结果数量 (1–100)。
    - `offset` (可选数字): 为分页跳过的结果数量。
- **返回**: JSON 响应，包含在指定漫画中出现的角色。详情请参见 `src/schemas.ts` 中的 `CharacterDataWrapperSchema`。

## 🛠️ 设置

注册一个 [Marvel Developer API](https://developer.marvel.com/documentation/getting_started) 账户并获取您的公钥和私钥。

如果您想直接在 MCP 主机上运行 MCP 服务器，请跳转到 [与 GitHub Copilot 一起使用](#use-with-github-copilot) 或 [与 Claude Desktop 一起使用](#use-with-claude-desktop) 部分。

### 本地运行服务器

1. 需要一个 Azure 存储模拟器。有两种选择：

    - 在 Docker 容器中启动 Azurite：

```bash
      docker run -p 10000:10000 -p 10001:10001 -p 10002:10002 \
          mcr.microsoft.com/azure-storage/azurite
```

    - 您可以使用 [Azurite VS Code 扩展](https://marketplace.visualstudio.com/items/?itemName=Azurite.azurite)。安装扩展后，通过 VS Code 命令面板运行 `Azurite: Start`。

1. 克隆此仓库：

```bash
    git clone https://github.com/DanWahlin/marvel-mcp-azure-functions
```

1. 将 `.env.template` 重命名为 `.env`。

1. 在 `.env` 文件中添加您的 Marvel API 公钥和私钥。

```bash
    MARVEL_PUBLIC_KEY=YOUR_PUBLIC_KEY
    MARVEL_PRIVATE_KEY=YOUR_PRIVATE_KEY
    MARVEL_API_BASE=https://gateway.marvel.com/v1/public
```

1. 安装所需的依赖项并构建项目。

```bash
    npm install
    npm run build
```

1. 本地启动 Azure Functions 主机：

```bash
    npm start
```

1. （可选）要使用 MCP Inspector 测试 MCP 服务器，请运行以下命令：

```bash
    # 启动 MCP Inspector
    npx @modelcontextprotocol/inspector node build/index.js
```

    访问控制台中显示的 MCP Inspector URL：
    - 将 `Transport Type` 更改为 `SSE`。
    - 输入 `http://0.0.0.0:7071/runtime/webhooks/mcp/sse` 作为 URL。
    - 选择 `Connect` 按钮。
    - 选择 `List Tools`。
    - 选择一个工具进行测试。

## 配置 MCP 主机

### 与 Claude Desktop 一起使用

将以下内容添加到您的 `claude_desktop_config.json` 中：

```json
{
  "mcpServers": {
    "marvel-mcp": {
      "type": "sse",
      "url": "http://0.0.0.0:7071/runtime/webhooks/mcp/sse"
    }
  }
}
```

### 在 VS Code 中与 GitHub Copilot 一起使用

> **注意**：如果您已经通过 Claude Desktop 启用了 MCP 服务器，请在您的 VS Code 设置中添加 `chat.mcp.discovery.enabled: true`，它将发现现有的 MCP 服务器列表。

如果您想将 MCP 服务器与特定仓库关联，请创建一个 `.vscode/mcp.json` 文件，并包含以下内容：

```json
   {
     "inputs": [],
     "servers": {
        "marvel-mcp": {
          "type": "sse",
          "url": "http://0.0.0.0:7071/runtime/webhooks/mcp/sse"
        }
     }
   }
```

如果您希望将 MCP 服务器与所有仓库关联，请将以下内容添加到您的 VS Code 用户设置 JSON 中：

```json
  "mcp": {
    "servers": {
      "marvel-mcp": {
        "type": "sse",
        "url": "http://0.0.0.0:7071/runtime/webhooks/mcp/sse"
      }
    }
  }
```

## 部署到 Azure 以实现远程 MCP

运行此 [azd](https://aka.ms/azd) 命令来配置函数应用（包括任何必需的 Azure 资源）并部署您的代码：

```shell
azd up
```

您可以选择在示例中使用 VNet。为此，在执行 `azd up` 之前进行如下操作：

```bash
azd env set VNET_ENABLED true
```

此外，可以使用 [API Management]() 来提高对您的 MCP 服务器的安全性和策略管理，同时可以使用 [App Service 内置认证](https://learn.microsoft.com/en-us/azure/app-service/overview-authentication-authorization) 来设置您喜欢的 OAuth 提供商，包括 Entra。

### 在 GitHub Copilot 中使用工具

1. 现在 MCP 服务器已经可以被发现了，打开 GitHub Copilot 并选择 `Agent` 模式（而不是 `Ask` 或 `Edit`）。
2. 在 Copilot 聊天文本字段中选择“刷新”按钮以刷新服务器列表。
3. 选择“🛠️”按钮查看所有可能的工具，包括来自该仓库的工具。
4. 在聊天中提出一个问题，自然地调用其中一个工具，例如：

```
    列出 10 个漫威角色。包括图片。

    金刚狼出现在哪些漫画中？

    哪些角色出现在复仇者联盟漫画中？

    Hedge Knight II: Sworn Sword (2007) 漫画中有哪些角色？
```

    > **注意**：如果您看到“抱歉，响应被负责任的人工智能服务过滤了。”请尝试再次运行或重新措辞提示。

**官方网站：** [https://github.com/DanWahlin/marvel-mcp-azure-functions](https://github.com/DanWahlin/marvel-mcp-azure-functions)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`art and culture`, `cloud platforms`, `chinese`

## MCP 配置

- 传输方式：`http`
- 启动命令：``
- 参数：无

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/danwahlin-marvel-azure-functions.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
