---
title: "yijing-bazi-mcp"
description: "A professional I Ching (Yijing) and BaZi (Eight Characters) analysis server based on the MCP (Model Context Protocol), providing traditional Chinese cultural analysis capabilities for AI assistants. T…"
---

# yijing-bazi-mcp

A professional I Ching (Yijing) and BaZi (Eight Characters) analysis server based on the MCP (Model Context Protocol), providing traditional Chinese cultural analysis capabilities for AI assistants. T…

# I Ching & BaZi Analysis MCP Server

A professional I Ching (Yijing) and BaZi (Eight Characters) analysis server based on the MCP (Model Context Protocol), providing traditional Chinese cultural analysis capabilities for AI assistants. This project integrates I Ching hexagram analysis, BaZi fortune calculation, and comprehensive fortune prediction, and supports integration with multiple AI clients.

> **Important Notice:** This project has been published to NPM, so you can now:
> - Run the `npx yijing-bazi-mcp` command from any directory
> - Install it globally via `npm install -g yijing-bazi-mcp`
> - Pin a version, e.g. `npx yijing-bazi-mcp@latest`

## Core Features

### I Ching Analysis System
- **Multiple hexagram casting methods**: coin method, yarrow stalk method, time method, number method
- **Professional hexagram interpretation**: comprehensive analysis of the primary hexagram, changing hexagram, and nuclear hexagram
- **Smart decision advice**: practical guidance based on the hexagram
- **Context awareness**: analysis combined with the specific question scenario

### BaZi (Eight Characters) System
- **Accurate BaZi chart generation**: supports Gregorian/lunar calendar conversion
- **Comprehensive personality analysis**: Five Elements, Ten Gods, and chart pattern analysis
- **Fortune prediction**: detailed prediction of major luck periods, yearly fortunes, and monthly fortunes
- **Multi-dimensional analysis**: career, wealth, relationships, and health

### Composite Analysis Engine
- **I Ching + BaZi integration**: deep combination of traditional culture
- **Smart correlation analysis**: cross-validation across systems
- **Personalized consultation**: targeted fortune advice
- **Case study library**: rich real-world case studies

### Technical Architecture
- **Standard protocol support**: fully compatible with the MCP protocol spec
- **Modular design**: decoupled engines for easy extension
- **Smart caching**: improved response speed
- **Complete logging**: easy debugging and monitoring

## Environment Requirements

- **Node.js**: 18.0.0 or later
- **npm**: latest version
- **OS**: Windows/macOS/Linux

## Quick Installation

### Option 1: Local install

```bash
# Download the project package
# Extract to a local directory
cd yijing-bazi-mcp

# Install dependencies
npm install

# Verify the installation
node src/index.js --version
```

### Option 2: Global install (recommended)

```bash
# Global install
npm install -g .

# Verify the installation
yijing-bazi-mcp --version

# Local development (currently recommended)
node src/index.js

# Or use npm exec (local project)
npm exec yijing-bazi-mcp

# Or use npx (requires publishing to NPM first)
npx yijing-bazi-mcp

# Note: these commands start the MCP server directly, they do not print version info
```

## Starting the Server

### MCP mode (standard protocol)

For MCP clients such as Claude Desktop and Cherry Studio:

```bash
# Development mode (auto-restart)
npm run dev

# Production mode
npm start
```

## Client Configuration

### Claude Desktop

**Step 1: Get the project**

**Option A: Install from NPM (recommended)**
```bash
# Global install
npm install -g yijing-bazi-mcp

# Or use npx (runs from any directory)
npx yijing-bazi-mcp@latest
```

**Option B: Local development/testing (currently recommended)**
```bash
# Clone or download the project
git clone
cd yijing-bazi-mcp

# Install dependencies
npm install

# Test run
node src/index.js
```

**Step 2: Configure Claude Desktop**

Edit the `claude_desktop_config.json` file:

**Method 1: Use npx (recommended)**
```json
{
  "mcpServers": {
    "yijing-bazi": {
      "command": "npx",
      "args": ["yijing-bazi-mcp@latest"],
      "env": {
        "LOG_LEVEL": "info",
        "NODE_ENV": "production"
      }
    }
  }
}
```

