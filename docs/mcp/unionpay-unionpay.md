---
title: "unionpay-mcp-server"
description: "The MCP Server provided by the UnionPay Open Platform allows you to easily integrate transaction creation, query, refund, and other capabilities offered by the UnionPay Open Platform into your LLM app…"
---

# unionpay-mcp-server

The MCP Server provided by the UnionPay Open Platform allows you to easily integrate transaction creation, query, refund, and other capabilities offered by the UnionPay Open Platform into your LLM app…

## 1. Introduction

unionpay-mcp-server is a payment tool (MCP Server) provided by UnionPay for AI agents based on the MCP protocol. All kinds of agent applications that support the MCP protocol can access UnionPay payment capabilities safely and conveniently. The following is an example of a trip planning agent providing hotel reservations for users:
In the traditional way, users need to independently query hotels, compare hotel prices, and complete reservations and payments, which takes up a lot of time and energy. In the agent mode, users only need to enter travel needs (such as departure point, destination, travel time, budget preferences, etc.) in the agent application, and the agent can automatically analyze the needs and recommend the best hotel options. After the user confirms, the order is automatically placed and the payment link is generated through the UnionPay MCP Server. After the user completes the payment, the agent completes the online hotel reservation operation and synchronizes the order information to the user in real time. The entire process does not require manual repeated inquiries and operations, which is efficient and convenient.

## 2. Usage and Configuration

Before using, users must first register as a merchant receiving payment on the UnionPay Open Platform and obtain the merchant private key. After that, users can use various payment tools in the UnionPay MCP Server on mainstream client applications that support MCP.

### Use in Cursor

Add the following configuration to `.cursor/mcp.json` in the Cursor project:

```json
{
  "mcpServers": {
    "unionpay-mcp-server": {
	   "command": "npx",
	   "args": ["-y","unionpay-mcp-server"],
	   "env": {
		   "UP_ACQ_INS_CODE": "
",
		   "UP_ACCESS_TYPE": "",
		   // Merchant ID
		   "UP_MER_ID": "",
		   "UP_TR_ID": "
",
		   "UP_TOKEN_TYPE": "",
		   "UP_FRONT_URL": "",
		   "UP_FRONT_FAIL_URL": "",
		   "UP_BACK_URL": "
",
		   "UP_SIGN_CERT_PATH": "
",
		   "UP_SIGN_CERT_PWD": "",
		   "UP_VALIDATE_CERT_DIR": "
",
		   "UP_NEED_ENCRYPT": "",
		   "UP_ENCRYPT_CERT_PATH": "
",
		   "UP_DECRYPT_CERT_PATH": "
",
		   "UP_ENCRYPT_CERT_PWD": "
",
		   "UP_LOG_DIR": "Log output directory, optional, logs are output to HOME directory by default"
	         }
     },
    "Other tools": {
      "...": "..."
    }
  }
}
```

### Use in Cline

Find the `cline_mcp_settings.json` configuration file in Cline settings and add the following configuration:

```json
{
  "mcpServers": {
    "unionpay-mcp-server": {
      "command": "npx",
      "args": ["-y", "unionpay-mcp-server"],
      "env": {
		    "UP_ACQ_INS_CODE": "
",
		    "UP_ACCESS_TYPE": "",
		   // Merchant ID
		   "UP_MER_ID": "",
		   "UP_TR_ID": "
",
		   "UP_TOKEN_TYPE": "",
		   "UP_FRONT_URL": "",
		   "UP_FRONT_FAIL_URL": "",
		   "UP_BACK_URL": "
",
		   "UP_SIGN_CERT_PATH": "
",
		   "UP_SIGN_CERT_PWD": "",
		   "UP_VALIDATE_CERT_DIR": "
",
		   "UP_NEED_ENCRYPT": "",
		   "UP_ENCRYPT_CERT_PATH": "
",
		   "UP_DECRYPT_CERT_PATH": "
",
		   "UP_ENCRYPT_CERT_PWD": "
",
		   "UP_LOG_DIR": "Log output path, optional, defaults to HOME directory"
      },
      "disable": false,
      "autoApprove": []
    },
    "Other tools": {
      "...": "..."
    }
  }
}
```

