---
title: "景点智能推荐"
description: "景点智能推荐 MCP Server（mcp-poi-smart-recommend） 一、产品介绍 以景点推荐为核心的 6 合 1 智能推荐服务，覆盖从「想去哪玩」到「怎么去」的全流程。结合飞猪旅行门票数据与高德地图位置服务，提供 AI 推荐、结构化搜索、周边发现、天气预报、交通规划等能力。 二、工具能力 ▸ recommendpoi：AI 智能推荐景点，自然语言描述即可返回最合适的景点及门票价格与预订链接 ▸ searchpoi：结构化搜索景点门票，支持按城市、关键词、类型、等级多维筛选 ▸ searchfast"
---

# 景点智能推荐

景点智能推荐 MCP Server（mcp-poi-smart-recommend） 一、产品介绍 以景点推荐为核心的 6 合 1 智能推荐服务，覆盖从「想去哪玩」到「怎么去」的全流程。结合飞猪旅行门票数据与高德地图位置服务，提供 AI 推荐、结构化搜索、周边发现、天气预报、交通规划等能力。 二、工具能力 ▸ recommendpoi：AI 智能推荐景点，自然语言描述即可返回最合适的景点及门票价格与预订链接 ▸ searchpoi：结构化搜索景点门票，支持按城市、关键词、类型、等级多维筛选 ▸ searchfast

景点智能推荐 MCP Server（mcp-poi-smart-recommend）

一、产品介绍

以景点推荐为核心的 6 合 1 智能推荐服务，覆盖从「想去哪玩」到「怎么去」的全流程。结合飞猪旅行门票数据与高德地图位置服务，提供 AI 推荐、结构化搜索、周边发现、天气预报、交通规划等能力。

二、工具能力

▸ recommend_poi：AI 智能推荐景点，自然语言描述即可返回最合适的景点及门票价格与预订链接

▸ search_poi：结构化搜索景点门票，支持按城市、关键词、类型、等级多维筛选

▸ search_fast：极速搜索，快速查询景点、门票、线路等信息

▸ nearby_poi：周边景点发现，基于位置搜索附近景点，返回距离、评分、地址

▸ search_weather：查询目的地天气预报，辅助出行决策

▸ search_transport：交通方案规划，含打车预估、地铁/公交换乘方案 + 一键打车链接

三、使用场景

▸ 出行规划：根据兴趣偏好推荐目的地景点

▸ 门票查询：按城市、类型、等级搜索景点门票价格和预订链接

▸ 周边游玩：基于当前位置发现附近隐藏好去处

▸ 出行准备：提前了解目的地天气和交通方案

四、使用方式

本 MCP 服务通过 PyPI 分发，使用以下命令安装：

bash
1
2
pip install mcp-poi-smart-recommend



安装后在 MCP 客户端配置中添加 Server 命令：

bash
1
2
mcp-poi-smart-recommend



五、参数说明

recommend_poi（AI 智能推荐）

▸ query（必填）：景点推荐描述，自然语言，如「三亚适合亲子的海边景点」「杭州 5A 景区推荐」

search_poi（结构化搜索景点门票）

▸ cityName（必填）：城市名，如杭州、西安

▸ keyword（可选）：景点名称关键词，如故宫、长城、迪士尼

▸ category（可选）：景点类型，如自然风光、主题乐园、人文古迹

▸ poiLevel（可选）：景点等级 1-5（5 为 5A），0 表示不限

search_fast（极速搜索）

▸ query（必填）：搜索词，如三亚景点、北京故宫门票、上海迪士尼

nearby_poi（周边景点发现）

▸ location（必填）：当前位置或地标，如西湖、外滩、故宫

▸ city（可选）：所在城市，如杭州、上海、北京

▸ radius（可选）：搜索半径（米），默认 3000

search_weather（天气预报）

▸ query（必填）：天气查询描述，如三亚天气预报、杭州明天天气

search_transport（交通方案）

▸ query（必填）：交通查询描述，如「浦东机场到外滩（上海）」「北京南站到故宫」

**官方网站：** [https://pypi.org/project/mcp-poi-smart-recommend/](https://pypi.org/project/mcp-poi-smart-recommend/)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`search`, `developer tools`, `location services`, `景点推荐`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`mcp-poi-smart-recommend==5.0.1`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/mako2026-smartpoi.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
