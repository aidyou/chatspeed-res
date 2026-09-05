---
title: "undoom-pdf-mcp"
description: "A powerful PDF conversion tool MCP server, based on the Model Context Protocol (MCP), integrating multiple file conversion features. - PDF to images: convert single or batch PDFs to high-quality image…"
---

# undoom-pdf-mcp

A powerful PDF conversion tool MCP server, based on the Model Context Protocol (MCP), integrating multiple file conversion features. - PDF to images: convert single or batch PDFs to high-quality image…

# undoom-pdf-mcp

[![Python Version](/mcp-assets/405b7b46d001e379991916d79670861b.svg)](https://www.python.org/downloads/)
[![License](/mcp-assets/5816f652aa1f0cc4eedb21a2f733e09e.svg)](https://github.com/kk520879/undoom_pdf_mcp/blob/HEAD/LICENSE)
[![Version](/mcp-assets/4fde9e9f0fdf6455a8458bae4c572d76.svg)](https://github.com/kk520879/undoom_pdf_mcp)

A powerful PDF conversion tool MCP server, based on the MCP (Model Context Protocol), integrating multiple file conversion features.

## Features

- **PDF to images**: convert single or batch PDFs to high-quality images
- **Office to PDF**: convert Word, Excel, and PowerPoint files to PDF
- **PDF encryption**: add password protection to PDF files
- **Images to PDF**: merge single or multiple images into a PDF
- **PDF info**: get detailed PDF file information
- **Batch processing**: support batch file conversion
- **Memory optimization**: automatic memory management to avoid leaks

## Feature Details

### PDF to image conversion
- **Single PDF to image**: convert a PDF file to JPG images
- **Batch PDF to image**: process multiple PDF files in batch
- **Page selection**: convert specific pages only
- **Quality control**: multiple image quality settings

### Office files to PDF
- **Word to PDF**: supports .doc and .docx formats
- **Excel to PDF**: supports .xls and .xlsx formats
- **PowerPoint to PDF**: supports .ppt and .pptx formats
- **Batch conversion**: convert Office files in batch

### PDF security features
- **PDF encryption**: set password protection on PDF files
- **Permission control**: configure access permissions for PDF files

### Images to PDF
- **Single image to PDF**: convert one image into a PDF file
- **Multiple images merged into PDF**: merge several images into a single PDF
- **Page size settings**: supports A4, A3, Letter, and other page sizes

### Other features
- **PDF info viewer**: get detailed information about a PDF file
- **Memory optimization**: automatic memory cleanup to avoid leaks

## Quick Start

### Requirements

- Python 3.10+
- Windows system (required for Office file conversion)
- Microsoft Office installed (Word, Excel, PowerPoint)

### Installation

#### Method 1: Use uv (recommended)

```bash
# Clone the repository
git clone https://github.com/kk520879/undoom_pdf_mcp.git
cd undoom_pdf_mcp

# Install dependencies
uv sync
```

#### Method 2: Use pip

```bash
# Clone the repository
git clone https://github.com/kk520879/undoom_pdf_mcp.git
cd undoom_pdf_mcp

# Create a virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install -e .
```

### Starting the server

```bash
# Run with uv
uv run python undoom_pdf_mcp/main.py

# Or run directly
python undoom_pdf_mcp/main.py
```

### MCP client configuration

#### Method 1: Use uvx (recommended)

The package is published on PyPI and can be used directly via uvx:

```json
{
  "mcpServers": {
    "undoom-pdf-mcp": {
      "command": "uvx",
      "args": [
        "--index-url",
        "https://pypi.tuna.tsinghua.edu.cn/simple",
        "undoom-pdf-mcp"
      ]
    }
  }
}
```

**Note**: The config uses the Tsinghua University PyPI mirror for faster, more reliable downloads.

#### Method 2: Local development configuration

If you are running from source, use this config:

```json
{
  "mcpServers": {
    "undoom-pdf-mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/your/undoom_pdf_mcp",
        "run",
        "python",
        "undoom_pdf_mcp/main.py"
      ]
    }
  }
}
```

Add the configuration above to your MCP client config file (such as the Claude Desktop config file).

## Main Dependencies

- `mcp[cli]>=1.12.4` - MCP protocol support
- `PyMuPDF>=1.23.0` - PDF processing library
- `Pillow>=10.0.0` - image processing library
- `pywin32>=306` - Windows COM interface (needed for Office conversion)
- `tkinterdnd2>=0.3.0` - GUI drag-and-drop support

## Usage

### Starting the MCP server

```bash
python main.py
```

### Available tools

#### 1. pdf_to_images
Convert a PDF file to images

**Parameters:**
- `pdf_path` (required): absolute path to the PDF file
- `pages` (optional): pages to convert, e.g. '1,2,3-5'; leave empty for all pages
- `quality` (optional): image quality multiplier; options: 0.25, 0.5, 1.0, 2.0, 4.0; default 2.0
- `output_dir` (optional): output directory; leave empty to use the PDF's directory

**Example:**
```json
{
  "pdf_path": "C:\\Documents\\example.pdf",
  "pages": "1,3-5",
  "quality": 2.0
}
```

#### 2. batch_convert_pdfs
Convert multiple PDF files to images in batch

**Parameters:**
- `folder_path` (required): path to the folder containing the PDF files
- `page_settings` (required): mapping of file names to page settings
- `quality` (optional): image quality multiplier, default 2.0

**Example:**
```json
{
  "folder_path": "C:\\Documents\\PDFs",
  "page_settings": {
    "file1.pdf": "1,2,3-5",
    "file2.pdf": "1-10",
    "file3.pdf": ""
  },
  "quality": 2.0
}
```

#### 3. word_to_pdf
Convert a Word document to PDF

**Parameters:**
- `word_path` (required): absolute path to the Word file
- `output_path` (optional): output PDF path; leave empty to auto-generate

#### 4. excel_to_pdf
Convert an Excel document to PDF

**Parameters:**
- `excel_path` (required): absolute path to the Excel file
- `output_path` (optional): output PDF path; leave empty to auto-generate

#### 5. ppt_to_pdf
Convert a PowerPoint document to PDF

**Parameters:**
- `ppt_path` (required): absolute path to the PowerPoint file
- `output_path` (optional): output PDF path; leave empty to auto-generate

#### 6. batch_office_to_pdf
Convert Office files to PDF in batch

**Parameters:**
- `folder_path` (required): path to the folder containing the Office files
- `file_types` (optional): list of file types to convert; defaults to all Office formats

#### 7. get_pdf_info
Get PDF file information

**Parameters:**
- `pdf_path` (required): absolute path to the PDF file

#### 8. encrypt_pdf
Encrypt a PDF file

**Parameters:**
- `pdf_path` (required): absolute path to the PDF file
- `password` (required): encryption password
- `output_path` (optional): output PDF path; leave empty to auto-generate

**Example:**
```json
{
  "pdf_path": "C:\\Documents\\example.pdf",
  "password": "mypassword123",
  "output_path": "C:\\Documents\\example_encrypted.pdf"
}
```

#### 9. images_to_pdf
Merge multiple images into a PDF

**Parameters:**
- `image_paths` (required): list of image file paths
- `output_path` (required): output PDF path
- `page_size` (optional): page size, e.g. A4, A3, Letter, etc.; default A4

**Example:**
```json
{
  "image_paths": [
    "C:\\Images\\page1.jpg",
    "C:\\Images\\page2.png",
    "C:\\Images\\page3.jpg"
  ],
  "output_path": "C:\\Documents\\merged.pdf",
  "page_size": "A4"
}
```

#### 10. single_image_to_pdf
Convert a single image to PDF

**Parameters:**
- `image_path` (required): absolute path to the image file
- `output_path` (optional): output PDF path; leave empty to auto-generate
- `page_size` (optional): page size, e.g. A4, A3, Letter, etc.; default A4

**Example:**
```json
{
  "image_path": "C:\\Images\\document.jpg",
  "page_size": "A4"
}
```

## Page Number Formats

Supported page formats:
- `1` - a single page
- `1,2,3` - multiple single pages
- `1-5` - a page range
- `1,3-5,7` - mixed format
- empty - convert all pages

## Image Quality

- `0.25` - low quality (small files)
- `0.5` - medium-low quality
- `1.0` - original resolution
- `2.0` - high quality (default)
- `4.0` - ultra-high quality (large files)

## Notes

1. **Office conversion**: requires the corresponding Office software (Word, Excel, PowerPoint) installed on Windows
2. **File paths**: all paths must be absolute paths
3. **Permissions**: ensure read access to input files and write access to the output directory
4. **Memory management**: memory is automatically cleaned when processing large files

## Error Handling

The server catches and returns detailed error messages, including:
- File-not-found errors
- Permission errors
- Unsupported-format errors
- Office application errors

## Development Notes

This project is built on the MCP protocol and integrates multiple PDF and Office file processing features:

1. **PDF to images**: high-quality PDF rendering based on PyMuPDF
2. **Office to PDF**: calls Office applications via the Windows COM interface
3. **PDF encryption**: uses PyMuPDF's security features
4. **Image processing**: uses Pillow's image processing capabilities

All features are exposed through the MCP protocol and can be called by MCP-capable AI assistants or applications.

### Project structure

```
undoom_pdf_mcp/
├── undoom_pdf_mcp/
│   ├── __init__.py
│   └── main.py          # Main program file
├── pyproject.toml       # Project config
├── README.md           # Project readme
├── LICENSE             # License
└── test_converter.py   # Test file
```

## Contributing

Contributions are welcome! Follow these steps:

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Changelog

### v0.2.3 (2024-12-19)
- Fixed a coroutine error when running via uvx
- Improved async entry point handling
- Published to PyPI, supporting direct uvx installation
- Optimized the MCP server startup flow

### v0.2.2 (2024-12-19)
- Optimized MCP configuration
- Updated documentation and config examples

### v0.2.0 (2024-12-19)
- Added PDF encryption
- Added images-to-PDF conversion
- Fixed a memory leak issue
- Improved documentation and examples

### v0.1.0 (2024-12-18)
- Initial release
- PDF to images
- Office files to PDF
- Batch processing

## Contact

- Author: undoom
- Email: kaikaihuhu666@163.com
- GitHub: [@kk520879](https://github.com/kk520879)

## License

This project is licensed under the [MIT License](https://github.com/kk520879/undoom_pdf_mcp/blob/HEAD/LICENSE).

## Support the Project

If this project helps you, please give it a star!

---

**Note**: This project is mainly tested on Windows; the Office conversion feature requires Microsoft Office to be installed.

**Official site: ** [https://github.com/kk520879/undoom_pdf_mcp](https://github.com/kk520879/undoom_pdf_mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `files`
- Tags: `file systems`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `--index-url https://pypi.tuna.tsinghua.edu.cn/simple undoom-pdf-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/undoom-undoom-pdf.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