**Note:** The `cwd` parameter is no longer needed; it can run from any directory.

**Method 2: Use a local project (currently recommended)**
```json
{
  "mcpServers": {
    "yijing-bazi": {
      "command": "node",
      "args": ["src/index.js"],
      "cwd": "/full/path/to/yijing-bazi-mcp",
      "env": {
        "LOG_LEVEL": "info",
        "NODE_ENV": "development"
      }
    }
  }
}
```

**Config file locations:**
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**Method 2 (alt): Direct invocation**
```json
{
  "mcpServers": {
    "yijing-bazi": {
      "command": "node",
      "args": ["/full/path/to/yijing-bazi-mcp/src/index.js"],
      "env": {
        "LOG_LEVEL": "info"
      }
    }
  }
}
```

**Windows example path**:
```json
"cwd": "E:\\Desktop\\ProjectResources\\TencentCloud\\baidu-netdisk-auto-delete"
"args": ["E:\\Desktop\\ProjectResources\\TencentCloud\\baidu-netdisk-auto-delete\\src\\index.js"]
```

### Trae AI / Cursor IDE

Add to the MCP settings in your IDE:

**Method 1: Use npm exec (recommended)**
```json
{
  "mcpServers": {
    "yijing-bazi": {
      "command": "npm",
      "args": ["exec", "yijing-bazi-mcp"],
      "cwd": "/full/project/path",
      "env": {
        "NODE_ENV": "development"
      }
    }
  }
}
```

**Method 1 (alt): Use npx (recommended)**
```json
{
  "mcpServers": {
    "yijing-bazi": {
      "command": "npx",
      "args": ["yijing-bazi-mcp@latest"],
      "env": {
        "NODE_ENV": "development"
      }
    }
  }
}
```

**Method 2: Direct invocation**
```json
{
  "mcpServers": {
    "yijing-bazi": {
      "command": "node",
      "args": ["src/index.js"],
      "cwd": "/full/project/path",
      "env": {
        "NODE_ENV": "development"
      }
    }
  }
}
```

### Cherry Studio

1. Open Settings -> MCP Servers
2. Add a new server:
   - **Name**: `I Ching BaZi Analysis Server`
   - **Type**: `STDIO`
   - **Command**: `npm` (recommended), `npx` (if available), or `node`
   - **Arguments**: `exec yijing-bazi-mcp` (npm), `yijing-bazi-mcp` (npx), or `/full/path/to/yijing-bazi-mcp/src/index.js` (node)
   - **Working directory**: `/full/path/to/yijing-bazi-mcp`

## Available Tools

### I Ching Tools

| Tool | Description | Main parameters |
|---------|---------|----------|
| `yijing_generate_hexagram` | Generate a hexagram | question, method, context |
| `yijing_interpret` | Interpret a hexagram | hexagram, focus, detail_level |
| `yijing_advise` | Decision advice | hexagram, question, time_frame |

### BaZi Tools

| Tool | Description | Main parameters |
|---------|---------|----------|
| `bazi_generate_chart` | Generate a BaZi chart | birth_time, gender, timezone |
| `bazi_analyze` | BaZi analysis | chart, analysis_type, detail_level |
| `bazi_forecast` | Fortune prediction | chart, period_type, focus_aspects |

### Composite Analysis

| Tool | Description | Main parameters |
|---------|---------|----------|
| `combined_analysis` | Combined analysis | bazi_chart, hexagram, question |
| `destiny_consult` | Destiny consultation | birth_info, question, consultation_type |

### Learning Features

| Tool | Description | Main parameters |
|---------|---------|----------|
| `knowledge_learn` | Knowledge learning | topic, level, learning_type |
| `case_study` | Case study | case_id, system, category |

## Usage Examples

### I Ching hexagram example

```json
{
  "tool": "yijing_generate_hexagram",
  "params": {
    "question": "Is this year a good time to start a business?",
    "method": "coin",
    "context": "Currently working at a large company and considering entrepreneurship"
  }
}
```

### BaZi analysis example

