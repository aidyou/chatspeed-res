---
title: "zotero-mcp"
description: "Connects your Zotero research library with Claude and other AI assistants via the Model Context Protocol, allowing you to search your library, access content, discuss papers, get summaries, and analyz…"
---

# zotero-mcp

Connects your Zotero research library with Claude and other AI assistants via the Model Context Protocol, allowing you to search your library, access content, discuss papers, get summaries, and analyz…

# Zotero MCP: Your Research Library in Claude

  

    

  

  

    

  

  

    

  

**Zotero MCP** seamlessly connects your [Zotero](https://www.zotero.org/) research library with [Claude](https://www.anthropic.com/claude) and other AI assistants ([Cherry Studio](https://cherry-ai.com/), [Cursor](https://www.cursor.com/), etc.) via the [Model Context Protocol](https://modelcontextprotocol.io/introduction). Discuss papers, get summaries, analyze citations, extract PDF annotations, and more!

## ✨ Features

### 🔍 Search Your Library
- Find papers, articles, and books by title, author, or content
- Perform complex searches with multiple criteria
- Browse collections, tags, and recent additions

### 📚 Access Your Content
- Retrieve detailed metadata for any item
- Get full text content (when available)
- Access attachments, notes, and child items

### 📝 Work with Annotations
- Extract and search PDF annotations directly
- Access Zotero's native annotations
- Create and update notes and annotations

### 🌐 Flexible Access Methods
- Local method for offline access (no API key needed)
- Web API for cloud library access
- Perfect for both local research and remote collaboration

## 🚀 Quick Install

### Installing via Smithery

To install Zotero MCP for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@54yyyu/zotero-mcp):

```bash
npx -y @smithery/cli install @54yyyu/zotero-mcp --client claude
```

### Manual Installation

#### Installing via uv

```bash
uv tool install "git+https://github.com/54yyyu/zotero-mcp.git"
zotero-mcp setup  # Auto-configure for Claude Desktop
```

#### Installing via pip

```bash
pip install git+https://github.com/54yyyu/zotero-mcp.git
zotero-mcp setup  # Auto-configure for Claude Desktop
```

## 🖥️ Setup & Usage

Full documentation is available at [Zotero MCP docs](https://stevenyuyy.us/zotero-mcp/).

**Requirements**
- Python 3.10+
- Zotero 7+ (for local API with full-text access)
- Claude Desktop or compatible AI assistant

### For Claude Desktop

#### Configuration
After installation, either:

1. **Auto-configure** (recommended):
```bash
   zotero-mcp setup
```

2. **Manual configuration**:
   Add to your `claude_desktop_config.json`:
```json
   {
     "mcpServers": {
       "zotero": {
         "command": "zotero-mcp",
         "env": {
           "ZOTERO_LOCAL": "true"
         }
       }
     }
   }
```

#### Usage

1. Start Zotero desktop (make sure local API is enabled in preferences)
2. Launch Claude Desktop
3. Access the Zotero-MCP tool through Claude Desktop's tools interface

Example prompts:
- "Search my library for papers on machine learning"
- "Find recent articles I've added about climate change"
- "Summarize the key findings from my paper on quantum computing"
- "Extract all PDF annotations from my paper on neural networks"
- "Search my notes and annotations for mentions of 'reinforcement learning'"

### For Cherry Studio

#### Configuration
Go to Settings -> MCP Servers -> Edit MCP Configuration, and add the following:

```json
{
  "mcpServers": {
    "zotero": {
      "name": "zotero",
      "type": "stdio",
      "isActive": true,
      "command": "zotero-mcp",
      "args": [],
      "env": {
        "ZOTERO_LOCAL": "true"
      }
    }
  }
}
```
Then click "Save".

Cherry Studio also provides a visual configuration method for general settings and tools selection.

## 🔧 Advanced Configuration

### Using Web API Instead of Local API

For accessing your Zotero library via the web API (useful for remote setups):

```bash
zotero-mcp setup --no-local --api-key YOUR_API_KEY --library-id YOUR_LIBRARY_ID
```

### Environment Variables

- `ZOTERO_LOCAL=true`: Use the local Zotero API (default: false)
- `ZOTERO_API_KEY`: Your Zotero API key (for web API)
- `ZOTERO_LIBRARY_ID`: Your Zotero library ID (for web API)
- `ZOTERO_LIBRARY_TYPE`: The type of library (user or group, default: user)

### Command-Line Options

```bash
# Run the server directly
zotero-mcp serve

# Specify transport method
zotero-mcp serve --transport stdio|sse

# Get help on setup options
zotero-mcp setup --help
```

## 📑 PDF Annotation Extraction

Zotero MCP includes advanced PDF annotation extraction capabilities:

- **Direct PDF Processing**: Extract annotations directly from PDF files, even if they're not yet indexed by Zotero
- **Enhanced Search**: Search through PDF annotations and comments 
- **Image Annotation Support**: Extract image annotations from PDFs
- **Seamless Integration**: Works alongside Zotero's native annotation system

For optimal annotation extraction, it is **highly recommended** to install the [Better BibTeX plugin](https://retorque.re/zotero-better-bibtex/installation/) for Zotero. The annotation-related functions have been primarily tested with this plugin and provide enhanced functionality when it's available.

The first time you use PDF annotation features, the necessary tools will be automatically downloaded.

## 📚 Available Tools

### Search Tools
- `zotero_search_items`: Search your library
- `zotero_advanced_search`: Perform complex searches
- `zotero_get_collections`: List collections
- `zotero_get_collection_items`: Get items in a collection
- `zotero_get_tags`: List all tags
- `zotero_get_recent`: Get recently added items

### Content Tools
- `zotero_get_item_metadata`: Get detailed metadata
- `zotero_get_item_fulltext`: Get full text content
- `zotero_get_item_children`: Get attachments and notes

### Annotation & Notes Tools
- `zotero_get_annotations`: Get annotations (including direct PDF extraction)
- `zotero_get_notes`: Retrieve notes from your Zotero library
- `zotero_search_notes`: Search in notes and annotations (including PDF-extracted)
- `zotero_create_note`: Create a new note for an item (beta feature)

## 🔍 Troubleshooting

- **No results found**: Ensure Zotero is running and the local API is enabled
- **Can't connect to library**: Check your API key and library ID if using web API
- **Full text not available**: Make sure you're using Zotero 7+ for local full-text access

## 📄 License

MIT

**Official site: ** [https://github.com/54yyyu/zotero-mcp](https://github.com/54yyyu/zotero-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `search`, `data`
- Tags: `research and data`, `search`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `zotero-mcp`
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/54yyyu-zotero.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
