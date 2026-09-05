---
title: "和风天气"
description: "QWeather API 的 MCP 服务器，通过模型上下文协议（MCP）提供全面的天气信息查询功能。"
---

# 和风天气

QWeather API 的 MCP 服务器，通过模型上下文协议（MCP）提供全面的天气信息查询功能。

# qweather-mcp
[mseep.ai](https://mseep.ai/app/ae24a36c-f029-49b3-9c42-fc111021add0)
[![MseeP.ai Security Assessment Badge](/mcp-assets/35c8dbcff4c38d1b415e403e20aa31bd.png)](https://mseep.ai/app/overstarry-qweather-mcp)
[Smithery](https://smithery.ai/server/@overstarry/qweather-mcp)

English | [简体中文](https://github.com/hello634528/qweather-mcp/blob/HEAD/README.zh-CN.md)

> 为 [QWeather](https://www.qweather.com/) API 提供的 MCP 服务器，通过模型上下文协议 (MCP) 提供全面的天气信息查询功能。

## ✨ 特性

- 🌤️ 实时天气查询
- 📍 基于经纬度的查询（无需城市查找）
- 📅 多日天气预报（3/7/10/15/30天）
- 🔑 简单的 API 密钥配置
- 🔌 自定义 API 基础 URL 支持
- 🛠️ 完整的工具集成

## 📦 安装

### 通过 Smithery

推荐：使用 [Smithery](https://smithery.ai/server/@overstarry/qweather-mcp) 为 Claude Desktop 自动安装：

```bash

npx -y @smithery/cli install @overstarry/qweather-mcp --client claude

```
### 手动配置

1. 首先，从 [QWeather 控制台](https://console.qweather.com/) 获取您的 API 密钥。

2. 启动服务器：

```bash

# stdio server

npx -y qweather-mcp

```
3. 配置环境变量：

```bash

QWEATHER_API_BASE=https://api.qweather.com

QWEATHER_API_KEY=

```
### JSON 配置

将以下内容添加到您的配置文件中：

```json

{

  "mcpServers": {

    "qweather": {

      "command": "npx",

      "args": ["-y", "qweather-mcp"],

      "env": {

        "QWEATHER_API_BASE": "",

        "QWEATHER_API_KEY": ""

      }

    }

  }

}

```
## 🛠️ 可用工具

所有工具都接受 **纬度** 和 **经度** 参数（以度为单位）。

### get-weather-now

获取指定纬度/经度的当前天气信息。

### get-weather-forecast

获取指定纬度/经度的天气预报信息，可自定义预报天数：
- 3天预报
- 7天预报
- 10天预报
- 15天预报
- 30天预报

预报数据包括：
- 温度范围（最低/最高）
- 白天/夜间天气状况
- 日出/日落时间
- 降水量
- 湿度
- 风况
- 紫外线指数

### get-minutely-precipitation

提供未来2小时内指定纬度/经度的分钟级降水预报，包括：
- 降水类型（雨/雪）
- 每分钟降水量
- 精确的时间预测
- 实时预报描述

### get-hourly-forecast

提供未来24、72或168小时内的每小时天气预报，包括：
- 温度变化
- 天气状况
- 风向和风力
- 相对湿度
- 大气压
- 降水概率
- 云量

### get-weather-warning

提供指定纬度/经度的实时天气预警信息，包括：
- 预警发布机构
- 预警级别和类型
- 详细的预警内容
- 预警有效期限
- 相关建议

### get-weather-indices

提供指定纬度/经度的天气生活指数信息，支持多种指数类型：
- 运动指数
- 洗车指数
- 穿衣指数
- 钓鱼指数
- 紫外线指数
- 旅游指数
- 过敏指数
以及其他16种生活指数

### get-air-quality

提供指定纬度/经度的实时空气质量数据，包括：
- AQI 指数
- 空气质量等级
- 主要污染物
- 健康建议
- 污染物浓度

### get-air-quality-hourly

提供未来24小时内指定纬度/经度的每小时空气质量预报：
- 每小时 AQI 预测
- 污染物浓度变化
- 健康影响评估
- 防护建议

### get-air-quality-daily

提供未来3天内指定纬度/经度的空气质量预报：
- 每日 AQI 预测
- 主要污染物预报
- 空气质量等级变化
- 健康防护建议

## 🤝 贡献

欢迎提出问题和改进建议！请查看我们的贡献指南。

## 📄 许可证

MIT

## 🔗 相关链接

- [QWeather 官方网站](https://www.qweather.com/)
- [API 文档](https://dev.qweather.com/)
- [控制台](https://console.qweather.com/)

**官方网站：** [https://github.com/hello634528/qweather-mcp](https://github.com/hello634528/qweather-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`research and data`, `location services`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @wangzmwzm/qweather-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/wzmmcp-qweather.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
