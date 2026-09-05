---
title: "qieman-mcp"
description: "Qieman MCP Server is an AI-specific financial toolkit. It enhances the capabilities of AI LLMs, enabling them to deliver real-time, professional, reliable, and high-quality financial services based on…"
---

# qieman-mcp

Qieman MCP Server is an AI-specific financial toolkit. It enhances the capabilities of AI LLMs, enabling them to deliver real-time, professional, reliable, and high-quality financial services based on…

# Qieman MCP Server

Qieman MCP Server, provided by Yingmi Company, is an AI-specific financial toolkit. It enhances the capabilities of AI LLMs, enabling them to deliver real-time, professional, reliable, and high-quality financial services based on accurate data in vertical fields. The toolkit specializes in mutual fund and investment advisory services, helping AI make more accurate and scientific investment decisions.

With one-click configuration, users can access the toolkit, which enables industry partners and investors to find efficient and convenient solutions to address real financial problems for themselves and their customers.

## Key Features

1. **Precise Financial Data**: Access to the Qieman MCP Server enables users to obtain real-time and accurate financial data, reducing inaccuracies and enhancing reliability.
2. **Comprehensive Investment Research System**: This system integrates the latest insights and summarized information from financial experts to enhance the quality of financial information services.
3. **Advanced Investment Advisory System**: It utilizes professional investment advisory calculation tools and various asset analysis capabilities to create a core competitive advantage in advisory services.
4. **Seamless User Experience**: After initial configuration, services will automatically update and upgrade, ensuring seamless and continuous access to the latest financial tool service packages.

## Tools

| Feature/API name | Description |
|------------------|-------------|
| BatchGetFundsDetail | Batch query detailed information of multiple funds including name, type, size, risk level, manager, establishment date, investment scope, etc. |
| BatchGetFundNavHistory | Batch obtain historical net value data of multiple funds, supporting querying by different time dimensions. |
| GetBatchFundPerformance | Batch obtain performance data of funds including performance analysis indicators and phase returns. |
| BatchGetFundsHolding | Batch obtain holding information of multiple funds including top ten holdings, bond holdings, etc. |
| BatchGetFundsHolderInfo | Batch obtain asset size and holder structure data of funds, including single share data, total share data, and holder structure information. |
| BatchGetFundsFeeRule | Batch obtain fee rules of multiple funds including subscription fee, purchase fee, redemption fee, and operational fee. |
| BatchGetFundTradeRules | Batch obtain trading rules of funds including minimum/maximum purchase amount, expected confirmation date, expected arrival date, fee rules, etc. |
| BatchGetFundTradeLimit | Batch obtain trading limit information of multiple funds including whether the fund is tradable, minimum purchase amount, minimum holding shares, fixed investment starting point, etc. |
| BatchGetFundsSplitHistory | Batch obtain split record information of funds including split date and ratio. |
| BatchGetFundsDividendRecord | Batch obtain dividend record of funds including rights registration date, dividend distribution date, and dividend amount per share. |
| GetFundAnnouncements | Query fund announcements including fund code, name, full name, announcement ID, date, source, title, link, and type. Supports querying by time range, announcement type, and title keywords. |
| SearchFunds | Search funds based on name, code, or other conditions, supporting sorting by return, size, fee, etc. |
| GetPopularFund | Obtain a list of recently popular funds to understand market focus and investment trends. |
| GuessFundCode | Match the closest fund code based on fund name. |
| GetAssetAllocation | Analyze asset allocation of fund portfolios, providing asset class distribution, radar chart scoring, and diagnostic results. |
| GetFundsCorrelation | Analyze correlation coefficients between multiple funds to understand the mutual influence of each fund's trend in the portfolio. |
| GetFundsBackTest | Conduct historical backtesting analysis of a given fund portfolio, calculating key indicators and providing comprehensive diagnostic results and scoring. |
| MonteCarloSimulate | Perform Monte Carlo simulation calculations based on given asset allocation weights to generate expected return distribution, volatility scenarios, and various percentile return data. |
| AnalyzeFundRisk | Obtain risk scores and detailed risk explanations of multiple funds, calculating indicators such as risk score, R-squared, residual variance, standard error, etc. |
| AnalyzePortfolioRisk | Conduct risk assessment analysis of a given fund portfolio, calculating multi-dimensional risk indicators. |
| SearchFinancialNews | Search tool supporting filtering and pagination by keywords and time range, returning detailed news content. |
| SearchManagerViewpoint | Obtain fund manager views and market analysis on various industries, supporting filtering by industry theme, time range, and keywords. |
| GetFundDiagnosis | Provide comprehensive fund diagnostic analysis including recent information, risk and opportunity assessment, industry holdings, asset allocation, performance, etc. |
| DiagnoseFundPortfolio | Provide comprehensive fund portfolio diagnostic analysis including asset allocation analysis, fund correlation analysis, and backtesting diagnosis. |
| GetAssetAllocationPlan | Obtain asset allocation plans based on investment parameters. |
| GetCompositeModel | Obtain corresponding composite models through asset allocation plan IDs. |
| RenderEchart | Render charts based on provided ECharts configuration and convert to images, supporting returning base64 encoded image content or OSS access URLs. |
| RenderHtmlToPdf | Convert HTML content to PDF documents, supporting custom PDF format and margin settings. |
| GetCurrentTime | Obtain the current time of the server, returning a formatted date and time string. |
| GetTxnDayRange | Obtain a list of trading days within a specified period based on the central time, supporting forward and backward specified days. |

## Official Website
https://qieman.com/mcp/landing

## Get Started
1. **Apply for Qieman MCP service**:
   Visit our Qieman MCP official website, log in or register a Qieman account, and fill out the form to get your own API Key.
2. **Use the link to get the services**:
   https://stargate.yingmi.com/mcp/sse?apiKey=[your API Key]

## User Guide
https://qieman.com/mcp/how-to-use

## Contact Us
oap@yingmi.cn

**Official site: ** [https://www.modelscope.cn/mcp](https://www.modelscope.cn/mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `finance`
- Tags: `finance`, `chinese`

## MCP Configuration

- Transport: `http`
- Command: ``
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/qieman-ai-qieman.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
