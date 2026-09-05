---
title: "mcp-youth-activities"
description: "A server based on the Model Context Protocol (MCP) for scraping and parsing the latest activity information of the Chengdu Youth Home. (The scope will be expanded later.)"
---

# mcp-youth-activities

A server based on the Model Context Protocol (MCP) for scraping and parsing the latest activity information of the Chengdu Youth Home. (The scope will be expanded later.)

# MCP Server · Chengdu Youth Home Activity Scraper

A server based on [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) for scraping and parsing the latest activity information from [Chengdu Youth Home](https://cdyouth.cdcyl.org.cn/jgc/).

This project provides an MCP Tool: `fetch_chengdu_youth_activities`

---

## ✨ Features

- 🔍 **Scrape Activity Information**: Fetch the latest activities from `https://cdyouth.cdcyl.org.cn/jgc/`.
- 📝 **Automatic Parsing**: Extract activity title, tags, time, location, status, views, images, etc.
- 📦 **MCP Tool Interface**: Can be directly used in MCP-compatible clients (e.g., Anthropic MCP Inspector).
- 🔄 **SSE Transport**: Implemented using Server-Sent Events (compatible with older MCP clients).
- 🧩 **Structured Output**: Returns a JSON array, including human-readable text.

---

## 📦 Installation and Running

### 1. Clone the Repository
bash
git clone https://github.com//mcp-chengdu-youth-activities.git
cd mcp-chengdu-youth-activities

**Official site: ** [https://github.com/fsyj123/mcp-chengdu-youth-activities](https://github.com/fsyj123/mcp-chengdu-youth-activities)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `art and culture`, `娱乐`, `生活`, `线下活动`, `成都`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `mcp-cd-youth`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/fsyj123-youth-activities.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
