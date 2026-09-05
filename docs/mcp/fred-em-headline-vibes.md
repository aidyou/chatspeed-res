---
title: "headline-vibes"
description: "Analyzes sentiment in news headlines from major US publications using both standard and natural language date inputs, enabling insights into public sentiment trends."
---

# headline-vibes

Analyzes sentiment in news headlines from major US publications using both standard and natural language date inputs, enabling insights into public sentiment trends.

# Headline Vibes Analysis MCP Server

A Model Context Protocol server that analyzes sentiment in news headlines from major US publications. The server provides both a standard date-based interface and natural language date parsing for easier use.

## Features

- Analyzes up to 100 headlines per request
- Even distribution of headlines across major US news sources
- Sentiment scoring on a 0-10 scale (0 = most negative, 10 = most positive)
- Natural language date parsing (e.g., "yesterday", "last Friday")
- Detailed source distribution information
- Sample headlines included in results

## Prerequisites

- Node.js v16 or higher
- NewsAPI key (get one at https://newsapi.org)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/fred-em/headline-vibes.git
cd headline-vibes
```

2. Install dependencies:
```bash
npm install
```

3. Build the server:
```bash
npm run build
```

4. Configure your NewsAPI key in your MCP settings file:
```json
{
  "mcpServers": {
    "headline-vibes": {
      "command": "node",
      "args": ["/path/to/headline-vibes/build/index.mjs"],
      "env": {
        "NEWS_API_KEY": "your-api-key-here"
      },
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

## Available Tools

### analyze_headlines
Analyze sentiment using natural language date input or specific dates.

Example usage:
```typescript
// Using natural language
{
  "name": "analyze_headlines",
  "arguments": {
    "input": "yesterday"
  }
}

// Or using specific dates
{
  "name": "analyze_headlines",
  "arguments": {
    "input": "2025-02-11"
  }
}
```

Input examples:
- "last Friday"
- "3 days ago"
- "March 10th"
- "two weeks ago"
- "2025-02-11" (YYYY-MM-DD format also supported)

## Response Format

The tool returns results in the following format:
```json
{
  "score": "6.50",              // Normalized sentiment score (0-10)
  "synopsis": "Overall positive sentiment in today's headlines",
  "headlines_analyzed": 100,    // Number of headlines analyzed
  "sources_analyzed": 12,       // Number of unique sources
  "source_distribution": {      // Distribution of headlines by source
    "Reuters": 10,
    "Associated Press": 8,
    "CNN": 9,
    // ... etc
  },
  "sample_headlines": [         // Up to 5 sample headlines
    "Example headline 1",
    "Example headline 2",
    // ... etc
  ]
}
```

## News Sources

The server pulls headlines from major US news sources including:
- Associated Press
- Reuters
- CNN
- Fox News
- NBC News
- ABC News
- Wall Street Journal
- Washington Post
- USA Today
- Bloomberg
- Business Insider
- Time

## Error Handling

The server provides clear error messages for common issues:
- Invalid date formats
- Unparseable natural language queries
- No headlines found for the specified date
- API errors from NewsAPI

## Development

To run the server in watch mode during development:
```bash
npm run watch
```

## License

MIT

**Official site: ** [https://github.com/fred-em/headline-vibes](https://github.com/fred-em/headline-vibes)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `research and data`, `search`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `node`
- Args: `/path/to/headline-vibes/build/index.mjs`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/fred-em-headline-vibes.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
