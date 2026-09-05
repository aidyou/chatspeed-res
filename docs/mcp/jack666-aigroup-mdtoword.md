---
title: "aigroup-mdtoword-mcp"
description: "aigroup-mdtoword-mcp \"MoGao Master\" is a local document conversion tool built based on the MCP protocol. It efficiently converts Markdown to Word documents and natively integrates rich preset template…"
---

# aigroup-mdtoword-mcp

aigroup-mdtoword-mcp "MoGao Master" is a local document conversion tool built based on the MCP protocol. It efficiently converts Markdown to Word documents and natively integrates rich preset template…

# aigroup-mdtoword-mcp

[![Version](/mcp-assets/e93ccb076d60f10d0a254b43f3ab3304.svg)](https://www.npmjs.com/package/aigroup-mdtoword-mcp)
![License](/mcp-assets/5816f652aa1f0cc4eedb21a2f733e09e.svg)
![Node.js](/mcp-assets/a6853f6b3626e12a1c348f7d36b64bc9.svg)

"MoGao Master" is a local document conversion tool built based on the MCP protocol. It efficiently converts Markdown to Word documents and natively integrates rich preset templates, precise style configurations, as well as advanced features such as headers, footers, and mathematical formulas, aiming to provide you with a professional-level typesetting experience.

## ✨ Core Features

### 🎯 Document Conversion
- ✅ **Full Markdown Syntax Support** - Titles, paragraphs, lists, tables, code blocks, quotes, etc.
- ✅ **Math Formula Support** - Full LaTeX math expression parsing and conversion
- ✅ **Multiple Preset Templates** - Professional templates for academic papers, business reports, technical documents, etc.
- ✅ **Rich Style Configuration** - Comprehensive control over themes, fonts, colors, spacing, etc.

### 🎨 Style System
- ✅ **Theme System** - Unified color, font, and spacing management
- ✅ **Watermark Function** - Custom text, transparency, rotation angle
- ✅ **Headers and Footers** - Custom content, automatic page numbers, different first/odd/even pages
- ✅ **Automatic Table of Contents** - Configurable levels and styles, supports page number leaders

### 📊 Table Handling
- ✅ **12 Predefined Table Styles** - Minimalist, professional, zebra, grid, etc.
- ✅ **Column Width Control** - Precise control over each column width
- ✅ **Cell Alignment** - Horizontal and vertical alignment
- ✅ **Zebra Stripe Style** - Different background colors for odd and even rows
- ✅ **Data Import** - Supports CSV and JSON format data import

### 🖼️ Image Processing
- ✅ **Multiple Image Sources** - Local files, web images, Base64 encoding
- ✅ **Adaptive Sizing** - Automatically adjusts image size
- ✅ **Format Detection** - Smart recognition of PNG, JPEG, GIF, SVG, etc.
- ✅ **Error Handling** - Displays placeholder on load failure

### 🧮 Math Formulas
- ✅ **LaTeX Math Expressions** - Full LaTeX syntax support
- ✅ **Inline and Display Formulas** - `$...$` and `$$...$$` formats
- ✅ **Multiple Math Components** - Fractions, roots, subscripts, superscripts, summation, integrals, etc.
- ✅ **High-Performance Processing** - Math formula preprocessing in milliseconds

### 🔧 MCP Protocol Features
- ✅ **Latest MCP SDK 1.20.1** - Uses the latest TypeScript SDK
- ✅ **Zod Type Validation** - Complete input and output type safety
- ✅ **Streamable HTTP Transport** - Supports both HTTP and stdio transport methods
- ✅ **Notification Debouncing** - Optimizes network performance, reduces unnecessary notifications
- ✅ **Structured Output** - Tool returns structured data for easy processing

## 📁 Project Structure

plaintext
aigroup-mdtoword-mcp/
├── src/                     # Source code directory
│   ├── converter/           # Converter module
│   │   └── markdown.ts      # Markdown to DOCX converter
│   ├── template/            # Template system
│   │   ├── presetLoader.ts  # Preset template loader
│   │   └── processor.ts     # Template processor
│   ├── types/               # Type definitions
│   │   ├── index.ts         # Main type definitions
│   │   ├── style.ts         # Style type definitions
│   │   └── template.ts      # Template type definitions
│   └── utils/               # Utility functions
│       ├── errorHandler.ts  # Error handling
│       ├── imageProcessor.ts # Image processing
│       ├── mathProcessor.ts  # Math formula processing
│       ├── styleConverter.ts # Style conversion
│       ├── styleEngine.ts   # Style engine
│       ├── tableBuilder.ts  # Table builder
│       ├── tableProcessor.ts # Table processor
│       ├── tocGenerator.ts  # Table of contents generator
│       └── watermarkProcessor.ts # Watermark processor
├── tests/                   # Test files
│   ├── test-header-footer.ts  # Header and footer tests
│   ├── test-math-formulas.ts  # Math formula tests
│   ├── test-resources.js    # Resource tests
│   └── temp/                # Temporary test files
├── docs/                    # Documentation directory
│   ├── release-notes/       # Release notes
│   ├── MATH_FORMULAS_GUIDE.md # Math formulas guide
│   ├── MATH_WPS_COMPATIBILITY.md # WPS compatibility notes
│   └── README.md           # Documentation
├── examples/                # Example files and templates
│   ├── templates/           # Template configurations
│   ├── enhanced-features-demo.md # Enhanced features demo
│   ├── math-formulas-demo.md    # Math formulas demo
│   └── table-features-demo.md   # Table features demo
├── charts/                  # Charts directory (example images)
├── dist/                    # Compiled output directory (auto-generated)
├── package.json             # Project configuration
├── tsconfig.json           # TypeScript configuration
└── README.md               # Project documentation## 🚀 Quick Start

### Installation

#### Global Installation
bash
npm install -g aigroup-mdtoword-mcp

#### Local Installation
bash
npm install aigroup-mdtoword-mcp

#### Use Directly with npx
bash
npx aigroup-mdtoword-mcp

### Usage

#### 1. As an MCP Server (Stdio)

Configure in Roo Code, Claude Desktop, or other MCP-supported tools:

json
{
  "mcpServers": {
    "aigroup-mdtoword-mcp": {
      "command": "npx",
      "args": ["-y", "aigroup-mdtoword-mcp"]
    }
  }
}

#### 2. As an HTTP Server

bash
npm run server:http
# or
node dist/http-server.js

The server will start at http://localhost:3000 and supports CORS configuration.

## 📋 MCP Tools

### Main Tools

| Tool Name | Description | Core Features |
|---------|-------------|---------------|
| `markdown_to_docx` | Convert Markdown to Word document | Core functionality, supports template and style configuration |
| `create_table_from_csv` | Convert CSV to table data | Table data import, supports multiple delimiters |
| `create_table_from_json` | Convert JSON to table data | JSON data to table, supports column selection |
| `list_table_styles` | Manage table styles | View available table styles, no input parameters required |

### Resources

| Resource Name | Description | URI Format |
|--------------|-------------|------------|
| `templates-list` | List of all available templates | `templates://list` |
| `templates-default` | Information about the default template | `templates://default` |
| `template-details` | Details of a specific template | `templates://{templateId}` |
| `style-guide` | Style configuration guide | `style-guide://complete` |
| `converters-supported-formats` | List of supported formats | `converters://supported_formats` |
| `performance-metrics` | Performance metrics description | `performance://metrics` |

### Tips

| Tip Name | Description | Parameters |
|----------|-------------|------------|
| `markdown_to_docx_help` | Usage help | None |
| `markdown_to_docx_examples` | Practical examples | None |
| `create_document` | Document creation guide | `documentType` |
| `batch_processing_workflow` | Batch processing workflow | `scenario` |
| `troubleshooting_guide` | Troubleshooting guide | `errorType` |

## 📝 Usage Examples

### Basic Conversion

json
{
  "markdown": "# My Document\n\nThis is the body content, which will automatically apply the default style.",
  "filename": "output.docx"
}

### Using a Preset Template

json
{
  "markdown": "# Academic Paper\n\nContent",
  "filename": "paper.docx",
  "template": {
    "type": "preset",
    "presetId": "academic"
  }
}

### Including Mathematical Formulas

json
{
  "markdown": "# Math Test\n\nPythagorean Theorem: $a^2 + b^2 = c^2$\n\nQuadratic Formula:\n\n$$x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$$",
  "filename": "math-test.docx"
}

### Adding Watermark and Headers/Footers

json
{
  "markdown": "# Confidential Document\n\nContent",
  "filename": "confidential.docx",
  "styleConfig": {
    "watermark": {
      "text": "Confidential",
      "opacity": 0.2,
      "rotation": -45
    },
    "headerFooter": {
      "header": {
        "content": "Company Document",
        "alignment": "center"
      },
      "footer": {
        "content": "Page ",
        "showPageNumber": true,
        "pageNumberFormat": " / ",
        "showTotalPages": true,
        "totalPagesFormat": " / Total ",
        "alignment": "center"
      }
    }
  }
}

### Reading from a File

json
{
  "inputPath": "./input/document.md",
  "filename": "output.docx",
  "outputPath": "./output"
}

## 🎨 Preset Templates

### Available Templates

| Template ID | Name | Category | Description | Default |
|-------------|------|----------|-------------|---------|
| `customer-analysis` | Customer Analysis Template | business | Designed for customer analysis reports | ⭐ |
| `academic` | Academic Paper Template | academic | Professional template for academic papers | |
| `business` | Business Report Template | business | Professional template for business reports | |
| `technical` | Technical Documentation Template | technical | Template for technical documentation | || `minimal` | Minimal Template | minimal | A concise document template | |
| `enhanced-features` | Enhanced Features Example | other | A template showcasing all enhanced features | |

### Table Styles

The system provides 12 predefined table styles:

1. **minimal** - Minimal modern style
2. **professional** - Professional business style  
3. **striped** - Zebra stripe style
4. **grid** - Grid style
5. **elegant** - Elegant style
6. **colorful** - Colorful style
7. **compact** - Compact style
8. **fresh** - Fresh style
9. **tech** - Tech style
10. **report** - Report style
11. **financial** - Financial style
12. **academic** - Academic style

## 🧮 Math Formula Support

### Supported LaTeX Commands

| Type | LaTeX Command | Example | Description |
|------|---------------|---------|-------------|
| **Fraction** | `\frac{numerator}{denominator}` | `\frac{1}{2}` | Fraction expression |
| **Square Root** | `\sqrt{content}` | `\sqrt{2}` | Square root |
| **Nth Root** | `\sqrt[n]{content}` | `\sqrt[3]{8}` | Nth root |
| **Superscript** | `^{content}` | `x^2` | Exponent/superscript |
| **Subscript** | `_{content}` | `x_1` | Subscript |
| **Summation** | `\sum_{lower}^{upper}` | `\sum_{i=1}^{n}` | Summation symbol |
| **Integral** | `\int` | `\int f(x)dx` | Integral symbol |
| **Trigonometric Functions** | `\sin`, `\cos`, `\tan` | `\sin\theta` | Trigonometric functions |
| **Logarithms** | `\log`, `\ln` | `\ln x` | Logarithmic functions |
| **Limit** | `\lim` | `\lim_{x \to 0}` | Limit |
| **Greek Letters** | `\alpha`, `\beta`, `\pi` etc. | `\pi r^2` | Greek letters |

### Usage Examples

# Math Formula Examples

## Inline Formula
This is an inline formula: $E = mc^2$, very simple.

## Display Formula
Euler's formula:

$$e^{i\pi} + 1 = 0$$

## Complex Formula
Quadratic formula:

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

## 🔧 Configuration Instructions

### Style Configuration Structure

typescript
{
  "styleConfig": {
    "document": {
      "defaultFont": "宋体",
      "defaultSize": 24,
      "page": {
        "size": "A4",
        "orientation": "portrait",
        "margins": {
          "top": 1440,
          "bottom": 1440,
          "left": 1440,
          "right": 1440
        }
      }
    },
    "theme": {
      "name": "Professional Theme",
      "colors": {
        "primary": "2E74B5",
        "secondary": "5A8FC4",
        "text": "333333"
      },
      "fonts": {
        "heading": "微软雅黑",
        "body": "宋体",
        "code": "Consolas"
      }
    },
    "watermark": {
      "text": "Watermark Text",
      "font": "Arial",
      "size": 48,
      "color": "CCCCCC",
      "opacity": 0.1,
      "rotation": -45
    },
    "tableOfContents": {
      "enabled": true,
      "title": "Table of Contents",
      "levels": [1, 2, 3],
      "showPageNumbers": true,
      "tabLeader": "dot"
    },
    "headerFooter": {
      "header": {
        "content": "Header Content",
        "alignment": "center"
      },
      "footer": {
        "content": "Page ",
        "showPageNumber": true,
        "pageNumberFormat": " / Total Pages",
        "showTotalPages": true,
        "totalPagesFormat": " / Total ",
        "alignment": "center"
      },
      "differentFirstPage": true,
      "differentOddEven": false,
      "pageNumberStart": 1,
      "pageNumberFormatType": "decimal"
    }
  }
}

### Unit Explanation

- **Twip**: 1/1440 inch = 1/20 point, used for spacing and margins
- **Half-point**: Font size unit, 24 half-points = 12pt
- **Example**: 2 character indent = 480 twips, 1 inch margin = 1440 twips

## 📊 Performance Metrics

### Conversion Performance

| Document Size | Number of Math Formulas | Preprocessing Time | Total Conversion Time | Memory Usage |
|---------------|-------------------------|--------------------|-----------------------|--------------|
|  100KB | 50-200 | 50-200ms | 500ms-2s | 100-200MB |

### System Requirements

- **Node.js**: >= 18.0.0
- **Memory**: At least 512MB available memory
- **Disk Space**: At least 100MB available space## 🔍 Troubleshooting

### Common Issues

1. **Images Not Displaying**
   - Check if the image path is correct
   - Ensure you are using common formats like PNG, JPEG, GIF, etc.
   - Compress images to under 5MB

2. **Math Formula Conversion Failure**
   - Check if the LaTeX syntax is correct
   - Ensure you are using supported LaTeX commands
   - Simplify overly complex nested structures

3. **Styles Not Applied**
   - Verify that the JSON format is correct
   - Check style priority (custom styles will override templates)
   - Use 6-digit hexadecimal color values

### Getting Help

- View complete documentation: `style-guide://complete`
- View template list: `templates://list`
- View performance metrics: `performance://metrics`
- View supported formats: `converters://supported_formats`

## 📄 License

MIT

## 🤝 Contributions

Pull Requests are welcome!

## 📚 Related Resources

- [MCP Official Documentation](https://modelcontextprotocol.io)
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Zod Documentation](https://zod.dev)
- [docx Library Documentation](https://docx.js.org)

## 👨‍💻 Author

AI Group - [jackdark425@gmail.com](mailto:jackdark425@gmail.com)

---

⭐ If this project has been helpful to you, please give it a Star!

**Official site: ** [https://github.com/jackdark425/aigroup-mdtoword-mcp](https://github.com/jackdark425/aigroup-mdtoword-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `files`, `data`
- Tags: `file systems`, `research and data`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y aigroup-mdtoword-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/jack666-aigroup-mdtoword.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
