---
title: "wanmei-ai-card"
description: "Perfect Campus AI All-in-One Card MCP Server 1.0 is based on the NewKaiPu all-in-one card service, featuring core capabilities such as card inquiries and management, which can be directly invoked by l…"
---

# wanmei-ai-card

Perfect Campus AI All-in-One Card MCP Server 1.0 is based on the NewKaiPu all-in-one card service, featuring core capabilities such as card inquiries and management, which can be directly invoked by l…

## Company Introduction
Perfect Union (Hangzhou) Technology Co., Ltd. is dedicated to deeply integrating with various vertical scenarios in schools, serving students' learning, campus life, education and training, internships, employment, and community services. It aims to help universities provide higher-quality life management, teaching management, and talent development management services, thereby enhancing the quality of campus life for college students, improving their employability and overall competence. The company also provides an effective connection platform between universities, enterprises, and society, becoming a co-builder of the university information ecosystem.

## Product Introduction
"Perfect Campus," a product under Perfect Union, is based on the "Internet + Education" concept, relying on the smart campus platform. It offers services centered around campus services and focuses on providing precise internship, employment, training, and growth planning services, as well as campus big data services. Since its launch in 2014, "Perfect Campus" has been deeply involved in the mobile internet market for campuses for 10 years, starting from campus card services, covering recharge, payment, consumption, identity recognition, access control, and other all-in-one card service scenarios. It continuously integrates with smart campus service scenarios such as academic affairs, orientation, dormitory management, student affairs, and employment, closely linking and coordinating with the company's full range of software and hardware products. This builds a hybrid cloud smart campus construction model combining public and private clouds, establishing an effective connection platform between universities, enterprises, and society, and supporting the comprehensive digital ecological construction of universities. As of 2024, Perfect Campus has connected over 1,100 institutions domestically, with more than 10 million active real-name authenticated users. For more details, visit: https://www.17wanxiao.com/new/index.html

## Perfect Campus AI One-Card MCP Service
The Perfect Campus AI One-Card MCP Server 1.0, based on common campus card operations, provides interfaces for inquiries and some processing functions. Users can create their own campus card management assistants/applications by setting up workflows or Agents, managing their card operations through voice, text, and other methods.
### Supported Function Authentication
#### 1. Supports Common Inquiry Services for Campus Cards

| Function Name                  | Description                                                                 |
|--------------------------------|------------------------------------------------------------------------------|
| **queryUserBalanceTrades**     | **Campus Card Balance Inquiry**
Inquires about the campus card balance based on the user ID. |
| **queryUserSelfTrade**         | **Campus Card Transaction Details Inquiry**
Queries transaction details based on the user ID and date range, returning a list of transaction records. Each item in the list includes complete transaction information such as transaction serial number, merchant name, date, and balance after the transaction. |
| **queryBasicInfo**             | **Campus Card Status Inquiry**
Queries the status of the card based on the user ID, name, and password. Possible account statuses include:
1-Normal, 2-Lost, 3-System Frozen, 4-Cancelled, 5-Pre-cancelled, 6-Manually Frozen. |

#### 2. Supports Common Processing Services for Campus Cards

| Function Name      | Description                                                                 |
|--------------------|------------------------------------------------------------------------------|
| **lostCard**       | **Report Lost Campus Card**
Allows reporting a lost card by providing the ID and password when a user loses their card. If the card status is not normal, it returns an operation failure and the corresponding status prompt. |

### Usage Authorization
To use the Perfect Campus AI One-Card MCP Server 1.0, users need to be authorized. You must confirm whether your school has authorized the activation of the Perfect Campus AI One-Card MCP service. After confirmation, you should go to https://aitoolkit.59wanmei.com/pc.html, log in, and obtain the API Key.

Activation Steps:

1. Open the Perfect Campus app and bind your campus card.
2. During login, authorize on the authentication page at https://aitoolkit.59wanmei.com/pc.html, using the Perfect Campus APP to scan the QR code to get the API key.
3. Enter your API key to activate (Note: The API key is an important credential for this MCP service; please keep it safe and do not share it). If you need to switch API Keys, you can cancel the current one and re-enter a new one.

**Official site: ** [https://app.59wanmei.com/new/index.html](https://app.59wanmei.com/new/index.html)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `productivity`
- Tags: `other`, `完美校园`, `完美校园一卡通`, `ai一卡通`, `一卡通mcp server`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `mcp-remote https://aitoolkit.59wanmei.com:8080/gateway/tools/sse?apikey=API_KEY --transport sse-only --allow-http`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/wmxiaoyuan-wanmei-ai-card.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
