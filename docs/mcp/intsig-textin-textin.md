---
title: "textin-mcp"
description: "A server that enables OCR capabilities to recognize text from images, PDFs, and Word documents, convert them to Markdown, and extract key information."
---

# textin-mcp

A server that enables OCR capabilities to recognize text from images, PDFs, and Word documents, convert them to Markdown, and extract key information.

# Textin MCP Server

TextIn MCP Server is a tool for extracting text and performing OCR on documents, including document text recognition, ID recognition, and invoice recognition. It also supports converting documents into Markdown format.

  

## Tools
- `recognition_text`
  - Text recognition from images, Word documents, and PDF files.
  - Input: `file path` (string)
  - Return: Text of the document.

- `doc_to_markdown`
  - Convert images, PDFs, and Word documents to Markdown.
  - Input: `file path` (string)
  - Return: Markdown of the document.

- `general_information_extration`
  - Automatically and intelligently extract key information from documents.
  - Input: `file path` (string)
  - Return: The key information JSON.

## Setup

### APP_ID and APP_SECRET

Click [here](https://www.textin.com/user/login?from=github_mcp) to register for a TextIn account.

Get Textin APP_ID and APP_SECRET by following the instructions [here](https://www.textin.com/doc/guide/account/%E5%A6%82%E4%BD%95%E8%8E%B7%E5%8F%96app%20id?status=first).

### NPX

```json
{
  "mcpServers": {
    "textin-ocr": {
      "command": "npx",
      "args": [
        "-y",
        "@intsig/server-textin"
      ],
      "env": {
        "APP_ID": "",
        "APP_SECRET": "",
        "MCP_SERVER_REQUEST_TIMEOUT": "600000"
      },
      "timeout": 600
    }
  }
}
```

## License

This MCP server is licensed under the MIT License. This means you are free to use, modify, and distribute the software, subject to the terms and conditions of the MIT License. For more details, please see the LICENSE file in the project repository.

**Official site: ** [https://github.com/intsig-textin/textin-mcp](https://github.com/intsig-textin/textin-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `files`
- Tags: `image and video processing`, `file systems`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @intsig/server-textin`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/intsig-textin-textin.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
