---
title: "Arxiv-Paper-MCP"
description: "ArXiv Paper MCP 一个基于 arXiv 的论文检索与内容解析工具。支持 Model Context Protocol (MCP) 标准，提供论文搜索、PDF链接获取和内容解析功能。"
---

# Arxiv-Paper-MCP

ArXiv Paper MCP 一个基于 arXiv 的论文检索与内容解析工具。支持 Model Context Protocol (MCP) 标准，提供论文搜索、PDF链接获取和内容解析功能。

# ArXiv Paper MCP

A paper search and content parsing tool based on arXiv. Supports the Model Context Protocol (MCP) standard, providing functions for paper search, PDF link acquisition, and content parsing.

## Features

* 🔍 **Intelligent arXiv Paper Search**: Keyword-based search to quickly locate the papers you care about
* 🔗 **Get PDF Download Links**: Obtain direct PDF download links for arXiv papers
* 📄 **Paper Content Parsing**: Smartly parse paper content, with preference given to HTML versions, falling back to PDF
* 🆕 **Latest AI Papers**: Get a list of the latest updated AI papers on arXiv today

## Installation and Usage

### NPX Method (Recommended)

bash
npx @langgpt/arxiv-paper-mcp

### Global Installation

bash
npm install -g @langgpt/arxiv-paper-mcp
arxiv-paper-mcp

## MCP Client Configuration

### Claude Desktop Configuration

Add the following to the Claude Desktop configuration file:

json
{
  "mcpServers": {
    "arxiv-paper-mcp": {
      "command": "npx",
      "args": ["-y", "@langgpt/arxiv-paper-mcp@latest"]
    }
  }
}

Configuration file locations:
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

### Other MCP Clients

For other MCP-supported clients, please refer to their documentation for configuring stdio transport.

## Available Tools and Parameters

### 1. Search Papers

* **Tool Name**: `search_arxiv`
* **Parameters**:
  * `query`: Search keywords
  * `maxResults`: Number of papers to return (optional, default 5)

### 2. Get PDF Download Link

* **Tool Name**: `get_arxiv_pdf_url`
* **Parameters**:
  * `input`: arXiv paper URL or arXiv ID (e.g., 2403.15137v1)

### 3. Parse Paper Content

* **Tool Name**: `parse_paper_content`
* **Parameters**:
  * `input`: arXiv paper URL or arXiv ID
  * `paperInfo`: Metadata of the paper (optional, used to add metadata to the paper)

### 4. Get Recent AI Papers

* **Tool Name**: `get_recent_ai_papers`
* **Parameters**: None

## Example Usage Workflow

1. **Search Papers**
   Use the `search_arxiv` tool to find relevant papers.
2. **Get Latest AI Papers**
   Use the `get_recent_ai_papers` tool to get today's latest AI papers.
3. **Get PDF Link**
   Use the `get_arxiv_pdf_url` tool to obtain the PDF download link.
4. **Parse Paper Content**
   Use the `parse_paper_content` tool to get the text content of the paper (preferring HTML, falling back to PDF).

## Development Guide

### Local Development

bash
# Clone the project
git clone https://github.com/yzfly/arxiv-paper-mcp.git
cd arxiv-paper-mcp

# Install dependencies
npm install

# Run in development mode
npm run dev

# Build
npm run build

# Run the built version
npm start

### Project Structure

arxiv-paper-mcp/
├── src/
│   └── index.ts          # Main server file
├── build/                # Compilation output directory
├── package.json          # Project configuration
├── tsconfig.json         # TypeScript configuration
├── README.md             # Project description
└── LICENSE               # License

## Tech Stack

- **Node.js** >= 18.0.0
- **TypeScript** - Type-safe JavaScript
- **Model Context Protocol** - Standardized AI context protocol
- **arXiv API** - Academic paper data source

## Troubleshooting

### Common Issues

1. **Paper Search Failure**
   
   Error: Search failed
   Solution: Check your internet connection and ensure the search keywords are correct
   

2. **PDF Parsing Failure**
   
   Error: PDF parsing failed
   Solution: Check if the arXiv ID is correct and ensure the paper exists
   

### Debugging Logs

Enable detailed logs:
bash
DEBUG=arxiv-paper-mcp npx @langgpt/arxiv-paper-mcp

## Contribution Guidelines

Contributions are welcome! Please follow these steps:

1. Fork this repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push the branch: `git push origin feature/amazing-feature`
5. Create a Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/yzfly/Arxiv-Paper-MCP/blob/HEAD/LICENSE) file for details.

## Author Information

- **Author**: yzfly
- **Email**: yz.liu.me@gmail.com
- **GitHub**: [https://github.com/yzfly](https://github.com/yzfly)

## Related Links- [Model Context Protocol](https://modelcontextprotocol.io/)
- [arXiv.org](https://arxiv.org/)
- [Claude Desktop](https://claude.ai/download)

## Support

If you find this project useful, please give it a ⭐!

For any questions or suggestions, feel free to reach out via:

- 📧 Email: yz.liu.me@gmail.com
- 🐛 GitHub Issues: [Project Issue Tracker](https://github.com/yzfly/arxiv-paper-mcp/issues)
- 💬 GitHub Discussions: [Project Discussion Forum](https://github.com/yzfly/arxiv-paper-mcp/discussions)

**Official site: ** [https://github.com/yzfly/Arxiv-Paper-MCP](https://github.com/yzfly/Arxiv-Paper-MCP)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `research and data`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @langgpt/arxiv-paper-mcp@latest`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/zephyr-arxiv-paper.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
