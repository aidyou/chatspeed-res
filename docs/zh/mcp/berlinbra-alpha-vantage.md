---
title: "Alpha Vantage股票数据服务器"
description: "一个模型上下文协议（MCP）服务器，通过免费的Alpha Vantage API提供对金融市场数据的实时访问。该服务器实现了一个标准化的接口，用于检索股票报价和公司信息。"
---

# Alpha Vantage股票数据服务器

一个模型上下文协议（MCP）服务器，通过免费的Alpha Vantage API提供对金融市场数据的实时访问。该服务器实现了一个标准化的接口，用于检索股票报价和公司信息。

# Alpha Vantage MCP 服务器
[Smithery](https://smithery.ai/server/@berlinbra/alpha-vantage-mcp)

一个模型上下文协议 (MCP) 服务器，通过免费的 [Alpha Vantage API](https://www.alphavantage.co/documentation/) 提供实时访问金融市场数据的功能。此服务器实现了用于检索股票报价和公司信息的标准接口。

# 特性

- 实时股票报价，包括价格、成交量和变化数据
- 详细的公司信息，包括行业、板块和市值
- 实时加密货币汇率，包括买入/卖出价格
- 历史期权链数据，支持高级过滤和排序
- 内置错误处理和速率限制管理

## 安装

### 使用 Claude 桌面版

#### 通过 Docker 安装

- 克隆仓库并构建本地镜像以供您的 Claude 桌面客户端使用

```sh
cd alpha-vantage-mcp
docker build -t mcp/alpha-vantage .
```

- 修改 `claude_desktop_config.json` 使其与以下内容匹配，将 `REPLACE_API_KEY` 替换为您的实际密钥：

 > `claude_desktop_config.json` 路径
 >
 > - 在 MacOS 上: `~/Library/Application\ Support/Claude/claude_desktop_config.json`
 > - 在 Windows 上: `%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "alphavantage": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "-e",
        "ALPHA_VANTAGE_API_KEY",
        "mcp/alpha-vantage"
      ],
      "env": {
        "ALPHA_VANTAGE_API_KEY": "REPLACE_API_KEY"
      }
    }
  }
}
```

#### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@berlinbra/alpha-vantage-mcp) 自动安装 Alpha Vantage MCP 服务器到 Claude 桌面版:

```bash
npx -y @smithery/cli install @berlinbra/alpha-vantage-mcp --client claude
```

 
 开发/未发布服务器配置 
 

```json
{
 "mcpServers": {
  "alpha-vantage-mcp": {
   "args": [
    "--directory",
    "/Users/{INSERT_USER}/YOUR/PATH/TO/alpha-vantage-mcp",
    "run",
    "alpha-vantage-mcp"
   ],
   "command": "uv",
   "env": {
    "ALPHA_VANTAGE_API_KEY": "
"
   }
  }
 }
}
```

#### 安装包

```
uv install -e .
```

#### 运行

在通过 json 文件连接 Claude 客户端与 MCP 工具并安装包后，Claude 应该能看到服务器的 MCP 工具：

您可以自己运行服务器：
在 alpha-vantage-mcp 仓库中:
```
uv run src/alpha_vantage_mcp/server.py
```

使用 inspector
```
* npx @modelcontextprotocol/inspector uv --directory /Users/{INSERT_USER}/YOUR/PATH/TO/alpha-vantage-mcp run src/alpha_vantage_mcp/server.py `
```

## 可用工具

服务器实现了五个工具：
- `get-stock-quote`: 获取特定公司的最新股票报价
- `get-company-info`: 获取特定公司的股票相关信息
- `get-crypto-exchange-rate`: 获取当前加密货币汇率
- `get-time-series`: 获取股票的历史每日价格数据
- `get-historical-options`: 获取具有排序功能的历史期权链数据

### get-stock-quote

**输入模式:**
```json
{
    "symbol": {
        "type": "string",
        "description": "Stock symbol (e.g., AAPL, MSFT)"
    }
}
```

**示例响应:**
```
Stock quote for AAPL:

Price: $198.50
Change: $2.50 (+1.25%)
Volume: 58942301
High: $199.62
Low: $197.20
```

### get-company-info

获取给定符号的详细公司信息。

**输入模式:**
```json
{
    "symbol": {
        "type": "string",
        "description": "Stock symbol (e.g., AAPL, MSFT)"
    }
}
```

**示例响应:**
```
Company information for AAPL:

Name: Apple Inc
Sector: Technology
Industry: Consumer Electronics
Market Cap: $3000000000000
Description: Apple Inc. designs, manufactures, and markets smartphones...
Exchange: NASDAQ
Currency: USD
```

### get-crypto-exchange-rate

获取带有额外市场数据的实时加密货币汇率。

**输入模式:**
```json
{
    "crypto_symbol": {
        "type": "string",
        "description": "Cryptocurrency symbol (e.g., BTC, ETH)"
    },
    "market": {
        "type": "string",
        "description": "Market currency (e.g., USD, EUR)",
        "default": "USD"
    }
}
```

**示例响应:**
```
Cryptocurrency exchange rate for BTC/USD:

From: Bitcoin (BTC)
To: United States Dollar (USD)
Exchange Rate: 43521.45000
Last Updated: 2024-12-17 19:45:00 UTC
Bid Price: 43521.00000
Ask Price: 43522.00000
```

### get-time-series

获取每日时间序列（OHLCV）数据。

**输入模式:**
```json
{
    "symbol": {
        "type": "string",
        "description": "Stock symbol (e.g., AAPL, MSFT)"
    },
    "outputsize": {
        "type": "string",
        "description": "compact (latest 100 data points) or full (up to 20 years of data)",
        "default": "compact"
    }
}
```

**示例响应:**
```
Time Series Data for AAPL (Last Refreshed: 2024-12-17 16:00:00):

Date: 2024-12-16
Open: $195.09
High: $197.68
Low: $194.83
Close: $197.57
Volume: 55,751,011
```

### get-historical-options

检索具有高级排序和过滤功能的历史期权链数据。

**输入模式:**
```json
{
    "symbol": {
        "type": "string",
        "description": "Stock symbol (e.g., AAPL, MSFT)"
    },
    "date": {
        "type": "string",
        "description": "Optional: Trading date in YYYY-MM-DD format (defaults to previous trading day, must be after 2008-01-01)",
        "pattern": "^20[0-9]{2}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])$"
    },
    "limit": {
        "type": "integer",
        "description": "Optional: Number of contracts to return (default: 10, use -1 for all contracts)",
        "default": 10,
        "minimum": -1
    },
    "sort_by": {
        "type": "string",
        "description": "Optional: Field to sort by",
        "enum": ["strike", "expiration", "volume", "open_interest", "implied_volatility", "delta", "gamma", "theta", "vega", "rho", "last", "bid", "ask"],
        "default": "strike"
    },
    "sort_order": {
        "type": "string",
        "description": "Optional: Sort order",
        "enum": ["asc", "desc"],
        "default": "asc"
    }
}
```

**示例响应:**
```
Historical Options Data for AAPL (2024-02-20):

Contract 1:
Strike: $190.00
Expiration: 2024-03-15
Last: $8.45
Bid: $8.40
Ask: $8.50
Volume: 1245
Open Interest: 4567
Implied Volatility: 0.25
Greeks:
  Delta: 0.65
  Gamma: 0.04
  Theta: -0.15
  Vega: 0.30
  Rho: 0.25

Contract 2:
...
```

## 错误处理

服务器包括针对各种情况的全面错误处理：

- 超出速率限制
- 无效的 API 密钥
- 网络连接问题
- 超时处理
- 格式错误的响应

错误消息以清晰、易读的格式返回。

## 前提条件

- Python 3.12 或更高版本
- httpx
- mcp

## 贡献者

- [berlinbra](https://github.com/berlinbra)
- [zzulanas](https://github.com/zzulanas)

## 贡献指南

欢迎贡献！请随时提交 Pull Request。

## 许可证
此 MCP 服务器根据 MIT 许可证许可。
这意味着您可以自由使用、修改和分发该软件，但需遵守 MIT 许可证的条款和条件。有关更多详细信息，请参阅项目仓库中的 LICENSE 文件。

**官方网站：** [https://github.com/berlinbra/alpha-vantage-mcp](https://github.com/berlinbra/alpha-vantage-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`finance`
- 标签：`finance`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`--directory /Users/{INSERT_USER}/YOUR/PATH/TO/alpha-vantage-mcp run alpha-vantage-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/berlinbra-alpha-vantage.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
