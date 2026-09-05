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
- **Risk and Judicial Information**: Covers public risk clues including Tianyancha risk overview, court judgments, case filings, dishonest被执行人、行政处罚、欠税、破产重整、司法拍卖等公开风险线索。
- **经营与公示信息**：支持纳税信用、债券主体评级、招投标、行政许可、抽查检查、资质证书、核心团队等经营信息查询。
- **知识产权与创新能力**：支持专利、商标、软件著作权、作品著作权、创新力评分等知识产权资产查询。
- **人员画像**：支持企业相关人员的商业角色、任职、持股和相关风险查询。

## 使用场景
- 企业开户、KYB、供应商准入或合作方签约前的主体核验。
- 授信、投融资、并购、采购和贸易融资场景下的尽职调查与风险排查。
- 法务合规、诉讼管理、合同审核、广告投放、资质核验等业务中的背景信息补充。
- 产业研究、竞争对手分析、招商拓客、招投标线索跟踪和企业画像构建。

## 鉴权与数据说明
调用天眼查 MCP 需要配置授权参数。平台侧可通过 Authorization 请求头传入天眼查 MCP API Key。具体可调用的数据范围、返回字段和更新频率以天眼查账号权限及线上服务实际返回为准。

## FAQ
Q：天眼查 MCP 能查询哪些类型的数据？
A：当前 MCP 工具覆盖企业基础信息、风险合规、经营公示、知识产权、历史信息、董监高/人员画像等主要类别，并按实体锚定、概要、明细和专业能力分层组织。

Q：是否需要用户自行部署服务端？
A：不需要。该服务按云端部署方式接入，用户在 Model Scope 中完成鉴权配置后即可调用。

Q：智能体如何避免查错企业？
A：建议先用企业检索工具（search_companies）完成主体锚定，确认唯一主体后，再以企业全名（或统一社会信用代码）作为主体参数调用后续工具；必要时先用 get_company_capabilities 确认该企业可用的明细工具再下钻，可有效避免简称重名导致的查错。

---

## Introduction
Tianyancha MCP is an enterprise business information connectivity service officially launched by Tianyancha, aimed at intelligent entities. It allows access to Tianyancha's enterprise data capabilities through standard MCP interfaces, covering dimensions such as enterprise entity search, business registration, equity structure, beneficial owners, directors and senior management, operational disclosures, risk litigation, intellectual property, listed company information, bidding and asset disposal. This service is suitable for providing credible data support to intelligent entities involved in corporate verification, customer due diligence, risk investigation, supplier evaluation, investment research, legal compliance, and operational analysis.

## Usage
This MCP Server has been deployed in the cloud. After completing the authentication parameter configuration in ModelScope, users can start using it. The server side is maintained by Tianyancha, and the platform connects via the MCP service address.

## Key Capabilities
- **Enterprise Entity Identification**: Supports searching and anchoring enterprise entities by company name, keywords, or unified social credit code.
- **Enterprise Profile Inquiry**: Returns information such as business registration, registered address, registered capital, establishment date, operational status, contact information, enterprise tags, and enterprise scale.
- **Equity and Relationship Penetration**: Supports queries on shareholders, external investments, branches, actual controllers, beneficial owners, group relationships, and relationship graphs.
- **Risk and Judicial Information**: Covers public risk clues including Tianyancha risk overview, court judgments, case filings, dishonest被执行人、行政处罚、欠税、破产重整、司法拍卖等公开风险线索。
- **经营与公示信息**：支持纳税信用、债券主体评级、招投标、行政许可、抽查检查、资质证书、核心团队等经营信息查询。
- **知识产权与创新能力**：支持专利、商标、软件著作权、作品著作权、创新力评分等知识产权资产查询。
- **人员画像**：支持企业相关人员的商业角色、任职、持股和相关风险查询。

## 使用场景
- 企业开户、KYB、供应商准入或合作方签约前的主体核验。
- 授信、投融资、并购、采购和贸易融资场景下的尽职调查与风险排查。
- 法务合规、诉讼管理、合同审核、广告投放、资质核验等业务中的背景信息补充。
- 产业研究、竞争对手分析、招商拓客、招投标线索跟踪和企业画像构建。

## 鉴权与数据说明
调用天眼查 MCP 需要配置授权参数。平台侧可通过 Authorization 请求头传入天眼查 MCP API Key。具体可调用的数据范围、返回字段和更新频率以天眼查账号权限及线上服务实际返回为准。

## FAQ
Q：天眼查 MCP 能查询哪些类型的数据？
A：当前 MCP 工具覆盖企业基础信息、风险合规、经营公示、知识产权、历史信息、董监高/人员画像等主要类别，并按实体锚定、概要、明细和专业能力分层组织。

Q：是否需要用户自行部署服务端？
A：不需要。该服务按云端部署方式接入，用户在 Model Scope 中完成鉴权配置后即可调用。

Q：智能体如何避免查错企业？
A：建议先用企业检索工具（search_companies）完成主体锚定，确认唯一主体后，再以企业全名（或统一社会信用代码）作为主体参数调用后续工具；必要时先用 get_company_capabilities 确认该企业可用的明细工具再下钻，可有效避免简称重名导致的查错。

---

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
