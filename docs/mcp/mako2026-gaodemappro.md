---
title: "高德地图全能版"
description: "🗺️ 高德地图MCP服务 免Key即用的高德地图MCP服务，17项位置能力全覆盖，无需申请高德API Key，开箱即用。 ✨ 核心特性 ▸ 零配置 — 无需申请高德API Key，无需填写任何环境变量，MCP URL直连即用 ▸ 17项能力 — 地理编码、POI搜索、路线规划、天气查询、行政区划等全面覆盖 ▸ 地址版路线 — 直接输入地址即可规划驾车/公交/步行/骑行路线，无需手动转换经纬度 ▸ 独家能力 — 输入提示（搜索框自动补全）、行政区划查询，其他高德MCP均无 ▸ 企业级代理 — 服务端托管API Key"
---

# 高德地图全能版

🗺️ 高德地图MCP服务 免Key即用的高德地图MCP服务，17项位置能力全覆盖，无需申请高德API Key，开箱即用。 ✨ 核心特性 ▸ 零配置 — 无需申请高德API Key，无需填写任何环境变量，MCP URL直连即用 ▸ 17项能力 — 地理编码、POI搜索、路线规划、天气查询、行政区划等全面覆盖 ▸ 地址版路线 — 直接输入地址即可规划驾车/公交/步行/骑行路线，无需手动转换经纬度 ▸ 独家能力 — 输入提示（搜索框自动补全）、行政区划查询，其他高德MCP均无 ▸ 企业级代理 — 服务端托管API Key

🗺️ 高德地图MCP服务

免Key即用的高德地图MCP服务，17项位置能力全覆盖，无需申请高德API Key，开箱即用。

✨ 核心特性

▸ 零配置 — 无需申请高德API Key，无需填写任何环境变量，MCP URL直连即用

▸ 17项能力 — 地理编码、POI搜索、路线规划、天气查询、行政区划等全面覆盖

▸ 地址版路线 — 直接输入地址即可规划驾车/公交/步行/骑行路线，无需手动转换经纬度

▸ 独家能力 — 输入提示（搜索框自动补全）、行政区划查询，其他高德MCP均无

▸ 企业级代理 — 服务端托管API Key，稳定可靠，不受个人Key日限额限制

🛠 工具

geocode — 地理编码

将详细的结构化地址转换为经纬度坐标，支持对地标性名胜景区、建筑物名称解析。

▸ address — 结构化地址，如"北京市朝阳区阜通东大街6号"

▸ city — 指定查询的城市（可选），如"北京"

regeocode — 逆地理编码

将高德经纬度坐标转换为行政区划地址信息。

▸ location — 经纬度坐标，格式"lng,lat"，如"116.397428,39.90923"

poi_search — 关键词搜索POI

根据关键词搜索POI兴趣点，返回相关的位置信息列表。

▸ keywords — 搜索关键词，如"餐厅"、"如家酒店"

▸ city — 查询城市（可选），如"北京"

▸ citylimit — 是否限制城市范围内搜索，"true"或"false"，默认"false"

poi_around — 周边搜索POI

根据中心点坐标和关键词搜索指定半径范围内的兴趣点。

▸ location — 中心点经纬度，格式"lng,lat"

▸ keywords — 搜索关键词（可选），如"加油站"

▸ radius — 搜索半径，单位米，默认1000，最大50000

poi_detail — POI详情

查询POI的详细信息，需提供关键词搜索或周边搜索获取到的POI ID。

▸ id — POI ID，从关键词搜索或周边搜索结果中获取

input_tips — 输入提示

根据用户输入的关键词返回匹配的POI建议列表，适用于搜索框自动补全场景。

▸ keywords — 输入关键词，如"肯德基"

▸ city — 查询城市（可选）

▸ datatype — 数据类型，"all"全部/"poi"仅POI/"bus"仅公交，默认"all"

driving_route — 驾车路线规划

根据起终点经纬度规划驾车出行方案。

