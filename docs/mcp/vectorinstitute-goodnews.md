---
title: "mcp-goodnews"
description: "A Model Context Protocol server that fetches and ranks positive news articles from NewsAPI using Cohere LLM sentiment analysis, enabling users to access uplifting news stories through interfaces like…"
---

# mcp-goodnews

A Model Context Protocol server that fetches and ranks positive news articles from NewsAPI using Cohere LLM sentiment analysis, enabling users to access uplifting news stories through interfaces like…

_x000D_
_x000D_
# MCP Goodnews_x000D_
_x000D_
---_x000D_
_x000D_
[![CodeQL](/mcp-assets/7cb6a07622c89f1868d26563ea3805aa.svg)](https://github.com/VectorInstitute/mcp-goodnews/actions/workflows/github-code-scanning/codeql)_x000D_
[![Linting](/mcp-assets/265aa86a63acfcc94b0810633c43edd8.svg)](https://github.com/VectorInstitute/mcp-goodnews/actions/workflows/lint.yml)_x000D_
[![Unit Testing and Upload Coverage](/mcp-assets/330ad3cad933784a3af4ce0d96f20edb.svg)](https://github.com/VectorInstitute/mcp-goodnews/actions/workflows/unit_test.yml)_x000D_
[![codecov](/mcp-assets/1a234f4d2d89ec3ce218d06c6d518c8b.svg)](https://codecov.io/github/VectorInstitute/mcp-goodnews)_x000D_
[![Release](/mcp-assets/d5ccd5c5c7571857b94be33d0359c687.svg)](https://github.com/VectorInstitute/mcp-goodnews/actions/workflows/release.yml)_x000D_
![GitHub License](/mcp-assets/443190a98194af50f87289b7ed6cab6a.svg)_x000D_
_x000D_

_x000D_
  
_x000D_

_x000D_
_x000D_
MCP Goodnews is a simple Model Context Protocol (MCP) application that features_x000D_
a server for getting good, positive, and uplifting news. This tool fetches news_x000D_
articles from the [NewsAPI](https://newsapi.org/) and uses a Cohere LLM to rank_x000D_
and return the top news articles based on positive sentiment._x000D_
_x000D_
## Motivation_x000D_
_x000D_
In a world where negative news often dominates headlines, Goodnews MCP aims to_x000D_
shine a light on more positive and uplifting news stories. This project was_x000D_
inspired by an earlier initiative called GoodnewsFirst, which delivered positive_x000D_
news daily to email subscribers — it was a really awesome project! While GoodnewsFirst_x000D_
predated recent breakthroughs in Large Language Models (LLMs) and relied on_x000D_
traditional methods for sentiment ranking, Goodnews MCP leverages modern LLMs to_x000D_
perform sentiment analysis in a zero-shot setting._x000D_
_x000D_
## Example Usage: MCP Goodnews with Claude Desktop_x000D_
_x000D_

_x000D_
_x000D_
### Requirements_x000D_
_x000D_
- [Cohere API Key](https://dashboard.cohere.com/)_x000D_
- [NewsAPI Key](https://newsapi.org/)_x000D_
- [Claude Desktop Application](https://claude.ai/download)_x000D_
- [uv Python Project and Package Manager](https://docs.astral.sh/uv/getting-started/installation/)_x000D_
_x000D_
### Clone `mcp-goodnews`_x000D_
_x000D_
```
# Clone the repository_x000D_
git clone https://github.com/VectorInstitute/mcp-goodnews.git_x000D_
```
_x000D_
In the next step, we'll need to provide the absolute path to the location of this_x000D_
cloned repository._x000D_
_x000D_
### Update Claude Desktop Config to find mcp-goodnews_x000D_
_x000D_
#### For Mac/Linux_x000D_
_x000D_
```
# Navigate to the configuration directory_x000D_
cd ~/Library/Application Support/Claude/config_x000D_
_x000D_
# Edit the claude_desktop_config.json file_x000D_
nano claude_desktop_config.json_x000D_
```
_x000D_
#### For Windows_x000D_
_x000D_
```
# Navigate to the configuration directory_x000D_
cd %APPDATA%Claudeconfig_x000D_
_x000D_
# Edit the claude_desktop_config.json file_x000D_
notepad claude_desktop_config.json_x000D_
```
_x000D_
And you'll want to add an entry under `mcpServers` for `Goodnews`:_x000D_
_x000D_
```
{_x000D_
  "mcpServers": {_x000D_
    "Goodnews": {_x000D_
      "command": "
/uv",_x000D_
      "args": [_x000D_
        "--directory",_x000D_
        "
/mcp-goodnews/src/mcp_goodnews",_x000D_
        "run",_x000D_
        "server.py"_x000D_
      ],_x000D_
      "env": {_x000D_
        "NEWS_API_KEY": "",_x000D_
        "COHERE_API_KEY": ""_x000D_
      }_x000D_
    }_x000D_
  }_x000D_
}_x000D_
```
_x000D_
### Start or Restart Claude Desktop_x000D_
_x000D_
Claude Desktop will use the updated config to build and run the mcp-goodnews server._x000D_
If successful, you will see the hammer tool in the bottom-right corner of the chat_x000D_
dialogue window._x000D_
_x000D_

_x000D_
_x000D_
Clicking the hammer tool icon will bring up a modal that lists available MCP tools._x000D_
You should see `fetch_list_of_goodnews` listed there._x000D_
_x000D_

_x000D_
_x000D_
### Ask Claude for Good News!_x000D_
_x000D_
Example prompts:_x000D_
_x000D_
- "Show me some good news from today."_x000D_
- "What positive things happened in the world this week?"_x000D_
- "Give me uplifting news stories about science."_x000D_
_x000D_
## How It Works_x000D_
_x000D_
1. When you request good news, the application queries the NewsAPI for recent articles_x000D_
2. The Cohere LLM analyzes the sentiment of each article_x000D_
3. Articles are ranked based on positive sentiment score_x000D_
4. The top-ranking good news stories are returned to you through Claude_x000D_
_x000D_
## License_x000D_
_x000D_
[Apache 2.0](https://github.com/VectorInstitute/mcp-goodnews/blob/HEAD/LICENSE)_x000D_
_x000D_
---_x000D_
_x000D_
_Stay positive with Goodnews MCP!__x000D_

**Official site: ** [https://github.com/VectorInstitute/mcp-goodnews](https://github.com/VectorInstitute/mcp-goodnews)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `search`, `research and data`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `<absolute-path-to-bin>/uv`
- Args: `--directory <absolute-path-to-cloned-repo>/mcp-goodnews/src/mcp_goodnews run server.py`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/vectorinstitute-goodnews.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
