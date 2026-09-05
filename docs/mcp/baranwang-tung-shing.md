---
title: "mcp-tung-shing"
description: "Tung Shing MCP Service Simplified Chinese English A traditional Chinese almanac (Tung Shing) calculation service, based on the Model Context Protocol (MCP) ✨ Features - 📅 Gregorian and Lunar Calendar…"
---

# mcp-tung-shing

Tung Shing MCP Service Simplified Chinese English A traditional Chinese almanac (Tung Shing) calculation service, based on the Model Context Protocol (MCP) ✨ Features - 📅 Gregorian and Lunar Calendar…

# Tung Shing MCP Service

[Smithery](https://smithery.ai/server/@baranwang/mcp-tung-shing)
[![NPM Version](/mcp-assets/a54621745a6198c873e1ad8fc7327b2b.svg)](https://www.npmjs.com/package/mcp-tung-shing)
[![License](/mcp-assets/5816f652aa1f0cc4eedb21a2f733e09e.svg)](https://github.com/baranwang/mcp-tung-shing/blob/main/LICENSE)

Simplified Chinese | [English](https://github.com/baranwang/mcp-tung-shing/blob/HEAD/README.en.md)

> A traditional Chinese almanac (Tung Shing) calculation service, based on the Model Context Protocol (MCP)

## ✨ Features

- 📅 **Gregorian and Lunar Calendar Conversion** - Supports mutual conversion between Gregorian and lunar dates
- 🍀 **Daily Auspicious and Inauspicious Activities** - Provides detailed information on daily fortune, auspicious, and inauspicious activities
- 🕐 **Hour Information** - Details of fortune, auspicious, and inauspicious activities for the twelve hours (Zi, Chou, Yin, etc.)
- 🔮 **Astrological Elements** - Detailed data on traditional astrology including the Five Elements, Deities, and Constellations

## 🚀 Installation and Usage

Add the following to your MCP configuration file:

json
{
  "mcpServers": {
    "tung-shing": {
      "command": "npx",
      "args": ["-y", "mcp-tung-shing@latest"]
    }
  }
}

## ⚙️ Tools

### get-tung-shing

Fetches almanac information for a specified date.

**Parameters:**

| Parameter Name   | Type             | Required | Default | Description                                      |
| ---------------- | ---------------- | -------- | ------- | ------------------------------------------------ |
| `startDate`      | string           | No       | Today   | Start date, format: "YYYY-MM-DD"                 |
| `days`           | number           | No       | 1       | Number of days to fetch                          |
| `includeHours`   | boolean          | No       | false   | Whether to include hour information              |
| `tabooFilters`   | array            | No       | -       | Filter types of auspicious and inauspicious activities, conditions are OR-based |
| `tabooFilters[].type` | 1 | 2  | Yes     | -      | Filter type: Auspicious (1), Inauspicious (2)    |
| `tabooFilters[].value` | string  | Yes   | -      | The specific auspicious or inauspicious activity to filter |

## 🤝 Contributions

We welcome Issues and Pull Requests to improve this project.

**Official site: ** [https://github.com/baranwang/mcp-tung-shing](https://github.com/baranwang/mcp-tung-shing)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `art and culture`, `other`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y mcp-tung-shing@latest`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/baranwang-tung-shing.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
