---
title: "tyc-mcp"
description: "Introduction Tianyancha MCP is an enterprise business information connectivity service officially launched by Tianyancha, aimed at intelligent entities. It allows access to Tianyancha's enterprise dat…"
---

# tyc-mcp

Introduction Tianyancha MCP is an enterprise business information connectivity service officially launched by Tianyancha, aimed at intelligent entities. It allows access to Tianyancha's enterprise dat…

## Introduction

Tianyancha MCP is an enterprise business information connectivity service officially launched by Tianyancha, aimed at intelligent entities. It allows access to Tianyancha's enterprise data capabilities through standard MCP interfaces, covering dimensions such as enterprise entity search, business registration, equity structure, beneficial owners, directors and senior management, operational disclosures, risk litigation, intellectual property, listed company information, bidding and asset disposal. This service is suitable for providing credible data support to intelligent entities involved in corporate verification, customer due diligence, risk investigation, supplier evaluation, investment research, legal compliance, and operational analysis.

## Usage

This MCP Server has been deployed in the cloud. After completing the authentication parameter configuration in ModelScope, users can start using it. The server side is maintained by Tianyancha, and the platform connects via the MCP service address.

## Key Capabilities

- **Enterprise Entity Identification**: Supports searching and anchoring enterprise entities by company name, keywords, or unified social credit code.
- **Enterprise Profile Inquiry**: Returns information such as business registration, registered address, registered capital, establishment date, operational status, contact information, enterprise tags, and enterprise scale.
- **Equity and Relationship Penetration**: Supports queries on shareholders, external investments, branches, actual controllers, beneficial owners, group relationships, and relationship graphs.
- **Risk and Judicial Information**: Covers public risk clues including Tianyancha risk overview, court judgments, case filings, dishonest persons subject to enforcement, administrative penalties, tax arrears, bankruptcy reorganization, and judicial auctions.
- **Operational and Disclosure Information**: Supports inquiries on tax credit, bond issuer ratings, bidding, administrative permits, random inspections, qualification certificates, and core team information.
- **Intellectual Property and Innovation Capability**: Supports inquiries on patents, trademarks, software copyrights, work copyrights, and innovation scores.
- **Personnel Profile**: Supports inquiries on the commercial roles, positions, shareholdings, and related risks of individuals associated with the enterprise.

## Use Cases

- Verification of entities before opening a corporate account, KYB (Know Your Business), supplier onboarding, or signing contracts with partners.
- Due diligence and risk assessment in scenarios such as credit granting, investment and financing, mergers and acquisitions, procurement, and trade financing.
- Supplementing background information in legal compliance, litigation management, contract review, advertising placement, and qualification verification.
- Industry research, competitor analysis, business development, tracking of bidding leads, and building enterprise profiles.

## Authentication and Data Description

To call the Tianyancha MCP, you need to configure authorization parameters. The platform can pass the Tianyancha MCP API Key through the Authorization request header. The specific data scope, return fields, and update frequency are based on the Tianyancha account permissions and the actual online service response.

## FAQ

Q: What types of data can be queried using Tianyancha MCP?
A: The current MCP tool covers major categories such as basic enterprise information, risk and compliance, operational disclosures, intellectual property, historical information, and profiles of directors, supervisors, and senior management. The data is organized in layers based on entity anchoring, summary, details, and specialized capabilities.

Q: Do users need to deploy the server themselves?
A: No. The service is accessed via cloud deployment. Users can start using it after completing the authentication configuration in ModelScope.

Q: How can intelligent entities avoid querying the wrong enterprise?
A: It is recommended to first use the enterprise search tool (`search_companies`) to anchor the entity and confirm the unique entity. Then, use the full company name (or unified social credit code) as the entity parameter to call subsequent tools. If necessary, use `get_company_capabilities` to confirm the available detailed tools for the enterprise before proceeding, which can effectively avoid errors caused by abbreviated names.

**Official site: ** [https://ai.tianyancha.com/](https://ai.tianyancha.com/)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`, `search`, `finance`
- Tags: `finance`, `search`, `developer tools`, `企业信息`, `商业数据`, `商业查询`, `工商信息`, `司法信息`, `行政处罚`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y mcp-remote https://mcp.tianyancha.com/v1 --header Authorization:${YOUR_API_KEY}`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/tianyancha-tyc.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
