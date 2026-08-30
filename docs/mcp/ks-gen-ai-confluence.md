---
title: "Confluence MCP Server工具"
description: "启用通过CQL搜索和页面内容提取从Confluence查询和检索内容，使Claude能够无缝访问存储在Confluence工作区中的信息。"
---

# Confluence MCP Server工具

启用通过CQL搜索和页面内容提取从Confluence查询和检索内容，使Claude能够无缝访问存储在Confluence工作区中的信息。

# Confluence 通信服务器 MCP 服务器

与 Confluence 交互

这是一个基于 TypeScript 的 MCP 服务器，提供了与 Confluence 交互的工具。它通过提供以下功能来展示核心的 MCP 概念：

- 执行 CQL 查询以搜索页面的工具
- 获取 Confluence 页面内容的工具

## 功能

## Confluence 工具

### `execute_cql_search`
- **目的**：运行 CQL 查询以搜索 Confluence 页面。
- **参数**：`cql`，`limit`（默认值：10）。

### `get_page_content`
- **目的**：获取 Confluence 页面的内容。
- **参数**：`pageId`。

## 开发

安装依赖：
```bash
npm install
```

构建服务器：
```bash
npm run build
```

对于带有自动重建的开发：
```bash
npm run watch
```

## 安装

要与 Claude Desktop 一起使用，请添加服务器配置：

在 MacOS 上：`~/Library/Application Support/Claude/claude_desktop_config.json`
在 Windows 上：`%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "Confluence communication server": {
      "command": "node",
      "args": [
        "/PATH_TO_THE_PROJECT/build/index.js"
      ],
      "env": {
        "CONFLUENCE_URL": "https://XXXXXXXX.atlassian.net/wiki",
        "CONFLUENCE_API_MAIL": "Your email",
        "CONFLUENCE_API_KEY": "KEY_FROM: https://id.atlassian.com/manage-profile/security/api-tokens"
      }
    }
  }
}
```

### 调试

由于 MCP 服务器通过 stdio 进行通信，调试可能会比较困难。我们建议使用 [MCP Inspector](https://github.com/modelcontextprotocol/inspector)，它作为包脚本可用：

```bash
npm run inspector
```

Inspector 将提供一个 URL，以便您可以在浏览器中访问调试工具。

**官方网站：** [https://github.com/KS-GEN-AI/confluence-mcp-server](https://github.com/KS-GEN-AI/confluence-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`memory`, `communication`
- 标签：`communication`, `knowledge and memory`, `search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`/PATH_TO_THE_PROJECT/build/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/ks-gen-ai-confluence.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
