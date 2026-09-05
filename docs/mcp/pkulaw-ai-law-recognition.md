---
title: "mcp_server_law_recognition"
description: "Automatically identify and extract legal provisions from texts (e.g., contracts, case descriptions, legal documents), accurately pinpoint specific provisions (such as \"Article 585 of the Civil Code\")…"
---

# mcp_server_law_recognition

Automatically identify and extract legal provisions from texts (e.g., contracts, case descriptions, legal documents), accurately pinpoint specific provisions (such as "Article 585 of the Civil Code")…

# Project description
[Chinalawinfo Co. Ltd.](https://www.pkulaw.com/) Treasure Legal Article Recognition MCP is a dynamic, real-time analysis engine that automatically recognizes and extracts legal provisions from text. It accepts input text, uses model reasoning and dictionary precise matching, and recognizes the legal names and specific provisions (clauses, items) mentioned in it in real time, and performs standardized verification and recommendation.

Usage scenarios:
1. Extract legal names and clauses from text paragraphs, such as in contracts, case descriptions or legal documents, accurately locate the specific legal provisions involved (such as "Article 585 of the Civil Code")
2. Verify and match the extracted legal names with the standard names and clauses in the legal database

# Requirements
- requires-python = ">=3.10"
- mcp>=1.0.0
# Installation
- pip install mcp_server_law_recognition
# Usage
## Sample
    from mcp import ClientSession, StdioServerParameters, types
    from mcp.client.stdio import stdio_client
    server_params = StdioServerParameters(
        command="python",  # Executable
        args=["-m","mcp_server_law_recognition"],  # Optional command line arguments
        env={
            "pkulaw_api_key": "da9629867ee841518***********"
        }  # Optional environment variables
    )

    async def run():
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(
                read, write
            ) as session:
                # Initialize the connection
                await session.initialize()

            tools = await session.list_tools()
            print('tools:',tools)
            result = await session.call_tool("get_law_recognition", arguments={"text": "根据《民法典》第一千二百六十条规定，该法自2021年1月1日起施行，同时废止了《中华人民共和国婚姻法》、《中华人民共和国继承法》、《中华人民共和国民法通则》..."})
            print('result:',result)

    if __name__ == "__main__":
        import asyncio

        asyncio.run(run())
# Return result
- Text: Name in the original text for model recognition
- Original: Standard regulatory names in the pkulaw database
- Full-text: Regulatory content in pkulaw database
- source: Pkulaw url
# Contact US
- Apply for an APIKEY:fxtj@chinalawinfo.com

**Official site: ** [https://pypi.org/project/mcp-server-law-recognition](https://pypi.org/project/mcp-server-law-recognition)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `developer tools`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `python`
- Args: `-m mcp_server_law_recognition`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/pkulaw-ai-law-recognition.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
