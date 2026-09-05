---
title: "KOSPI-KOSDAQ股服"
description: "一个使用FastMCP提供KOSPI/KOSDAQ股票数据的MCP服务器。"
---

# KOSPI-KOSDAQ股服

一个使用FastMCP提供KOSPI/KOSDAQ股票数据的MCP服务器。

# kospi-kosdaq-stock-server

[![PyPI version](/mcp-assets/23d249c45ee2b821646377d032be8e84.svg)](https://badge.fury.io/py/kospi-kosdaq-stock-server)
[Smithery](https://smithery.ai/server/@dragon1086/kospi-kosdaq-stock-server)

  

一个使用 FastMCP 提供 KOSPI/KOSDAQ 股票数据的 MCP 服务器。

## 功能

- 查询 KOSPI/KOSDAQ 的股票代码和名称
- 获取特定股票的 OHLCV 数据
- 获取特定股票的市值数据
- 获取特定股票的基本面数据（PER/PBR/股息收益率）
- 获取特定股票按投资者类型划分的交易量

## 可用工具

- `load_all_tickers` - 将所有 KOSPI 和 KOSDAQ 的股票代码和名称加载到内存中。
    - 无参数。

- `get_stock_ohlcv` - 获取特定股票的 OHLCV（开盘价/最高价/最低价/收盘价/成交量）数据。
    - `fromdate` (字符串, 必需): 开始日期 (YYYYMMDD)
    - `todate` (字符串, 必需): 结束日期 (YYYYMMDD)
    - `ticker` (字符串, 必需): 股票代码
    - `adjusted` (布尔值, 可选): 是否使用调整后的价格 (True: 调整后, False: 未调整)。默认为 True。

- `get_stock_market_cap` - 获取特定股票的市值数据。
    - `fromdate` (字符串, 必需): 开始日期 (YYYYMMDD)
    - `todate` (字符串, 必需): 结束日期 (YYYYMMDD)
    - `ticker` (字符串, 必需): 股票代码

- `get_stock_fundamental` - 获取特定股票的基本面数据（PER/PBR/股息收益率）。
    - `fromdate` (字符串, 必需): 开始日期 (YYYYMMDD)
    - `todate` (字符串, 必需): 结束日期 (YYYYMMDD)
    - `ticker` (字符串, 必需): 股票代码

- `get_stock_trading_volume` - 获取特定股票按投资者类型划分的交易量。
    - `fromdate` (字符串, 必需): 开始日期 (YYYYMMDD)
    - `todate` (字符串, 必需): 结束日期 (YYYYMMDD)
    - `ticker` (字符串, 必需): 股票代码

## 安装

此包需要 [uv](https://github.com/astral-sh/uv) 才能安装和执行。

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@dragon1086/kospi-kosdaq-stock-server) 自动安装适用于 Claude Desktop 的 KOSPI/KOSDAQ 股票数据服务器：

```bash
npx -y @smithery/cli install @dragon1086/kospi-kosdaq-stock-server --client claude
```

### 手动安装
```bash
# Create and activate a virtual environment
uv venv .venv
source .venv/bin/activate  # On Unix/macOS
# .venv\Scripts\activate   # On Windows

# Install the package
uv pip install kospi-kosdaq-stock-server
```

## 配置 Claude.app

安装包后，您需要在 `claude_desktop_config.json` 文件中配置 MCP 服务器。

1.  **定位配置文件：**
    *   在 macOS 上，该文件通常位于：
        `/Users/username/Library/Application Support/Claude/claude_desktop_config.json`
    *   在 Windows 上，该文件通常位于：
        `%APPDATA%/Claude/claude_desktop_config.json`

2.  **添加服务器配置：**
    打开 `claude_desktop_config.json` 文件，并向 `mcpServers` 对象中添加一个新的条目：

```json
{
    "mcpServers": {
        "kospi-kosdaq": {
            "command": "uvx",
            "args": ["kospi_kosdaq_stock_server"]
        }
    }
}
```

配置详情：
- **`command`**: 使用 `uvx` 来利用 uv 的隔离和依赖管理
- **`args`**: 只需要包名，因为入口点已在包中定义
- 不需要额外的环境变量

3.  **重启 Claude:** 保存对 `claude_desktop_config.json` 的更改后，重启 Claude 以使更改生效。

## 使用示例

配置完服务器后，您可以在 Claude 中这样使用它：

1. 首先，加载所有可用的股票代码：
```
Human: Please load all available stock tickers.
Assistant: I'll help you load all KOSPI and KOSDAQ stock tickers.

> Using tool 'load_all_tickers'...
Successfully loaded 2,873 stock tickers.
```

2. 获取特定股票的 OHLCV 数据：
```
Human: Show me Samsung Electronics' stock data for the last month.
Assistant: I'll retrieve Samsung Electronics' (005930) OHLCV data for the last month.

> Using tool 'get_stock_ohlcv'...
Date        Open    High    Low     Close   Volume
2024-02-14  73,800  74,000  73,400  73,700  7,823,124
2024-02-13  73,600  74,200  73,200  73,800  8,943,217
...
```

**官方网站：** [https://github.com/dragon1086/kospi-kosdaq-stock-server](https://github.com/dragon1086/kospi-kosdaq-stock-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`finance`
- 标签：`finance`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`kospi_kosdaq_stock_server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/dragon1086-kospi-kosdaq-stock.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
