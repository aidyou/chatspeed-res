---
title: "Docx_MCP"
description: "A powerful Word document processing MCP service that provides a complete document processing solution, including document structure extraction, content modification, and cloud storage integration. It…"
---

# Docx_MCP

A powerful Word document processing MCP service that provides a complete document processing solution, including document structure extraction, content modification, and cloud storage integration. It…

# 📚 DOCX MCP Complete User Guide

## 🌟 Project Overview

**DOCX MCP** is a powerful Word document processing tool based on the MCP (Model Context Protocol) protocol, providing 42 professional document processing tools that support advanced features such as intelligent table analysis, automated filling, and document generation.

### Core Features

- 🎯 **42 MCP Tools**: Covering comprehensive functions including document management, table processing, and image editing
- 🤖 **AI Friendly**: Perfectly compatible with AI assistants like Claude and ChatGPT
- 📊 **Intelligent Tables**: Automatically recognize table structures and intelligently fill data
- 🎨 **Rich Formatting**: Support for fine-grained control over text, images, and tables
- 🚀 **High Performance**: Based on the FastMCP framework for quick response
- 🔧 **Easy Integration**: Standard MCP protocol for easy integration into various applications

---

## 📦 Quick Installation

### Method 1: Using pip (Recommended)

bash
pip install docx-mcp

### Method 2: Using uv (Faster)

bash
uv pip install docx-mcp

### Method 3: Using uvx (Temporary Run)

bash
uvx docx-mcp

### Verify Installation

bash
# Check version
pip show docx-mcp

# Test command
docx-mcp --help

---

## 🚀 Quick Start

### 1. Running as an MCP Server

bash
# Start the MCP server
docx-mcp

# Or use uvx (no installation required)
uvx docx-mcp

After the server starts, it will display:
plaintext
Starting the final complete MCP server...
Function modules:
- 📊 Tool Categories (42)
- 📁 Document Management Tools (8)
- ✍️ Text Content Tools (5)
- 📊 Table Operation Tools (6)
- 🔍 Table Analysis Tools (5)
- 📝 Table Filling Tools (4)
- 🖼️ Image Processing Tools (3)
- 📐 Page Setup Tools (3)
- 🧠 Intelligent Function Tools (5)
- ⚙️ System Status Tools (3)
...
Total: 42 tools

### 2. Configuring Claude Desktop

Edit `claude_desktop_config.json`:

json
{
  "mcpServers": {
    "docx-mcp": {
      "command": "uvx",
      "args": ["docx-mcp"]
    }
  }
}

**Configuration File Location**:
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

---

## 🛠️ Full List of 42 Tools

### 📁 Document Management Tools (8)

#### 1. `create_document`
Create a new Word document

**Parameters**:
- `file_path` (required): Path to save the document

**Example**:
python
create_document("report.docx")

#### 2. `open_document`
Open an existing document

**Parameters**:
- `file_path` (required): Path to the document

#### 3. `save_document`
Save the current document

#### 4. `save_as_document`
Save as a new document

**Parameters**:
- `new_file_path` (required): Path to the new document

#### 5. `close_document`
Close the current document

#### 6. `get_document_info`
Get document information (number of paragraphs, number of tables, etc.)

#### 7. `copy_document`
Copy the document to a new location

**Parameters**:
- `source_path` (required): Source file path
- `target_path` (required): Target path

#### 8. `create_work_copy`
Create a working copy of the document

**Parameters**:
- `file_path` (required): Original file path
- `suffix` (optional): Suffix, default is "_工作版"

---

### ✍️ Text Content Tools (5)

#### 9. `add_paragraph`
Add a paragraph

**Parameters**:
- `text` (required): Paragraph text
- `bold` (optional): Whether to bold
- `italic` (optional): Whether to italicize
- `underline` (optional): Whether to underline
- `font_size` (optional): Font size
- `font_name` (optional): Font name
- `color` (optional): Color (hexadecimal)
- `alignment` (optional): Alignment

**Example**:
python
add_paragraph(
    text="This is important content",
    bold=True,
    font_size=14,
    color="#FF0000",
    alignment="center"
)

#### 10. `add_heading`
Add a heading

**Parameters**:
- `text` (required): Heading text
- `level` (optional): Heading level (1-9)

#### 11. `add_text_with_formatting`
Add precisely formatted text

#### 12. `search_and_replace`
Search and replace text

