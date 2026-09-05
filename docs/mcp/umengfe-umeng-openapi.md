---
title: "mcp-server-umeng-openapi"
description: "The Node.js client library for Umeng MCP (Model Context Protocol) API provides a series of wrappers for the Umeng statistics API."
---

# mcp-server-umeng-openapi

The Node.js client library for Umeng MCP (Model Context Protocol) API provides a series of wrappers for the Umeng statistics API.

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

// Example response data (numbers are illustrative)

{

  "allAppData": [

    {

      "yesterdayNewUsers": 1234,        // new users yesterday

      "yesterdayUniqNewUsers": 1234,    // unique new users yesterday

      "todayLaunches": 5000,            // launches today

      "totalUsers": 100000,             // total users

      "todayNewUsers": 500,             // new users today

      "yesterdayUniqActiveUsers": 2000,  // unique active users yesterday

      "todayActivityUsers": 1500,        // active users today

      "yesterdayLaunches": 4800,         // launches yesterday

      "yesterdayActivityUsers": 2100     // active users yesterday

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

**Official site: ** [https://www.npmjs.com/package/@umengfe/mcp-server-umeng-openapi](https://www.npmjs.com/package/@umengfe/mcp-server-umeng-openapi)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `research and data`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @umengfe/mcp-server-umeng-openapi`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/umengfe-umeng-openapi.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
