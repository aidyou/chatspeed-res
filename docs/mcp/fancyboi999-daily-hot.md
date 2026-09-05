---
title: "daily-hot-mcp"
description: "🔥 Daily Hots 基于 Model Context Protocol (MCP) 协议的全网热点趋势一站式聚合服务 - Python实现"
---

# daily-hot-mcp

🔥 Daily Hots 基于 Model Context Protocol (MCP) 协议的全网热点趋势一站式聚合服务 - Python实现

# 🔥 Daily Hots

One-stop aggregation service for internet hot trends based on the Model Context Protocol (MCP) - Python Implementation

## ✨ Features

- 📊 **One-stop Aggregation** - Aggregates hot news from across the web, covering 30 high-quality data sources
- 🔄 **Real-time Updates** - Keeps the latest trending data in sync with the source sites
- 🧩 **MCP Protocol Support** - Fully compatible with the Model Context Protocol, making it easy to integrate into AI applications
- 🔌 **Easy to Extend** - Add custom data sources with simple configuration
- 🎨 **Flexible Customization** - Easily adjust return fields via environment variables
- 🐍 **Python Implementation** - Developed using Python for better maintainability and scalability
- 🌐 **Multi-field Coverage** - News, social media, tech development, finance and investment, automobiles, lifestyle and consumption, etc.

## 📦 Installation

### Method One: Install from Source Code

bash
git clone https://github.com/fancyboi999/daily-hot-mcp.git
cd daily-hot-mcp
pip install -r requirements.txt
pip install -e .

## 📖 User Guide

### Configure Environment Variables

First, copy the environment variable template file:

bash
cp env.example .env

#### Custom Configuration Options

##### `TRENDS_HUB_CUSTOM_RSS_URL` - Custom RSS Feed URL

Supports adding a custom RSS feed through an environment variable:

bash
TRENDS_HUB_CUSTOM_RSS_URL=https://your-rss-feed-url.com/feed

After configuration, the system will automatically add a `custom-rss` tool to fetch content from the specified RSS feed.

##### `FIRECRAWL_API_KEY` - Web Crawler Service API Key

Used to obtain detailed information about trending topics:

bash
FIRECRAWL_API_KEY=your_api_key_here

