---
title: "全球航班查询与预订"
description: "✈️ RollingGo全球航班查询与预订 一句话查全球航班，支持中文城市名直接输入，直飞与中转分开展示，航司中文映射，非民用机场过滤，性价比标签一目了然。新增座位余量和行李额度查询，出行信息一次掌握。 ✨ 核心特性 ▸ 中文城市名直接输入 — 100+城市映射，说\"北京飞东京\"即可查询，无需记忆机场代码 ▸ 航司代码中文映射 — 60+航司，CA→国航、NH→全日空、SQ→新航，阅读无障碍 ▸ 非民用机场过滤 — 自动排除军用基地、轮渡码头、直升机坪等非民用设施 ▸ 中转等待时间 — 中转方案清晰展示等待时长，方"
---

# 全球航班查询与预订

✈️ RollingGo全球航班查询与预订 一句话查全球航班，支持中文城市名直接输入，直飞与中转分开展示，航司中文映射，非民用机场过滤，性价比标签一目了然。新增座位余量和行李额度查询，出行信息一次掌握。 ✨ 核心特性 ▸ 中文城市名直接输入 — 100+城市映射，说"北京飞东京"即可查询，无需记忆机场代码 ▸ 航司代码中文映射 — 60+航司，CA→国航、NH→全日空、SQ→新航，阅读无障碍 ▸ 非民用机场过滤 — 自动排除军用基地、轮渡码头、直升机坪等非民用设施 ▸ 中转等待时间 — 中转方案清晰展示等待时长，方

✈️ RollingGo全球航班查询与预订

一句话查全球航班，支持中文城市名直接输入，直飞与中转分开展示，航司中文映射，非民用机场过滤，性价比标签一目了然。新增座位余量和行李额度查询，出行信息一次掌握。

✨ 核心特性

▸ 中文城市名直接输入 — 100+城市映射，说"北京飞东京"即可查询，无需记忆机场代码

▸ 航司代码中文映射 — 60+航司，CA→国航、NH→全日空、SQ→新航，阅读无障碍

▸ 非民用机场过滤 — 自动排除军用基地、轮渡码头、直升机坪等非民用设施

▸ 中转等待时间 — 中转方案清晰展示等待时长，方便评估换乘合理性

▸ 性价比标签 SmartValueScore — 综合价格、时长、时刻评分，快速识别高性价比航班

▸ 座位余量查询 — 查看航班各舱位可用座位分布，选座购票心中有数

▸ 行李额度查询 — 托运和随身行李限额一目了然，避免超规收费

🛠 工具

search_flights — 全球航班查询

查询全球航班实时价格与时刻表，支持中文城市名、舱位筛选、单程/往返，直飞与中转分开展示。

参数：

▸ from_city（必填）— 出发城市，支持中文（如"北京"、"上海"、"东京"）或城市代码（如"BJS"、"SHA"），中文自动映射为代码

▸ to_city（必填）— 到达城市，支持中文（如"三亚"、"首尔"、"曼谷"）或城市代码（如"SYX"、"SEL"、"BKK"）

▸ from_date（必填）— 出发日期，格式 YYYY-MM-DD，如"2026-06-15"

▸ from_airport（可选）— 出发机场代码，如"PEK"、"PVG"，用于精确指定机场

▸ to_airport（可选）— 到达机场代码，如"NRT"、"HKT"，用于精确指定机场

▸ cabin_grade（可选）— 舱位等级：ECONOMY=经济舱（默认）、BUSINESS=商务舱、FIRST=头等舱

▸ trip_type（可选）— 行程类型：ONE_WAY=单程（默认）、ROUND_TRIP=往返

▸ ret_date（可选）— 返程日期，往返时必填，格式 YYYY-MM-DD

▸ adult_number（可选）— 成人数量，默认1

▸ child_number（可选）— 儿童数量，默认0

search_airports — 机场/城市代码查询

按关键词查找机场信息，返回cityCode和airportCode用于查航班。中文城市名优先走内置映射，自动过滤非民用机场。

参数：

▸ keyword（必填）— 搜索关键词，支持城市名（如"杭州"）、机场名（如"浦东"）、或IATA代码（如"PVG"）

check_flight_seats — 座位余量查询

查询指定航班的可用座位分布，支持按舱位筛选，出行前掌握座位情况，选座购票更有底气。

参数：

▸ flight_id（必填）— 航班ID，从 search_flights 结果中获取

▸ cabin_grade（可选）— 舱位等级：ECONOMY=经济舱（默认）、BUSINESS=商务舱、FIRST=头等舱

check_baggage_allowance — 行李额度查询

查询航班托运和随身行李限额，不同舱位不同航司政策不同，出行前确认避免超规收费。

参数：

▸ flight_id（必填）— 航班ID，从 search_flights 结果中获取

▸ cabin_grade（可选）— 舱位等级：ECONOMY=经济舱（默认）、BUSINESS=商务舱、FIRST=头等舱

📝 使用示例

▸ "明天上海飞北京航班有哪些" → search_flights(from_city="上海", to_city="北京", from_date="2026-06-04")

▸ "下周北京去东京的机票多少钱" → search_flights(from_city="北京", to_city="东京", from_date="2026-06-10")

▸ "暑假广州去曼谷一家三口经济舱" → search_flights(from_city="广州", to_city="曼谷", from_date="2026-07-01", adult_number=2, child_number=1)

▸ "上海到巴黎商务舱往返" → search_flights(from_city="上海", to_city="巴黎", from_date="2026-07-01", trip_type="ROUND_TRIP", ret_date="2026-07-10", cabin_grade="BUSINESS")

▸ "杭州有哪些机场" → search_airports(keyword="杭州")

▸ "PVG是哪个机场" → search_airports(keyword="PVG")

▸ "这个航班还有座位吗" → check_flight_seats(flight_id="CA1234", cabin_grade="ECONOMY")

▸ "这趟航班能托运多少行李" → check_baggage_allowance(flight_id="CA1234", cabin_grade="ECONOMY")

适用场景

▸ 商务出行 — 快速查询航班时刻与价格，直飞中转方案分开呈现，高效比价决策

▸ 旅行规划 — 中文城市名直接输入，无需查机场代码，一站式完成航班搜索

▸ 座位确认 — 查看航班座位余量，热门航班提前了解满座情况

▸ 行李准备 — 出发前确认行李额度，避免到机场才发现超规收费

▸ 机场信息确认 — 不确定城市对应哪个机场时，快速查询cityCode和airportCode

**官方网站：** [https://pypi.org/project/mcp-rollinggo-flight/](https://pypi.org/project/mcp-rollinggo-flight/)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`search`, `developer tools`, `全球航班`, `航班查询`, `机票搜索`, `国际航班`, `国内航班`, `ai航班查询`, `机票比价`, `机票查询`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`mcp-rollinggo-flight==2.0.1`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/mako2026-rollinggo-flight.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
