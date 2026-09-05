---
title: "worldbank-mcp"
description: "World Bank MCP 🌐 World Bank Model Context Protocol service based on World Bank Open Data API, which provides query capabilities for global economic and social development data. 📋 Features - ✅ Country…"
---

# worldbank-mcp

World Bank MCP 🌐 World Bank Model Context Protocol service based on World Bank Open Data API, which provides query capabilities for global economic and social development data. 📋 Features - ✅ Country…

# World Bank MCP 🌐

[![npm version](/mcp-assets/85282d2522c3ad09bd6756ee61e7d586.svg)](https://www.npmjs.com/package/worldbank-mcp)
[![License: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://opensource.org/licenses/MIT)
[![GitHub issues](/mcp-assets/a5455c15cf287264ca31cd6dbdf53fd3.svg)](https://github.com/tianyuio/worldbank-mcp/issues)

World Bank Model Context Protocol service based on World Bank Open Data API, which provides query capabilities for global economic and social development data.

## 📋 Features

- ✅ Country information query
- ✅ Indicator search (education, health, environment, etc.)
- ✅ Economic data query (GDP, inflation, unemployment, etc.)
- ✅ Social development data query (population, life expectancy, internet usage, etc.)
- ✅ Education data query (literacy rate, school enrollment, etc.)
- ✅ Health and nutrition data query (hospitals, immunization, HIV prevalence, malnutrition, etc.)
- ✅ Real-time World Bank API integration
- ✅ Model Context Protocol compatibility

## 📦 Installation

### Install globally with npm
```bash
npm install -g worldbank-mcp
```

### Run instantly with npx
```bash
npx worldbank-mcp
```

## 💻 Usage in MCP Clients

To use this service in MCP-compatible clients (such as Claude Desktop, Cursor, Cherry Studio, etc.), you need to configure it as follows:

Configuration example:

### Run with npm if you have installed it globally:

```json
{
  "mcpServers": {
    "worldbank-mcp": {
      "name": "World Bank Data",
      "command": "worldbank-mcp",
      "description": "World Bank Open Data MCP Server"
    }
  }
}
```

### Run instantly with npx:

```json
{
  "mcpServers": {
    "worldbank-mcp": {
      "name": "World Bank Data",
      "command": "npx",
      "args": ["worldbank-mcp"],
      "description": "World Bank Open Data MCP Server"
    }
  }
}
```

### Run directly with node:

```json
{
  "mcpServers": {
    "worldbank-mcp": {
      "name": "World Bank Data",
      "command": "node",
      "args": ["path/to/worldbank-mcp/build/index.js"],
      "description": "World Bank Open Data MCP Server"
    }
  }
}
```

Replace `path/to/` with the actual path to your project directory.

## 📎 Usage Example

### 🧑‍💻 User
> Compare the economics of China and US with tables

### 🤖 Assistant
> I'll help you compare the economics of China and US with detailed tables. Let me gather comprehensive economic data for both countries.

> *World Bank Data : get-economic-data* ✅

> #### **China vs US Economic Comparison (2010-2024)**
> 
> Based on World Bank data, here's a comprehensive comparison of the ecomonics of Chinese and American with detailed tables:
> 
> ##### **Table 1: GDP Comparison (Trillion USD)**
> | Year | China GDP | US GDP | US as % of China | China Growth Rate |
> |------|-----------|--------|------------------|-------------------|
> | 2024 | 18.74 | 29.18 | 156% | 2.6% |
> | 2023 | 18.27 | 27.72 | 152% | 6.2% |
> | 2022 | 18.32 | 26.01 | 142% | -2.5% |
> | 2021 | 18.20 | 23.68 | 130% | 9.2% |
> | 2020 | 14.99 | 21.35 | 142% | -17.6% |
> | 2019 | 14.56 | 21.54 | 148% | 2.9% |
> | 2018 | 14.15 | 20.66 | 146% | 12.9% |
> | 2017 | 12.54 | 19.61 | 156% | 10.0% |
> | 2016 | 11.46 | 18.80 | 164% | 7.9% |
> | 2015 | 11.28 | 18.29 | 162% | 5.9% |
> | 2014 | 10.67 | 17.61 | 165% | 9.5% |
> | 2013 | 9.74 | 16.88 | 173% | 12.4% |
> | 2012 | 8.67 | 16.25 | 187% | 13.1% |
> | 2011 | 7.67 | 15.60 | 203% | 19.1% |
> | 2010 | 6.19 | 15.05 | 243% | - |
> 
> **Key Insights:**
> - US economy remains significantly larger (56% larger in 2024)
> - China's GDP has grown 203% since 2010
> - Gap between the two economies has been narrowing
> 
> ##### **Table 2: GDP Per Capita (USD)**
> ##### **Table 3: GDP Growth Rate (%)**
> ##### **Table 4: Inflation Rate (%)**
> ##### **Table 5: Unemployment Rate (%)**
> ##### **Table 6: Exports as % of GDP**
> ##### **Table 7: Foreign Direct Investment - Net Inflows (Billion USD)**
>
> ##### **Summary Analysis**
> 
> ###### **Economic Size & Growth**
> - **US**: Larger economy, mature growth (2-3% annually)
> - **China**: Smaller but growing faster (5-6% recently), catching up
> 
> ###### **Development Level**
> - **US**: High-income developed economy ($85K per capita)
> - **China**: Upper-middle income developing economy ($13K per capita)
>
> ###### **Economic Stability**
> - **China**: More stable inflation and unemployment
> - **US**: More volatile but achieves lower unemployment during booms
> 
> ###### **Economic Structure**
> - **China**: Export-oriented, manufacturing-based
> - **US**: Consumption-oriented, service-based
> 
> ###### **Investment Flows**
> - **China**: Traditionally net capital exporter, recently attracting more FDI
> - **US**: Mixed pattern, attracts significant investment during favorable conditions
> 
> This comparison highlights two economic superpowers at different stages of development, each with distinct strengths, challenges, and economic structures.

## 🔧 MCP Tools

### 1. Get Countries List
```json
{
  "name": "get-countries",
  "description": "Get all countries supported by World Bank",
  "parameters": {
    "region": "Filter by region (optional)",
    "incomeLevel": "Filter by income level (optional)"
  }
}
```

### 2. Get Country Information
```json
{
  "name": "get-country-info", 
  "description": "Get detailed information for a specific country",
  "parameters": {
    "countryCode": "Country code (e.g.: CN, US)"
  }
}
```

### 3. Search Indicators
```json
{
  "name": "search-indicators",
  "description": "Search for available indicators",
  "parameters": {
    "keyword": "Search keyword"
  }
}
```

### 4. Get Economic Data
```json
{
  "name": "get-economic-data",
  "description": "Get economic data for a country",
  "parameters": {
    "countryCode": "Country code",
    "indicator": "Economic indicator (GDP, GDP_GROWTH, GDP_PER_CAPITA, GNI, GNI_PER_CAPITA, EXPORTS_GDP, FDI_NET, INFLATION, UNEMPLOYMENT)",
    "years": "Number of years to query (optional, default 10 years)"
  }
}
```

### 5. Get Social Development Data
```json
{
  "name": "get-social-data",
  "description": "Get social development data for a country", 
  "parameters": {
    "countryCode": "Country code",
    "indicator": "Social indicator (POPULATION, LIFE_EXPECTANCY, BIRTH_RATE, DEATH_RATE, INTERNET_USERS)",
    "years": "Number of years to query (optional, default 10 years)"
  }
}
```

### 6. Get Education Data
```json
{
  "name": "get-education-data",
  "description": "Get education data for a country", 
  "parameters": {
    "countryCode": "Country code",
    "indicator": "Education indicator (LITERACY_RATE, SCHOOL_ENROLLMENT, SCHOOL_COMPLETION, TEACHERS_PRIMARY, EDUCATION_EXPENDITURE)",
    "years": "Number of years to query (optional, default 10 years)"
  }
}
```

### 7. Get Health and Nutrition Data
```json
{
  "name": "get-health-data",
  "description": "Get health and nutrition data for a country", 
  "parameters": {
    "countryCode": "Country code",
    "indicator": "Health indicator (HEALTH_EXPENDITURE, PHYSICIANS, HOSPITAL_BEDS, IMMUNIZATION, HIV_PREVALENCE, MALNUTRITION, TUBERCULOSIS)",
    "years": "Number of years to query (optional, default 10 years)"
  }
}
```

## 📖 Supported Indicators

### Economic Indicators

| Indicator Code | Description | Unit |
|---------|------|------|
| GDP | Gross Domestic Product | Current US$ |
| GDP_GROWTH | GDP growth rate | Annual % |
| GDP_PER_CAPITA | GDP per capita | Current US$ |
| GNI | Gross National Income | Current US$ |
| GNI_PER_CAPITA | GNI per capita | Current US$ |
| EXPORTS_GDP | Exports of goods and services | % of GDP |
| FDI_NET | Foreign direct investment, net inflows | Current US$ |
| INFLATION | Inflation rate | Annual % |
| UNEMPLOYMENT | Unemployment rate | % of total labor force |

### Social Indicators

| Indicator Code | Description | Unit |
|---------|------|------|
| POPULATION | Population, total | People |
| LIFE_EXPECTANCY | Life expectancy at birth | Years |
| BIRTH_RATE | Birth rate | per 1,000 people |
| DEATH_RATE | Death rate | per 1,000 people |
| INTERNET_USERS | Internet users | % of population |

### Education Indicators

| Indicator Code | Description | Unit |
|---------|------|------|
| LITERACY_RATE | Literacy rate | % of people ages 15 and above |
| SCHOOL_ENROLLMENT | School enrollment, primary | % gross |
| SCHOOL_COMPLETION | Primary completion rate | % of relevant age group |
| TEACHERS_PRIMARY | Teachers in primary education | Count |
| EDUCATION_EXPENDITURE | Government expenditure on education | % of GDP |

### Health and Nutrition Indicators

| Indicator Code | Description | Unit |
|---------|------|------|
| HEALTH_EXPENDITURE | Current health expenditure | % of GDP |
| PHYSICIANS | Physicians | per 1,000 people |
| HOSPITAL_BEDS | Hospital beds | per 1,000 people |
| IMMUNIZATION | Immunization, measles | % of children ages 12-23 months |
| HIV_PREVALENCE | Prevalence of HIV | % of population ages 15-49 |
| MALNUTRITION | Prevalence of undernourishment | % of population |
| TUBERCULOSIS | Incidence of tuberculosis | per 100,000 people |

### Common Country Codes

| Country | Code | Country | Code |
|------|------|------|------|
| China | CN | United States | US |
| Japan | JP | Germany | DE |
| United Kingdom | GB | France | FR |
| India | IN | Brazil | BR |
| Russia | RU | Australia | AU |

## Project Structure

```
worldbank-mcp/
├── src/
│   ├── index.ts      # Main entry file
│   └── types.ts      # Type definitions
├── build/            # Compiled output
├── package.json      # Project configuration
├── tsconfig.json     # TypeScript configuration
└── README.md         # Documentation
```

## Technology Stack

- **TypeScript** - Type-safe development language
- **Model Context Protocol SDK** - MCP protocol implementation
- **Axios** - HTTP client
- **Zod** - Data validation
- **Commander** - Command-line tool

## API Endpoints

Project uses World Bank Open Data API:
- Base URL: `https://api.worldbank.org/v2`
- Country data: `/countries`
- Indicator data: `/indicators`
- Country indicator data: `/country/{code}/indicator/{id}`

## License

This project is licensed under the **MIT License** - see the [LICENSE](https://github.com/tianyuio/worldbank-mcp/blob/HEAD/LICENSE) file for details.

**Official site: ** [https://github.com/tianyuio/worldbank-mcp](https://github.com/tianyuio/worldbank-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `search`, `finance`, `data`
- Tags: `search`, `finance`, `research and data`, `world bank`, `世界银行`, `数据`, `经济`, `社会`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `worldbank-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/tianyuio-worldbank.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
