---
title: "word-cloud-mcp"
description: "一个专注于从文档内容制作词云图的 MCP (Model Context Protocol) 工具，支持 PDF、Word、TXT、MD 等多种格式的智能文字提取。 - PDF 文档：支持从 PDF 文件中提取文字内容 - Word 文档：支持 .docx 和 .doc 格式的文档解析 - 文本文件：支持 .txt 纯文本文件 - Markdown：支持 .md 和 .markdown 文件，自动清…"
---

# word-cloud-mcp

一个专注于从文档内容制作词云图的 MCP (Model Context Protocol) 工具，支持 PDF、Word、TXT、MD 等多种格式的智能文字提取。 - PDF 文档：支持从 PDF 文件中提取文字内容 - Word 文档：支持 .docx 和 .doc 格式的文档解析 - 文本文件：支持 .txt 纯文本文件 - Markdown：支持 .md 和 .markdown 文件，自动清…

# @lucianaib/word-cloud-mcp

A MCP (Model Context Protocol) tool focused on creating word clouds from document content, supporting intelligent text extraction from various formats such as PDF, Word, TXT, MD, and more.

## Features

### 🔍 Intelligent Text Extraction
- **PDF Documents**: Supports extracting text content from PDF files
- **Word Documents**: Supports parsing .docx and .doc format documents
- **Text Files**: Supports .txt plain text files
- **Markdown**: Supports .md and .markdown files, automatically cleans up Markdown syntax

### 🧹 Content Purification
- Automatically removes meaningless stop words (e.g., "我", "我们", "的", "了" etc.)
- Cleans up punctuation and special characters
- Intelligent word segmentation, supports mixed Chinese and English text
- Customizable stop word list

### 🎨 Word Cloud Generation
- **Multiple Output Formats**: Supports SVG, PNG, JPG, WebP, and more
- **Multiple Themes**: default, warm, cool, nature, business
- **Flexible Configuration**: Font size, word spacing, angle range, background color, etc.
- **Intelligent Layout**: Avoids text overlap, optimizes visual effects
- **High-Quality Output**: Supports high resolution and quality adjustment

## Installation

### Global Installation (Recommended)
bash
npm install -g @lucianaib/word-cloud-mcp

## Usage

### As an MCP Server

1. Add this server to your MCP client configuration:

**Method 1: Using npx (Recommended, for global installation)**
json
{
  "mcpServers": {
    "word-cloud": {
      "command": "npx",
      "args": ["@lucianaib/word-cloud-mcp"]
    }
  }
}



**Method 2: Running directly with node (for local development)**
json
{
  "mcpServers": {
    "word-cloud": {
      "command": "node",
      "args": ["path/to/word-cloud-mcp/dist/index.js"],
      "cwd": "path/to/word-cloud-mcp"
    }
  }
}

**Method 3: Using absolute path (Windows example)**
json
{
  "mcpServers": {
    "word-cloud": {
      "command": "node",
      "args": ["D:/word-cloud-mcp/dist/index.js"],
      "cwd": "D:/word-cloud-mcp"
    }
  }
}

2. Restart your MCP client (e.g., CodeBuddy, Cursor, etc.)

### Available Tools

#### 1. extract_text_from_file
Extracts text content from a document file

**Parameters:**
- `filePath` (string): Path to the document file
- `fileType` (string): File type ('pdf' | 'docx' | 'txt' | 'md')

**Example:**
json
{
  "filePath": "./documents/sample.pdf",
  "fileType": "pdf"
}

#### 2. generate_wordcloud
Generates a word cloud based on the text content

Usage Example:
md
Use MCP to convert the following content into a word cloud: Google AI Studio and Gemini API availability regions

content_copy

If you are redirected to this page after trying to open Google AI Studio, it may be because Google AI Studio is not available in your region, or you do not meet the age requirement (18 years old). For more information on available regions, see below; for other requirements, see the terms of service.

