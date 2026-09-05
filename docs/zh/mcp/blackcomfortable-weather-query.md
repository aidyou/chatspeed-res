---
title: "天气 查询"
description: "获取指定条件的天气信息（MCP标准化接口）。 解决的核心痛点：替代手动查询天气的重复劳动，支持多场景自动化整合（如旅游攻略、办公提醒、农业预警）。 Args: location (str, 必填): 具体城市/区域（如\"北京市朝阳区\"、\"巴黎\"），需明确到城市级； timerange (str, 可选): 时间范围，可选值为[\"实时\", \"未来1天\", \"未来3天\"]，默认\"实时\"； needty…"
---

# 天气 查询

获取指定条件的天气信息（MCP标准化接口）。 解决的核心痛点：替代手动查询天气的重复劳动，支持多场景自动化整合（如旅游攻略、办公提醒、农业预警）。 Args: location (str, 必填): 具体城市/区域（如"北京市朝阳区"、"巴黎"），需明确到城市级； timerange (str, 可选): 时间范围，可选值为["实时", "未来1天", "未来3天"]，默认"实时"； needty…

获取指定条件的天气信息（MCP标准化接口）。  
    解决的核心痛点：替代手动查询天气的重复劳动，支持多场景自动化整合（如旅游攻略、办公提醒、农业预警）。  

    Args:  
        location (str, 必填): 具体城市/区域（如"北京市朝阳区"、"巴黎"），需明确到城市级；  
        time_range (str, 可选): 时间范围，可选值为["实时", "未来1天", "未来3天"]，默认"实时"；  
        need_type (str, 可选): 需求类型，可选值为["综合", "温度+降水", "风力+空气质量"]，默认"综合"。  

    Returns:  
        tuple[Dict, str]: 结构化数据（用于MCP集成）、人性化反馈（用于直接展示）。

**官方网站：** [https://www.modelscope.cn/studios/blackcomfortable/weather_query](https://www.modelscope.cn/studios/blackcomfortable/weather_query)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`
- 标签：`search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`mcp-remote https://blackcomfortable-weather-query.ms.show/gradio_api/mcp/sse --transport sse-only`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/blackcomfortable-weather-query.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
