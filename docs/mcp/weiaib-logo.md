---
title: "Logo-MCP"
description: "An intelligent logo extraction and processing MCP (Model Context Protocol) server that supports automatically identifying and extracting logo icons from website URLs, and provides image processing and…"
---

# Logo-MCP

An intelligent logo extraction and processing MCP (Model Context Protocol) server that supports automatically identifying and extracting logo icons from website URLs, and provides image processing and…

# logo-mcp

An intelligent Logo extraction and analysis MCP (Model Context Protocol) server that supports automatic recognition and extraction of Logo icons from website URLs, and provides detailed Logo analysis features.

## Features

### 🎯 Intelligent Logo Extraction
- **Multi-source Recognition**: Supports extracting Logos from favicon, Apple Touch icons, OpenGraph images, CSS class names, and more.
- **Intelligent Scoring**: Automatically evaluates the quality of candidate Logos and selects the best version.
- **Format Support**: Supports multiple image formats such as PNG, JPG, SVG, etc.
- **Size Optimization**: Automatically selects the appropriate size version of the Logo.

### 📊 Logo Analysis
- **Detailed Information**: Provides complete information about the Logo, including dimensions, format, type, etc.
- **Multiple Candidate Comparison**: Displays all possible Logo candidates and their scores.
- **Quality Assessment**: Automatically assesses the quality and usability of the Logo image.
- **Quick URL Retrieval**: Supports directly obtaining the URL address of the best Logo.

## Installation and Usage

### As an MCP Server

1. Install dependencies:
bash
npm install @lucianaib/logo-mcp

2. Add to MCP client configuration:
json
{
  "mcpServers": {
    "logo-mcp": {
      "command": "npx",
      "args": ["@lucianaib/logo-mcp"]
    }
  }
}



### Development Environment Setup

1. Clone the repository:
bash
git clone https://github.com/lfrbmw/Logo-MCP.git
cd Logo-MCP

2. Install dependencies:
bash
npm install

3. Build the project:
bash
npm run build

4. Start the development server:
bash
npm run dev

## MCP Tools
Usage example:
> Use mcp to extract the Logo from https://juejin.cn/

### get_best_logo_url
Extracts and returns the URL of the best Logo from a website, suitable for scenarios where only the best Logo URL is needed.

**Parameters:**
- `url` (required): The URL of the website to be analyzed

**Example:**
json
{
  "name": "get_best_logo_url",
  "arguments": {
    "url": "https://www.google.com"
  }
}

### analyze_logo
Analyzes basic information about the Logo (dimensions, format, quality, etc.), with an optional parameter `onlyBestUrl` to return only the URL of the best Logo.

**Parameters:**
- `url` (required): The URL of the website to be analyzed
- `onlyBestUrl` (optional): Whether to return only the URL of the best Logo, default is false

**Example:**
json
{
  "name": "analyze_logo",
  "arguments": {
    "url": "https://www.github.com",
    "onlyBestUrl": false
  }
}

## Technical Architecture

### Core Modules

- **LogoExtractor**: Responsible for extracting Logo candidates from websites, implementing multi-source recognition and intelligent scoring algorithms.
- **ImageProcessor**: Provides image processing functions, including format conversion, resizing, and quality enhancement.

### Dependencies

- `@modelcontextprotocol/sdk`: MCP protocol support, providing server and communication framework.
- `axios`: HTTP request handling, used for fetching website content and downloading Logo images.
- `cheerio`: HTML parsing, used for extracting Logo-related information from web pages.
- `sharp`: Image processing, providing format conversion, resizing, and enhancement functions.
- `image-size`: Image dimension detection, used for obtaining the dimensions of Logo images.
- `url-parse`: URL parsing, used for handling and normalizing website URLs.
- `mime-types`: MIME type detection, used for identifying image file formats.

## Logo Extraction Strategy

### 1. Multi-source Candidate Extraction
- Favicon link (`
`)
- Apple Touch icon (`
`)
- OpenGraph image (``)
- CSS class name recognition (`.logo`, `#logo`, `.brand`, etc.)
- Brand-related images

### 2. Intelligent Scoring Algorithm
- **Type Weighting**: Logo class name > Apple Touch > Favicon > Brand image > OG image
- **Size Scoring**: Prefers square or nearly square images between 32-512px
- **Quality Check**: Filters out damaged or blank images

### 3. Best Selection
Automatically selects the most visually appealing Logo version based on a comprehensive score.

## Logo Analysis Process

### 1. Multi-source Extraction
- **HTML Parsing**: Extracts favicon, apple-touch-icon, etc., from page meta tags.
- **CSS Analysis**: Identifies potential Logo elements through class names and IDs.
- **OpenGraph**: Parses OG image tags to obtain Logos used in social media.- **Smart Detection**: Identify potential brand logo elements on the page

### 2. Candidate Scoring
- **Type Weighting**: Assign weights based on the source type (e.g., explicit logo class names are given higher weight)
- **Size Analysis**: Evaluate if the image size is suitable for a logo (within the range of 32px to 512px)
- **Aspect Ratio**: Prefer images that are close to square
- **Quality Check**: Inspect if the image is corrupted or too blurry

### 3. Result Output
- **Detailed Analysis**: Provide detailed information and scores for all candidates
- **Best Recommendation**: Recommend the most suitable logo based on the comprehensive score
- **Quick Access**: Support directly returning the URL of the best logo

## Error Handling

- **Network Errors**: Timeout retries and friendly prompts
- **Image Corruption**: Automatic detection and skipping
- **Unsupported Formats**: Clear error messages
- **No Logo Found**: Return a friendly no-result message

## Performance Optimization

- **Concurrent Processing**: Parallel validation of multiple candidate logos
- **Caching Mechanism**: Avoid repeated downloads
- **Memory Management**: Timely release of image buffers
- **Timeout Control**: Prevent long-term blocking

## Contribution Guidelines

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/lfrbmw/Logo-MCP/blob/HEAD/LICENSE) file for details

## Authors

- **lucianaib** - [GitHub](https://github.com/lfrbmw)

## Support

If you encounter any issues or have feature suggestions, please raise them in [GitHub Issues](https://github.com/lfrbmw/Logo-MCP/issues).

---

**Logo MCP** - Making logo extraction simple and smart 🚀

**Official site: ** [https://github.com/lfrbmw/Logo-MCP](https://github.com/lfrbmw/Logo-MCP)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `files`, `media`
- Tags: `developer tools`, `entertainment and media`, `file systems`, `图标`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `@lucianaib/logo-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/weiaib-logo.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
