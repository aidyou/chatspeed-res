---
title: "RollingGo_Flight"
description: "DaoLiu MCP Global Flight MCP Service Notice of Suspension of Flight MCP Service The Flight MCP is about to undergo an architectural upgrade. The specific schedule is as follows: - Service Suspension T…"
---

# RollingGo_Flight

DaoLiu MCP Global Flight MCP Service Notice of Suspension of Flight MCP Service The Flight MCP is about to undergo an architectural upgrade. The specific schedule is as follows: - Service Suspension T…

# DaoLiu MCP Global Flight MCP Service
Notice of Suspension of Flight MCP Service

The Flight MCP is about to undergo an architectural upgrade. The specific schedule is as follows:

- **Service Suspension Time**: Starting from July 27, 2026, the Flight MCP service will be suspended.
- **Affected Scope**: The Flight Query MCP tool will not be available.
- **Resumption Time**: To be determined; a separate notice will be issued upon resumption. We appreciate your understanding.

- **Target Audience**: Third-party developers, AI Agent builders, and MCP client users
- **Objective**: Complete the first MCP Tool call within 5 minutes and obtain flight query results.
- **Global Flight Booking**: Provides full-process capabilities for querying, comparing prices, and booking flights. Both enterprises and individuals can use it for free with one click.

## Core Advantages
- **Officially Produced, Global Coverage**: 500+ partner airlines, covering 200+ countries and regions, and 1000+ global destinations.
- **Rich Routes**: Millions of route combinations to meet diverse travel needs, supporting direct flights and connecting flights.
- **Price Advantage**: Integrates high-quality flight resources globally, providing more competitive real-time prices.
- **Service Assurance**: Professional team support, 7×24-hour customer service response.
- **Direct Connection to Airline Supply Chain, Early Bird Ticket Inquiry, Automatic Price Alerts**

## Target Users
- Individual users with needs for flight monitoring, hotel queries, and hotel price comparisons.
- Teams or individual developers working on AI Agents.
- Developers who want to integrate flight booking capabilities into MCP clients.
- Developers building travel planning, business travel management, OTA, and lifestyle service agents.
- Product teams looking to validate the commercial transaction loop of AI Agents.

## Application Scenarios
- **General AI Agent**: Enable your large model agent to directly have native flight booking capabilities, allowing users to complete the entire process from understanding needs, intelligent recommendations, price comparisons, to order creation through natural conversation.
- **AI Travel Assistant**: Precisely recommend flights based on the user's departure location, destination, travel date, budget, and personalized preferences, supporting multi-dimensional demand matching.
- **Itinerary Planning Tool**: Seamlessly integrate flight search and booking capabilities into conversational itinerary planning, achieving an integrated "plan and book" experience.
- **MCP / Agent Demo**: Quickly verify the product capability of "AI Agent directly completing flight transactions" and create a demonstrable complete loop.

## Core Features
- Supports precise searches for airports and flight information using various keywords such as city names, airport codes, airline names, and flight numbers.
- Provides flexible settings for departure/return dates, cabin class selection (economy/premium economy/business/first class), passenger configuration, direct/connecting flight filters, and airline preferences.
- Offers personalized recommendations based on user preferences, generating professional lists in multiple dimensions such as cost-effectiveness, fastest arrival, least connections, and popular airlines.
- Full natural language interaction, intelligently completing the entire loop from location parsing, flight queries, price comparisons, personalized recommendations to order generation.
- Real-time synchronization of prices and inventory with supplier data to ensure accurate and bookable query results.

## You Can Have Your Agent Perform the Following Flight-Related Tasks
- Search for flights based on departure location, destination, travel date, and number of passengers.
- Query flight prices, cabin information, and real-time inventory.
- Determine if a flight or cabin is bookable.
- Build AI workflows for flight recommendations, price comparisons, and itinerary planning.
- Integrate flight capabilities into Claude, Cursor, Cherry Studio, ChatGPT MCP Client, or other MCP protocol-supported clients.

