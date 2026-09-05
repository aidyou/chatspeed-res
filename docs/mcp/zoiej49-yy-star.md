---
title: "yy-star-mcp"
description: "Star MCP Service (Star MCP) A fully-featured constellation MCP (Model Context Protocol) service, providing functionalities such as constellation information queries, fortune analysis, compatibility te…"
---

# yy-star-mcp

Star MCP Service (Star MCP) A fully-featured constellation MCP (Model Context Protocol) service, providing functionalities such as constellation information queries, fortune analysis, compatibility te…

# Star MCP Service (Star MCP)

A fully-featured constellation MCP (Model Context Protocol) service, providing functionalities such as constellation information queries, fortune analysis, compatibility tests, and more.

## Features

### 🌟 Core Features
- **Constellation Information Query**: Obtain detailed information about the 12 constellations, including personality traits, ruling planets, elements, etc.
- **Today's Fortune**: Provide inquiries on love, career, health, wealth, and overall fortune
- **Constellation Compatibility**: Analyze the compatibility index and relationship between two constellations
- **Birthday Constellation**: Automatically determine the constellation based on the birth date
- **Rising Sign Calculation**: Calculate the rising sign based on accurate astronomical algorithms, including Julian Day, Sidereal Time, etc.
- **Rising Sign Information**: Get a detailed characteristic analysis of the rising sign, including physical features and personality traits
- **Constellation List**: Retrieve basic information about all constellations

### 🎯 Supported Constellations
- ♈ Aries (白羊座)
- ♉ Taurus (金牛座)
- ♊ Gemini (双子座)
- ♋ Cancer (巨蟹座)
- ♌ Leo (狮子座)
- ♍ Virgo (处女座)
- ♎ Libra (天秤座)
- ♏ Scorpio (天蝎座)
- ♐ Sagittarius (射手座)
- ♑ Capricorn (摩羯座)
- ♒ Aquarius (水瓶座)
- ♓ Pisces (双鱼座)

## Installation and Running

### Prerequisites
- Node.js 18+ 
- npm or pnpm

### Install Dependencies
```bash
cd star
npm install
```
### Run the Service
```bash
# 开发模式（自动重启）
npm run dev

# 生产模式
npm start
```
## API Endpoints

### 1. Get Constellation Information
```javascript
{
  name: 'get_zodiac_info',
  arguments: {
    zodiac: '白羊座' // 或 'aries'
  }
}
```
### 2. Get Today's Fortune
```javascript
{
  name: 'get_daily_horoscope',
  arguments: {
    zodiac: '狮子座',
    category: 'love' // love, career, health, wealth, luck
  }
}
```
### 3. Constellation Compatibility Analysis
```javascript
{
  name: 'get_compatibility',
  arguments: {
    zodiac1: '白羊座',
    zodiac2: '狮子座'
  }
}
```
### 4. Query Constellation by Birthday
```javascript
{
  name: 'get_zodiac_by_date',
  arguments: {
    month: 8,
    day: 15
  }
}
```
### 5. Get All Constellation List
```javascript
{
  name: 'get_all_zodiacs',
  arguments: {}
}
```
### 6. Calculate Rising Sign
```javascript
{
  name: 'get_rising_sign',
  arguments: {
    birthHour: 14,        // 出生小时 (0-23)
    birthMinute: 30,      // 出生分钟 (0-59)
    latitude: 39.9042,    // 出生地纬度 (-90到90)
    longitude: 116.4074,  // 出生地经度 (-180到180)
    birthMonth: 8,        // 出生月份 (1-12)
    birthDay: 15,         // 出生日期 (1-31)
    birthYear: 1990       // 出生年份 (1900-2100)
  }
}
```
**Algorithm Explanation:**
The calculation of the rising sign is based on precise astronomical algorithms, including:
- Julian Day Calculation
- Greenwich Sidereal Time Calculation
- Local Sidereal Time Calculation
- Ascendant Longitude Calculation
- Determination of Constellation Boundaries

The returned result includes detailed astronomical calculation data to ensure accuracy.

### 7. Get Rising Sign Information
```javascript
{
  name: 'get_rising_sign_info',
  arguments: {
    risingSign: '白羊座' // 或 'aries'
  }
}
```
## Deployment Instructions

### Local Deployment
1. Clone the project to your local machine
2. Install dependencies: `npm install`
3. Start the service: `npm start`

### Docker Deployment
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
```
### Publishing to MCP Marketplace
1. Ensure the code complies with MCP specifications
2. Add appropriate error handling and logging
3. Write comprehensive documentation
4. Submit to the MCP registry

## Tech Stack

- **Node.js**: Runtime environment
- **MCP SDK**: Official Model Context Protocol SDK
- **ES Modules**: Using modern JavaScript module system

## Project Structure

```

star/

├── index.js                    # 主服务文件

├── package.json                # 项目配置

├── README.md                   # 项目文档

├── RISING_SIGN_GUIDE.md        # 上升星座计算使用指南

├── test.js                     # 测试文件

├── demo.js                     # 演示文件

├── simple_test.js              # 简单测试文件

└── rising_sign_test.js         # 上升星座准确性测试

```
## Development Guide

### Adding New Features
1. Define new tools in the `tools` array
2. Add processing logic in the `switch` statement
3. Update documentation and tests

### Customizing Data
- Modify the `zodiacData` object to add constellation information
- Update the `horoscopeData` to add fortune content
- Adjust the `compatibilityData` to modify compatibility rules
- Modify the `risingSignData` to adjust rising sign characteristics

### Rising Sign Calculation
- The algorithm is based on standard astronomical calculations
- Supports dates between 1900-2100
- Includes detailed astronomical data output
- Provides error handling and fallback algorithms

For detailed usage instructions, please refer to [RISING_SIGN_GUIDE.md](https://github.com/jlankellii/star-mcp/blob/HEAD/RISING_SIGN_GUIDE.md)

## License

MIT License

## Contributions

Feel free to submit Issues and Pull Requests!

## Contact

If you have any questions or suggestions, please contact us through the following methods:
- Submit a GitHub Issue
- Send an email to the project maintainers

---

**Note**: This service is for entertainment purposes only. The contents related to zodiac fortunes do not have scientific basis.

**Official site: ** [https://github.com/jlankellii/star-mcp](https://github.com/jlankellii/star-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `entertainment and media`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `star-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/zoiej49-yy-star.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