This configuration allows the system to crawl the full content of target trending topics, providing richer information. The API key can be obtained from the [FireCrawl official website](https://www.firecrawl.dev/app).

### Running via Command Line

bash
# Run the module directly
python daily_hot_mcp/__main__.py

### MCP Client Configuration

#### JSON Configuration

json
{
  "mcpServers": {
    "daily-news": {
      "type": "http",
      "url": "http://localhost:8000/mcp/"
    }
  }
}

## 🛠️ Supported Tools (30)

### 📰 News Information Category (11)

| Tool Name | Description |
| --- | --- |
| get-baidu-trending | Fetches Baidu Hot Trends, including real-time search trends, social hotspots, technology news, entertainment gossip, and more across multiple Chinese-language fields |
| get-toutiao-trending | Fetches Toutiao Hot Trends, including political news, social events, international news, technological developments, and entertainment gossip across multiple Chinese-language fields |
| get-ithome-trending | Fetches IT Home Hot Trends, including technology news, digital products, internet dynamics, software applications, and cutting-edge technology developments in Chinese-language tech news |
| get-bbc-news | Fetches BBC News, providing global news, UK news, business, politics, health, education, technology, and entertainment information |
| get-36kr-trending | Fetches 36Kr Hot Trends, providing startup, business, and technology news, including investment and financing dynamics, emerging industry analysis, and business model innovation information |
| get-netease-news-trending | Fetches Netease News Hot Trends, including political news, social events, financial information, technological developments, and entertainment and sports news in comprehensive Chinese-language news |
| get-infoq-news | Fetches InfoQ Technical News, including software development, architectural design, cloud computing, AI, and other enterprise-level technical content and cutting-edge developer dynamics |
| get-thepaper-trending | Fetches The Paper Hot Trends, including political news, financial dynamics, social events, cultural education, and in-depth reports in high-quality Chinese-language news |
| get-tencent-news-trending | Fetches Tencent News Hot Trends, including domestic and international current affairs, social hotspots, financial information, entertainment dynamics, and sports events in comprehensive Chinese-language news |
| get-theverge-news | Fetches The Verge News, including technological innovations, digital product reviews, internet trends, and technology company dynamics in English-language tech news |
| get-9to5mac-news | Fetches 9to5Mac Apple-related news, including Apple product launches, iOS updates, Mac hardware, app recommendations, and Apple company dynamics in English-language news |

### 📱 Social Media Hot Trend Category (9)

| Tool Name | Description |
| --- | --- || get-kuaishou-trending | Get Kuaishou trending, including popular short videos, hot topics, and trending content in real-time on the Kuaishou platform |
| get-xiaohongshu-trending | Get Xiaohongshu trending, featuring popular notes, fashion and beauty, lifestyle, and product recommendations on the Xiaohongshu platform |
| get-so360-trending | Get 360 Hot Search, covering popular search terms, real-time news, and highly followed Chinese information on the 360 Search platform |
| get-sogou-trending | Get Sogou Hot Search, including popular search keywords, real-time search trends, and user-focused hot Chinese information on the Sogou Search platform |
| get-hupu-trending | Get Hupu trending, featuring sports events, popular posts from the walking street, basketball and football discussions, and popular Chinese content related to men's lifestyle interests on the Hupu platform |
| get-weibo-trending | Get Weibo trending, covering current affairs, social phenomena, entertainment news, celebrity updates, and widely discussed online topics in real-time |
| get-zhihu-trending | Get Zhihu trending, featuring current affairs, social topics, technology updates, entertainment gossip, and popular Q&A and discussions across multiple fields |
| get-douyin-trending | Get Douyin Hot Search, showcasing the most popular social topics, entertainment events, internet hotspots, and trending topics |
| get-bilibili-trending | Get Bilibili trending videos |

### 🎮 Entertainment and Content Platforms (4)

| Tool Name | Description |
| --- | --- |
| get-bilibili-rank | Get Bilibili video rankings, covering popular videos across the entire site, animation, music, games, and more, reflecting the content consumption trends of young people |
| get-douban-rank | Get Douban real-time hot lists, providing information on currently popular books, movies, TV series, and variety shows, including ratings and popularity data |
| get-weread-rank | Get WeRead rankings, featuring popular novels, bestsellers, new book recommendations, and reading data and ranking information for various literary works |
| get-gcores-new | Get Gcores game-related information, including in-depth content on electronic game reviews, player culture, game development, and gaming peripherals |

### 🚗 Automotive (1)

| Tool Name | Description |
| --- | --- |
| get-autohome-trending | Get Autohome trending, covering automotive news, new car launches, car buying guides, test drive experiences, car reviews, and industry dynamics |

### 🛒 Lifestyle and Consumer (3)

| Tool Name | Description |
| --- | --- |
| custom-rss | Custom RSS feed: your_url_here |
| get-smzdm-rank | Get Smzdm trending, featuring product recommendations, discount information, shopping guides, product reviews, and consumer experience sharing |
| get-sspai-rank | Get Sspai trending, featuring digital product reviews, software application recommendations, lifestyle guides, and productivity tips |

### 🌐 Other Tools (2)

| Tool Name | Description |
| --- | --- |
| crawl_website | Crawl website content, often used when users want to gain a detailed understanding of a specific website's content |
| get-ifanr-news | Get iFanr tech news, covering the latest in tech products, digital devices, and internet trends |

> 💡 **Tip**: More data sources are being continuously added. We are committed to providing you with the most comprehensive trend information!

## 📄 License

MIT License

## 🙏 Acknowledgements

- [DailyHotApi](https://github.com/imsyy/DailyHotApi) - Provided excellent design ideas for trending APIs
- [RSSHub](https://github.com/DIYgod/RSSHub) - Inspiration for RSS aggregation services
- [Model Context Protocol](https://modelcontextprotocol.io/) - MCP protocol specifications
- Thanks to all contributors and users for their support and feedback

---

**🎯 Building the most comprehensive Chinese trend aggregation service, making information easily accessible!**

**Official site: ** [https://github.com/fancyboi999/daily-hot-mcp](https://github.com/fancyboi999/daily-hot-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `research and data`, `chinese`

## MCP Configuration

- Transport: `http`
- Command: ``
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/fancyboi999-daily-hot.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
