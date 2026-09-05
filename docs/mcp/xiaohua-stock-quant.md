---
title: "stock_quant_mcp"
description: "This service is built based on the FastMCP framework, providing stock price quantitative analysis capabilities. It calculates Q-level price levels (conservative level, normal level, and extreme level)…"
---

# stock_quant_mcp

This service is built based on the FastMCP framework, providing stock price quantitative analysis capabilities. It calculates Q-level price levels (conservative level, normal level, and extreme level)…

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
  "Conservative Level": "calculation result",
  "Normal Level": "calculation result",
  "Extreme Level": "calculation result"
} ```
```

**Official site: ** [https://github.com/virgo777/qMCP](https://github.com/virgo777/qMCP)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `finance`, `data`
- Tags: `finance`, `research and data`

## MCP Configuration

- Transport: `http`
- Command: ``
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/xiaohua-stock-quant.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
