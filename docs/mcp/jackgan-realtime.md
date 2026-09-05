---
title: "realtime"
description: "Global timezone time lookup: a web application built with Python and Gradio that fetches detailed time information for any timezone in the world in real time. Features include: - time lookup using sta…"
---

# realtime

Global timezone time lookup: a web application built with Python and Gradio that fetches detailed time information for any timezone in the world in real time. Features include: - time lookup using sta…

# Global Timezone Time Lookup

## Project Introduction

The Global Timezone Time Lookup is a web application built with Python and Gradio that can fetch detailed time information for any timezone in the world in real time. Its features include:

- Time lookup using standard timezone formats (such as "Asia/Shanghai", "America/New_York", etc.)
- Default display of China Standard Time (UTC+8)
- Detailed time information including current time, date, weekday, year, month, hour, minute, second, etc.
- Computes and displays the UTC offset, with Chinese-friendly time difference descriptions
- Shows the day of the year and week of the year
- Daylight saving time detection
- An intuitive web interface with example queries

This tool can be used not only as a standalone time lookup app, but also to help LLMs get the current time when their time-related instructions are ambiguous (e.g. "recent", "lately"), improving the accuracy of time-related Q&A.

## Deployment Guide

### Environment Requirements

- Python 3.9+ (Python 3.10 or higher recommended)
- pip package manager

### Install Dependencies

The project depends on the following Python libraries:
- gradio: for creating the web interface
- zoneinfo: for timezone handling (built into Python 3.9+)
- datetime: for date/time handling (Python standard library)

Install the required dependencies with pip:

```bash
pip install gradio
```

### Run the Project

1. Make sure all dependencies are installed
2. Run the following command in the project directory:

```bash
python time2.py
```

3. After the app starts, the console shows the local access URL (usually http://127.0.0.1:7863) and a public access URL
4. Open the local access URL in your browser to use the app

## Usage Examples

### Basic usage

1. Open the Global Timezone Time Lookup web interface
2. It shows detailed info for China Standard Time (UTC+8) by default
3. Enter another timezone name in the input box (e.g. "America/New_York") and click the submit button to get the time info for that timezone

### Example queries

The app provides example queries for several common timezones; click the example buttons to view them quickly:

- UTC: Coordinated Universal Time
- Asia/Shanghai: China Standard Time
- America/New_York: New York time
- Europe/London: London time
- Asia/Tokyo: Tokyo time

### Interpreting the output

Query results include:

- Timezone name
- Timezone abbreviation
- Current time (YYYY-MM-DD HH:MM:SS format)
- Weekday (displayed in Chinese)
- Detailed date info
- Detailed time info
- Day of the year
- Week of the year
- Whether daylight saving time is in effect
- UTC offset (format: +-HH:MM)
- Chinese-friendly time difference description (e.g. "8.0 hours ahead of UTC")

### MCP service configuration
```json
{
  "mcpServers": {
    "gradio": {
      "args": [
        "mcp-remote",
        "https://jackgan-realtime.ms.show/gradio_api/mcp/sse",
        "--transport",
        "sse-only"
      ],
      "command": "npx"
    }
  }
}
```

**Official site: ** [https://modelscope.cn/studios/JackGan/realtime/summary](https://modelscope.cn/studios/JackGan/realtime/summary)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `productivity`
- Tags: `search`, `developer tools`, `calendar management`, `时间,地区`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `mcp-remote https://jackgan-realtime.ms.show/gradio_api/mcp/sse --transport sse-only`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/jackgan-realtime.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
