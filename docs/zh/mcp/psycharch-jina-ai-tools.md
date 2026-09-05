---
title: "Jina-AI-MCP-Tools"
description: "一个与Jina AI搜索基础API集成的模型上下文协议（MCP）服务器，提供网页阅读和搜索功能。"
---

# Jina-AI-MCP-Tools

一个与Jina AI搜索基础API集成的模型上下文协议（MCP）服务器，提供网页阅读和搜索功能。

# Jina AI MCP 工具

一个与[Jina AI 搜索基础 API](https://docs.jina.ai/)集成的模型上下文协议 (MCP) 服务器。

## 功能

此 MCP 服务器提供对以下 Jina AI API 的访问：

- **Web Reader** - 使用 r.jina.ai 从网页中提取内容
- **Web Search** - 使用 s.jina.ai 或 svip.jina.ai（通过 `--search-endpoint` 配置）进行网络搜索

## 前提条件

1. **Jina AI API 密钥**（可选）- 从 [https://jina.ai/?sui=apikey](https://jina.ai/?sui=apikey) 获取免费 API 密钥以增强功能
2. **Node.js** - 版本 16 或更高

## MCP 服务器

### 使用 stdio 传输（默认）

对于由其他进程（例如 Claude Desktop、VS Code、Cursor）启动的本地集成：

```json

{

  "mcpServers": {

    "jina-mcp-tools": {

      "command": "npx",

      "args": [

        "jina-mcp-tools",

        "--transport", "stdio",

        "--tokens-per-page", "15000",

        "--search-endpoint", "standard"

      ],

      "env": {

        "JINA_API_KEY": "your_jina_api_key_here_optional"

      }

    }

  }

}

```
### 使用 HTTP 传输

对于可通过 HTTP 访问的远程服务器部署：

**启动服务器：**
```bash
# With API key
JINA_API_KEY=your_api_key npx jina-mcp-tools --transport http --port 3000

# Without API key (reader tool only)
npx jina-mcp-tools --transport http --port 3000
```
**从 MCP 客户端连接：**
- MCP Inspector: `npx @modelcontextprotocol/inspector` → `http://localhost:3000/mcp`
- Claude Code: `claude mcp add --transport http jina-tools http://localhost:3000/mcp`
- VS Code: `code --add-mcp '{"name":"jina-tools","type":"http","url":"http://localhost:3000/mcp"}'`

**CLI 选项：**
- `--transport` - 传输类型：`stdio` 或 `http`（默认：stdio）
- `--port` - HTTP 服务器端口（默认：3000，仅适用于 HTTP 传输）
- `--tokens-per-page` - 分页每页的令牌数（默认：15000）
- `--search-endpoint` - 要使用的搜索端点：`standard`（s.jina.ai）或 `vip`（svip.jina.ai）（默认：standard）

## 可用工具

### jina_reader

提取并读取网页内容。

**参数：**
- `url` - 要读取的 URL（必需）
- `page` - 分页内容的页码（默认：1）
- `customTimeout` - 超时覆盖（秒）（可选）

**特性：**
- 大文档自动分页
- LRU 缓存（50 个 URL）用于即时后续页面请求
- GitHub 文件 URL 自动转换为原始内容 URL

### jina_search / jina_search_vip

搜索网络。返回部分内容；使用 `jina_reader` 获取完整内容。需要 API 密钥。

根据 `--search-endpoint` 注册的工具：
- `jina_search` → `standard`（s.jina.ai，默认）
- `jina_search_vip` → `vip`（svip.jina.ai）

**参数：**
- `query` - 搜索查询（必需）
- `count` - 结果数量（默认：5）
- `siteFilter` - 限制到特定域名（例如，“github.com”）

## 许可证

MIT

## 链接

- GitHub: [https://github.com/PsychArch/jina-mcp-tools](https://github.com/PsychArch/jina-mcp-tools)
- 问题: [https://github.com/PsychArch/jina-mcp-tools/issues](https://github.com/PsychArch/jina-mcp-tools/issues)

**官方网站：** [https://github.com/PsychArch/jina-mcp-tools](https://github.com/PsychArch/jina-mcp-tools)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`
- 标签：`search`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`jina-mcp-tools --transport stdio --tokens-per-page 15000 --search-endpoint standard`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/psycharch-jina-ai-tools.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
