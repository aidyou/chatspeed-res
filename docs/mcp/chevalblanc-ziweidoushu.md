---
title: "MCP-ZIWEIDOUSHU"
description: "A professional Purple Star Astrology (Zi Wei Dou Shu) analysis server based on the Model Context Protocol (MCP), providing complete services for natal chart generation, interpretation, analysis, and v…"
---

# MCP-ZIWEIDOUSHU

A professional Purple Star Astrology (Zi Wei Dou Shu) analysis server based on the Model Context Protocol (MCP), providing complete services for natal chart generation, interpretation, analysis, and v…

# Zi Wei Dou Shu MCP Server

A professional Zi Wei Dou Shu (Purple Star Astrology) fortune-telling analysis server based on the Model Context Protocol (MCP), providing complete chart generation, interpretation, analysis, and visualization. It supports traditional Zi Wei Dou Shu algorithms and integrates modern data persistence and visualization technologies.

## Features

### Core features
- **Chart generation**: generate complete Zi Wei Dou Shu charts based on lunar calendar algorithms
- **Chart interpretation**: detailed chart analysis and professional explanations
- **Fortune analysis**: analyze current and future fortune trends
- **Compatibility analysis**: pairing analysis of compatibility between two charts
- **Auspicious date selection**: pick lucky dates based on the chart
- **AI-powered interpretation**: combine traditional astrology with modern AI technology

### Visualization
- **Chart images**: generate chart visualizations in multiple styles
- **Data visualization**: supports SVG, PNG, and HTML output formats
- **Theme customization**: traditional, modern, colorful, and monochrome palettes

### Professional analysis
- **Star information**: detailed info and influence of each star
- **Palace analysis**: meanings and in-depth analysis of the 12 palaces
- **Life timeline**: detailed analysis of major luck periods and yearly fortunes
- **Relationships**: family, friendship, and career relationship analysis
- **Career guidance**: career development and decision support
- **Health analysis**: health trends and wellness advice
- **Educational guidance**: learning ability and education planning

## Installation

### Requirements
- Node.js 18.0+
- npm 8.0+
- SQLite 3.0+

### Install dependencies

```bash
npm install
```

## Usage

### Start the server

```bash
# Development mode
npm run dev

# Production mode
npm start
```

### Client configuration (stdio)

If you use an MCP-capable client (such as Claude Desktop), you can connect to this service via stdio:

#### Claude Desktop configuration

Add the following to your Claude Desktop config file:

```json
{
  "mcpServers": {
    "ziwei-doushu": {
      "command": "npx",
      "args": ["-y","ziwei-mcp"]
    }
  }
}
```

## API Documentation

### Core tools

#### 1. generate_chart - Generate a chart
Generates a complete Zi Wei Dou Shu chart

**Parameters:**
- `name` (string): name
- `birthDate` (string): birth date (YYYY-MM-DD)
- `birthTime` (string): birth time (HH:MM)
- `gender` (string): gender (male/female)
- `location` (object): birth location
  - `province` (string): province
  - `city` (string): city
  - `longitude` (number): longitude
  - `latitude` (number): latitude
- `timezone` (string): timezone (default: Asia/Shanghai)
- `calendar` (string): calendar (solar/lunar, default: solar)

#### 2. interpret_chart - Chart interpretation
Provides detailed chart analysis and interpretation

**Parameters:**
- `chartId` (string): chart ID
- `aspects` (array): aspects to interpret
  - personality: personality traits
  - career: career development
  - wealth: wealth fortune
  - relationships: romantic relationships
  - health: health condition
  - family: family relationships
- `detailLevel` (string): detail level (basic/detailed/comprehensive)

#### 3. analyze_fortune - Fortune analysis
Analyzes fortune trends for a specific period

**Parameters:**
- `chartId` (string): chart ID
- `period` (string): analysis period (current_year/next_year/decade/custom)
- `startDate` (string): start date (YYYY-MM-DD)
- `endDate` (string): end date (YYYY-MM-DD)
- `aspects` (array): aspects to analyze

#### 4. analyze_compatibility - Compatibility analysis
Pairing analysis of two charts

**Parameters:**
- `chart1Id` (string): first person's chart ID
- `chart2Id` (string): second person's chart ID
- `analysisType` (string): analysis type (marriage/business/friendship)
- `aspects` (array): analysis dimensions

#### 5. select_auspicious_date - Auspicious date selection
Selects lucky dates based on the chart

**Parameters:**
- `chartId` (string): chart ID
- `eventType` (string): event type
- `dateRange` (object): date range
- `preferences` (object): preference settings

### Visualization tools

