---
title: "office-editor-mcp"
description: "Office Document Processing MCP Server EN CN MCP Server Python License An MCP (Model Context Protocol) server for Office document processing, enabling creation and editing of Word, Excel, and PowerPoin…"
---

# office-editor-mcp

Office Document Processing MCP Server EN CN MCP Server Python License An MCP (Model Context Protocol) server for Office document processing, enabling creation and editing of Word, Excel, and PowerPoin…

Office Document Processing MCP Server
EN CN

MCP Server Python License

An MCP (Model Context Protocol) server for Office document processing, enabling creation and editing of Word, Excel, and PowerPoint documents within MCP Clients without leaving the AI assistant environment.

Overview
Office-Editor-MCP implements the Model Context Protocol standard to expose Office document operations as tools and resources. It serves as a bridge between AI assistants and Microsoft Office documents, allowing you to create, edit, format, and analyze various Office documents through AI assistants.

Features
Word Document Operations
Document Management
Create new Word documents with metadata (title, author, etc.)
Extract text content and analyze document structure
View document properties and statistics
List available documents in a directory
Create document copies
Content Creation
Add headings with different levels
Insert paragraphs with optional styling
Create tables with custom data
Add images with proportional scaling
Insert page breaks
Text Formatting
Format specific text sections (bold, italic, underline)
Change text color and font properties
Apply custom styles to text elements
Search and replace text throughout documents
Excel Operations
Workbook Management
Create new Excel workbooks
Open existing Excel files
Add/delete/rename worksheets
Data Processing
Read and write cell contents
Insert/delete rows and columns
Sort and filter data
Apply formulas and functions
PowerPoint Operations
Presentation Management
Create new PowerPoint presentations
Add/delete/rearrange slides
Set slide themes and backgrounds
Content Editing
Add text and graphic elements
Insert tables and charts
Add animations and transitions
Advanced Features
OCR recognition (extract text from images)
Document comparison (compare differences between documents)
Document translation
Document encryption and decryption
Table data import/export (database interaction)
Installation Guide
Prerequisites
Python 3.7 or higher
pip package manager
Microsoft Office or compatible components (such as python-docx, openpyxl)
Basic Installation
# Clone the repository
git clone https://github.com/theWDY/office-editor-mcp.git
cd office-editor-mcp

# Install dependencies
pip install -r requirements.txt
Configuration
Configuration in Cursor
Method 1: UI Configuration
Open Cursor
Go to Settings > Features > MCP
Click "+ Add New MCP Server"
Fill in the configuration information:
Name: Office Assistant (modify as preferred)
Type: Select stdio
Command: Enter the full path to run the server, for example:
python /path/to/office_server.py
Note: Replace with your actual file path

Method 2: JSON Configuration File (Recommended)
Create a .cursor folder in the project directory (if it doesn't exist)
Create an mcp.json file in that folder with the following content:
{
  "mcpServers": {
    "office-assistant": {
      "command": "python",
      "args": ["/path/to/office_server.py"],
      "env": {}
    }
  }
}
Configuration in Claude for Desktop
Edit the Claude configuration file:

macOS: ~/Library/Application Support/Claude/claude_desktop_config.json
Windows: %APPDATA%\Claude\claude_desktop_config.json
Add the following configuration:

{
  "mcpServers": {
    "office-document-server": {
      "command": "python",
      "args": [
        "/path/to/office_server.py"
      ]
    }
  }
}
Restart Claude to apply the configuration.
Usage Examples
After configuration, you can issue commands to your AI assistant like:

Word Document Operations
"Create a new document called 'quarterly_report.docx' with a title page"
"Add a heading and three paragraphs to the document"
"Insert a 4x4 table with sales data"
"Make the word 'important' in paragraph 2 bold and red"
"Search and replace all instances of 'old term' with 'new term'"
Excel Operations
"Create a new Excel workbook named 'financial_analysis.xlsx'"
"Insert 'Quarterly Sales' as a title in cell A1"
"Create a table with department sales data and calculate the sum"
"Create a bar chart for the sales data"
"Sort the data in column B in descending order"
PowerPoint Operations
"Create a presentation named 'project_presentation.pptx'"
"Add a new slide with the title 'Project Overview'"
"Insert the company logo in slide 2"
"Add a fly-in animation to the title"
API Reference
Word Document Operations
# Document Creation and Properties
create_document(filename, title=None, author=None)
get_document_info(filename)
get_document_text(filename)
get_document_outline(filename)
list_available_documents(directory=".")
copy_document(source_filename, destination_filename=None)

# Content Addition
add_heading(filename, text, level=1)
add_paragraph(filename, text, style=None)
add_table(filename, rows, cols, data=None)
add_picture(filename, image_path, width=None)
add_page_break(filename)

# Text Formatting
format_text(filename, paragraph_index, start_pos, end_pos, bold=None, 
            italic=None, underline=None, color=None, font_size=None, font_name=None)
search_and_replace(filename, find_text, replace_text)
delete_paragraph(filename, paragraph_index)
create_custom_style(filename, style_name, bold=None, italic=None, 
                    font_size=None, font_name=None, color=None, base_style=None)
Excel Operations
# Workbook Operations
create_workbook(filename)
open_workbook(filename)
save_workbook(filename, new_filename=None)
add_worksheet(filename, sheet_name=None)
list_worksheets(filename)

# Cell Operations
read_cell(filename, sheet_name, cell_reference)
write_cell(filename, sheet_name, cell_reference, value)
format_cell(filename, sheet_name, cell_reference, **format_args)
PowerPoint Operations
# Presentation Operations
create_presentation(filename)
open_presentation(filename)
save_presentation(filename, new_filename=None)
add_slide(filename, layout=None)
Troubleshooting
Common Issues
Missing Styles

Some documents may lack required styles for heading and table operations
The server will attempt to create missing styles or use direct formatting
For best results, use templates with standard Office styles
Permission Issues

Ensure the server has permission to read/write to document paths
Use the copy_document function to create editable copies of locked documents
Check file ownership and permissions if operations fail
Image Insertion Problems

Use absolute paths for image files
Verify image format compatibility (JPEG, PNG recommended)
Check image file size and permissions
Debugging
Enable detailed logging by setting the environment variable:

export MCP_DEBUG=1  # Linux/macOS
set MCP_DEBUG=1     # Windows
Implementation Progress
✅ Build MCP server basic framework
✅ Successful integration with AI assistants
✅ Basic Word document operations
✅ Basic Excel workbook operations
✅ Basic PowerPoint presentation operations
✅ Advanced features enhancement
✅ Performance optimization
✅ Cross-platform compatibility testing
Contributing
Contributions are welcome! Feel free to submit a Pull Request.

Fork the repository
Create your feature branch (git checkout -b feature/amazing-feature)
Commit your changes (git commit -m 'Add some amazing feature')
Push to the branch (git push origin feature/amazing-feature)
Open a Pull Request
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Model Context Protocol for protocol specification
python-docx for Word document processing
openpyxl for Excel processing
python-pptx for PowerPoint processing
Note: This server interacts with document files on your system. Always verify that requested operations are appropriate before confirming them in AI assistants or other MCP clients.

**Official site: ** [https://pypi.org/project/office-editor-mcp/](https://pypi.org/project/office-editor-mcp/)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `memory`
- Tags: `knowledge and memory`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `--from office-editor-mcp==0.2.1 pptserver`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/lesyeuxderr-office-editor.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
