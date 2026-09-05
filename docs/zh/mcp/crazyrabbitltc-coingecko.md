---
title: "CoinGecko金融数据接口"
description: "启用与CoinGecko Pro API的交互，通过MCP和OpenAI功能调用访问加密货币数据，包括价格历史和市场指标。"
---

# CoinGecko金融数据接口

启用与CoinGecko Pro API的交互，通过MCP和OpenAI功能调用访问加密货币数据，包括价格历史和市场指标。

# CoinGecko 服务器

一个用于与 CoinGecko Pro API 交互的模型上下文协议（MCP）服务器和 OpenAI 函数调用服务。

## 功能

- 支持的加密货币分页列表
- 按名称或符号查找币 ID
- 历史价格、市值和交易量数据
- OHLC（开盘价、最高价、最低价、收盘价）K线数据
- 具有刷新功能的本地币缓存

## 安装

```bash
npm install coingecko-server
```

## 环境设置

在你的项目根目录下创建一个 `.env` 文件：

```env
COINGECKO_API_KEY=your_api_key_here
```

## 与 Claude Desktop 一起使用

Claude Desktop 提供了对 MCP 特性的全面支持。要使用此服务器：

1. 安装 [Claude Desktop](https://claude.ai/download)

2. 添加到你的 Claude Desktop 配置中：
   - 在 macOS 上：`~/Library/Application Support/Claude/claude_desktop_config.json`
   - 在 Windows 上：`%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "coingecko": {
      "command": "node",
      "args": ["/path/to/coingecko-server/build/index.js"],
      "env": {
        "COINGECKO_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

3. 重启 Claude Desktop

服务器提供了以下工具：
- `get-coins`: 获取支持的币种分页列表
- `find-coin-ids`: 查找币名/符号对应的 CoinGecko ID
- `get-historical-data`: 获取历史价格、市值和交易量数据
- `get-ohlc-data`: 获取 OHLC K线数据
- `refresh-cache`: 刷新本地币种列表缓存

## 与 OpenAI 函数调用一起使用

```typescript
import { CoinGeckoService } from 'coingecko-server';
import OpenAI from 'openai';

const openai = new OpenAI();
const coinGeckoService = new CoinGeckoService(process.env.COINGECKO_API_KEY);

// Get function definitions
const functions = CoinGeckoService.getOpenAIFunctionDefinitions();

// Example: Get historical data
const response = await openai.chat.completions.create({
  model: "gpt-4-turbo-preview",
  messages: [{ role: "user", content: "Get Bitcoin's price history for the last week" }],
  functions: [functions[2]], // get_historical_data function
  function_call: "auto",
});

if (response.choices[0].message.function_call) {
  const args = JSON.parse(response.choices[0].message.function_call.arguments);
  const history = await coinGeckoService.getHistoricalData(
    args.id,
    args.vs_currency,
    args.from,
    args.to,
    args.interval
  );
}
```

## 数据类型

### OHLCData
```typescript
interface OHLCData {
  timestamp: number;
  open: number;
  high: number;
  low: number;
  close: number;
}
```

### HistoricalData
```typescript
interface HistoricalData {
  prices: [number, number][];
  market_caps: [number, number][];
  total_volumes: [number, number][];
}
```

### CoinInfo
```typescript
interface CoinInfo {
  id: string;
  symbol: string;
  name: string;
  platforms?: Record;
}
```

## 速率限制

请参考 [CoinGecko Pro API 文档](https://www.coingecko.com/api/documentation) 以获取当前的速率限制和使用指南。

## 许可证

MIT

**官方网站：** [https://github.com/crazyrabbitLTC/mcp-coingecko-server](https://github.com/crazyrabbitLTC/mcp-coingecko-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`finance`
- 标签：`finance`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`/path/to/coingecko-server/build/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/crazyrabbitltc-coingecko.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
