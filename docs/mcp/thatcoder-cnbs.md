---
title: "cnbs"
description: "MCP server for querying China National Bureau of Statistics data. Add to claudedesktopconfig."
---

# cnbs

MCP server for querying China National Bureau of Statistics data. Add to claudedesktopconfig.

# CNBS MCP Server

China National Bureau of Statistics + Major International Statistical Databases MCP Server. Fully connected to real APIs, with no simulated data.

## Data Sources

| Data Source | Authentication | Coverage |
|-------------|----------------|----------|
| **National Bureau of Statistics (NBS)** (data.stats.gov.cn) | None | Domestic monthly/quarterly/annual/provincial full data |
| **World Bank** (api.worldbank.org) | None | 200+ countries, GDP/trade/population/FDI/Gini coefficient, etc. |
| **IMF DataMapper** | None | WEO forecasts: GDP growth/inflation/government debt/current account, etc. |
| **OECD SDMX** | None | Quarterly GDP/employment/composite leading indicators/trade for member countries |
| **BIS Statistics** | None | Effective exchange rates/credit gaps/residential property prices/cross-border banking statistics |
| **FRED (Federal Reserve)** | `X-Fred-Api-Key` header | US interest rates/RMB exchange rate/crude oil/gold/S&P 500/M2 |
| **NBS Census Data** | None | Population census (2020)/economic census (2018)/agricultural census (2016) |
| **NBS Sectoral Statistics** | None | Fiscal/industrial/commercial/agricultural/monetary and financial/social security/real estate/energy |

> **FRED API Key:** Apply for free at https://fred.stlouisfed.org/docs/api/api_key.html, pass it via the `X-Fred-Api-Key` request header (HTTP mode), or set the `FRED_API_KEY` environment variable (stdio mode).

---

## Installation and Usage

### Run Directly with npx (Recommended)

bash
npx mcp-cnbs

### HTTP Mode

bash
npx mcp-cnbs --port 12345

### Global Installation

bash
npm install -g mcp-cnbs
mcp-cnbs

---

## MCP Client Configuration

### stdio Mode (npx)

**Supported Clients:** Claude Desktop, Cursor, Windsurf, Cherry Studio, Trae, Continue, and all other clients that support MCP.

json
{
  "mcpServers": {
    "cnbs": {
      "command": "npx",
      "args": ["mcp-cnbs"]
    }
  }
}

With FRED Support:

json
{
  "mcpServers": {
    "cnbs": {
      "command": "npx",
      "args": ["mcp-cnbs"],
      "env": {
        "FRED_API_KEY": "your_fred_api_key"
      }
    }
  }
}

### HTTP Mode (Remote Access)

**Supported Clients:** Trae, Cherry Studio, and other clients that support HTTP transport.

**ModelScope Free Demo (without FRED):**
json
{
  "mcpServers": {
    "cnbs": {
      "url": "https://mcp.api-inference.modelscope.net/c2ca6ece4e9946/mcp"
    }
  }
}

**HTTP Mode with FRED Support** — Include API Key in the request header:
json
{
  "mcpServers": {
    "cnbs": {
      "url": "https://your-cnbs-server/mcp",
      "headers": {
        "X-Fred-Api-Key": "your_fred_api_key"
      }
    }
  }
}

