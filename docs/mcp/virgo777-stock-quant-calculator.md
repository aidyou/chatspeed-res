---
title: "Stock-Quant-Calculator-MCP"
description: "Based on the Qwen3 inference engine, the stock quant agent calculates the support levels for a specific stock when it is declining and provides recommendations. Detailed usage instructions can be obta…"
---

# Stock-Quant-Calculator-MCP

Based on the Qwen3 inference engine, the stock quant agent calculates the support levels for a specific stock when it is declining and provides recommendations. Detailed usage instructions can be obta…

# Stock Quant MCP Service User Manual

## Introduction
The **intelligent stock quant support-level calculation service (MCP)** is a professional financial analysis tool built on the Qwen3 large-model reasoning capability and a remote quant calculation server. It provides the following core functions:
- Calculation of target stock support entry prices
- Standardized API interface and SSE streaming data transmission

---

## Service Configuration
Add the following JSON configuration to your system to enable the service:
```json
{
    "mcpServers": {
        "quant_mcp_server": {
            "type": "sse",
            "url": "http://www.socoo.xyz:9000/sse"
        }
    }
}
```
---
# Direct usage:
# We recommend using the SSE address above directly

| Tool | How to use | Description |
|:-----------------|:------------------------|:------------------------------|
| cookbook | How do I use this socoo stock MCP service? | Returns the usage guide for the socoo quant service MCP |
| get_support_quant_price | Help me calculate the support level for 000858.SZ. | Returns the quant-calculated support levels for a specific stock (conservative, normal, extreme) |
| get- | Request... API | Redundant quant calculation API service |

## FAQ

Q1: How do I get detailed documentation?

Sample input:
```text
    What are the usage methods of the stock quant MCP service? (when many MCP services are installed, it is best to include the socoo keyword)
    How do I use this socoo stock MCP service?
    How do I use this socoo quant service?
    Can you provide a detailed documentation of the quant trading MCP service?
    I want to know how to use the MCP service for stock data analysis.
    What function calls does the MCP service support, and what do these functions do?
    Tell me how to use this stock quant MCP service;
    Tell me how to use this quant MCP service;
    How do I use this stock MCP service?
    How do I use this stock quant tool?
```

## Technical Support:
Official docs: https://mcp-docs.socoo.xyz

Developer email: virgo_wang@qq.com

**Official site: ** [https://www.modelscope.cn/mcp](https://www.modelscope.cn/mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `communication`, `finance`
- Tags: `communication`, `finance`, `股票量化`, `量化`, `支撑点位`, `股票`

## MCP Configuration

- Transport: `http`
- Command: ``
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/virgo777-stock-quant-calculator.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
