---
title: "th-express-query"
description: "Supports tracking services for thousands of courier companies worldwide, including major ones like SF Express, YTO Express, and STO Express. Automatically identifies the courier company and tracking n…"
---

# th-express-query

Supports tracking services for thousands of courier companies worldwide, including major ones like SF Express, YTO Express, and STO Express. Automatically identifies the courier company and tracking n…

# Tonghu - Nationwide Express Inquiry MCP Service Documentation

## What is the Tonghu - Nationwide Express Inquiry MCP Service?
The Tonghu Nationwide Express Inquiry MCP Server provides the following core functionalities:
- Nationwide express inquiry

Service Features:
- **Comprehensive Coverage**: Supports tracking services for over a thousand global courier companies, including major ones like SF Express, YTO Express, and STO Express.
- **Real-time Updates**: Official data sources are dynamically updated
- **Precise Inquiry**: Supports precise inquiries through express waybill numbers
- **Return Fields**: Returns detailed express logistics information such as logistics status and logistics trajectory.

---

## How to Use the Tonghu - Nationwide Express Inquiry MCP Service?
### API Key Acquisition
1. Register and log in to the [Tonghu MCP Platform](https://mcp.tonghu.top "Tonghu MCP")
2. Create your API Key (if already created, you can use it directly)
3. Activate the [Nationwide Express Inquiry] service in the [Product Center](https://mcp.tonghu.top/#/layout/prodCenter "Tonghu MCP")

### Deployment Method 1 (SSE)
json
{
  "mcpServers": {
    "TH_MCP": {
      "url": "https://mcp.tonghu.top/sse?apiKey=Your apiKey obtained from the Tonghu MCP platform"
    }
  }
}

### Deployment Method 2 (Streamable Http)
json
{
  "mcpServers": {
    "TH_MCP": {
      "url": "https://mcp.tonghu.top/streamable?apiKey=Your apiKey obtained from the Tonghu MCP platform"
    }
  }
}

> **Note**:
- The service is now supported for integration into agents and workflows.

---

## Use Cases of the Tonghu - Nationwide Express Inquiry MCP Service

1. **Automated Customer Service Response for Logistics Issues**  
   After a user places an order, the system automatically generates an order and associates it with an express waybill number. The customer service AI calls the MCP express inquiry interface to display real-time logistics dynamics.

2. **Integration with Internal Logistics Management Systems**  
   Integrate the MCP express inquiry service into internal WMS or ERP systems. Batch query the logistics status of multiple express waybill numbers for report analysis, anomaly alerts, etc.

---

## Frequently Asked Questions

**Q: Is there a fee for using the Tonghu - Nationwide Express Inquiry MCP Service?**  
A: There is a free trial quota upon first activation. Once the quota is exhausted, you can choose:
- Purchase a package (limited-time offer)
- Recharge balance and pay per use
- For large volumes, contact customer service for additional discounts

**Q: What should I be aware of when using the Tonghu - Nationwide Express Inquiry MCP Service?**  
A: For first-time users, please:
1. Log in to the [Tonghu MCP Platform](https://mcp.tonghu.top "Tonghu MCP") and register an account with your phone number
2. Create an API Key
3. Activate the service in the Product Center (additional packages can be purchased)

> **Technical Support**  
Contact platform customer service or Mr. Wang: 18363092551 (WeChat ID same)

**Official site: ** [https://mcp.tonghu.top](https://mcp.tonghu.top)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `productivity`
- Tags: `other`, `企业服务`, `快递服务`, `电商服务`, `chinese`

## MCP Configuration

- Transport: `http`
- Command: ``
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/kid1235789-th-express-query.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
