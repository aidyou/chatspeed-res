---
title: "mcp-stockscreen"
description: "Provides comprehensive stock screening capabilities through Yahoo Finance. Enables LLMs to screen stocks based on technical, fundamental, and options criteria, with support for watchlist management an…"
---

# mcp-stockscreen

Provides comprehensive stock screening capabilities through Yahoo Finance. Enables LLMs to screen stocks based on technical, fundamental, and options criteria, with support for watchlist management an…

# StockScreen MCP Server

A Model Context Protocol (MCP) server providing comprehensive stock screening capabilities through Yahoo Finance. Enables LLMs to screen stocks based on technical, fundamental, and options criteria, with support for watchlist management and result storage.

## Features

### Stock Screening
- Technical Analysis Screening
  - Price and volume filters
  - Moving averages (20, 50, 200 SMA)
  - RSI indicators
  - Average true Range (ATR)
  - Trend analysis (1d, 5d, 20d changes)
  - MA distance calculations

- Fundamental Screening
  - Market capitalization filters
  - P/E ratio analysis
  - Dividend yield criteria
  - Revenue growth metrics
  - ETF-specific metrics (AUM, expense ratio)

- Options Screening
  - Implied Volatility (IV) filters
  - Options volume and open interest
  - Put/Call ratio analysis
  - Bid-ask spread evaluation
  - Earnings date proximity checks

### Data Management
- Watchlist Creation and Management
- Screening Result Storage
- Default Symbol Categories
  - Mega Cap (>$200B)
  - Large Cap ($10B-$200B)
  - Mid Cap ($2B-$10B)
  - Small Cap ($300M-$2B)
  - Micro Cap ($200B
- "large_cap": $10B-$200B
- "mid_cap": $2B-$10B
- "small_cap": $300M-$2B
- "micro_cap": <$300M
- "etf": ETF instruments

2. `manage_watchlist`
```python
{
    "action": str,                       # Required: "create", "update", "delete", "get"
    "name": str,                         # Required: watchlist name (1-50 chars, alphanumeric with _ -)
    "symbols": List[str]                 # Required for create/update: list of stock symbols
}
```

3. `get_screening_result`
```python
{
    "name": str                          # Required: name of saved screening result
}
```

## Response Formats

### Technical Screen Response
```python
{
    "screen_type": "technical",
    "criteria": dict,                    # Original criteria used
    "matches": int,                      # Number of matching stocks
    "results": [                         # List of matching stocks
        {
            "symbol": str,
            "price": float,
            "volume": float,
            "rsi": float,
            "sma_20": float,
            "sma_50": float,
            "sma_200": float,
            "atr": float,
            "atr_pct": float,
            "price_changes": {
                "1d": float,             # 1-day price change %
                "5d": float,             # 5-day price change %
                "20d": float             # 20-day price change %
            },
            "ma_distances": {
                "pct_from_20sma": float,
                "pct_from_50sma": float,
                "pct_from_200sma": float
            }
        }
    ],
    "rejected": [                        # List of stocks that didn't match
        {
            "symbol": str,
            "rejection_reasons": List[str]
        }
    ],
    "timestamp": str
}
```
## Usage Prompt for Claude

"I've enabled the stockscreen tools which provide stock screening capabilities. You can use three main functions:

1. Screen stocks with various criteria types:
   - Technical: Price, volume, RSI, moving averages, ATR
   - Fundamental: Market cap, P/E, dividends, growth
   - Options: IV, volume, earnings dates
   - Custom: Combine multiple criteria types

2. Manage watchlists:
   - Create and update symbol lists
   - Delete existing watchlists
   - Retrieve watchlist contents

3. Access saved screening results:
   - Load previous screen results
   - Review matched symbols and criteria

All functions include error handling, detailed market data, and comprehensive responses."

## Requirements

- Python 3.12+
- MCP Server
- yfinance
- pandas
- numpy
- asyncio

## Limitations

- Data sourced from Yahoo Finance with potential delays
- Rate limits based on Yahoo Finance API restrictions
- Options data availability depends on market hours
- Some financial metrics may be delayed or unavailable

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/twolven/mcp-stockscreen/blob/HEAD/LICENSE) file for details.

## Author

Todd Wolven - (https://github.com/twolven)

## Acknowledgments

- Built with the Model Context Protocol (MCP) by Anthropic
- Data provided by [Yahoo Finance](https://finance.yahoo.com/)
- Developed for use with Anthropic's Claude

**Official site: ** [https://github.com/twolven/mcp-stockscreen](https://github.com/twolven/mcp-stockscreen)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `finance`
- Tags: `finance`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `python`
- Args: `path/to/stockscreen.py`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/twolven-stockscreen.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
