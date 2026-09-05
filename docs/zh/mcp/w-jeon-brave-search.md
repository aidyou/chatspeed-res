---
title: "无畏搜索"
description: "勇敢搜索"
---

# 无畏搜索

勇敢搜索

# Brave Search MCP 服务器

一个集成了 Brave Search API 的 MCP 服务器实现，提供网页和本地搜索功能。

## 功能

- **网页搜索**：通用查询、新闻、文章，支持分页和新鲜度控制
- **本地搜索**：查找企业、餐馆和服务，并提供详细信息
- **灵活的过滤**：控制结果类型、安全级别和内容新鲜度
- **智能回退**：当没有找到本地结果时自动回退到网页搜索

## 工具

- **brave_web_search**
  - 执行带有分页和过滤的网页搜索
  - 输入：
    - `query` (字符串)：搜索词
    - `count` (数字, 可选)：每页结果数（最大20）
    - `offset` (数字, 可选)：分页偏移量（最大9）

- **brave_local_search**
  - 搜索本地企业和服务
  - 输入：
    - `query` (字符串)：本地搜索词
    - `count` (数字, 可选)：结果数量（最大20）
  - 如果没有找到本地结果，将自动回退到网页搜索

## 配置

### 获取 API 密钥
1. 注册 [Brave Search API 账户](https://brave.com/search/api/)
2. 选择一个计划（免费套餐每月提供2,000次查询）
3. 从开发者仪表板生成您的 API 密钥 [从开发者仪表板](https://api.search.brave.com/app/keys)

### 与 Claude Desktop 一起使用
在 `claude_desktop_config.json` 中添加以下内容：

### Docker

```json
{
  "mcpServers": {
    "brave-search": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e",
        "BRAVE_API_KEY",
        "mcp/brave-search"
      ],
      "env": {
        "BRAVE_API_KEY": "YOUR_API_KEY_HERE"
      }
    }
  }
}
```

### NPX

```json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-brave-search"
      ],
      "env": {
        "BRAVE_API_KEY": "YOUR_API_KEY_HERE"
      }
    }
  }
}
```

## 构建

Docker 构建：

```bash
docker build -t mcp/brave-search:latest -f src/brave-search/Dockerfile .
```

## 许可证

此 MCP 服务器根据 MIT 许可证授权。这意味着您可以自由使用、修改和分发该软件，但须遵守 MIT 许可证的条款和条件。更多详情，请参阅项目仓库中的 LICENSE 文件。

**官方网站：** [https://github.com/w-jeon/mcp-brave-search](https://github.com/w-jeon/mcp-brave-search)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`search`, `location services`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @modelcontextprotocol/server-brave-search`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/w-jeon-brave-search.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
