---
title: "luner_info"
description: "lunermcp This is an MCP that can fetch the lunar calendar information for a specific day. You can input an empty value or a date to get the lunar calendar information for that day or the current day."
---

# luner_info

lunermcp This is an MCP that can fetch the lunar calendar information for a specific day. You can input an empty value or a date to get the lunar calendar information for that day or the current day.

# luner_mcp
This is an MCP that can fetch the lunar calendar information for a specific day. You can input either an empty value or a date to get the lunar calendar information for that day or the current day. The date format should be: 1991年1月1日 or 1991-01-01.

The response you will receive is as follows:

日期	:	2025-07-01 00:00:00
农历	:	二零二五 乙巳[蛇]年 六月大初七
星期	:	Tuesday
八字	:	乙巳 壬午 辛未 戊子
今日节气:	None
下一节气:	('小暑', (7, 7), 2025)
季节	:	Midsummer
生肖冲煞:	Sheep day clashes with Ox
星座	:	Cancer
吉神方位:	['Joy God Southwest', 'Wealth God East', 'Blessing God Northwest', 'Yang Noble Northeast', 'Yin Noble South']
宜		:	['Sacrifice', 'Travel', 'Banquet', 'Bathing', 'Haircut', 'Construction', 'Submitting Petitions', 'Taking Office', 'Admitting People', 'Erecting Beams and Columns', 'Acupuncture', 'Gaining Wealth', 'Cleaning House', 'Planting', 'Rearing Livestock', 'Breaking Ground', 'Burial', 'Praying for Blessings', 'Caring for Orphans and Widows', 'Promoting Uprightness', 'Tailoring', 'Engagement', 'Moving', 'Recruiting Talents', 'Announcing Government Affairs', 'Granting Pardon', 'Bestowing Favors', 'Pacifying Borders', 'Resolving Disputes', 'Seeking Heirs', 'Trimming Nails', 'Granting Rewards', 'Repairing Granaries', 'Signing Contracts', 'Selecting Generals', 'Building Fortifications', 'Registering Titles', 'Dispatching Troops', 'Exercising Governance', 'Acquiring Livestock', 'Repairing City Walls', 'Grooming', 'Issuing Edicts', 'Redressing Wrongs']
忌		:	['Hunting', 'Fishing']

**Official site: ** [https://github.com/Bald0Wang/luner_mcp](https://github.com/Bald0Wang/luner_mcp)
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

Resource file: `resources/mcp/minmin1023-luner-info.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
