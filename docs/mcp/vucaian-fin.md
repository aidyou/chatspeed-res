---
title: "fin-mcp-server"
description: "Financial MCP Server is a financial technical analysis tool based on multimodal large models, capable of downloading stock data from Yahoo Finance, calculating technical indicators, generating profess…"
---

# fin-mcp-server

Financial MCP Server is a financial technical analysis tool based on multimodal large models, capable of downloading stock data from Yahoo Finance, calculating technical indicators, generating profess…

# Financial MCP Server

Financial MCP Server is a financial technical analysis tool based on multimodal large models. It can download stock data from Yahoo Finance, calculate technical indicators, generate professional K-line charts, and use multimodal large models such as Qwen2.5-VL to analyze the charts and produce professional financial analysis reports.

## Project Introduction

This project aims to provide financial analysts and investors with an automated technical analysis tool, implementing intelligent financial analysis through the following process:

1. Data acquisition: fetch real-time historical stock data from Yahoo Finance
2. Technical indicator calculation: compute various indicators including EMA, SMA, MACD, RSI, KDJ, Bollinger Bands, ATR, OBV, etc.
3. Chart generation: produce professional financial charts with a main K-line chart and multiple technical indicator sub-charts
4. Intelligent analysis: use multimodal large models (such as Qwen2.5-VL) to deeply analyze the generated charts
5. Report generation: output professional financial analysis reports including trend analysis, buy/sell signals, and risk assessment

### Core Features

- Multimodal analysis: supports image and text multimodal large-model analysis
- Rich technical indicators: built-in calculation of many commonly used technical indicators
- Professional charts: generates professional K-line charts that meet financial industry standards

### Tools
| Tool | Description |
|---|-------------|
| get_compony_info | Get basic company information |
| get_quarterly_balance_sheet | Get quarterly balance sheet information |
| get_data | Get recent stock data |
| generate_fin_report | Generate a professional financial analysis report |

## Deployment Guide

Environment requirements

- Python 3.12+
- pip package manager
- ta-lib financial quantitative technical analysis library

## Configuration File

You need a YAML configuration file to configure the server. A default configuration is provided in config_demo.yml, as follows:

```yaml
transport: "sse" # supports stdio, sse, streamable-http
mcp:
  host: "0.0.0.0"
  port: 8000

stock:
  source: "yahoo" # data source, supports yahoo or local
  data_dir: /app/data # directory for stock data and K-line charts
  public_base_url: "http://your-domain.com"  # URL used for generating images
llm:
  base_url: "https://api.openai.com/v1" # API base URL
  api_key: ${API_KEY} # API key; set it in .env or environment variables
  model: "Qwen/Qwen2.5-VL-72B-Instruct" # model to use
  temperature: 0.7 # generation temperature
  max_tokens: 4096 # max tokens
```

### MCP Configuration

You can set the transport protocol to `stdio`, `sse`, or `streamable-http`.

#### STDIO

For the `stdio` protocol, configure it like this:

```yaml
transport: "stdio"
```

#### SSE

For the `sse` protocol, configure it like this:

```yaml
transport: "sse"
mcp:
  host: "0.0.0.0"
  port: 8000
```

### LLM Configuration

`model` is the model name to use, `api_key` is the model's API key, and `base_url` is the model's API address. We support the following models.

- OpenAI series: GPT-4, GPT-4o, GPT-4o-mini, etc.
- Qwen series: Qwen2.5-VL, Qwen-VL and other multimodal models

## Starting the Service

```
YML=config.yml python -m fin_mcp_server
```

## stock Configuration
```yaml
stock:
  source: "yahoo" # currently only Yahoo Finance is supported
  data_dir: /app/data # directory for stock data and K-line charts
  public_base_url: "http://your-domain.com"  # URL used for generating images
```

## Output Example

#### The generated analysis report contains the following:
1. Company information
2. Recent quarterly balance sheet information
3. Recent stock data
4. Recent K-line chart
5. Price trend analysis: short-term, medium-term, and long-term trend judgments
6. Technical indicator interpretation: cross-validation of indicators such as MACD, RSI, KDJ
7. Volume-price analysis: the relationship between trading volume and price
8. Support and resistance levels: dynamically computed key support and resistance levels
9. Risk warnings: identification of potential risk signals
10. Trading strategy: specific entry, stop-loss, and take-profit suggestions
11. Confidence assessment: A/B/C three-tier confidence rating

## Notes

1. Data source limits: Yahoo Finance rate-limits requests; use it reasonably
2. API costs: using commercial APIs incurs corresponding fees
3. Model capabilities: different models vary in image understanding ability
4. Network environment: make sure the network connection is stable for fetching data and calling APIs

## License

This project is licensed under the `APACHE` license. See the `LICENSE` file for details.

**Official site: ** [https://github.com/vuca-ian/fin-mcp-server.git](https://github.com/vuca-ian/fin-mcp-server.git)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `finance`
- Tags: `finance`, `金融`, `分析报告`

## MCP Configuration

- Transport: `stdio`
- Command: `python`
- Args: `-m fin_mcp_server`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/vucaian-fin.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
