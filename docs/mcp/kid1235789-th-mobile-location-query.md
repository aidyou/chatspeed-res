---
title: "th-mobile-location-query"
description: "Pass in the phone number to query the information about the phone number's location, operator, including province, city, postal code, area code, etc. Supports Mobile, Telecom, Unicom, Broadcasting & T…"
---

# th-mobile-location-query

Pass in the phone number to query the information about the phone number's location, operator, including province, city, postal code, area code, etc. Supports Mobile, Telecom, Unicom, Broadcasting & T…

# Tonghu - Mobile Phone Location Query MCP Service Documentation

## What is the Tonghu - Mobile Phone Location Query MCP Service?
The Tonghu Mobile Phone Location Query MCP Server provides the following core functions:
- Querying location information and whether it's a virtual operator through the phone number

Service Features:
- **Comprehensive Coverage**: Directly connected to four major operators, supporting Mobile, Telecom, Unicom, Broadcasting, and virtual numbers
- **Real-time Updates**: Real-time verification, millisecond response, precise verification.
- **Returned Fields**: Returns information such as operator, area, province, postal code, etc.

---

## How to Use the Tonghu - Mobile Phone Location Query MCP Service?
### API Key Acquisition
1. Register and log in to the [Tonghu MCP Platform](https://mcp.tonghu.top "Tonghu MCP")
2. Create your API Key (if already created, you can use it directly)
3. Activate the [Mobile Phone Location Query] service in the [Product Center](https://mcp.tonghu.top/#/layout/prodCenter "Tonghu MCP")

### Deployment Method 1 (SSE)
json
{
  "mcpServers": {
    "TH_MCP": {
      "url": "https://mcp.tonghu.top/sse?apiKey=YourAPIKeyFromTonghuMCPPlatform"
    }
  }
}

### Deployment Method 2 (Streamable Http)
json
{
  "mcpServers": {
    "TH_MCP": {
      "url": "https://mcp.tonghu.top/streamable?apiKey=YourAPIKeyFromTonghuMCPPlatform"
    }
  }
}

> **Note**:
- The service is already supported for integration into intelligent agents and workflows.

---

## Use Cases of the Tonghu - Mobile Phone Location Query MCP Service

1. **Customer Geolocation Verification**
   - After the user enters their phone number during the registration process, the system automatically calls the MCP mobile phone location query interface to obtain the corresponding location information for that number.
   - Enhances account security and reduces false registrations.

2. **Call Location in Customer Support**
   - When an incoming call is received, the system automatically queries the caller's location and displays it to the customer support staff.
   - Supports personalized service recommendations based on the region.

3. **Geographically Targeted Marketing Campaigns**
   - Analyze the user's phone number location and conduct targeted marketing campaigns for specific regions.
   - Improves marketing effectiveness and increases conversion rates.

4. **Risk Control and Fraud Detection**
   - Use the MCP to query the phone number location as one of the additional risk assessment factors, combined with other data (such as IP address) to determine if there are any abnormal behaviors.

---

## Frequently Asked Questions

**Q: Is there a fee for using the Tonghu - Mobile Phone Location Query MCP Service?**  
A: There is a free trial quota when you first activate the product. Once the quota is exhausted, you can choose:
- Purchase a package (limited time offer)
- Recharge and pay per use
- For large volumes, contact customer service for additional discounts

**Q: What should I be aware of when using the Tonghu - Mobile Phone Location Query MCP Service?**  
A: For first-time users, please:
1. Log in to the [Tonghu MCP Platform](https://mcp.tonghu.top "Tonghu MCP") and register an account with your phone number
2. Create an API Key
3. Activate the service in the Product Center (additional packages can be purchased)

> **Technical Support**  
Contact platform customer service or Mr. Wang: 18363092551 (WeChat ID same as phone number)

**Official site: ** [https://mcp.tonghu.top](https://mcp.tonghu.top)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `location services`, `other`, `developer tools`, `企业服务`, `运营商`, `chinese`

## MCP Configuration

- Transport: `http`
- Command: ``
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/kid1235789-th-mobile-location-query.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