- ⚠️ If you are using platforms like ClawHub, Kouzi, or Qclaw, please use our [Rollinggo All-in-One Flight and Hotel Booking Skill](https://modelscope.cn/collections/yorklu/RollingGo-quannengdingjiudianjipiao-Skill). Refer to the [RollingGo Skill Configuration Guide](https://rollinggo.store/docs/skill-docs/skill-config).
---

## 🚀 Quick Start
> 💡 In summary, you only need to do two things: apply for an API Key and configure it in the AI assistant. **No coding required**, and any MCP-supported AI assistant can have flight search capabilities, completing the first MCP Tool call within 5 minutes.

### Step 1: Obtain the API Key

1. [Click to enter the application page](https://mcp.agentichotel.cn/apply)
2. Fill in the basic information, and after automatic approval, you will receive an email containing:
   - Partner Center account (login name + initial password)
   - After logging in, you can configure markup percentages, view orders, and check earnings.
3. ⚠️ Please check your email, including the spam folder, if you do not receive it.To thank the first batch of developers who are willing to try out and act quickly, we are offering a limited-time benefit: **all those who complete their first tool call within 3 days of receiving the API Key will automatically unlock unlimited free calls forever.** We hope to prioritize support for developers who truly have a need and the ability to execute, allowing everyone to experience the full capabilities of the flight MCP at zero cost.

> The email includes both the hotel MCP endpoint and the flight MCP endpoint, and you can access both with a single Key. You may choose to use either or both. We have also listed the [RollingGo Hotel MCP](https://modelscope.cn/mcp/servers/yorklu/AI_Go_Hotel_MCP) product introduction on ModelScope.

**Why is it necessary to fill in information to apply for a KEY?**

Hotel prices, inventory, and order capabilities involve real transaction processes, so we need to provide each developer with a **free, dedicated, and independent KEY**. When applying for a KEY, you only need to fill in a small amount of information, which is mainly for:
- Granting you the appropriate interface permissions for free
- Providing technical support during the integration process
- Determining your use case to reduce the cost of ineffective configurations
- Protecting the stability of the interfaces, avoiding malicious calls or abnormal traffic
- Being able to contact you promptly regarding issues such as test orders, price inquiries, and inventory checks

We will only use this information for KEY activation, integration support, and service security. It will not be shared externally or used for unrelated purposes. If you just want to experience the MCP, you can also specify your testing objectives, and we will try to provide lightweight testing support.

### Step 2: Configure in the AI Assistant

> We recommend using the Claude CLI, Codex, and Cursor clients. The configuration methods for other MCP-supported clients (such as Kiro, Doupao, etc.) are similar.

### Claude CLI

Create a `.mcp.json` file in the root directory of your project:

json
{
  "mcpServers": {
    "RollingGo-Hotel": {
      "url": "https://mcp.rollinggo.cn/mcp",
      "type": "http",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    },
    "RollingGo-Flight": {
      "url": "https://mcp.rollinggo.cn/mcp/flight",
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
  RollingGo-Hotel \
  https://mcp.rollinggo.cn/mcp

claude mcp add \
  --transport http \
  --header "Authorization: Bearer YOUR_API_KEY" \
  RollingGo-Flight \
  https://mcp.rollinggo.cn/mcp/flight

### Codex

Configuration file location: `.codex/config.json` in the root directory of your project or globally at `~/.codex/config.json`

json
{
  "mcpServers": {
    "RollingGo-Hotel": {
      "url": "https://mcp.rollinggo.cn/mcp",
      "type": "streamable-http",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    },
    "RollingGo-Flight": {
      "url": "https://mcp.rollinggo.cn/mcp/flight",
      "type": "streamable-http",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}

### Cursor

Configuration file location: `.cursor/mcp.json` in the root directory of your project or globally at `~/.cursor/mcp.json`

json
{
  "mcpServers": {
    "RollingGo-Hotel": {
      "url": "https://mcp.rollinggo.cn/mcp",
      "type": "streamable-http",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    },
    "RollingGo-Flight": {
      "url": "https://mcp.rollinggo.cn/mcp/flight",
      "type": "streamable-http",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}

> Replace `YOUR_API_KEY` with the actual API Key you received. The authentication method for hotels and flights is the same, with the only difference being the URL (`/mcp` vs `/mcp/flight`).

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
        "originQuery": "上海外滩五星酒店",
        "place": "上海外滩",
        "placeType": "景点",
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
## Step 4: First MCP Call

After the configuration is complete, say to your AI assistant:

> "Help me search for flights from Hangzhou to Beijing." The AI will automatically call the Tool and return a list of flights.

### Flight Search Example (Two Steps)

**Step 1**: Search for airports to get city codes

json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": {
    "name": "searchAirports",
    "arguments": { "keyword": "Hangzhou" }
  },
  "id": 1
}

**Step 2**: Use the city codes to query flights

json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": {
    "name": "searchFlights",
    "arguments": {
      "adultNumber": 1,
      "childNumber": 0,
      "cabinGrade": "ECONOMY",
      "tripType": "ONE_WAY",
      "fromCity": "HGH",
      "toCity": "CTU",
      "fromDate": "2026-06-01"
    }
  },
  "id": 1
}

---

## Step 5: View Results, Demonstration Case

### Flight Search Results (Actual Data)

> Hangzhou → Chengdu, one-way, economy class, **95 flights returned**:

| Flight Number | Route | Time | Price |
|--------|------|------|------|
| CA1741 | Hangzhou Xiaoshan → Chengdu Tianfu | 07:40 - 10:40 | ¥2,869 |
| CZ6198 | Hangzhou Xiaoshan → Wuhan | 13:10 - 15:00 | ¥4,631 |
| CA3338 | Hangzhou Xiaoshan → Shenzhen | 12:55 - 15:15 | ¥5,341 |
---

## Appendix

[mcp tool reference documentation](https://rollinggo.store/docs/mcp-docs/mcp-tool-reference)

### Recommended Call Flow
**Flight Search**

1. User says "Help me search for flights"
2. Call searchAirports → Get city codes
3. Call searchFlights → Return flight list
4. Display to user (⚠️ Prices and inventory change in real-time)

### Frequently Asked Questions

**Q1: Client cannot see Tool after configuration**
1. Check if the JSON configuration format is correct
2. Confirm that `url` and `type` are correct
3. Confirm that the API Key in the `Authorization` header is correct
4. Restart the client (configuration changes require a restart to take effect)

**Q2: Returns 401 Unauthorized**
Invalid or incorrectly formatted API Key:
1. The API Key should start with `mcp_`
2. There should be a space after `Bearer` in `Authorization: Bearer YOUR_API_KEY`
3. Ensure there are no extra spaces or line breaks in the API Key

**Q3: Returns 400 Bad Request**
Common when using cURL directly, check if the Accept header is included:
bash
-H "Accept: application/json, text/event-stream"

**Q4: searchHotels returns empty results**
1. Check if `place` and `placeType` match (e.g., "Shanghai Bund" should be paired with "attraction")
2. Relax the filter conditions (remove star/rating restrictions)
3. Ensure `checkInDate` is not in the past

**Q5: searchFlights returns an error**
1. Confirm that `searchAirports` was called first to get the correct city codes
2. Ensure `fromDate` is not in the past
3. For round trips, `retDate` must be provided

**Q6: Prices do not match actual prices**
The prices in the search results are reference prices, and real-time prices may vary. Currently, only search is supported, and online booking is not available yet.

**Q7: How to obtain an API Key?**
Go to [https://rollinggo.store/apply](https://rollinggo.store/apply) to submit an application. Approval is automatic within 1-3 minutes, and it's free with no limits.

### Access Thresholds and Restrictions

| Item | Description |
|------|------|
| Registration Required | Yes, an application must be submitted on the developer platform |
| API Key Required | Yes, all requests need `Authorization: Bearer 
` |
| Call Limit | No limit |
| Cost | Completely free |
| Review Period | Automatic approval within 1-3 minutes |
| Supported Regions/Currencies | Global hotels and flights, CNY for domestic, USD for overseas |
| Booking Capability | Currently supports search only, online booking is planned |

### Contact Us
Join the WeChat group for technical support
Don't worry about any issues during the integration process! Join our WeChat technical support group, where our core development team will be available to help you with environment setup, API/MCP call troubleshooting, and guide you through your first successful hotel booking call, ensuring a smooth and quick launch.

You can get the following in the group:
- Integration configuration guidance
- API/MCP call issue resolution
- Hotel search, pricing, and booking process explanations
- Integration suggestions tailored to your business scenario
---- 💬 WeChat Group: [Scan to Join](https://raw.githubusercontent.com/young63/dida-picbed/main/groupchat_QR.jpg)

| Other Types | Method |
| ------ | ------ |
| API Key Application | [https://rollinggo.store/apply](https://rollinggo.store/apply) |
| Business Cooperation | contact@rollinggo.cn |
| Partner Center | [https://travelportal-partner-center.dida.com](https://travelportal-partner-center.dida.com) |
| Skill Hub | [https://rollinggo.store/solutions/skills](https://rollinggo.store/solutions/skills) |
| GitHub | [https://github.com/RollingGo-AI/rollinggo-readme](https://github.com/RollingGo-AI/rollinggo-readme) |

---

*Document Version: v1.0*

**Official site: ** [https://rollinggo.store/](https://rollinggo.store/)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `productivity`
- Tags: `search`, `developer tools`, `calendar management`, `机票服务`, `机票查询`, `机票`, `chinese`

## MCP Configuration

- Transport: `http`
- Command: ``
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/yorklu-rollinggo-flight.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
