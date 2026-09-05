---
title: "Suppr_mcp"
description: "Suppr MCP - Usage Guide Providing Document Translation and Chinese PubMed Search MCP Service Suppr Super Literature Quick Start 1. Installation Global installation: bash npm install -g suppr-mcp Or us…"
---

# Suppr_mcp

Suppr MCP - Usage Guide Providing Document Translation and Chinese PubMed Search MCP Service Suppr Super Literature Quick Start 1. Installation Global installation: bash npm install -g suppr-mcp Or us…

# Suppr MCP - Usage Guide | Providing Document Translation and Chinese PubMed Search MCP Service | Suppr Super Literature

## Quick Start

### 1. Installation

Global installation:
bash
npm install -g suppr-mcp

Or use npx (no installation required):
bash
npx suppr-mcp

### 2. Get API Key

Visit [Suppr API](https://suppr.wilddata.cn/api-keys) to get your API key.

### 3. Configure Environment Variables

bash
export SUPPR_API_KEY=your_api_key_here

### 4. Use in MCP Client

#### Claude Desktop Configuration

Edit `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or the corresponding configuration file:

json
{
  "mcpServers": {
    "suppr": {
      "command": "npx",
      "args": ["-y", "suppr-mcp"],
      "env": {
        "SUPPR_API_KEY": "your_api_key_here"
      }
    }
  }
}

Or use global installation:

json
{
  "mcpServers": {
    "suppr": {
      "command": "suppr-mcp",
      "env": {
        "SUPPR_API_KEY": "your_api_key_here"
      }
    }
  }
}

## Available Tools

### 1. create_translation - Create a Translation Task

Creates a document translation task.

**Parameters:**
- `file_path` (either `file_path` or `file_url`): Source file path
- `file_url` (either `file_path` or `file_url`): URL of the document to be translated
- `to_lang` (required): Target language code
- `from_lang` (optional): Source language code (auto-detected by default)
- `optimize_math_formula` (optional): Optimize math formulas (PDF only)

**Example:**
json
{
  "file_url": "https://example.com/document.pdf",
  "to_lang": "en",
  "from_lang": "zh",
  "optimize_math_formula": true
}

**Response:**
json
{
  "task_id": "02a6c6d1-3f70-4a5a-80bc-971d53a37bb1",
  "status": "INIT",
  "consumed_point": 453,
  "source_lang": "zh",
  "target_lang": "en",
  "optimize_math_formula": true
}

### 2. get_translation - Get Translation Details

Gets detailed information and status of a translation task.

**Parameters:**
- `task_id` (required): Translation task ID

**Example:**
json
{
  "task_id": "02a6c6d1-3f70-4a5a-80bc-971d53a37bb1"
}

**Response:**
json
{
  "task_id": "02a6c6d1-3f70-4a5a-80bc-971d53a37bb1",
  "status": "DONE",
  "progress": 1.0,
  "consumed_point": 453,
  "source_file_name": "document.pdf",
  "source_file_url": "https://example.com/source.pdf",
  "target_file_url": "https://example.com/translated.pdf",
  "source_lang": "zh",
  "target_lang": "en",
  "error_msg": null,
  "optimize_math_formula": true
}

**Task Status Explanation:**
- `INIT`: Initialization
- `PROGRESS`: In progress
- `DONE`: Completed
- `ERROR`: Error

### 3. list_translations - List Translation Tasks

Gets a list of translation tasks with pagination support.

**Parameters:**
- `offset` (optional): Pagination offset, default 0
- `limit` (optional): Number of items per page, default 20

**Example:**
json
{
  "offset": 0,
  "limit": 10
}

**Response:**
json
{
  "total": 42,
  "offset": 0,
  "limit": 10,
  "list": [
    {
      "task_id": "...",
      "status": "DONE",
      "progress": 1.0,
      ...
    }
  ]
}

### 4. search_documents - Document Search

AI-driven semantic search for documents.

**Parameters:**
- `query` (required): Natural language query
- `topk` (optional): Maximum number of results to return (1-100, default 20)
- `return_doc_keys` (optional): Specify fields to return
- `auto_select` (optional): Automatically select the best result (default true)

**Example:**
json
{
  "query": "最新糖尿病研究进展",
  "topk": 5,
  "return_doc_keys": ["title", "abstract", "doi", "authors"],
  "auto_select": true
}

**Available Return Fields:**
- `title`: Title
- `abstract`: Abstract
- `authors`: List of authors
- `doi`: DOI
- `pmid`: PubMed ID
- `link`: Link
- `publication`: Publication
- `pub_year`: Publication year
- For more fields, refer to the API documentation

**Response:**
json
{
  "search_items": [
    {
      "doc": {
        "title": "...",
        "abstract": "...",
        "authors": [...],
        "doi": "...",
        ...
      },
      "search_gateway": "pubmed"
    }
  ],
  "consumed_points": 20
}## Supported Languages

Common language codes:
- `en`: English (English)
- `zh`: Chinese (Chinese)
- `ko`: Korean (Korean)
- `ja`: Japanese (Japanese)
- `fr`: French (French)
- `de`: German (German)
- `es`: Spanish (Spanish)
- `ru`: Russian (Russian)
- `ar`: Arabic (Arabic)
- `pt`: Portuguese (Portuguese)
- `it`: Italian (Italian)
- `auto`: Auto-detect

## Error Handling

All errors return in a standard format:

json
{
  "code": non-zero error code,
  "msg": "Error message",
  "data": null
}


Common errors:
- **401**: Invalid or missing API key
- **400**: Bad request parameters
- **404**: Resource not found

## Usage Examples

### Using in Claude Desktop

1. Restart Claude Desktop after configuring the API key.

2. Use the tool in the conversation:

**Document Translation:**
> Please help me translate this document: https://example.com/paper.pdf, into English

**Literature Search:**
> Help me find the latest literature on "applications of deep learning in medical imaging"

**Check Translation Status:**
> Check the translation progress of task 02a6c6d1-3f70-4a5a-80bc-971d53a37bb1

## Frequently Asked Questions

### Q: How to get an API key?
A: Visit https://suppr.wilddata.cn/api-keys to register and obtain an API key.

### Q: What document formats are supported?
A: Supports common formats such as PDF, DOCX, PPTX, XLSX, HTML, TXT, EPUB, etc.

### Q: How long does the translation take?
A: It depends on the size of the document, usually ranging from a few minutes to about ten minutes. You can use `get_translation` to check the progress.

### Q: How to download the translated document?
A: After the translation is complete, `get_translation` will return `target_file_url`, simply access the link to download.

### Q: npx fails to run?
A: Ensure that Node.js version >= 18.0.0 and the SUPPR_API_KEY environment variable is set.

## 🔗 Suppr Super Literature Products

- **Zotero Plugin** : https://github.com/WildDataX/suppr-zotero-plugin
- **Official Website**: [https://suppr.wilddata.cn](https://suppr.wilddata.cn)
- **AI Document Translation**:https://suppr.wilddata.cn/translate/upload
- **API Service**:https://openapi.suppr.wilddata.cn/introduction
- **Chinese Search for Pubmed**: https://suppr.wilddata.cn/
- **Deep Research**: [https://suppr.wilddata.cn/deep-research](https://suppr.wilddata.cn/deep-research)  
- **GitHub Organization**: [WildDataX](https://github.com/WildDataX)

## Technical Support

For assistance, please contact: IT@wilddata.cn

Made with ❤️ by [WildData](https://wilddata.cn)

**Official site: ** [https://github.com/WildDataX/suppr-mcp](https://github.com/WildDataX/suppr-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `research and data`, `文档翻译`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y suppr-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/zjg678-suppr.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
