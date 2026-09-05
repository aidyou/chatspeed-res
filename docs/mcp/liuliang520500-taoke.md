---
title: "taoke-mcp"
description: "In the comprehensive shopping price comparison scenario, searching for coupons and comparing prices by calling the official API interfaces of the three major platforms—Taobao, JD.com, and Pinduoduo—in…"
---

# taoke-mcp

In the comprehensive shopping price comparison scenario, searching for coupons and comparing prices by calling the official API interfaces of the three major platforms—Taobao, JD.com, and Pinduoduo—in…

# Taobao MCP Service

[Smithery](https://smithery.ai/server/@liuliang520530/taoke-mcp)

The Taobao Alliance, JD Alliance, and Pinduoduo full-platform MCP service is a service based on the Model Context Protocol (MCP), supporting link conversion and product promotion functions for the three major e-commerce platforms: Taobao, JD, and Pinduoduo. It also includes a series of tools such as product search.

# GitHub:

https://github.com/liuliang520530/taoke-mcp/

## Video Tutorial

https://www.bilibili.com/video/BV1tE5jzLEMu/

## Smithery Service Hosting
https://smithery.ai/server/@liuliang520530/taoke-mcp

## Docker Deployment Support
https://hub.docker.com/r/liuliang520500/taoke-mcp

shell
docker run -dit \
--name taoke-mcp  \
--restart always \
-p 8081:8081 \
-e ENV_URL=https://config.sinataoke.cn/api/mcp/secret \
-e ENV_SECRET=url:mcp.sinataoke.cn \
-e ENV_OVERRIDE=false \
liuliang520500/taoke-mcp

You can add more environment variables with -e, refer to the stdio configuration below.

## Official Documentation

https://mcp.sinataoke.cn/docs

## Tool Demonstration on Cherry Studio

# Usage

### Environment Variable Configuration

The service requires the following environment variables to be configured:

shell
# Environment variable loading configuration
ENV_URL=https://config.sinataoke.cn/api/mcp/secret
ENV_SECRET=url:mcp.sinataoke.cn
ENV_OVERRIDE=false  # Optional, whether to override existing environment variables, this must be false, otherwise the following configurations will not take effect

# Taobao Alliance API configuration
TAOBAO_PID=your-pid # Taobao Alliance PID
TAOBAO_SESSION=your-session # Your authorization ID, see the authorization link below

# JD Alliance API configuration
JD_KEY=your-jd-key # Obtained from union.jd.com
JD_PID=your-pid-id # The first part of the PID

# Pinduoduo API configuration
PDD_PID=your-pid # Obtained from jinbao.pinduoduo.com, requires authorization
PDD_SESSION_TOKEN=your-session-token # Authorization token, see the authorization link below

# Taobao Alliance Authorization Link:

https://oauth.taobao.com/authorize?response_type=token&client_id=34297717&state=1212&view=web

# Pinduoduo Authorization Link

https://jinbao.pinduoduo.com/open.html?client_id=313cc43a30cf487da0a336d9f2df7de2&response_type=code&redirect_uri=http%3A%2F%2Fddk.mintaoke.cn%2FApi%2Fget_access_token&view=web

# Pinduoduo PID Authorization

- Use the tool `pdd.goods.prom.url` to convert a promotional link, with the parameter `generate_authority_url=true`. If not authorized, it will prioritize the authorization link.
- If you want the AI to authorize through MCP, simply send a product link and tell the AI to set `generate_authority_url=true`. The AI will then use the current tool's authorization link to convert a promotional link and return an authorization link to you.

# Integration with Claude Desktop or Cherry Studio

To use this service in Claude Desktop:

### Using MCP Configuration File

You can also start the service using an MCP configuration file. Create a file named `mcp.json` with the following content [stdio configuration]:

json
{
	"mcpServers": {
		"taobao-mcp": {
			"name": "Shopping Assistant",
			"type": "stdio",
			"isActive": true,
			"command": "npx",
			"args": [
				"-y",
				"@liuliang520500/sinataoke_cn@latest",
				"g:win11desktop/logs/" // Optional, log folder path, replace with a folder on your local computer if needed
			],
			"env": {
				"ENV_URL": "https://config.sinataoke.cn/api/mcp/secret",
				"ENV_SECRET": "url:mcp.sinataoke.cn",
				"ENV_OVERRIDE": "false",
				"TAOBAO_PID": "Taobao PID",
				"TAOBAO_SESSION": "Taobao authorization token, see the authorization link above, copy the token here after authorization",
				"JD_KEY": "Obtain from union.jd.com",
				"JD_PID": "Obtain from union.jd.com",
				"PDD_PID": "Pinduoduo PID",
				"PDD_SESSION_TOKEN": "Pinduoduo authorization token, see the authorization link above"
			}
		}
	}
}

## Supported Features

### Taobao Platform

- Link conversion
- Link parsing
- Activity conversion
- Order details query
- Tool list
- Promotion request
- Create promotion position
- Taokouling creation
- Material search
- Penalty order query-   Product Information Inquiry
-   Preferred Promotion

### JD Platform

-   Promotion Position Inquiry
-   Promotion Position Creation
-   Alliance Promotion
-   Product Inquiry
-   Coupon Inquiry

### Pinduoduo Platform

-   Product Details
-   CMS Promotion Link
-   Promotion Position Generation
-   Promotion Position Inquiry
-   Promotion Link Generation
-   Product Recommendation
-   Product Search
-   Duoduo Jinbao Link Conversion
-   Member Permission Inquiry
-   Order Details Inquiry
-   Order Incremental Inquiry
-   Promotion Position Generation

## License

ISC

## Author VX

-   liuliangzheng

### For any usage issues, please contact the author and verify the package name:

-   @liuliang520500/sinataoke_cn@latest Beware of counterfeits

**Official site: ** [https://github.com/liuliang520530/taoke-mcp](https://github.com/liuliang520530/taoke-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `search`, `research and data`, `电商,淘宝客,淘宝,京东,拼多多`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @liuliang520500/sinataoke_cn@latest g:win11desktop/logs/`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/liuliang520500-taoke.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
