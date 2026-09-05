---
title: "mentor-mcp-server"
description: "Provides LLM Agents with AI-powered mentorship for code review, design critique, writing feedback, and brainstorming using the Deepseek API, enabling enhanced output in various development and strateg…"
---

# mentor-mcp-server

Provides LLM Agents with AI-powered mentorship for code review, design critique, writing feedback, and brainstorming using the Deepseek API, enabling enhanced output in various development and strateg…

# mentor-mcp-server

[![TypeScript](/mcp-assets/49904649f602ceb829cc76dcf6be1703.svg)](https://www.typescriptlang.org/)
[![Model Context Protocol](/mcp-assets/69961a4849edddd35de5143c0035e099.svg)](https://modelcontextprotocol.io/)
[![Version](/mcp-assets/b3bf466f985d1cb8019f262681fdd935.svg)]()
[![License](/mcp-assets/fa73b4786cfc281bb30f39f895ada091.svg)](https://opensource.org/licenses/Apache-2.0)
[![Status](/mcp-assets/9a22554be918edafcc71c8bd0058366d.svg)]()
[![GitHub](/mcp-assets/fe6113458dd9b6cc2f99e34f47b5a356.svg)](https://github.com/cyanheads/mentor-mcp-server)

A Model Context Protocol server providing LLM Agents a second opinion via AI-powered Deepseek-Reasoning (R1) mentorship capabilities, including code review, design critique, writing feedback, and idea brainstorming through the Deepseek API. Set your LLM Agent up for success with expert second opinions and actionable insights.

## Model Context Protocol

The Model Context Protocol (MCP) enables communication between:

- **Clients**: Claude Desktop, IDEs, and other MCP-compatible clients
- **Servers**: Tools and resources for task management and automation
- **LLM Agents**: AI models that leverage the server's capabilities

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Tools](#tools)
- [Examples](#examples)
- [Development](#development)
- [Project Structure](#project-structure)
- [License](#license)

## Features

### Code Analysis
- Comprehensive code reviews
- Bug detection and prevention
- Style and best practices evaluation
- Performance optimization suggestions
- Security vulnerability assessment

### Design & Architecture
- UI/UX design critiques
- Architectural diagram analysis
- Design pattern recommendations
- Accessibility evaluation
- Consistency checks

### Content Enhancement
- Writing feedback and improvement
- Grammar and style analysis
- Documentation review
- Content clarity assessment
- Structural recommendations

### Strategic Planning
- Feature enhancement brainstorming
- Second opinions on approaches
- Innovation suggestions
- Feasibility analysis
- User value assessment

## Installation

```bash
# Clone the repository
git clone git@github.com:cyanheads/mentor-mcp-server.git
cd mentor-mcp-server

# Install dependencies
npm install

# Build the project
npm run build
```

## Configuration

Add to your MCP client settings:

```json
{
  "mcpServers": {
    "mentor": {
      "command": "node",
      "args": ["build/index.js"],
      "env": {
        "DEEPSEEK_API_KEY": "your_api_key",
        "DEEPSEEK_MODEL": "deepseek-reasoner",
        "DEEPSEEK_MAX_TOKENS": "8192",
        "DEEPSEEK_MAX_RETRIES": "3",
        "DEEPSEEK_TIMEOUT": "30000"
      }
    }
  }
}
```

### Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| DEEPSEEK_API_KEY | Yes | - | Your Deepseek API key |
| DEEPSEEK_MODEL | Yes | deepseek-reasoner | Deepseek model name |
| DEEPSEEK_MAX_TOKENS | No | 8192 | Maximum tokens per request |
| DEEPSEEK_MAX_RETRIES | No | 3 | Number of retry attempts |
| DEEPSEEK_TIMEOUT | No | 30000 | Request timeout (ms) |

## Tools

### Code Review
```xml

mentor-mcp-server
code_review

{
  "file_path": "src/app.ts",
  "language": "typescript"
}

```

### Design Critique
```xml

mentor-mcp-server
design_critique

{
  "design_document": "path/to/design.fig",
  "design_type": "web UI"
}

```

### Writing Feedback
```xml

mentor-mcp-server
writing_feedback

{
  "text": "Documentation content...",
  "writing_type": "documentation"
}

```

### Feature Enhancement
```xml

mentor-mcp-server
brainstorm_enhancements

{
  "concept": "User authentication system"
}

```

## Examples

Detailed examples of each tool's usage and output can be found in the [examples](https://github.com/cyanheads/mentor-mcp-server/tree/HEAD/examples) directory:

- [Second Opinion Example](https://github.com/cyanheads/mentor-mcp-server/blob/HEAD/examples/second-opinion.md) - Analysis of authentication system requirements
- [Code Review Example](https://github.com/cyanheads/mentor-mcp-server/blob/HEAD/examples/code-review.md) - Detailed TypeScript code review with security and performance insights
- [Design Critique Example](https://github.com/cyanheads/mentor-mcp-server/blob/HEAD/examples/design-critique.md) - Comprehensive UI/UX feedback for a dashboard design
- [Writing Feedback Example](https://github.com/cyanheads/mentor-mcp-server/blob/HEAD/examples/writing-feedback.md) - Documentation improvement suggestions
- [Brainstorm Enhancements Example](https://github.com/cyanheads/mentor-mcp-server/blob/HEAD/examples/brainstorm-enhancements.md) - Feature ideation with implementation details

Each example includes the request format and sample response, demonstrating the tool's capabilities and output structure.

## Development

```bash
# Build TypeScript code
npm run build

# Start the server
npm run start

# Development with watch mode
npm run dev

# Clean build artifacts
npm run clean
```

## Project Structure

```
src/
├── api/         # API integration modules
├── tools/       # Tool implementations
│   ├── second-opinion/
│   ├── code-review/
│   ├── design-critique/
│   ├── writing-feedback/
│   └── brainstorm-enhancements/
├── types/       # TypeScript type definitions
├── utils/       # Utility functions
├── config.ts    # Server configuration
├── index.ts     # Entry point
└── server.ts    # Main server implementation
```

## License

Apache License 2.0. See [LICENSE](https://github.com/cyanheads/mentor-mcp-server/blob/HEAD/LICENSE) for more information.

---

Built with the Model Context Protocol

**Official site: ** [https://github.com/cyanheads/mentor-mcp-server](https://github.com/cyanheads/mentor-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `developer tools`, `research and data`, `cloud platforms`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `node`
- Args: `build/index.js`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/cyanheads-mentor.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
