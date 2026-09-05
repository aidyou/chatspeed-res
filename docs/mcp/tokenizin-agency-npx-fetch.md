---
title: "mcp-npx-fetch"
description: "A powerful MCP server for fetching and transforming web content into various formats (HTML, JSON, Markdown, Plain Text) with ease."
---

# mcp-npx-fetch

A powerful MCP server for fetching and transforming web content into various formats (HTML, JSON, Markdown, Plain Text) with ease.

# MCP NPX Fetch

[![npm version](/mcp-assets/f158cbea937d67f46dd06a0879b88710.svg)](https://www.npmjs.com/package/@tokenizin/mcp-npx-fetch)
[![License: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://opensource.org/licenses/MIT)
[![TypeScript](/mcp-assets/49904649f602ceb829cc76dcf6be1703.svg)](https://www.typescriptlang.org/)
[![Model Context Protocol](/mcp-assets/dea21ef1b755e12c928a6fd915869854.svg)](https://github.com/modelcontextprotocol)

A powerful MCP server for fetching and transforming web content into various formats (HTML, JSON, Markdown, Plain Text) with ease.

[Installation](#installation) •
[Features](#features) •
[Usage](#usage) •
[Documentation](#documentation) •
[Contributing](#contributing)

---

## 🚀 Features

- 🌐 **Universal Content Fetching**: Supports HTML, JSON, plain text, and Markdown formats
- 🔒 **Custom Headers Support**: Add authentication and custom headers to your requests
- 🛠 **Built-in Transformations**: Automatic conversion between formats
- ⚡ **High Performance**: Built with modern JavaScript features and optimized for speed
- 🔌 **MCP Compatible**: Seamlessly integrates with Claude Desktop and other MCP clients
- 🎯 **Type-Safe**: Written in TypeScript with full type definitions

## 📦 Installation

### NPM Global Installation

```bash
npm install -g @tokenizin/mcp-npx-fetch

```

### Direct Usage with NPX

```bash
npx @tokenizin/mcp-npx-fetch
```

## 📚 Documentation

### Available Tools

#### `fetch_html`

Fetches and returns raw HTML content from any URL.

```typescript
{
  url: string;     // Required: Target URL
  headers?: {      // Optional: Custom request headers
    [key: string]: string;
  };
}
```

#### `fetch_json`

Fetches and parses JSON data from any URL.

```typescript
{
  url: string;     // Required: Target URL
  headers?: {      // Optional: Custom request headers
    [key: string]: string;
  };
}
```

#### `fetch_txt`

Fetches and returns clean plain text content, removing HTML tags and scripts.

```typescript
{
  url: string;     // Required: Target URL
  headers?: {      // Optional: Custom request headers
    [key: string]: string;
  };
}
```

#### `fetch_markdown`

Fetches content and converts it to well-formatted Markdown.

```typescript
{
  url: string;     // Required: Target URL
  headers?: {      // Optional: Custom request headers
    [key: string]: string;
  };
}
```

## 🔧 Usage

### CLI Usage

Start the MCP server directly:

```bash
mcp-npx-fetch
```

Or via npx:

```bash
npx @tokenizin/mcp-npx-fetch
```

### Claude Desktop Integration

1. Locate your Claude Desktop configuration file:

   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%/Claude/claude_desktop_config.json`
   - Linux: `~/.config/Claude/claude_desktop_config.json`

2. Add the following configuration to your `mcpServers` object:

```json
{
  "mcpServers": {
    "fetch": {
      "command": "npx",
      "args": ["-y", "@tokenizin/mcp-npx-fetch"],
      "env": {}
    }
  }
}
```

## 💻 Local Development

1. Clone the repository:

```bash
git clone https://github.com/tokenizin-agency/mcp-npx-fetch.git
cd mcp-npx-fetch
```

2. Install dependencies:

```bash
npm install
```

3. Start development mode:

```bash
npm run dev
```

4. Run tests:

```bash
npm test
```

## 🛠 Technical Stack

- [Model Context Protocol SDK](https://github.com/modelcontextprotocol/sdk) - Core MCP functionality
- [JSDOM](https://github.com/jsdom/jsdom) - HTML parsing and manipulation
- [Turndown](https://github.com/mixmark-io/turndown) - HTML to Markdown conversion
- [TypeScript](https://www.typescriptlang.org/) - Type safety and modern JavaScript features
- [Zod](https://github.com/colinhacks/zod) - Runtime type validation

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/tokenizin-agency/mcp-npx-fetch/blob/HEAD/LICENSE) file for details.

---

Made with ❤️ by 
PT Tokenizin Technology Agency

**Official site: ** [https://github.com/tokenizin-agency/mcp-npx-fetch](https://github.com/tokenizin-agency/mcp-npx-fetch)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `browser`
- Tags: `browser automation`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @tokenizin/mcp-npx-fetch`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/tokenizin-agency-npx-fetch.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
