---
title: "Google-Search-MCP-Server"
description: "An MCP (Model Context Protocol) server that provides Google search capabilities and webpage content analysis tools. This server enables AI models to perform Google searches and analyze webpage content…"
---

# Google-Search-MCP-Server

An MCP (Model Context Protocol) server that provides Google search capabilities and webpage content analysis tools. This server enables AI models to perform Google searches and analyze webpage content…

# Built For use with Cline + VS Code!_x000D_
_x000D_
# Google Search MCP Server_x000D_
_x000D_
An MCP (Model Context Protocol) server that provides Google search capabilities and webpage content analysis tools. This server enables AI models to perform Google searches and analyze webpage content programmatically._x000D_
_x000D_
## Features_x000D_
_x000D_
- Advanced Google Search with filtering options (date, language, country, safe search)_x000D_
- Detailed webpage content extraction and analysis_x000D_
- Batch webpage analysis for comparing multiple sources_x000D_
- Environment variable support for API credentials_x000D_
- Comprehensive error handling and user feedback_x000D_
- MCP-compliant interface for seamless integration with AI assistants_x000D_
_x000D_
## Prerequisites_x000D_
_x000D_
- Node.js (v16 or higher)_x000D_
- Python (v3.8 or higher)_x000D_
- Google Cloud Platform account_x000D_
- Custom Search Engine ID_x000D_
- Google API Key_x000D_
_x000D_
## Installation_x000D_
_x000D_
1. Clone the repository:_x000D_
```
   git clone https://github.com/your-username/google-search-mcp.git_x000D_
   cd google-search-mcp_x000D_
```
_x000D_
2. Install Node.js dependencies:_x000D_
```
   npm install_x000D_
```
_x000D_
3. Install Python dependencies:_x000D_
```
   pip install flask google-api-python-client flask-cors beautifulsoup4 trafilatura markdownify_x000D_
```
_x000D_
4. Build the TypeScript code:_x000D_
```
   npm run build_x000D_
```
_x000D_
5. Create a helper script to start the Python servers (Windows example):_x000D_
```
   # Create start-python-servers.cmd_x000D_
   @echo off_x000D_
   echo Starting Python servers for Google Search MCP..._x000D_
   _x000D_
   REM Start Python search server_x000D_
   start "Google Search API" cmd /k "python google_search.py"_x000D_
   _x000D_
   REM Start Python link viewer_x000D_
   start "Link Viewer" cmd /k "python link_view.py"_x000D_
   _x000D_
   echo Python servers started. You can close this window._x000D_
```
_x000D_
## Configuration_x000D_
_x000D_
### API Credentials_x000D_
_x000D_
You can provide Google API credentials in two ways:_x000D_
_x000D_
1. **Environment Variables** (Recommended):_x000D_
   - Set `GOOGLE_API_KEY` and `GOOGLE_SEARCH_ENGINE_ID` in your environment_x000D_
   - The server will automatically use these values_x000D_
_x000D_
2. **Configuration File**:_x000D_
   - Create an `api-keys.json` file in the root directory:_x000D_