**Parameters**:- `search_text` (required): Search text
- `replace_text` (required): Replacement text
- `case_sensitive` (optional): Whether to be case sensitive

#### 13. `smart_add_content`
Intelligently add content (automatically recognize type)

**Parameters**:
- `content` (required): Content
- `content_type` (optional): Type (paragraph/heading/list)
- `style` (optional): Style (normal/emphasis/quote)
- `auto_format` (optional): Auto format

---

### 📊 Table Operation Tools (6)

#### 14. `add_table`
Add a table

**Parameters**:
- `rows` (required): Number of rows
- `cols` (required): Number of columns
- `data` (optional): Table data (2D array)
- `has_header` (optional): Whether it has a header

**Example**:
python
add_table(
    rows=3,
    cols=3,
    data=[
        ["Name", "Age", "Occupation"],
        ["Zhang San", "25", "Engineer"],
        ["Li Si", "30", "Designer"]
    ],
    has_header=True
)

#### 15. `add_table_row`
Add a table row

**Parameters**:
- `table_index` (required): Table index
- `row_data` (required): Row data array

#### 16. `add_table_column`
Add a table column

**Parameters**:
- `table_index` (required): Table index
- `column_index` (optional): Insertion position
- `data` (optional): Column data

#### 17. `format_table`
Format a table

**Parameters**:
- `table_index` (required): Table index
- `style` (optional): Table style

#### 18. `merge_table_cells`
Merge table cells

**Parameters**:
- `table_index` (required): Table index
- `row_start` (required): Start row
- `col_start` (required): Start column
- `row_end` (required): End row
- `col_end` (required): End column

#### 19. `intelligent_create_table`
Intelligently create a table (automatic styling)

**Parameters**:
- `data` (required): Table data (2D array)
- `auto_style` (optional): Automatically apply style

---

### 🔍 Table Analysis Tools (5)

#### 20. `extract_table_structure`
Extract table structure (full analysis)

**Parameters**:
- `file_path` (required): Document path
- `table_index` (required): Table index

**Returns**: Detailed table structure in JSON format

**Example**:
python
structure = extract_table_structure("report.docx", 0)
# Returns: number of rows and columns, cell contents, merge information, etc.

#### 21. `extract_all_tables_structure`
Extract all table structures

**Parameters**:
- `file_path` (required): Document path

#### 22. `extract_document_structure`
Extract full document structure

**Parameters**:
- `file_path` (required): Document path
- `include_cell_details` (optional): Whether to include cell details

#### 23. `get_table_structure_cache_info`
Get table structure cache information

#### 24. `clear_table_structure_cache`
Clear table structure cache

---

### 📝 Table Filling Tools (4)

#### 25. `extract_fillable_fields`
Extract fillable fields (coordinate-specific)

**Parameters**:
- `file_path` (required): Document path

**Returns**: Field coordinate mapping, empty space information, filling suggestions

**Example**:
python
fields = extract_fillable_fields("template.docx")
# Returns: {"field_coordinates": {"Name": [0, 1, 2]}, ...}

#### 26. `fill_with_coordinates`
Fill using coordinates (main function)

**Parameters**:
- `file_path` (required): Document path
- `coordinate_data` (required): Coordinate data dictionary

**Example**:
python
fill_with_coordinates(
    "template.docx",
    {
        "Zhang San": [0, 1, 2],  # [table index, row, column]
        "2023001": [0, 2, 2],
        "School of Computer Science": [0, 3, 2]
    }
)

#### 27. `basic_table_fill`
Basic table filling (smart matching)

**Parameters**:
- `file_path` (required): Document path
- `fill_data` (required): Fill data dictionary

**Example**:
python
basic_table_fill(
    "template.docx",
    {
        "Name": "Zhang San",
        "Student ID": "2023001",
        "School": "School of Computer Science",
        "Major": "Computer Science and Technology"
    }
)

#### 28. `intelligent_table_fill`
Intelligent table filling (auxiliary function)

---

### 🖼️ Image Processing Tools (3)

#### 29. `add_image`
Add an image

**Parameters**:- `image_path` (required): Image path
- `width` (optional): Width (in inches)
- `height` (optional): Height (in inches)

**Example**:
python
add_image("logo.png", width=3, height=2)

#### 30. `extract_images`
Extracts all images from the document

**Parameters**:
- `output_dir` (optional): Output directory

