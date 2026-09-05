---
title: "Yiyanstock"
description: "Financial Data MCP Toolkit Based on HTTP API encapsulation, it provides full-chain financial data query capabilities for A-shares. There are a total of 20 MCP tools, covering core scenarios such as ma…"
---

# Yiyanstock

Financial Data MCP Toolkit Based on HTTP API encapsulation, it provides full-chain financial data query capabilities for A-shares. There are a total of 20 MCP tools, covering core scenarios such as ma…

# Financial Data MCP Toolkit

> Based on HTTP API encapsulation, it provides full-chain financial data query capabilities for A-shares.  
> There are a total of **20** MCP tools, covering core scenarios such as market quotes, financials, technical indicators, macroeconomics, fund valuations, trading calendars, and announcement queries.

---

## Table of Contents

| # | Tool Name | Function Description |
|---|-----------|----------------------|
| 1 | [get_stock_code](#1-get_stock_code) | Stock name → Full code |
| 2 | [get_stock_real_time_quotation](#2-get_stock_real_time_quotation) | Real-time A-share market quotes |
| 3 | [get_stock_history_quotation](#3-get_stock_history_quotation) | Historical A-share market quotes |
| 4 | [get_high_frequency_quotes](#4-get_high_frequency_quotes) | High-frequency (minute-level) market quotes |
| 5 | [get_intraday_snapshot](#5-get_intraday_snapshot) | Intraday tick-by-tick snapshots |
| 6 | [get_date_sequence](#6-get_date_sequence) | Financial/fundamental date sequence |
| 7 | [get_edb_data](#7-get_edb_data) | Macroeconomic database (EDB) |
| 8 | [get_thematic_report](#8-get_thematic_report) | Thematic reports |
| 9 | [get_fund_realtime_valuation](#9-get_fund_realtime_valuation) | Fund real-time valuation (minute frequency) |
| 10 | [get_fund_daily_valuation](#10-get_fund_daily_valuation) | Daily final fund valuation |
| 11 | [query_trading_dates](#11-query_trading_dates) | Trading calendar query |
| 12 | [offset_trading_date](#12-offset_trading_date) | Trading date offset calculation |
| 13 | [search_securities_code](#13-search_securities_code) | Securities code/name query |
| 14 | [query_announcement](#14-query_announcement) | Listed company announcement query |
| 15 | [get_stock_basic_info](#15-get_stock_basic_info) | A-share basic information summary (25 items) |
| 16 | [get_listed_company_info](#16-get_listed_company_info) | Listed company basic information (30 items) |
| 17 | [get_stock_equity_shareholder](#17-get_stock_equity_shareholder) | Equity and shareholder data (36 items) |
| 18 | [get_stock_financial_data](#18-get_stock_financial_data) | Financial statements and derived indicators (300+ items) |
| 19 | [get_stock_daily_quotes_tech](#19-get_stock_daily_quotes_tech) | Daily market quotes and technical indicators (75 items) |
| 20 | [smart_stock_picking](#20-smart_stock_picking) | Smart stock picking |

---

## General Instructions

### Stock Code Format

All parameters involving stock codes must include the exchange suffix (standard format):

| Exchange | Suffix | Example |
|----------|--------|---------|
| SSE      | `.SH`  | `600030.SH` |
| SZSE     | `.SZ`  | `000001.SZ` |
| GEB      | `.SZ`  | `300033.SZ` |
| STAR     | `.SH`  | `688001.SH` |

Multiple codes should be separated by English commas, e.g., `300033.SZ,600030.SH`

### Date Format

- Date parameters should follow the format: `YYYY-MM-DD`, e.g., `2025-09-30`
- Time parameters should follow the format: `YYYY-MM-DD HH:mm:ss`, e.g., `2025-08-25 09:30:00`

### Return Structure

Most tools return JSON strings, grouped by `thscode`, with a general format as follows:

json
[
  {
    "thscode": "300033.SZ",
    "data": [
      {"indicator": "Indicator English Name", "description": "Indicator Chinese Name", "value": "Value"}
    ]
  }
]

---

## Tool Details

---

### 1. `get_stock_code`

**Function**: Query the complete exchange code corresponding to the stock's Chinese name, supporting fuzzy name correction.

#### Parameters

| Parameter Name | Type   | Required | Description |
|----------------|--------|----------|-------------|
| `stock_name`   | string | ✅        | Stock name, supports approximate input, e.g., "HUADAJIYIN" will be corrected to "HUADA JIYIN (BGI)" |

#### Example Response

json
{
  "name": "HUADAJIYIN (mistyped)",
  "corrected_name": "BGI (HUADAJIYIN corrected)",
  "stock_code": "300676.SZ"
}

> `corrected_name` is the standard name after system correction.

---

### 2. `get_stock_real_time_quotation`

**Function**: Obtain the current real-time market quote snapshot for A-shares, returning the specified market fields.

#### Parameters

| Parameter Name | Type   | Required | Description |
|----------------|--------|----------|-------------|
| `stock_code`   | string | ✅        | Complete stock code, e.g., `601988.SH`, multiple codes separated by English commas |
| `indicators`   | string | ✅        | Fields to query, separated by English commas (see field list below) |#### Available `indicators` Fields

| Field Name | Meaning |
|------------|---------|
| `preClose` | Previous closing price |
| `open` | Opening price |
| `high` | Highest price |
| `low` | Lowest price |
| `latest` | Latest price / closing price of the day |
| `amount` | Turnover (in RMB) |
| `volume` | Volume (in lots) |
| `changeRatio` | Price change ratio (%) |
| `turnoverRatio` | Turnover ratio (%) |

#### Example Response

json
[
  {
    "thscode": "300676.SZ",
    "time": ["2025-09-16 16:30:07"],
    "table": {
      "open": [53.12],
      "high": [53.20],
      "latest": [52.80],
      "changeRatio": [-0.60]
    }
  }
]

---

### 3. `get_stock_history_quotation`

**Function**: Retrieve historical daily stock quotation data (K-line data) for A-shares, supporting batch queries for multiple stocks.

#### Parameters

| Parameter Name | Type | Required | Description |
|----------------|------|----------|-------------|
| `stock_code` | string | ✅ | Full stock code(s), separated by commas if multiple |
| `indicators` | string | ✅ | Quotation fields, same as real-time quotations (see the field list above) |
| `startdate` | string | ✅ | Start date, format `YYYY-MM-DD` |
| `enddate` | string | ✅ | End date, format `YYYY-MM-DD` |

> The unit for volume (`volume`) is **lots**.

---

### 4. `get_high_frequency_quotes`

**Function**: Retrieve high-frequency minute-level market data for stocks, futures, and options, supporting various periods and adjustment methods.

#### Parameters

| Parameter Name | Type | Required | Default Value | Description |
|----------------|------|----------|---------------|-------------|
| `stock_code` | string | ✅ | — | Full stock code(s), separated by commas if multiple |
| `indicators` | string | ✅ | — | Quotation fields, separated by commas (open/high/low/close/volume/amount/changeRatio/turnoverRatio) |
| `starttime` | string | ✅ | — | Start time, format `YYYY-MM-DD HH:mm:ss` |
| `endtime` | string | ✅ | — | End time, format `YYYY-MM-DD HH:mm:ss` |
| `interval` | string | ❌ | `"1"` | Period (minutes): 1 / 3 / 5 / 10 / 15 / 30 / 60 |
| `cps` | string | ❌ | `"no"` | Adjustment method: `no`-no adjustment, `backward1`-backward adjustment, `forward3`-forward adjustment |

---

### 5. `get_intraday_snapshot`

**Function**: Retrieve intraday tick-by-tick market snapshot for stocks, **start and end times must be within the same trading day**.

#### Parameters

| Parameter Name | Type | Required | Description |
|----------------|------|----------|-------------|
| `stock_code` | string | ✅ | Full stock code(s), separated by commas if multiple |
| `indicators` | string | ✅ | Field list, commonly used: `tradeDate,tradeTime,preClose,open,high,low,latest,vol,amount,bid1,ask1,bidSize1,askSize1` |
| `starttime` | string | ✅ | Start time, format `YYYY-MM-DD HH:mm:ss` |
| `endtime` | string | ✅ | End time, format `YYYY-MM-DD HH:mm:ss`, **must be on the same day as starttime** |

---

### 6. `get_date_sequence`

**Function**: Retrieve historical date sequences for financial/fundamental indicators of a stock, such as return on equity, net profit attributable to shareholders, etc., over time.

#### Parameters

| Parameter Name | Type | Required | Default Value | Description |
|----------------|------|----------|---------------|-------------|
| `stock_code` | string | ✅ | — | Full stock code(s), separated by commas if multiple |
| `indicators_json` | string | ✅ | — | List of indicators in JSON string format, see example below |
| `startdate` | string | ✅ | — | Start date, format `YYYY-MM-DD` |
| `enddate` | string | ✅ | — | End date, format `YYYY-MM-DD` |
| `interval` | string | ❌ | `"D"` | Interval: D-daily / W-weekly / M-monthly / Q-quarterly / S-semi-annually / Y-annually |
| `fill` | string | ❌ | `"Previous"` | Handling of non-trading days: `Previous`-carry forward previous value / `Blank`-leave blank |

#### `indicators_json` Example

json
[
  {"indicator": "ths_roe_stock", "indiparams": ["20241231"]},
  {"indicator": "ths_net_profit_stock", "indiparams": [""]}
]

---

### 7. `get_edb_data`

**Function**: Retrieve data from the Economic Database (EDB), such as GDP, CPI, PMI, social financing, M2, and other macroeconomic indicators.

#### Parameters

| Parameter Name | Type | Required | Description |
|----------------|------|----------|-------------|| `indicators` | string | ✅ | EDB indicator codes, separated by English commas, e.g., `M001620326,M002822183` (can be queried via the super command terminal) |
| `startdate` | string | ✅ | Start date, format `YYYY-MM-DD` |
| `enddate` | string | ✅ | End date, format `YYYY-MM-DD` |
| `startrtime` | string | ❌ | Data update time filter - start, format `YYYY-MM-DD HH:mm:ss`, can be empty |
| `endrtime` | string | ❌ | Data update time filter - end, format `YYYY-MM-DD HH:mm:ss`, can be empty |

---

### 8. `get_thematic_report`

**Function**: Obtain thematic report data, such as an overview of REITs projects and industry-specific data. The report code is obtained through the command terminal.

#### Parameters

| Parameter Name | Type | Required | Description |
|----------------|------|----------|-------------|
| `reportname` | string | ✅ | Report code, e.g., `p03341` (query via the command terminal) |
| `functionpara_json` | string | ✅ | Report filter parameters, JSON string, e.g., `{"sdate":"20210421","edate":"20211119","xmzt":"ALL"}` |
| `outputpara` | string | ✅ | Output field control, format `field_name:Y`, e.g., `"p03341_f001:Y,p03341_f002:Y"` |

---

### 9. `get_fund_realtime_valuation`

**Function**: Obtain real-time fund valuation (minute frequency), which can fetch the latest or specified time range valuation data.

#### Parameters

| Parameter Name | Type | Required | Default Value | Description |
|----------------|------|----------|---------------|-------------|
| `fund_codes` | string | ✅ | — | Fund codes, separated by English commas, e.g., `000001.OF,000003.OF` |
| `outputpara` | string | ✅ | — | Output fields, format `field_name:Y` (see the list of fields below) |
| `only_latest` | string | ❌ | `"1"` | `"1"`-return only the latest valuation, `"0"`-return the time range |
| `begin_time` | string | ❌ | `""` | Start time (required if `only_latest="0"`), format `YYYY-MM-DD HH:mm:ss` |
| `end_time` | string | ❌ | `""` | End time (required if `only_latest="0"`), format `YYYY-MM-DD HH:mm:ss` |

#### Available `outputpara` Fields

| Field Name | Meaning |
|------------|---------|
| `changeRatioValuation` | Valuation change ratio (%) |
| `realTimeValuation` | Real-time valuation net value |
| `Deviation30TDays` | 30 trading days average deviation (%) |
| `rank` | Valuation change ratio ranking |

---

### 10. `get_fund_daily_valuation`

**Function**: Obtain daily final fund valuation (daily frequency), including valuation net value, actual net value, and deviation rate.

#### Parameters

| Parameter Name | Type | Required | Default Value | Description |
|----------------|------|----------|---------------|-------------|
| `fund_codes` | string | ✅ | — | Fund codes, separated by English commas, e.g., `000001.OF,000003.OF` |
| `begin_date` | string | ✅ | — | Start date, format `YYYY-MM-DD` |
| `end_date` | string | ✅ | — | End date, format `YYYY-MM-DD` |
| `outputpara` | string | ❌ | `"finalValuation:Y,netAssetValue:Y,deviation:Y"` | Output fields: `finalValuation`-daily final valuation, `netAssetValue`-daily actual net value, `deviation`-deviation rate (%) |

---

### 11. `query_trading_dates`

**Function**: Query the trading calendar for a specified market, returning a list of all trading dates within the interval or the number of dates.

#### Parameters

| Parameter Name | Type | Required | Default Value | Description |
|----------------|------|----------|---------------|-------------|
| `marketcode` | string | ✅ | — | Exchange code (`212001`-SSE, `212100`-SZSE, `212200`-HKEX) |
| `startdate` | string | ✅ | — | Start date, format `YYYY-MM-DD` |
| `enddate` | string | ✅ | — | End date, format `YYYY-MM-DD` |
| `date_type` | string | ❌ | `"0"` | `"0"`-trading day, `"1"`-calendar day |
| `period` | string | ❌ | `"D"` | D-day / W-week / M-month / Q-quarter / S-half year / Y-year |
| `date_format` | string | ❌ | `"0"` | `"0"`-YYYY-MM-DD, `"1"`-YYYY/MM/DD, `"2"`-YYYYMMDD |
| `mode` | string | ❌ | `"1"` | `"1"`-return date list, `"2"`-return only the number of dates |

---

### 12. `offset_trading_date`

**Function**: Calculate the target date after offsetting a certain number of trading days forward or backward from a base date.

#### Parameters

| Parameter Name | Type | Required | Default Value | Description ||--------|------|------|--------|------|
| `marketcode` | string | ✅ | — | Exchange code, such as `212001` (SSE) |
| `startdate` | string | ✅ | — | Base date, format `YYYY-MM-DD` |
| `offset` | string | ✅ | — | Offset, negative for backward (e.g., `"-5"`), positive for forward (e.g., `"5"`) |
| `period` | string | ❌ | `"D"` | D-Daily / W-Weekly / M-Monthly / Q-Quarterly / S-Semi-annually / Y-Yearly |
| `date_type` | string | ❌ | `"0"` | `"0"`-Trading day, `"1"`-Calendar day |
| `date_format` | string | ❌ | `"0"` | `"0"`-YYYY-MM-DD, `"1"`-YYYY/MM/DD, `"2"`-YYYYMMDD |
| `output` | string | ❌ | `"singledate"` | `"singledate"`-Return single date, `"sequencedate"`-Return full sequence |

---

### 13. `search_securities_code`

**Function**: Query standard codes through market codes or security short names, supporting fuzzy/precise matching.

#### Parameters

| Parameter Name | Type | Required | Default Value | Description |
|--------|------|------|--------|------|
| `query` | string | ✅ | — | Query content: market code (e.g., `"000001"`) or security short name (e.g., `"Ping An Bank"`) |
| `mode` | string | ❌ | `"seccode"` | `"seccode"`-Search by code, `"secname"`-Search by name |
| `sectype` | string | ❌ | `""` | Security type filter: `001`-Stock, `002`-Fund, empty-All |
| `market` | string | ❌ | `""` | Market filter: `212001`-SSE, `212100`-SZSE, empty-All |
| `tradestatus` | string | ❌ | `"0"` | `"0"`-All, `"1"`-Normal trading, `"2"`-Suspended |
| `isexact` | string | ❌ | `"0"` | `"0"`-Fuzzy match, `"1"`-Exact match |

---

### 14. `query_announcement`

**Function**: Query announcements of listed companies, supporting queries by code or sector, with filtering by announcement type and date range.

#### Parameters

| Parameter Name | Type | Required | Default Value | Description |
|--------|------|------|--------|------|
| `codes` | string | ✅ | — | Security codes, separated by English commas; if querying by sector, pass an empty string and use the `mode` parameter |
| `outputpara` | string | ✅ | — | Output fields, format `field_name:Y`, e.g., `"thscode:Y,secname:Y,reportType:Y,title:Y,publishDate:Y"` |
| `report_type` | string | ❌ | `"903"` | Announcement type: `"903"`-All, `"901002004"`-Listing announcement (other types see documentation) |
| `begin_date` | string | ❌ | `""` | Start date of announcements, format `YYYY-MM-DD` |
| `end_date` | string | ❌ | `""` | End date of announcements, format `YYYY-MM-DD` |
| `mode` | string | ❌ | `""` | Query by sector: `"allAStock"`-All A-shares, `"allBond"`-All bonds, empty-Query by code |

---

### 15. `get_stock_basic_info`

**Function**: Query **25 items** of static basic information for A-share stocks in one go.

#### Parameters

| Parameter Name | Type | Required | Description |
|--------|------|------|------|
| `stock_code` | string | ✅ | Full stock code, multiple codes separated by English commas |

#### Included Indicators (25 items)

Stock short name, English short name, initial pinyin, former security names, stock code, H-share information of the same company, US share information of the same company, stock type, IPO date, backdoor listing date, listing exchange, listing sector, listing status, trading currency, related concepts, whether it is a risk warning board, whether it is a component of major indices, index weight, whether it is a margin trading target, whether it is a Shanghai/Hong Kong Connect buy target, whether it is a new stock, convertible bond short name of the same company.

#### Example Response

json
[
  {
    "thscode": "300033.SZ",
    "data": [
      {"indicator": "ths_stock_short_name_stock", "description": "Stock short name", "value": "Tonghua Shun"},
      {"indicator": "ths_ipo_date_stock", "description": "IPO date", "value": "2012-05-18"},
      {"indicator": "ths_listedsector_stock", "description": "Listing sector", "value": "GEM"}
    ]
  }
]

---

### 16. `get_listed_company_info`

**Function**: Query **30 items** of basic information for A-share listed companies, including time-varying indicators (controlling shareholder, industry classification, etc.), with support for specifying historical time points.

#### Parameters

| Parameter Name | Type | Required | Default Value | Description || Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `stock_code` | string | ✅ | — | Full stock code, multiple codes separated by English commas |
| `date` | string | ❌ | Today | Query time point, format `YYYY-MM-DD`. For time-varying indicators such as controlling shareholder, actual controller, main business, and industry classification, this date is used. If not provided, the latest data will be fetched |

#### Indicators Included (30 items)

Company Chinese/English name, establishment date, business registration number, unified social credit code, registered capital and currency, **controlling shareholder**, **controlling shareholder shareholding ratio**, **actual controller** (including shareholding ratio, type), enterprise type, legal representative, business scope, **main business**, main product name/type, competitive companies, comparable companies, **new CSRC industry affiliation** (including code), **SW industry affiliation** (including code), chairman/CFO/board secretary (current + former).

#### Example Response

json
[
  {
    "thscode": "300033.SZ",
    "query_date": "2026-04-01",
    "data": [
      {"indicator": "ths_corp_cn_name_stock", "description": "Company Chinese name", "value": "Tonghuashun"},
      {"indicator": "ths_controlling_holder_stock", "description": "Controlling shareholder", "value": "Yi Zheng"},
      {"indicator": "ths_the_sw_industry_stock", "description": "SW industry", "value": "Internet software & services"}
    ]
  }
]

---

### 17. `get_stock_equity_shareholder`

**Function**: Query A-share equity structure and shareholder data, including details of the top ten shareholders/circulating shareholders. Summary indicators for the top ten automatically include the latest reporting period field.

#### Parameters

| Parameter Name | Type | Required | Description |
|----------------|------|----------|-------------|
| `stock_code` | string | ✅ | Full stock code, multiple codes separated by English commas |

#### Indicators Included (36 items)

Total shares, depository receipt ratio, total A-shares (including circulating/restricted A-shares, ex-rights), total B-shares (including circulating/restricted), NEEQ shares, Hong Kong-listed shares, overseas-listed shares, free-floating shares, total circulating/restricted shares, non-circulating shares before share reform, **top ten shareholders** (name/number of shares/market value/shareholding ratio/nature of shares/shareholder nature/institution type), **top ten circulating shareholders** (name/number of shares/ratio/nature of shares), total number of shares held by the top ten shareholders, **total shareholding ratio of the top ten shareholders**, total number of shares/proportion held by the top ten circulating

**Official site: ** [https://www.wanxingai.com/](https://www.wanxingai.com/)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `finance`
- Tags: `finance`, `developer tools`, `search`, `金融服务`, `chinese`

## MCP Configuration

- Transport: `http`
- Command: ``
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/caiweige-yiyanstock.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
