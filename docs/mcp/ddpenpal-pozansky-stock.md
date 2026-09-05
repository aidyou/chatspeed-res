---
title: "pozansky-stock-server"
description: "StockAnalysisServer - Intelligent Stock Analysis System Built on the FastMCP framework, this professional stock analysis tool provides comprehensive technical analysis features, including candlestick…"
---

# pozansky-stock-server

StockAnalysisServer - Intelligent Stock Analysis System Built on the FastMCP framework, this professional stock analysis tool provides comprehensive technical analysis features, including candlestick…

# StockAnalysisServer - Intelligent Stock Analysis System

Built on the FastMCP framework, this professional stock analysis tool provides comprehensive technical analysis features, including candlestick pattern recognition, chart pattern detection, technical indicator calculation, and multi-timeframe analysis.

## 🌟 Core Features

### 📊 Multi-Dimensional Technical Analysis
- **Candlestick Pattern Recognition** - Detects over 30 types of patterns, including single, double, and multiple candlestick combinations.
- **Chart Pattern Recognition** - Identifies classic patterns such as head and shoulders, double tops and bottoms, and triangle consolidations.
- **Technical Indicator Calculation** - Computes mainstream indicators like moving averages, RSI, MACD, and Bollinger Bands.
- **Multi-Timeframe Analysis** - Supports 15 timeframes from 1-minute to monthly charts.

### 🌍 Global Market Coverage
- **US Markets** - Major stocks like AAPL, TSLA, GOOGL.
- **Hong Kong Markets** - Stocks like 0700.HK, 0005.HK.
- **China A-Shares** - Main stocks in Shanghai and Shenzhen markets.
- **Global Indices** - S&P 500, NASDAQ, Hang Seng Index, etc.

### 🛠️ Smart Features
- **Automatic Data Source Switching** - Supports multiple data sources with automatic fallback to simulated data.
- **Visualized Charts** - Automatically generates K-line charts with annotated patterns.
- **Confidence Assessment** - Provides a confidence score for each detected pattern.
- **Multi-Timeframe Synergy** - Analyzes technical signals across multiple timeframes simultaneously.

## 🚀 Quick Start

### Basic Usage

python
# Get stock code examples
await get_stock_examples()

# Search for stock symbols
await search_stock_symbols("苹果")

# Single timeframe analysis
await analyze_stock_price("AAPL", "1d")

# Multi-timeframe analysis (recommended)
await analyze_stock_multiple_intervals("AAPL")

# 📈 Supported Analysis Timeframes

## Minute Timeframes
- `1m`, `2m`, `5m`, `15m`, `30m`, `60m`, `90m`

## Hourly Timeframes
- `1h`, `4h`

## Daily and Above Timeframes
- `1d`, `1wk`, `1mo`

## Recommended Combinations
- **Short-term Trading**: 15 minutes + 1 hour + 4 hours
- **Medium-term Investment**: 1 hour + 4 hours + daily
- **Long-term Investment**: 4 hours + daily + weekly

# 🎯 Technical Analysis Features

## Candlestick Pattern Recognition
The system can recognize three major categories of candlestick patterns:

### Single Candlestick Patterns (12 types)
- **Bullish Patterns**: White Marubozu, Hammer, Inverted Hammer, etc.
- **Bearish Patterns**: Black Marubozu, Hanging Man, Shooting Star, etc.
- **Neutral Patterns**: Doji, T-Line, etc.

### Double Candlestick Combinations (7 types)
- Dark Cloud Cover, Piercing Line, Engulfing Pattern, Harami Pattern, etc.

### Multiple Candlestick Combinations (8 types)
- Evening Star, Morning Star, Three White Soldiers, Three Black Crows, etc.

## Chart Pattern Detection

### Continuation Patterns
- Symmetrical Triangle, Ascending Triangle, Descending Triangle
- Flag, Pennant, Rectangle
- Ascending Channel, Descending Channel

### Reversal Patterns
- Head and Shoulders, Inverse Head and Shoulders
- Double Top, Double Bottom
- Triple Top, Triple Bottom
- Rounded Top, Rounded Bottom

### Breakout Patterns
- Channel Breakout, Support/Resistance Breakout

## Technical Indicators

### Trend Indicators
- Moving Averages (MA5, MA10, MA20)
- Exponential Moving Average (EMA)
- MACD
- Bollinger Bands

### Momentum Indicators
- Relative Strength Index (RSI)
- Stochastic Oscillator
- Williams %R
- Commodity Channel Index (CCI)

### Volume Indicators
- Volume Analysis
- On-Balance Volume (OBV)
- Volume Distribution

# 📋 API Reference

## Core Analysis Tools

### `analyze_stock_price(symbol, interval)`
Single timeframe stock analysis

python
await analyze_stock_price("AAPL", "1d")
await analyze_stock_price("0700.HK", "4h")

# 🎨 Output Examples

## Analysis Report Includes
- **Price Information**: Current price, change, volume
- **Pattern Detection**: Candlestick and chart patterns with confidence scores
- **Technical Indicators**: Values and signals of various indicators
- **Visualization**: Path to the annotated K-line chart
- **Time Information**: Analysis time and data timeframe

## Chart Features
- **Color Coding**: Red for bullish candles, green for bearish candles
- **Pattern Annotation**: Automatic marking of detected patterns
- **Confidence Display**: Confidence score for each pattern
- **Multi-Timeframe Comparison**: Pattern distribution across different timeframes

# ⚙️ Technical Architecture

## Core Modules
- **CandlestickPatterns**: Candlestick pattern recognition engine
- **ChartPatterns**: Chart pattern detection algorithms- **TechnicalIndicators**: Technical indicators calculation library
- **StockAnalyzer**: Main analysis coordinator

## Data Source Architecture
- **Primary Data Source**: Yahoo Finance API
- **Fallback Data Sources**: Automatic switching among multiple data sources
- **Degradation Strategy**: Automatically use simulated data in case of network anomalies
- **Caching Mechanism**: Temporary chart file storage

## Error Handling
- **Network Fault Tolerance**: Automatic switching among multiple data sources
- **Data Validation**: Stock code validity check
- **Exception Recovery**: Fallback mechanism using simulated data

# 📝 Usage Recommendations

## Trading Strategy References
1. **Multiple Verifications**: Combine signals from multiple time periods
2. **Pattern Confirmation**: Wait for the pattern to fully form before taking action
3. **Risk Control**: Set stop-loss and target levels
4. **Volume and Price Coordination**: Pay attention to volume confirmation signals

## Best Practices for Analysis
1. **From Large to Small**: Start with long-term cycles, then move to short-term cycles
2. **Multi-Indicator Synergy**: Do not rely on a single indicator
3. **Market Environment**: Consider the overall market trend
4. **Probabilistic Thinking**: Technical analysis is a game of probabilities

# 🔧 Troubleshooting

## Common Issues
1. **Data Retrieval Failure**: The system will automatically continue analysis using simulated data
2. **Chart Generation Failure**: Check temporary directory permissions and disk space
3. **Chinese Display Issues**: The system is configured with Chinese font support

## Performance Optimization
- Adjust the range of analysis time periods
- Reasonably select the number of stocks to focus on
- Regularly clean up temporary chart files

**Official site: ** [https://github.com/pozansky/Stock-server](https://github.com/pozansky/Stock-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `search`, `finance`
- Tags: `finance`, `search`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `pozansky-stock-server`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/ddpenpal-pozansky-stock.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
