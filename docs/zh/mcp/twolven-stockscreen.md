---
title: "Yahoo股票筛"
description: "通过Yahoo Finance提供全面的股票筛选功能。使大型语言模型（LLM）能够根据技术、基本面和期权标准筛选股票，并支持观察列表管理和结果存储。"
---

# Yahoo股票筛

通过Yahoo Finance提供全面的股票筛选功能。使大型语言模型（LLM）能够根据技术、基本面和期权标准筛选股票，并支持观察列表管理和结果存储。

# StockScreen MCP 服务器

一个通过 Yahoo Finance 提供全面股票筛选功能的模型上下文协议 (MCP) 服务器。支持基于技术、基本面和期权标准进行股票筛选，并支持观察列表管理和结果存储。

## 功能

### 股票筛选
- 技术分析筛选
  - 价格和成交量过滤器
  - 移动平均线（20、50、200日简单移动平均线）
  - RSI 指标
  - 平均真实波动范围 (ATR)
  - 趋势分析（1天、5天、20天变化）
  - MA 距离计算

- 基本面筛选
  - 市值过滤器
  - P/E 比率分析
  - 股息收益率标准
  - 收入增长指标
  - ETF 特定指标（资产管理规模、费用比率）

- 期权筛选
  - 隐含波动率 (IV) 过滤器
  - 期权成交量和未平仓合约
  - 看跌/看涨比率分析
  - 买卖价差评估
  - 盈利日期临近检查

### 数据管理
- 观察列表创建和管理
- 筛选结果存储
- 默认符号类别
  - 超大市值（>2000亿美元）
  - 大市值（100亿-2000亿美元）
  - 中等市值（20亿-100亿美元）
  - 小市值（3亿-20亿美元）
  - 微市值（2000亿美元
- "large_cap": 100亿-2000亿美元
- "mid_cap": 20亿-100亿美元
- "small_cap": 3亿-20亿美元
- "micro_cap": <3亿美元
- "etf": ETF 工具

2. `manage_watchlist`
```python
{
    "action": str,                       # Required: "create", "update", "delete", "get"
    "name": str,                         # Required: watchlist name (1-50 chars, alphanumeric with _ -)
    "symbols": List[str]                 # Required for create/update: list of stock symbols
}
```

3. `get_screening_result`
```python
{
    "name": str                          # Required: name of saved screening result
}
```

## 响应格式

### 技术筛选响应
```python
{
    "screen_type": "technical",
    "criteria": dict,                    # Original criteria used
    "matches": int,                      # Number of matching stocks
    "results": [                         # List of matching stocks
        {
            "symbol": str,
            "price": float,
            "volume": float,
            "rsi": float,
            "sma_20": float,
            "sma_50": float,
            "sma_200": float,
            "atr": float,
            "atr_pct": float,
            "price_changes": {
                "1d": float,             # 1-day price change %
                "5d": float,             # 5-day price change %
                "20d": float             # 20-day price change %
            },
            "ma_distances": {
                "pct_from_20sma": float,
                "pct_from_50sma": float,
                "pct_from_200sma": float
            }
        }
    ],
    "rejected": [                        # List of stocks that didn't match
        {
            "symbol": str,
            "rejection_reasons": List[str]
        }
    ],
    "timestamp": str
}
```
## Claude 使用提示

“我已经启用了提供股票筛选功能的 stockscreen 工具。您可以使用三个主要功能：

1. 用各种标准类型筛选股票：
   - 技术：价格、成交量、RSI、移动平均线、ATR
   - 基本面：市值、P/E、股息、增长率
   - 期权：IV、成交量、盈利日期
   - 自定义：结合多种标准类型

2. 管理观察列表：
   - 创建和更新符号列表
   - 删除现有观察列表
   - 检索观察列表内容

3. 访问已保存的筛选结果：
   - 加载之前的筛选结果
   - 查看匹配的符号和标准

所有功能都包括错误处理、详细的市场数据和全面的响应。”

## 要求

- Python 3.12+
- MCP 服务器
- yfinance
- pandas
- numpy
- asyncio

## 限制

- 数据来源于雅虎财经，可能存在延迟
- 根据雅虎财经API的限制进行速率限制
- 期权数据的可用性取决于市场时间
- 某些财务指标可能有延迟或不可用

## 贡献

欢迎贡献！请随时提交Pull Request。

## 许可证

本项目采用MIT许可证 - 详情请参阅[LICENSE](https://github.com/twolven/mcp-stockscreen/blob/HEAD/LICENSE)文件。

## 作者

Todd Wolven - ([https://github.com/twolven](https://github.com/twolven))

## 致谢

- 使用Anthropic的模型上下文协议（MCP）构建
- 数据由[Yahoo Finance](https://finance.yahoo.com/)提供
- 为与Anthropic的Claude一起使用而开发

**官方网站：** [https://github.com/twolven/mcp-stockscreen](https://github.com/twolven/mcp-stockscreen)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`finance`
- 标签：`finance`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`python`
- 参数：`path/to/stockscreen.py`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/twolven-stockscreen.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
