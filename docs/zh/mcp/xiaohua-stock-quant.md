---
title: "股票量化价位分析MCP"
description: "该服务基于FastMCP框架构建，提供股票价格的量化分析能力。它为指定的股票计算Q级价格水平（保守级、正常级和极端级），以辅助投资决策。"
---

# 股票量化价位分析MCP

该服务基于FastMCP框架构建，提供股票价格的量化分析能力。它为指定的股票计算Q级价格水平（保守级、正常级和极端级），以辅助投资决策。

## Overview
This service is built based on the FastMCP framework, providing stock price quantitative analysis capabilities. It calculates Q-level price levels (conservative level, normal level, and extreme level) for specified stocks to assist investment decisions.

## Server Information
### Server Configuration
| Property | Value |
|---------|-------|
| Service Name | `stock_quant_mcp` |
| Communication Protocol | `sse` (Server-Sent Events) |
| Access URL | `http://211.159.225.228:9000/sse` |
| Model Identifier | `calculateQuantMcp` |

## Tool Interface
### `get_quant_price`
#### Functional Description

Calculates the Q-level price levels for a specified stock, including the following three key indicators:
- **Conservative Level**:
- **Normal Level**:
- **Extreme Level**:
(A denotes the lowest price, B denotes the highest price)

#### Parameter Definition
| Parameter Name | Type | Default Value | Description |
|----------------|------|---------------|-------------|
| `symbol` | `string` | `000001.SZ` | Stock code in formats like `'000858.SZ'` (Shenzhen Market/GEM) or `'000001.SH'` (Shanghai Market) |

#### Return Format
```json
{
  "保守位": "calculation result",
  "正常位": "calculation result",
  "极限位": "calculation result"
} ```
```

**官方网站：** [https://github.com/virgo777/qMCP](https://github.com/virgo777/qMCP)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`finance`, `data`
- 标签：`finance`, `research and data`

## MCP 配置

- 传输方式：`http`
- 启动命令：``
- 参数：无

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/xiaohua-stock-quant.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
