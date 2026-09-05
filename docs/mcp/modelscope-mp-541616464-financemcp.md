---
title: "FinanceMCP"
description: "Professional financial data server based on the MCP protocol, integrating the Tushare API, providing real-time financial data and technical indicator analysis for AI assistants like Claude. - - - - -…"
---

# FinanceMCP

Professional financial data server based on the MCP protocol, integrating the Tushare API, providing real-time financial data and technical indicator analysis for AI assistants like Claude. - - - - -…

![English](/mcp-assets/b9a78e1b7835d058a9d2196a4c747d2d.svg)

# FinanceMCP - Professional Financial Data MCP Server

[Smithery](https://smithery.ai/server/@guangxiangdebizi/finance-mcp)

**A professional financial data server based on the MCP protocol, integrating the Tushare API to provide real-time financial data and technical indicator analysis for AI assistants like Claude.**

## Table of Contents

- [Free Public Cloud Service](#free-public-cloud-service)
- [Core Features](#core-features)
- [Tool Overview](#tool-overview)
- [Technical Highlights](#technical-highlights)
- [Quick Start](#quick-start)
- [Example Queries](#example-queries)
- [Local Deployment](#local-deployment)
- [Latest Updates](#latest-updates)
- [License](#license)

## Free Public Cloud Service

**Get started instantly, no deployment needed!**
We offer multiple free public cloud service options:

### Web Online Experience
**The simplest way to get started!**

Visit our online experience website: **[http://106.14.205.176:3090/](http://106.14.205.176:3090/)**

- **Zero-configuration experience** - No setup required, just open the web page and start using
- **Integrated with large models** - Converse directly with AI assistants for financial analysis
- **Intelligent interaction** - Ask questions in natural language and get real-time financial data
- **Multi-device support** - Accessible from computers, smartphones, and tablets

> **Service Notice**: This is a personal small server. Please use it reasonably and do not abuse or attack it.

### Claude Desktop Configuration

#### Latest version (v4.0.0) - Use your own API key
**Recommended for production use; configure your own Tushare token:**

```json
{
  "mcpServers": {
    "finance-mcp": {
      "disabled": false,
      "timeout": 600,
      "type": "streamableHttp",
      "url": "http://106.14.205.176:8080/mcp",
      "headers": {
        "X-Tushare-Token": "your-tushare-token"
      }
    }
  }
}
```

**How to get your Tushare token:**
1. Register an account at [tushare.pro](https://tushare.pro/register)
2. Get the API token from your personal center
3. Replace `your-tushare-token` with your actual token

#### Legacy free service (rate-limited)
You can also use our shared service without an API key (may be rate-limited):

```json
{
  "mcpServers": {
    "finance-data-server": {
      "disabled": false,
      "timeout": 600,
      "type": "sse",
      "url": "http://106.14.205.176:3101/sse"
    }
  }
}
```

**Service advantages:**
- **Latest version (v4.0.0)** - Use your own API key for unlimited access
- **24/7 availability** - The server runs continuously
- **Full functionality** - All 14 tools and technical indicators
- **Real-time data** - Connected to professional Tushare data
- **No rate limits** - Enjoy unlimited API calls with your own token
- **Production ready** - Stable streamable HTTP protocol

> **Tutorial video**: [Complete FinanceMCP Usage Guide](https://www.bilibili.com/video/BV1qeNnzEEQi/)

## Core Features

### Smart Technical Indicator System
- **Smart data prefetching** - Automatically computes the required historical data, eliminating NaN values
- **Mandatory parameters** - Requires explicit parameter specification (e.g. `macd(12,26,9)`) for precision
- **Modular architecture** - Parameter parsing, data computation, and indicator engine are fully decoupled
- **5 core indicators** - MACD, RSI, KDJ, BOLL, MA

### Comprehensive Market Coverage
- **10 major markets** - A-shares, US stocks, HK stocks, forex, futures, funds, bonds, options
- **Real-time news** - Smart search across 7+ mainstream financial media outlets
- **Macro data** - 11 economic indicators (GDP, CPI, PPI, PMI, etc.)
- **Company analysis** - Financial statements, management information, shareholder structure

## Tool Overview

| Tool | Description | Highlights |
|---------|---------|---------|
| **current_timestamp** | Current timestamp | UTC+8 timezone, multiple output formats |
| **finance_news** | Financial news search | Baidu News crawler; input: `query` (space-separated keywords, OR filtering) |
| **stock_data** | Stock + technical indicators | 10 markets + 5 technical indicators, smart prefetching |
| **index_data** | Index data | Historical data of major market indices |
| **csi_index_constituents** | CSI index constituents & weights summary | CSI (China Securities Index) only; index range quotes + weights and range returns of all constituents |
| **macro_econ** | Macroeconomic data | 11 indicators: GDP/CPI/PPI/PMI/Shibor, etc. |
| **company_performance** | A-share company financial analysis | Financial statements + management + fundamentals, 13 data types |
| **company_performance_hk** | HK-listed company financial analysis | HK income statement, balance sheet, cash flow statement |
| **company_performance_us** | US-listed company financial analysis | 4 major financial statements + composite financial indicator analysis |
| **fund_data** | Fund data | NAV/holdings/dividends, 85% performance optimization |
| **fund_manager_by_name** | Fund manager lookup | Personal background, managed fund list |
| **convertible_bond** | Convertible bond data | Basic info + issuance data + conversion terms |
| **block_trade** | Block trade data | Trade details + counterparty information |
| **money_flow** | Capital flow data | Main/large/medium/small order flow analysis |
| **margin_trade** | Margin trading data | 4 APIs: underlying stocks/summary/details/refinancing |
| **dragon_tiger_inst** | Dragon-Tiger list institution details | Per trading day (optional code), buy/sell amounts, ratios, net amounts, reasons table |
| **hot_news_7x24** | 24/7 hot news | Based on the latest Tushare batch (up to 1500 items), 80% similarity dedup, items separated by `---` |

## Technical Highlights

### Smart Technical Indicator Engine
```
User request -> Parameter parsing -> Data requirement calculation -> Extended historical data fetch -> Indicator calculation -> Result returned
```

**Supported indicators:**
- **MACD** `macd(12,26,9)` - Trend analysis
- **RSI** `rsi(14)` - Overbought/oversold detection
- **KDJ** `kdj(9,3,3)` - Stochastic indicator
- **BOLL** `boll(20,2)` - Bollinger Bands
- **MA** `ma(5/10/20/60)` - Moving averages

### Core Technical Advantages
1. **Smart prefetching** - Automatically computes and fetches the extra historical data indicators need
2. **Mandatory parameters** - Avoids calculation differences caused by default parameters
3. **High performance** - Fund data query performance improved by 85% (5.2s to 0.8s)
4. **Data integration** - Seamlessly integrates 43+ Tushare API endpoints

## Quick Start

### 1. Use the public cloud service (recommended)
Copy the JSON configuration above into the Claude Desktop config file, restart Claude, and you are ready to go!

### 2. Config file location
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

### 3. Start using it
Once configured, just ask questions directly in Claude!

## Example Queries

### Stock Technical Analysis

```
"Analyze the technical situation of Moutai (600519.SH) and calculate MACD(12,26,9), RSI(14), KDJ(9,3,3)"
"Check CATL's (300750.SZ) Bollinger Bands BOLL(20,2) and four moving averages MA(5,10,20,60)"
"Apple (AAPL) stock price trend over the past month and MACD indicator analysis"
```

### Composite Analysis

```
"Comprehensive analysis of BYD: financial situation, technical indicators, capital flow, latest news"
"Compare market performance across A-shares, US stocks and HK stocks, including major indices and technical indicators"
"Evaluate CATL's investment value: fundamentals + technicals + capital flow"
"Get the CSI constituent summary for CSI 300 (000300.SH) from 2024-01-01 to 2024-06-30"
```

### News and Macro

```
"Search for the latest policies and market developments in the new-energy vehicle sector"
"Analyze the current macroeconomic situation: GDP, CPI, PPI, PMI data"
"Impact of Fed rate hikes on China's stock market, related news and data"
```

### Funds and Bonds

```
"Query the latest NAV and holdings structure of the CSI 300 ETF"
"Analyze Zhang Kun's fund performance"
"Convertible bond market overview and investment opportunities"
```

### HK Stock Analysis

```
"Get Tencent's (00700.HK) 2024 income statement, including key financial ratios"
"Analyze Alibaba's (09988.HK) balance sheet and financial structure"
"Compare China Construction Bank's (00939.HK) cash flow performance across multiple periods"
```

### Dragon-Tiger List

```
"Query the Dragon-Tiger list institution details for 20240525"
"Query the Dragon-Tiger list institution details for 20240525 (focusing on 000001.SZ)"
```

### US Stock Analysis

```
"Analyze NVIDIA's (NVDA) 2024 financial performance, including income statement and cash flow"
"Get Apple's (AAPL) balance sheet, focusing on cash reserves and debt structure"
"Compare Tesla's (TSLA) financial indicators across multiple periods and analyze profitability trends"
"View Microsoft's (MSFT) composite financial indicators, including ROE, ROA, gross margin, etc."
```

## Local Deployment (Streamable HTTP)

### Complete local deployment guide

If you need to deploy locally, follow these steps:

### Environment requirements
- **Node.js >= 18** - Download from [nodejs.org](https://nodejs.org/)
- **Tushare API token** - Get it from [tushare.pro](https://tushare.pro)

### Getting a Tushare API token

1. **Register an account** - Visit [tushare.pro](https://tushare.pro/register) to register
2. **Get the token** - Get the API token from your personal center
3. **Points info** - Some premium data requires points

**Student perk** - Apply for 2000 free points:
- Follow Tushare's official Xiaohongshu account and interact
- Join the student QQ group: **290541801**
- Complete your personal information (school email/student ID)
- Submit application materials to the administrator

### Installation steps

#### Method 1: Install via npm (recommended)
```bash
# Global install
npm install -g finance-mcp

# Or local install
npm install finance-mcp
```

After installation, you can use it directly:
```bash
# If installed globally
finance-mcp

# If installed locally
npx finance-mcp
```

#### Method 2: Install via Smithery
```bash
npx -y @smithery/cli install @guangxiangdebizi/finance-mcp --client claude
```

#### Method 3: Manual installation
```bash
# 1. Clone the repository
git clone https://github.com/guangxiangdebizi/FinanceMCP.git
cd FinanceMCP

# 2. Install dependencies
npm install

# 3. Configure the API key
echo "TUSHARE_TOKEN=your_token_here" > .env
# Or edit src/config.ts directly

# 4. Build the project
npm run build
```

### Starting the service

**Streamable HTTP mode (recommended)**
```bash
npm run build
node build/httpServer.js
# or
npm run start:http
```

**SSE mode**
```bash
npm run build
npm run start:sse
```

Once the service is running:
- MCP endpoint: `http://localhost:3000/mcp`
- Health check: `http://localhost:3000/health`

### Claude Configuration

Config file location:
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

#### Latest config: Streamable HTTP mode (Tushare token passed via Header)
```json
{
  "mcpServers": {
    "finance-data-server": {
      "type": "streamableHttp",
      "url": "http://localhost:3000/mcp",
      "timeout": 600,
      "headers": {
        "X-Tushare-Token": "your_tushare_token"
        // You may also use either of the following:
        // "Authorization": "Bearer your_tushare_token"
        // "X-Api-Key": "your_tushare_token"
      }
    }
  }
}
```

#### Token header rules
- Read from `X-Tushare-Token` first;
- If not provided, try `Authorization: Bearer `;
- Then fall back to `X-Api-Key`;
- If not provided in the header, fall back to the server environment variable `TUSHARE_TOKEN` (optional).

### Verifying the installation
After configuration, restart Claude Desktop and ask: "Get the current time". If time information is returned, the installation succeeded.

## Latest Updates

### Version 4.0.0 - Enhanced Web Experience

**Latest major release**: We released v4.0.0 with a comprehensive web experience and enhanced features!

### What's new in v4.0.0

- **Web online experience** - Brand new web interface `http://106.14.205.176:3090/`
- **Integrated with large models** - Converse directly with AI assistants for financial analysis
- **Intelligent interaction** - Ask questions in natural language and get real-time financial data
- **Multi-device support** - Accessible from computers, smartphones, and tablets
- **Zero-configuration experience** - No setup required, just open the web page and start using

- **NPM package** - Now published to the npm registry under the name `finance-mcp`
- **Public cloud service** - Production-ready deployment at `http://106.14.205.176:8080/mcp`
- **Custom API key** - Use your own Tushare token for unlimited access
- **Streamable HTTP** - Enhanced protocol support for better performance
- **Production stability** - Improved error handling and session management
- **No rate limits** - Unlimited API calls with your own token
- **Easy installation** - Simple npm install and configuration

**Migration guide**: Update your Claude config to use the new streamable HTTP endpoint and your own API key for the best experience.

### US Stock Financial Analysis Module (NEW!)

**Latest addition**: We added complete US stock financial analysis functionality!

### New features

- **company_performance_us** - A professional US stock financial analysis tool
- **Income statement analysis** - Revenue, gross margin, net income, EPS analysis
- **Balance sheet analysis** - Assets, liabilities, equity structure, and financial ratios
- **Cash flow statement analysis** - Operating, investing, financing cash flows and free cash flow
- **Composite financial indicators** - ROE, ROA, profitability, growth, solvency, etc.
- **Smart data processing** - Multi-period comparison, trend calculation, key indicator extraction
- **Bilingual support** - Smart recognition of Chinese and English financial line items

**Supported companies**: Covers major US-listed and China ADR stocks, including NVIDIA (NVDA), Apple (AAPL), Tesla (TSLA), Microsoft (MSFT), etc.

**API integration**: Based on the [Tushare US stock financial data API](https://tushare.pro/document/2?doc_id=394), fully integrating 4 data endpoints.

### HK Stock Financial Analysis Module

**Added**: We added comprehensive HK stock financial analysis functionality!

### Features

- **company_performance_hk** - A dedicated HK stock financial analysis tool
- **Income statement analysis** - Revenue, profit margin, EPS, comprehensive income analysis
- **Balance sheet analysis** - Assets, liabilities, equity structure, and key financial ratios
- **Cash flow statement analysis** - Operating, investing, financing activities and free cash flow calculation
- **Smart data processing** - Automatic financial ratio calculation and multi-period comparison
- **Enhanced user experience** - Structured tables, smart categorization, trend analysis

**Supported companies**: All companies listed on the Hong Kong Stock Exchange, including Tencent (00700.HK), Alibaba (09988.HK), China Construction Bank (00939.HK), etc.

**API integration**: Based on the [Tushare HK stock financial data API](https://tushare.pro/document/2?doc_id=389), with fully optimized data formats.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/guangxiangdebizi/FinanceMCP/blob/HEAD/LICENSE) file for details.

---

**Author**: Chen Xingyu
**Email**: guangxiangdebizi@gmail.com
**GitHub**: [guangxiangdebizi](https://github.com/guangxiangdebizi)

If this project helps you, please give us a Star!

**Official site: ** [https://github.com/guangxiangdebizi/FinanceMCP](https://github.com/guangxiangdebizi/FinanceMCP)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `finance`
- Tags: `finance`, `tushare`, `mcp`, `llm`, `fintech`, `stock`, `index`

## MCP Configuration

- Transport: `http`
- Command: ``
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/modelscope-mp-541616464-financemcp.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
