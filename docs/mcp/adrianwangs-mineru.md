---
title: "MinerU"
description: "MinerU MCP Service 1. Overview MinerU MCP is a powerful document parsing service specifically designed to convert online documents into high-quality Markdown format. Our service supports multiple docu…"
---

# MinerU

MinerU MCP Service 1. Overview MinerU MCP is a powerful document parsing service specifically designed to convert online documents into high-quality Markdown format. Our service supports multiple docu…

# MinerU MCP Service

## 1. Overview

**MinerU MCP** is a powerful document parsing service specifically designed to convert online documents into high-quality Markdown format. Our service supports multiple document formats, including PDF, Word, PowerPoint, and various image formats.

## 2. Core Features

* **Multi-Format Support**: Supports PDF, DOC/DOCX, PPT/PPTX, as well as JPG/JPEG/PNG image formats
* **Batch Processing**: Supports processing multiple document URLs simultaneously (by providing a list of URLs separated by spaces, commas, or newlines)
* **OCR Recognition**: Optional OCR functionality to process text in scanned documents and images
* **Multilingual Support**: Supports recognition of documents in Chinese, English, and other languages
* **Intelligent Parsing**: Maintains the original format and structure of the document, generating high-quality Markdown content
* **Page Range Selection**: Supports specifying particular pages for conversion, improving processing efficiency

## 3. API Key Acquisition

To use the MinerU API, visit the [MinerU official website](https://mineru.net) to register an account and apply for an API key.

## 4. Usage

We provide the following API functionalities:

### 4.1 Document Parsing (parse_documents)

Converts online document URLs into Markdown format.

**Parameter Description:**

| Parameter          | Type    | Description                                                                 | Default Value |
| ------------------ | ------- | -------------------------------------------------------------------------- | ------------- |
| `file_sources`     | String  | Document URL, multiple URLs can be separated by commas or newlines (supports pdf, ppt, pptx, doc, docx, and image formats jpg, jpeg, png) | -             |
| `enable_ocr`       | Boolean | Whether to enable OCR functionality                                        | `false`       |
| `language`         | String  | Document language, default "ch" for Chinese, options include "en" for English, etc. | `ch`          |
| `page_ranges`      | String (optional) | Specifies page ranges, formatted as a comma-separated string. For example: "2,4-6" means select page 2, pages 4 to 6; "2--2" means select from page 2 to the second-to-last page. | `None`        |

### 4.2 Get OCR Language List (get_ocr_languages)

Retrieves the list of supported OCR recognition languages, no parameters required.

## 5. Supported Document Formats

- **PDF Documents**: .pdf
- **Word Documents**: .doc, .docx  
- **PowerPoint Presentations**: .ppt, .pptx
- **Image Files**: .jpg, .jpeg, .png

## 6. Local Deployment Options

### 6.1 Local API Deployment

If you need to deploy a local API for document parsing (suitable for scenarios with high data privacy requirements or offline use), please refer to the project's **[README](https://github.com/opendatalab/MinerU/blob/master/projects/mcp/README.md)** for detailed local deployment instructions.

### 6.2 Local File Parsing

Our online API service **does not support local file parsing** and can only handle publicly accessible online document URLs.

If you need to process local files, consider the following solutions:
- **Local MCP Deployment**: Deploy the MCP server locally. For detailed configuration, see the project's **[README](https://github.com/opendatalab/MinerU/blob/master/projects/mcp/README.md)**.
- **File Upload**: Upload local files to a publicly accessible cloud storage service (such as cloud drives, object storage, etc.), and then use their public links for parsing.

## 7. Frequently Asked Questions

### 7.1 API Key Issues

**Issue**: Unable to connect to the MinerU API or receiving a 401 error.

**Solution**: Please check if your API key is correct. Ensure that you have obtained a valid API key from the [MinerU official website](https://mineru.net).

### 7.2 URL Access Issues

**Issue**: Receiving an error about being unable to access the URL when processing online documents.

**Solution**: Ensure that the provided URL is a publicly accessible and valid link. Our servers need to be able to download these documents.

### 7.3 Timeout on Large Files

**Issue**: Encountering a timeout when processing large documents.

**Solution**: It is recommended to split large documents into smaller parts for processing, or use the page range parameter to process only the specific pages needed.

### 7.4 Handling Local Files

**Issue**: How to handle local files?

**Solution**: Our online API does not support direct processing of local files. You can:
- Upload the files to a cloud storage service to obtain a public link and then use it.- Refer to the README document to deploy a local MCP server for local file processing

**Official site: ** [https://github.com/opendatalab/MinerU/tree/master/projects/mcp](https://github.com/opendatalab/MinerU/tree/master/projects/mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`, `memory`, `files`
- Tags: `file systems`, `developer tools`, `knowledge and memory`, `pdf、图片、word、ppt`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `mineru-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/adrianwangs-mineru.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
