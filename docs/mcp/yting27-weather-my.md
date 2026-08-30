---
title: "MCP天气预报服务"
description: "提供与洪水相关的水位、天气预报、警报以及地震报告的模型上下文协议（MCP）服务器，数据来源于马来西亚政府的开放API。"
---

# MCP天气预报服务

提供与洪水相关的水位、天气预报、警报以及地震报告的模型上下文协议（MCP）服务器，数据来源于马来西亚政府的开放API。

# 天气 MCP 服务器

这是一个基本的模型上下文协议（MCP）服务器，它从马来西亚官方开放数据门户的开放 API 中获取天气信息。
该服务器使 LLMs 能够获取天气预报、警告、与洪水相关的水位以及地震报告。

API 文档：[data.gov.my](https://developer.data.gov.my/)

## 组件

### 工具

1. get_water_level_condition
    - 获取指定地区或州的洪水预警相关水位情况。
        如果同时提供了地区和州，则优先考虑地区。
        如果未指定地区或州，则将该字段留空。

    - 参数：
        - district: 指定州内要检索洪水预警条件的地区的名称。
        - state: 马来西亚要检索洪水预警条件的州的名称。

2. get_warning
    - 在指定日期范围内检索发布的通用天气警告。

    - 参数：
        - datetime_start: 以 `YYYY-MM-DD HH:MM:SS` 格式表示的最早时间戳（包含），从此时间戳开始检索天气警告。如果省略，默认为当前日期。
        - datetime_end: 以 `YYYY-MM-DD HH:MM:SS` 格式表示的最晚时间戳（包含），在此时间戳之前停止检索天气警告。如果省略，默认为当前日期。

3. get_weather_forecast
    - 在给定日期范围内检索特定地点的天气预报。

    - 参数：
        - location_name: 要检索预报的地点的名称或标识符。
        - date_start: 最早日期（包含），从此日期开始检索天气预报。如果省略，默认为当前日期。
        - date_end: 最晚日期（包含），在此日期之前停止检索天气预报。如果省略，默认为当前日期。

4. get_earthquake_news
    - 在指定日期范围内获取给定地点的地震新闻。

    - 参数：
        - location: 发生地震的地方的名称或标识符。
        - date_start: 最早日期（包含），从此日期开始搜索地震新闻。如果省略，默认为当前日期。
        - date_end: 最晚日期（包含），在此日期之前停止搜索地震新闻。如果省略，默认为当前日期。

## Claude Desktop 配置

将以下内容添加到 `claude_desktop_config.json` 文件中。更多信息，请参阅 [For Claude Desktop Users](https://modelcontextprotocol.io/quickstart/user)。

```json
{
    "mcpServers": {
        "weather": {
            "command": "uv",
            "args": [
                "--directory",
                "weather-my-mcp",
                "run",
                "weather.py"
            ]
        }
    }
}
```

## 许可证

此 MCP 服务器根据 MIT 许可证许可。这意味着您可以在遵守 MIT 许可证条款和条件的前提下自由使用、修改和分发该软件。更多详细信息，请参见项目存储库中的 LICENSE 文件。

**官方网站：** [https://github.com/yting27/weather-my-mcp](https://github.com/yting27/weather-my-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`, `data`
- 标签：`search`, `location services`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`--directory weather-my-mcp run weather.py`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/yting27-weather-my.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