#### 31. `resize_image`
Resizes an image

**Parameters**:
- `image_index` (required): Image index
- `width` (required): New width
- `height` (required): New height

---

### 📐 Page Setup Tools (3)

#### 32. `set_page_margins`
Sets page margins

**Parameters**:
- `top` (optional): Top margin (in inches)
- `bottom` (optional): Bottom margin
- `left` (optional): Left margin
- `right` (optional): Right margin

**Example**:
python
set_page_margins(top=1, bottom=1, left=1.5, right=1.5)

#### 33. `set_page_orientation`
Sets page orientation

**Parameters**:
- `orientation` (optional): portrait (portrait) or landscape (landscape)

#### 34. `set_page_size`
Sets page size

**Parameters**:
- `width` (optional): Width (in inches)
- `height` (optional): Height (in inches)

---

### 🧠 Intelligent Function Tools (5)

#### 35. `intelligent_create_document`
Intelligently creates a document (with template)

**Parameters**:
- `file_path` (required): Document path
- `template_type` (optional): Template type
  - `basic`: Basic document
  - `business`: Business document
  - `academic`: Academic paper
- `auto_optimize` (optional): Automatically optimize pages

**Example**:
python
intelligent_create_document(
    "report.docx",
    template_type="business",
    auto_optimize=True
)

#### 36. `get_smart_suggestions`
Gets smart suggestions

**Parameters**:
- `context` (optional): Context type
  - `document_editing`: Document editing
  - `table_creation`: Table creation
  - `content_formatting`: Content formatting
  - `structure_optimization`: Structure optimization
  - `professional_polish`: Professional polish

#### 37. `get_intelligent_planning_guide`
Gets intelligent planning guide

**Returns**: A complete guide for using MCP tools with AI

#### 38. `create_intelligent_workflow_plan`
Creates an intelligent workflow plan

**Parameters**:
- `user_request` (required): User request description

**Returns**: A detailed tool call plan

#### 39. `get_tool_detailed_guidance`
Gets detailed guidance for a tool

**Parameters**:
- `tool_name` (required): Tool name

---

### ⚙️ System Status Tools (3)

#### 40. `get_system_status`
Gets system status

**Returns**: Current document status, list of available tools, etc.

#### 41. `test_connection`
Tests connection

**Returns**: Connection status confirmation

#### 42. `get_server_info`
Gets server information

**Returns**: Server version, feature list, etc.

---

## 💡 Usage Scenario Examples

### Scenario 1: Batch Report Generation

python
from final_complete_server import *

# 1. Create document
intelligent_create_document("report.docx", "business", True)

# 2. Add heading
add_heading("Monthly Work Report", level=1)

# 3. Add table
intelligent_create_table([
    ["Project Name", "Completion Rate", "Notes"],
    ["Project A", "100%", "Completed"],
    ["Project B", "80%", "In Progress"]
])

# 4. Save
save_document()

### Scenario 2: Intelligent Form Filling

python
from core.universal_table_filler import UniversalTableFiller

filler = UniversalTableFiller()

# 1. Analyze table structure
coordinates = filler.analyze_and_get_coordinates("template.docx")

# 2. Prepare data
data = {
    "Name": "Zhang San",
    "Student ID": "2023001",
    "College": "School of Computer Science",
    "Major": "Computer Science and Technology",
    "Contact": "13800138000"
}

# 3. Intelligent fill
fill_with_coordinates("template.docx", {
    "Zhang San": [0, 1, 2],
    "2023001": [0, 2, 2],
    "School of Computer Science": [0, 3, 2],
    "Computer Science and Technology": [0, 4, 2],
    "13800138000": [0, 5, 2]
})

### Scenario 3: Batch Document Processing

python
import os
from pathlib import Path

# Batch process all documents in a folder
folder = Path("documents")
for doc in folder.glob("*.docx"):
    # Open document
    open_document(str(doc))
    
    # Add page number
    add_paragraph(f"Page `{{PAGE}}`", alignment="center")
    
    # Set uniform margins
    set_page_margins(1, 1, 1, 1)
    
    # Save
    save_document()
    close_document()---

## 🎯 Advanced Features

### 1. Table Structure Analysis

python
from core.table_structure_extractor import table_extractor

# Extract table structure
structure = table_extractor.extract_table_structure("document.docx", 0)

