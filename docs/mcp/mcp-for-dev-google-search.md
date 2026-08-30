---
title: "MCP 谷歌搜索工具"
description: "一个使用Google自定义搜索API和网页内容提取功能提供网络搜索功能的模型上下文协议服务器。"
---

# MCP 谷歌搜索工具

一个使用Google自定义搜索API和网页内容提取功能提供网络搜索功能的模型上下文协议服务器。

# MCP 服务器用于 Google 搜索

一个使用 Google 自定义搜索 API 和网页内容提取功能提供网络搜索能力的模型上下文协议服务器。

## 工具

### 搜索
使用 Google 自定义搜索 API 执行网络搜索：
- 搜索整个网络或特定站点
- 控制结果数量（1-10）
- 获取带有标题、链接和摘要的结构化结果

### 网页阅读器
从任何网页中提取内容：
- 获取并解析网页内容
- 提取页面标题和主体文本
- 通过移除脚本和样式来清理内容
- 返回带有标题、文本和 URL 的结构化数据

## 安装

### 获取 Google API 密钥和搜索引擎 ID

1. 创建 Google Cloud 项目：
   - 前往 [Google Cloud 控制台](https://console.cloud.google.com/)
   - 创建新项目或选择现有项目
   - 为您的项目启用计费

2. 启用自定义搜索 API：
   - 前往 [API 库](https://console.cloud.google.com/apis/library)
   - 搜索“Custom Search API”
   - 单击“启用”

3. 获取 API 密钥：
   - 前往 [凭据](https://console.cloud.google.com/apis/credentials)
   - 单击“创建凭据”>“API 密钥”
   - 复制您的 API 密钥
   - （可选）将 API 密钥限制为仅自定义搜索 API 使用

4. 创建自定义搜索引擎：
   - 前往 [可编程搜索引擎](https://programmablesearchengine.google.com/create/new)
   - 输入您想要搜索的站点（对于一般的网络搜索，使用 www.google.com）
   - 单击“创建”
   - 在下一页上，单击“自定义”
   - 在设置中启用“搜索整个网络”
   - 复制您的搜索引擎 ID (cx)

### 客户端配置

要与 Claude Desktop 一起使用，请使用您的 Google API 凭证添加服务器配置：

在 MacOS 上：`~/Library/Application Support/Claude/claude_desktop_config.json`
在 Windows 上：`%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "google-search": {
      "command": "npx",
      "args": ["-y", "@mcp-for-dev/mcp-google-search"],
      "env": {
        "GOOGLE_API_KEY": "your-api-key-here",
        "GOOGLE_SEARCH_ENGINE_ID": "your-search-engine-id-here"
      }
    }
  }
}
```

**官方网站：** [https://github.com/mcp-for-dev/mcp-google-search](https://github.com/mcp-for-dev/mcp-google-search)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`browser`
- 标签：`search`, `browser automation`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @mcp-for-dev/mcp-google-search`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/mcp-for-dev-google-search.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
