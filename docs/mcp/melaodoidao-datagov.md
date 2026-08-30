---
title: "政府数据MCP服务器"
description: "一个MCP服务器，提供来自Data.gov的政府数据集访问，使用户能够搜索数据包、查看数据集详情、列出组和标签，并通过URL访问资源。"
---

# 政府数据MCP服务器

一个MCP服务器，提供来自Data.gov的政府数据集访问，使用户能够搜索数据包、查看数据集详情、列出组和标签，并通过URL访问资源。

# Data.gov MCP 服务器

一个用于访问 Data.gov 数据的MCP服务器，提供与政府数据集交互的工具和资源。

  

## 安装

1. **全局安装包：**

```bash
    npm install -g @melaodoidao/datagov-mcp-server
```

2. **配置 MCP 服务器：**

   - 在您的 `cline_mcp_settings.json` 文件中添加以下条目（通常位于 macOS 上的 `~/Library/Application Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings/`）：

```json
      {
        "mcpServers": {
          "datagov": {
            "command": "datagov-mcp-server",
            "args": [],
            "env": {}
          }
        }
      }
```
    - 如果您使用的是 Claude 桌面应用程序，请将条目添加到 `~/Library/Application Support/Claude/claude_desktop_config.json` 中。

## 使用方法

此服务器提供了以下工具：

*   `package_search`: 在 Data.gov 上搜索数据包（数据集）。
*   `package_show`: 获取特定数据包（数据集）的详细信息。
*   `group_list`: 列出 Data.gov 上的组。
*   `tag_list`: 列出 Data.gov 上的标签。

它还提供了以下资源模板：

*   `datagov://resource/{url}`: 通过 URL 访问 Data.gov 资源。

您可以使用 Cline 并指定服务器名称 (`datagov-mcp-server`) 和工具/资源名称来使用这些工具和资源。

## 贡献

欢迎贡献！请随时提交问题或拉取请求。

## 许可证

MIT 许可证

**官方网站：** [https://github.com/melaodoidao/datagov-mcp-server](https://github.com/melaodoidao/datagov-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`research and data`, `search`, `databases`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`datagov-mcp-server`
- 参数：无

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/melaodoidao-datagov.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
