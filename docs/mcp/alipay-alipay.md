---
title: "mcp-server-alipay"
description: "@alipay/mcp-server-alipay 是支付宝开放平台提供的 MCP Server，让你可以轻松将支付宝开放平台提供的交易创建、查询、退款等能力集成到你的 LLM 应用中，并进一步创建具备支付能力的智能工具。"
---

# mcp-server-alipay

@alipay/mcp-server-alipay 是支付宝开放平台提供的 MCP Server，让你可以轻松将支付宝开放平台提供的交易创建、查询、退款等能力集成到你的 LLM 应用中，并进一步创建具备支付能力的智能工具。

## 0. One-Stop Access Assistant
Don't want to read the long README?

We have prepared a one-stop access Agent for our esteemed users. Let it assist you in completing the preparatory work:
(Click the link below and log in to your Alipay account to enjoy this service)
https://b.alipay.com/page/product-workspace/all-product?aigcSceneCode=PRODUCT_CENTER_SCENE&aigcSendMsg=%E5%BC%80%E9%80%9A%E6%94%AF%E4%BB%98MCP&contextParams=%7B%22channelCode%22%3A%22COZE%22%7D

## 1. Introduction

`@alipay/mcp-server-alipay` is an MCP Server provided by the Alipay Open Platform, allowing you to easily integrate transaction creation, inquiry, refund, and other capabilities offered by the Alipay Open Platform into your LLM applications, and further create intelligent tools with payment capabilities.

Here is a fictional simplified use case to help understand the tool's capabilities:

> An illustrator hopes to earn income by providing customized original illustration services. Traditionally, he/she would need to repeatedly communicate with each customer about their requirements, determine the price, and send a payment link, then manually confirm the payment status, which is a tedious and time-consuming process.
>
> Now, using the Alipay MCP Server and intelligent Agent tools, the illustrator has built a platform through the Agent and developed a smart chat application (web or mini-program). Customers only need to describe their drawing needs (such as style preferences, illustration purpose, delivery time, etc.) in the application, and the AI will automatically analyze the requirements, quickly generate accurate and reasonable custom quotes, and instantly create a dedicated Alipay payment link through the tool.
>
> After the customer clicks and pays, the creator immediately receives a notification and proceeds to the creation phase. There is no need for back-and-forth manual confirmation of the transaction status or payment situation. The entire process is not only convenient and smooth but also significantly improves transaction efficiency and customer satisfaction, allowing the illustrator to focus more on their creative work and achieve a more relaxed personalized service business model.

