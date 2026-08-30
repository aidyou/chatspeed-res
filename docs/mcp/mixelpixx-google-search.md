---
title: "Google Search MCP 服务器（模型上下文协议）"
description: "一个提供谷歌搜索功能和网页内容分析工具的MCP（模型上下文协议）服务器。该服务器使人工智能模型能够以编程方式执行谷歌搜索并分析网页内容。"
---

# Google Search MCP 服务器（模型上下文协议）

一个提供谷歌搜索功能和网页内容分析工具的MCP（模型上下文协议）服务器。该服务器使人工智能模型能够以编程方式执行谷歌搜索并分析网页内容。

# 专为 Cline + VS Code 设计！

# Google 搜索 MCP 服务器

一个提供 Google 搜索功能和网页内容分析工具的 MCP（模型上下文协议）服务器。该服务器使 AI 模型能够以编程方式执行 Google 搜索并分析网页内容。

## 功能

- 高级 Google 搜索，支持过滤选项（日期、语言、国家/地区、安全搜索）
- 详细的网页内容提取和分析
- 批量网页分析，用于比较多个来源
- 支持环境变量来设置 API 凭证
- 全面的错误处理和用户反馈
- 符合 MCP 的接口，可与 AI 助手无缝集成

## 前提条件

- Node.js (v16 或更高版本)
- Python (v3.8 或更高版本)
- Google Cloud Platform 账户
- 自定义搜索引擎 ID
- Google API 密钥

## 安装

1. 克隆仓库：
```bash
   git clone https://github.com/your-username/google-search-mcp.git
   cd google-search-mcp
```

2. 安装 Node.js 依赖项：
```bash
   npm install
```

3. 安装 Python 依赖项：
```bash
   pip install flask google-api-python-client flask-cors beautifulsoup4 trafilatura markdownify
```

4. 构建 TypeScript 代码：
```bash
   npm run build
```

5. 创建一个帮助脚本来启动 Python 服务器（Windows 示例）：
```bash
   # 创建 start-python-servers.cmd
   @echo off
   echo Starting Python servers for Google Search MCP...
   
   REM 启动 Python 搜索服务器
   start "Google Search API" cmd /k "python google_search.py"
   
   REM 启动 Python 链接查看器
   start "Link Viewer" cmd /k "python link_view.py"
   
   echo Python servers started. You can close this window.
```

## 配置

### API 凭证

您可以使用以下两种方式之一提供 Google API 凭证：

1. **环境变量**（推荐）：
   - 在您的环境中设置 `GOOGLE_API_KEY` 和 `GOOGLE_SEARCH_ENGINE_ID`
   - 服务器将自动使用这些值

2. **配置文件**：
   - 在根目录下创建一个 `api-keys.json` 文件：
```json
   {
       "api_key": "your-google-api-key",
       "search_engine_id": "your-custom-search-engine-id"
   }
```

### MCP 设置配置

将服务器配置添加到您的 MCP 设置文件中：

#### 对于 Cline（VS Code 扩展）
文件位置：`%APPDATA%\Code\User\globalStorage\saoudrizwan.claude-dev\settings\cline_mcp_settings.json`

```json
{
  "mcpServers": {
    "google-search": {
      "command": "C:\\Program Files\\nodejs\\node.exe",
      "args": ["C:\\path\\to\\google-search-mcp\\dist\\google-search.js"],
      "cwd": "C:\\path\\to\\google-search-mcp",
      "env": {
        "GOOGLE_API_KEY": "your-google-api-key",
        "GOOGLE_SEARCH_ENGINE_ID": "your-custom-search-engine-id"
      },
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

#### 对于 Claude 桌面应用程序
文件位置：`%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "google-search": {
      "command": "C:\\Program Files\\nodejs\\node.exe",
      "args": ["C:\\path\\to\\google-search-mcp\\dist\\google-search.js"],
      "cwd": "C:\\path\\to\\google-search-mcp",
      "env": {
        "GOOGLE_API_KEY": "your-google-api-key",
        "GOOGLE_SEARCH_ENGINE_ID": "your-custom-search-engine-id"
      },
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

## 运行服务器

### 方法 1：单独启动 Python 服务器（推荐）

1. 首先，使用帮助脚本启动 Python 服务器：
```bash
   start-python-servers.cmd
```

2. 配置 MCP 设置以仅运行 Node.js 服务器：
```json
   {
     "command": "C:\\Program Files\\nodejs\\node.exe",
     "args": ["C:\\path\\to\\google-search-mcp\\dist\\google-search.js"]
   }
```

### 方法 2：一体化脚本

使用单个命令启动 TypeScript 和 Python 服务器：
```bash
npm run start:all
```

## 可用工具

### 1. google_search
使用 Google 搜索引擎搜索并返回相关网页结果。此工具可以找到特定主题的网页、文章和信息。

```typescript
{
  "name": "google_search",
  "arguments": {
    "query": "your search query",
    "num_results": 5, // optional, default: 5, max: 10
    "date_restrict": "w1", // optional, restrict to past day (d1), week (w1), month (m1), year (y1)
    "language": "en", // optional, ISO 639-1 language code (en, es, fr, de, ja, etc.)
    "country": "us", // optional, ISO 3166-1 alpha-2 country code (us, uk, ca, au, etc.)
    "safe_search": "medium" // optional, safe search level: "off", "medium", "high"
  }
}
```

### 2. extract_webpage_content
从网页中提取并分析内容，将其转换为可读文本。此工具在提取主要内容时会移除广告、导航元素和其他杂项。

```typescript
{
  "name": "extract_webpage_content",
  "arguments": {
    "url": "https://example.com"
  }
}
```

### 3. extract_multiple_webpages
在单个请求中从多个网页中提取并分析内容。非常适合比较不同来源的信息或收集某个主题的全面信息。

```typescript
{
  "name": "extract_multiple_webpages",
  "arguments": {
    "urls": [
      "https://example1.com",
      "https://example2.com"
    ]
  }
}
```

## 使用示例

以下是一些如何使用 Google Search MCP 工具的示例：

### 基本搜索
```
Search for information about artificial intelligence
```

### 高级搜索与过滤器
```
Search for recent news about climate change from the past week in Spanish
```

### 内容提取
```
Extract the content from https://example.com/article
```

### 多内容比较
```
Compare information from these websites:
- https://site1.com/topic
- https://site2.com/topic
- https://site3.com/topic
```

## 获取 Google API 凭据

1. 前往 [Google Cloud Console](https://console.cloud.google.com/)
2. 创建新项目或选择现有项目
3. 启用自定义搜索 API
4. 创建 API 凭据（API 密钥）
5. 访问 [Custom Search Engine](https://programmablesearchengine.google.com/about/) 页面
6. 创建一个新的搜索引擎并获取您的搜索引擎 ID
7. 将这些凭据添加到您的 `api-keys.json` 文件中

## 错误处理

服务器提供详细的错误消息，包括：
- 缺少或无效的 API 凭据
- 搜索请求失败
- 无效的网页 URL
- 网络连接问题

## 架构

服务器由两个主要组件组成：
1. TypeScript MCP 服务器：处理 MCP 协议通信并提供工具接口
2. Python Flask 服务器：管理 Google API 交互和网页内容分析

## 许可证

MIT

**官方网站：** [https://github.com/mixelpixx/Google-Search-MCP-Server](https://github.com/mixelpixx/Google-Search-MCP-Server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`browser`
- 标签：`search`, `browser automation`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`/path/to/google-search-mcp-server/dist/google-search.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/mixelpixx-google-search.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