Available Regions
Note: For Colab users - regional restrictions are applied based on the location of the Colab instance, not the user's location. You can use !curl ipinfo.io
to check the location of the Colab instance
Gemini API and Google AI Studio have been launched in the following countries and regions. If you are not in one of these countries or regions, try using the Gemini API in Vertex AI:

Albania
Algeria
American Samoa
Angola
....

**Parameters:**
- `text` (string): Text content used to generate the word cloud
- `theme` (string, optional): Theme color (default: 'default')
- `shape` (string, optional): Shape of the word cloud (default: 'rectangle')
- `wordGap` (number, optional): Word spacing (default: 2)
- `fontSize` (object, optional): Font size range (default: {min: 10, max: 100})
- `angleRange` (object, optional): Angle range (default: {min: -90, max: 90})
- `angleStep` (number, optional): Angle step (default: 45)- `outputPath` (string, optional): Output file path (default: './wordcloud.svg')
- `format` (string, optional): Output format ('svg' | 'png' | 'jpg' | 'jpeg' | 'webp', default: 'svg')
- `backgroundColor` (string, optional): Background color (default: '#ffffff')
- `quality` (number, optional): Quality setting for JPG/WebP formats (1-100, default: 90)

**Example:**
json
{
  "text": "This is a sample text content for generating a word cloud",
  "theme": "warm",
  "format": "png",
  "fontSize": {"min": 15, "max": 80},
  "backgroundColor": "#f8f9fa",
  "outputPath": "./my-wordcloud.png"
}

#### 3. create_wordcloud_from_file
Generate a word cloud directly from a document file (combined operation)

**Parameters:**
- `filePath` (string): Path to the document file
- `fileType` (string): File type
- Other parameters are the same as in `generate_wordcloud`

**Example:**
json
{
  "filePath": "./documents/article.md",
  "fileType": "md",
  "theme": "nature",
  "outputPath": "./article-wordcloud.svg"
}

## Theme Styles

### default
A classic colorful theme suitable for most scenarios.

### warm
A warm tone theme that creates a cozy atmosphere.

### cool
A cool tone theme with a modern and minimalist style.

### nature
A natural color theme that feels fresh and natural.

### business
A business color theme that is professional and formal.

## Supported File Formats

### Input File Formats

| Format | Extension | Description |
|--------|-----------|-------------|
| PDF    | .pdf      | Supports text-based PDFs, not scanned versions |
| Word   | .docx, .doc | Microsoft Word documents |
| Text   | .txt      | Plain text files |
| Markdown | .md, .markdown | Markdown formatted documents |

### Output Formats

| Format | Extension | Characteristics | Suitable Scenarios |
|--------|-----------|-----------------|--------------------|
| **SVG** | .svg | Vector graphics, lossless scaling, small file size | Web display, print, scenarios requiring scaling |
| **PNG** | .png | Supports transparent background, lossless compression | Web, presentations, requires transparency |
| **JPG** | .jpg/.jpeg | Lossy compression, small file size, no transparency support | Photo processing, social media sharing |
| **WebP** | .webp | Modern format, high compression rate, good quality | Modern web, mobile applications |

## Development

### Local Development

bash
# Clone the project
git clone https://github.com/lfrbmw/word-cloud-mcp.git
cd word-cloud-mcp

# Install dependencies
npm install

# Build the project
npm run build

# Run tests
npm test

### Project Structure

src/
├── index.ts                 # MCP server main entry point
├── extractors/
│   └── text-extractor.ts    # Text extractor
├── utils/
│   └── content-cleaner.ts   # Content cleaner
└── wordcloud/
    └── generator.ts         # Word cloud generator

## License

MIT License

## Contributions

Issues and Pull Requests are welcome!

**Official site: ** [https://github.com/OnePieceLwc/word-cloud-mcp](https://github.com/OnePieceLwc/word-cloud-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `memory`
- Tags: `knowledge and memory`, `词云图`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `@lucianaib/word-cloud-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/weiaib-word-cloud.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
