---
title: "AlphaVentage 股票价格"
description: "Alpha Vantage MCP 服务器 English 中文 这是一个 Model Context Protocol (MCP) 服务器，提供了对 Alpha Vantage 金融数据 API 的访问。该服务器使 AI 助手能够获取实时和历史金融市场数据，包括股票价格、外汇汇率、加密货币数据以及各种技术指标。 ✨ 特性 - 实时股票数据：获取当前股票价格、报价和市场信息 - 历史数据：访问历史…"
---

# AlphaVentage 股票价格

Alpha Vantage MCP 服务器 English 中文 这是一个 Model Context Protocol (MCP) 服务器，提供了对 Alpha Vantage 金融数据 API 的访问。该服务器使 AI 助手能够获取实时和历史金融市场数据，包括股票价格、外汇汇率、加密货币数据以及各种技术指标。 ✨ 特性 - 实时股票数据：获取当前股票价格、报价和市场信息 - 历史数据：访问历史…

# Alpha Vantage MCP 服务器

[English](https://github.com/jeasionr-ui/alpha-ventage-mcp/blob/HEAD/README.md) | [中文](https://github.com/jeasionr-ui/alpha-ventage-mcp/blob/HEAD/README.zh.md)

这是一个 Model Context Protocol (MCP) 服务器，提供了对 Alpha Vantage 金融数据 API 的访问。该服务器使 AI 助手能够获取实时和历史金融市场数据，包括股票价格、外汇汇率、加密货币数据以及各种技术指标。

## ✨ 特性

- **实时股票数据**：获取当前股票价格、报价和市场信息
- **历史数据**：访问历史股票价格和交易量
- **技术指标**：计算各种技术分析指标（SMA、EMA、RSI、MACD 等）
- **外汇数据**：实时和历史外汇汇率
- **加密货币**：数字货币价格和市场数据
- **公司信息**：基本面数据、收益和公司概况
- **市场新闻**：最新财经新闻和市场情绪

## 🚀 快速开始

### 前提条件

- 安装 Node.js 16+
- Alpha Vantage API 密钥（在 [Alpha Vantage](https://www.alphavantage.co/support/#api-key) 免费获取一个）

### 安装

无需安装！使用 npx 自动下载并运行包。

对于本地开发：
```bash
git clone https://github.com/jeasionr-ui/alpha-ventage-mcp.git
cd alpha-ventage-mcp
npm install
```
## ⚙️ 配置

在您的 MCP 设置文件中配置服务器：

```json

{

  "mcpServers": {

    "alpha-vantage": {

      "command": "npx",

      "args": ["alpha-ventage-mcp"],

      "env": {

        "ALPHA_VANTAGE_API_KEY": "your-api-key-here"

      },

      "disabled": false,

      "alwaysAllow": []

    }

  }

}

```
## 🔑 API 密钥

获取您的免费 Alpha Vantage API 密钥：
1. 访问 [Alpha Vantage](https://www.alphavantage.co/support/#api-key)
2. 注册一个免费账户
3. 复制您的 API 密钥
4. 将其添加到环境变量或 MCP 配置中

## 📊 可用工具

### 股票数据
- `get_stock_quote` - 获取实时股票报价
- `get_stock_intraday` - 获取日内股票数据
- `get_stock_daily` - 获取每日股票价格
- `get_stock_weekly` - 获取每周股票价格
- `get_stock_monthly` - 获取每月股票价格

### 技术指标
- `get_sma` - 简单移动平均线
- `get_ema` - 指数移动平均线
- `get_rsi` - 相对强弱指数
- `get_macd` - 移动平均收敛发散
- `get_bollinger_bands` - 布林带
- `get_stochastic` - 随机振荡器

### 外汇与加密货币
- `get_forex_rate` - 实时外汇汇率
- `get_crypto_rating` - 加密货币评级
- `get_crypto_intraday` - 日内加密货币数据

### 公司信息
- `get_company_overview` - 公司基本面数据
- `get_earnings` - 季度和年度收益
- `search_symbol` - 搜索股票代码

### 市场新闻
- `get_news_sentiment` - 市场新闻和情绪分析

## 🛠️ 开发

### 构建
```bash
npm run build
```
### 测试
```bash
# Test with environment variable
ALPHA_VANTAGE_API_KEY=your_key_here node build/index.js
```
## 📝 示例用法

配置完成后，您可以向您的 AI 助手提问，例如：

- "AAPL 当前的股票价格是多少？"
- "显示特斯拉股票的 RSI"
- "获取微软最新的收益报告"
- "EUR/USD 汇率是多少？"
- "显示今天比特币的价格趋势"

## 🤝 贡献

欢迎贡献！请随时提交 Pull Request。

## 📄 许可证

MIT 许可证 - 详情见 LICENSE 文件。

## 🔗 链接

- [Alpha Vantage API 文档](https://www.alphavantage.co/documentation/)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [MCP 规范](https://spec.modelcontextprotocol.io/)

**官方网站：** [https://github.com/jeasionr-ui/alpha-ventage-mcp](https://github.com/jeasionr-ui/alpha-ventage-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`finance`
- 标签：`finance`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`alpha-ventage-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/daybed8207-alphaventage.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
