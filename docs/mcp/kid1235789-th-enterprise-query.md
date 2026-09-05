---
title: "th-enterprise-query"
description: "Tonghu Enterprise Business Information MCP Server provides multiple services including fuzzy search by enterprise name, query of shareholder and executive information, query of enterprise change infor…"
---

# th-enterprise-query

Tonghu Enterprise Business Information MCP Server provides multiple services including fuzzy search by enterprise name, query of shareholder and executive information, query of enterprise change infor…

# Tonghu - Enterprise Business Information MCP Service Documentation

## What is the Tonghu - Enterprise Business Information MCP Service?
The Tonghu Enterprise Business Information MCP Server provides the following core functionalities:
- Fuzzy search for enterprise names
- Querying shareholder and executive information
- Querying enterprise change information
- Querying enterprise business information

Service Features:
- **Comprehensive Coverage**: Integrates core fields such as business registration, shareholder structure, and executive information.
- **Real-time Updates**: Dynamic updates to operational status, telephone numbers, and other data sources.
- **Precise Queries**: Supports queries through any of the following: full company name, registration number, or social credit code.
- **Returned Fields**: Legal representative, registered capital, credit code, registration authority, operational status, telephone number, etc.

---

## How to Use the Tonghu - Enterprise Business Information MCP Service?
### API Key Acquisition
1. Register and log in to the [Tonghu MCP Platform](https://mcp.tonghu.top "Tonghu MCP").
2. Create your API Key (if already created, you can use it directly).
3. Enable the [Enterprise Business Inquiry] service in the [Product Center](https://mcp.tonghu.top/#/layout/prodCenter "Tonghu MCP").

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
- The service supports integration into agents and workflows.

---

## Key Features of the MCP Service

- **Multi-dimensional Data Integration**  
  Covers core fields including business registration, shareholder structure, executive information, and change records. Data sources are updated in real-time (e.g., operational status, telephone numbers).

- **Flexible Input Methods**  
  Supports precise queries via multiple methods such as full company name, registration number, and social credit code. Fuzzy search enhances fault tolerance (e.g., spelling errors or abbreviation matching).

---

## Use Cases for the Tonghu - Enterprise Business Information MCP Service

1. **Enterprise Risk Assessment**  
   AI agents chain-call the "Enterprise Change Information Query" and "Shareholder Information Query" services to analyze risks associated with changes in corporate equity.

2. **Due Diligence for Business Partnerships**  
   Users input the partner company's name, and the system automatically performs a fuzzy search, returning business information, operational status, and executive backgrounds.

3. **Automated Report Generation**  
   Combines MCP services with AI models to automatically generate corporate credit analysis reports (e.g., "Company X has had no administrative penalties in the past year, and its shareholder structure is stable").

---

## Frequently Asked Questions

**Q: Is there a fee for using the Tonghu - Enterprise Business Information MCP Service?**  
A: There is a free trial quota upon first activation. After the quota is exhausted, you can choose from the following options:
- Purchase a package (limited-time offer)
- Recharge balance and pay per use
- For large volumes, contact customer service for additional discounts

**Q: What should I be aware of when using the Tonghu - Enterprise Business Information MCP Service?**  
A: For first-time users, please:
1. Log in to the [Tonghu MCP Platform](https://mcp.tonghu.top "Tonghu MCP") and register an account with your phone number.
2. Create an API Key.
3. Enable the service in the Product Center (additional packages can be purchased).

> **Technical Support**  
Contact platform customer service or Mr. Wang: 18363092551 (WeChat ID same)

**Official site: ** [https://mcp.tonghu.top](https://mcp.tonghu.top)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `productivity`
- Tags: `other`, `企业服务`, `chinese`

## MCP Configuration

- Transport: `http`
- Command: ``
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/kid1235789-th-enterprise-query.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
