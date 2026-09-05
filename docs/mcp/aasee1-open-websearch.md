---
title: "open-webSearch"
description: "Open-WebSearch MCP 服务器 English"
---

# open-webSearch

Open-WebSearch MCP 服务器 English

# Open-WebSearch MCP Server

[![ModelScope](/mcp-assets/c4cd95316a856a211a0787c96a4104c0.svg)](https://www.modelscope.cn/mcp/servers/Aasee1/open-webSearch)
[Smithery](https://smithery.ai/server/@Aas-ee/open-websearch)
![Version](/mcp-assets/bce8d6827d8524c4d5889bd04245a7f8.svg)
![License](/mcp-assets/443190a98194af50f87289b7ed6cab6a.svg)
![Issues](/mcp-assets/073392f73ddf9639c8800be249f9f141.svg)

**🇨🇳 Chinese | [🇺🇸 English](https://github.com/Aas-ee/open-webSearch/blob/HEAD/README.md)**

A Model Context Protocol (MCP) server based on multi-engine search results, supporting free web searches without the need for an API key.

  
Click to expand and view a simple example (deepseek-v3)

---

### 🧩 Example Start

### prompt:

> Use the websearch tool to query "Open-WebSearch MCP" with the CSDN engine, fetch 20 records, and tell me the engine used and related information. Then, through the URL, query the content of articles by Aasee (if there are multiple, query them in sequence, do not query simultaneously). Provide a structured output.

---

### assistant:

I will use the MCP_search tool to query "Open-WebSearch MCP" and use the CSDN engine to fetch 20 records.

### Query Result Analysis

1. **Search Engine Used**: CSDN
2. **Total Records**: 20

### List of Articles by Author Aasee
The search results show 2 articles by "Aasee":

1. **Article Title**: "Open Source AI Web Search Tool: Open-WebSearch MCP Fully Upgraded, Supports Multiple Engines + Streaming Response!"
   **URL**: https://blog.csdn.net/weixin_45801664/article/details/149000138
   **Summary**: This project provides free, controllable web search capabilities for AI plugin development, supporting Bing, Baidu, CSDN, and other multi-engine combined searches...

2. **Article Title**: "Web Search MCP Launched!"
   **URL**: https://blog.csdn.net/weixin_45801664/article/details/148813614
   **Summary**: The open-source Web search MCP server, Open-WebSearch, is now available, solving the problem of AI models being unable to access the latest web information...

### Start Querying the First Article Content
I will first query the full content of the first article:

# Search Result Analysis

## Engine Information Returned by the Tool
The CSDN search engine was used for the query, returning 20 relevant records.

## Content of Articles by Author Aasee

### Article 1: "Open Source AI Web Search Tool: Open-WebSearch MCP Fully Upgraded, Supports Multiple Engines + Streaming Response!"

🚀 Open Source AI Web Search Tool: Open-WebSearch MCP Fully Upgraded, Supports Multiple Engines + Streaming Response!

💡 "Let your AI plugins truly connect to the web" — No API Key required, controllable search results, ready to use out of the box!

Project Highlights:
✅ Multi-engine real-time search: Supports Bing, Baidu, CSDN, DuckDuckGo, Exa, Brave
✅ Streaming response (MCP protocol): Compatible with Claude plugin (MCP) protocol
✅ Article body extraction: Supports extracting full text of CSDN blog articles
✅ Completely free & no API Key required
✅ One-click Docker deployment

Installation Methods:
- Git clone the project: `git clone https://github.com/Aas-ee/open-webSearch`
- Or use Docker: `docker run -d --name web-search -p 3000:3000 -e ENABLE_CORS=true -e CORS_ORIGIN=* ghcr.io/aas-ee/open-web-search:latest`

MCP Tool Support:

🔍 search: Multi-engine search tool  
📄 fetchCsdnArticle: Extracts full text of CSDN articles  
🧪 fetchLinuxDoArticle: Fetches Linux.do articles (in development)  

Project Address:  
🧩 GitHub: https://github.com/Aas-ee/open-webSearch📦 Docker: ghcr.io/aas-ee/open-web-search:latest  

### Article 2: "Web Search MCP Launched!"

The open-source Web search MCP server, Open-WebSearch, is now online, addressing the issue of AI models not being able to access the latest web information. This project provides a free Baidu search results API, supporting structured JSON return formats and compatible with the MCP protocol of AI tools like Claude. Users can simply install and use it without needing an API key...

Do you need to look up content from other articles by Aasee? I can continue to retrieve them for you.

### ✅ Example Ends

---
## Features

- Conduct web searches using multiple search engines
  - bing
  - baidu
  - ~~linux.do~~ (not supported)
  - csdn
  - duckduckgo
  - exa
  - brave
- Supports HTTP proxy configuration, easily solving network access restrictions
- No API key or authentication required
- Returns structured results with title, URL, and description
- Configurable number of results returned per search
- Customizable default search engine
- Supports fetching the content of individual articles
  - csdn
  - github (README files)

## TODO
- Support for ~~Bing~~ (supported), ~~DuckDuckGo~~ (supported), ~~Exa~~ (supported), ~~Brave~~ (supported), Google, and more search engines
- Support for more blogs, forums, and social software
- Optimize article content extraction function, adding support for more sites
- ~~Support for GitHub README retrieval~~ (supported)

## Installation Guide

### NPX Quick Start (Recommended)

The fastest way to get started:

bash
# Basic usage
npx open-websearch@latest

# With environment variables (Linux/macOS)
DEFAULT_SEARCH_ENGINE=duckduckgo ENABLE_CORS=true npx open-websearch@latest

# Windows PowerShell
$env:DEFAULT_SEARCH_ENGINE="duckduckgo"; $env:ENABLE_CORS="true"; npx open-websearch@latest

# Cross-platform (requires cross-env, for local development)
# Global installation
npm install -g open-websearch
npx cross-env DEFAULT_SEARCH_ENGINE=duckduckgo ENABLE_CORS=true open-websearch

**Environment Variable Explanation:**

| Variable Name | Default Value                     | Possible Values | Description |
|---------------|-----------------------------------|-----------------|-------------|
| `ENABLE_CORS` | `false`                           | `true`, `false` | Enable CORS |
| `CORS_ORIGIN` | `*`                               | Any valid origin | CORS origin configuration |
| `DEFAULT_SEARCH_ENGINE` | `bing`                            | `bing`, `duckduckgo`, `exa`, `brave` | Default search engine |
| `USE_PROXY`   | `false`                           | `true`, `false` | Enable HTTP proxy |
| `PROXY_URL`   | `http://127.0.0.1:7890`           | Any valid URL    | Proxy server URL |
| `PORT`        | `3000`                            | 1-65535          | Server port |

**Common Configuration Examples:**
bash
# Enable proxy (for regions with restricted internet access)
USE_PROXY=true PROXY_URL=http://127.0.0.1:7890 npx open-websearch@latest

# Full configuration
DEFAULT_SEARCH_ENGINE=duckduckgo ENABLE_CORS=true USE_PROXY=true PROXY_URL=http://127.0.0.1:7890 PORT=8080 npx open-websearch@latest

**Notes for Windows Users:**
- Use `$env:VAR="value";` syntax in PowerShell
- For local development, it's recommended to use `npx cross-env` for cross-platform compatibility

### Local Installation

1. Clone or download this repository
2. Install dependencies:
   bash
   npm install
   
3. Build the server:
   bash
   npm run build
   
4. Add the server to your MCP configuration:

**Cherry Studio:**
json
{
  "mcpServers": {
    "web-search": {
      "name": "Web Search MCP",
      "type": "streamableHttp",
      "description": "Multi-engine web search with article fetching",
      "isActive": true,
      "baseUrl": "http://localhost:3000/mcp"
    }
  }
}

**VSCode Version (Claude Development Extension):**
json
{
  "mcpServers": {
    "web-search": {
      "transport": {
        "type": "streamableHttp",
        "url": "http://localhost:3000/mcp"
      }
    },
    "web-search-sse": {
      "transport": {
        "type": "sse",
        "url": "http://localhost:3000/sse"
      }
    }
  }
}

**Claude Desktop Version:**
json
{
  "mcpServers": {
    "web-search": {
      "transport": {
        "type": "streamableHttp",
        "url": "http://localhost:3000/mcp"
      }
    },
    "web-search-sse": {
      "transport": {
        "type": "sse",
        "url": "http://localhost:3000/sse"
      }
    }
  }
}

### Docker Deployment

Quick deployment using Docker Compose:

bashbash
docker-compose up -d

Or directly using Docker:
bash
docker run -d --name web-search -p 3000:3000 -e ENABLE_CORS=true -e CORS_ORIGIN=* ghcr.io/aas-ee/open-web-search:latest

Environment Variable Configuration Explanation:

| Variable Name | Default Value | Possible Values | Description |
|---------------|---------------|-----------------|-------------|
| `ENABLE_CORS` | `false` | `true`, `false` | Enable CORS |
| `CORS_ORIGIN` | `*` | Any valid origin | CORS origin configuration |
| `DEFAULT_SEARCH_ENGINE` | `bing` | `bing`, `duckduckgo`, `exa`, `brave` | Default search engine |
| `USE_PROXY` | `false` | `true`, `false` | Enable HTTP proxy |
| `PROXY_URL` | `http://127.0.0.1:7890` | Any valid URL | Proxy server URL |
| `PORT` | `3000` | 1-65535 | Server port |

Then, configure in the MCP client:
json
{
  "mcpServers": {
    "web-search": {
      "name": "Web Search MCP",
      "type": "streamableHttp",
      "description": "Multi-engine web search and article retrieval",
      "isActive": true,
      "baseUrl": "http://localhost:3000/mcp"
    },
    "web-search-sse": {
      "transport": {
        "name": "Web Search MCP",
        "type": "sse",
        "description": "Multi-engine web search and article retrieval",
        "isActive": true,
        "url": "http://localhost:3000/sse"
      }
    }
  }
}

## Usage Instructions

The server provides four tools: `search`, `fetchLinuxDoArticle`, `fetchCsdnArticle`, and `fetchGithubReadme`.

### Usage of the `search` Tool

typescript
{
  "query": string,        // Search query
  "limit": number,        // Optional: Number of results to return (default: 10)
  "engines": string[]     // Optional: Engines to use (bing, baidu, linuxdo, csdn, duckduckgo, exa, brave) default is bing
}

Example usage:
typescript
use_mcp_tool({
  server_name: "web-search",
  tool_name: "search",
  arguments: {
    query: "search content",
    limit: 3,  // Optional parameter
    engines: ["bing", "csdn", "duckduckgo", "exa", "brave"] // Optional parameter, supports multi-engine combined search
  }
})

Example response:
json
[
  {
    "title": "Example search result",
    "url": "https://example.com",
    "description": "Description text of the search result...",
    "source": "Source",
    "engine": "Used engine"
  }
]

### Usage of the `fetchCsdnArticle` Tool

Used to fetch the full content of a CSDN blog post.

typescript
{
  "url": string    // URL obtained from the `search` tool using the csdn engine
}

Example usage:
typescript
use_mcp_tool({
  server_name: "web-search",
  tool_name: "fetchCsdnArticle",
  arguments: {
    url: "https://blog.csdn.net/xxx/article/details/xxx"
  }
})

Example response:
json
[
  {
    "content": "Example search result"
  }
]

### Usage of the `fetchLinuxDoArticle` Tool

Used to fetch the full content of a Linux.do forum post.

typescript
{
  "url": string    // URL obtained from the `search` tool using the linuxdo engine
}

Example usage:
typescript
use_mcp_tool({
  server_name: "web-search",
  tool_name: "fetchLinuxDoArticle",
  arguments: {
    url: "https://xxxx.json"
  }
})

Example response:
json
[
  {
    "content": "Example search result"
  }
]

### Usage of the `fetchGithubReadme` Tool

Used to fetch the content of a GitHub repository's README file.

typescript
{
  "url": string    // GitHub repository URL (supports HTTPS, SSH formats)
}

Example usage:
typescript
use_mcp_tool({
  server_name: "web-search",
  tool_name: "fetchGithubReadme",
  arguments: {
    url: "https://github.com/Aas-ee/open-webSearch"
  }
})

Supported URL formats:
- HTTPS: `https://github.com/owner/repo`
- HTTPS with .git: `https://github.com/owner/repo.git`
- SSH: `git@github.com:owner/repo.git`
- URL with parameters: `https://github.com/owner/repo?tab=readme`

Example response:
json
[
  {

# Open-WebSearch MCP Server...

## Usage Limitations

Since this tool implements multi-engine search results through scraping, please note the following important limitations:

1. **Rate Limiting**:
    - Excessive searches in a short period may cause the used engines to temporarily block requests.
    - Recommendations:
        - Maintain a reasonable search frequency.
        - Use the `limit` parameter cautiously.
        - Set delays between searches if necessary.2. **Result Accuracy**:
    - Depends on the HTML structure of the corresponding engine, which may become invalid with engine updates
    - Some results may lack metadata such as descriptions
    - Complex search operators may not work as expected

3. **Legal Terms**:
    - This tool is for personal use only
    - Please comply with the service terms of the corresponding engine
    - It is recommended to implement appropriate frequency limits based on the actual usage scenario

4. **Search Engine Configuration**:
   - The default search engine can be set via the environment variable `DEFAULT_SEARCH_ENGINE`
   - Supported engines include: bing, duckduckgo, exa, brave
   - When searching for content on a specific website, the default search engine will be used automatically

5. **Proxy Service Configuration**:
   - When certain search engines are unavailable in specific regions, an HTTP proxy can be configured
   - Enable the proxy by setting the environment variable `USE_PROXY=true`
   - Configure the proxy server address using `PROXY_URL`

## Contribution Guidelines

We welcome bug reports and suggestions for feature improvements!

### Contributor Guidelines

If you want to fork this repository and publish your own Docker image, you need to configure the following:

#### GitHub Secrets Configuration

To enable automatic Docker image building and publishing, add the following secrets in your GitHub repository settings (Settings → Secrets and variables → Actions):

**Required Secrets:**
- `GITHUB_TOKEN`: Automatically provided by GitHub (no need to set)

**Optional Secrets (for Alibaba Cloud ACR):**
- `ACR_REGISTRY`: Your Alibaba Cloud Container Registry URL (e.g., `registry.cn-hangzhou.aliyuncs.com`)
- `ACR_USERNAME`: Your Alibaba Cloud ACR username
- `ACR_PASSWORD`: Your Alibaba Cloud ACR password
- `ACR_IMAGE_NAME`: Your image name in ACR (e.g., `your-namespace/open-web-search`)

#### CI/CD Workflow

The repository includes a GitHub Actions workflow (`/.github/workflows/docker.yml`) that will automatically:

1. **Trigger Conditions**:
    - Push to the `main` branch
    - Push a version tag (e.g., `v*`)
    - Manually trigger the workflow

2. **Build and Push to**:
    - GitHub Container Registry (ghcr.io) - always enabled
    - Alibaba Cloud Container Registry - only enabled if ACR secrets are configured

3. **Image Tags**:
    - `ghcr.io/your-username/open-web-search:latest`
    - `your-acr-address/your-image-name:latest` (if ACR is configured)

#### Fork and Publish Steps:

1. **Fork the repository** to your GitHub account
2. **Configure secrets** (if ACR publishing is needed):
    - Go to your forked repository's Settings → Secrets and variables → Actions
    - Add the ACR-related secrets listed above
3. **Push changes** to the `main` branch or create a version tag
4. **GitHub Actions will automatically build and push** your Docker image
5. **Use your image** by updating the Docker command:
   bash
   docker run -d --name web-search -p 3000:3000 -e ENABLE_CORS=true -e CORS_ORIGIN=* ghcr.io/your-username/open-web-search:latest
   

#### Notes:
- If you do not configure ACR secrets, the workflow will only publish to the GitHub Container Registry
- Ensure that your GitHub repository has Actions enabled
- The workflow will use your GitHub username (converted to lowercase) as the GHCR image name

## Star History
If the project is helpful to you, please consider giving it a ⭐ Star!

[![Star History Chart](/mcp-assets/7ff5ea12648cd650854ef8cf69c6f49e.svg)](https://www.star-history.com/#Aas-ee/open-webSearch&Date)

**Official site: ** [https://github.com/Aas-ee/open-webSearch](https://github.com/Aas-ee/open-webSearch)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `search`
- Tags: `search`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `open-websearch@1.2.5`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/aasee1-open-websearch.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