### Use in other MCP Clients

You can also use it in any other MCP Client, configure the Server process startup method `npx -y unionpay-mcp-server` appropriately, and set the environment parameters as described below.

### All parameters

UnionPay MCP Server receives parameters through environment variables.
UnionPay open platform configuration:

```json
UnionPay open platform configuration：
{
		"UP_ACQ_INS_CODE": "
",
		"UP_ACCESS_TYPE": "",
		"UP_MER_ID": "",
		"UP_TR_ID": "
",
		"UP_TOKEN_TYPE": "",
		"UP_FRONT_URL": "",
		"UP_FRONT_FAIL_URL": "",
		"UP_BACK_URL": "
",
		"UP_SIGN_CERT_PATH": "
",
		"UP_SIGN_CERT_PWD": "",
		"UP_VALIDATE_CERT_DIR": "
",
		"UP_NEED_ENCRYPT": "",
		"UP_ENCRYPT_CERT_PATH": "
",
		"UP_DECRYPT_CERT_PATH": "
",
		"UP_ENCRYPT_CERT_PWD": "
",
      }

MCP Server Configuration：
    "UP_LOG_DIR": "Log output path, optional, defaults to HOME directory"
```

## 3. Debugging with MCP Inspector

Developers can use MCP Inspector to debug and understand the functions of UnionPay MCP Server. The specific operations are as follows:

1. Set various environment variables through export;
2. Execute npx -y @modelcontextprotocol/inspector && npx -y unionpay-mcp-server to start MCP Inspector;
3. Debug in MCP Inspector WebUI.

## 4. Supported capabilities

The following table lists the payment tools available in this version of MCP Server. For specific usage of the capabilities provided in this version, please refer to the UnionPay Open Platform Contract Payment Products.（https://open.unionpay.com/tjweb/acproduct/list?apiSvcId=3301）

In addition, when platform merchants and acquiring institutions access, they need to send the following fields when calling other tools besides query-unionpay-payment:

| Name       | Description                     | Parameters                            |
| ---------- | ------------------------------- | ------------------------------------- |
| merCatCode | Merchant Category               | Required for acquiring access         |
| merName    | Merchant Name                   | Required for acquiring access         |
| merAbbr    | Merchant Abbreviation           | Required for acquiring access         |
| subMerId   | Secondary Merchant Code         | Required for platform merchant access |
| subMerName | Secondary Merchant Name         | Required for platform merchant access |
| subMerAbbr | Secondary Merchant Abbreviation | Required for platform merchant access |

## 5. How to choose the right payment method

During the development process, in order to allow LLM to more accurately select the appropriate payment method, it is recommended to clearly explain the product usage scenario in the prompt:
Web payment: Applicable to scenarios where users see the payment interface on the computer screen. If the intelligent application is mainly run on the desktop (PC), you can explain in the prompt: "My application is a desktop software/PC website, and the payment QR code needs to be displayed on the computer."
Mobile payment: Applicable to scenarios where users initiate payment in the mobile browser. If the application is a mobile H5 page or mobile website, you can explain in the prompt: "My page is a mobile web page, and you need to initiate online payment directly on the phone."
More MCP payment tools are under development, so stay tuned.

##  6. Notes

* UnionPay MCP payment service is currently in the early stages of release, and related capabilities and supporting facilities are being continuously improved. If you have any questions or suggestions during use, please contact us.
* When developing any intelligent service using MCP Server and providing it to users, please understand the necessary security knowledge to prevent security risks such as prompt attacks unique to AI applications and arbitrary command execution of MCP Server.

##  7. Terms of Use

This tool is part of the UnionPay open platform capabilities. During use, please comply with China UnionPay Developer Usage Guidelines
(https://open.unionpay.com/tjweb/support/doc/online/3/122), the open platform "China UnionPay Service Agreement" (https://user.95516.com/pages/misc/newAgree.html) and relevant business behavior regulations.

**Official site: ** [https://www.npmjs.com/package/unionpay-mcp-server?activeTab=code](https://www.npmjs.com/package/unionpay-mcp-server?activeTab=code)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `finance`
- Tags: `finance`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @unionpay/unionpay-mcp-server`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/unionpay-unionpay.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