```json
{
  "tool": "bazi_generate_chart",
  "params": {
    "birth_time": "1990-05-15T10:30:00+08:00",
    "gender": "male",
    "is_lunar": false,
    "timezone": "Asia/Shanghai"
  }
}
```

### Composite analysis example

```json
{
  "tool": "combined_analysis",
  "params": {
    "birth_time": "1990-05-15T10:30:00+08:00",
    "gender": "male",
    "question": "Career direction for the next three years",
    "analysis_focus": ["career", "wealth", "timing"]
  }
}
```

## Project Architecture

```
yijing-bazi-mcp/
├── .promptx/              # PromptX AI configuration
│   ├── pouch.json         # Project configuration
│   └── resource/          # Resource files
├── src/                  # Source code directory
│   ├── engines/          # Core analysis engines
│   │   ├── yijing-engine.js        # I Ching analysis engine
│   │   ├── bazi-engine.js          # BaZi analysis engine
│   │   ├── combined-engine.js      # Combined analysis engine
│   │   ├── combined-analysis-engine.js # Deep analysis engine
│   │   └── knowledge-engine.js     # Knowledge learning engine
│   ├── data/             # Database modules
│   │   ├── hexagram-database.js    # Hexagram database
│   │   ├── bazi-database.js        # BaZi database
│   │   └── knowledge-database.js   # Knowledge base
│   ├── utils/            # Utility functions
│   │   ├── logger.js              # Logging system
│   │   ├── error-handler.js       # Error handling
│   │   ├── validator.js           # Parameter validation
│   │   ├── cache.js               # Cache management
│   │   ├── date-utils.js          # Date utilities
│   │   ├── yijing-calculator.js   # I Ching calculations
│   │   ├── bazi-calculator.js     # BaZi calculations
│   │   ├── analysis-integrator.js # Analysis integration
│   │   ├── search-engine.js       # Search engine
│   │   ├── performance.js         # Performance monitoring
│   │   └── validation.js          # Data validation
│   ├── config/           # Configuration files
│   │   └── config.js              # Main configuration
│   ├── index.js             # MCP server entry point
├── mcp-config.json       # MCP server config
├── start-mcp-servers.js  # Server start script
├── stop-mcp-servers.js   # Server stop script
├── package.json          # Project dependency config
└── README.md             # Project documentation
```

## Testing & Debugging

### Running tests

```bash
# Test the BaZi chart generation
node -e "const { YijingBaziMCPServer } = require('./src/index.js'); const server = new YijingBaziMCPServer(); server.baziEngine.generateChart({birth_datetime: '1990-05-15T10:30:00+08:00', timezone: 'Asia/Shanghai', gender: 'male'}).then(result => console.log('Test success:', JSON.stringify(result, null, 2))).catch(err => console.error('Test failed:', err.message));"

# Test the I Ching hexagram function
node -e "const { YijingBaziMCPServer } = require('./src/index.js'); const server = new YijingBaziMCPServer(); server.yijingEngine.generateHexagram({method: 'random', question: 'test question'}).then(result => console.log('Casting success:', JSON.stringify(result, null, 2))).catch(err => console.error('Casting failed:', err.message));"

# Check the server startup status
node src/index.js
```

### Debug mode

```bash
# Windows PowerShell debugging
$env:LOG_LEVEL="debug"; node src/index.js

# View log files
Get-Content logs/app.log -Wait

# Or view with Notepad
notepad logs/app.log
```

### Troubleshooting

**1. "could not determine executable to run" error**
```bash
# Solution A: Use the latest version
npx yijing-bazi-mcp@latest

# Solution B: Clear the NPM cache
npm cache clean --force

# Solution C: Use local development mode (if inside the project directory)
node src/index.js
```

**2. "spawn npx ENOENT" error**
```bash
# Solution: use npm exec instead of npx
# Change "command": "npx" to "command": "npm"
# Change "args": ["yijing-bazi-mcp"] to "args": ["exec", "yijing-bazi-mcp"]
```

**3. "MCP server failed to start" error**
```bash
# Check the following:
# 1. Verify the Node.js version
node --version  # needs 18.0.0+

# 2. Check project dependencies
npm install

# 3. Test direct startup
node src/index.js

# 4. Test npm exec
npm exec yijing-bazi-mcp
```

