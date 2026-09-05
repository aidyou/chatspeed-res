---
title: "taobao-selection"
description: "🛒 Taobao Selection MCP service for searching and recommending quality products on Taobao. Input your shopping needs, and get a selection of high-quality goods. Users can click on the short link to mak…"
---

# taobao-selection

🛒 Taobao Selection MCP service for searching and recommending quality products on Taobao. Input your shopping needs, and get a selection of high-quality goods. Users can click on the short link to mak…

🛒 Taobao Selection

MCP service for searching and recommending quality products on Taobao. Input your shopping needs, and get a selection of high-quality goods. Users can click on the short link to make a purchase.

✨ Core Features

▸ Curated Quality Goods — Only reliable products are recommended, with low-quality items automatically filtered out

▸ Precise Search — Get exactly what you search for, no more results showing accessories when you search for a phone

▸ Final Price Display — Shows the final price after discounts, with coupons automatically applied

▸ Clickable Short Links — Provides promotional short links that can be opened in WeChat or any browser, leading directly to the purchase page on Taobao

▸ Configuration-Ready Access — No need to apply for a Key; just configure in Stdio to start using

🛠 Tools

**search_standard — Standard Product Search**

Search for 3C electronics, home appliances, and other clearly branded and model-specified products, sorted by final price, prioritizing Tmall.

Parameters:

▸ **keyword (required)** — Search keyword, such as "iPhone 16 Pro Max 256G", "Dyson Hair Dryer HD15"

▸ **price_min (optional)** — Minimum price

▸ **price_max (optional)** — Maximum price

▸ **is_tmall (optional)** — Tmall only, default is true

▸ **page (optional)** — Page number, default is 1

**search_lifestyle — Non-Standard Product Search**

Search for clothing, beauty, home furnishings, and other products that rely on sales volume and reputation, sorted by sales volume.

Parameters:

▸ **keyword (required)** — Search keyword, such as "summer dress", "men's sports shoes"

▸ **category (optional)** — Primary category, such as "clothing, shoes, and bags"

▸ **price_min (optional)** — Minimum price

▸ **price_max (optional)** — Maximum price

▸ **is_tmall (optional)** — Tmall only, default is not limited

▸ **page (optional)** — Page number, default is 1

**shop_search — Shop Search**

Search for official brand flagship stores or well-known shops.

Parameters:

▸ **keyword (required)** — Shop name keyword, such as "Uniqlo Official Flagship Store"

▸ **page (optional)** — Page number, default is 1

📝 Usage Examples

▸ "Recommend an iPhone 16 for me" → `search_standard`

▸ "Which robot vacuum is good" → `search_standard`

▸ "How much is the Dyson Hair Dryer HD15" → `search_standard`

▸ "Summer dress recommendation" → `search_lifestyle`

▸ "Men's sports shoes under 200" → `search_lifestyle`, `price_max=200`

▸ "Find the Uniqlo flagship store" → `shop_search`

Applicable Scenarios

▸ AI assistants/smart agents recommending quality products from Taobao to users

▸ Shopping comparison agents searching and comparing prices

▸ Travel/lifestyle agents integrating product recommendation capabilities

▸ Quickly finding product information in an IDE

**Official site: ** [https://pypi.org/project/taobao-selection-mcp/](https://pypi.org/project/taobao-selection-mcp/)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `search`, `development`
- Tags: `search`, `developer tools`, `other`, `淘宝精选`, `淘宝搜索`, `淘宝推荐`, `淘宝购物`, `好货推荐`, `智能购物`, `淘宝mcp`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `taobao-selection-mcp==0.2.3`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/mako2026-taobao-selection.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
