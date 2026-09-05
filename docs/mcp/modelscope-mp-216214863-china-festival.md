---
title: "china-festival-mcp"
description: "A Chinese holiday and lunar calendar information server based on the Model Context Protocol (MCP), providing AI assistants with accurate public holidays, holiday workday adjustments, traditional Chine…"
---

# china-festival-mcp

A Chinese holiday and lunar calendar information server based on the Model Context Protocol (MCP), providing AI assistants with accurate public holidays, holiday workday adjustments, traditional Chine…

# China Holiday MCP Server

A Chinese holiday and lunar calendar information server based on the Model Context Protocol (MCP), providing AI assistants with accurate public holidays, holiday workday adjustments, traditional Chinese festivals, lunar calendar conversion, the 24 solar terms, and BaZi (Eight Characters) calculation. Western festivals all fall on fixed Gregorian dates, so no lookup tool is needed.

## Features

- **Holiday lookup**: query Chinese public holidays, traditional festivals, and workday adjustments
- **Lunar conversion**: convert between Gregorian and lunar dates
- **Lunar info**: detailed lunar date descriptions including zodiac and Heavenly Stems/Earthly Branches
- **24 solar terms**: query solar term info and season divisions
- **BaZi calculation**: compute the Four Pillars and Five Elements based on birth date and time
- **FastMCP architecture**: built on the officially recommended FastMCP framework for better performance and stability

## Technical Architecture

This project is built on the officially recommended FastMCP framework and has the following features:

- **Simplified tool registration**: uses the `@mcp.tool()` decorator
- **Automatic type validation**: handles parameter validation and type conversion automatically
- **Standardized interface**: fully conforms to MCP protocol best practices

## Installation

### Requirements

- Python 3.8+
- An MCP-capable AI client (such as Claude Desktop)

### Install with uvx (recommended)

```bash
# Install and run directly from PyPI
uvx china-festival-mcp
```

### Local development install

```bash
# Clone the project
git clone https://github.com/your-username/china-festival-mcp.git
cd china-festival-mcp

# Run with uvx (dependencies are installed automatically)
uvx --from . python -m src.server_fastmcp
```

## Usage

```bash
# Run directly from PyPI
uvx china-festival-mcp

# Or run as local development
uvx --from . python -m src.server_fastmcp
```

## MCP Client Configuration

### Claude Desktop configuration

Edit `~/Library/Application Support/Claude/claude_desktop_config.json`:

#### Install from PyPI (recommended)

```json
{
  "mcpServers": {
    "china-festival-mcp": {
      "command": "uvx",
      "args": ["china-festival-mcp"]
    }
  }
}
```

#### Local development

```json
{
  "mcpServers": {
    "china-festival-mcp": {
      "command": "uvx",
      "args": ["--from", ".", "python", "-m", "src.server_fastmcp"],
      "cwd": "/path/to/china-festival-mcp"
    }
  }
}
```

### Other MCP clients

For other MCP-capable clients, use the same uvx configuration:

```json
{
  "mcpServers": {
    "china-festival-mcp": {
      "command": "uvx",
      "args": ["china-festival-mcp"]
    }
  }
}
```

## API Documentation

### Holiday tools

#### `holiday_info`
Queries holiday info for a specified date, including whether it is a holiday

**Returns:**
```json
{
  "date": "2024-01-01",
  "name": "New Year's Day",
  "type": "holiday",
  "is_holiday": true,
  "is_work_day": false,
  "note": "Public holiday",
  "weekday_name_en": "Monday"
}
```

#### `next_holiday`
Gets the next holiday

**Returns:**
```json
{
  "name": "Spring Festival",
  "date": "2024-02-10",
  "days_until": 40,
  "note": "Public holiday",
  "weekday_name_en": "Saturday"
}
```

#### `current_year_holidays`
Gets all holidays in the current year

**Returns:**
```json
{
  "year": 2024,
  "holidays": [
    {
      "date": "2024-01-01",
      "name": "New Year's Day",
      "note": "Public holiday"
    }
  ],
  "total_count": 1
}
```

#### `current_year_work_days`
Gets the workday adjustment schedule for the current year

