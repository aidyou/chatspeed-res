---
title: "DuckDuckGo MCP 服务器"
description: "一种模型上下文协议（MCP）服务器，通过DuckDuckGo提供网页搜索功能，并具有内容获取和解析的附加功能。"
---

# DuckDuckGo MCP 服务器

一种模型上下文协议（MCP）服务器，通过DuckDuckGo提供网页搜索功能，并具有内容获取和解析的附加功能。

# DuckDuckGo Search MCP 服务器

[Smithery](https://smithery.ai/server/@nickclyde/duckduckgo-mcp-server)

这是一个通过 DuckDuckGo 提供网络搜索功能的模型上下文协议 (MCP) 服务器，还具有内容获取和解析的附加功能。

  

## 功能

- **网络搜索**：使用高级速率限制和结果格式化进行 DuckDuckGo 搜索
- **内容获取**：智能文本提取以检索和解析网页内容
- **速率限制**：内置针对搜索和内容获取的速率限制保护
- **错误处理**：全面的错误处理和日志记录
- **LLM 友好输出**：专门为大型语言模型消费而格式化的结果

## 安装

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@nickclyde/duckduckgo-mcp-server) 自动为 Claude Desktop 安装 DuckDuckGo 搜索服务器：

```bash
npx -y @smithery/cli install @nickclyde/duckduckgo-mcp-server --client claude
```

### 通过 `uv` 安装

直接从 PyPI 使用 `uv` 安装：

```bash
uv pip install duckduckgo-mcp-server
```

## 使用方法

### 与 Claude Desktop 一起运行

1. 下载 [Claude Desktop](https://claude.ai/download)
2. 创建或编辑您的 Claude Desktop 配置：
   - 在 macOS 上：`~/Library/Application Support/Claude/claude_desktop_config.json`
   - 在 Windows 上：`%APPDATA%\Claude\claude_desktop_config.json`

添加以下配置：

```json
{
    "mcpServers": {
        "ddg-search": {
            "command": "uvx",
            "args": ["duckduckgo-mcp-server"]
        }
    }
}
```

3. 重启 Claude Desktop

### 开发

对于本地开发，您可以使用 MCP CLI：

```bash
# Run with the MCP Inspector
mcp dev server.py

# Install locally for testing with Claude Desktop
mcp install server.py
```
## 可用工具

### 1. 搜索工具

```python
async def search(query: str, max_results: int = 10) -> str
```

在 DuckDuckGo 上执行网络搜索并返回格式化结果。

**参数：**
- `query`：搜索查询字符串
- `max_results`：要返回的最大结果数量（默认：10）

**返回：**
包含标题、URL 和摘要的格式化字符串。

### 2. 内容获取工具

```python
async def fetch_content(url: str) -> str
```

从网页中获取并解析内容。

**参数：**
- `url`：要从中获取内容的网页 URL

**返回：**
来自网页的清理和格式化文本内容。

## 功能详细说明

### 速率限制

- 搜索：每分钟限 30 次请求
- 内容获取：每分钟限 20 次请求
- 自动队列管理和等待时间

### 结果处理

- 移除广告和不相关的内容
- 清理 DuckDuckGo 重定向 URL
- 格式化结果以便于 LLM 使用
- 适当截断长内容

### 错误处理

- 全面的错误捕获和报告
- 通过 MCP 上下文进行详细的日志记录
- 在达到速率限制或超时时优雅降级

## 贡献

欢迎提交问题和拉取请求！一些可能改进的地方包括：

- 额外的搜索参数（地区、语言等）
- 增强的内容解析选项
- 频繁访问内容的缓存层
- 更多的速率限制策略

## 许可证

此项目根据 MIT 许可证授权。

**官方网站：** [https://github.com/nickclyde/duckduckgo-mcp-server](https://github.com/nickclyde/duckduckgo-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`browser`
- 标签：`browser automation`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`duckduckgo-mcp-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/nickclyde-duckduckgo.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
