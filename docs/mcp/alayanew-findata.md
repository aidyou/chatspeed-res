---
title: "finData-mcp-server"
description: "An open-source MCP Server that supports various data providers such as Tushare, Wind, DataYes, etc. This enables AI applications to quickly retrieve financial data."
---

# finData-mcp-server

An open-source MCP Server that supports various data providers such as Tushare, Wind, DataYes, etc. This enables AI applications to quickly retrieve financial data.

width="400" align=center/>

![English](/mcp-assets/3789e0255aa72033cee70ede86310f02.svg)
![License](/mcp-assets/fee234587b371ccef8eaa9f331e5180d.svg)
[![Python Versions](/mcp-assets/01a3df7bb78637b1b7168f9c97e0a389.svg)]()
[![Tushare](/mcp-assets/356bd8a380cb8570e2c8ebe652ae0b93.svg)]()

  
Overview
 •
  
Demo
 •
  
Quick Start
 •
  
Supported Data Providers
 •
  
Tools

# Overview

**FinData** is an open-source **Model Context Protocol(MCP) Server** that provides professional financial data access capabilities for LLM. It supports various data providers such as **Tushare**, **Wind**, **DataYes**, etc. This enables AI applications to quickly retrieve financial data.

Fully supports both **Stdio** and **SSE** transports, offering flexibility for different environments.

# Demonstration

https://github.com/user-attachments/assets/1a6d02af-22a3-44a0-ada7-a771a1c4818d

# Quick Start

## Prerequisites

Before getting started, please complete the following preparations:

- python => 3.11
- mcp[cli]>=1.6.0
- pandas>=2.2.3
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

Depending on your data provider, install optional packages such as:

- tushare>=1.4.21

## Configuration

### Stdio Transport

You will need to edit the MCP client configuration file to add finData:

```JSON
{
  "mcpServers": {
    "finData": {
      "command": "uv",
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/PARENT/FOLDER/finData-mcp-server/src/findata",
        "run",
        "server.py"
      ],
      "env": {
        "DATA_API_TOKEN": "",  // API Token for accessing data provider
        "PROVIDER": "tushare"  // Specified data provider
      }
    }
  }
}
```

### SSE Transport

Set the environment variables `DATA_API_TOKEN` and `PROVIDER` on the server hosting the MCP Server:

   **Windows**
```bash
    set DATA_API_TOKEN=

    set PROVIDER=
```

   **Linux**
```bash
    export DATA_API_TOKEN=

    export PROVIDER=
```

Then, start the MCP Server:

```bash
uv run server.py --transport sse
```

- Optional Arguments:

  `--sse-host` Host to bind SSE server to (default: localhost)

  `--sse-port` Port for SSE server (default: 8000)

Once the MCP Server is running, update your MCP client's configuration with the following settings to connect to it.

```JSON
{
  "mcpServers": {
    "finData": {
      "name": "finData",
      "type": "sse",
      "baseUrl": "http://localhost:8000/sse"
    }
  }
}
```

**Note:** Variable names in configuration files may vary slightly between MCP clients. Refer to each client's documentation for proper configuration.

# Supported Data Providers

Set the `PROVIDER` environment variable to specify your provider:

- tushare

# Tools

## Tushare

### Market Data

- `daily` Get unadjusted daily stock market data.

### Fundamental Data

- `stock_basic` Get stock basic information including name, code, etc.
- `stock_company` Get listed company basic information.
- `bak_basic`  Get fundamental data for specific stocks within a given time range.

### Financial Data

- `income` Get company income statement data.
- `balancesheet` Get company balance sheet data.
- `cashflow` Get company cash flow statement data.

### Macroeconomic Data

- `shibor_lpr` Get Loan Prime Rate (LPR) data.
- `cn_gdp` Get Gross Domestic Product (GDP) data.
- `cn_cpi` Get Consumer Price Index (CPI) data.
- `cn_ppi` Get Producer Price Index (PPI) data.
- `cn_m` Get Money Supply data.
- `sf_month` Get Social Financing data.
- `cn_pmi` Get Purchasing Managers' Index (PMI) data.

# DataCanvas

![datacanvas](/mcp-assets/10f4495f4bdf0ec8db35d3ce8cc2fc1e.png)

This project is open-sourced by [DataCanvas](https://datacanvas.com/)

**Official site: ** [https://github.com/AlayaNeW/finData-mcp-server](https://github.com/AlayaNeW/finData-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `finance`
- Tags: `finance`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uv`
- Args: `--directory /ABSOLUTE/PATH/TO/PARENT/FOLDER/finData-mcp-server/src/findata run server.py`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/alayanew-findata.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