```
   {_x000D_
       "api_key": "your-google-api-key",_x000D_
       "search_engine_id": "your-custom-search-engine-id"_x000D_
   }_x000D_
```
_x000D_
### MCP Settings Configuration_x000D_
_x000D_
Add the server configuration to your MCP settings file:_x000D_
_x000D_
#### For Cline (VS Code Extension)_x000D_
File location: `%APPDATA%CodeUserglobalStoragesaoudrizwan.claude-devsettingscline_mcp_settings.json`_x000D_
_x000D_
```
{_x000D_
  "mcpServers": {_x000D_
    "google-search": {_x000D_
      "command": "C:\Program Files\nodejs\node.exe",_x000D_
      "args": ["C:\path\to\google-search-mcp\dist\google-search.js"],_x000D_
      "cwd": "C:\path\to\google-search-mcp",_x000D_
      "env": {_x000D_
        "GOOGLE_API_KEY": "your-google-api-key",_x000D_
        "GOOGLE_SEARCH_ENGINE_ID": "your-custom-search-engine-id"_x000D_
      },_x000D_
      "disabled": false,_x000D_
      "autoApprove": []_x000D_
    }_x000D_
  }_x000D_
}_x000D_
```
_x000D_
#### For Claude Desktop App_x000D_
File location: `%APPDATA%Claudeclaude_desktop_config.json`_x000D_
_x000D_
```
{_x000D_
  "mcpServers": {_x000D_
    "google-search": {_x000D_
      "command": "C:\Program Files\nodejs\node.exe",_x000D_
      "args": ["C:\path\to\google-search-mcp\dist\google-search.js"],_x000D_
      "cwd": "C:\path\to\google-search-mcp",_x000D_
      "env": {_x000D_
        "GOOGLE_API_KEY": "your-google-api-key",_x000D_
        "GOOGLE_SEARCH_ENGINE_ID": "your-custom-search-engine-id"_x000D_
      },_x000D_
      "disabled": false,_x000D_
      "autoApprove": []_x000D_
    }_x000D_
  }_x000D_
}_x000D_
```
_x000D_
## Running the Server_x000D_
_x000D_
### Method 1: Start Python Servers Separately (Recommended)_x000D_
_x000D_
1. First, start the Python servers using the helper script:_x000D_
```
   start-python-servers.cmd_x000D_
```
_x000D_
2. Configure the MCP settings to run only the Node.js server:_x000D_
```
   {_x000D_
     "command": "C:\Program Files\nodejs\node.exe",_x000D_
     "args": ["C:\path\to\google-search-mcp\dist\google-search.js"]_x000D_
   }_x000D_
```
_x000D_
### Method 2: All-in-One Script_x000D_
_x000D_
Start both the TypeScript and Python servers with a single command:_x000D_
```
npm run start:all_x000D_
```
_x000D_
## Available Tools_x000D_
_x000D_
### 1. google_search_x000D_
Search Google and return relevant results from the web. This tool finds web pages, articles, and information on specific topics using Google's search engine._x000D_
_x000D_
```
{_x000D_
  "name": "google_search",_x000D_
  "arguments": {_x000D_
    "query": "your search query",_x000D_
    "num_results": 5, // optional, default: 5, max: 10_x000D_
    "date_restrict": "w1", // optional, restrict to past day (d1), week (w1), month (m1), year (y1)_x000D_
    "language": "en", // optional, ISO 639-1 language code (en, es, fr, de, ja, etc.)_x000D_
    "country": "us", // optional, ISO 3166-1 alpha-2 country code (us, uk, ca, au, etc.)_x000D_
    "safe_search": "medium" // optional, safe search level: "off", "medium", "high"_x000D_
  }_x000D_
}_x000D_
```
_x000D_
### 2. extract_webpage_content_x000D_
Extract and analyze content from a webpage, converting it to readable text. This tool fetches the main content while removing ads, navigation elements, and other clutter._x000D_
_x000D_
```
{_x000D_
  "name": "extract_webpage_content",_x000D_
  "arguments": {_x000D_
    "url": "https://example.com"_x000D_
  }_x000D_
}_x000D_
```
_x000D_
### 3. extract_multiple_webpages_x000D_
Extract and analyze content from multiple webpages in a single request. Ideal for comparing information across different sources or gathering comprehensive information on a topic._x000D_
_x000D_
```
{_x000D_
  "name": "extract_multiple_webpages",_x000D_
  "arguments": {_x000D_
    "urls": [_x000D_
      "https://example1.com",_x000D_
      "https://example2.com"_x000D_
    ]_x000D_
  }_x000D_
}_x000D_
```
_x000D_
## Example Usage_x000D_
_x000D_
Here are some examples of how to use the Google Search MCP tools:_x000D_
_x000D_
### Basic Search_x000D_
```
Search for information about artificial intelligence_x000D_
```
_x000D_
### Advanced Search with Filters_x000D_
```
Search for recent news about climate change from the past week in Spanish_x000D_
```
_x000D_
### Content Extraction_x000D_
```
Extract the content from https://example.com/article_x000D_
```
_x000D_
### Multiple Content Comparison_x000D_
```
Compare information from these websites:_x000D_
- https://site1.com/topic_x000D_
- https://site2.com/topic_x000D_
- https://site3.com/topic_x000D_
```
_x000D_
## Getting Google API Credentials_x000D_
_x000D_
1. Go to the [Google Cloud Console](https://console.cloud.google.com/)_x000D_
2. Create a new project or select an existing one_x000D_
3. Enable the Custom Search API_x000D_
4. Create API credentials (API Key)_x000D_
5. Go to the [Custom Search Engine](https://programmablesearchengine.google.com/about/) page_x000D_
6. Create a new search engine and get your Search Engine ID_x000D_
7. Add these credentials to your `api-keys.json` file_x000D_
_x000D_
## Error Handling_x000D_
_x000D_
The server provides detailed error messages for:_x000D_
- Missing or invalid API credentials_x000D_
- Failed search requests_x000D_
- Invalid webpage URLs_x000D_
- Network connectivity issues_x000D_
_x000D_
## Architecture_x000D_
_x000D_
The server consists of two main components:_x000D_
1. TypeScript MCP Server: Handles MCP protocol communication and provides the tool interface_x000D_
2. Python Flask Server: Manages Google API interactions and webpage content analysis_x000D_
_x000D_
## License_x000D_
_x000D_
MIT_x000D_

**Official site: ** [https://github.com/mixelpixx/Google-Search-MCP-Server](https://github.com/mixelpixx/Google-Search-MCP-Server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `browser`
- Tags: `search`, `browser automation`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `node`
- Args: `/path/to/google-search-mcp-server/dist/google-search.js`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/mixelpixx-google-search.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