> This is a free public demo provided by Alibaba Cloud ModelScope, no authentication required.  
> For production use, it is recommended to deploy your own instance: [Free Deployment on ModelScope](https://modelscope.cn/mcp/servers/thatcoder/cnbs)

---

## Endpoint Description

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` or `/mcp` | POST | Streamable HTTP — Initialize session or send request |
| `/` or `/mcp` | GET | SSE notification stream (requires `Mcp-Session-Id` header) |
| `/` or `/mcp` | DELETE | Terminate session (requires `Mcp-Session-Id` header) |
| `/sse` | GET | Legacy SSE mode |
| `/message` | POST | Legacy SSE message |

---

## Tool List

### NBS Core Queries

| Tool | Function |
|------|----------|
| `cnbs_search` | Keyword search, returns the latest data values — **preferred** |
| `cnbs_batch_search` | Batch search for multiple keywords |
| `cnbs_economic_snapshot` | Get the latest values of 10 core macroeconomic indicators in one go (GDP, CPI, PPI, PMI, unemployment rate, industrial added value, retail sales, fixed investment, imports and exports, M2) |
| `cnbs_compare` | Regional comparison / time comparison |
| `cnbs_fetch_nodes` | Fetch category tree nodes — supports passing multiple category codes simultaneously |
| `cnbs_fetch_metrics` | Fetch dataset metric list — supports passing multiple setId simultaneously |
| `cnbs_fetch_series` | Fetch historical time series |
| `cnbs_fetch_end_nodes` | Recursively fetch all leaf nodes |

### NBS Auxiliary

| Tool | Function |
|------|----------|| `cnbs_get_guide` | Get the complete tool guide (suitable for LLM self-orientation) |
| `cnbs_get_regions` | Get region codes and names (GB/T 2260) |
| `cnbs_get_categories` | Get all NBS category codes |
| `cnbs_list_data_sources` | List all available data sources and tool mappings |
| `cnbs_fetch_data_from_source` | Fetch data from a specified data source |
| `cnbs_get_source_categories` | Get data source category information |
| `cnbs_search_in_source` | Search within a specified data source |

### World Bank

| Tool | Function |
|------|----------|
| `ext_world_bank` | Query a single indicator, supports multiple countries/years |
| `ext_world_bank_multi` | Query multiple indicators simultaneously, batch comparison across countries |
| `ext_world_bank_indicators` | List all predefined World Bank indicators |

### IMF

| Tool | Function |
|------|----------|
| `ext_imf` | Query IMF WEO data — supports multiple indicators at once |
| `ext_imf_indicators` | List predefined IMF indicators |
| `ext_imf_all_indicators` | Get the complete list of IMF DataMapper indicators |

### OECD

| Tool | Function |
|------|----------|
| `ext_oecd` | Query OECD SDMX data |
| `ext_oecd_datasets` | List predefined OECD datasets |

### BIS

| Tool | Function |
|------|----------|
| `ext_bis` | Query BIS statistics — supports multiple countries at once |
| `ext_bis_datasets` | List BIS datasets and key templates |

### FRED (Federal Reserve)

| Tool | Function |
|------|----------|
| `ext_fred` | Query FRED series — supports multiple series at once |
| `ext_fred_series` | List all predefined FRED series |

### Domestic Extended Data Sources

| Tool | Function |
|------|----------|
| `ext_cn_census` | Query NBS census data (population/economic/agricultural census) |
| `ext_cn_department` | Query NBS statistical indicators by department |
| `ext_cn_department_list` | List all department categories and indicator keywords |

### Cross-Source Comparison

| Tool | Function |
|------|----------|
| `ext_global_compare` | Fetch the same indicator from both the World Bank and IMF for quick cross-country comparison |

---

## Quick Examples

### Chinese Macroeconomic Overview

python
# Fetch all core macroeconomic indicators at once
cnbs_economic_snapshot()

# Latest value of a single indicator
cnbs_search(keyword="GDP")

# Batch query
cnbs_batch_search(keywords=["GDP", "CPI", "birth rate", "urbanization rate"])

# Regional comparison
cnbs_compare(keyword="GDP", regions=["Beijing", "Shanghai", "Guangdong"], compareType="region")

# Historical time series (first search to get cid/indic_id)
cnbs_search(keyword="GDP")
cnbs_fetch_series(setId="...", metricIds=["..."], periods=["2015YY-2024YY"])

### International Data

python
# G7 + China GDP growth comparison
ext_world_bank(indicator="GDP_GROWTH", countries=["CHN","USA","DEU","JPN","GBR","FRA","ITA","CAN"], startYear=2015)

# Batch query for multiple indicators in China
ext_world_bank_multi(indicators=["GDP_GROWTH","CPI","UNEMPLOYMENT","FDI_INFLOWS"], countries=["CHN"], startYear=2010)

# Single IMF indicator
ext_imf(indicators="GDP_GROWTH", countries=["CHN","USA","JPN","DEU"], periods=["2022","2023","2024","2025"])

# Multiple IMF indicators in one query
ext_imf(indicators=["GDP_GROWTH","CPI_INFLATION","GOVT_DEBT"], countries=["CHN","USA"], periods=["2020","2021","2022","2023","2024"])

# Cross-verification from World Bank and IMF
ext_global_compare(wbIndicator="GDP_GROWTH", imfIndicator="GDP_GROWTH", countries=["CHN","USA","DEU","JPN","IND"], startYear=2015)

### BIS & FRED

python
# Single country BIS
ext_bis(dataset="EER", countries="CN", lastNObservations=36)

# Multiple countries BIS in one query
ext_bis(dataset="EER", countries=["CN","US","DE","JP"], lastNObservations=24)

# Credit gap (early warning for systemic financial risk)
ext_bis(dataset="CREDIT_GAP", countries=["CN","US"], lastNObservations=20)

# Single FRED series
ext_fred(series="OIL_PRICE_WTI", limit=100, sortOrder="desc")

# Multiple FRED series in one query
ext_fred(series=["FED_FUNDS","CNY_USD","OIL_PRICE_WTI","GOLD_PRICE"], limit=30, sortOrder="desc")

# CNY to USD exchange rate (since 2020)
ext_fred(series="CNY_USD", observationStart="2020-01-01")### NBS Census and Departments

 
// Seventh National Population Census
ext_cn_census(type="population")

// Central Bank Monetary and Financial Data
ext_cn_department(department="monetary", indicator="M2 Money Supply")

// Fiscal Revenue and Expenditure
ext_cn_department(department="finance", indicator="Fiscal Revenue")

// View All Department Categories
ext_cn_department_list()

---

## NBS Classification Codes

| Code | Category | Typical Indicators |
|------|----------|--------------------|
| 1    | Monthly  | CPI, PPI, Industrial Added Value, PMI |
| 2    | Quarterly| GDP Quarterly Growth Rate |
| 3    | Annual   | Annual GDP, Population, Urbanization Rate |
| 5    | Provincial Quarterly | Provincial GDP Quarterly Values |
| 6    | Provincial Annual | Provincial GDP, Population Annual Values |
| 7    | Other/Surveys | Resident Surveys, Special Surveys |

## NBS Time Formats

- Annual: `2024YY`, range `["2020YY-2024YY"]`
- Quarterly: `2024A/B/C/D` (A=Q1, B=Q2, C=Q3, D=Q4), shortcuts `LAST6/LAST12/LAST18`
- Monthly: `202401MM`, range `["202301MM-202412MM"]`

## NBS Region Codes

Follows the GB/T 2260 standard. Use `cnbs_get_regions` to get the complete list.

| Region | Code         |
|--------|--------------|
| Nationwide | `000000000000` |
| Beijing | `110000000000` |
| Shanghai | `310000000000` |
| Guangdong | `440000000000` |
| Zhejiang | `330000000000` |
| Jiangsu | `320000000000` |

---

## Authentication Configuration

Authentication is not required by default. It can be enabled using a Bearer Token:

### stdio / HTTP Mode

bash
npx mcp-cnbs --port 12345 --auth-token your-secret-token
# or via environment variable
MCP_CNBS_AUTH_TOKEN=your-secret-token npx mcp-cnbs --port 12345

After enabling, requests must include:

Authorization: Bearer your-secret-token

### Cloudflare Workers

bash
npx wrangler secret put MCP_CNBS_AUTH_TOKEN

---

## Development

bash
npm install
npm run build
npm run start

## Environment Requirements

- Node.js >= 18.0.0
- Network access to: `data.stats.gov.cn`, `api.worldbank.org`, `www.imf.org`, `sdmx.oecd.org`, `stats.bis.org`, `api.stlouisfed.org`

## License

MIT

**Official site: ** [https://github.com/icen-ai/mcp-cnbs](https://github.com/icen-ai/mcp-cnbs)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `research and data`, `学术研究`, `搜索工具`, `数据查询`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `mcp-cnbs`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/thatcoder-cnbs.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
