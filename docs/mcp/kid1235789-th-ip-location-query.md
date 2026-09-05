---
title: "th-ip-location-query"
description: "Query IP attribution information through the IP address, including province, city, and ISP (Internet Service Provider) details. It supports global IP queries and is compatible with IPv4."
---

# th-ip-location-query

Query IP attribution information through the IP address, including province, city, and ISP (Internet Service Provider) details. It supports global IP queries and is compatible with IPv4.

# Tonghu-IP Location Query MCP Service Documentation

## What is the Tonghu-IP Location Query MCP Service?
The Tonghu IP Location Query MCP Server provides the following core functionalities:
- Querying IP location-related information through an IP address.

Service Features:
- **Comprehensive Coverage**: Directly connected to four major carriers, supporting Mobile, Telecom, Unicom, Broadcasting, and virtual numbers.
- **Real-time Updates**: Real-time verification, millisecond response, precise verification.
- **Returned Fields**: Returns carrier, city, province, postal code, and other information.

---

## How to Use the Tonghu-IP Location Query MCP Service?
### API Key Acquisition
1. Register and log in to the [Tonghu MCP Platform](https://mcp.tonghu.top "Tonghu MCP")
2. Create your API Key (if already created, you can use it directly)
3. Enable the [IP Location Query] service in the [Product Center](https://mcp.tonghu.top/#/layout/prodCenter "Tonghu MCP")

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
- The service is now supported for integration into agents and workflows.

---

## Use Cases of the Tonghu-IP Location Query MCP Service

1. **Visitor Geolocation**
   - When a visitor enters the website, the system automatically detects their IP address and calls the MCP IP Location Query interface to obtain location information.
   - Based on the obtained information, dynamically adjust the page language or display relevant content (such as promotions for specific regions).
   - Enhance user experience, increase user engagement, and improve the relevance and appeal of the content.

3. **Security Protection and Fraud Detection**
   - During login or transaction processes, check the user's IP address location in real-time.
   - If the IP address is from a known risky area, trigger additional security verification steps or directly reject the request.
   - Strengthen account security and reduce unauthorized access. Prevent online fraud and other forms of cybercrime.

4. **Digital Marketing and Ad Placement Optimization**
   - Analyze the IP addresses of website visitors to determine their geographical locations and then adjust ad content and placement accordingly.
   - Increase ad click-through rates and conversion rates.
   - More accurately reach potential customer groups.

---

## Frequently Asked Questions

**Q: Is there a cost associated with using the Tonghu-IP Location Query MCP Service?**  
A: There is a free trial quota when you first activate the product. After the quota is exhausted, you can choose:
- Purchase a package (limited-time offer)
- Recharge your balance and pay per use
- For large volumes, contact customer service for customized discounts

**Q: What should I be aware of when using the Tonghu-IP Location Query MCP Service?**  
A: For first-time users, please:
1. Log in to the [Tonghu MCP Platform](https://mcp.tonghu.top "Tonghu MCP") and register an account with your phone number.
2. Create an API Key.
3. Enable the service in the Product Center (additional packages can be purchased).

> **Technical Support**  
Contact platform customer service or Mr. Wang: 18363092551 (same WeChat number)

**Official site: ** [https://mcp.tonghu.top](https://mcp.tonghu.top)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `location services`, `developer tools`, `other`, `运营商`, `电商服务`, `营销`, `chinese`

## MCP Configuration

- Transport: `http`
- Command: ``
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/kid1235789-th-ip-location-query.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
