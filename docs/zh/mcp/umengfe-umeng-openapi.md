---
title: "友盟MCP"
description: "Umeng MCP（Model Context Protocol）API 的 Node.js 客户端库对 Umeng 统计 API 进行了一系列封装。"
---

# 友盟MCP

Umeng MCP（Model Context Protocol）API 的 Node.js 客户端库对 Umeng 统计 API 进行了一系列封装。

# @umengfe/mcp-server-umeng-openapi

A Node.js client library for the Umeng MCP (Model Context Protocol) API, providing a series of encapsulations for Umeng statistical data APIs.

## Installation

```bash

npm install @umengfe/mcp-server-umeng-openapi

```
## Configuration in Cursor
> Add the following to the mcp.json file in Cursor:
```json
{
	"mcpServers": {
		"umeng-openapi": {
			"command": "npx",
			"args": [
        "-y",
        "@umengfe/mcp-server-umeng-openapi"
			],
			"env": {
				"UMENG_API_KEY": "xxx",
				"UMENG_API_SECRET": "xxx"
			}
		}
	}
}
```
> On Windows, you need to add a separate configuration
```json
{
  "mcpServers": {
    "umeng-openapi": {
          "command": "cmd",
          "args": [
            "/c",
            "npx",
            "-y",
            "@umengfe/mcp-server-umeng-openapi"
          ],
          "env": {
            "UMENG_API_KEY": "xxx",
            "UMENG_API_SECRET": "xxx"
          }
        }
  }
}
```
## Umeng OpenAPI Signature Helper
> This library provides a signature helper. Input your API key and API security key, fill in the function and parameters to generate a signed request URL.

```typescript

import UmengOpenAPI from '@umengfe/mcp-server-umeng-openapi/dist/src/umopenapi.js';

const client = new UmengOpenAPI('your_api_key','your_api_security');

const signedUrl = client.generateSignedUrl('param2/1/com.umeng.uapp/umeng.uapp.getAllAppData', {a:1,b:2});

fetch(signedUrl).then(res => res.json()).then(data => console.log(data));

```
## API Documentation

### Umeng Statistical Data

Get statistical data for all applications.

```typescript

// 示例返回数据（数字仅供参考）

{

  "allAppData": [

    {

      "yesterdayNewUsers": 1234,        // 昨天新增用户

      "yesterdayUniqNewUsers": 1234,    // 昨天新增独立用户

      "todayLaunches": 5000,            // 今天启动次数

      "totalUsers": 100000,             // 总用户数

      "todayNewUsers": 500,             // 今天新增用户

      "yesterdayUniqActiveUsers": 2000,  // 昨天活跃独立用户

      "todayActivityUsers": 1500,        // 今天活跃用户

      "yesterdayLaunches": 4800,         // 昨天启动次数

      "yesterdayActivityUsers": 2100     // 昨天活跃用户

    }

  ]

}

```
## License

MIT

## Changelog

### [1.0.6] - 2025-05-20
#### Fixes
- Fixed parameter extraction serialization error

### [1.0.5] - 2025-05-19
#### Added
- Get event parameter value duration list.
- Get today and yesterday's application statistics.
- Get yesterday's application statistics.
- Get today's application statistics.
- Get unique user count for custom events.
- Get channel dimension statistics.
- Get version dimension statistics.
- Get event parameter value statistics.
- Get event parameter value list.
- Get custom event statistics.
- Get event parameter list.
- Get event list.
- Get new user retention rate for the application.
- Get application usage duration.
- Get application launch counts.
- Get active users for the application.
- Get new users for the application.
- Get application statistics.
- Create a custom event.

### [1.0.4] - 2025-05-12
#### Added
- Get new accounts for a single application.
- Get active accounts for a single application.
- Get application launch counts based on channel or version conditions.
- Get active users for an application based on channel or version conditions.
- Get new users for an application based on channel or version conditions.

### [1.0.3] - 2025-10-06
#### Added
- Added the ability to get the total number of all applications.
- Added the ability to get the application list.

## Frequently Asked Questions (FAQ)

- **How to get `UMENG_API_KEY` and `UMENG_API_SECRET`?**
  Please visit the [Open API status page](https://developer.umeng.com/open-api/state) on the Umeng Developer Platform to obtain this information.

**官方网站：** [https://www.npmjs.com/package/@umengfe/mcp-server-umeng-openapi](https://www.npmjs.com/package/@umengfe/mcp-server-umeng-openapi)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`research and data`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @umengfe/mcp-server-umeng-openapi`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/umengfe-umeng-openapi.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