**4. Path configuration issues**
```json
// Windows path example (note the double backslashes)
{
  "mcpServers": {
    "yijing-bazi": {
      "command": "npm",
      "args": ["exec", "yijing-bazi-mcp"],
      "cwd": "E:\\Desktop\\ProjectResources\\TencentCloud\\baidu-netdisk-auto-delete",
      "env": {
        "LOG_LEVEL": "info"
      }
    }
  }
}
```

**5. Permission issues**
```bash
# Make sure the file has execute permissions (Linux/Mac)
chmod +x src/index.js

# On Windows, run the terminal as administrator
```

#### Testing the configuration

Run the test script to verify your configuration:
```bash
# Run the configuration test
node test-npx.js

# Manually test various startup methods
node src/index.js                    # direct startup
npm exec yijing-bazi-mcp            # npm exec method
npx yijing-bazi-mcp                 # npx method (if available)
```

### Environment variable configuration

Optionally create a `.env` file (the project ships with defaults):

```bash
# Logging config
LOG_LEVEL=info
NODE_ENV=production

# MCP config
SERVER_NAME=yijing-bazi-mcp-server
SERVER_VERSION=1.0.0

# Feature switches
ENABLE_CACHE=true
ENABLE_PERFORMANCE_MONITORING=true
```

## Documentation Resources

- [Project structure](#project-architecture) - detailed code organization
- [Tool list](#available-tools) - complete API tool documentation
- [Usage examples](#usage-examples) - real invocation examples
- [Configuration guide](#client-configuration) - configuration for various clients

## Publishing to the ModelScope Community

### NPX usage

ModelScope community users can use this project directly via npx:

```bash
# Run directly (recommended)
npx yijing-bazi-mcp@latest

# Or install globally and use it
npm install -g yijing-bazi-mcp
yijing-bazi-mcp
```

### ModelScope community config example

Configure the MCP server in your AI client:

```json
{
  "mcpServers": {
    "yijing-bazi": {
      "command": "npx",
      "args": ["yijing-bazi-mcp@latest"],
      "env": {
        "LOG_LEVEL": "info"
      }
    }
  }
}
```

### Features

- **BaZi analysis**: fortune analysis based on birth time
- **I Ching hexagrams**: hexagram interpretation and divination
- **Smart Q&A**: AI dialogue grounded in traditional cultural knowledge
- **Real-time calculation**: dynamically generates personalized analysis results
- **Detailed reports**: comprehensive fortune reading reports

## Development & Contributions

### Local development

1. **Edit code** - directly edit the source files
2. **Test features** - use the test commands above to verify
3. **View logs** - check the log files in the `logs/` directory
4. **Restart the service** - restart the MCP client to load changes

### Development standards

- Keep code style consistent
- Add necessary error handling
- Update related comments and documentation
- Test the stability of new features

### Issue reporting

If you run into problems, check:
1. Whether the Node.js version meets the requirement (18+)
2. Whether the dependency packages are installed correctly
3. Whether the path config is correct
4. The error messages in the log files

## Version Info

- **Current version**: 1.0.0
- **Release date**: 2024
- **Compatibility**: MCP protocol standard
- **Node.js**: 18.0.0+

## Acknowledgments

- [MCP protocol](https://modelcontextprotocol.io/) - the standardized AI tool protocol
- [lunar-javascript](https://github.com/6tail/lunar-javascript) - precise lunar calendar library
- [PromptX](https://promptx.ai/) - AI development tool support
- Traditional Yijing culture - the deep theoretical foundation of this project
- The open-source community - continuous support and contributions

## Disclaimer

This project is for learning and research purposes only. The analysis results are for reference and do not constitute decision-making advice. Users should treat the results rationally and consider practical circumstances for important decisions.

---

**A professional I Ching & BaZi analysis MCP server**

*The perfect combination of traditional culture and modern AI technology*

**Official site: ** [https://github.com/SiwuXue/yijing-bazi-mcp-server](https://github.com/SiwuXue/yijing-bazi-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `memory`
- Tags: `knowledge and memory`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `yijing-bazi-mcp@latest`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/wuai60-yijing-bazi.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
