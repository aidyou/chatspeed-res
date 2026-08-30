---
title: "yfinance股票数据服务"
description: "一个简单的用于雅虎财经的MCP服务器，使用yfinance。该服务器提供了一组工具来获取股票数据、新闻和其他财务信息。"
---

# yfinance股票数据服务

一个简单的用于雅虎财经的MCP服务器，使用yfinance。该服务器提供了一组工具来获取股票数据、新闻和其他财务信息。

# Yahoo Finance MCP 服务器

使用 yfinance 的一个简单的 Yahoo Finance MCP 服务器。该服务器提供了一组工具来获取股票数据、新闻和其他金融信息。

## 工具

- **get_ticker_info**

  - 获取包括公司信息、财务状况、交易指标和治理数据在内的股票数据。
  - 输入：
    - `symbol` (字符串): 股票代码。

- **get_ticker_news**

  - 获取与特定股票代码相关的最近新闻文章，包括标题、内容和来源详情。
  - 输入：
    - `symbol` (字符串): 股票代码。

- **search**

  - 从 Yahoo Finance 获取并组织搜索结果，包括股票报价和新闻文章。
  - 输入：
    - `query` (字符串): 搜索查询（股票代码或公司名称）。
    - `search_type` (字符串): 要检索的搜索结果类型（选项："all", "quotes", "news"）。

- **get_top**

  - 获取某一行业内的顶级实体（ETF、共同基金、公司、成长型公司或表现优异的公司）。
  - 输入：
    - `sector` (字符串): 要获取的行业。
    - `top_type` (字符串): 要检索的顶级公司类型（选项："top_etfs", "top_mutual_funds", "top_companies", "top_growth_companies", "top_performing_companies"）。
    - `top_n` (数字, 可选): 要检索的顶级实体数量（默认为10）。

## 使用方法

您可以通过 uv（Python 包管理器）或 Docker 来使用此 MCP 服务器。

### 通过 uv

1. [安装 uv](https://docs.astral.sh/uv/getting-started/installation/)
2. 将以下配置添加到您的 MCP 服务器配置文件中：

```json
{
  "mcpServers": {
    "yfmcp": {
      "command": "uvx",
      "args": ["yfmcp"]
    }
  }
}
```

### 通过 Docker

将以下配置添加到您的 MCP 服务器配置文件中：

```json
{
  "mcpServers": {
    "yfmcp": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "narumi/yfinance-mcp"]
    }
  }
}
```

**官方网站：** [https://github.com/narumiruna/yfinance-mcp](https://github.com/narumiruna/yfinance-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`finance`
- 标签：`finance`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`yfmcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/narumiruna-yfinance.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
