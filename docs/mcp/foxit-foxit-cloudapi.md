---
title: "mcp-server-foxit-cloudapi"
description: "Foxit PDF Services API provides a cloud-based REST API that allows processing of PDF files via HTTP clients. It offers rich features suitable for integration into various applications. 📌 Key Features…"
---

# mcp-server-foxit-cloudapi

Foxit PDF Services API provides a cloud-based REST API that allows processing of PDF files via HTTP clients. It offers rich features suitable for integration into various applications. 📌 Key Features…

# MCP server for using the Foxit Cloud API

## Requirements
- Node.js >= 18.0.0

## Features
- PDF Creation and Conversion: Supports creating PDF files from other file formats and converting PDFs to other formats such as HTML, Word, etc.
- PDF Merging and Splitting: Supports merging multiple PDF files into one or splitting a PDF file into multiple files.
- PDF Compression and Optimization: Reduces PDF file size through image compression and optimization, flattening, linearization, and other functions.
- PDF Security: Provides password protection and advanced encryption features to ensure the security of PDF files.

## Tools

### combine_pdf

Merge multiple PDF documents from compressed or archived files into one PDF document. Example 1: Merge PDF documents from 
 into one PDF. Example 2: Merge ,  into one PDF.

Parameters:
  - path: string - Absolute path of the compressed or archived file or multiple URL addresses
  - config: object - Configuration options
    - isAddBookmark: boolean - Whether to add bookmarks
    - isAddTOC: boolean - Whether to add a table of contents
    - isContinueMerge: boolean - Whether to continue merging if an error occurs
    - isRetainPageNum: boolean - Whether to retain logical page numbers
    - bookmarkLevels: enum('0', '1', '2', '3', '4', '5') - Level of table of contents display

### compare_pdf

Compare one PDF document (as the "base document") with another PDF document (as the "comparison document") page by page. Example 1: Compare 
 with 
. Example 2: Compare 
 with 
, result type: pdf. Example 3: Compare  with .

Parameters:
  - basePath: string - Absolute path or URL address of the base PDF document
  - comparePath: string - Absolute path or URL address of the comparison PDF document
  - resultType: enum('json', 'pdf') - Result type
  - compareType: enum('all', 'text') - Comparison type

### compress_pdf

Compress PDF documents using the specified compression level. Example 1: Compress 
. Example 2: Compress 
, compression level: high. Example 3: Compress .

Parameters:
  - path: string - Absolute path or URL address of the PDF document
  - compressionLevel: enum('low', 'medium', 'high') - Compression level

### convert_pdf

Convert PDF documents to other formats, supported formats: word, excel, ppt, image, text, html. Example 1: Convert 
 to word. Example 2: Convert 
 to text. Example 3: Convert  to excel.

Parameters:
  - path: string - Absolute path or URL address of the PDF document
  - format: enum('word', 'excel', 'ppt', 'image', 'text', 'html') - Converted file type

### create_pdf

Create or convert to PDF documents from other formats, supported formats: word, excel, ppt, image, text. Example 1: Convert 
 to PDF. Example 2: Convert 
 to PDF. Example 3: Convert  to PDF.

Parameters:
  - path: string - Absolute path or URL address of the file to be converted
  - format: enum('word', 'excel', 'ppt', 'image', 'text') - Input file type

### create_pdf_from_html

Create PDF from HTML files or specified site URLs. Example 1: Convert 
 to PDF. Example 2: Convert  to PDF. Example 3: Convert  to PDF, page mode: single page. Example 4：Convert  to PDF, input format: html.

Parameters:
  - format: enum('url', 'html', 'htm', 'shtml') - Input format, if url, the url parameter cannot be empty, otherwise the path parameter cannot be empty
  - path: string - Absolute path or URL address of the HTML file
  - url: string - URL
  - config: object - Configuration options
    - width: number - Page width, must be greater than 16, default value is 900 (unit is 1/72 inch)
    - height: number - Page height, must be greater than 16, default value is 600 (unit is 1/72 inch)
    - rotate: number - Page rotation, 0: 0 degrees, 1: 90 degrees, 2: 180 degrees, 3: 270 degrees
    - pageMode: number - Page mode, 0: single page, 1: multiple pages
    - pageScaling: number - Page scaling, 1: fit to page, 2: fit to content

### extract_pdf

Extract text or images from PDF documents. Example 1: Extract text from 
. Example 2: Extract images from 
. Example 3: Extract text from .

Parameters:
  - path: string - Absolute path or URL address of the PDF document
  - mode: enum('extractImages', 'extractText') - Extraction mode, extractText means extracting text, extractImages means extracting images
  - pageRange: string - Page range for extraction, separated by commas for A, B, and C. A, B, or C can be a number, such as 99, or a range, such as 1-30. If empty, the entire document is extracted

