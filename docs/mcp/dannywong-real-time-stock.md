---
title: "real-time-stock-mcp"
description: "Real-time Stock Analysis MCP Service --- This is an MCP server for a real-time stock data service. It fetches financial data from EastMoney and XueQiu, and exposes these data as tools to MCP-supported…"
---

# real-time-stock-mcp

Real-time Stock Analysis MCP Service --- This is an MCP server for a real-time stock data service. It fetches financial data from EastMoney and XueQiu, and exposes these data as tools to MCP-supported…

# Real-time Stock Analysis MCP Service

---

This is an MCP server for a real-time stock data service. It fetches financial data from EastMoney and XueQiu, and exposes these data as tools to MCP-supported Agents.

> **Code Repository:** https://github.com/DannyWongIsAvailable/real-time-stock-mcp-service.git

- Free and no-login required to get data

## Features

- 📊 Stock Search
- 📈 K-line Data Query (Supports B-shares, H-shares, market indices, and intraday charts)
- 📉 Technical Indicator Analysis (MA, MACD, BOLL, RSI, etc.)
- 💰 Fundamental Data Analysis (Business composition, business scope, etc.)
- 📊 Financial Analysis (Financial ratios, performance overview, etc.)
- 💰 Valuation Analysis Data (P/E ratio, P/B ratio, etc.)
- 📈 Market Trend Tracking (Sector trends, peer comparison, capital flow, etc.)
- 🤖 Intelligent Comments and Ratings

Total of 34 MCP tools

## Usage

You can use this service in the following three ways:

### 1. One-click Deployment with Free Cloud Resources on ModelScope Community

You can experience this service online in the ModelScope MCP Playground, which also supports remote client connections (via streamable HTTP or SSE protocol).

https://modelscope.cn/mcp/servers/DannyWong/real-time-stock-mcp

### 2. Local Stdio Mode (Running via Package Installation)

Add the following configuration:

json
{
  "mcpServers": {
    "stock-mcp": {
      "command": "uvx",
      "args": [
        "real-time-stock-mcp-service"
      ],
      "env": {
        "EASTMONEY_COOKIE": "Copy the EastMoney Cookie from your browser",
        "XUEQIU_COOKIE": "Copy the XueQiu Cookie from your browser"
      }
    }
  }
}

### 3. Local Stdio Mode (Running from Source Code)

json
{
  "mcpServers": {
    "stock-mcp": {
      "command": "path/to/python.exe",
      "args": ["-m", "stock_mcp"],
      "cwd": "path/to/real-time-stock-mcp-service",
      "env": {
        "EASTMONEY_COOKIE": "Copy the EastMoney Cookie from your browser",
        "XUEQIU_COOKIE": "Copy the XueQiu Cookie from your browser"
      }
    }
  }
}

> **Note:** Replace the paths with your actual project paths.

### Environment Variables for Cookies

Some interfaces (such as EastMoney datacenter, XueQiu real-time quotes/K-lines) require browser cookies to function properly. Set these in the `env` field of the MCP configuration:

| Environment Variable | Description |
|----------------------|-------------|
| `EASTMONEY_COOKIE`   | EastMoney Cookie, used for datacenter, push2, etc. |
| `XUEQIU_COOKIE`      | XueQiu Cookie, used for real-time quotes, K-lines, etc. |
| `LOG_LEVEL`          | Optional, log level, default `INFO` |

**How to Get Cookies:**

1. Log in to [eastmoney.com](https://www.eastmoney.com) or [xueqiu.com](https://xueqiu.com) in your browser.
2. Open Developer Tools (F12) → Network → Any request → Request Headers.
3. Copy the full content of the `Cookie` field and paste it into the corresponding environment variable in the MCP configuration.

Cookies will expire, and if you encounter a 403 error or data anomalies, simply copy and update the configuration, then restart the MCP service.

> **Security Tip:** Do not hardcode the cookies in your source code or commit them to Git. Store them only in the local MCP configuration.

#### Video Tutorials:
- [What is MCP? How to Use It? How to Develop Your Own MCP Service? A Video to Get You Started!](https://www.bilibili.com/video/BV13R5EzbE6E/?spm_id_from=333.337.search-card.all.click&vd_source=08fc400fe0cfc7eaa723687b764b29f3)
- [Cherry Studio MCP Getting Started Tutorial: From Configuration to Usage](https://www.bilibili.com/video/BV1bkdAYTEYp/?spm_id_from=333.337.search-card.all.click&vd_source=08fc400fe0cfc7eaa723687b764b29f3)

## Core Design

This project uses the **Dependency Injection** design pattern:

1. The `crawler` module fetches data.
2. `data_source_interface.py` defines the abstract data source interface.
3. `stock_data_source.py` provides the concrete implementation.
4. Each tool module obtains the data source instance through dependency injection.

This design allows for:
- ✅ Easy expansion of new features
- ✅ Seamless switching between different data sources
- ✅ Facilitates unit testing
- ✅ Decoupled code, making it highly maintainable

## Tool Modules

The project includes 34 MCP tool modules, each providing specific functionalities:

- `search.py` - Stock search and trading day information
- `real_time_data.py` - Real-time stock quote data
- `kline_data.py` - K-line data and technical indicators
- `fundamental.py` - Fundamental data (business composition, business scope, etc.)- `valuation.py` - Valuation analysis data (P/E ratio, P/B ratio, etc.)
- `financial_analysis.py` - Financial analysis data (financial ratios, performance overview, etc.)
- `market.py` - Market data (sector performance, capital flow, etc.)
- `smart_review.py` - Intelligent comments and ratings

## Development Guide

For more details, please refer to the [Development Guide](https://github.com/DannyWongIsAvailable/real-time-stock-mcp-service/blob/HEAD/DEVELOPMENT.md)

## Important Notes

⚠️ **Important Reminder**:
1. The data provided by this service is for reference only and does not constitute investment advice.
2. Use is permitted for personal learning, research, and non-commercial purposes only. Commercial use and abuse are strictly prohibited!
3. Please comply with the data usage agreement and relevant laws and regulations.

## Open Source License

[MIT License](https://github.com/DannyWongIsAvailable/real-time-stock-mcp-service/blob/HEAD/LICENSE)

## Contributions

We welcome Issues and Pull Requests!

## Contact

If you have any questions, please submit an Issue or contact the project developers.
A star would be greatly appreciated!

**Official site: ** [https://github.com/DannyWongIsAvailable/real-time-stock-mcp-service.git](https://github.com/DannyWongIsAvailable/real-time-stock-mcp-service.git)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `finance`
- Tags: `finance`, `股票`, `金融分析`, `炒股`, `捞数`, `赚钱`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `real-time-stock-mcp-service==2.1.0`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/dannywong-real-time-stock.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
