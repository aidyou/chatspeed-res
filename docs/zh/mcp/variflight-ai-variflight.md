---
title: "飞常准-Aviation"
description: "VariFlight航班信息服务的模型上下文协议（MCP）服务器实现方案。该服务器提供了多种工具，支持查询航班信息、天气数据及航班舒适度指标。"
---

# 飞常准-Aviation

VariFlight航班信息服务的模型上下文协议（MCP）服务器实现方案。该服务器提供了多种工具，支持查询航班信息、天气数据及航班舒适度指标。

# Variflight MCP 服务器

为 VariFlight 航班信息服务实现的模型上下文协议（MCP）服务器。该服务器提供了多种工具来查询航班信息、天气数据和飞行舒适度指标。

# Variflight API 密钥

要使用 Variflight MCP 服务器，您需要拥有一个 Variflight API 密钥。您可以从[这里](https://mcp.variflight.com)获取它。

## 安装

```json

{

    "mcpServers": {

        "variflight": {

            "command": "npx",

            "args": [

                "-y",

                "@variflight-ai/variflight-mcp"

            ],

            "env": {

                "VARIFLIGHT_API_KEY": "your_api_key_here"

            }

        }

    }

}

```
## 可用工具

### 1. 按出发地和目的地搜索航班
使用 IATA 代码搜索机场之间的航班：
```typescript
searchFlightsByDepArr({
  dep: "PEK",  // Beijing
  arr: "SHA",  // Shanghai
  date: "2024-03-20"
})
```
### 2. 按航班号搜索航班
使用航班号搜索航班：
```typescript
searchFlightsByNumber({
  fnum: "MU2157",
  date: "2024-03-20"
})
```
### 3. 获取航班中转信息
查找城市间的中转选项：
```typescript
getFlightTransferInfo({
  depcity: "BJS",
  arrcity: "LAX",
  depdate: "2024-03-20"
})
```
### 4. 飞行幸福指数
获取详细的飞行舒适度指标：
```typescript
flightHappinessIndex({
  fnum: "MU2157",
  date: "2024-03-20"
})
```
### 5. 实时飞机位置
使用注册号跟踪飞机位置：
```typescript
getRealtimeLocationByAnum({
  anum: "B2021"
})
```
### 6. 机场天气预报
获取机场三天天气预报：
```typescript
getFutureWeatherByAirport({
  airport: "PEK"
})
```
### 7. 搜索航班行程
搜索可购买的航班选项并获取最低价格：
```typescript
searchFlightItineraries({
  depCityCode: "BJS",  // Beijing
  arrCityCode: "SHA",  // Shanghai
  depDate: "2025-04-20"
})
```
## 许可证

ISC 许可证 - 详情请参阅 LICENSE。

## 作者

Variflight (https://mcp.variflight.com)

## 版本

当前版本：0.0.2

**官方网站：** [https://www.npmjs.com/package/@variflight-ai/variflight-mcp](https://www.npmjs.com/package/@variflight-ai/variflight-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`, `search`, `productivity`
- 标签：`calendar management`, `developer tools`, `search`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @variflight-ai/variflight-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/variflight-ai-variflight.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
