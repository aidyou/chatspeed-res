---
title: "openrouterai"
description: "Provides integration with OpenRouter.ai, allowing access to various AI models through a unified interface."
---

# openrouterai

Provides integration with OpenRouter.ai, allowing access to various AI models through a unified interface.

# OpenRouter MCP Server

[![MCP Server](/mcp-assets/cb56a0889b99f9bc45a0b547b9f87230.svg)](https://github.com/heltonteixeira/openrouterai)
![Version](/mcp-assets/d58b7f6784e65408fe1c317cfc0473dd.svg)
[![TypeScript](/mcp-assets/754e1918c2ab1fa621c9e6e01628f1e0.svg)](https://www.typescriptlang.org/)
![License](/mcp-assets/4159b5048650fda64b541eaec9d81bd1.svg)

A Model Context Protocol (MCP) server providing seamless integration with OpenRouter.ai's diverse model ecosystem. Access various AI models through a unified, type-safe interface with built-in caching, rate limiting, and error handling.

## Features

- **Model Access**
  - Direct access to all OpenRouter.ai models
  - Automatic model validation and capability checking
  - Default model configuration support

- **Performance Optimization**
  - Smart model information caching (1-hour expiry)
  - Automatic rate limit management
  - Exponential backoff for failed requests

- **Unified Response Format**
  - Consistent `ToolResult` structure for all responses
  - Clear error identification with `isError` flag
  - Structured error messages with context
## Installation

```bash
pnpm install @mcpservers/openrouterai
```

## Configuration

### Prerequisites

1. Get your OpenRouter API key from [OpenRouter Keys](https://openrouter.ai/keys)
2. Choose a default model (optional)

### Environment Variables
```env
OPENROUTER_API_KEY=your-api-key-here
OPENROUTER_DEFAULT_MODEL=optional-default-model
```

### Setup

Add to your MCP settings configuration file (`cline_mcp_settings.json` or `claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "openrouterai": {
      "command": "npx",
      "args": ["@mcpservers/openrouterai"],
      "env": {
        "OPENROUTER_API_KEY": "your-api-key-here",
        "OPENROUTER_DEFAULT_MODEL": "optional-default-model"
      }
    }
  }
}
```

## Response Format

All tools return responses in a standardized structure:

```typescript
interface ToolResult {
  isError: boolean;
  content: Array;
}
```

**Success Example:**
```json
{
  "isError": false,
  "content": [{
    "type": "text",
    "text": "{"id": "gen-123", ...}"
  }]
}
```

**Error Example:**
```json
{
  "isError": true,
  "content": [{
    "type": "text",
    "text": "Error: Model validation failed - 'invalid-model' not found"
  }]
}
```

## Available Tools

### chat_completion

Send messages to OpenRouter.ai models:

```typescript
interface ChatCompletionRequest {
  model?: string;
  messages: Array;
  temperature?: number; // 0-2
}

// Response: ToolResult with chat completion data or error
```

### search_models

Search and filter available models:

```typescript
interface ModelSearchRequest {
  query?: string;
  provider?: string;
  minContextLength?: number;
  capabilities?: {
    functions?: boolean;
    vision?: boolean;
  };
}

// Response: ToolResult with model list or error
```

### get_model_info

Get detailed information about a specific model:

```typescript
{
  model: string;           // Model identifier
}
```

### validate_model

Check if a model ID is valid:

```typescript
interface ModelValidationRequest {
  model: string;
}

// Response: 
// Success: { isError: false, valid: true }
// Error: { isError: true, error: "Model not found" }
```

## Error Handling

The server provides structured errors with contextual information:

```typescript
// Error response structure
{
  isError: true,
  content: [{
    type: "text",
    text: "Error: [Category] - Detailed message"
  }]
}
```

**Common Error Categories:**
- `Validation Error`: Invalid input parameters
- `API Error`: OpenRouter API communication issues
- `Rate Limit`: Request throttling detection
- `Internal Error`: Server-side processing failures

**Handling Responses:**
```typescript
async function handleResponse(result: ToolResult) {
  if (result.isError) {
    const errorMessage = result.content[0].text;
    if (errorMessage.startsWith('Error: Rate Limit')) {
      // Handle rate limiting
    }
    // Other error handling
  } else {
    const data = JSON.parse(result.content[0].text);
    // Process successful response
  }
}
```

## Development

See CONTRIBUTING.md for detailed information about:
- Development setup
- Project structure
- Feature implementation
- Error handling guidelines
- Tool usage examples

```bash
# Install dependencies
pnpm install

# Build project
pnpm run build

# Run tests
pnpm test
```

## Changelog
See CHANGELOG.md for recent updates including:
- Unified response format implementation
- Enhanced error handling system
- Type-safe interface improvements

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

**Official site: ** [https://github.com/heltonteixeira/openrouterai](https://github.com/heltonteixeira/openrouterai)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `developer tools`, `other`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `@mcpservers/openrouterai`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/heltonteixeira-openrouterai.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