# Get table information
print(f"Number of rows: {structure.rows}")
print(f"Number of columns: {structure.columns}")
print(f"Table type: {structure.table_type}")
print(f"Page format: {structure.page_format}")

# Traverse cells
for row in structure.cells:
    for cell in row:
        print(f"({cell.row_index}, {cell.col_index}): {cell.text}")


### 2. Intelligent Workflow Planning

python
from core.intelligent_tool_planner import intelligent_planner

# Get tool planning
plan = intelligent_planner.create_intelligent_plan(
    "Create a student information table, including name, student ID, and class, and fill with example data"
)

# Execute according to the plan
for step in plan.workflow_steps:
    print(f"Step {step.step_id}: {step.description}")
    print(f"Tool: {step.tool_name}")
    print(f"Parameters: {step.parameters}")


### 3. Custom Templates

python
# Create a custom business template
intelligent_create_document("template.docx", "business")

# Add company information
add_paragraph("ABC Company", bold=True, font_size=16, alignment="center")
add_paragraph("Address: No. XX, XX Road, XX City")
add_paragraph("Phone: 021-12345678")

# Add table framework
add_table(10, 3, has_header=True)

# Save as template
save_as_document("custom_template.docx")


---

## 🔧 Configuration and Optimization

### Environment Variable Configuration

bash
# Set cache directory
export UV_CACHE_DIR=/path/to/cache

# Disable progress bar
export UV_NO_PROGRESS=1

# Use domestic mirror
export UV_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple


### Performance Optimization Suggestions

1. **Use Cache**: Table structures are automatically cached, improving the speed of repeated operations.
2. **Batch Operations**: Try to complete multiple operations at once after opening the document.
3. **Reasonable Tool Usage**: Choose the appropriate tool based on your needs (e.g., basic vs. intelligent).

---

## 🐛 Frequently Asked Questions

### Q1: What to do if installation fails?

bash
# Method 1: Use domestic mirror
pip install docx-mcp -i https://pypi.tuna.tsinghua.edu.cn/simple

# Method 2: Upgrade pip
python -m pip install --upgrade pip
pip install docx-mcp

# Method 3: Use uv (faster)
curl -LsSf https://astral.sh/uv/install.sh | sh
uv pip install docx-mcp


### Q2: Module import failure?

python
# Ensure correct import method
from final_complete_server import mcp  # ✅ Correct
# from docx_mcp import mcp  # ❌ Incorrect


### Q3: Inaccurate table filling?

python
# Recommended to use coordinate-based filling
# 1. Analyze structure first
fields = extract_fillable_fields("template.docx")

# 2. Fill based on returned coordinate information
fill_with_coordinates("template.docx", coordinate_data)


### Q4: How to debug?

python
# Enable detailed logging
import logging
logging.basicConfig(level=logging.DEBUG)

# View tool list
status = get_system_status()
print(status)


---

## 📝 API Reference

### Python API

python
# Import method
from final_complete_server import mcp
from core.universal_table_filler import UniversalTableFiller
from core.intelligent_table_analyzer import IntelligentTableAnalyzer
from core.table_structure_extractor import table_extractor


### MCP Protocol API

When running as an MCP server, call tools via the standard MCP protocol:

json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": {
    "name": "create_document",
    "arguments": {
      "file_path": "example.docx"
    }
  }
}


---

## 🔗 Related Links

- **PyPI**: https://pypi.org/project/docx-mcp/
- **GitHub**: https://github.com/rockcj/Docx_MCP_cj
- **Issue Feedback**: https://github.com/rockcj/Docx_MCP_cj/issues
- **MCP Protocol**: https://modelcontextprotocol.io/
- **FastMCP**: https://gofastmcp.com

---

## 📄 License

MIT License

---

## 🙏 AcknowledgmentsThank you to all contributors and users for your support!

---

**Version**: 0.1.6  
**Update Date**: 2025-10-02  
**Author**: DOCX MCP Team

---

## 📞 Getting Help

If you encounter any issues or need assistance:

1. Check the FAQ section of this document
2. Visit the GitHub Issues page
3. Review the example code
4. Contact the maintenance team

Happy Documenting! 📝✨

**Official site: ** [https://github.com/rockcj/Docx_MCP_cj.git](https://github.com/rockcj/Docx_MCP_cj.git)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `files`
- Tags: `file systems`, `ai智能化处理docx文档助手`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `docx-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/rockcj-docx.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
