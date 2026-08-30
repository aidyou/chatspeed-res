---
title: "mcp-server-ccxt 加密货币市场数据服务器"
description: "通过与主要交易所的集成，提供实时和历史加密货币市场数据。此服务器使 Claude 等大型语言模型能够获取当前价格、分析市场趋势并访问详细的交易信息。"
---

# mcp-server-ccxt 加密货币市场数据服务器

通过与主要交易所的集成，提供实时和历史加密货币市场数据。此服务器使 Claude 等大型语言模型能够获取当前价格、分析市场趋势并访问详细的交易信息。

# 加密货币市场数据 MCP 服务器

一个通过与主要交易所集成来提供实时和历史加密货币市场数据的模型上下文协议 (MCP) 服务器。该服务器使像 Claude 这样的大语言模型能够获取当前价格、分析市场趋势并访问详细的交易信息。

[![MCP](/mcp-assets/0702aa0c36b56660b23d8cf0298b9b37.svg)](https://modelcontextprotocol.io)
[![Python](/mcp-assets/8bd4a93e951852c158977ff6aeff1b0f.svg)](https://www.python.org)
[![CCXT](/mcp-assets/1b6e9c20882c27412857bbece9df722c.svg)](https://github.com/ccxt/ccxt)
[Smithery](https://smithery.ai/server/mcp-server-ccxt)

## 功能

- **实时市场数据**
  - 当前加密货币价格
  - 包含买卖价差的市场概要
  - 按成交量排名的顶级交易对
  - 支持多个交易所

- **历史分析**
  - OHLCV（K线）数据
  - 价格变动统计
  - 成交量历史追踪
  - 可自定义的时间范围

- **交易所支持**
  - Binance
  - Coinbase
  - Kraken
  - KuCoin
  - HyperLiquid
  - Huobi
  - Bitfinex
  - Bybit
  - OKX
  - MEXC

## 安装

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/mcp-server-ccxt) 自动安装适用于 Claude Desktop 的加密货币市场数据服务器：

```bash
npx -y @smithery/cli install mcp-server-ccxt --client claude
```

### 手动安装

```bash
# Using uv (recommended)
uv pip install mcp ccxt

# Using pip
pip install mcp ccxt
```

## 使用

### 运行服务器

```bash
python crypto_server.py
```

### 与 Claude Desktop 连接

1. 打开你的 Claude Desktop 配置文件：
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`

2. 添加服务器配置：

```json
{
    "mcpServers": {
        "crypto": {
            "command": "python",
            "args": ["/path/to/crypto_server.py"]
        }
    }
}
```

3. 重启 Claude Desktop

### 可用工具

1. **get-price**
   - 获取任何交易对的当前价格
   - 示例： "Binance 上 BTC/USDT 的当前价格是多少？"

2. **get-market-summary**
   - 获取详细的市场信息
   - 示例： "显示 ETH/USDT 的市场概要"

3. **get-top-volumes**
   - 列出按成交量排名的顶级交易对
   - 示例： "Kraken 上成交量排名前五的交易对是什么？"

4. **list-exchanges**
   - 显示所有支持的交易所
   - 示例： "支持哪些交易所？"

5. **get-historical-ohlcv**
   - 获取历史 K 线数据
   - 示例： "显示过去 7 天 BTC/USDT 价格数据，时间间隔为 1 小时"

6. **get-price-change**
   - 计算不同时间段的价格变动
   - 示例： "SOL/USDT 在 24 小时内的价格变动是多少？"

7. **get-volume-history**
   - 跟踪一段时间内的交易量
   - 示例： "显示过去一周内 ETH/USDT 的交易量历史"

### 示例查询

以下是一些在连接服务器后可以向 Claude 提出的示例问题：

```
- What's the current Bitcoin price on Binance?
- Show me the top 5 trading pairs by volume on Coinbase
- How has ETH/USDT performed over the last 24 hours?
- Give me a detailed market summary for SOL/USDT on Kraken
- What's the trading volume history for BNB/USDT over the last week?
```

## 技术细节

### 依赖项

- `mcp`: Model Context Protocol SDK
- `ccxt`: 加密货币交易所交易库
- Python 3.9 或更高版本

### 架构

服务器使用：
- CCXT 的异步支持，以实现高效的交易所通信
- MCP 的工具系统，用于 LLM 集成
- 标准化的数据格式，以确保一致的输出
- 连接池，以实现最佳性能

### 错误处理

服务器实现了针对以下情况的强大错误处理机制：
- 无效的交易对
- 交易所连接问题
- 速率限制
- 请求格式不正确
- 网络超时

## 开发

### 运行测试

```bash
# To be implemented
pytest tests/
```

### 贡献代码

1. 分叉仓库
2. 创建一个功能分支
3. 进行你的更改
4. 提交拉取请求

### 本地开发

```bash
# Clone the repository
git clone [repository-url]
cd crypto-mcp-server

# Install dependencies
uv pip install -e .
```

## 故障排除

### 常见问题

1. **交易所连接错误**
   - 检查您的互联网连接
   - 确认交易所是否正常运行
   - 确保所选交易所存在该交易对

2. **速率限制**
   - 在请求之间实现延迟
   - 对于高频查询使用不同的交易所
   - 检查特定交易所的速率限制

3. **数据格式问题**
   - 验证交易对格式（例如：BTC/USDT，而不是 BTCUSDT）
   - 检查时间框架规格
   - 确保数值参数在有效范围内

## 许可证

MIT 许可证 - 详情请参阅 LICENSE 文件

## 致谢

- [CCXT](https://github.com/ccxt/ccxt) 为交易所集成提供支持
- [Model Context Protocol](https://modelcontextprotocol.io) 提供 MCP 规范
- 加密货币交易所提供市场数据 API

**官方网站：** [https://github.com/Nayshins/mcp-server-ccxt](https://github.com/Nayshins/mcp-server-ccxt)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`finance`
- 标签：`finance`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`python`
- 参数：`/path/to/crypto_server.py`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/nayshins-ccxt.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
