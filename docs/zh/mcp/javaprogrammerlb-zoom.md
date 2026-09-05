---
title: "Zoom约会助手服务器"
description: "一个由人工智能辅助的服务器，可在Zoom会议中实现约会功能，设置时需要提供Zoom API凭证（客户端ID、客户端密钥、账户ID）。"
---

# Zoom约会助手服务器

一个由人工智能辅助的服务器，可在Zoom会议中实现约会功能，设置时需要提供Zoom API凭证（客户端ID、客户端密钥、账户ID）。

# Zoom MCP Server

[![NPM Version](/mcp-assets/8cbae245c0357e4b060d80948c0bef6f.svg)](https://www.npmjs.com/package/@yitianyigexiangfa/zoom-mcp-server) ![MIT licensed](/mcp-assets/5816f652aa1f0cc4eedb21a2f733e09e.svg) [Smithery](https://smithery.ai/server/@JavaProgrammerLB/zoom-mcp-server) ![Zoom MCP Server](/mcp-assets/c1486b4e2d8cfd67ed0257afeefda188.svg "MCP Server")

现在你可以借助AI的帮助安排Zoom会议

## 使用方法

### 1. 列出会议

- `list my meetings`
- `list my upcoming meetings`

### 2. 创建会议

- `Schedule a meeting at today 3 pm with a introduce mcp topic`

### 3. 删除会议

- `delete the latest meeting`
- `delete the 86226580854 meeting`

### 4. 获取会议详情

- `Retrieve the latest meeting's details`
- `Retrieve 86226580854 meeting's details`

## 两步开始使用 zoom-mcp-server

- 获取Zoom客户端ID、Zoom客户端密钥和账户ID
- 配置MCP服务器

### 1. 获取Zoom客户端ID、Zoom客户端密钥和账户ID

1. 访问 [Zoom Marketplace](https://marketplace.zoom.us/)
1. 构建应用并选择 **Server to Server OAuth App**
1. 添加权限 > 会议 > 选择所有会议权限
1. 激活你的应用
   然后你可以在应用凭证页面获取**账户ID**、**客户端ID**、**客户端密钥**

### 2. 配置MCP服务器

```json
{
  "mcpServers": {
    "zoom-mcp-server": {
      "command": "npx",
      "args": ["-y", "@yitianyigexiangfa/zoom-mcp-server@latest"],
      "env": {
        "ZOOM_ACCOUNT_ID": "${ZOOM_ACCOUNT_ID}",
        "ZOOM_CLIENT_ID": "${ZOOM_CLIENT_ID}",
        "ZOOM_CLIENT_SECRET": "${ZOOM_CLIENT_SECRET}"
      }
    }
  }
}
```

**官方网站：** [https://github.com/JavaProgrammerLB/zoom-mcp-server](https://github.com/JavaProgrammerLB/zoom-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`communication`
- 标签：`communication`, `social media`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @yitianyigexiangfa/zoom-mcp-server@latest`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/javaprogrammerlb-zoom.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
