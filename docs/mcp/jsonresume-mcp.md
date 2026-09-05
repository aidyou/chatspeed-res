---
title: "mcp"
description: "A server that enhances AI assistants with the ability to update your JSON Resume by analyzing your coding projects, automatically extracting skills and generating professional descriptions."
---

# mcp

A server that enhances AI assistants with the ability to update your JSON Resume by analyzing your coding projects, automatically extracting skills and generating professional descriptions.

# JSON Resume MCP Server

[![npm version](/mcp-assets/021165c1d98f342a44b4b4c516a3a7d8.svg)](https://www.npmjs.com/package/@jsonresume/mcp)
[![License: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://opensource.org/licenses/MIT)
[![GitHub Issues](/mcp-assets/246bdfaf8869026642f59da7103dfd04.svg)](https://github.com/jsonresume/mcp/issues)
[Smithery](https://smithery.ai/server/@jsonresume/mcp)

**Automate your resume updates with AI by analyzing your coding projects**

[Installation](#installation) • [Features](#features) • [Usage](#usage) • [Configuration](#configuration) • [Contributing](#contributing) • [Testing](#testing)

## What is JSON Resume MCP Server?

This is a [Model Context Protocol (MCP)](https://modelcontextprotocol.ai) server that enhances AI assistants with the ability to update your [JSON Resume](https://jsonresume.org) by analyzing your coding projects. The MCP server provides tools that allow AI assistants like those in [Windsurf](https://www.windsurf.io/) or [Cursor](https://cursor.sh/) to:

1. Check if you have an existing JSON Resume
2. Analyze your codebase to understand your technical skills and projects
3. Enhance your resume with details about your current project

With this tool, you can simply ask your AI assistant to "enhance my resume with my current project," and it will automatically analyze your code, extract relevant skills and project details, and update your resume accordingly.

Video demo: [https://x.com/ajaxdavis/status/1896953226282594381](https://x.com/ajaxdavis/status/1896953226282594381)

## Features

- **Resume Enhancement**: Automatically analyzes your codebase and adds project details to your resume
- **GitHub Integration**: Fetches and updates your resume stored in GitHub Gists
- **AI-Powered**: Uses OpenAI to generate professional descriptions of your projects and skills
- **TypeScript/Zod Validation**: Ensures your resume follows the JSON Resume standard
- **JSON Resume Ecosystem**: Compatible with the [JSON Resume registry](https://registry.jsonresume.org)

## Installation

### Prerequisites

- GitHub account with a personal access token (with gist scope)
- OpenAI API key
- Node.js 18+
- An IDE with MCP support (Windsurf or Cursor)

### Installing via Smithery

To install mcp for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@jsonresume/mcp):

```bash
npx -y @smithery/cli install @jsonresume/mcp --client claude
```

### Install via NPM

```bash
npm install -g @jsonresume/mcp
```

### Install in Windsurf or Cursor

Add the following to your Windsurf or Cursor configuration:

#### Windsurf

Open Settings → MCP Servers and add:

```json
{
  "jsonresume": {
    "command": "npx",
    "args": ["-y", "@jsonresume/mcp"],
    "env": {
      "GITHUB_TOKEN": "your-github-token",
      "OPENAI_API_KEY": "your-openai-api-key",
      "GITHUB_USERNAME": "your-github-username"
    }
  }
}
```

#### Cursor

Add to your `~/.cursor/mcp_config.json`:

```json
{
  "mcpServers": {
    "jsonresume": {
      "command": "npx",
      "args": ["-y", "@jsonresume/mcp"],
      "env": {
        "GITHUB_TOKEN": "your-github-token",
        "OPENAI_API_KEY": "your-openai-api-key",
        "GITHUB_USERNAME": "your-github-username"
      }
    }
  }
}
```

## Usage

Once installed and configured, you can use the following commands with your AI assistant:

### Enhance Your Resume with Current Project

Ask your AI assistant:
```
"Can you enhance my resume with details from my current project?"
```

The assistant will:
1. Find your existing resume on GitHub (or create a new one if needed)
2. Analyze your current project's codebase
3. Generate professional descriptions of your project and skills
4. Update your resume with the new information
5. Save the changes back to GitHub
6. Provide a link to view your updated resume

### Check Your Resume Status

Ask your AI assistant:
```
"Can you check if I have a JSON Resume?"
```

The assistant will check if you have an existing resume and show its details.

### Analyze Your Codebase

Ask your AI assistant:
```
"What technologies am I using in this project?"
```

The assistant will analyze your codebase and provide insights about languages, technologies, and recent commits.

## Configuration

The MCP server requires the following environment variables:

| Variable | Description |
|----------|-------------|
| `GITHUB_TOKEN` | Your GitHub personal access token with gist permissions |
| `GITHUB_USERNAME` | Your GitHub username |
| `OPENAI_API_KEY` | Your OpenAI API key |

## Development

To run the server in development mode:

1. Clone the repository:
```bash
git clone https://github.com/jsonresume/mcp.git
cd mcp
```

2. Install dependencies:
```bash
npm install
```

3. Run in development mode:
```bash
npm run dev
```

This starts the MCP server with the inspector tool for debugging.

## Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add some amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

Please ensure your code follows the existing style and includes appropriate tests.

## Testing

The MCP server includes several test scripts to help debug and verify functionality.

### Running Tests

All test scripts are located in the `tests/` directory.

Before running tests, set your environment variables:

```bash
export GITHUB_TOKEN=your_github_token
export OPENAI_API_KEY=your_openai_api_key
export GITHUB_USERNAME=your_github_username
```

#### Check OpenAI API Key

Validates that your OpenAI API key is working correctly:

```bash
npx tsx tests/check-openai.ts
```

#### Mock Resume Enhancement

Tests the resume enhancement functionality using mock data (no API calls):

```bash
npx tsx tests/debug-mock.ts
```

#### Full Resume Enhancement Test

Tests the complete resume enhancement process with live API calls:

```bash
npx tsx tests/debug-enhance.ts
```

#### MCP Protocol Test

Tests the MCP server protocol communication:

```bash
node tests/test-mcp.js
```

### Adding to package.json

For convenience, you can add these test commands to your package.json:

```json
"scripts": {
  "test:openai": "tsx tests/check-openai.ts",
  "test:mock": "tsx tests/debug-mock.ts",
  "test:enhance": "tsx tests/debug-enhance.ts",
  "test:mcp": "node tests/test-mcp.js"
}
```

Then run them with `npm run test:mock`, etc.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/jsonresume/mcp/blob/HEAD/LICENSE) file for details.

## Acknowledgments

- [JSON Resume](https://jsonresume.org) for the resume standard
- [Model Context Protocol](https://modelcontextprotocol.ai) for enabling AI tool integration
- [OpenAI](https://openai.com) for powering the AI resume enhancements

**Official site: ** [https://github.com/jsonresume/mcp](https://github.com/jsonresume/mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `version control`, `developer tools`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @jsonresume/mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/jsonresume-mcp.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
