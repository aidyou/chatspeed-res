---
title: "metaso-search"
description: "MCP Service of Mitell AI Search 1. 概述 秘塔AI搜索的MCP（Multi-Cloud Platform）服务是一种多云平台解决方案，旨在帮助企业更高效地管理和利用来自不同云服务商的资源。通过MCP，用户可以轻松地在多个云环境之间迁移应用和服务，同时享受统一的管理和监控体验。 2. 功能特点 - 跨云管理：支持对阿里云、腾讯云等主流云服务商的资源进行集中管理。 -…"
---

# metaso-search

MCP Service of Mitell AI Search 1. 概述 秘塔AI搜索的MCP（Multi-Cloud Platform）服务是一种多云平台解决方案，旨在帮助企业更高效地管理和利用来自不同云服务商的资源。通过MCP，用户可以轻松地在多个云环境之间迁移应用和服务，同时享受统一的管理和监控体验。 2. 功能特点 - 跨云管理：支持对阿里云、腾讯云等主流云服务商的资源进行集中管理。 -…

# Metasota AI Search MCP Service

## Introduction

The Metasota AI Search MCP service is an intelligent search and Q&A service based on the Model Context Protocol (MCP), providing powerful web search, content reading, and intelligent Q&A capabilities for AI assistants. By integrating this service, AI assistants can obtain real-time web information, read web page content, and provide accurate intelligent Q&A based on RAG technology.

## Service Address

**ModelScope Address**: [https://www.modelscope.cn/mcp/servers/metasota/metaso-search](https://www.modelscope.cn/mcp/servers/metasota/metaso-search)

**API Endpoint**: `https://metaso.cn/api/mcp`

## Features

### 🔍 Multi-Dimensional Search
- Supports searching various content types including web pages, documents, papers, images, videos, and podcasts
- Flexible search scope configuration
- Customizable number of returned results

### 📖 Web Content Reading
- Extracts content from any URL
- Provides output in JSON and Markdown formats
- Intelligent content parsing and structuring

### 💬 Intelligent Q&A Service
- Based on RAG (Retrieval-Augmented Generation) technology
- Supports multiple models, with a fast model as the default
- Provides accurate answers combined with search results

## Tool List

### 1. metaso_web_search - Web Search Tool

**Function Description**: Searches for web pages, documents, papers, images, videos, and podcasts based on keywords

**Parameter Explanation**:
- `q` (Required, string): Search query keyword
- `scope` (Optional, string): Search scope, possible values: `webpage`, `document`, `paper`, `image`, `video`, `podcast`
- `includeSummary` (Optional, boolean): Enhances search result recall through web page summary information
- `includeRawContent` (Optional, boolean): Scrapes the original text from all source web pages
- `size` (Optional, integer): Number of returned results, default is 10

**Usage Example**:

json
{
  "q": "latest developments in artificial intelligence",
  "scope": "paper",
  "includeSummary": true,
  "size": 5
}

### 2. metaso_web_reader - Web Content Reading Tool

**Function Description**: Reads the content of a specified URL

**Parameter Explanation**:
- `url` (Required, string): The URL to be read
- `format` (Required, string): Output format, possible values: `json`, `markdown`

**Usage Example**:

json
{
  "url": "https://example.com/article",
  "format": "markdown"
}

### 3. metaso_chat - Intelligent Q&A Tool

**Function Description**: Intelligent Q&A service based on RAG

**Parameter Explanation**:
- `message` (Required, string): User question
- `model` (Optional, string): The model to use, default is "fast"

**Usage Example**:

json
{
  "message": "Please explain the basic principles of quantum computing",
  "model": "fast"
}

## Configuration

### 1. Basic Configuration

Add the following configuration to your MCP client configuration file:
> Replace YOUR_API_KEY with your own API key
json
{
  "mcpServers": {
    "metaso": {
      "url": "https://metaso.cn/api/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}

VSCode Configuration
json
{
  "servers": {
    "metaso": {
      "url": "https://metaso.cn/api/mcp",
      "type": "http",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  },
  "inputs": []
}

### 2. API Key Acquisition

1. Visit the Metasota AI Search official website
2. Register and log in to your account
3. Obtain the API key from the API console [(https://metaso.cn/search-api/api-keys)](https://metaso.cn/search-api/api-keys)
4. Replace `YOUR_API_KEY` in the configuration with the obtained key

## Use Cases

### 📚 Academic Research
- Search for the latest papers and research materials
- Obtain academic documents in specific fields
- Quickly get background information for research

### 📰 Information Retrieval
- Real-time news and information search
- Quick extraction of web page content
- Discovery of multimedia content

### 🤖 AI Enhancement
- Provide real-time information retrieval capabilities for AI assistants
- Enhance the knowledge base of conversational systems
- Support intelligent Q&A based on the latest information

### 💼 Business Applications
- Market research and competitive analysis
- Industry trend monitoring
- Construction of customer service knowledge bases

## Technical Advantages

- **High Performance**: Based on the powerful search engine of Metasota AI Search
- **Multi-Format Support**: Supports various content types and output formats- **RAG Technology**: Combines retrieval and generation to provide accurate answers
- **Easy Integration**: Standard MCP protocol, highly compatible
- **Flexible Configuration**: Rich parameter options to meet different needs

## Precautions

1. **API Quota**: Please be aware of the API call quota limits and use the service reasonably.
2. **Content Compliance**: Ensure that the content searched for and obtained complies with relevant laws and regulations.
3. **Caching Strategy**: It is recommended to implement an appropriate caching strategy to improve efficiency.
4. **Error Handling**: Please implement suitable error handling mechanisms in your application.

## Support and Feedback

If you encounter any issues or have suggestions for improvement during use, feel free to contact us through the following methods:

- Official Technical Support Email: support-1@metasota.ai
- Customer Service on Official Website: 19980541467 (same number for WeChat)

---

*This service is supported by the Metasota AI Search team, dedicated to providing high-quality AI search solutions for developers.*

**Official site: ** [https://metaso.cn/api/mcp](https://metaso.cn/api/mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `developer tools`, `chinese`

## MCP Configuration

- Transport: `http`
- Command: ``
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/metasota-metaso-search.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
