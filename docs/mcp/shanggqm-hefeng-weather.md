---
title: "和风天气"
description: "使用和风天气API为中国地区的地点提供天气预报数据，包括实时、逐小时或逐日的预报以及基于位置的查询。"
---

# 和风天气

使用和风天气API为中国地区的地点提供天气预报数据，包括实时、逐小时或逐日的预报以及基于位置的查询。

# HeFeng 天气 MCP 服务器

一个通过 HeFeng 天气 API 提供中国各地天气预报数据的 Model Context Protocol 服务器。

## 功能

- 获取实时天气数据
- 获取每小时天气预报（24小时/72小时/168小时）
- 获取每日天气预报（3天/7天/10天/15天/30天）
- 支持通过经纬度坐标查询位置
- 完全中文天气描述

## API

此 MCP 服务器提供以下工具：

### get-weather

获取特定位置的天气预报数据。

# 使用 MCP 主机（例如 Claude Desktop）

将以下内容添加到你的 claude_desktop_config.json 文件中

## NPX

```json
{
  "mcpServers": {
    "hefeng-weather": {
      "command": "npx",
      "args": ["hefeng-mcp-weather@latest", "--apiKey=${API_KEY}"]
    }
  }
}
```

# 许可证

该 MCP 服务器根据 MIT 许可证进行许可。这意味着您可以自由使用、修改和分发软件，但须遵守 MIT 许可证的条款和条件。有关更多详细信息，请参阅项目存储库中的 LICENSE 文件。

**官方网站：** [https://github.com/shanggqm/hefeng-mcp-weather](https://github.com/shanggqm/hefeng-mcp-weather)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`location services`, `travel and transportation`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`hefeng-mcp-weather@latest --apiKey=${API_KEY}`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/shanggqm-hefeng-weather.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
