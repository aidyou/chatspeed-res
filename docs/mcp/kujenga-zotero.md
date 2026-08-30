---
title: "Zotero-MCP 智搜"
description: "该服务器允许用户通过模型上下文协议与他们的Zotero图书馆进行交互，提供用于搜索项目、检索元数据和使用自然语言查询访问全文的工具。"
---

# Zotero-MCP 智搜

该服务器允许用户通过模型上下文协议与他们的Zotero图书馆进行交互，提供用于搜索项目、检索元数据和使用自然语言查询访问全文的工具。

# Zotero 的 Model Context Protocol 服务器

这个项目是一个用 Python 实现的服务器，它为 [Zotero](https://www.zotero.org/) 实现了 [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction)，让你能够在 AI 助手中访问你的 Zotero 库。它的目的是实现一组小但非常有用的与 Zotero 的交互，以便与 [MCP 客户端](https://modelcontextprotocol.io/clients)一起使用。

## 特性

此 MCP 服务器提供以下工具：

- `zotero_search_items`：使用文本查询在您的 Zotero 库中搜索条目
- `zotero_item_metadata`：获取特定 Zotero 条目的详细元数据信息
- `zotero_item_fulltext`：获取特定 Zotero 条目的全文（即 PDF 内容）

这些可以通过任何 MCP 客户端或通过 [MCP 检查器](https://modelcontextprotocol.io/docs/tools/inspector)发现和访问。

每个工具返回包含来自您的 Zotero 条目的相关信息的格式化文本，像 Claude 这样的 AI 助手可以依次使用它们，先搜索条目然后检索其元数据或文本内容。

## 安装

要与 Claude Desktop 一起使用，请将以下内容添加到 `mcpServers` 配置中：

```json
{
  "mcpServers": {
    "zotero": {
      "command": "uvx",
      "args": ["zotero-mcp"],
      "env": {
        "ZOTERO_LOCAL": "true"
      }
    }
  }
}
```

`ZOTERO_LOCAL` 设置指向 [本地 Zotero API](https://groups.google.com/g/zotero-dev/c/ElvHhIFAXrY/m/fA7SKKwsAgAJ)，并要求 Zotero 7（或测试版，见下文说明）在同一台机器上运行。

若要使用 Zotero Web API，您需要创建一个 API 密钥，并在您的 Zotero 账户设置中找到您的库 ID（通常是您的用户 ID）: [https://www.zotero.org/settings/keys](https://www.zotero.org/settings/keys)

以下环境变量提供了配置选项：

- `ZOTERO_LOCAL=true`: 使用本地 Zotero API（默认值：false，见下文说明）
- `ZOTERO_API_KEY`: 您的 Zotero API 密钥（对于本地 API 不是必需的）
- `ZOTERO_LIBRARY_ID`: 您的 Zotero 库 ID（用户库时为您的用户 ID，对于本地 API 不是必需的）
- `ZOTERO_LIBRARY_TYPE`: 库的类型（用户或组，默认值：用户）

> [!IMPORTANT]
> 若要本地访问全文 API，需要即将发布的 Zotero 版本。在此期间，您需要安装 [Zotero 测试版构建](https://www.zotero.org/support/beta_builds)才能使该功能正常工作（截至 2025-03-07）。有关更多信息，请参阅 https://github.com/zotero/zotero/pull/5004。

## 开发

1. 克隆此仓库
1. 通过运行 `uv sync` 使用 [uv](https://docs.astral.sh/uv/) 安装依赖项
1. 在项目根目录下创建一个 `.env` 文件，并填充上述环境变量

启动 [MCP 检查器](https://modelcontextprotocol.io/docs/tools/inspector)进行本地开发：

```bash
npx @modelcontextprotocol/inspector uv run zotero-mcp
```

### 运行测试

要运行测试套件：

```bash
uv run pytest
```

## 相关文档

- https://modelcontextprotocol.io/tutorials/building-mcp-with-llms
- https://github.com/modelcontextprotocol/python-sdk
- https://pyzotero.readthedocs.io/en/latest/
- https://www.zotero.org/support/dev/web_api/v3/start

**官方网站：** [https://github.com/kujenga/zotero-mcp](https://github.com/kujenga/zotero-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`, `data`
- 标签：`research and data`, `note taking`, `search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`zotero-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/kujenga-zotero.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
