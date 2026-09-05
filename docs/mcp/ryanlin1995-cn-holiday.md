---
title: "mcp_cn_holiday"
description: "China Holiday Inquiry MCP Service This is a China holiday inquiry service based on MCP (Message Control Protocol), providing the functionality to query holidays and working days. The data is sourced f…"
---

# mcp_cn_holiday

China Holiday Inquiry MCP Service This is a China holiday inquiry service based on MCP (Message Control Protocol), providing the functionality to query holidays and working days. The data is sourced f…

# China Holiday Query MCP Service

This is a China holiday and workday query service based on MCP (Message Control Protocol), providing functionalities to check if a specific date is a holiday or a workday. The data source is from the [holiday-cn](https://github.com/NateScarlet/holiday-cn) project.

## Features

- Supports querying whether a specified date is a holiday
- Supports querying whether a specified date is a workday
- Automatically caches and updates holiday data
- Asynchronous processing for efficient response
- Uses the FastMCP framework, making it easy to integrate

## Installation Requirements

- Python 3.7+
- aiohttp
- mcp
- Node.js (for running MCP Inspector)

## Installation Steps

1. Clone the repository:
bash
```bash
git clone [repository-url]
cd mcp_holiday
```
2. Install dependencies:
bash
```bash
pip install aiohttp mcp
```
3. Install the MCP Inspector tool (used for testing MCP services):
bash
```bash
# 确保已安装Node.js
npm install -g @modelcontextprotocol/inspector
```
## Running the Service

1. Start the Holiday MCP service:
bash
```bash
python holiday_mcp_server.py
```
2. Test the service using MCP Inspector:
bash
```bash
npx @modelcontextprotocol/inspector python holiday_mcp_server
```
This will launch the MCP Inspector interface, through which you can test and debug various interfaces of the Holiday MCP service.

### API Documentation:

### Check if a Date is a Holiday

- Resource: `date://is_holiday/{date}`
- Parameters:
  - `date`: Date string (format: YYYY-MM-DD), optional, defaults to the current date
- Return Value:
  - `true`: It is a holiday
  - `false`: It is not a holiday
- Exceptions:
  - `ValueError`: Incorrect date format
  - `Exception`: Failed to fetch holiday data

### Check if a Date is a Workday

- Resource: `date://is_workday/{date}`
- Parameters:
  - `date`: Date string (format: YYYY-MM-DD), optional, defaults to the current date
- Return Value:
  - `true`: It is a workday
  - `false`: It is not a workday
- Exceptions:
  - `ValueError`: Incorrect date format
  - `Exception`: Failed to fetch holiday data

### Get Detailed Information of a Date

- Resource: `date://get_holiday_info/{date}`
- Parameters:
  - `date`: Date string (format: YYYY-MM-DD), optional, defaults to the current date
- Return Value: A JSON object containing the following fields
  - `date`: The queried date
  - `is_holiday`: Whether it is a holiday
  - `is_workday`: Whether it is a workday
  - `weekday`: Day of the week (0-6, 0 represents Monday)
  - `weekday_name`: Chinese name of the day of the week (e.g., "周一")
- Exceptions:
  - `ValueError`: Incorrect date format
  - `Exception`: Failed to fetch holiday data

## Data Caching

- Holiday data is cached in the `holiday_data/holiday_data.json` file
- Data is automatically updated once a year
- If the cache file is corrupted or fails to read, it will be automatically re-downloaded

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/RyanLin1995/mcp_cn_holiday/blob/HEAD/LICENSE) file for details

## Acknowledgements

- [holiday-cn](https://github.com/NateScarlet/holiday-cn) - Source of holiday data
- [FastMCP](https://github.com/MCP-Foundation/FastMCP) - MCP service framework

**Official site: ** [https://github.com/RyanLin1995/mcp_cn_holiday](https://github.com/RyanLin1995/mcp_cn_holiday)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `productivity`
- Tags: `calendar management`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `@modelcontextprotocol/inspector python holiday_mcp_server`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/ryanlin1995-cn-holiday.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
