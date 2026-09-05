---
title: "mcp-ragdocs"
description: "An MCP server implementation that provides tools for retrieving and processing documentation through vector search, enabling AI assistants to augment their responses with relevant documentation contex…"
---

# mcp-ragdocs

An MCP server implementation that provides tools for retrieving and processing documentation through vector search, enabling AI assistants to augment their responses with relevant documentation contex…

# RAG Documentation MCP Server

An MCP server implementation that provides tools for retrieving and processing documents through vector search, enabling AI assistants to enhance their responses with relevant document context.

## Features

- Vector-based document search and retrieval
- Support for multiple document sources
- Semantic search capabilities
- Automated document processing
- Real-time context enhancement for LLMs

## Tools

### search_documentation
Searches stored documents using a natural language query. Returns matching excerpts with context, sorted by relevance.

**Inputs:**
- `query` (string): The text to search within the documents. Can be a natural language query, specific term, or code snippet.
- `limit` (number, optional): The maximum number of results to return (1-20, default: 5). A higher limit provides more comprehensive results but may require longer processing time.

### list_sources
Lists all document sources currently stored in the system. Returns a comprehensive list of all indexed documents, including source URL, title, and last updated time. Use this function to see what documents are searchable or to verify if a specific source has been indexed.

### extract_urls
Extracts and analyzes all URLs from a given web page. This tool crawls the specified web page, identifies all hyperlinks, and can optionally add them to the processing queue.

**Inputs:**
- `url` (string): The full URL of the web page to analyze (must include the protocol, e.g., https://). The page must be publicly accessible.
- `add_to_queue` (boolean, optional): If true, automatically adds the extracted URLs to the processing queue for later indexing. Use with caution for large sites to avoid over-queueing.

### remove_documentation
Removes a specific document source from the system by its URL. Removal is permanent and will affect future search results.

**Inputs:**
- `urls` (array of strings): An array of URLs to be removed from the database. Each URL must exactly match the one used when adding the document.

### list_queue
Lists all URLs currently waiting in the document processing queue. Displays the pending document sources that will be processed when calling run_queue. Use this function to monitor queue status, verify that URLs were added correctly, or check for backlog.

### run_queue
Processes and indexes all URLs in the document queue. Each URL is processed in order, with appropriate error handling and retry logic. Progress updates are provided during processing. Long-running operations will continue until the queue is empty or an unrecoverable error occurs.

### clear_queue
Removes all pending URLs from the document processing queue. Use this function when you want to start over, remove unwanted URLs, or cancel pending processing. This operation takes effect immediately and is irreversible—if you wish to process these URLs later, you will need to re-add them.

## Usage Instructions

Please note that the original document ends here and does not provide specific usage examples or guides. For information on how to configure or specific command-line parameters, please refer to the relevant sections or contact the support team for further assistance.

The RAG documentation tools are designed to achieve the following:

- Enhance AI responses with relevant documents
- Build document-aware AI assistants
- Create context-aware tools for developers
- Implement semantic document search
- Augment existing knowledge bases

## Configuration

### Using in Claude Desktop

Add the following to your `claude_desktop_config.json` file:

```json

{

  "mcpServers": {

    "rag-docs": {

      "command": "npx",

      "args": [

        "-y",

        "@hannesrudolph/mcp-ragdocs"

      ],

      "env": {

        "OPENAI_API_KEY": "",

        "QDRANT_URL": "",

        "QDRANT_API_KEY": ""

      }

    }

  }

}

```
You need to provide values for the following environment variables:
- `OPENAI_API_KEY`: OpenAI API key for generating embeddings
- `QDRANT_URL`: URL of your Qdrant vector database instance
- `QDRANT_API_KEY`: API key for authenticating with Qdrant

## License

This MCP server is licensed under the MIT License. This means you are free to use, modify, and distribute the software, subject to the terms and conditions of the MIT License. For more details, please refer to the LICENSE file in the project repository.

## Acknowledgments

This project is a fork of [qpd-v/mcp-ragdocs](https://github.com/qpd-v/mcp-ragdocs), originally developed by qpd-v. The original project provided the foundation for this implementation.

**Official site: ** [https://github.com/hannesrudolph/mcp-ragdocs](https://github.com/hannesrudolph/mcp-ragdocs)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`, `search`, `memory`
- Tags: `search`, `knowledge and memory`, `developer tools`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @hannesrudolph/mcp-ragdocs`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/hannesrudolph-ragdocs.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
