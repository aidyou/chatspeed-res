---
title: "mcp-trends-hub"
description: "A MCP server that aggregates hot trends and rankings from various Chinese websites and platforms including Weibo, Zhihu, Bilibili, and more."
---

# mcp-trends-hub

A MCP server that aggregates hot trends and rankings from various Chinese websites and platforms including Weibo, Zhihu, Bilibili, and more.

# Trends Hub

[Smithery](https://smithery.ai/server/@baranwang/mcp-trends-hub)
[![NPM Version](/mcp-assets/bba9ad2fb73b4ccc707c784e8897a0a2.svg)](https://www.npmjs.com/package/mcp-trends-hub)
![NPM License](/mcp-assets/5816f652aa1f0cc4eedb21a2f733e09e.svg)

A one-stop aggregation service for hot trends across the web, built on the Model Context Protocol (MCP).

## Example

## Features

- **One-stop aggregation** - aggregates hot news from across the web, with 20+ quality data sources
- **Real-time updates** - keeps hot data in sync with the source sites
- **MCP protocol support** - fully compatible with Model Context Protocol, easy to integrate into AI applications
- **Easy to extend** - add custom RSS sources with simple configuration
- **Flexible customization** - adjust returned fields easily via environment variables

## Usage Guide

First, familiarize yourself with the [MCP](https://modelcontextprotocol.io/introduction) protocol, then add the Trends Hub service using the configuration below.

Different MCP clients may differ in implementation; here are some common configuration examples:

### JSON configuration

```json
{
  "mcpServers": {
    "trends-hub": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-trends-hub@1.6.0"
      ]
    }
  }
}
```

### Command line configuration

```bash
npx -y mcp-trends-hub@1.6.0
```

### Installation

#### Install via Smithery

Install Trends Hub via [Smithery](https://smithery.ai/server/@baranwang/mcp-trends-hub) for Claude Desktop:

```bash
npx -y @smithery/cli install @baranwang/mcp-trends-hub --client claude
```

(The following applies to MCP model clients only)

### Configure environment variables

### `TRENDS_HUB_HIDDEN_FIELDS` - hidden field list

This environment variable controls which fields appear in the returned data:

- Applies to all tools: `{field-name}`, e.g. `cover`
- Applies to a specific tool: `{tool-name}:{field-name}`, e.g. `get-toutiao-trending:cover`

Separate multiple entries with commas, for example:

```jsonc
{
  "mcpServers": {
    "trends-hub": {
      "command": "npx",
      "args": ["-y", "mcp-trends-hub"],
      "env": {
        "TRENDS_HUB_HIDDEN_FIELDS": "cover,get-nytimes-news:description" // hide the cover field for all tools and the description for NYTimes news
      }
    }
  }
}
```

### `TRENDS_HUB_CUSTOM_RSS_URL` - custom RSS feed

Trends Hub supports adding custom RSS sources via environment variables:

```jsonc
{
  "mcpServers": {
    "trends-hub": {
      "command": "npx",
      "args": ["-y", "mcp-trends-hub"],
      "env": {
        "TRENDS_HUB_CUSTOM_RSS_URL": "https://news.yahoo.com/rss" // add the Yahoo News RSS feed
      }
    }
  }
}
```

After configuration, a `custom-rss` tool is added automatically for fetching the specified RSS feed content.

## Supported Tools

| Tool | Description |
| --- | --- |
| get-36kr-trending | Get the 36Kr hot list with hot news in startup, business, and tech, including funding activity, emerging industry analysis, and business model innovation |
| get-9to5mac-news | Get Apple-related news from 9to5Mac, including product launches, iOS updates, Mac hardware, app recommendations, and Apple company news in English |
| get-bbc-news | Get BBC news covering world news, UK news, business, politics, health, education, technology, entertainment, and more |
| get-bilibili-rank | Get the Bilibili video ranking, including popular videos across the whole site, animation, music, games, and other sections, reflecting what younger audiences are consuming |
| get-douban-rank | Get Douban's real-time hot lists with currently popular books, movies, TV series, and variety shows, including ratings and popularity data |
| get-douyin-trending | Get Douyin hot search lists showing the most popular social topics, entertainment events, viral trends, and internet hotspots |
| get-gcores-new | Get gaming news from Gcores, including in-depth video game reviews, player culture, game development, and game merchandise content |
| get-ifanr-news | Get tech news from iFanr, including the latest tech products, digital devices, and internet developments |
| get-infoq-news | Get InfoQ technology news covering software development, architecture design, cloud computing, AI, and other enterprise tech content plus cutting-edge developer updates |
| get-juejin-article-rank | Get the Juejin article ranking with high-quality Chinese tech articles and tutorials on frontend, backend, AI, mobile development, and technical architecture |
| get-netease-news-trending | Get the NetEase News hot list with comprehensive Chinese news covering politics, social events, finance, tech, entertainment, and sports |
| get-nytimes-news | Get New York Times news covering international politics, economics and finance, society and culture, science and technology, and art reviews in high-quality English or Chinese |
| get-smzdm-rank | Get Smzdm hot items with practical Chinese consumer content including product recommendations, deals, shopping guides, product reviews, and shopping experience sharing |
| get-sspai-rank | Get the Sspai hot list with quality Chinese tech and lifestyle content including digital product reviews, software recommendations, lifestyle guides, and productivity tips |
| get-tencent-news-trending | Get the Tencent News hot list with comprehensive Chinese news covering domestic and international affairs, social hotspots, finance, entertainment, and sports |
| get-thepaper-trending | Get the The Paper hot list with high-quality Chinese news covering politics, finance, social events, culture and education, and in-depth reporting |
| get-theverge-news | Get The Verge news covering tech innovation, digital product reviews, internet trends, and tech company news in English |
| get-toutiao-trending | Get the Toutiao hot list with popular Chinese news across politics, social events, international news, tech developments, and entertainment gossip |
| get-weibo-trending | Get the Weibo hot search list with real-time popular Chinese news covering current events, social phenomena, entertainment news, celebrity updates, and hot online topics |
| get-weread-rank | Get the WeRead ranking with reading data and rankings for popular novels, bestsellers, new book recommendations, and various literary works |
| get-zhihu-trending | Get the Zhihu hot list with popular Q&A and discussions in Chinese across current events, social topics, tech news, and entertainment gossip |

More data sources are being added continuously.

## Acknowledgments

- [DailyHotApi](https://github.com/imsyy/DailyHotApi)
- [RSSHub](https://github.com/DIYgod/RSSHub)

**Official site: ** [https://github.com/baranwang/mcp-trends-hub](https://github.com/baranwang/mcp-trends-hub)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `search`, `browser`
- Tags: `search`, `browser automation`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y mcp-trends-hub@1.6.0`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/baranwang-trends-hub.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