### flatten_pdf

Flatten PDF document pages, making annotations and form fields part of the page content. Example 1: Flatten 
. Example 2: Flatten .

Parameters:
  - path: string - Absolute path or URL address of the PDF document
  - pageRange: string - Page range of the PDF document. Pages in the document can be referenced in any order, from start or end. For example: 1, 2, 3, 7-9, all. If not specified, all pages are executed

### linearize_pdf

Linearize PDF documents. Example 1: Linearize 
. Example 2: Linearize .

Parameters:
  - path: string - Absolute path or URL address of the PDF document

### manipulation_pdf

Manipulate PDF documents, such as deleting pages, rotating pages, moving pages. Example 1: Delete page 1 of 
. Example 2: Move page 2 of 
 to page 1. Example 3: Delete page 1 of .

Parameters:
  - path: string - Absolute path or URL address of the PDF document
  - config: object - PDF document operation configuration
    - pageAction: enum('delete', 'rotate', 'move') - Page operation type
    - pages: array(number) - Page numbers to operate on, such as [0,1,2,3], page index starts from 0
    - angle: number - Page rotation, 0: 0 degrees, 1: 90 degrees, 2: 180 degrees, -1: 270 degrees
    - destination: number - Destination page number, required if "page operation type" is "move"

### protect_pdf

Protect PDF documents with user and/or owner passwords and set restrictions on certain functions. Example 1: Set user password for 
, password: 123456. Example 2: Set owner password for 
, password: 123456, permission settings: do not allow modification of PDF content. Example 3: Set user password for , password: 123456.

Parameters:
  - path: string - Absolute path or URL address of the PDF document
  - passwordProtection: object - Password protection settings, at least one password must be set
    - userPassword: string - User password
    - ownerPassword: string - Owner password
  - permission: object - Permission settings
    - PRINT_LOW_QUALITY: boolean - Print PDF document in normal mode
    - PRINT_HIGH_QUALITY: boolean - Print PDF document in high quality
    - EDIT_CONTENT: boolean - Modify PDF content. If set, users can modify the content of the PDF document through operations
    - EDIT_FILL_AND_SIGN_FORM_FIELDS: boolean - Fill PDF forms. If set, users can fill interactive form fields (including signature fields)
    - EDIT_ANNOTATION: boolean - Operate text annotations and fill interactive form fields. If "modify PDF content" is also set, users can create or modify interactive form fields
    - EDIT_DOCUMENT_ASSEMBLY: boolean - Assemble PDF documents. If set, documents can be assembled (insert, rotate or delete pages and create bookmarks or thumbnails), regardless of whether "modify PDF content" is set
    - COPY_CONTENT: boolean - Support for disabilities. If set, users can extract text and graphics to support accessibility for disabled users or for other purposes
  - encryptionAlgorithm: enum('AES_128', 'AES_256', 'RC4') - Encryption algorithm

### remove_password

Remove password security from PDF documents. Example 1: Remove user password from 
, password: 123456. Example 2: Remove owner password from 
, password: 123456. Example 3: Remove user password from , password: 123456.

Parameters:
  - path: string - Absolute path or URL address of the PDF document
  - password: string - PDF document password. If the PDF is protected by an owner password, the user needs to use the owner password in this field to remove document security, otherwise the user needs to pass in the user password to open the document

### split_pdf

Split PDF documents into multiple smaller documents. Example 1: Split 
 into multiple documents, number of pages after splitting: 3. Example 2: Split  into multiple documents, number of pages after splitting: 2.

Parameters:
  - path: string - Absolute path or URL address of the PDF document
  - config: object - Configuration options
    - pageCount: number - Number of pages after splitting

## Using in VS Code's GitHub Copilot

Open the VS Code configuration file `settings.json`, add the following configuration, and replace `your_client_id`:

- Windows, MacOS, Linux

```json
{
  "mcp": {
    "servers": {
      // Other configurations ...
      "mcp-server-foxit-cloudapi": {
        "command": "npx",
        "args": [
          "-y",
          "@foxitsoftware/mcp-server-foxit-cloudapi"
        ],
        "env": {
          "CLIENT_ID": "your_client_id"
        }
      }
      // Other configurations ...
    }
  }
}
```

**Official site: ** [https://github.com/deckflow/gezhe-ppt-mcp](https://github.com/deckflow/gezhe-ppt-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `communication`, `media`
- Tags: `developer tools`, `communication`, `entertainment and media`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @foxitsoftware/mcp-server-foxit-cloudapi`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/foxit-foxit-cloudapi.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
