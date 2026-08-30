---
title: "AkTools MCP 分析股票、虚拟货币"
description: "📈 AkTools MCP Server 基于 akshare 的 MCP (Model Context Protocol) 服务器，提供股票、虚拟货币的数据查询和分析功能。 功能 - 股票搜索: 根据公司名称、股票名称等关键词查找股票代码 - 股票信息: 获取股票的详细信息，包括价格、市值等 - 历史价格: 获取股票、虚拟货币历史价格数据，包含技术分析指标 - 相关新闻: 获取股票、虚拟货币相关的最新新闻资讯 - 财务指标: 支持A股和港股的财务报告关键指标查询 安装 方式1: uvx yaml { \"mcpSe"
---

# AkTools MCP 分析股票、虚拟货币

📈 AkTools MCP Server 基于 akshare 的 MCP (Model Context Protocol) 服务器，提供股票、虚拟货币的数据查询和分析功能。 功能 - 股票搜索: 根据公司名称、股票名称等关键词查找股票代码 - 股票信息: 获取股票的详细信息，包括价格、市值等 - 历史价格: 获取股票、虚拟货币历史价格数据，包含技术分析指标 - 相关新闻: 获取股票、虚拟货币相关的最新新闻资讯 - 财务指标: 支持A股和港股的财务报告关键指标查询 安装 方式1: uvx yaml { "mcpSe

# 📈 AkTools MCP Server

基于 akshare 的 MCP (Model Context Protocol) 服务器，提供股票、虚拟货币的数据查询和分析功能。

## 功能

- **股票搜索**: 根据公司名称、股票名称等关键词查找股票代码
- **股票信息**: 获取股票的详细信息，包括价格、市值等
- **历史价格**: 获取股票、虚拟货币历史价格数据，包含技术分析指标
- **相关新闻**: 获取股票、虚拟货币相关的最新新闻资讯
- **财务指标**: 支持A股和港股的财务报告关键指标查询

## 安装

### 方式1: uvx
```yaml
{
  "mcpServers": {
    "mcp-aktools": {
      "command": "uvx",
      "args": ["mcp-aktools"]
    }
  }
}
```

### 方式2: Docker
```bash
mkdir /opt/mcp-aktools
cd /opt/mcp-aktools
wget https://raw.githubusercontent.com/aahl/mcp-aktools/refs/heads/main/docker-compose.yml
docker-compose up -d
```
```yaml
{
  "mcpServers": {
    "mcp-aktools": {
      "url": "http://0.0.0.0:8808/mcp" # Streamable HTTP
    }
  }
}
```

### 一键安装
- 添加到 Cursor [![Install MCP Server](/mcp-assets/ec1e84b0a4f6576d1ecdf0b2651745c5.svg)](https://cursor.com/zh/install-mcp?name=aktools&config=eyJjb21tYW5kIjoidXZ4IiwiYXJncyI6WyJtY3AtYWt0b29scyJdfQ%3D%3D)
- 添加到 VS Code [
](https://insiders.vscode.dev/redirect?url=vscode:mcp/install%3F%7B%22name%22%3A%22aktools%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22mcp-aktools%22%5D%7D)
- 添加到 Claude code, 执行命令: `claude mcp add --transport stdio aktools -- uvx mcp-aktools`
- 添加到 OpenAI CodeX, 执行命令: `codex mcp add aktools -- uvx mcp-aktools`

**官方网站：** [https://github.com/aahl/mcp-aktools](https://github.com/aahl/mcp-aktools)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`finance`
- 标签：`finance`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`mcp-aktools`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/aalone-aktools.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
