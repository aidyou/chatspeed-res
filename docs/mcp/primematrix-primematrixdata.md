---
title: "PrimeMatrixData"
description: "Prime Magic Square MCP Usage Documentation --- Access Guide The following is a general access method for any AI tool that supports the MCP protocol (such as WorkBuddy, ClaudeCode, QoderWork, etc.). Ac…"
---

# PrimeMatrixData

Prime Magic Square MCP Usage Documentation --- Access Guide The following is a general access method for any AI tool that supports the MCP protocol (such as WorkBuddy, ClaudeCode, QoderWork, etc.). Ac…

# Prime Magic Square MCP Usage Documentation

---

## Access Guide

The following is a general access method for any AI tool that supports the MCP protocol (such as WorkBuddy, ClaudeCode, QoderWork, etc.).

Access steps are as follows:

### Obtain MCP Access Credentials

Complete account registration and log in on the official Prime Magic Square platform ([https://mcp.yidian.cn/](https://mcp.yidian.cn/)). Enter the "API KEY Service" to generate a new key. In the "One-Click Use" area, obtain the complete set of MCP configuration content (including your API Key), which can be directly copied and used.

### Configure MCP Service

In the agent client, find the "Add MCP Service / MCP Configuration" entry, paste the JSON copied above, save and restart; or input "Please configure Prime Magic Square MCP" in the agent dialog box, and paste the JSON copied above. The agent will automatically complete the MCP configuration.

### Verify MCP Access Effectiveness

Input an enterprise query question in the conversation, such as "Please query the corporate entity information of Huawei Technologies Co., Ltd." If the enterprise business information is returned normally, it indicates that the MCP has been successfully connected and all service capabilities can be used normally.

---

## Product Introduction

Prime Magic Square provides five core MCP capabilities: corporate entities, risk information, operational status, financial data, and intellectual property, to support AI-based business inquiry scenarios. Through standardized MCP (Model Context Protocol) tools, developers can quickly integrate corporate information query capabilities into various AI applications, enabling intelligent enterprise queries, risk assessments, and business decision support, among other scenarios.

---

## Access Configuration

### Authentication Method

All MCP requests must carry the `Authorization` authentication header in the HTTP Header, with the format `Bearer 
`. The API Key can be created and managed on the "API Key" page of the console.

text
"Authorization": "Bearer 
"

All MCP requests must include the service code in the service address:

text
https://mcp.yidian.cn/mcp/{service_code}

### Transport Protocol

text
Transport: streamable-http

---

## Input/Output Specifications

The following are possible input parameters that may be used by each tool. For specific parameters supported by each tool, see the tool list.

### Input Specifications

| Parameter Name | Type | Description |
| --- | --- | --- |
| `ent_name` | String | Enterprise name or Unified Social Credit Code (commonly used in most tools, it is recommended to pass the full and accurate enterprise name) |
| `credit_code` | String | Unified Social Credit Code (18 digits) |

### Output Specifications

All MCP tools' return results follow the standard response format of the MCP protocol.

| Parameter Name | Type | Description |
| --- | --- | --- |
| `content` | Array | Response content array |
| `content[].type` | String | Content type, fixed value is text |
| `content[].text` | String | Returned business data content, usually in JSON string format |
| `isError` | Boolean | Whether an error occurred, true indicates an error, false indicates success |

Response example:

json
{
  "content": [
    {
      "type": "text",
      "text": "{\"CODE\":200,\"MSG\":\"ok\",\"DATA\":{...}}"
    }
  ],
  "isError": false
}

---

## MCP Tool List

### Entity Recognition and Query

Provides identity recognition and basic information query services for corporate entities, including fuzzy search of enterprises, beneficial owner results, basic enterprise information, change information, enterprise contact information, key personnel information, and shareholder information.

| Tool Name | Chinese Name | Function Description | Input Parameters |
| --- | --- | --- | --- |
| `get_company_precise_name` | Precise Enterprise Matching | Based on the abbreviation or keyword of the enterprise, returns a unique exact match or a candidate list. | ent_name (String, required): Abbreviation or keyword of the enterprise |
| `get_registration_info` | Core Registration Information | Queries the core business registration information of the enterprise, including legal representative, registered capital, establishment date, registration status, etc. | ent_name (String, required): Enterprise name or Unified Social Credit Code |
| `get_branches` | Branches | Queries the names, responsible persons, regions, establishment dates, and registration statuses of the enterprise's branches. | ent_name (String, required): Enterprise name or Unified Social Credit Code || `get_company_profile` | Company Profile | Query the company profile and main body overview, to quickly understand the company's operations and basic portrait. | ent_name (String, Required): Company name or Unified Social Credit Code |
| `get_change_records` | Change Records | Query the historical changes of the company, including the content before and after the change and the date of change. | ent_name (String, Required): Company name or Unified Social Credit Code |
| `get_shareholder_info` | Shareholder Information | Query the shareholder and capital contribution information of the company. For listed companies, it can return the top ten shareholders' information. | ent_name (String, Required): Company name or Unified Social Credit Code |
| `get_listing_info` | Listing Information | Query the stock code, listing date, exchange, sector, total market value, and other information of listed companies. | ent_name (String, Required): Company name or Unified Social Credit Code |
| `get_external_investments` | External Investments | Query the external investment information of the company, including the name of the invested company, business status, establishment date, registered capital, shareholding ratio, etc. | ent_name (String, Required): Company name or Unified Social Credit Code |

### Risk Information

Obtain judicial risks, operational risks, and asset risks of the company, covering risk scenarios such as dishonesty in execution, court judgments, business abnormalities, administrative penalties, and equity freezes.

| Tool Name | Chinese Name | Function Description | Input Parameters |
| --- | --- | --- | --- |
| `get_dishonest_info` | Dishonest Executed Person | Query the name of the dishonest executed person, case amount, executing court, release date, etc. | ent_name (String, Required): Company name or Unified Social Credit Code |
| `get_judgment_debtor_info` | Judgment Debtor | Query the case information of the judgment debtor, including the filing date, execution subject, executing court, etc. | ent_name (String, Required): Company name or Unified Social Credit Code |
| `get_high_consumption_restriction` | High Consumption Restriction | Query the high consumption restriction records, including the restricted party, filing date, and releasing court, etc. | ent_name (String, Required): Company name or Unified Social Credit Code |
| `get_terminated_execution` | Terminated Case | Query the terminated cases, including the termination date, execution subject, unfulfilled amount, etc. | ent_name (String, Required): Company name or Unified Social Credit Code |
| `get_judicial_auction` | Judicial Auction | Query the judicial auction information, including the title, appraised value, starting bid, auction time, etc. | ent_name (String, Required): Company name or Unified Social Credit Code |
| `get_bankruptcy_info` | Bankruptcy Information | Query the bankruptcy-related information of the company, including restructuring, liquidation, etc. | ent_name (String, Required): Company name or Unified Social Credit Code |
| `get_case_filing_info` | Case Filing Information | Query the court case filing information, including the case number, cause of action, filing date, plaintiff and defendant information, etc. | ent_name (String, Required): Company name or Unified Social Credit Code |
| `get_hearing_notice` | Hearing Notice | Query the hearing notices, including the case number, cause of action, hearing time, identity of the parties, etc. | ent_name (String, Required): Company name or Unified Social Credit Code |
| `get_court_notice` | Court Notice | Query the court notices, including the type of notice, cause of action, plaintiff and defendant information, etc. | ent_name (String, Required): Company name or Unified Social Credit Code |
| `get_judicial_documents` | Judicial Documents | Query the judicial documents, including the case number, cause of action, judgment result, case amount, etc. | ent_name (String, Required): Company name or Unified Social Credit Code |
| `get_service_notice` | Service Notice | Query the service notices, including the case number, cause of action, court, release date, etc. | ent_name (String, Required): Company name or Unified Social Credit Code |
| `get_business_exception` | Business Abnormality | Query the list of business abnormalities, including the inclusion date, removal reason, and decision-making authority, etc. | ent_name (String, Required): Company name or Unified Social Credit Code |
| `get_serious_violation` | Serious Violation | Query the records of serious illegal and dishonest lists and corresponding regulatory information. | ent_name (String, Required): Company name or Unified Social Credit Code || `get_cancellation_record_info` | Cancellation Record | Query cancellation record information, including reasons for cancellation, cancellation date, and cancellation status. | ent_name (String, Required): Enterprise name or Unified Social Credit Code |
| `get_simple_cancellation_info` | Simplified Cancellation | Query simplified cancellation information, including cancellation result, registration authority, and announcement period. | ent_name (String, Required): Enterprise name or Unified Social Credit Code |
| `get_administrative_penalty` | Administrative Penalty | Query administrative penalties, including penalty results, penalizing units, amount, and date. | ent_name (String, Required): Enterprise name or Unified Social Credit Code |
| `get_environmental_penalty` | Environmental Penalty | Query environmental administrative penalties, including penalty results, penalizing units, amount, and date. | ent_name (String, Required): Enterprise name or Unified Social Credit Code |
| `get_procurement_debarment_list` | Dishonesty List | Query if the enterprise is listed on the serious illegal and dishonest list of government procurement, including reasons for listing, penalty results, penalty time, and enforcement unit. | ent_name (String, Required): Enterprise name or Unified Social Credit Code |
| `get_tax_abnormal` | Tax Abnormality | Query tax abnormal records and related tax supervision information. | ent_name (String, Required): Enterprise name or Unified Social Credit Code |
| `get_tax_arrears_notice` | Tax Arrears Notice | Query types of taxes in arrears, amounts, issuing units, and issue dates. | ent_name (String, Required): Enterprise name or Unified Social Credit Code |
| `get_tax_violation` | Tax Violation | Query the nature of tax violation cases, tax authorities, and issue dates. | ent_name (String, Required): Enterprise name or Unified Social Credit Code |
| `get_chattel_mortgage_info` | Chattel Mortgage | Query chattel mortgage registration number, mortgagee, amount, status, and registration date. | ent_name (String, Required): Enterprise name or Unified Social Credit Code |
| `get_equity_freeze` | Equity Freeze | Query judicial equity freeze, including the amount frozen, duration, and executing court. | ent_name (String, Required): Enterprise name or Unified Social Credit Code |
| `get_stock_pledge_info` | Stock Pledge | Query stock pledge of listed companies, including pledgor, pledgee, number of shares, and market value. | ent_name (String, Required): Enterprise name or Unified Social Credit Code |
| `get_equity_pledge_info` | Equity Pledge | Query equity pledgor, pledgee, equity amount, status, and registration date. | ent_name (String, Required): Enterprise name or Unified Social Credit Code |
| `get_ipr_pledge` | IPR Pledge | Query intellectual property rights pledge type, name, term, and announcement date. | ent_name (String, Required): Enterprise name or Unified Social Credit Code |

### Business Operations

Gain insights into the real business vitality of an enterprise, covering qualifications and permits, bidding and tendering dynamics, financing history, credit ratings, news and public opinion, and recruitment information.

| Tool Name | Chinese Name | Function Description | Input Parameters |
| --- | --- | --- | --- |
| `get_administrative_license` | Administrative License | Query enterprise administrative license information and licensed items. | ent_name (String, Required): Enterprise name or Unified Social Credit Code |
| `get_qualifications` | Qualification Certificates | Query qualification names, certificate numbers, categories, levels, validity periods, and status. | ent_name (String, Required): Enterprise name or Unified Social Credit Code |
| `get_honor_info` | Honor Information | Query honor names, types, levels, issue dates, and issuing units. | ent_name (String, Required): Enterprise name or Unified Social Credit Code |
| `get_credit_evaluation` | Credit Rating | Query official credit ratings, tax credit ratings, and other evaluation information. | ent_name (String, Required): Enterprise name or Unified Social Credit Code |
| `get_financing_records` | Financing Information | Query venture capital financing, IPO financing, additional issuance financing, and other financing records. | ent_name (String, Required): Enterprise name or Unified Social Credit Code |
| `get_bidding_info` | Bidding Information | Query bidding project names, winning bid situations, amounts, and bidding units. | ent_name (String, Required): Enterprise name or Unified Social Credit Code || `get_random_check` | Dual Random Check | Query records and results of dual random spot checks. | ent_name (String, Required): Enterprise name or Unified Social Credit Code |
| `get_spot_check_info` | Spot Check | Query information on the implementing agency, type, date, result, etc. of inspections. | ent_name (String, Required): Enterprise name or Unified Social Credit Code |
| `get_news_sentiment` | News Sentiment | Query news titles, publication dates, sentiment types, and other public opinion information. | ent_name (String, Required): Enterprise name or Unified Social Credit Code |
| `get_taxpayer_qualification` | Taxpayer Qualification | Query taxpayer identification number, qualification type, competent tax authority, validity period, etc. | ent_name (String, Required): Enterprise name or Unified Social Credit Code |
| `get_recruitment_info` | Recruitment Information | Query job positions, monthly salary, education level, experience, office location, publication date, etc. | ent_name (String, Required): Enterprise name or Unified Social Credit Code |

### Financial Data

Structured output of core financial data and analysis indicators for listed companies, covering balance sheets, cash flow statements, income statements, and comprehensive financial indicators.

| Tool Name | Chinese Name | Function Description | Input Parameters |
| --- | --- | --- | --- |
| `get_financial_data` | Core Financial Indicators | Query core financial data and analysis indicators of listed companies | ent_name (String, Required): Enterprise name or Unified Social Credit Code |
| `get_balance_sheet` | Balance Sheet | Query balance sheet data of listed companies. | ent_name (String, Required): Enterprise name or Unified Social Credit Code |
| `get_cash_flow_statement` | Cash Flow Statement | Query cash flow statement data of listed companies. | ent_name (String, Required): Enterprise name or Unified Social Credit Code |
| `get_income_statement` | Income Statement | Query income statement data of listed companies. | ent_name (String, Required): Enterprise name or Unified Social Credit Code |

### Intellectual Property

Evaluate the hard power of enterprise innovation and technology, providing intellectual property information such as patents, trademarks, software copyrights, work copyrights, and internet filings.

| Tool Name | Chinese Name | Function Description | Input Parameters |
| --- | --- | --- | --- |
| `get_patent_info` | Patent Information | Query total number of patents, total number of authorizations, and up to 20 detailed patent entries. | ent_name (String, Required): Enterprise name or Unified Social Credit Code |
| `get_copyright_work_info` | Work Copyright | Query work name, category, registration number, registration date, etc. | ent_name (String, Required): Enterprise name or Unified Social Credit Code |
| `get_software_copyright_info` | Software Copyright | Query full software name, abbreviation, version number, registration number, registration time, etc. | ent_name (String, Required): Enterprise name or Unified Social Credit Code |
| `get_trademark_info` | Trademark Information | Query trademark name, international classification, status, application number, registration number, application date, etc. | ent_name (String, Required): Enterprise name or Unified Social Credit Code |
| `get_internet_service_info` | Internet Filing | Query ICP filing, APP filing, mini-program filing, algorithm filing, etc. | ent_name (String, Required): Enterprise name or Unified Social Credit Code |

---

## Example Calls

The following demonstrates the actual call effects of MCP tools during user-AI interactions.

### Example 1: Business Registration and Shareholder Information Query

> Question: Can you help me check the business registration and shareholder information of Tencent?

**AI Application Call Process:**

**Step 1:** Call `get_company_precise_name`

json
{
  "ent_name": "Tencent"
}

Result: Returns a list of matching enterprises, confirming the full name as "Shenzhen Tencent Computer Systems Co., Ltd."

**Step 2:** Call `get_registration_info`

json
{
  "ent_name": "Shenzhen Tencent Computer Systems Co., Ltd."
}

Result: Returns the business registration information of the enterprise, including legal representative, registered capital, establishment date, business status, etc.

**Step 3:** Call `get_shareholder_info`

json
{
  "ent_name": "Shenzhen Tencent Computer Systems Co., Ltd."
}

Result: Returns the shareholder and capital contribution information of the enterprise, assisting in identifying the equity structure.

### Example 2: Risk Information Query> Issue: Query whether Tencent has any business anomalies, administrative penalties, and equity freeze risks.

**AI Application Call Process:**

**Step 1:** Call `get_company_precise_name`

json
{
  "ent_name": "Tencent"
}

Result: Returns a list of matching companies, confirming the full name as "Shenzhen Tencent Computer Systems Co., Ltd."

**Step 2:** Call `get_business_exception`

json
{
  "ent_name": "Shenzhen Tencent Computer Systems Co., Ltd."
}

Result: Returns records of business anomalies; if no records are found, an empty result is returned.

**Step 3:** Call `get_administrative_penalty`

json
{
  "ent_name": "Shenzhen Tencent Computer Systems Co., Ltd."
}

Result: Returns records of administrative penalties, including the penalty decision, penalizing authority, date of penalty, etc.

**Step 4:** Call `get_equity_freeze`

json
{
  "ent_name": "Shenzhen Tencent Computer Systems Co., Ltd."
}

Result: Returns information on judicial equity freezes, which can be used to assist in assessing asset risks.

### Example 3: Bidding Information Inquiry

> Issue: Please help me find the latest bidding information for Tencent.

**AI Application Call Process:**

**Step 1:** Call `get_company_precise_name`

json
{
  "ent_name": "Tencent"
}

Result: Returns a list of matching companies, confirming the full name as "Shenzhen Tencent Computer Systems Co., Ltd."

**Step 2:** Call `get_bidding_info`

json
{
  "

**Official site: ** [https://mcp.yidian.cn](https://mcp.yidian.cn)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `finance`, `data`
- Tags: `research and data`, `search`, `finance`, `mcp`, `chinese`

## MCP Configuration

- Transport: `http`
- Command: ``
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/primematrix-primematrixdata.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
