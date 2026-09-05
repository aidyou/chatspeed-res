---
title: "MatherMCP"
description: "lunerinfo Daily Almanac This is an MCP that can fetch the almanac information for a specific day. You can input either an empty string or a date to get the almanac for the current day or a specific da…"
---

# MatherMCP

lunerinfo Daily Almanac This is an MCP that can fetch the almanac information for a specific day. You can input either an empty string or a date to get the almanac for the current day or a specific da…

# luner_info Daily Almanac
This is an MCP that can fetch the almanac information for a specific day. You can input either an empty string or a date to get the almanac for the current day or a specific day. The date format should be: 1991年1月1日 or 1991-01-01.

The response you receive will look like this:

日期 : 2025-07-01 00:00:00
农历 : 二零二五 乙巳[蛇]年 六月大初七
星期 : 星期二
八字 : 乙巳 壬午 辛未 戊子
今日节气: 无
下一节气: ('小暑', (7, 7), 2025)
季节 : 仲夏
生肖冲煞: 羊日冲牛
星座 : 巨蟹座
吉神方位: ['喜神西南', '财神正东', '福神西北', '阳贵东北', '阴贵正南']
宜 : ['祭祀', '出行', '宴会', '沐浴', '剃头', '修造', '上表章', '上官', '进人口', '竖柱上梁', '经络', '纳财', '扫舍宇', '栽种', '牧养', '破土', '安葬', '祈福', '恤孤茕', '举正直', '裁制', '纳采', '搬移', '招贤', '宣政事', '覃恩', '施恩', '安抚边境', '解除', '求嗣', '整手足甲', '庆赐', '修仓库', '立券交易', '选将', '营建', '上册', '出师', '临政', '纳畜', '缮城郭', '整容', '颁诏', '雪冤']
忌 : ['畋猎', '取鱼']

**Official site: ** [https://modelscope.cn/studios/modelscope/mcp-inspector](https://modelscope.cn/studios/modelscope/mcp-inspector)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `productivity`
- Tags: `calendar management`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `mcp-remote https://minmin1023-luner-info1.ms.show/gradio_api/mcp/sse --transport sse-only`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/vincentxing-mathermcp.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
