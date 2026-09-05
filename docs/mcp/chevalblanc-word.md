---
title: "MCP-word"
description: "DOCX MCP Service A powerful Word document processing MCP service providing a complete document processing solution including document structure extraction, content modification, and cloud storage inte…"
---

# MCP-word

DOCX MCP Service A powerful Word document processing MCP service providing a complete document processing solution including document structure extraction, content modification, and cloud storage inte…

# DOCX MCP Service

A powerful Word document processing MCP service providing a complete document processing solution including document structure extraction, content modification, and cloud storage integration. Supports downloading documents from URLs, batch content modification, and automatic upload to Alibaba Cloud OSS. Fully compatible with the MCP protocol and seamlessly integrable into various AI assistants.

## Service Features

- **Document structure extraction**: intelligently parses .docx files, extracting structured content such as paragraphs and tables, and assigns a unique ID to each element
- **Batch content modification**: precise text replacement and content updates based on element IDs
- **Cloud storage integration**: automatically uploads modified documents to Alibaba Cloud OSS and provides convenient download links
- **URL document processing**: downloads, processes, and re-uploads documents directly from a web URL
- **MCP standard compliance**: fully conforms to the Model Context Protocol specification, supporting standard MCP clients

## System Requirements

- Python 3.13+
- uvx (Python package manager, recommended)

## Service Configuration

### Server config

```json
{
  "command": "uvx",
  "args": ["docx-mcp"]
}
```

## Available Tools

### 1. extract_document_structure
Downloads a .docx file from a URL and parses its structure

**Parameters:**
- `document_url` (string): URL of the .docx file

**Returns:** a dict containing the document structure, with a unique ID for each element

### 2. apply_modifications_to_document
Applies modifications to a .docx file

**Parameters:**
- `original_file_content_base64` (string): Base64 encoding of the original file
- `patches_json` (string): list of modification instructions in JSON format

**Returns:** Base64 encoding of the modified file

### 3. get_modified_document
Gets the modified document (alias of apply_modifications_to_document)

**Parameters:** same as apply_modifications_to_document

### 4. prepare_document_for_download
Uploads the modified document to Alibaba Cloud OSS

**Parameters:**
- `original_file_content_base64` (string): Base64 encoding of the original file
- `patches_json` (string): modification instructions in JSON format

**Returns:** a dict containing the upload result and download link

### 5. process_document_from_url
Complete flow: download the document from a URL, apply modifications, and upload to OSS

**Parameters:**
- `document_url` (string): URL of the original document
- `patches_json` (string): modification instructions in JSON format

**Returns:** a dict containing the processing result and download link

## Usage Examples

### Modification instruction format

```json
[
  {
    "element_id": "p_0",
    "new_content": "New paragraph content"
  },
  {
    "element_id": "table_0_cell_0_0",
    "new_content": "New table cell content"
  }
]
```

### Typical workflow

1. **Extract document structure**: use `extract_document_structure` to get the IDs of all elements in the document
2. **Prepare modification instructions**: create the modification JSON based on the element IDs
3. **Process the document**: use `process_document_from_url` to download, modify, and upload in one step
4. **Get the result**: obtain the processed document from the returned download link

## Quick Start

### Run via uvx (recommended)

```bash
# Run directly (published to PyPI)
uvx docx-mcp

# Run from a local project
uvx --from . docx-mcp
```

### Configure in an MCP client

Add the following config to an MCP-capable client:

```json
{
  "mcpServers": {
       "docx_filler_service": {
      "command": "cmd",
      "args": [
        "/c",
        "uvx",
        "docx-mcp"
      ]
    }
  }
}
```

## Deployment Advantages

- **Zero-config deployment**: no environment variables needed, works out of the box
- **One-click install**: runs directly via uvx, dependencies handled automatically
- **Built-in configuration**: OSS storage config is built in, simplifying deployment
- **Ready immediately**: can process documents right after installation

## Project Structure

```
docx_mcp/
├── core/                    # Core functionality modules
│   ├── docx_processor.py   # Document processor
│   └── models.py           # Data model definitions
├── main.py                 # MCP service main entry
├── pyproject.toml         # Project config and dependencies
├── requirements.txt       # Dependency list
├── LICENSE               # MIT license
└── README.md             # Project docs
```

## Tech Stack

- **MCP framework**: FastMCP - high-performance MCP service framework
- **Document processing**: python-docx - Office document library
- **Cloud storage**: Alibaba Cloud OSS Python SDK
- **Package management**: uvx/uv - modern Python package management

## Performance Features

- **Memory efficient**: streams large documents to avoid out-of-memory issues
- **Concurrency safe**: supports multiple clients accessing simultaneously
- **Error recovery**: complete exception handling and recovery mechanisms
- **Format compatibility**: supports .docx format (Office 2007+)
- **Zero configuration**: built-in cloud storage config, no extra setup

## Contribution Guide

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source under the MIT License - see the [LICENSE](https://github.com/taurusduan/Docx_MCP_cj/blob/HEAD/LICENSE) file for details.

## Related Links

- [MCP official docs](https://modelcontextprotocol.io/)
- [FastMCP framework](https://github.com/pydantic/fastmcp)
- [python-docx docs](https://python-docx.readthedocs.io/)
- [Alibaba Cloud OSS Python SDK](https://help.aliyun.com/document_detail/32026.html)

## FAQ

**Q: Do I need to configure any environment variables?**
A: No! The OSS configuration is built into the service; it works out of the box.

**Q: Which document formats are supported?**
A: Currently only .docx format (Office 2007+ format).

**Q: Is there a document size limit?**
A: We recommend keeping a single document under 50MB for best performance.

**Q: How do I get started?**
A: Just run `uvx docx-mcp` to start the service; no configuration needed.

**Q: Where are documents stored?**
A: Processed documents are automatically uploaded to the preconfigured Alibaba Cloud OSS storage, with a download link provided.

---

**Tip**: If you have questions or suggestions, feel free to submit an Issue or Pull Request!

**Official site: ** [https://github.com/taurusduan/Docx_MCP_cj](https://github.com/taurusduan/Docx_MCP_cj)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `productivity`
- Tags: `other`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `docx-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/chevalblanc-word.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
