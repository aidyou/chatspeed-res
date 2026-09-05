---
title: "AI_Go_Hotel_MCP"
description: "RollingGo Hotel MCP RollingGo— Hotel Search & Booking MCP 🏠 Official Website 🚀 Quick Start 📚 Usage Examples 💬 Technical Support 📚 Integration Video (No Coding Required, Practical Operation) 📚 Integrat…"
---

# AI_Go_Hotel_MCP

RollingGo Hotel MCP RollingGo— Hotel Search & Booking MCP 🏠 Official Website 🚀 Quick Start 📚 Usage Examples 💬 Technical Support 📚 Integration Video (No Coding Required, Practical Operation) 📚 Integrat…

# RollingGo Hotel MCP | RollingGo— Hotel Search & Booking MCP

[![Version](/mcp-assets/b3bf466f985d1cb8019f262681fdd935.svg)](https://github.com/DIDA-AI/DIDA-Hotel-MCP-CN/releases)
[![ModelScope](/mcp-assets/87931ea64ccd51f78d3b55f9a464e457.svg)](https://modelscope.cn/)
[![Calls](/mcp-assets/4b90e8e66c1982cfa0726bd19195d163.svg)](https://github.com/DIDA-AI/DIDA-Hotel-MCP-CN)
[![License: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](/mcp-assets/d52fa8fd608496fb7cb57d905d36fafc.svg)](https://www.python.org/downloads/)

🏠 [Official Website](https://rollinggo.store/) 🚀 [Quick Start](#快速开始) 📚 [Usage Examples](#使用示例) 💬 [Technical Support](#技术支持) 📚 [Integration Video (No Coding Required, Practical Operation)](https://www.xiaohongshu.com/discovery/item/6a22affe0000000017029504?app_platform=ios&app_version=9.33.4&share_from_user_hidden=true&xsec_source=app_share&type=video&xsec_token=CBwWFsJ1iLP0QLjYWHV4RatLComUk4vekr3adma28ssMU=&author_share=1&xhsshare=CopyLink&shareRedId=NzxGN0RLSTo-O0pGTEwzOTszTkBGSUlM&apptime=1782376771&share_id=09ec1dc114174939916826fc8471d07a&code=051iMqFa1D1hXL08HNGa1Eq5Jb3iMqF7&state=wx_oauth)
📚 [Integration Documentation](https://rollinggo.store/docs/mcp-docs/quick-start) · 💰 [Developer Monetization](https://rollinggo.store/docs/partnerdoc/partner1)

## Project Overview
**RollingGo Hotel MCP** provides hotel booking capabilities for AI Agents and MCP clients. It is suitable for developers, Agent builders, travel product teams, and corporate travel scenarios who wish to integrate hotel transaction capabilities into their AI products. Both enterprises and individuals can connect for free with no call volume limits.

🔍 **Intelligent filtering and price comparison** based on needs, making hotel selection hassle-free

📋 Real-time checks on **room types, quotes, and cancellation policies**, ensuring transparency and avoiding pitfalls

🛏️ **Lock in** your preferred room type in advance, eliminating the worry of late bookings

💳 Simply say "place order" to confirm inventory and prices in real-time and **pay directly**

📑 Check order status anytime, ensuring a worry-free experience throughout

💴 Set up 24-hour automatic **price monitoring**, and get **notifications** immediately if there's a price drop

| Service | Endpoint | Available Tools | Authentication |
|---------|----------|-----------------|----------------|
| Hotel MCP | `https://mcp.rollinggo.cn/mcp` | searchHotels, getHotelDetail, getHotelSearchTags | `Authorization: Bearer ` |

- **Transport Protocol**: `streamable-http`
- **Price**: Completely free, with no call volume limits
- **Integration Method**: Self-service integration as per this document, suitable for rapid prototyping and tool development

Dida MCP also offers OAuth 2.0 authorization code mode, providing 7 tools including: getHotelSearchTags, searchHotels, getHotelDetail, hotelPriceConfirm, searchHotelOrders, etc. This mode is suitable for deep integration in enterprise-level production applications and requires business coordination via contact@rollinggo.ai.
> If you are an international user or your target users are from countries outside China, please refer to [Dida-Hotel-MCP-Global](https://github.com/DIDA-AI/Dida-Hotel-MCP-Global). This version supports credit card payments and is suitable for business scenarios outside mainland China.

## MCP Highlights
- ✅ **Real-time Inventory and Price Confirmation** - Direct inventory connection + real-time price confirmation, zero information delay, all query results can be booked directly
- ✅ **Mature Supply Chain Assurance** - The world's third-largest official B2B data source for travel products, with 14 years of supply chain experience, full-link API direct connection
- ✅ **Massive Hotel Coverage** - Access to over 2 million hotels, covering major destinations globally
- ✅ **Directly Signed Hotel Resources** - Over 110,000 directly signed hotels, with real-time price and inventory response, ensuring accurate and bookable query results
- ✅ **Diverse Supply System** - Integration of over 500 global suppliers, covering various hotel brands, meeting different user booking needs
- ✅ **Differentiated Price Advantage** - Anchored to upstream OTA supply, significant price advantages for overseas hotels and popular destinations such as Shanghai, Hong Kong, Japan, and Korea
- ✅ **Compatibility** - Supports over 40 mainstream large model agents including Cursor, Claude Code, Codex, Windsurf, Copilot, etc. For Agent platforms like ClawHub, Kouzi, Qclaw, etc., it also provides an [All-in-One Hotel Booking Skill](https://rollinggo.store/solutions/skills)
- ✅ **Developer Rebate** - Set markup percentages by country upon integration. When users complete bookings through your tool, the corresponding amount will be rebated. Order, revenue, and withdrawal status can be checked in real-time, with flexible withdrawals

## Suitable Users
- Teams or individual developers working on AI Agents
- Developers looking to integrate hotel booking capabilities into MCP Clients
- Developers building travel planning, business travel management, OTA, and lifestyle service agents
- Product teams hoping to validate the commercial transaction loop of AI Agents
- Users with needs for hotel inquiries, price comparisons, and price drop notifications

## Application Scenarios- **Universal Agent**: Enables the Agent to natively handle hotel booking capabilities, allowing users to complete the entire process from price comparison and selection to order creation through natural conversation.
- **AI Travel Assistant**: Precisely recommends hotels based on the user's destination, dates, budget, and personalized preferences, supporting multi-dimensional demand matching.
- **MCP / Agent Demo**: Quickly validate the product capability of "AI Agents directly completing hotel transactions" and create a fully demonstrable closed loop.

## Core Features
- Supports precise search for 6 types of target locations including **city names, popular attractions, transportation hubs, hotel names, and specific addresses**.
- Provides flexible professional filtering functions such as **star rating filters, check-in date settings, accommodation duration configuration, and price range filtering**.
- Offers **personalized recommendations** based on user preferences, generating multi-dimensional professional lists such as high cost-performance, highly-rated popular, and popular selections.
- Full natural language interaction, intelligently completing the entire closed loop from **location parsing, screening and price comparison, personalized recommendations to order generation**.

## Quick Start
> 💡 In summary, you only need to do two things: apply for an API Key + one-click configuration in the AI assistant. Without writing any code, you can enable any MCP-supported AI assistant with hotel search capabilities, and complete your first MCP Tool call within 5 minutes.

### Step 1: Obtain API Key

1. [Click to Apply](https://travelportal-partner-center.dida.com/register?lang=zh)
2. Fill in basic information, no waiting, get it immediately upon application.
3. Why is it necessary to fill in information to apply for a KEY? Hotel prices, inventory, and order capabilities involve real transaction chains, so we need to provide each developer with a dedicated independent KEY. When applying for a KEY, only a small amount of information needs to be filled out. This is mainly to reduce the cost of invalid configurations, protect interface stability, prevent malicious calls or abnormal traffic, and allow us to contact you promptly regarding test orders, price inquiries, and inventory checks.

### Step 2: Integrate Agent Tools

> We recommend using Claude CLI, Codex, and Cursor clients. Other MCP-supported clients (such as Kiro, Doupao, etc.) have similar configuration methods.

### Claude CLI

Create `.mcp.json` in the project root directory:

json
{
  "mcpServers": {
    "DIDA-Hotel": {
      "url": "https://mcp.rollinggo.cn/mcp",
      "type": "http",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}

You can also add it directly via the command line:

bash
claude mcp add \
  --transport http \
  --header "Authorization: Bearer YOUR_API_KEY" \
  DIDA-Hotel \
  https://mcp.rollinggo.cn/mcp

### Codex

Configuration file location: Project root directory `.codex/config.json` or global `~/.codex/config.json`

json
{
  "mcpServers": {
    "DIDA-Hotel": {
      "url": "https://mcp.rollinggo.cn/mcp",
      "type": "streamable-http",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}

### Cursor

Configuration file location: Project root directory `.cursor/mcp.json` or global `~/.cursor/mcp.json`

json
{
  "mcpServers": {
    "DIDA-Hotel": {
      "url": "https://mcp.rollinggo.cn/mcp",
      "type": "streamable-http",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}

> Replace `YOUR_API_KEY` with the actual API Key you received. Hotels and flights use the same authentication method, with the only difference being the URL (`/mcp` vs `/mcp/flight`).

### Direct Testing with cURL

> **Note**: cURL must include the `-H "Accept: application/json, text/event-stream"` header; otherwise, the server will return a 400 error.

bash
curl -X POST https://mcp.rollinggo.cn/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
      "name": "searchHotels",
      "arguments": {
        "originQuery": "Shanghai Bund five-star hotel",
        "place": "Shanghai Bund",
        "placeType": "attraction",
        "checkInParam": {
          "checkInDate": "2026-06-01",
          "stayNights": 2
        },
        "filterOptions": {
          "starRatings": [5.0]
        },
        "size": 3
      }
    },
    "id": 1
  }'---
## Step 3: First MCP Call

After the configuration is complete, say to your AI assistant:

> "Help me find a five-star hotel near the Bund in Shanghai for check-in the day after tomorrow."

The AI will automatically call the `searchHotels` Tool and return a list of hotels.

### Hotel Search Example

json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": {
    "name": "searchHotels",
    "arguments": {
      "originQuery": "five-star hotel near the Bund in Shanghai",
      "place": "the Bund in Shanghai",
      "placeType": "attraction",
      "checkInParam": {
        "checkInDate": "2026-06-01",
        "stayNights": 2
      },
      "filterOptions": {
        "starRatings": [5.0]
      },
      "size": 3
    }
  },
  "id": 1
}

## Usage Examples
### Example 1: Hotel Price Monitoring
> "Help me monitor the price of this hotel near Xixi Wetland in Hangzhou."

### Example 2: City Hotel Search
> "Help me find recommended hotels with 4 stars or above in Hangzhou for the next three days?"

![showcase1](/mcp-assets/1805e9718782362661722aea3f2b8ed3.png)
![showcase2](/mcp-assets/356dd2f74a890f60a14c09fd6ade3fb0.png)

### Example 3: Search Around Attractions
> "For Qixi Festival in 2026, I want to find a cost-effective hotel near Hong Kong Disneyland."

![showcase3](/mcp-assets/ff25b475c60c8479353f2a0ae3a43df0.png)
![showcase5](/mcp-assets/3635a531c31e164f5e44b58189837765.png)
---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🏙️ **Multi-location Search** | Supports cities, attractions, airports, train stations, subway stations, etc. |
| 📅 **Date Filtering** | Specify check-in date and number of nights |
| ⭐ **Star Rating Filter** | Supports 0-5 star filtering, precise to 0.5 star increments |
| 📍 **Distance Search** | Centered on an attraction, limit the radius (in meters) |
| 🛏️ **Facility Details** | Optional return of hotel facilities and room amenities information |
| 🌐 **Multilingual Support** | Supports Chinese, English, and other language environments |

### Configuration Parameter Explanation

#### Common Core Parameters

| Parameter | Required | Description | Example |
|-----------|----------|-------------|---------|
| place | ✅ | Search location | Hangzhou, Disneyland |
| placeType | ✅ | Location type | City, attraction, airport, subway station, district/county... |
| originQuery | ✅ | Your original request description | Help me find a hotel |
| checkIn | ❌ | Check-in date (yyyy-MM-dd) | 2026-05-01 |
| stayNights | ❌ | Number of nights | 2 |
| starRatings | ❌ | Star rating range | [4, 5] indicates 4-5 stars |
| size | ❌ | Number of results to return (default 10), maximum 20 | 5 |

> Note:
> - The actual fields are based on the data returned by the API; the examples above show only some of the fields.
> - As backend capabilities evolve, fields may be added or adjusted. It is recommended that MCP clients handle these changes by using available fields and ignoring missing ones.

## ❓ Frequently Asked Questions
### Q: Which AI assistants/IDEs are supported?

**A:** Currently supported platforms include:
- Cursor
- Windsurf
- Antigravity
- Claude Desktop
- Cherry studio and other clients that support the MCP protocol

### Q: What information is included in the search results?

**A:** By default, the results include the hotel name, star rating, price, address, booking link, hotel images, and hotel facilities. (Refer to the actual returned data for specifics.)

### Q: Are there any call limits?

**A:** It is currently free to use.

## 🔒 Security and Authentication

### Authentication Methods

| Environment | Authentication Method | Header |
|-------------|-----------------------|--------|
| Remote (cloud) | Bearer Token | \Authorization: Bearer YOUR_API_KEY\ |
| Local service | Secret Key | \X-Secret-Key: YOUR_API_KEY\ |

### Security Recommendations

- Safeguard your API Key and do not hard-code it in your code.
- Use environment variables for managing keys in production.
- Use HTTPS for public network access.

## 🤝 Technical Support
Thank you to every developer for their communication, sharing, and feedback, which makes DIDA's iterations more efficient.

Join the WeChat group, where the core development team will be online to assist with environment setup, API debugging, and help you successfully make your first hotel booking call, ensuring a smooth and fast deployment.

You can get the following in the group:
- ✅ Configuration guidance
- ✅ API / MCP call troubleshooting
- ✅ Explanations of hotel search, pricing, and booking processes
- ✅ Integration suggestions suitable for your business scenario
---Email: [york.lu@dida.com](mailto:york.lu@dida.com)

## ⚠ Appendix: DIDA Hotel MCP (OAuth) v2.3 Update Notes

v2.3 optimizes the order query structure and adds multiple new order detail fields, helping Agents to better handle check-in, payment, and cancellation scenarios. Note: This update is applicable only to the OAuth integration version, not the API Key version described in this document. The OAuth version requires a business connection.

### What changed

#### Unchanged tools (4)

- `getHotelSearchTags` — Retrieve all available hotel filter tags
- `searchHotels` — Search for a list of global hotels based on conditions
- `getHotelDetail` — Get available room types and prices for a specified hotel
- `hotelPriceConfirm` — Lock in the real-time final retail price for the selected room type

#### Modified tools (2)

- `createHotelBookingWithPaymentURL` — Removed the `alipayUrlScene` parameter; `bookingResult.paymentUrl` is now a unified checkout page
- `searchHotelOrders` — Output is streamlined to 9 core fields (`orderNo`, `hotelName`, `roomName`, `orderStatus`, `totalPrice`, etc.), used only for list display; full details are moved to a separate query interface

#### New tools (1)

- `getHotelOrderDetail` — Query complete order details by `orderNo`, including `hotelConfirmationNo`, guest list, bed type, contact phone number, latitude and longitude, payment/cancellation deadline, policy indicators, etc.

#### New fields

- `hotelConfirmationNo` — The actual confirmation number from the hotel, for front desk check-in inquiries
- `stayInfo.bedTypeStr` — Chinese description of the bed type (e.g., `"1张特大床 (1.8m)"`)
- `stayInfo.guestNames` — List of guests' pinyin/English names, for check-in verification
- `priceInfo.paymentDeadline` — Payment deadline (`YYYY-MM-DD HH:mm:ss`), for countdown reminders
- `policyInfo.freeCancelDeadline` — Free cancellation deadline, for determining the refund window
- `policyInfo.isCancelable` — Whether it can still be canceled for free at the current time

#### **Total number of tools**: 7 (6 in V2.2) — 1 new, 2 modified, 4 unchanged.
---
**Made with ❤️ by DIDA Team**

**Official site: ** [https://rollinggo.store/](https://rollinggo.store/)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`, `search`, `data`
- Tags: `search`, `developer tools`, `location services`, `全球酒店预订`, `全球酒店查询`, `酒店分佣`, `酒店mcp`, `旅行mcp`, `酒店预订mcp`, `旅行规划mcp`

## MCP Configuration

- Transport: `http`
- Command: ``
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/yorklu-ai-go-hotel.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
