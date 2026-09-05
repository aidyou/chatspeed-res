---
title: "hotel-recommend"
description: "🏨 Hotel Search and Intelligent Recommendations The Hotel Search and Intelligent Recommendations MCP service connects large language models with nationwide hotel data, providing real-time hotel search…"
---

# hotel-recommend

🏨 Hotel Search and Intelligent Recommendations The Hotel Search and Intelligent Recommendations MCP service connects large language models with nationwide hotel data, providing real-time hotel search…

🏨 Hotel Search and Intelligent Recommendations

The Hotel Search and Intelligent Recommendations MCP service connects large language models with nationwide hotel data, providing real-time hotel search and recommendation capabilities for AI assistants, travel intelligences, and IDEs like Cursor/Windsurf. A single call completes the entire process from search → details → cancellation policy interpretation, eliminating the need to call multiple tools and significantly saving on tokens.

✨ Core Features

- **One-Call Full Process**: Scene routing → search → details → cancellation policy interpretation, replacing the traditional "search + details + interpretation" three-step process with a single call, greatly saving on tokens.
- **Automatic Scene Recognition**: Automatically detects five types of travel scenarios (business/parent-child/vacation/backpacker/general) and intelligently matches the best filter tags.
- **Three-Tier Price Segmentation**: Searches 20 hotels and categorizes them into three tiers (value-for-money/quality recommendations/luxury experience), each with 4 hotels, totaling 12, to meet different budget needs in one go.
- **Budget Awareness**: When a user specifies a budget (e.g., "under 500"), it automatically returns only hotels within that budget, excluding those that exceed it.
- **Cancellation Policy Interpretation**: Automatically converts raw JSON cancellation rules into human-readable text, such as "cancellation after May 31st incurs a deduction of ¥553".
- **Curated Output**: Returns concise emoji-formatted results, including hotel information, cancellation policies, and booking links, with high information density.

🛠 Tools

**hotel_search_and_recommend**

Hotel Search and Intelligent Recommendations: One call completes scene routing → search → details → cancellation policy interpretation.

Parameters:

| Parameter | Type   | Required | Description |
|-----------|--------|----------|-------------|
| destination | string | ✅ | Destination city/area/landmark, e.g., "Shanghai", "Sanya Haitang Bay" |
| scene | string | ❌ | Travel scenario: business/parent-child/vacation/backpacker/general, default is general. Can also be automatically detected via query |
| check_in | string | ❌ | Check-in date YYYY-MM-DD, defaults to tomorrow if not provided |
| check_out | string | ❌ | Check-out date YYYY-MM-DD, defaults to the day after tomorrow if not provided |
| guests | int | ❌ | Number of guests, default is 1 |
| max_price | int | ❌ | Maximum nightly budget (in CNY), e.g., 500 means under 500 CNY |
| query | string | ❌ | User's original query, used for automatic scene detection |

Automatic Scene Detection:

| Scene | Keywords | Tag Strategy |
|-------|----------|--------------|
| 💼 Business | Business trip/business/office/meeting/business travel | Must-have: business hotel; Preferred: free WiFi/24-hour front desk |
| 👨‍👩‍👧 Parent-Child | Parent-child/family/with kids/taking kids out | Must-have: family-friendly hotel; Preferred: children's playground/children's pool |
| 🌴 Vacation | Vacation/couple/honeymoon/hot spring | Preferred: resort hotel/SPA/outdoor pool |
| 🎒 Backpacker | Budget travel/student/youth hostel/cheap | Preferred: value-for-money hotel; Excluded: adults-only |
| 🏨 General | No matching keywords | No tag filtering |

Example Output:

👨‍👩‍👧 Parent-Child + Vacation Recommendation · Beijing · 2026-06-02 (3 nights) · ¥1431-¥2933/night

💰 Value-for-Money Choice ¥1431-¥1667/night

1. Tibet Hotel Beijing (Bird's Nest Branch) ⭐4 💰¥1431/night
   📍 No. 118, North Fourth Ring East Road
   🏷️ Offers family rooms, room service
   💡 Value-for-money choice, with family rooms
   🔄 Cancellation: Non-refundable, cancellation fee ¥1431
   🔗 https://rollinggo.cn/...

2. Ramada by Wyndham Beijing North ⭐4 💰¥1542/night
   ...

🏨 Quality Recommendations ¥1764-¥1982/night

5. Poly Plaza Hotel Beijing ⭐4 💰¥1764/night
   ...

✨ Luxury Experience ¥2546-¥2933/night

9. Lanzhiz Xi Shan Garden Hotel Beijing ⭐5 💰¥2546/night
   ...

📦 Installation

bash
pip install mcp-rollinggo-hotel

⚙️ MCP Client Configuration

json
{
  "mcpServers": {
    "hotel-recommend": {
      "command": "uvx",
      "args": ["--from", "mcp-rollinggo-hotel==1.3.1", "mcp-rollinggo-hotel"]
    }
  }
}

💡 Ready to use with zero configuration, no API key required, plug-and-play.

📝 Usage Examples

- "Where to stay for a business trip to Shanghai" → Automatically detects the business scenario
- "Where to stay with kids in Sanya" → Automatically detects the parent-child scenario
- "Cheap hotels in Hangzhou" → Automatically detects the backpacker scenario
- "Hotels in Beijing under 500" → Automatically filters, returning only those under 500
- "Help me find a hotel in Beijing" → General scenario

📄 License

MIT License

**Official site: ** [https://pypi.org/project/mcp-rollinggo-hotel/](https://pypi.org/project/mcp-rollinggo-hotel/)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `search`, `developer tools`, `location services`, `酒店推荐`, `酒店搜索`, `酒店预订`, `酒店查询`, `酒店价格`, `订酒店`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `mcp-rollinggo-hotel==1.5.1`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/mako2026-hotel-recommend.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
