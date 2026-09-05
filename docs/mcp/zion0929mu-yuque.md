---
title: "yuque"
description: "This project is based on the FastMCP framework and provides an MCP server dedicated to managing Yuque knowledge bases. The server supports automatically identifying and creating knowledge base groups…"
---

# yuque

This project is based on the FastMCP framework and provides an MCP server dedicated to managing Yuque knowledge bases. The server supports automatically identifying and creating knowledge base groups…

# Yuque Knowledge Base Management MCP Server

## Project Introduction
This project is based on the FastMCP framework and provides an MCP server dedicated to managing Yuque knowledge bases.
The server supports automatically identifying and creating knowledge base groups, creating or updating documents, getting document details, document lists, and the full knowledge base table of contents, with pagination and structured data return support.
All operations are based on the official Yuque API.

## Environment Configuration

### Dependency installation
Make sure Python 3.8+ is installed, then install the dependencies.
This project mainly depends on the following Python packages:
- fastmcp
- starlette
- requests
- python-dotenv

Install them with:
```bash
pip install fastmcp starlette requests python-dotenv
```

If the project root has a `requirements.txt` file, you can also use:
```bash
pip install -r requirements.txt
```

### Environment variable configuration
Create a `.env` file in the project root and configure the following environment variables:
- `YUQUE_SPACE_SUBDOMAIN`: Yuque space subdomain (used as the URL prefix to access the Yuque space, e.g. https://[SUBDOMAIN].yuque.com)
- `DEFAULT_API_TOKEN`: default API access token (used to authenticate calls to the Yuque API)
- `DEFAULT_GROUP_LOGIN`: default group (team) alias (identifies the Yuque group to access)
- `DEFAULT_BOOK_SLUG`: default knowledge base alias (the unique identifier of a Yuque doc library, used to locate a specific doc library)

Example:
```
YUQUE_SPACE_SUBDOMAIN=your_space_subdomain_here
DEFAULT_API_TOKEN=your_api_token_here
DEFAULT_GROUP_LOGIN=your_group_login_here
DEFAULT_BOOK_SLUG=your_book_slug_here
```

These variables can also be passed through the MCP client request headers. Example config file:

```json
{
    "mcpServers": {
       "yuque-mcp": {
          "url": "http://192.168.125.89:8000/mcp",
          "headers": {
              "YUQUE_SPACE_SUBDOMAIN": "www",
              "DEFAULT_API_TOKEN": "M4HeyBFsRmyNDsdfsdfsdf7ut3YFPX",
              "DEFAULT_GROUP_LOGIN": "oxsdf47",
              "DEFAULT_BOOK_SLUG": "vfgsd6"
            }
        }
    }
}
```

## Starting the Service

Run the main server program `server.py`, supporting multiple transport modes:

```bash
python server.py --transport streamable-http
```

Available transport modes:
- `streamable-http` (default): HTTP stream-based transport
- `sse`: Server-Sent Events
- `stdio`: standard input/output streams

## Tools

The server automatically loads all tool modules in the `tools/` directory, mainly including:

- `create_yuque_group(name: str)`
  Creates a group (directory) in the Yuque knowledge base.

  Parameters:
    * `name (str)`: the group name to create. The name should be unique within the current knowledge base.

- `create_yuque_doc_in_group(...)`
  Creates a document under a specified group in the Yuque knowledge base. If the group does not exist, it will be created first, then the document is created in it.

  Parameters:
    * `group_name (str)`: group name. If it does not exist, it will be created automatically.
    * `doc_title (str)`: the title of the document to create.
    * `doc_body (str)`: the document content, supporting Markdown format.

- `get_yuque_doc_list(group_login, book_slug, offset, limit)`
  Gets the document list in the knowledge base, with pagination support.

- `get_yuque_doc_detail(...)`
  Gets the detailed content of a specified document.

- `get_yuque_repo_toc(...)`
  Gets the full table of contents of the knowledge base.

## Usage Examples

Start the server with the default transport:

```bash
python server.py
```

Specify the SSE transport mode:

```bash
python server.py --transport sse
```

## Important Yuque Concepts
The API domain is https://www.yuque.com, but note that accessing resources in a space requires using that space's subdomain.

URL path:

Yuque URLs follow a certain format, e.g. https://www.yuque.com/yuque/developer/api.
This contains the user or team name, the knowledge base identifier, and the document identifier.

```
https://www.yuque.com/yuque/developer/api        [Full document access path]
                        |
                        +-- yuque/               [team or user login name (group_login)]
                                |
                                +-- developer/   [knowledge base identifier (book_slug)]
                                       |
                                       +-- api   [document identifier (doc_slug)]
```

## Yuque Authentication

All Yuque open APIs require Token authentication before access.

### Individual user authentication (super member exclusive benefit)
You can get the Token by clicking your Yuque avatar and entering the Personal Settings page, as shown below:

![image](/mcp-assets/8cf4c6f82bbac039a3c8f97076084382.png)

### Enterprise team authentication (flagship space exclusive benefit)
Teams within the space can get it from the team settings page (only available in flagship spaces), as shown below.

![image](/mcp-assets/2e0c10d8804ee1f82d33c36ca587af67.png)

## Contribution Guide

Issues and Pull Requests are welcome to improve features or fix problems.

## Contact

If you have questions, please contact the project maintainer.

**Official site: ** [https://github.com/lijian-ui/yuque-mcp](https://github.com/lijian-ui/yuque-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `memory`
- Tags: `knowledge and memory`, `chinese`

## MCP Configuration

- Transport: `http`
- Command: ``
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/zion0929mu-yuque.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
