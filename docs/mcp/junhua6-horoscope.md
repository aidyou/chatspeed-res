---
title: "Horoscope"
description: "Horoscope Luck"
---

# Horoscope

Horoscope Luck

# Horoscope Zodiac Fortune:
This is an MCP that allows you to query zodiac information. You can input a birthday to get the corresponding zodiac sign and its attributes. The supported birthday formats are: YYYY-MM-DD, MM/DD, or YYYY年MM月DD日. The response you will receive is as follows:
Your zodiac sign is: Gemini.
# Zodiac Attributes:
Element: Air
Mode: Mutable
Ruling Planet: Mercury

**Official site: ** [https://www.modelscope.cn/studios/junhua6/Horoscope](https://www.modelscope.cn/studios/junhua6/Horoscope)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `art and culture`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `mcp-remote https://junhua6-horoscope.ms.show/gradio_api/mcp/sse --transport sse-only`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/junhua6-horoscope.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