▸ origin — 起点经纬度，格式"lng,lat"

▸ destination — 终点经纬度，格式"lng,lat"

transit_route — 公交路线规划

综合火车、公交、地铁等公共交通方式规划出行方案，跨城场景下必须传终点城市。

▸ origin — 起点经纬度，格式"lng,lat"

▸ destination — 终点经纬度，格式"lng,lat"

▸ city — 起点城市，如"北京"

▸ cityd — 终点城市（跨城时必填），如"上海"

walking_route — 步行路线规划

根据起终点经纬度规划100km以内的步行出行方案。

▸ origin — 起点经纬度，格式"lng,lat"

▸ destination — 终点经纬度，格式"lng,lat"

cycling_route — 骑行路线规划

根据起终点经纬度规划骑行出行方案，最大支持500km。

▸ origin — 起点经纬度，格式"lng,lat"

▸ destination — 终点经纬度，格式"lng,lat"

driving_route_by_address — 驾车路线（地址版）

直接输入地址即可规划驾车路线，无需手动转换经纬度，推荐优先使用。

▸ origin_address — 起点地址，如"北京市朝阳区阜通东大街6号"

▸ destination_address — 终点地址，如"北京市海淀区上地十街10号"

▸ origin_city — 起点城市（可选），用于提高地理编码准确性

▸ destination_city — 终点城市（可选）

transit_route_by_address — 公交路线（地址版）

直接输入地址即可规划公交路线，无需手动转换经纬度，推荐优先使用。

▸ origin_address — 起点地址

▸ destination_address — 终点地址

▸ city — 起点城市

▸ cityd — 终点城市（跨城时必填）

▸ origin_city — 起点城市（地理编码用，可选）

▸ destination_city — 终点城市（地理编码用，可选）

walking_route_by_address — 步行路线（地址版）

直接输入地址即可规划步行路线，无需手动转换经纬度。

▸ origin_address — 起点地址

▸ destination_address — 终点地址

▸ origin_city — 起点城市（可选）

▸ destination_city — 终点城市（可选）

cycling_route_by_address — 骑行路线（地址版）

直接输入地址即可规划骑行路线，无需手动转换经纬度。

▸ origin_address — 起点地址

▸ destination_address — 终点地址

▸ origin_city — 起点城市（可选）

▸ destination_city — 终点城市（可选）

weather — 天气查询

根据城市名称或adcode查询指定城市的天气信息。

▸ city — 城市名称或adcode，如"北京"或"110000"

district — 行政区划查询

查询省、市、区县的行政区划信息，支持关键词搜索和层级控制。

▸ keywords — 查询关键词（可选），如"北京"；留空则返回全国省级列表

▸ subdistrict — 子级层数，0不返回/1返回一级/2返回二级/3返回三级，默认1

ip_location — IP定位

根据IP地址定位所在位置，不传IP则定位当前请求的IP。

▸ ip — IP地址（可选），如"114.247.50.1"；留空则定位当前IP

📝 使用示例

▸ "帮我查北京天安门的经纬度" → geocode

▸ "附近3公里内有什么加油站" → poi_around

▸ "从北京站到天安门怎么走" → walking_route_by_address

▸ "北京到上海驾车路线" → driving_route_by_address

▸ "上海明天天气怎么样" → weather

▸ "输入'肯德'能推荐什么" → input_tips

适用场景

▸ 旅行规划Agent的位置查询与路线规划

▸ 本地生活助手的POI搜索与周边推荐

▸ 智能客服的地址解析与天气查询

▸ IDE插件的地理解码与出行建议

**官方网站：** [https://pypi.org/project/mcp-gaode-map/](https://pypi.org/project/mcp-gaode-map/)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`search`, `developer tools`, `location services`, `高德地图`, `路线规划`, `周边搜索`, `位置服务`, `驾车导航`, `步行导航`, `骑行路线`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`--from mcp-gaode-map==1.2.0 mcp-gaode-map`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/mako2026-gaodemappro.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