```

     最终用户设备                     Agent 运行环境

+---------------------+        +--------------------------+      +-------------------+

|                     |  交流  |   支付宝 MCP Server +    |      |                   |

|    小程序/WebApp    ||   其他 MCP Server +      ||     支付服务      |

|                     |  支付  |   Agent 开发工具         |      |   交易/退款/查询  |

+---------------------+        +--------------------------+      +-------------------+

     创作服务买家                     智能工具开发者                   支付宝开放平台

      (最终用户)                         (创作者)

```
For more information and usage guidelines about this tool, including the prerequisite process of preparing a merchant identity for receiving payments, please refer to the [Payment MCP Service Documentation](https://opendocs.alipay.com/open/0go80l) on the Alipay Open Platform.

## 2. Usage and Configuration

To use most of the payment capabilities of the tool, you first need to become a receiving merchant on the Alipay Open Platform and obtain the merchant private key. After that, you can directly use the Alipay MCP Server on mainstream MCP Clients:

### Using in Cursor

Add the following configuration to the `.cursor/mcp.json` file in your Cursor project:

```json

{

  "mcpServers": {

    "mcp-server-alipay": {

      "command": "npx",

      "args": ["-y", "@alipay/mcp-server-alipay"],

      "env": {

        "AP_APP_ID": "2014...222",

        "AP_APP_KEY": "MIIE...DZdM=",

        "AP_PUB_KEY": "MIIB...DAQAB",

        "AP_RETURN_URL": "https://success-page",

        "AP_NOTIFY_URL": "https://your-own-server",

        "...其他参数": "...其他值"

      }

    },

    "其他工具": { 

      "...": "..."

    }

  }

}

```
### Using in Cline

Find the `cline_mcp_settings.json` configuration file in your Cline settings and add the following configuration:

```json

{

  "mcpServers": {

    "mcp-server-alipay": {

      "command": "npx",

      "args": ["-y", "@alipay/mcp-server-alipay"],

      "env": {

        "AP_APP_ID": "2014...222",

        "AP_APP_KEY": "MIIE...DZdM=",

        "AP_PUB_KEY": "MIIB...DAQAB",

        "AP_RETURN_URL": "https://success-page",

        "AP_NOTIFY_URL": "https://your-own-server",

        "...其他参数": "...其他值"

      },

      "disable": false,

      "autoApprove": []

    },

    "其他工具": { 

      "...": "..."

    }

  }

}

```
### Using in Other MCP Clients

You can also use it in any other MCP Client. Properly configure the Server process startup method `npx -y @alipay/mcp-server-alipay`, and set the environment parameters as described below.

### All Parameters

The Alipay MCP Server receives parameters via environment variables. The parameters and their default values include:

```shell

# 支付宝开放平台配置

AP_APP_ID=2014...222                    # 商户在开放平台申请的应用 ID（APPID）。必需。

AP_APP_KEY=MIIE...DZdM=                 # 商户在开放平台申请的应用私钥。必需。

AP_PUB_KEY=MIIB...DAQAB                 # 用于验证支付宝服务端数据签名的支付宝公钥，在开放平台获取。必需。

AP_RETURN_URL=https://success-page      # 网页支付完成后对付款用户展示的「同步结果返回地址」。

AP_NOTIFY_URL=https://your-own-server   # 支付完成后，用于告知开发者支付结果的「异步结果通知地址」。

AP_ENCRYPTION_ALGO=RSA2                 # 商户在开放平台配置的参数签名方式。可选值为 "RSA2" 或 "RSA"。缺省值为 "RSA2"。

AP_CURRENT_ENV=prod                     # 连接的支付宝开放平台环境。可选值为 "prod"（线上环境）或 "sandbox"（沙箱环境）。缺省值为 "prod"。

# MCP Server 配置

AP_SELECT_TOOLS=all                      # 允许使用的工具。可选值为 "all" 或逗号分隔的工具名称列表。工具名称包括 `mobilePay`, `webPagePay`, `queryPay`, `refundPay`, `refundQuery`。缺省值为 "all"。

AP_LOG_ENABLED=true                      # 是否在 $HOME/mcp-server-alipay.log 中记录日志。默认值为 true。

```
## 3. Debugging with MCP Inspector

You can use MCP Inspector to debug and understand the functionality of the Alipay MCP Server:

1. Set the environment variables using `export`;
2. Start MCP Inspector by running `npx -y @modelcontextprotocol/inspector npx -y @alipay/mcp-server-alipay`;
3. Debug in the MCP Inspector WebUI.

## 4. Supported Capabilities

The following table lists all available payment tool capabilities:

| Name | Description | Parameters | Output |
|-------|------|------|------|
| `create-mobile-alipay-payment` | For developers with merchant qualifications, creates an Alipay order and returns a Markdown text with a payment link. This link, when opened in a mobile browser, can redirect to Alipay or allow direct payment in the browser. This tool is suitable for mobile websites or mobile apps. | - outTradeNo: Merchant order number, up to 64 characters
- totalAmount: Payment amount, unit: yuan, minimum 0.01
- orderTitle: Order title, up to 256 characters | - url: Markdown text of the payment link || `create-web-page-alipay-payment` | Suitable for developers with merchant qualifications, creates an Alipay order and returns a Markdown text containing a payment link. When this link is opened in a computer browser, it displays a QR code for payment, which the user can scan to complete the payment. This tool is suitable for desktop websites or PC clients. | - outTradeNo: Merchant order number, up to 64 characters
- totalAmount: Payment amount, unit: yuan, minimum 0.01
- orderTitle: Order title, up to 256 characters | - url: The markdown text of the payment link |
| `create-alipay-payment-agent` | Accessible to individual developers, creates an Alipay order for personal merchants and returns a Markdown text containing a payment page link and QR code. Users can click on the link or scan the QR code with Alipay to proceed to the payment page and complete the payment. | - outTradeNo: Merchant order number, up to 64 characters
- totalAmount: Payment amount, unit: yuan, minimum 0.01
- agentName: Agent name, up to 128 characters | - Mobile payment link: Can be directly accessed from mobile devices for payment
- Payment QR code: Use Alipay to scan and pay |
| `query-alipay-payment` | Queries an Alipay order and returns a text containing order information. | - outTradeNo: Merchant order number, up to 64 characters | - tradeStatus: Transaction status of the order
- totalAmount: Transaction amount of the order
- tradeNo: Alipay transaction number |
| `refund-alipay-payment` | Initiates a refund for a transaction and returns the refund status and amount. | - outTradeNo: Merchant order number, up to 64 characters
- refundAmount: Refund amount, unit: yuan, minimum 0.01
- outRequestNo: Refund request number, up to 64 characters
- refundReason: Reason for refund, up to 256 characters (optional) | - tradeNo: Alipay transaction number
- refundResult: Refund result |
| `query-alipay-refund` | Queries an Alipay refund and returns the refund status and amount. | - outRequestNo: Refund request number, up to 64 characters
- outTradeNo: Merchant order number, up to 64 characters | - tradeNo: Alipay transaction number
- refundAmount: Refund amount
- refundStatus: Refund status |

## 5. How to Choose the Right Payment Method

During development, to help the LLM more accurately choose the appropriate payment method, it is recommended to clearly specify your product's usage scenario in the Prompt:

- **Web Page Payment (`create-web-page-alipay-payment`)**: Suitable for developers with merchant qualifications where users see the payment interface on a computer screen. If your application or website primarily runs on a desktop (PC), you can specify in the Prompt: "My application is a desktop software/PC website, and I need to display the payment QR code on a computer."

- **Mobile Payment (`create-mobile-alipay-payment`)**: Suitable for developers with merchant qualifications where users initiate payments within a mobile browser. If your application is a mobile H5 page or a mobile website, you can specify in the Prompt: "My page is a mobile webpage, and I need to directly invoke Alipay payment on the phone."

- **Zhiyi Shou (`create-alipay-payment-agent`)**: Suitable for individual developers (without a business license). Users can directly jump to the payment page on mobile or use the Alipay app to scan the QR code displayed on a PC. For more details, see [Zhiyi Shou Solution Introduction](https://opendocs.alipay.com/solution/0im3wl).
We will provide more payment methods suitable for AI applications in the future, stay tuned.

## 6. Precautions

* The Alipay MCP service is currently in its early release stage, and related capabilities and supporting facilities are continuously being improved. If you have any feedback, experience sharing, or suggestions, please participate in discussions at the [Alipay Developer Community](https://open.alipay.com/portal/forum).
* When deploying and using agent services, make sure to properly safeguard your merchant private key to prevent leaks. If necessary, refer to the instructions on [Alipay Open Platform - How to Invalidate a Key](https://opendocs.alipay.com/support/01rav9) to invalidate existing keys.
* When developing any agent service that uses the MCP Server and providing it for user use, understand the necessary security knowledge to guard against specific security risks associated with AI applications, such as prompt attacks and arbitrary command execution on the MCP Server.
* For more precautions and best practices, please refer to the [About Alipay MCP Service](https://opendocs.alipay.com/open/0go80l) documentation on the Alipay Open Platform.

## 7. Usage AgreementThis tool is part of the Alipay Open Platform capabilities. During use, please comply with the [Alipay Open Platform Developer Service Agreement](https://ds.alipay.com/fd-ifz2dlhv/index.html) and relevant commercial conduct regulations.

**Official site: ** [https://www.npmjs.com/package/@alipay/mcp-server-alipay](https://www.npmjs.com/package/@alipay/mcp-server-alipay)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `finance`
- Tags: `finance`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @alipay/mcp-server-alipay`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/alipay-alipay.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
