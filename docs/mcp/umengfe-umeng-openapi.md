---
title: "mcp-server-umeng-openapi"
description: "The Node.js client library for Umeng MCP (Model Context Protocol) API provides a series of wrappers for the Umeng statistics API."
---

# mcp-server-umeng-openapi

The Node.js client library for Umeng MCP (Model Context Protocol) API provides a series of wrappers for the Umeng statistics API.

# @umengfe/mcp-server-umeng-openapi

用于友盟 MCP（模型上下文协议）API 的 Node.js 客户端库，为友盟统计数据 API 提供一系列封装。

## 安装

```bash
npm install @umengfe/mcp-server-umeng-openapi
```

## 在 Cursor 中的配置
> 将以下内容添加到 Cursor 中的 mcp.json 文件：
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
> 在 Windows 上，你需要添加单独的配置
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

## 友盟 OpenAPI 签名辅助工具
> 此库提供了一个签名辅助工具。输入 API 密钥和 API 安全密钥，填写函数和参数以生成签名请求 URL。

```typescript
import UmengOpenAPI from '@umengfe/mcp-server-umeng-openapi/dist/src/umopenapi.js';
const client = new UmengOpenAPI('your_api_key','your_api_security');
const signedUrl = client.generateSignedUrl('param2/1/com.umeng.uapp/umeng.uapp.getAllAppData', {a:1,b:2});
fetch(signedUrl).then(res => res.json()).then(data => console.log(data));
```

## API 文档

### 友盟统计数据

获取所有应用的统计数据。

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

## 许可证

MIT

## 更新日志

### [1.0.6] - 2025-05-20
#### 修复
- 修复参数提取序列化错误

### [1.0.5] - 2025-05-19
#### 添加
- 获取事件参数值持续时间列表。
- 获取今天和昨天的应用统计数据。
- 获取昨天的应用统计数据。
- 获取今天的应用统计数据。
- 获取自定义事件的独立用户数。
- 获取渠道维度统计数据。
- 获取版本维度统计数据。
- 获取事件参数值统计数据。
- 获取事件参数值列表。
- 获取自定义事件统计数据。
- 获取事件参数列表。
- 获取事件列表。
- 获取应用的新用户留存率。
- 获取应用使用时长。
- 获取应用启动次数。
- 获取应用活跃用户。
- 获取应用新增用户。
- 获取应用统计数据。
- 创建自定义事件。

### [1.0.4] - 2025-05-12
#### 添加
- 获取单个应用的新账号。
- 获取单个应用的活跃账号。
- 根据渠道或版本条件获取应用启动次数。
- 根据渠道或版本条件获取应用活跃用户。
- 根据渠道或版本条件获取应用新增用户。

### [1.0.3] - 2025-10-06
#### 添加
- 增加获取所有应用总数的能力。
- 增加获取应用列表的能力。

## 常见问题解答 (FAQ)

- **如何获取 `UMENG_API_KEY` 和 `UMENG_API_SECRET`？**
  请访问友盟开发者平台上的 [Open API 状态页面](https://developer.umeng.com/open-api/state) 获取此信息。

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