**Returns:**
```json
{
  "year": 2024,
  "work_days": [
    {
      "date": "2024-02-04",
      "name": "Spring Festival makeup workday",
      "note": "Makeup workday"
    }
  ],
  "total_count": 1
}
```

### Lunar tools

#### `gregorian_to_lunar`
Gregorian to lunar conversion

**Returns:**
```json
{
  "gregorian_date": "2024-01-01",
  "lunar_year": 2023,
  "lunar_month": 11,
  "lunar_day": 20,
  "is_leap_month": false,
  "zodiac": "Rabbit"
}
```

#### `lunar_to_gregorian`
Lunar to Gregorian conversion

**Returns:**
```json
{
  "lunar_date": "Lunar 11th month, 20th day, 2023",
  "gregorian_year": 2024,
  "gregorian_month": 1,
  "gregorian_day": 1,
  "gregorian_date": "2024-01-01"
}
```

#### `get_lunar_string`
Gets a detailed Chinese description of the lunar date

**Returns:**
```json
{
  "gregorian_date": "2024-01-01",
  "lunar_year": 2023,
  "lunar_month": 11,
  "lunar_day": 20,
  "is_leap_month": false,
  "zodiac": "Rabbit",
  "year_gan_zhi": "癸卯",
  "tian_gan": "癸",
  "di_zhi": "卯",
  "lunar_month_name": "Eleventh month",
  "lunar_day_name": "Twentieth day",
  "lunar_string": "Gui Mao year, 11th month, 20th day"
}
```

#### `get_24_lunar_feast`
Gets the 24 solar terms info

**Returns:**
```json
{
  "year": 2024,
  "month": 1,
  "solar_terms": [
    {
      "name": "Minor Cold",
      "date": "2024-01-06",
      "days_until": 5,
      "season": "Winter"
    },
    {
      "name": "Major Cold",
      "date": "2024-01-20",
      "days_until": 19,
      "season": "Winter"
    }
  ]
}
```

#### `get_8zi`
Calculates BaZi (Four Pillars)

**Returns:**
```json
{
  "eight_characters": "甲辰 丙寅 甲子 庚午"
}
```

### Date tools

#### `get_weekday`
Calculates the weekday for a Gregorian date

**Returns:**
```json
{
  "weekday_number": 1,
  "weekday_name_zh": "Monday",
  "weekday_name_en": "Monday",
  "date": "2024-01-01"
}
```

## Project Structure

```
china-festival-mcp/
├── src/                       # Core source code
│   ├── __init__.py
│   ├── server_fastmcp.py      # FastMCP server main program
│   ├── data/                  # Data modules
│   │   ├── bazi_calculator.py # BaZi calculation module
│   │   └── solar_terms.py     # 24 solar terms data
│   ├── tools/                 # Tool modules
│   │   ├── __init__.py
│   │   ├── holiday.py         # Holiday lookup tool
│   │   ├── lunar.py           # Lunar conversion tool
│   │   └── weekday.py         # Weekday calculation tool
│   └── utils/                 # Utility functions
│       ├── __init__.py
│       ├── date_utils.py      # Date utilities
│       └── logger.py          # Logging
├── scripts/                   # Publish scripts
│   └── publish.py             # Auto publish script
├── test_solar_terms.py        # Solar terms test script
├── .gitignore                 # Git ignore rules
├── pyproject.toml             # Project config and dependencies
├── README.md                  # Project readme
├── LICENSE                    # License
├── PUBLISH_GUIDE.md           # Publishing guide
└── publish.sh                 # Publish script
```

## Acknowledgments

This project is developed based on the [PyLunar](https://github.com/swordzjj/PyLunar/tree/master) project and the [holiday-cn](https://github.com/NateScarlet/holiday-cn) project. Thanks to the original authors for their contributions.

- Thanks to all contributors
- Based on traditional lunar algorithms and modern calculation methods
- Referenced several open-source lunar conversion projects

**Official site: ** [https://github.com/Eis4TY/china-festival-mcp](https://github.com/Eis4TY/china-festival-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `productivity`
- Tags: `calendar management`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `china-festival-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/modelscope-mp-216214863-china-festival.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
