---
title: "little-red-book-card-mcp"
description: "An MCP tool that converts Markdown documents into beautiful knowledge cards, supporting multiple styles. It can be used as an MCP (Model Context Protocol) tool and provides features such as converting…"
---

# little-red-book-card-mcp

An MCP tool that converts Markdown documents into beautiful knowledge cards, supporting multiple styles. It can be used as an MCP (Model Context Protocol) tool and provides features such as converting…

# Little Red Book Card MCP

An MCP tool that converts Markdown documents into beautiful knowledge cards, supporting multiple styles.

[![npm version](/mcp-assets/ae3f1f68b65710da6a2b989a0d0ff914.svg)](https://www.npmjs.com/package/little-red-book-card-mcp)
[![License: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://opensource.org/licenses/MIT)
[![TypeScript](/mcp-assets/e2f4f7eb3c57946e147a6d1fb44ccbbc.svg)](https://www.typescriptlang.org/)
[![Node.js](/mcp-assets/148c8c2430c0ccd90f9e06f3c3ea5e04.svg)](https://nodejs.org/)

## How to configure the Little Red Book card tool in MCP

### Basic configuration format

```json
{
  "mcpServers": {
    "little-red-book-card-mcp": {
      "command": "npx",
      "args": ["@lucianaib/little-red-book-card-mcp"]
    }
  }
}
```

### Usage effect
> Make some Markdown content and convert it into a knowledge card image, children's fairy-tale style, phone-size dimensions

The effect is as follows:

## Features

### Multiple theme styles
Supports 18 different theme styles to meet the needs of various scenarios:

**Modern styles**
- **Apple Memo** - a clean and fresh Apple-style memo
- **Glassmorphism** - modern glassmorphism effect
- **Dreamy Gradient** - dreamy gradient colors
- **Fresh Nature** - fresh natural green tones

**Creative styles**
- **Pop Art** - bold and vivid pop art style
- **Art Deco** - luxurious art deco style
- **Watercolor Art** - watercolor painting effect
- **Cyberpunk** - cyberpunk neon style

**Professional styles**
- **Business Briefing** - professional business briefing style
- **Japanese Magazine** - Japanese magazine layout style
- **Retro Typewriter** - retro typewriter style
- **Notebook** - notebook paper effect

**Featured styles**
- **Purple Little Red Book** - Little Red Book style purple theme
- **Chinese Traditional** - traditional Chinese culture style
- **Children's Fairy Tale** - children's fairy tale style
- **Minimalist Black & White** - minimalist black and white palette
- **Warm & Soft** - warm and comfortable soft tones
- **Simple Premium Gray** - minimalist premium gray tones
- **Dark Tech** - dark tech style

### Core features
- **Markdown to HTML cards** - converts Markdown documents into beautiful knowledge cards
- **Image generation** - converts HTML cards into PNG/JPEG image files
- **File reading support** - reads Markdown files directly
- **Multiple card types** - supports specifying card type/size via the type parameter
- **Content statistics** - automatically counts words and characters
- **Long content handling** - intelligently splits long content to avoid performance issues
- **MCP integration** - full MCP tool integration, easy to integrate into various platforms

## Quick Start

### Global installation

```bash
npm install -g little-red-book-card-mcp
```

Or use pnpm:

```bash
pnpm add little-red-book-card-mcp
```

### Use as an MCP tool

1. **Start the MCP server**:
```bash
   node dist/index.js
```

2. **Available tools**:
   - `convert_markdown_to_card` - converts Markdown to a knowledge card
   - `generate_card_image` - converts Markdown to a knowledge card image
   - `list_available_themes` - lists all available themes

3. **Conversion examples**:

   **HTML card generation (default mobile size)**:
```json
   {
     "name": "convert_markdown_to_card",
     "arguments": {
       "content": "# Title\n\nThis is Markdown content.",
       "theme": "Purple Little Red Book",
       "type": "mobile",
       "filePath": "optional/path/to/file.md"
     }
   }
```

   **Image generation example (default mobile size)**:
```json
   {
     "name": "generate_card_image",
     "arguments": {
       "content": "# Title\n\nThis is Markdown content.",
       "theme": "Fresh Nature",
       "type": "mobile",
       "outputDir": "./output",
       "format": "png",
       "quality": 80
     }
   }
```

## API Reference

### convert_markdown_to_card
Converts Markdown content into a knowledge card.

**Parameters**:
- `content` (string, required) - the Markdown content
- `theme` (string, required) - the theme name
- `type` (string, optional) - card type ('mobile', 'standard', 'large', 'small', 'wide'), default `mobile`
- `filePath` (string, optional) - the Markdown file path

**Returns**:
```json
{
  "html": "full HTML card code",
  "css": "theme CSS styles",
  "metadata": {
    "theme": "theme name",
    "type": "card type",
    "wordCount": "word count",
    "charCount": "character count"
  }
}
```

### generate_card_image
Converts Markdown content into a knowledge card image.

**Parameters**:
- `content` (string, required) - the Markdown content
- `theme` (string, required) - the theme name
- `type` (string, optional) - card type ('mobile', 'standard', 'large', 'small', 'wide'), default `mobile`
- `filePath` (string, optional) - the Markdown file path
- `outputDir` (string, optional) - output directory, default is the current directory
- `format` (string, optional) - image format ('png', 'jpeg'), default 'png'
- `quality` (number, optional) - image quality (jpeg only), default 80

**Returns**:
```json
{
  "imagePath": "generated image file path",
  "metadata": {
    "theme": "theme name",
    "type": "card type",
    "format": "image format",
    "size": "file size (bytes)",
    "wordCount": "word count",
    "charCount": "character count"
  }
}
```

### list_available_themes
Lists all available theme styles.

**Returns**:
```json
{
  "themes": [
    {
      "name": "theme name",
      "key": "theme key",
      "description": "theme description"
    }
  ],
  "count": "number of themes"
}
```

## Development Environment Setup

### Clone and install

```bash
git clone
cd little-red-book-card-mcp
pnpm install
```

### Build and run

```bash
# Build the project
npm run build

# Run the development server
npm run dev

# Run tests (Jest)
npm test

# View test coverage
npm run test:coverage
```

## File Structure

```
├── src/
│   ├── index.ts          # Main MCP server implementation
├── tests/
│   ├── index.test.ts     # Main test file
│   ├── setup.ts          # Test environment setup
├── dist/                 # Build output directory
├── package.json          # Project configuration
├── tsconfig.json         # TypeScript configuration
├── jest.config.js        # Jest test configuration
└── README.md             # Project documentation

### Common scripts

- `npm run build`: compiles TypeScript
- `npm run start`: starts the MCP server (stdio)
- `npm run generate:pop-mobile`: generates a pop-art mobile-size sample image
```

## Tech Stack

- **TypeScript** - type-safe JavaScript development
- **Node.js** - runtime environment
- **MCP SDK** - Model Context Protocol development framework
- **marked** - Markdown parser
- **cheerio** - HTML manipulation library
- **puppeteer** - HTML to image conversion
- **Jest** - testing framework

## License

MIT License - see the LICENSE file for details

## Contributing

Issues and Pull Requests are welcome!

### Development guide

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code standards

- Write in TypeScript
- Follow the ESLint rules
- Add appropriate unit tests
- Keep code comments clear

## Changelog

### v1.0.2 (2024-10-29)
- Successfully published to the npm registry
- Fixed package name configuration issues
- Updated MCP configuration examples
- Optimized the release pipeline

### v1.0.0 (2024-10-29)
- Initial release
- Supports 18 theme styles
- Implemented Markdown to HTML card conversion
- File reading support
- Full MCP tool integration
- Automatic content statistics
- Intelligent splitting of long content
- Complete test coverage

## Support

If you have problems, you can get help through:

- Check the [docs](#api-reference)
- Submit an [Issue](https://github.com/your-repo/issues)
- Email [support@example.com](mailto:support@example.com)

## Acknowledgments

Thanks to all developers and testers who contributed to this project!

---

**Little Red Book Card MCP** - breathe new life into your Markdown content!

**Official site: ** [https://github.com/OnePieceLwc/little-red-book-card-mcp](https://github.com/OnePieceLwc/little-red-book-card-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `memory`
- Tags: `knowledge and memory`, `小红薯📕卡片`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `@lucianaib/little-red-book-card-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/weiaib-little-red-book-card.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
