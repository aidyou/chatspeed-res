---
title: "pkulaw-mcp-law-search"
description: "This is the MCP service provided by 北大法宝 for intelligent retrieval of laws and regulations. It uses text embedding for semantic retrieval."
---

# pkulaw-mcp-law-search

This is the MCP service provided by 北大法宝 for intelligent retrieval of laws and regulations. It uses text embedding for semantic retrieval.

# Peking University Fabao Legal Intelligent Retrieval MCP Service

This is the MCP service provided by [Peking University Fabao](https://www.pkulaw.com/) for intelligent retrieval of laws and regulations.

Tags: Search Tool

Peking University Fabao – Making law smarter.

## Tools

The legal intelligent retrieval MCP service provides the following tools:
- `get_article`: Retrieves the content of a legal article and its full name of the regulation through text containing the name of the regulation and the article number.
- `search_article`: Retrieves matching legal article contents and corresponding regulation names by performing semantic search on the text.

## MCP Client Usage

On the right side of the current page, under [Service Configuration Information], select [Streamable HTTP] or [sse], choose "No Authentication" for [Authentication Type], select the [Validity Period], and click [Connect] to generate the service configuration.

In the MCP client (e.g., CherryStudio), use the generated configuration to add the legal intelligent retrieval MCP service.

In the toolbar of the large model conversation, first enable the intelligent retrieval MCP service, then input something similar to the following to call the MCP service to complete the response:
- Please provide the exact content of Article 7 of the Civil Procedure Law without any modifications.
- What is the definition of dangerous goods in the law?

If the MCP client does not call the MCP service, add the prompt "Please use the tool to answer" at the beginning of the input:
- Please use the tool to answer, what is the definition of dangerous goods in the law?

## Contact

For any questions, please contact: .

**Official site: ** [https://pypi.org/project/pkulaw-mcp-proxy/@latest](https://pypi.org/project/pkulaw-mcp-proxy/@latest)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `search`
- Tags: `search`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `pkulaw-mcp-proxy --name pkulaw-mcp-law-search --backend-url https://apim-gateway.pkulaw.com/mcp-law-search-service --backend-token c5d14fd3-1c46-3bba-9fa7-64be73cc97ad`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/pkulaw-pkulaw-law-search.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
