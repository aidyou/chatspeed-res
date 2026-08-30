---
title: "一言选股"
description: "金融数据 MCP 工具集 基于 HTTP API 封装，提供 A 股全链路金融数据查询能力。 共 20 个 MCP 工具，涵盖行情、财务、技术指标、宏观经济、基金估值、交易日历、公告查询等核心场景。 --- 目录 工具名 功能简介 -------------------- 1 getstockcode 股票名称 → 完整代码 2 getstockrealtimequotation A 股实时行情 3 getstockhistoryquotation A 股历史行情 4 gethighfrequencyquotes "
---

# 一言选股

金融数据 MCP 工具集 基于 HTTP API 封装，提供 A 股全链路金融数据查询能力。 共 20 个 MCP 工具，涵盖行情、财务、技术指标、宏观经济、基金估值、交易日历、公告查询等核心场景。 --- 目录 工具名 功能简介 -------------------- 1 getstockcode 股票名称 → 完整代码 2 getstockrealtimequotation A 股实时行情 3 getstockhistoryquotation A 股历史行情 4 gethighfrequencyquotes 

#  金融数据 MCP 工具集

> 基于 HTTP API 封装，提供 A 股全链路金融数据查询能力。  
> 共 **20 个** MCP 工具，涵盖行情、财务、技术指标、宏观经济、基金估值、交易日历、公告查询等核心场景。

---

## 目录

