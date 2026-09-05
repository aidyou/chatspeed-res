---
title: "baranwang"
description: "通胜 MCP 服务 简体中文 English 中国传统黄历（通胜）计算服务，基于 Model Context Protocol (MCP) ✨ 功能特点 - 📅 公历农历转换 - 支持公历与农历日期的相互转换 - 🍀 每日宜忌 - 提供每日吉凶、宜忌活动的详细信息 - 🕐 时辰信息 - 十二时辰（子、丑、寅等）的吉凶宜忌 - 🔮 命理元素 - 五行、神煞、星宿等传统命理学详细数据 🚀 安装与使用…"
---

# baranwang

通胜 MCP 服务 简体中文 English 中国传统黄历（通胜）计算服务，基于 Model Context Protocol (MCP) ✨ 功能特点 - 📅 公历农历转换 - 支持公历与农历日期的相互转换 - 🍀 每日宜忌 - 提供每日吉凶、宜忌活动的详细信息 - 🕐 时辰信息 - 十二时辰（子、丑、寅等）的吉凶宜忌 - 🔮 命理元素 - 五行、神煞、星宿等传统命理学详细数据 🚀 安装与使用…

# 通胜 MCP 服务

[Smithery](https://smithery.ai/server/@baranwang/mcp-tung-shing)
[![NPM Version](/mcp-assets/a54621745a6198c873e1ad8fc7327b2b.svg)](https://www.npmjs.com/package/mcp-tung-shing)
[![License](/mcp-assets/5816f652aa1f0cc4eedb21a2f733e09e.svg)](https://github.com/baranwang/mcp-tung-shing/blob/main/LICENSE)

简体中文 | [English](https://github.com/baranwang/mcp-tung-shing/blob/HEAD/README.en.md)

> 中国传统黄历（通胜）计算服务，基于 Model Context Protocol (MCP)

## ✨ 功能特点

- 📅 **公历农历转换** - 支持公历与农历日期的相互转换
- 🍀 **每日宜忌** - 提供每日吉凶、宜忌活动的详细信息
- 🕐 **时辰信息** - 十二时辰（子、丑、寅等）的吉凶宜忌
- 🔮 **命理元素** - 五行、神煞、星宿等传统命理学详细数据

## 🚀 安装与使用

在你的 MCP 配置文件中添加以下内容：

```json
{
  "mcpServers": {
    "tung-shing": {
      "command": "npx",
      "args": ["-y", "mcp-tung-shing@latest"]
    }
  }
}
```

## ⚙️ 工具

### get-tung-shing

获取指定日期的黄历信息

**参数:**

| 参数名         | 类型             | 必填 | 默认值 | 描述                                  |
| -------------- | ---------------- | ---- | ------ | ------------------------------------- |
| `startDate`    | string           | 否   | 当天   | 开始日期，格式："YYYY-MM-DD"          |
| `days`         | number           | 否   | 1      | 获取天数                              |
| `includeHours` | boolean          | 否   | false  | 是否包含时辰信息                      |
| `tabooFilters` | array            | 否   | -      | 筛选宜忌事项类型，条件之间为或关系     |
| `tabooFilters[].type`   | 1 | 2  | 是   | -      | 过滤类型：宜(1)、忌(2)                |
| `tabooFilters[].value`  | string  | 是   | -      | 要筛选的宜忌事项                      |

## 🤝 贡献

欢迎提交 Issues 和 Pull Requests 来完善此项目。

**官方网站：** [https://github.com/baranwang/mcp-tung-shing](https://github.com/baranwang/mcp-tung-shing)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`art and culture`, `other`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y mcp-tung-shing@latest`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/baranwang-tung-shing.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
