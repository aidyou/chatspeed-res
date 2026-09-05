---
title: "literature-review-mcp"
description: "An academic paper management and analysis tool for graduate-level literature reviews. Supports the Model Context Protocol (MCP) standard, providing multi-source academic search, intelligent compressio…"
---

# literature-review-mcp

An academic paper management and analysis tool for graduate-level literature reviews. Supports the Model Context Protocol (MCP) standard, providing multi-source academic search, intelligent compressio…

# Literature Review MCP Server

[![npm](/mcp-assets/a2a7577bfa2bb96a9e980d54bdaa18b5.svg)](https://www.npmjs.com/package/@ydzat/literature-review-mcp)
[![License: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://opensource.org/licenses/MIT)

An academic paper management and analysis tool for graduate-level literature reviews. It supports the Model Context Protocol (MCP) standard, providing multi-source academic search, intelligent compression, batch analysis, cross-paper literature review generation, and more.

> Designed specifically for graduate thesis-level literature reviews, ensuring academic rigor and high-quality output!

## Core Features

### Complete Literature Review Workflow
1. **Multi-source academic search**: intelligently searches across DBLP, OpenReview, Papers With Code, and other sources
2. **Batch download and analysis**: concurrently downloads PDFs and generates in-depth single-paper reviews (low temperature, academically rigorous)
3. **Cross-paper literature review generation**: generates detailed cross-paper synthesis based on individual reviews (4000+ characters)
4. **Review export**: exports single/cross-paper reviews as Markdown files
5. **Notion integration**: automatically generates Notion-friendly formats (requires the Notion MCP)

### Intelligent Compression System
- **Precise token calculation**: uses tiktoken for accurate token counting
- **Section recognition and tiered compression**: Abstract/Method kept at 100%, Reference kept at 0%
- **Rolling compression**: merges progressively to avoid processing overly long text at once
- **Semantic compression**: LLM-based smart compression, not simple truncation
- **Measured results**: 138K tokens -> 38K tokens (72.3% compression)

### Multiple LLM Provider Support
- **SiliconFlow**: default, supports the Qwen series
- **Deepseek**: high cost-performance (128K context, 8K output)
- **OpenAI**: GPT-4o, GPT-4-turbo
- **Custom API**: any OpenAI-compatible API

### Intelligent Quality Assessment
- Composite scoring based on citation count, conference tier, author reputation, and institution tier
- Automatically recognizes A*/A conferences, top scholars, and prestigious institutions
- Special attention to papers from the last 30 days

## Acknowledgments

This project is forked from [arxiv-mcp-server](https://github.com/yzfly/arxiv-mcp-server). Thanks to the original author [@yzfly](https://github.com/yzfly) for the open-source contribution. It has been heavily refactored and extended on top of the original project (v2.0.0 fully modular architecture).

## Installation and Usage

### NPX method (recommended)

```bash
npx -y @ydzat/literature-review-mcp@latest
```

### Global installation

```bash
npm install -g @ydzat/literature-review-mcp@latest
literature-review-mcp
```

### Local development

```bash
# Clone the project
git clone https://github.com/ydzat/literature-review-mcp.git
cd literature-review-mcp

# Install dependencies
npm install

# Copy the environment variable template
cp .env.example .env

# Edit the .env file and configure your LLM Provider
# vim .env

# Run in development mode (runs TypeScript directly with tsx)
npm run dev

# Build (compiles TypeScript to the build/ directory)
npm run build

# Run the built version (must run npm run build first)
npm start
# or run directly
node build/index.js

# Run tests
npm run build && node build/tests/test-literature-review.js
```

**Important notes**:
- If you use a local path in the MCP client configuration, you must run `npm run build` first
- The local path must point to `build/index.js`, not `src/index.ts`
- After every code change, you need to re-run `npm run build`

## Configuration Requirements

### Environment Variables

Configuration is supported via environment variables or a `.env` file:

```bash
# LLM Provider configuration (required)
LLM_PROVIDER=siliconflow  # options: siliconflow, openai, custom
LLM_API_KEY=your_api_key_here

# Optional configuration
LLM_BASE_URL=https://api.siliconflow.cn/v1  # custom API endpoint
LLM_MODEL=Qwen/Qwen2.5-7B-Instruct          # specify a model
LLM_TEMPERATURE=0.3                         # temperature (default 0.7)
```

### Supported LLM Providers

| Provider | LLM_PROVIDER | LLM_BASE_URL | Recommended model |
|----------|--------------|--------------|---------|
| SiliconFlow (default) | `siliconflow` | auto-set | `Qwen/Qwen2.5-7B-Instruct` |
| Deepseek | `custom` | `https://api.deepseek.com/v1` | `deepseek-chat` |
| OpenAI | `openai` | auto-set | `gpt-4o` |
| Other | `custom` | your API endpoint | your model name |

**Getting an API Key**:
- SiliconFlow: [https://cloud.siliconflow.cn/i/TxUlXG3u](https://cloud.siliconflow.cn/i/TxUlXG3u)
- Deepseek: [https://platform.deepseek.com/](https://platform.deepseek.com/)
- OpenAI: [https://platform.openai.com/](https://platform.openai.com/)

### Data Storage

All data is automatically stored in the `~/.arxiv-mcp/` directory:
- `arxiv-mcp.db` - SQLite database (papers, authors, institutions, reviews)
- `pdfs/` - downloaded PDF files
- `texts/` - extracted text content
- `generated/` - generated review files

## MCP Client Configuration

### Claude Desktop Configuration

Config file locations:
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

#### Method 1: Use NPX (recommended)

```json
{
  "mcpServers": {
    "literature-review-mcp": {
      "command": "npx",
      "args": ["-y", "@ydzat/literature-review-mcp@latest"],
      "env": {
        "LLM_PROVIDER": "siliconflow",
        "LLM_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

**Other Provider configurations**:
- **Deepseek**: set `LLM_PROVIDER="custom"`, `LLM_BASE_URL="https://api.deepseek.com/v1"`, `LLM_MODEL="deepseek-chat"`
- **OpenAI**: set `LLM_PROVIDER="openai"`, `LLM_MODEL="gpt-4o"`

#### Method 2: Use the local development version

```bash
# Build the project first
cd /path/to/literature-review-mcp
npm install && npm run build
```

```json
{
  "mcpServers": {
    "literature-review-mcp": {
      "command": "node",
      "args": ["/absolute/path/to/literature-review-mcp/build/index.js"],
      "env": {
        "LLM_PROVIDER": "siliconflow",
        "LLM_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

**Note**: the path must be an absolute path pointing to `build/index.js` (not `src/index.ts`)

## Usage Examples

### Complete workflow

```mermaid
graph LR
    A[Search papers] --> B[Batch download]
    B --> C[Batch analysis]
    C --> D[Generate review]
    D --> E[Export file/Notion]
```

#### 1. Search papers
```
Please search for high-quality papers on "transformer attention",
requirements: DBLP + OpenReview, at most 20 papers, quality score >= 60
```

#### 2. Batch download and analysis
```
Please download and analyze the following papers:
- arXiv:1706.03762 (Attention Is All You Need)
- arXiv:2010.11929 (ViT)
- arXiv:2005.14165 (GPT-3)
```

**Automatic processing**:
- Download PDF -> extract text -> smart compression (if needed) -> generate single-paper review (2000-3000 characters)

#### 3. Generate a cross-paper literature review
```
Please generate a unified literature review based on these 3 papers,
focusing on: methodology evolution, comparative analysis, future directions
```

**Generated content**:
- 8 detailed sections (research field overview, motivation comparison, methodology comparison, experimental analysis, innovations, limitations, future directions, critical discussion)
- 4000+ character in-depth analysis
- Automatically saved to `~/.arxiv-mcp/generated/`

#### 4. Export the review
```
Please export the single-paper review as a Markdown file
```

**Time estimate**: search 10s + download 30s + analysis 5-10min + review 3-5min = **10-15 minutes**

---

## Main Tools

### Academic search and analysis
- **`search_academic_papers`** - multi-source academic search (DBLP, OpenReview, Papers With Code)
- **`batch_download_papers`** - batch download paper PDFs
- **`batch_analyze_papers`** - batch generate in-depth single-paper reviews

### Review generation and export
- **`generate_unified_literature_review`** - generate cross-paper literature review (4000+ characters)
- **`export_individual_review_to_md`** - export a single review as Markdown
- **`batch_export_individual_reviews`** - batch export all individual reviews

### Legacy tools
- **`search_arxiv`** - search arXiv papers
- **`download_arxiv_pdf`** - download PDFs
- **`parse_pdf_to_markdown`** - parse into Chinese Markdown
- **`convert_to_wechat_article`** - generate a WeChat article
- **`process_arxiv_paper`** - full-flow processing

### Notion integration
- **`export_to_notion_full`** - full export to Notion
- **`export_to_notion_update`** - incremental Notion update

For the complete tool list and parameter descriptions, refer to `src/tools/tool-registry.ts` in the source code.

## Development Guide

### Local development

```bash
git clone https://github.com/ydzat/literature-review-mcp.git
cd literature-review-mcp
npm install
cp .env.example .env  # configure the LLM Provider
npm run dev           # development mode
npm run build         # build
npm start             # run
```

### Project architecture (v2.0.0)

```
src/
├── core/              # Core features (PDF, arXiv, processing)
├── tools/             # Tool wrappers (grouped by function)
├── llm/               # LLM abstraction (Provider + smart compression)
├── storage/           # Storage management (files + database)
├── database/          # SQLite database
├── sources/           # Academic data sources (DBLP, OpenReview, etc.)
├── reputation/        # Quality scoring system
└── index.ts           # MCP server entry (89 lines)
```

### Tech stack

- **Node.js** >= 18.0.0, **TypeScript**, **MCP**
- **SQLite** (better-sqlite3) - database
- **LLM**: SiliconFlow / OpenAI / Deepseek / custom
- **Smart compression**: tiktoken + pdfjs-dist
- **Academic data sources**: arXiv / DBLP / OpenReview / Papers With Code

## Troubleshooting

| Problem | Solution |
|------|---------|
| API Key error | Check the `LLM_API_KEY` configuration in the `.env` file |
| Paper download failure | Check whether the arXiv ID is correct and the network connection is normal |
| Database permission issue | Make sure `~/.arxiv-mcp/` has write permission |
| Notion integration not working | The Notion MCP Server needs to be configured separately |

## Contribution Guide

Contributions are welcome! Please follow:
1. Fork the project -> create a feature branch -> commit changes -> push the branch -> create a PR
2. Use TypeScript and follow the ESLint rules
3. Add appropriate error handling and tests
4. Keep the code simple and avoid over-engineering

Detailed design docs are in the `docs/` directory.

## Changelog

### v2.0.0 (2025-10-20) - major refactor

**Architecture refactor**:
- Fully modular design (`index.ts` went from 1210 lines to 89 lines, a 93% reduction)
- Backward compatible (all tool names and parameters unchanged)
- Complete tests (unit + integration + compatibility, all 57 passing)
- Smart compression integration (automatically used by all LLM calls)
- Bug fixes (author info, PDF extraction, Markdown generation, etc.)

**New features**:
- Cross-paper literature review generation (4000+ character detailed analysis)
- Review export tools (single/batch export as Markdown)
- Tool registry (config-based management)
- Enhanced LLMProvider (new convenience methods)

### v1.0.0 (2025-10-18) - initial release

Forked from [arxiv-mcp-server](https://github.com/yzfly/arxiv-mcp-server), adding:
- Multiple LLM Provider support
- Smart compression system (138K -> 38K tokens)
- Multi-source academic search (DBLP, OpenReview, Papers With Code)
- Intelligent quality assessment
- Batch concurrent processing
- Notion integration
- SQLite database

See the full changelog at [CHANGELOG.md](https://github.com/ydzat/literature-review-mcp/blob/HEAD/CHANGELOG.md)

## License

MIT License - see the [LICENSE](https://github.com/ydzat/literature-review-mcp/blob/HEAD/LICENSE) file

## Support

If you find this project useful, please give it a star!

Questions or suggestions? Feel free to open an [Issue](https://github.com/ydzat/literature-review-mcp/issues)!

**Official site: ** [https://github.com/ydzat/literature-review-mcp](https://github.com/ydzat/literature-review-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `research and data`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @ydzat/literature-review-mcp@latest`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/oafoak-literature-review.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
