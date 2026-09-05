---
title: "kuaidi100-mcp"
description: "The Express100 MCP Server provides functions such as querying express delivery information, comparing and estimating express delivery costs, and checking delivery times (including pre-shipment deliver…"
---

# kuaidi100-mcp

The Express100 MCP Server provides functions such as querying express delivery information, comparing and estimating express delivery costs, and checking delivery times (including pre-shipment deliver…

## What is Kuaidi100 MCP Server?

Kuaidi100 MCP Server is the first logistics information service platform in China that is compatible with the MCP protocol, launched by Kuaidi100. The core services of Baidiyun·API Open Platform under Kuaidi100 now fully support the MCP protocol. Developers can quickly access core functions such as parcel tracking, freight estimation, and intelligent delivery time prediction (including full journey and in-transit modes) through simple configuration. Its AI Agent not only significantly lowers the threshold for calling logistics data services during development, improving development efficiency, but also enhances the empowerment of logistics data for various industries, promoting their innovation and development.

## Core Functions

1. **Parcel Tracking**
   - The Kuaidi100 API Open Platform provides the capability to query the tracking information of over 3,000 global logistics companies.
   - Input: Waybill number
   - Output: Logistics tracking information including time nodes and detailed tracking
2. **Freight Estimation**
   - Based on big data analysis by Kuaidi100, it estimates the shipping cost of logistics companies according to the sender and recipient addresses and package weight.
   - Input: Recipient address, sender address, courier company name, package weight
   - Output: Estimated shipping cost
3. **Intelligent Delivery Time Prediction (Full Journey Mode)**
   - Before shipment, it predicts the estimated delivery time for different courier companies based on the sender and recipient addresses.
   - Input: Courier company code, recipient address, sender address
   - Output: Estimated delivery time
4. **Intelligent Delivery Time Prediction (In-Transit Mode)**
   - Utilizing the self-developed AI delivery time prediction model by Kuaidi100, it predicts the delivery time of parcels.
   - Input: Order placement time, logistics tracking information, recipient address, sender address
   - Output: Estimated delivery time

## Key Features of Kuaidi100 MCP Server

1. **Top-Quality Domestic Express Logistics Data**
   - Data originates from the Baidiyun Open Platform, supporting the query of logistics information for over 3,000 global express companies. Focused on the industry for 15 years, it has been chosen by more than 2.5 million enterprise customers.
2. **AI+Data+MCP API Redefined**
   - The AI Agent significantly reduces the threshold for calling logistics data services during development, enhancing development efficiency and empowering various industries with logistics data, thus promoting their innovation and development. Kuaidi100 MCP Server supports integration with any platform that supports the MCP protocol via SSE.
3. **AI+Data Express Map Intelligent Leap, Query Product Renewal**
   - Combining the capabilities of the Kuaidi100 AI large model, billion-scale data cleansing, and express logistics knowledge graph technology, it provides accurate estimated delivery times and routes, elevating parcel tracking from "where is the parcel" to "when will the parcel arrive".
4. **One-Time Configuration, Automatic Iteration**
   - After user configuration, there is no need for repeated operations; the Baidiyun Open Platform continuously updates and iterates its services.

## Use Cases of Kuaidi100 MCP Server

- Query real-time logistics information for order packages
- Compare logistics solutions from different courier companies based on shipping costs and delivery times, intelligently selecting the most suitable courier service
- Query the estimated delivery time of parcels, dynamically updating with logistics tracking and route node information, making the estimated arrival time increasingly accurate as the destination approaches, facilitating users in planning their receipt arrangements in advance

## Frequently Asked Questions

**Q: Is there a fee for using Kuaidi100 MCP Server?**  
A: Users need to register on the [Kuaidi100 API Open Platform](https://api.kuaidi100.com/extend/register?code=d1660fe0390d4084b4f27b19d2feee02) to obtain an API Key. The platform provides each user with a separate free call quota; if the quota is exceeded, users can recharge on the platform. For any questions, please contact:  
Contact Email: api@kuaidi100.com  
Contact Phone: 0755-86719032  

## Kuaidi100 MCP Server (Python)
Install `python` with `uv`, requiring at least version 3.11

bash
uv python install 3.11

### 1. Online Dependency Acquisition and Usage (Recommended)
Use the `uvx` command to get kuaidi100_mcp and use it in one step
json
{
  "mcpServers": {
    "kuaidi100": {
      "command": "uvx",
      "args": [
        "kuaidi100-mcp"
      ],
      "env": {
        "KUAIDI100_API_KEY": ""
      }
    }
  }
}

### 2. Download and Configure Local Project
Create a project with `uv`

bash
uv init mcp_server_kuaidi100

Copy `api_mcp.py` to this directory and test whether the mcp server is running normally with the following command

bash
uv run --with mcp[cli] mcp run {YOUR_PATH}/mcp_server_kuaidi100/api_mcp.py
# If on Mac, add escape characters
uv run --with mcp\[cli\] mcp run {YOUR_PATH}/mcp_server_kuaidi100/api_mcp.pyIf there are no errors, the MCP Server has started successfully.

### Obtain Kuaidi100 API KEY
Log in to Kuaidi100 to obtain your API key: https://api.kuaidi100.com/extend/register?code=d1660fe0390d4084b4f27b19d2feee02 (Be cautious not to leak your authorization key to prevent unauthorized use by others!!!)

### Using in an MCP-supported Client
Add the following content to the MCP Server configuration file and save it:

json
{
  "mcpServers": {
    "kuaidi100": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "mcp[cli]",
        "mcp",
        "run",
        "{YOUR_PATH}/mcp_server_kuaidi100/api_mcp.py"
      ],
      "env": {
        "KUAIDI100_API_KEY": ""
      }
    }
  }
}

### Testing

#### Tracking Query:
![trae_test_queryTrace.png](/mcp-assets/f3b326086e0e093f44f0190cb93cd372.png)
#### Estimated Delivery Time:
![trae_test_estimateTime.png](/mcp-assets/64f86c077a4d95076d80e5addd11c732.png)
#### Estimated Shipping Cost:
![trae_test_estimatePrice.png](/mcp-assets/e07fbf15c219348e5641f87a5056c191.png)

### Tips
To get account information (such as key, customer, secret), or to try out 100 orders for free, please visit the [API Open Platform](https://api.kuaidi100.com/home) and register.

**Official site: ** [https://github.com/kuaidi100-api/kuaidi100-MCP](https://github.com/kuaidi100-api/kuaidi100-MCP)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`, `search`, `browser`, `productivity`, `memory`, `files`, `communication`, `finance`, `media`, `data`
- Tags: `other`, `search`, `browser automation`, `communication`, `developer tools`, `entertainment and media`, `file systems`, `finance`, `knowledge and memory`, `location services`

## MCP Configuration

- Transport: `http`
- Command: ``
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/kuaidi100-kuaidi100.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