| # | 工具名 | 功能简介 |
|---|--------|---------|
| 1 | [get_stock_code](#1-get_stock_code) | 股票名称 → 完整代码 |
| 2 | [get_stock_real_time_quotation](#2-get_stock_real_time_quotation) | A 股实时行情 |
| 3 | [get_stock_history_quotation](#3-get_stock_history_quotation) | A 股历史行情 |
| 4 | [get_high_frequency_quotes](#4-get_high_frequency_quotes) | 高频（分钟级）行情 |
| 5 | [get_intraday_snapshot](#5-get_intraday_snapshot) | 日内逐笔快照 |
| 6 | [get_date_sequence](#6-get_date_sequence) | 财务/基本面日期序列 |
| 7 | [get_edb_data](#7-get_edb_data) | 宏观经济数据库（EDB） |
| 8 | [get_thematic_report](#8-get_thematic_report) | 专题报表 |
| 9 | [get_fund_realtime_valuation](#9-get_fund_realtime_valuation) | 基金实时估值（分钟频） |
| 10 | [get_fund_daily_valuation](#10-get_fund_daily_valuation) | 基金日最终估值 |
| 11 | [query_trading_dates](#11-query_trading_dates) | 交易日历查询 |
| 12 | [offset_trading_date](#12-offset_trading_date) | 交易日偏移计算 |
| 13 | [search_securities_code](#13-search_securities_code) | 证券代码/名称查询 |
| 14 | [query_announcement](#14-query_announcement) | 上市公司公告查询 |
| 15 | [get_stock_basic_info](#15-get_stock_basic_info) | A 股基本信息摘要（25项） |
| 16 | [get_listed_company_info](#16-get_listed_company_info) | 上市公司基本资料（30项） |
| 17 | [get_stock_equity_shareholder](#17-get_stock_equity_shareholder) | 股本及股东数据（36项） |
| 18 | [get_stock_financial_data](#18-get_stock_financial_data) | 财务三表及衍生指标（300+项） |
| 19 | [get_stock_daily_quotes_tech](#19-get_stock_daily_quotes_tech) | 日行情与技术指标（75项） |
| 20 | [smart_stock_picking](#20-smart_stock_picking) | 智能选股 |

---

## 通用说明

### 股票代码格式

所有涉及股票代码的参数均需带交易所后缀（标准格式）：

| 交易所 | 后缀 | 示例 |
|--------|------|------|
| 上交所 | `.SH` | `600030.SH` |
| 深交所 | `.SZ` | `000001.SZ` |
| 创业板 | `.SZ` | `300033.SZ` |
| 科创板 | `.SH` | `688001.SH` |

多个代码用英文逗号分隔，如：`300033.SZ,600030.SH`

### 日期格式

- 日期参数统一格式：`YYYY-MM-DD`，如 `2025-09-30`
- 时间参数格式：`YYYY-MM-DD HH:mm:ss`，如 `2025-08-25 09:30:00`

### 返回结构

大多数工具返回 JSON 字符串，按 `thscode` 分组，通用格式如下：

```json
[
  {
    "thscode": "300033.SZ",
    "data": [
      {"indicator": "指标英文名", "description": "指标中文名", "value": "值"}
    ]
  }
]
```

---

## 工具详情

---

### 1. `get_stock_code`

**功能**：根据股票中文名称查询对应的完整交易所代码，支持模糊名称纠错。

#### 参数

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `stock_name` | string | ✅ | 股票名称，支持近似输入，如"花大基因"会被纠正为"华大基因" |

#### 返回示例

```json
{
  "name": "花大基因",
  "corrected_name": "华大基因",
  "stock_code": "300676.SZ"
}
```

> `corrected_name` 为系统纠正后的标准名称。

---

### 2. `get_stock_real_time_quotation`

**功能**：获取 A 股股票当前实时行情快照，返回指定的行情字段。

#### 参数

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `stock_code` | string | ✅ | 完整股票代码，如 `601988.SH`，多个用英文逗号分隔 |
| `indicators` | string | ✅ | 需查询的字段，英文逗号分隔（见下方字段列表） |

#### 可用 indicators 字段

| 字段名 | 含义 |
|--------|------|
| `preClose` | 前收盘价 |
| `open` | 开盘价 |
| `high` | 最高价 |
| `low` | 最低价 |
| `latest` | 最新价/当日收盘价 |
| `amount` | 成交额（元） |
| `volume` | 成交量（手） |
| `changeRatio` | 涨跌幅（%） |
| `turnoverRatio` | 换手率（%） |

#### 返回示例

```json
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
```

---

### 3. `get_stock_history_quotation`

**功能**：获取 A 股历史日行情数据（K 线数据），支持多只股票批量查询。

#### 参数

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `stock_code` | string | ✅ | 完整股票代码，多个用英文逗号分隔 |
| `indicators` | string | ✅ | 行情字段，与实时行情相同（见上方字段列表） |
| `startdate` | string | ✅ | 开始日期，格式 `YYYY-MM-DD` |
| `enddate` | string | ✅ | 结束日期，格式 `YYYY-MM-DD` |

> 成交量（`volume`）单位为**手**。

---

### 4. `get_high_frequency_quotes`

**功能**：获取股票/期货/期权高频分钟级行情数据，支持多种周期和复权方式。

#### 参数

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
|--------|------|------|--------|------|
| `stock_code` | string | ✅ | — | 完整股票代码，多个用逗号分隔 |
| `indicators` | string | ✅ | — | 行情字段，英文逗号分隔（open/high/low/close/volume/amount/changeRatio/turnoverRatio） |
| `starttime` | string | ✅ | — | 开始时间，格式 `YYYY-MM-DD HH:mm:ss` |
| `endtime` | string | ✅ | — | 结束时间，格式 `YYYY-MM-DD HH:mm:ss` |
| `interval` | string | ❌ | `"1"` | 周期（分钟）：1 / 3 / 5 / 10 / 15 / 30 / 60 |
| `cps` | string | ❌ | `"no"` | 复权方式：`no`-不复权，`backward1`-后复权，`forward3`-前复权 |

---

### 5. `get_intraday_snapshot`

**功能**：获取股票日内逐笔行情快照，**起止时间必须在同一交易日内**。

#### 参数

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `stock_code` | string | ✅ | 完整股票代码，多个用逗号分隔 |
| `indicators` | string | ✅ | 字段列表，常用：`tradeDate,tradeTime,preClose,open,high,low,latest,vol,amount,bid1,ask1,bidSize1,askSize1` |
| `starttime` | string | ✅ | 开始时间，格式 `YYYY-MM-DD HH:mm:ss` |
| `endtime` | string | ✅ | 结束时间，格式 `YYYY-MM-DD HH:mm:ss`，**须与 starttime 同一天** |

---

### 6. `get_date_sequence`

**功能**：获取股票财务/基本面指标的历史日期序列，如净资产收益率、归母净利润等随时间的变化。

#### 参数

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
|--------|------|------|--------|------|
| `stock_code` | string | ✅ | — | 完整股票代码，多个用逗号分隔 |
| `indicators_json` | string | ✅ | — | 指标列表 JSON 字符串，格式见下方示例 |
| `startdate` | string | ✅ | — | 开始日期，格式 `YYYY-MM-DD` |
| `enddate` | string | ✅ | — | 结束日期，格式 `YYYY-MM-DD` |
| `interval` | string | ❌ | `"D"` | 周期：D-日 / W-周 / M-月 / Q-季 / S-半年 / Y-年 |
| `fill` | string | ❌ | `"Previous"` | 非交易日处理：`Previous`-沿用前值 / `Blank`-空值 |

#### `indicators_json` 示例

```json
[
  {"indicator": "ths_roe_stock", "indiparams": ["20241231"]},
  {"indicator": "ths_net_profit_stock", "indiparams": [""]}
]
```

---

### 7. `get_edb_data`

**功能**：获取宏观经济数据库（EDB）数据，如 GDP、CPI、PMI、社融、M2 等宏观指标。

#### 参数

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `indicators` | string | ✅ | EDB 指标代码，英文逗号分隔，如 `M001620326,M002822183`（可通过超级命令终端查询） |
| `startdate` | string | ✅ | 开始日期，格式 `YYYY-MM-DD` |
| `enddate` | string | ✅ | 结束日期，格式 `YYYY-MM-DD` |
| `startrtime` | string | ❌ | 数据更新时间筛选-开始，格式 `YYYY-MM-DD HH:mm:ss`，可为空 |
| `endrtime` | string | ❌ | 数据更新时间筛选-结束，格式 `YYYY-MM-DD HH:mm:ss`，可为空 |

---

### 8. `get_thematic_report`

**功能**：获取专题报表数据，如 REITs 项目一览、行业专题数据等。报表编码通过命令终端查询获取。

#### 参数

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `reportname` | string | ✅ | 报表编码，如 `p03341`（通过命令终端查询） |
| `functionpara_json` | string | ✅ | 报表筛选参数，JSON 字符串，如 `{"sdate":"20210421","edate":"20211119","xmzt":"全部"}` |
| `outputpara` | string | ✅ | 输出字段控制，格式 `字段名:Y`，如 `"p03341_f001:Y,p03341_f002:Y"` |

---

### 9. `get_fund_realtime_valuation`

**功能**：获取基金实时估值（分钟频），可获取最新或指定时间区间的估值数据。

#### 参数

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
|--------|------|------|--------|------|
| `fund_codes` | string | ✅ | — | 基金代码，英文逗号分隔，如 `000001.OF,000003.OF` |
| `outputpara` | string | ✅ | — | 输出字段，格式 `字段名:Y`（见下方字段列表） |
| `only_latest` | string | ❌ | `"1"` | `"1"`-仅返回最新估值，`"0"`-返回时间区间 |
| `begin_time` | string | ❌ | `""` | 开始时间（`only_latest="0"` 时必填），格式 `YYYY-MM-DD HH:mm:ss` |
| `end_time` | string | ❌ | `""` | 结束时间（`only_latest="0"` 时必填），格式 `YYYY-MM-DD HH:mm:ss` |

#### 可用 outputpara 字段

| 字段名 | 含义 |
|--------|------|
| `changeRatioValuation` | 估值涨跌幅（%） |
| `realTimeValuation` | 实时估值净值 |
| `Deviation30TDays` | 30 交易日均偏差（%） |
| `rank` | 估值涨跌幅排名 |

---

### 10. `get_fund_daily_valuation`

**功能**：获取基金日最终估值（日频），含估值净值、实际净值及偏差率。

#### 参数

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
|--------|------|------|--------|------|
| `fund_codes` | string | ✅ | — | 基金代码，英文逗号分隔，如 `000001.OF,000003.OF` |
| `begin_date` | string | ✅ | — | 开始日期，格式 `YYYY-MM-DD` |
| `end_date` | string | ✅ | — | 结束日期，格式 `YYYY-MM-DD` |
| `outputpara` | string | ❌ | `"finalValuation:Y,netAssetValue:Y,deviation:Y"` | 输出字段：`finalValuation`-日最终估值，`netAssetValue`-日实际净值，`deviation`-偏差率（%） |

---

### 11. `query_trading_dates`

**功能**：查询指定市场交易日历，返回区间内所有交易日期列表或日期数量。

#### 参数

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
|--------|------|------|--------|------|
| `marketcode` | string | ✅ | — | 交易所代码（`212001`-上交所，`212100`-深交所，`212200`-港交所） |
| `startdate` | string | ✅ | — | 开始日期，格式 `YYYY-MM-DD` |
| `enddate` | string | ✅ | — | 结束日期，格式 `YYYY-MM-DD` |
| `date_type` | string | ❌ | `"0"` | `"0"`-交易日，`"1"`-日历日 |
| `period` | string | ❌ | `"D"` | D-日 / W-周 / M-月 / Q-季 / S-半年 / Y-年 |
| `date_format` | string | ❌ | `"0"` | `"0"`-YYYY-MM-DD，`"1"`-YYYY/MM/DD，`"2"`-YYYYMMDD |
| `mode` | string | ❌ | `"1"` | `"1"`-返回日期列表，`"2"`-仅返回日期数量 |

---

### 12. `offset_trading_date`

**功能**：计算基准日期向前/向后偏移若干交易日后的目标日期。

#### 参数

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
|--------|------|------|--------|------|
| `marketcode` | string | ✅ | — | 交易所代码，如 `212001`（上交所） |
| `startdate` | string | ✅ | — | 基准日期，格式 `YYYY-MM-DD` |
| `offset` | string | ✅ | — | 偏移量，前推为负数（如 `"-5"`），后推为正数（如 `"5"`） |
| `period` | string | ❌ | `"D"` | D-日 / W-周 / M-月 / Q-季 / S-半年 / Y-年 |
| `date_type` | string | ❌ | `"0"` | `"0"`-交易日，`"1"`-日历日 |
| `date_format` | string | ❌ | `"0"` | `"0"`-YYYY-MM-DD，`"1"`-YYYY/MM/DD，`"2"`-YYYYMMDD |
| `output` | string | ❌ | `"singledate"` | `"singledate"`-返回单个日期，`"sequencedate"`-返回完整序列 |

---

### 13. `search_securities_code`

**功能**：通过行情代码或证券简称查询标准代码，支持模糊/精确匹配。

#### 参数

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
|--------|------|------|--------|------|
| `query` | string | ✅ | — | 查询内容：行情代码（如 `"000001"`）或证券简称（如 `"平安银行"`） |
| `mode` | string | ❌ | `"seccode"` | `"seccode"`-按代码查，`"secname"`-按名称查 |
| `sectype` | string | ❌ | `""` | 证券类型过滤：`001`-股票，`002`-基金，空-全部 |
| `market` | string | ❌ | `""` | 市场过滤：`212001`-上交所，`212100`-深交所，空-全部 |
| `tradestatus` | string | ❌ | `"0"` | `"0"`-全部，`"1"`-正常交易，`"2"`-已停牌 |
| `isexact` | string | ❌ | `"0"` | `"0"`-模糊匹配，`"1"`-精确匹配 |

---

### 14. `query_announcement`

**功能**：查询上市公司公告，支持按代码或板块查询，可按公告类型和日期范围筛选。

#### 参数

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
|--------|------|------|--------|------|
| `codes` | string | ✅ | — | 证券代码，英文逗号分隔；若按板块查询则传空字符串并配合 `mode` 参数 |
| `outputpara` | string | ✅ | — | 输出字段，格式 `字段名:Y`，如 `"thscode:Y,secname:Y,reportType:Y,title:Y,publishDate:Y"` |
| `report_type` | string | ❌ | `"903"` | 公告类型：`"903"`-全部，`"901002004"`-上市公告书（其他类型见文档） |
| `begin_date` | string | ❌ | `""` | 公告开始日期，格式 `YYYY-MM-DD` |
| `end_date` | string | ❌ | `""` | 公告截止日期，格式 `YYYY-MM-DD` |
| `mode` | string | ❌ | `""` | 按板块查询：`"allAStock"`-全部 A 股，`"allBond"`-全部债券，空-按代码查 |

---

### 15. `get_stock_basic_info`

**功能**：一次性查询 A 股股票 **25 项**静态基础信息。

#### 参数

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `stock_code` | string | ✅ | 完整股票代码，多个用英文逗号分隔 |

#### 包含指标（25项）

股票简称、英文简称、简称首拼、证券曾用名、股票代码、同公司H股信息、同公司美股信息、股票种类、首发上市日期、借壳上市日期、上市交易所、上市板块、上市状态、交易币种、所属概念、是否风险警示板、是否重要指数成分、所属指数权重、是否融资融券标的、是否沪/深港通买入标的、是否次新股、同公司可转债简称。

#### 返回示例

```json
[
  {
    "thscode": "300033.SZ",
    "data": [
      {"indicator": "ths_stock_short_name_stock", "description": "股票简称", "value": "同花顺"},
      {"indicator": "ths_ipo_date_stock", "description": "首发上市日期", "value": "2012-05-18"},
      {"indicator": "ths_listedsector_stock", "description": "上市板块", "value": "创业板"}
    ]
  }
]
```

---

### 16. `get_listed_company_info`

**功能**：查询 A 股上市公司 **30 项**基本资料，包含时变指标（控股股东、行业分类等），支持指定历史时间点查询。

#### 参数

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
|--------|------|------|--------|------|
| `stock_code` | string | ✅ | — | 完整股票代码，多个用英文逗号分隔 |
| `date` | string | ❌ | 今天 | 查询时间点，格式 `YYYY-MM-DD`。控股股东、实际控制人、主营业务、行业分类等时变指标以此日期为准，不传则取当前最新数据 |

#### 包含指标（30项）

公司中/英文名称、成立日期、工商登记号、统一社会信用代码、注册资本及币种、**控股股东**、**控股股东持股比例**、**实际控制人**（含持股比例、类型）、企业类型、法人代表、经营范围、**主营业务**、主营产品名称/类型、竞争公司、可比公司、**所属新证监会行业**（含代码）、**所属申万行业**（含代码）、董事长/财务总监/董事会秘书（现任+历任）。

#### 返回示例

```json
[
  {
    "thscode": "300033.SZ",
    "query_date": "2026-04-01",
    "data": [
      {"indicator": "ths_corp_cn_name_stock", "description": "公司中文名称", "value": "同花顺"},
      {"indicator": "ths_controlling_holder_stock", "description": "控股股东", "value": "易峥"},
      {"indicator": "ths_the_sw_industry_stock", "description": "所属申万行业", "value": "互联网软件与服务"}
    ]
  }
]
```

---

### 17. `get_stock_equity_shareholder`

**功能**：查询 A 股股本结构及股东数据 **36 项**，含前十大股东/流通股东详情。前十大汇总类指标自动附带最新报告期字段。

#### 参数

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `stock_code` | string | ✅ | 完整股票代码，多个用英文逗号分隔 |

#### 包含指标（36项）

总股本、预托证券比例、A 股合计（含流通/限售 A 股、除权）、B 股合计（含流通/限售）、股转系统股、香港上市股、海外上市股、自由流通股、流通/限售股合计、股改前非流通股、**前十大股东**（名称/持股数量/持股市值/持股比例/股份性质/股东性质/机构类型）、**前十大流通股东**（名称/持股数量/比例/股份性质）、前十大股东持股数量合计、**前十大股东持股比例合计**、前十大流通股东持股数量/比例合计。

#### 返回示例

```json
[
  {
    "thscode": "300033.SZ",
    "latest_report_period": "20250930",
    "data": [
      {"indicator": "ths_total_shares_stock", "description": "总股本", "value": 300000000},
      {"indicator": "ths_top10_hlolder_held_ratio_stock", "description": "前十大股东持股比例合计", "value": 62.35}
    ]
  }
]
```

> `latest_report_period` 为前十大股东数据对应的报告期，格式 `YYYYMMDD`，如 `20250930`。

---

### 18. `get_stock_financial_data`

**功能**：一次性查询 A 股财务三表及单季度衍生数据，共 **300+ 项**财务指标，涵盖资产负债表、利润表、现金流量表全科目。

#### 参数

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `stock_code` | string | ✅ | 完整股票代码，多个用英文逗号分隔 |

#### 数据范围（300+ 项）

**资产负债表**：货币资金、应收账款、存货、固定资产、无形资产、商誉、递延税、总资产、负债合计、股东权益合计等全科目（约 130 项）

**利润表**：营业总收入、营业成本、税金及附加、销售/管理/研发/财务费用、资产减值/信用减值损失、投资收益、营业利润、净利润、归母净利润、少数股东损益、基本/稀释 EPS、其他综合收益等（约 70 项）

**现金流量表**：经营/投资/筹资活动现金流入/流出小计及净额、期初/期末现金余额等全科目（约 80 项）

**单季度数据**：上述利润表、现金流量表的单季度拆分版本（约 80 项，字段名含 `_sq_` 前缀）

---

### 19. `get_stock_daily_quotes_tech`

**功能**：查询 A 股指定日期的 **75 项**技术分析指标，默认取今日数据。

#### 参数

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
|--------|------|------|--------|------|
| `stock_code` | string | ✅ | — | 完整股票代码，多个用英文逗号分隔 |
| `date` | string | ❌ | 今天 | 查询日期，格式 `YYYY-MM-DD`，技术指标以该日收盘数据为计算基准 |

#### 涵盖指标分类（75项）

| 分类 | 指标 |
|------|------|
| **行情形态** | 连涨/连跌天数、创历史/阶段新高/新低、N天M板 |
| **均线突破** | 向上/向下有效突破均线、均线多空头排列（看涨看跌） |
| **涨跌停** | 涨停打开日、跌停打开日 |
| **量价技术** | 量比、TAPI、VMA、VMACD、VOSC、VSTD、OBV、PVT、MFI、CR、VR、ARBR、WAD、WVAD |
| **趋势类** | MA、EXPMA、MACD、BBI、DMA、DDI、MTM、TRIX、PRICEOSC、顶底指标（长/中周期） |
| **摆动类** | KDJ、RSI、CCI、BIAS、LWR、WR、ROC、SI、SKDJ、DPO、DBCD、SRDM、VROC、VRSI、B3612、ADTM |
| **通道/波动** | BOLL、BBIBOLL、CDP、SAR、ENV、MIKE、ATR、CVLT、MASS、STD、VHF |
| **强弱类** | JDQS（阶段强势）、JDRS（阶段弱势）、ZDZB（筑底）、DPTB（大盘同步） |
| **动量类** | MI、MICD、RC、RCCD、SRMI |

#### 返回示例

```json
[
  {
    "thscode": "300033.SZ",
    "query_date": "2026-04-01",
    "data": [
      {"indicator": "ths_up_days_stock", "description": "连涨天数", "value": 3},
      {"indicator": "ths_macd_stock", "description": "MACD指数平滑异同平均", "value": 0.12},
      {"indicator": "ths_kdj_stock", "description": "KDJ随机指标", "value": 65.3},
      {"indicator": "ths_boll_stock", "description": "BOLL布林线", "value": 52.80}
    ]
  }
]
```

---

### 20. `smart_stock_picking`

**功能**：用**自然语言**描述选股条件，智能匹配并返回符合条件的证券列表。支持 A 股、港股、美股、基金等多种证券类型。

#### 参数

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
|--------|------|------|--------|------|
| `searchstring` | string | ✅ | — | 自然语言选股描述，例如：`"个股热度最高的前20只A股"`、`"近一个月涨幅超过20%的科技股"`、`"市盈率低于20倍且净利润增速超过30%的消费股"` |
| `searchtype` | string | ❌ | `"stock"` | 证券类型：`stock`-A股，`HK_stock`-港股，`US_stock`-美股，`fund`-基金，`index`-指数，`NEEQ`-新三板 |

#### 使用示例

```
searchstring: "近三个月涨幅超过50%且换手率大于10%的中小盘股"
searchtype: "stock"
```

---

## 错误处理

所有工具在以下情况下会返回对应错误信息：

| 场景 | 返回格式 |
|------|---------|
| Token 无效或余额不足 | `{"status": 401, "message": "错误描述"}` |
| 参数格式错误（如 JSON 解析失败） | `{"status": 400, "message": "错误描述"}` |
| 接口无 tables 字段返回 | 原始响应字符串（便于排查） |

---

## 版本信息

| 属性 | 值 |
|------|----|
| 服务名 | `ExtServer` |
| 协议 | SSE（Server-Sent Events）|
| 默认端口 | `5020` |
| 接入地址 | `http://:5020/sse` |
| 更新日期 | 2026-04-01 |

**官方网站：** [https://www.wanxingai.com/](https://www.wanxingai.com/)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`finance`
- 标签：`finance`, `developer tools`, `search`, `金融服务`, `chinese`

## MCP 配置

- 传输方式：`http`
- 启动命令：``
- 参数：无

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/caiweige-yiyanstock.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