#### 6. generate_visualization - Generate a chart visualization
Generates chart visualizations in multiple styles and formats

**Parameters:**
- `chartId` (string): chart ID
- `visualizationType` (string): visualization type
  - traditional_chart: traditional chart
  - modern_wheel: modern wheel
  - palace_grid: palace grid
  - star_map: star map
- `includeElements` (array): elements to include
- `colorScheme` (string): color scheme
- `outputFormat` (string): output format (svg/png/html)

### Professional analysis tools

#### 7. analyze_life_timeline - Life timeline analysis
Analyzes the life timeline, including major luck periods and yearly fortunes

#### 8. analyze_relationships - Relationship analysis
Analyzes relationships, including family, friends, and colleagues

#### 9. career_guidance - Career development guidance
Career development guidance and decision support

#### 10. health_analysis - Health analysis
Health analysis and wellness advice

#### 11. educational_guidance - Educational guidance
Education and learning guidance

## Development Guide

### Development environment setup

```bash
# Enter the project directory
cd ziwei

# Install dependencies
npm install

# Start the MCP server
npm start

# Or start in development mode
npm run dev
```

### Available scripts

```bash
npm start      # Start the MCP server
npm run dev    # Start development mode (with debugging)
npm test       # Run basic tests
npm run lint   # ESLint code checks
npm run format # Prettier code formatting
```

### Code standards

- Use ESLint for code checks
- Use Prettier for code formatting
- Follow CommonJS module conventions
- Support Node.js 18.0+

## Configuration

### Config files

The project uses the following config files:

- `config/sqlite-config.js` - SQLite database config
- `config/persistence-config.js` - data persistence config
- `package.json` - project dependencies and scripts

### Database configuration

The project uses SQLite for data storage; the config file is at `config/sqlite-config.js`.

## Usage Examples

### Chart generation example

```javascript
// Via MCP call
const chart = await mcpClient.callTool('generate_chart', {
  name: 'Zhang San',
  birthDate: '1990-01-01',
  birthTime: '08:30',
  gender: 'male',
  location: {
    province: 'Beijing',
    city: 'Beijing',
    longitude: 116.4074,
    latitude: 39.9042
  }
});
```

### Chart interpretation example

```javascript
const interpretation = await mcpClient.callTool('interpret_chart', {
  chartId: chart.id,
  aspects: ['personality', 'career', 'wealth'],
  detailLevel: 'detailed'
});
```

## Contribution Guide

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Commit conventions

```
feat: new feature
fix: bug fix
docs: documentation update
style: code formatting
refactor: code refactoring
test: tests
chore: build process or tooling changes
```

## License

This project is licensed under the MIT License.

## Support & Feedback

- **Detailed docs**: Zi Wei Dou Shu MCP development documentation
- **SQLite deployment**: [SQLite deployment guide](https://github.com/taurusduan/ziwei-mcp/blob/HEAD/SQLite部署指南.md)
- **SVG generation**: [SVG generator usage guide](https://github.com/taurusduan/ziwei-mcp/blob/HEAD/SVG生成器使用指南.md)

## Related Links

- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Claude Desktop](https://claude.ai/desktop)
- [lunar-javascript library](https://github.com/6tail/lunar-javascript) - core lunar calendar conversion library

---

**Note**: This project is for learning and research only. Fortune analysis results are for reference only and should not be the sole basis for major life decisions.

## Changelog

### v1.0.0 (2024-01-01)
- Initial release
- Basic chart generation
- Chart interpretation and fortune analysis
- SVG image generation
- SQLite data persistence
- AI-powered chart interpretation
- Compatibility analysis
- Auspicious date selection

## FAQ

**Q: Why does the generated chart differ from other software?**
A: Different Zi Wei Dou Shu software may use different algorithms and parameters. This service is based on traditional algorithms, so results may vary.

**Q: Which timezones are supported?**
A: All major global timezones are supported, with Asia/Shanghai (Beijing time) as the default.

**Q: How long is data retained?**
A: Data is currently stored permanently in the local SQLite database; you can manually clean up data you no longer need.

**Q: How can I get more accurate results?**
A: Make sure to enter accurate birth date, time, and location, with the time precise to the minute.

## Technical Support

If you encounter technical issues, please provide:
1. The error message and error code
2. The input parameters used
3. Your operating system and Node.js version
4. Detailed reproduction steps

Interpretation data

**Official site: ** [https://github.com/taurusduan/ziwei-mcp](https://github.com/taurusduan/ziwei-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `memory`
- Tags: `knowledge and memory`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y ziwei-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/chevalblanc-ziweidoushu.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
