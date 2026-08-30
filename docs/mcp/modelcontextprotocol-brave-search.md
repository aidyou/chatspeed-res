---
title: "Brave搜索"
description: "一个集成了Brave Search API的MCP服务器实现，提供网页和本地搜索功能。"
---

# Brave搜索

一个集成了Brave Search API的MCP服务器实现，提供网页和本地搜索功能。

# Brave Search MCP Server

一个集成了Brave Search API的MCP服务器实现，提供网页和本地搜索功能。

## 特性

- **网页搜索**：通用查询、新闻、文章，支持分页和新鲜度控制
- **本地搜索**：查找带有详细信息的企业、餐馆和服务
- **灵活过滤**：控制结果类型、安全级别和内容新鲜度
- **智能回退**：当没有找到本地结果时自动回退到网页搜索

## 工具

- **brave_web_search**
  - 执行带分页和过滤的网页搜索
  - 输入：
    - `query` (字符串)：搜索词
    - `count` (数字, 可选)：每页结果数（最大20）
    - `offset` (数字, 可选)：分页偏移量（最大9）

- **brave_local_search**
  - 搜索本地企业和服务
  - 输入：
    - `query` (字符串)：本地搜索词
    - `count` (数字, 可选)：结果数量（最大20）
  - 如果未找到本地结果，则自动回退到网页搜索

## 配置

### 获取API密钥
1. 注册[Brave Search API账号](https://brave.com/search/api/)
2. 选择计划（免费层每月提供2,000次查询）
3. 从[开发者仪表板](https://api.search.brave.com/app/keys)生成您的API密钥

### 与Claude Desktop一起使用
将以下内容添加到您的`claude_desktop_config.json`中：

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

Docker构建命令：

```bash
docker build -t mcp/brave-search:latest -f src/brave-search/Dockerfile .
```

## 许可证

此MCP服务器根据MIT许可证发布。这意味着您可以自由地使用、修改和分发该软件，但需遵守MIT许可证的条款和条件。更多详情，请参阅项目仓库中的LICENSE文件。

**官方网站：** [https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`
- 标签：`search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @modelcontextprotocol/server-brave-search`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/modelcontextprotocol-brave-search.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
