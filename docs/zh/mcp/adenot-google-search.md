---
title: "Google 搜索"
description: "通过使用Google自定义搜索API提供网络搜索功能，使用户能够通过Model Context Protocol服务器进行搜索。"
---

# Google 搜索

通过使用Google自定义搜索API提供网络搜索功能，使用户能够通过Model Context Protocol服务器进行搜索。

# mcp-google-server 一个用于 Google 自定义搜索和网页阅读的 MCP 服务器
[Smithery](https://smithery.ai/server/@adenot/mcp-google-search)

这是一个使用 Google 自定义搜索 API 和网页内容提取功能提供网络搜索能力的模型上下文协议（MCP）服务器。

## 设置

### 获取 Google API 密钥和搜索引擎 ID

1. 创建 Google Cloud 项目：
   - 前往 [Google Cloud 控制台](https://console.cloud.google.com/)
   - 创建新项目或选择现有项目
   - 为您的项目启用计费

2. 启用自定义搜索 API：
   - 前往 [API 库](https://console.cloud.google.com/apis/library)
   - 搜索“Custom Search API”
   - 点击“启用”

3. 获取 API 密钥：
   - 前往 [凭证](https://console.cloud.google.com/apis/credentials)
   - 点击“创建凭据”>“API 密钥”
   - 复制您的 API 密钥
   - （可选）将 API 密钥限制为仅适用于自定义搜索 API

4. 创建自定义搜索引擎：
   - 前往 [可编程搜索引擎](https://programmablesearchengine.google.com/create/new)
   - 输入您想要搜索的站点（对于通用网络搜索，请使用 www.google.com）
   - 点击“创建”
   - 在下一页，点击“自定义”
   - 在设置中，启用“搜索整个网络”
   - 复制您的搜索引擎 ID (cx)

## 开发

安装依赖项：
```bash
npm install
```

构建服务器：
```bash
npm run build
```

开发时自动重建：
```bash
npm run watch
```

## 功能

### 搜索工具
使用 Google 自定义搜索 API 执行网络搜索：
- 搜索整个网络或特定站点
- 控制结果数量（1-10）
- 获取带有标题、链接和摘要的结构化结果

### 网页阅读器工具
从任何网页中提取内容：
- 获取并解析网页内容
- 提取页面标题和主要文本
- 通过移除脚本和样式来清理内容
- 返回包含标题、文本和 URL 的结构化数据

## 安装

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@adenot/mcp-google-search) 自动为 Claude Desktop 安装 Google 自定义搜索服务器：

```bash
npx -y @smithery/cli install @adenot/mcp-google-search --client claude
```

要与 Claude Desktop 一起使用，请使用您的 Google API 凭证添加服务器配置：

在 MacOS 上：`~/Library/Application Support/Claude/claude_desktop_config.json`
在 Windows 上：`%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "google-search": {
      "command": "npx",
      "args": [
        "-y",
        "@adenot/mcp-google-search"
      ],
      "env": {
        "GOOGLE_API_KEY": "your-api-key-here",
        "GOOGLE_SEARCH_ENGINE_ID": "your-search-engine-id-here"
      }
    }
  }
}
```

## 使用方法

### 搜索工具
```json
{
  "name": "search",
  "arguments": {
    "query": "your search query",
    "num": 5  // optional, default is 5, max is 10
  }
}
```

### 网页阅读器工具
```json
{
  "name": "read_webpage",
  "arguments": {
    "url": "https://example.com"
  }
}
```

来自网页阅读器的示例响应：
```json
{
  "title": "Example Domain",
  "text": "Extracted and cleaned webpage content...",
  "url": "https://example.com"
}
```

### 调试

由于 MCP 服务器通过 stdio 进行通信，调试可能具有挑战性。我们建议使用 [MCP Inspector](https://github.com/modelcontextprotocol/inspector)，它作为包脚本可用：

```bash
npm run inspector
```

Inspector 将提供一个 URL，以便您在浏览器中访问调试工具。

**官方网站：** [https://github.com/adenot/mcp-google-search](https://github.com/adenot/mcp-google-search)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`
- 标签：`search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @adenot/mcp-google-search`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/adenot-google-search.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
