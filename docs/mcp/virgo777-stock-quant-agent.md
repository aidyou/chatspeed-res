---
title: "Stock-Quant-Agent"
description: "Based on the Qwen3 inference engine, the detailed usage method for the stock quantification agent can be obtained through the \"Query Operation Manual\" built into the MCP platform. For detailed usage i…"
---

# Stock-Quant-Agent

Based on the Qwen3 inference engine, the detailed usage method for the stock quantification agent can be obtained through the "Query Operation Manual" built into the MCP platform. For detailed usage i…

# Stock Quantitative MCP Service User Manual

## 📌 Introduction
**Intelligent Stock Quantitative Support Point Calculation Service (MCP)** is a professional financial analysis tool built on the reasoning capabilities of the Qwen3 large model and remote quantitative computing servers, providing the following core functions:
- Real-time market data analysis and quantitative strategy recommendations
- Standardized API interfaces and SSE streaming data transmission

---

## ⚙️ Service Configuration Instructions
Add the following JSON configuration to your system to enable the service:
json
{
    "mcpServers": {
        "quant_mcp_server": {
            "type": "sse",
            "url": "http://www.socoo.xyz:9000/sse"
        }
    }
}

## ❓ Frequently Asked Questions
Q1: How to obtain detailed documentation?
Example inputs:
text
    What are the usage methods for the stock quantitative MCP service? (When installing too many MCP services, it's best to include the socoo keyword)
    What are the usage methods for the socoo stock quantitative MCP service?
    How do I use this socoo stock MCP service?
    How do I use this socoo quantification?
    Can you provide a detailed description document about the quantitative trading MCP service?
    I want to know how to use the MCP service for stock data analysis.
    What function calls does the MCP service support, and what are their functions?
    Tell me about the usage method of this stock quantitative MCP service;
    Explain the usage method of this quantitative MCP;
    How do I use this stock MCP service?
    How do I use this stock quantification?

---

This document includes:
1. Service configuration methods
2. Core function call examples
3. Complete list of functions and parameter descriptions
4. Real-time data integration guide
5. Solutions to common issues

## Technical Support:
Official Documentation: https://mcp-docs.socoo.xyz

Developer Email: virgo_wang@qq.com

**Official site: ** [https://www.modelscope.cn/mcp](https://www.modelscope.cn/mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`, `search`, `memory`, `files`, `communication`, `finance`, `media`
- Tags: `finance`, `search`, `knowledge and memory`, `developer tools`, `communication`, `entertainment and media`, `file systems`, `股票`, `量化`, `量化计算`

## MCP Configuration

- Transport: `http`
- Command: ``
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/virgo777-stock-quant-agent.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
