---
title: "ziwei_iztro-mcpserver1.1"
description: "npm version License: MIT Node.js Version TypeScript Based on iztro's Model Context Protocol (MCP) Server Generate a Purple Star Astrology chart, supporting geocoding and true solar time conversion ✨ F…"
---

# ziwei_iztro-mcpserver1.1

npm version License: MIT Node.js Version TypeScript Based on iztro's Model Context Protocol (MCP) Server Generate a Purple Star Astrology chart, supporting geocoding and true solar time conversion ✨ F…

npm version License: MIT Node.js Version TypeScript

A Model Context Protocol (MCP) server based on iztro

Generates Purple Star Astrology (Zi Wei Dou Shu) charts, supporting geocoding and true solar time conversion

## Features
- **Chart generation**: generate detailed Zi Wei Dou Shu charts based on birth information
- **Geocoding service**: convert place names to precise coordinates using the AMap API
- **True solar time conversion**: calculate high-precision true solar time using astronomical algorithms
- **MCP integration**: seamless integration with MCP-compatible clients
- **Secure configuration**: supports environment variables and config files

## Quick Start

### Installation
```
npm install -g ziwei_iztro-mcpserver
```

### Configuration
**Important: configure your own API key before use!**

**Method 1: Environment variables (recommended)**
```bash
# Copy the example environment file
cp .env.example .env

# Edit the .env file and add your AMap API key
echo "AMAP_API_KEY=your_actual_api_key_here" > .env
```

**Method 2: Config file**
```bash
# Copy the example config file
cp iztro-mcp-config.example.json iztro-mcp-config.json

# Edit the config file and add your API key
```

### Getting an AMap API key
1. Visit the [AMap Open Platform](https://lbs.amap.com/)
2. Register an account and log in
3. Create an app and select the "Web Service" type
4. Get your API key

### Automated setup (recommended)
```bash
# Run the interactive setup script
npm run setup
```
This guides you through the configuration process and creates the necessary files.

## Usage

### As a standalone server
```bash
# Start the MCP server
ziwei_iztro-mcpserver
# or
npm start
```

### Integration with MCP clients
Add to your MCP client configuration:

```json
{
  "mcpServers": {
    "iztro": {
      "command": "npx",
      "args": ["ziwei_iztro-mcpserver"]
    }
  }
}
```

Or install locally:

```json
{
  "mcpServers": {
    "iztro": {
      "command": "node",
      "args": ["/path/to/ziwei_iztro-mcpserver/dist/index.js"]
    }
  }
}
```

## Available Tools

### 1. geocode_location
Converts a place name to precise coordinates.

**Parameters:**
- `location` (string, required): place name, e.g. "Jinniu Town, Lujiang County, Hefei City, Anhui Province"

**Returns:**
```json
{
  "location": "Jinniu Town, Lujiang County, Hefei City, Anhui Province",
  "longitude": 117.123456,
  "latitude": 31.654321,
  "formatted_address": "Jinniu Town, Lujiang County, Hefei City, Anhui Province"
}
```

### 2. convert_to_apparent_solar_time
Converts Beijing time to true solar time based on the geographic location.

**Parameters:**
- `beijingTime` (string, required): Beijing time in YYYY-MM-DD HH:mm:ss format
- `longitude` (number, required): longitude (positive east, negative west)
- `latitude` (number, optional): latitude (positive north, negative south)

**Returns:**
```json
{
  "beijing_time": "2024-01-01 12:00:00",
  "longitude": 117.123456,
  "latitude": 31.654321,
  "apparent_solar_time": "2024-01-01 12:08:30"
}
```

### 3. generate_astrolabe
Generates a Zi Wei Dou Shu chart, supporting location-based true solar time conversion.

**Parameters:**
- `birthday` (string, required): birth date in YYYY-MM-DD format
- `birthTime` (number, required): birth time period (0-11), where 0=Zi hour, 1=Chou hour, and so on
- `gender` (string, required): gender, 'male' or 'female'
- `calendarType` (string, optional): calendar type, 'solar' or 'lunar', default 'solar'
- `isLeapMonth` (boolean, optional): whether it is a leap month (lunar calendar only)
- `language` (string, optional): output language, supports 'zh-CN', 'zh-TW', 'en-US', 'ja-JP', 'ko-KR', 'vi-VN'
- `location` (string, optional): birth location, used for true solar time conversion

**Returns:** complete chart data; if a location parameter is provided, location processing info is also included.

## Development

### Prerequisites
- Node.js >= 16.0.0
- npm or yarn
- TypeScript 5.0+

### Local development
```bash
# Clone the repository
git clone https://github.com/smogievogie/ziwei_iztro-mcpserver.git
cd ziwei_iztro-mcpserver

# Install dependencies
npm install

# Build the project
npm run build

# Run the setup script
npm run setup

# Start the dev server
npm run dev
```

### Testing
```bash
# Test with MCP Inspector
npx @modelcontextprotocol/inspector node dist/index.js
```

## Technical Details

### True solar time calculation
- Based on Jean Meeus' "Astronomical Algorithms"
- Accounts for the ellipticity of Earth's orbit and axial tilt
- Accuracy within 3 seconds compared to the astronomical almanac
- Supports early and late Zi hour distinction

### Geocoding service
- Powered by the AMap API
- High-precision coordinate conversion
- Supports detailed address resolution within China
- Automatically falls back to the original time if geocoding fails

## Contributing
Contributions are welcome! Feel free to submit a Pull Request.

### Development guide
1. Fork this repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Submit a Pull Request

### Code standards
- Use TypeScript for type safety
- Follow the ESLint configuration
- Add appropriate unit tests
- Update documentation as needed

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/smogievogie/ziwei_iztro-mcpserver/blob/HEAD/LICENSE) file for details.

## Acknowledgments
- iztro - the core Zi Wei Dou Shu library
- MCP SDK - the Model Context Protocol TypeScript SDK
- AMap API - geocoding service provider

## Support
- Issue feedback: GitHub Issues
- Discussion: GitHub Discussions
- Documentation: project Wiki

Made with <3 for Zi Wei Dou Shu enthusiasts

**Official site: ** [https://github.com/smogievogie/ziwei_iztro-mcpserver.git](https://github.com/smogievogie/ziwei_iztro-mcpserver.git)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `art and culture`, `research and data`, `other`, `（"mcp&agent挑战赛"）`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `ziwei_iztro-mcpserver`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/haha008gg-ziwei-iztro-mcpserver1-1.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
