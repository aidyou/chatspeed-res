---
title: "mcp-perplexity-search"
description: "Enables integration of Perplexity's AI API with LLMs, delivering advanced chat completion by utilizing specialized prompt templates for tasks like technical documentation, code review, and API documen…"
---

# mcp-perplexity-search

Enables integration of Perplexity's AI API with LLMs, delivering advanced chat completion by utilizing specialized prompt templates for tasks like technical documentation, code review, and API documen…

# mcp-perplexity-search

---

## ⚠️ Notice

**This repository is no longer maintained.**

The functionality of this tool is now available in [mcp-omnisearch](https://github.com/spences10/mcp-omnisearch), which combines multiple MCP tools in one unified package.

Please use [mcp-omnisearch](https://github.com/spences10/mcp-omnisearch) instead.

---

A Model Context Protocol (MCP) server for integrating Perplexity's AI
API with LLMs. This server provides advanced chat completion
capabilities with specialized prompt templates for various use cases.

  

## Features

- 🤖 Advanced chat completion using Perplexity's AI models
- 📝 Predefined prompt templates for common scenarios:
  - Technical documentation generation
  - Security best practices analysis
  - Code review and improvements
  - API documentation in structured format
- 🎯 Custom template support for specialized use cases
- 📊 Multiple output formats (text, markdown, JSON)
- 🔍 Optional source URL inclusion in responses
- ⚙️ Configurable model parameters (temperature, max tokens)
- 🚀 Support for various Perplexity models including Sonar and LLaMA

## Configuration

This server requires configuration through your MCP client. Here are
examples for different environments:

### Cline Configuration

Add this to your Cline MCP settings:

```json
{
	"mcpServers": {
		"mcp-perplexity-search": {
			"command": "npx",
			"args": ["-y", "mcp-perplexity-search"],
			"env": {
				"PERPLEXITY_API_KEY": "your-perplexity-api-key"
			}
		}
	}
}
```

### Claude Desktop with WSL Configuration

For WSL environments, add this to your Claude Desktop configuration:

```json
{
	"mcpServers": {
		"mcp-perplexity-search": {
			"command": "wsl.exe",
			"args": [
				"bash",
				"-c",
				"source ~/.nvm/nvm.sh && PERPLEXITY_API_KEY=your-perplexity-api-key /home/username/.nvm/versions/node/v20.12.1/bin/npx mcp-perplexity-search"
			]
		}
	}
}
```

### Environment Variables

The server requires the following environment variable:

- `PERPLEXITY_API_KEY`: Your Perplexity API key (required)

## API

The server implements a single MCP tool with configurable parameters:

### chat_completion

Generate chat completions using the Perplexity API with support for
specialized prompt templates.

Parameters:

- `messages` (array, required): Array of message objects with:
  - `role` (string): 'system', 'user', or 'assistant'
  - `content` (string): The message content
- `prompt_template` (string, optional): Predefined template to use:
  - `technical_docs`: Technical documentation with code examples
  - `security_practices`: Security implementation guidelines
  - `code_review`: Code analysis and improvements
  - `api_docs`: API documentation in JSON format
- `custom_template` (object, optional): Custom prompt template with:
  - `system` (string): System message for assistant behaviour
  - `format` (string): Output format preference
  - `include_sources` (boolean): Whether to include sources
- `format` (string, optional): 'text', 'markdown', or 'json' (default:
  'text')
- `include_sources` (boolean, optional): Include source URLs (default:
  false)
- `model` (string, optional): Perplexity model to use (default:
  'sonar')
- `temperature` (number, optional): Output randomness (0-1, default:
  0.7)
- `max_tokens` (number, optional): Maximum response length
  (default: 1024)

## Development

### Setup

1. Clone the repository
2. Install dependencies:

```bash
pnpm install
```

3. Build the project:

```bash
pnpm build
```

4. Run in development mode:

```bash
pnpm dev
```

### Publishing

The project uses changesets for version management. To publish:

1. Create a changeset:

```bash
pnpm changeset
```

2. Version the package:

```bash
pnpm changeset version
```

3. Publish to npm:

```bash
pnpm release
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - see the [LICENSE](https://github.com/spences10/mcp-perplexity-search/blob/HEAD/LICENSE) file for details.

## Acknowledgments

- Built on the
  [Model Context Protocol](https://github.com/modelcontextprotocol)
- Powered by
  [Perplexity SONAR](https://docs.perplexity.ai/api-reference/chat-completions)

**Official site: ** [https://github.com/spences10/mcp-perplexity-search](https://github.com/spences10/mcp-perplexity-search)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `search`, `development`
- Tags: `search`, `developer tools`, `other`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y mcp-perplexity-search`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/spences10-perplexity-search.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
