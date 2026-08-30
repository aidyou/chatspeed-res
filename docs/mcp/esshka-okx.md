---
title: "OKX行情数据"
description: "通过模型上下文协议接口提供OKX交易所的实时加密货币价格数据，允许访问任何交易工具的历史K线数据和当前市场价格。"
---

# OKX行情数据

通过模型上下文协议接口提供OKX交易所的实时加密货币价格数据，允许访问任何交易工具的历史K线数据和当前市场价格。

# OKX MCP 服务器

这是一个模型上下文协议（MCP）服务器，提供来自OKX交易所的实时加密货币价格数据。

## 特性

此MCP服务器连接到OKX API，通过一个简单的工具界面提供加密货币的价格信息。它包括全面的错误处理、请求日志记录以及通过OKX API实现的速率限制。

### 工具

#### `get_candlesticks`

检索OKX上任何工具的历史K线（OHLCV）数据。

- **输入**:
  - `instrument`: 字符串（必需）- 工具ID（例如 "BTC-USDT"）
  - `bar`: 字符串（可选）- 时间间隔（例如 "1m", "5m", "1H", "1D"），默认为 "1m"
  - `limit`: 数字（可选）- 返回的K线条数（最大100），默认为100
- **输出**: JSON对象数组，每个包含：
  - `timestamp`: K线的时间戳
  - `open`: 开盘价
  - `high`: 最高价
  - `low`: 最低价
  - `close`: 收盘价
  - `volume`: 成交量
  - `volumeCurrency`: 成交量以货币单位表示

示例用法：

```json
[
  {
    "timestamp": "2025-03-07T17:00:00.000Z",
    "open": "87242.8",
    "high": "87580.2",
    "low": "86548.0",
    "close": "87191.8",
    "volume": "455.72150427",
    "volumeCurrency": "39661166.242091111"
  }
]
```

#### `get_price`

获取OKX上任何工具的最新价格和24小时市场数据。

- **输入**:
  - `instrument`: 字符串（必需）- 工具ID（例如 "BTC-USDT"）
- **输出**: 包含以下内容的JSON对象：
  - `instrument`: 请求的工具ID
  - `lastPrice`: 最新成交价
  - `bid`: 当前最佳买入价
  - `ask`: 当前最佳卖出价
  - `high24h`: 24小时内最高价
  - `low24h`: 24小时内最低价
  - `volume24h`: 24小时内成交量
  - `timestamp`: 数据的时间戳

示例用法：

```json
{
  "instrument": "BTC-USDT",
  "lastPrice": "65432.1",
  "bid": "65432.0",
  "ask": "65432.2",
  "high24h": "66000.0",
  "low24h": "64000.0",
  "volume24h": "1234.56",
  "timestamp": "2024-03-07T17:22:28.000Z"
}
```

## 开发

安装依赖项：

```bash
npm install
```

构建服务器：

```bash
npm run build
```

使用自动重建进行开发：

```bash
npm run watch
```

## 安装

要与Claude Desktop或VSCode一起使用，请将服务器配置添加到您的MCP设置中：

macOS (VSCode):

```bash
~/Library/Application Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json
```

macOS (Claude Desktop):

```bash
~/Library/Application Support/Claude/claude_desktop_config.json
```

Windows (VSCode):

```bash
%APPDATA%/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json
```

Windows (Claude Desktop):

```bash
%APPDATA%/Claude/claude_desktop_config.json
```

配置：

```json
{
  "mcpServers": {
    "okx": {
      "command": "node",
      "args": ["/path/to/okx-mcp-server/build/index.js"],
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

### 错误处理

服务器实现了全面的错误处理：

- 捕获并返回带有上下文的网络错误
- 对于无效的工具ID，返回适当的错误消息
- 通过axios超时配置遵守API速率限制
- 所有错误均被记录以供调试使用

**官方网站：** [https://github.com/esshka/okx-mcp](https://github.com/esshka/okx-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`finance`
- 标签：`finance`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`/path/to/okx-mcp-server/build/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/esshka-okx.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
