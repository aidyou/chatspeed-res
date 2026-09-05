---
title: "wechat_oa_mcp"
description: "WeChat Official Account MCP Service Description Service Overview The WeChat Official Account MCP (Model Control Protocol) service is a specialized tool designed to streamline the management of WeChat…"
---

# wechat_oa_mcp

WeChat Official Account MCP Service Description Service Overview The WeChat Official Account MCP (Model Control Protocol) service is a specialized tool designed to streamline the management of WeChat…

# WeChat Official Account MCP Server

This is a WeChat Official Account MCP server based on the FastMCP framework, providing a series of practical WeChat Official Account API interface encapsulations, including draft creation, publishing, deletion, and other functions.

## Project Introduction

This project uses Python and the FastMCP framework to provide WeChat Official Account management APIs through the Model Control Protocol (MCP) specification. It can be easily integrated into various AI systems and automated workflows, helping users conveniently manage WeChat Official Account content.

## WeChat Official Platform

WeChat Official Platform official website: [https://mp.weixin.qq.com](https://mp.weixin.qq.com)

You need to register and create an official account on the WeChat Official Platform first, and obtain the developer ID (AppID) and secret key (AppSecret) to use this tool.

## Installation Method

### Install via pip

```bash
pip install wechat_oa_mcp
```

## Project Structure

```
./
├── README.md              # Project documentation
├── examples/              # Usage examples
│   └── simple_usage.py    # Simple usage example
├── setup.py               # Installation configuration
├── pyproject.toml         # Python project configuration
└── wechat_oa_mcp/         # Main package directory
    ├── __init__.py        # Package initialization file
    ├── __main__.py        # Module direct execution entry
    ├── cli.py             # Command line tool entry
    └── server.py          # Main functionality code
```

## Dependencies

- Python 3.10+
- fastmcp
- requests

## Feature List

This server provides the following features:

- **Get WeChat Access Token**: Obtain interface calling credentials
- **Create WeChat Official Account Draft**: Create rich text message drafts
- **Publish WeChat Official Account Draft**: Publish drafts to the official account
- **Delete WeChat Official Account Draft**: Delete unpublished drafts
- **Delete Permanent Material**: Delete permanent materials in the official account

## API Interface Description

### 1. Get Access Token

```python
WeChat_get_access_token
```

**Input Parameters:**
```json
AppID: String·Third-party user unique credential (obtained from Official Account - Settings and Development - Development Interface Management)
AppSecret: String·Third-party user unique credential secret key (obtained from Official Account - Settings and Development - Development Interface Management)
```

**Output:**
```json
{
  "success": true,
  "error": null,
  "access_token": "obtained access_token",
  "expires_in": 7200
}
```

### 2. Create Draft

```python
WeChat_create_draft
```

**Input Parameters:**
```json
access_token: String·Your access_token, interface calling credential, can be obtained through WeChat_get_access_token
image_url: String·Cover image URL
title: String·Article title
content: String·The specific content of the rich text message, supports HTML tags, must be less than 20,000 characters, less than 1M
author: String·(Optional) Author name
digest: String·(Optional) Summary of the rich text message, only single rich text messages have summaries, multi-rich text is empty here. If this field is not filled, it will default to grab the first 54 characters of the content.
content_source_url: String·(Optional) Original address of the rich text message, i.e., the URL after clicking "Read original"
need_open_comment: Integer·(Optional) Uint32 Whether to open comments, 0 does not open (default), 1 opens
```

**Output:**
```json
{
  "success": true,
  "error": null,
  "draft_media_id": "draft's media_id",
  "image_media_id": "cover image's media_id"
}
```

### 3. Publish Draft

```python
WeChat_publish_draft
```

**Input Parameters:**
```json
access_token: String·Interface calling credential, can be obtained through WeChat_get_access_token
draft_media_id: String·The draft_media_id returned after previously calling WeChat_create_draft
```

**Output:**
```json
{
  "success": true,
  "error": null,
  "errmsg": "ok",
  "publish_id": "publish task id"
}
```

### 4. Delete Draft

```python
WeChat_del_draft
```

**Input Parameters:**
```json
access_token: String·Interface calling credential, can be obtained through WeChat_get_access_token
media_id: String·Draft corresponding credential, which is the draft_media_id returned by WeChat_create_draft
```

**Output:**
```json
{
  "success": true,
  "error": null,
  "errcode": 0,
  "errmsg": "ok"
}
```

### 5. Delete Permanent Material

```python
WeChat_del_material
```

**Input Parameters:**
```json
access_token: String·Interface calling credential, can be obtained through WeChat_get_access_token
media_id: String·Permanent material corresponding credential, which is the image_media_id returned by WeChat_create_draft
```

**Output:**
```json
{
  "success": true,
  "error": null,
  "errcode": 0,
  "errmsg": "ok"
}
```

## Usage Methods

### 1. Install the Server

```bash
# Install via pip
pip install wechat_oa_mcp
```

### 2. Several Ways to Call the MCP Server

#### 2.1 Call via Code

You can directly call the WeChat MCP API in Python code as follows (just complete the installation step to use it):

```python
from wechat_oa_mcp import (
    WeChat_get_access_token,
    WeChat_create_draft,
    WeChat_publish_draft,
    WeChat_del_draft,
    WeChat_del_material
)

# Get access_token
token_result = WeChat_get_access_token({
    "AppID": "Your WeChat AppID",
    "AppSecret": "Your WeChat AppSecret"
})

if token_result["success"]:
    access_token = token_result["access_token"]

    # Create draft
    draft_result = WeChat_create_draft({
        "access_token": access_token,
        "image_url": "https://example.com/image.jpg",
        "title": "Test Article Title",
        "content": "
This is the article content
",
        "author": "Author Name"
    })

    if draft_result["success"]:
        draft_id = draft_result["draft_media_id"]
        image_id = draft_result["image_media_id"]

        # Publish draft
        publish_result = WeChat_publish_draft({
            "access_token": access_token,
            "draft_media_id": draft_id
        })

        if publish_result["success"]:
            print(f"Published successfully! Publish ID: {publish_result['publish_id']}")

        # Delete draft example
        # Note: Usually drafts are deleted after publishing, this is just to demonstrate the API usage
        del_draft_result = WeChat_del_draft({
            "access_token": access_token,
            "media_id": draft_id
        })

        if del_draft_result["success"]:
            print(f"Deleted draft successfully: {del_draft_result['errmsg']}")

        # Delete material example
        # Note: Usually materials are deleted when they are no longer needed, this is just to demonstrate the API usage
        del_material_result = WeChat_del_material({
            "access_token": access_token,
            "media_id": image_id
        })

        if del_material_result["success"]:
            print(f"Deleted material successfully: {del_material_result['errmsg']}")
```

#### 2.2 Debug via MCP Inspector

After completing the installation step, you can use the following command for interactive testing:

```bash
npx @modelcontextprotocol/inspector python -m wechat_oa_mcp
```

Then visit http://localhost:6274 to conduct interactive testing

#### 2.3 Add mcp server via json

**Note: This method requires starting the MCP server first**

1. First start the service via command line:

```bash
# Direct startup (default port 8000)
wechat-oa-mcp
# Or
python -m wechat_oa_mcp

# Specify port to start
wechat-oa-mcp --port 8123
# Or
python -m wechat_oa_mcp --port 8123
```

2. Then add the WeChat MCP server to the configuration of other MCP compatible applications (such as Cursor):

```json
{
    "mcpServers": {
        "wechat_oa_mcp": {
            "type": "sse",
            "url": "http://localhost:8000/sse"
        }
    }
}
```

**Configuration Parameter Description:**
- `type`: Communication protocol type, supports "sse" (Server-Sent Events)
- `url`: Server address, the default port is 8000. If a port was previously specified, the specified port number will be used
- `wechat_oa_mcp`: Server name, can be customized

## Technical Architecture

This project is based on the FastMCP framework and provides WeChat Official Account related services through the MCP protocol. The server adopts a modular design, with each function encapsulated as an independent MCP tool that can be called separately.

The server internally communicates with the WeChat Official Account API through HTTP requests, handling authentication, parameter validation, and other details, allowing users to focus on business logic without worrying about the underlying implementation.

## Usage Limitations

To distribute server pressure, each IP can call the same interface at most five times per minute.

## IP Whitelist Configuration

According to the WeChat Official Account development interface management regulations, when calling the access_token interface through the developer ID and password, the source IP of the visit needs to be set as a whitelist. Please add the following IP to WeChat Official Account - Settings and Development - Development Interface Management - IP Whitelist:

```
106.15.125.133
```

## Acknowledgements

- Thanks to the FastMCP project for providing framework support

**Disclaimer: This MCP server is for research purposes only and is prohibited for commercial use.**

**Official site: ** [https://www.modelscope.cn/mcp](https://www.modelscope.cn/mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `developer tools`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `python`
- Args: `--directory /Users/project/mcp/wechat/wechat_oa_mcp -m wechat_oa_mcp --port 8123`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/jupiterc-wechat-oa.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
