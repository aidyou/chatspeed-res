---
title: "china-stock-mcp"
description: "china-stock-mcp An MCP (Model Context Protocol) server built on akshare-one, providing interfaces for Chinese stock market data. It offers a series of tools to fetch financial information, including h…"
---

# china-stock-mcp

china-stock-mcp An MCP (Model Context Protocol) server built on akshare-one, providing interfaces for Chinese stock market data. It offers a series of tools to fetch financial information, including h…

# china-stock-mcp
[Smithery](https://smithery.ai/server/@xinkuang/china-stock-mcp)
An MCP (Model Context Protocol) server built on [akshare-one](https://github.com/zwldarren/akshare-one), providing interfaces for Chinese stock market data. It offers a series of tools to fetch financial information, including historical stock data, real-time data, news, financial statements, and more.

## 🚀 Core Features

- **Dual Mode Operation**: Supports both stdio local mode and HTTP network mode
- **Rich Financial Data**: Comprehensive access to A/B/H share data
- **Real-Time Data**: Supports real-time stock prices, trading information, etc.
- **Financial Statements**: Balance sheets, income statements, cash flow statements, etc.
- **Technical Indicators**: Automatic calculation and addition of 30+ technical indicators
- **News Data**: Stock-related news and announcements
- **Ease of Use**: Simple configuration for integration with AI assistants (Claude, Cursor, etc.)
- **Data Caching**: Built-in in-memory and disk caching mechanisms to improve data retrieval efficiency and response speed
- **Containerization**: Supports Docker deployment

## 🛠️ Architecture Overview

### Main Components

- `server.py`: The core of the MCP server, defining all tools and data interfaces
- `__main__.py`: Command-line entry point, supporting multiple operation modes
- FastMCP Framework: Handles MCP protocol communication
- akshare-one Library: Provides underlying capabilities for fetching Chinese stock market data
- `cache_utils.py`: Caching utilities, offering in-memory and disk caching functionalities

### Supported Data Sources

- **Data Source Fallback**: Built-in `_fetch_data_with_fallback` mechanism, supporting automatic switching of data sources based on priority. When the primary data source fails or returns empty data, the system will automatically try the backup data source, thereby enhancing the stability and reliability of data acquisition.

- East Money (eastmoney, eastmoney_direct)
- Sina Finance (sina)
- Xueqiu (xueqiu)

## 📋 Available Tools

### 1. `Fetch historical stock price data, supporting multiple data sources and technical indicators` (get_hist_data)

Fetches historical stock price data.

**Parameters:**
- `symbol` (string): Stock code (e.g., '000001')
- `interval` (Literal): Time period: minute, hour, day, week, month, year. Default: day
- `interval_multiplier` (int): Time period multiplier
- `start_date` (string): Start date, format YYYY-MM-DD
- `end_date` (string): End date, format YYYY-MM-DD
- `adjust` (Literal): Adjustment type: none, qfq (pre-adjustment), hfq (post-adjustment). Default: none
- `indicators_list` (string|list): Technical indicators to add, can be a comma-separated string (e.g., 'SMA,EMA') or a list of strings (e.g., ['SMA', 'EMA']). Supported indicators include: SMA, EMA, RSI, MACD, BOLL, STOCH, ATR, CCI, ADX, WILLR, AD, ADOSC, OBV, MOM, SAR, TSF, APO, AROON, AROONOSC, BOP, CMO, DX, MFI, MINUS_DI, MINUS_DM, PLUS_DI, PLUS_DM, PPO, ROC, ROCP, ROCR, ROCR100, TRIX, ULTOSC. Commonly used indicators: SMA, EMA, RSI, MACD, BOLL, STOCH, OBV, MFI. It is recommended not to exceed 10.
- `output_format` (Literal): Output data format: json, csv, xml, excel, markdown, html. Default: json

### 2. `Fetch real-time stock price data, supporting multiple data sources` (get_realtime_data)

Fetches real-time stock price data. Supported data sources include: eastmoney, eastmoney_direct, xueqiu.

**Parameters:**
- `symbol` (string): Stock code (e.g., '000001')
- `output_format` (Literal): Output data format: json, csv, xml, excel, markdown, html. Default: json

### 3. `Fetch stock-related news data` (get_news_data)

Fetches stock-related news data.

**Parameters:**
- `symbol` (string): Stock code (e.g., '000001')
- `output_format` (Literal): Output data format: json, csv, xml, excel, markdown, html. Default: json

### 4. `Fetch company balance sheet data` (get_balance_sheet)

Fetches company balance sheet data.

**Parameters:**
- `symbol` (string): Stock code (e.g., '000001')
- `output_format` (Literal): Output data format: json, csv, xml, excel, markdown, html. Default: json

### 5. `Fetch income statement data for a specified stock code` (get_income_statement)

Fetches company income statement data.

**Parameters:**- `symbol` (string): Stock code (e.g., '000001')
- `output_format` (Literal): Output data format: json, csv, xml, excel, markdown, html. Default: json

### 6. `Get the cash flow statement data of the company with the specified stock code` (get_cash_flow)

Retrieve the cash flow statement data of a company.

**Parameters:**
- `symbol` (string): Stock code (e.g., '000001')
- `output_format` (Literal): Output data format: json, csv, xml, excel, markdown, html. Default: json

### 7. `Get the fund flow data for the last 100 trading days of a stock` (get_fund_flow)

Retrieve the fund flow data for the last 100 trading days of a stock.

**Parameters:**
- `symbol` (string): Stock code (e.g., '000001')
- `output_format` (Literal): Output data format: json, csv, xml, excel, markdown, html. Default: json

### 8. `Get the insider trading data of the company` (get_inner_trade_data)

Retrieve the insider trading data of a company.

**Parameters:**
- `symbol` (string): Stock code (e.g., '000001')
- `output_format` (Literal): Output data format: json, csv, xml, excel, markdown, html. Default: json

### 9. `Get key financial indicators from the three major financial statements` (get_financial_metrics)

Retrieve key financial indicators from the three major financial statements.

**Parameters:**
- `symbol` (string): Stock code (e.g., '000001')
- `output_format` (Literal): Output data format: json, csv, xml, excel, markdown, html. Default: json

### 10. `Get current time (ISO format, timestamp) and the most recent trading day` (get_time_info)

Retrieve the current time (in ISO format, timestamp) and the most recent trading day.

**Parameters:** None

### 11. `Get basic summary information of the specified stock` (get_stock_basic_info)

Retrieve basic summary information of a stock, supporting A-shares and Hong Kong stocks.

**Parameters:**
- `symbol` (string): Stock code (e.g., '000001')
- `output_format` (Literal): Output data format: json, csv, xml, excel, markdown, html. Default: json

### 12. `Get single macroeconomic indicator data` (get_macro_data)

Retrieve single macroeconomic indicator data.

**Parameters:**
- `indicator` (Literal): The macroeconomic indicator to retrieve. Supported indicators include: money_supply, gdp, cpi, pmi, stock_summary. Default: 'gdp'
- `output_format` (Literal): Output data format: json, csv, xml, excel, markdown, html. Default: json

### 13. `Analyze the investment sentiment of retail and institutional investors` (get_investor_sentiment)

Analyze the investment sentiment of retail and institutional investors.

**Parameters:**
- `symbol` (string): Stock code (e.g., '000001')
- `output_format` (Literal): Output data format: json, csv, xml, excel, markdown, html. Default: json

### 14. `Get shareholder information of the specified stock` (get_shareholder_info)

Retrieve shareholder information.

**Parameters:**
- `symbol` (string): Stock code (e.g., '000001')
- `output_format` (Literal): Output data format: json, csv, xml, excel, markdown, html. Default: json

### 15. `Get the main products or business composition of the specified stock company` (get_product_info)

Retrieve product information.

**Parameters:**
- `symbol` (string): Stock code (e.g., '000001')
- `output_format` (Literal): Output data format: json, csv, xml, excel, markdown, html. Default: json

### 16. `Get the performance forecast data of the stock, including forecasted annual net profit and earnings per share` (get_profit_forecast)

Retrieve the performance forecast data of a stock.

**Parameters:**
- `symbol` (string): Stock code (e.g., '600519')
- `output_format` (Literal): Output data format: json, csv, xml, excel, markdown, html. Default: json

### 17. `Get dividend and bonus details` (get_stock_fhps_detail)

Retrieve the dividend and bonus details of a specified stock.

**Parameters:**
- `symbol` (string): Stock code (e.g., '000001')
- `output_format` (Literal): Output data format: json, csv, xml, excel, markdown, html. Default: json

### 18. `Get chip distribution data` (get_stock_cyq)

Retrieve the chip distribution data of a specified stock.

**Parameters:**
- `symbol` (string): Stock code (e.g., '000001')
- `date` (string): Query date in YYYY-MM-DD format- `output_format` (Literal): Output data format: json, csv, xml, excel, markdown, html. Default: json
### 19. `Get stock research reports` (get_stock_research_report)

Retrieve the research report data for a specified stock.

**Parameters:**
- `symbol` (string): Stock code (e.g., '000001')
- `output_format` (Literal): Output data format: json, csv, xml, excel, markdown, html. Default: json

### 20. `Get circulating shareholder data` (get_stock_circulate_stock_holder)

Retrieve the circulating shareholder data for a specified stock.

**Parameters:**
- `symbol` (string): Stock code (e.g., '000001')
- `output_format` (Literal): Output data format: json, csv, xml, excel, markdown, html. Default: json

### 21. `Get management change data` (get_stock_management_change)

Retrieve the management change data for a specified stock.

**Parameters:**
- `symbol` (string): Stock code (e.g., '000001')
- `output_format` (Literal): Output data format: json, csv, xml, excel, markdown, html. Default: json

### 22. `Get restricted-share release data` (get_stock_restricted_release_queue)

Retrieve the restricted release data for a specified stock.

**Parameters:**
- `symbol` (string): Stock code (e.g., '000001')
- `output_format` (Literal): Output data format: json, csv, xml, excel, markdown, html. Default: json

### 23. `Get A-share codes and names` (get_stock_a_code_name)

Retrieve the codes and names of all A-share stocks.

**Parameters:**
- `output_format` (Literal): Output data format: json, csv, xml, excel, markdown, html. Default: json

### 24. `Get stock valuation data` (get_stock_value)

Retrieve the valuation data for a specified stock.

**Parameters:**
- `symbol` (string): Stock code (e.g., '000001')
- `output_format` (Literal): Output data format: json, csv, xml, excel, markdown, html. Default: json

### 25. `Calculate volatility indicators for a stock` (get_stock_volatility)

Calculate the volatility indicators for a specified stock using minute-level historical market data.
**Parameters:**
- `symbol` (string): Stock code (e.g., '000001')
- `start_date` (string): Start date
- `end_date` (string): End date
- `period` (int): Time period in minutes (e.g., '1', '5', '15', '30', '60')
- `adjust` (string): Adjustment type: none, qfq (forward adjustment), hfq (backward adjustment). Default: none
- `output_format` (Literal): Output data format: json, csv, xml, excel, markdown, html. Default: json

### 26. `Get codes and basic info of all indices` (get_all_cni_indices)

Retrieve the codes and basic information of all indices, excluding real-time fluctuation data and supporting caching.

**Parameters:**
- `output_format` (Literal): Output data format: json, csv, xml, excel, markdown, html. Default: json

### 27. `Get daily historical market data for an index` (get_cni_index_hist)

Retrieve the daily frequency historical market data for a specified index.

**Parameters:**
- `symbol` (string): Index code (e.g., '399005')
- `start_date` (string): Start date in YYYYMMDD format (e.g., '20230114')
- `end_date` (string): End date in YYYYMMDD format (e.g., '20240114')
- `output_format` (Literal): Output data format: json, csv, xml, excel, markdown, html. Default: json

### 28. `Get constituent stock details of an index` (get_cni_index_detail)

Retrieve the detailed constituent stock samples for a specified index.

**Parameters:**
- `symbol` (string): Index code (e.g., '399001')
- `date` (string): Date in YYYYMM format (e.g., '202404')
- `output_format` (Literal): Output data format: json, csv, xml, excel, markdown, html. Default: json

### 29. `Get technical stock-picking indicators, including new highs, new lows, consecutive rises, consecutive falls, persistent volume increases, persistent volume decreases, upward breakouts, downward breakouts, volume-price double rise, volume-price double fall, and insurance capital stake.` (get_stock_technical_rank)

**Parameters:**- `indicator_name` (string): The name of the technical indicator to be obtained (e.g., New High - Monthly High, New High - Half-Year High, New High - Yearly High, New High - All-Time High, New Low - Monthly Low, New Low - Half-Year Low, New Low - Yearly Low, New Low - All-Time Low, Continuous Rise, Continuous Fall, Persistent Volume Increase, Persistent Volume Decrease, Upward Break - 5-day Moving Average, Upward Break - 10-day Moving Average, Upward Break - 20-day Moving Average, Upward Break - 30-day Moving Average, Upward Break - 60-day Moving Average, Upward Break - 90-day Moving Average, Upward Break - 250-day Moving Average, Upward Break - 500-day Moving Average, Downward Break - 5-day Moving Average, Downward Break - 10-day Moving Average, Downward Break - 20-day Moving Average, Downward Break - 30-day Moving Average, Downward Break - 60-day Moving Average, Downward Break - 90-day Moving Average, Downward Break - 250-day Moving Average, Downward Break - 500-day Moving Average, Volume and Price Both Rising, Volume and Price Both Falling, Insurance Capital Stake)
- `output_format` (Literal): Output data format: json, csv, xml, excel, markdown, html. Default: json

### 30. `Get Real-Time Data for All Industry Sectors` (get_stock_board_industry_summary)
**Parameters:**
- `output_format` (Literal): Output data format: json, csv, xml, excel, markdown, html. Default: json

## 🚀 Installation and Running
### Method One: Using Smithery

Automatically install to Claude Desktop via [Smithery](https://smithery.ai/server/@xinkuang/china-stock-mcp):

bash
npx -y @smithery/cli install @xinkuang/china-stock-mcp


### Method Two: Using Docker

#### 1. Pull the Image
bash
docker pull ghcr.io/xinkuang/china-stock-mcp:latest


#### 2. Run the Container
bash
docker run -p 8081:8081 ghcr.io/xinkuang/china-stock-mcp:latest


### Method Three: Local Source Code Installation

#### 1. Environment Requirements
- Python 3.12+
- Git
- uv (recommended Python package manager)

#### 2. Clone the Repository
bash
git clone https://github.com/xinkuang/china-stock-mcp
cd china-stock-mcp


#### 3. Install Dependencies
bash
# Recommended using uv package manager
uv sync

# Or use pip
pip install -r requirements.txt


#### 4. Run the Server

**Stdio Mode (default, suitable for local MCP clients):**
bash
uv run -m china_stock_mcp


**HTTP Mode (suitable for remote access):**
bash
uv run -m china_stock_mcp --streamable-http --host 0.0.0.0 --port 8081


The server will be available at `http://localhost:8081/mcp`.

## ⚙️ Example MCP Configuration

### Claude Desktop Configuration

Edit `claude_desktop_config.json`:

**Option One: Local Source Code**
json
{
  "mcpServers": {
    "china-stock-mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/china_stock_mcp",
        "run",
        "china-stock-mcp"
      ]
    }
  }
}


**Option Two: Using uvx**
json
{
    "mcpServers": {
        "china-stock-mcp": {
            "command": "uvx",
            "args": [
              "china-stock-mcp"
            ]
        }
    }
}


**Option Three: HTTP Mode**
json
{
  "mcpServers": {
    "china-stock-mcp": {
      "command": "uvx",
      "args": ["china-stock-mcp", "--streamable-http", "--host", "0.0.0.0", "--port", "8081"],
      "env": {
        "MCP_BASE_URL": "http://localhost:8081/mcp"
      }
    }
  }
}


### Other AI Client Configurations

**Cursor:**
json
{
  "mcpServers": {
    "china-stock-mcp": {
      "command": "uvx",
      "args": [ "china-stock-mcp"]
    }
  }
}


**Clion with MCP:**
json
{
  "mcpServers": {
    "china-stock-mcp": {
      "command": "uvx",
    "args": [ "china-stock-mcp"]
    }
  }
}


## 🏃‍♂️ Command Line Arguments

- `--streamable-http`: Enable HTTP streamable mode (default: stdio mode)
- `--host`: Bind host in HTTP mode (default: 0.0.0.0)
- `--port`: Listening port in HTTP mode (default: 8081)

## 📊 Data Coverage

### Stock Markets
- A-shares (Shanghai, Shenzhen)
- B-shares
- H-shares (Hong Kong stocks)
- SME Board, Growth Enterprise Market, NEEQ

### Data Types
- Historical market data (minute, hourly, daily, weekly, monthly, yearly)
- Real-time market data
- Technical indicators calculation- News and Information
- Financial Statements (Balance Sheet, Income Statement, Cash Flow Statement)
- Financial Indicators
- Insider Trading Data

## 🔧 Development and Contribution

### Setting Up the Development Environment

1. Clone the repository
bash
git clone https://github.com/xinkuang/china-stock-mcp
cd china-stock-mcp

2. Install development dependencies
bash
uv sync --dev

3. Enter development mode
bash
uv run -m china_stock_mcp

### Code Structure

src/china_stock_mcp/
├── __init__.py
├── __main__.py    # Command line entry point, handles startup parameters
├── server.py      # MCP server core, defines all tools
├── mcp.json       # MCP configuration specification (optional)
└── py.typed       # Type annotation file

### Adding New Tools

Add new tools in `server.py` using the `@mcp.tool` decorator:

python
@mcp.tool(name="Tool Chinese Name", description="Chinese Description of the Tool")
def your_tool_name(param1: Annotated[str, Field(description="Parameter Description")]) -> str:
    """Detailed description of the tool"""
    # Implementation logic
    pass

## 📝 License

MIT License - See [LICENSE](https://github.com/xinkuang/china-stock-mcp/blob/HEAD/LICENSE) for details

## 🤝 Contribution

Feel free to submit Issues and Pull Requests!

## 🙋‍♂️ Frequently Asked Questions

**Q: Why can't I fetch data?**
A: Please check your internet connection and the availability of the data source. Some data sources may have access restrictions.

**Q: Unable to connect in HTTP mode?**
A: Ensure that port 8081 is not being used by another service and that the firewall allows access to the corresponding port.

**Q: How do I update to the latest version?**
A: If installed via Smithery, updates are automatic. For manual installations, please re-clone the repository code.
## 🐞 Debugging

For detailed instructions on how to debug this server using @modelcontextprotocol/inspector, see DEBUG.md.

**Official site: ** [https://github.com/xinkuang/china-stock-mcp](https://github.com/xinkuang/china-stock-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `finance`
- Tags: `finance`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `china-stock-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/postback-china-stock.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
