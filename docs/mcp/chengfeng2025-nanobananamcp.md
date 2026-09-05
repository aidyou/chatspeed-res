---
title: "NanoBananaMCP"
description: "Gemini MCP is an MCP (Model Context Protocol) server based on the Google Gemini 2.0 Flash model, dedicated to image analysis and processing. It can be seamlessly integrated into MCP-protocol-supportin…"
---

# NanoBananaMCP

Gemini MCP is an MCP (Model Context Protocol) server based on the Google Gemini 2.0 Flash model, dedicated to image analysis and processing. It can be seamlessly integrated into MCP-protocol-supportin…

# Gemini MCP - Smart Image Analysis Service Based on Gemini

## Project Overview

Gemini MCP is an MCP (Model Context Protocol) server based on the Google Gemini 2.0 Flash model, dedicated to image analysis and processing. It can be seamlessly integrated into MCP-protocol-supporting AI assistants such as Claude Desktop and Cursor, providing powerful visual understanding capabilities.

## Core Features

### Main Functions
- **Multimodal analysis**: supports image content understanding, scene recognition, text extraction, etc.
- **Flexible input**: supports local file paths, web URLs, Base64 encoding, and other image input methods
- **Streaming responses**: real-time streaming output of analysis results for a better user experience
- **Smart storage**: automatically saves processing results and generated images

### Technical Advantages
- **Zero-dependency installation**: supports running directly with uvx, no pre-installation needed
- **Cross-platform compatibility**: supports macOS, Windows, Linux, and other mainstream operating systems
- **Proxy support**: built-in SOCKS5 proxy support for various network environments
- **Standard protocol**: fully compliant with MCP specifications, integrable with any MCP client

## Quick Start

### Getting an API key

1. **Rabbit API**: visit the [Rabbit API recharge platform](https://api.tu-zi.com/topup) to purchase API services compatible with the official format (direct domestic access, no VPN needed, fully compatible with the official Gemini API interface)

### Method 1: Run with uvx (recommended)

No installation needed, run directly:

```bash
# Set the API key and start the service
GEMINI_API_KEY=your-api-key uvx gemini-mcp
```

### Method 2: Install via pip

```bash
# Install the package
pip install gemini-mcp

# Run the service
GEMINI_API_KEY=your-api-key gemini-mcp
```

### Method 3: Run from source

```bash
# Clone the repository
git clone https://github.com/chengfeng2025/gemini-mcp-python.git
cd gemini-mcp-python

# Install dependencies
pip install -r requirements.txt

# Run the service
python -m gemini_mcp
```

## Client Configuration

### Claude Desktop Configuration

1. Open the config file:
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`

2. Add the following configuration:

```json
{
  "mcpServers": {
    "gemini": {
      "command": "uvx",
      "args": [
        "gemini-mcp"
      ],
      "env": {
        "GEMINI_API_KEY": "API",
        "GEMINI_MCP_OUTPUT_DIR": "specify download directory, optional"
      }
    }
  }
}
```

### Cursor Configuration

Edit `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "gemini": {
      "command": "uvx",
      "args": ["gemini-mcp"],
      "env": {
        "GEMINI_API_KEY": "your-api-key"
      }
    }
  }
}
```

## Usage Examples

In a configured Claude Desktop or Cursor, you can:

```
# Analyze a local image
Please analyze this image: /Users/name/Pictures/photo.jpg

# Analyze a web image
Describe the content of this image: https://example.com/image.png

# Extract text from an image
Extract all text from the image: /path/to/document.png

# Scene understanding
In what scene was this image taken? /path/to/scene.jpg
```

## Advanced Configuration

### Environment Variables

| Variable | Description | Default |
|--------|------|--------|
| `GEMINI_API_KEY` | Gemini API key (required) | - |
| `OUTPUT_DIR` | Output file save directory | `./outputs` |
| `ALL_PROXY` | SOCKS5 proxy address | - |
| `LOG_LEVEL` | Log level | `INFO` |

### Command Line Parameters

```bash
# View all available parameters
gemini-mcp --help

# Run in HTTP service mode
gemini-mcp --mode http --port 8080

# Enable debug mode
gemini-mcp --debug

# Specify the output directory
gemini-mcp --output-dir /custom/path
```

## API Reference

### Supported Tools

#### `analyze_image`
Analyzes image content and returns a description.

**Parameters:**
- `image_input`: image input (file path, URL, or Base64)
- `prompt`: analysis prompt (optional)

**Example:**
```python
{
  "tool": "analyze_image",
  "arguments": {
    "image_input": "/path/to/image.jpg",
    "prompt": "Describe the main content of this image"
  }
}
```

## Development Guide

### Local development

```bash
# Clone the project
git clone https://github.com/chengfeng2025/gemini-mcp-python.git
cd gemini-mcp-python

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest tests/
```

### Contributing

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Create a Pull Request

## Troubleshooting

### Common Issues

**Q: "API key not found" error**
A: Make sure the `GEMINI_API_KEY` environment variable is set correctly.

**Q: Connection timeout error**
A: Check the network connection, or configure a proxy:
```bash
ALL_PROXY=socks5://127.0.0.1:1080 gemini-mcp
```

**Q: Claude Desktop cannot recognize the service**
A: Restart the Claude Desktop app to reload the configuration.

## Project Info

- **Author**: chengfeng2025
- **License**: MIT
- **Version**: 1.0.0
- **Updated**: January 2025
- **GitHub**: [gemini-mcp-python](https://github.com/chengfeng2025/gemini-mcp-python)

## Related Links

- [MCP protocol spec](https://modelcontextprotocol.io/)
- [Gemini API docs](https://ai.google.dev/gemini-api/docs)
- [Issue feedback](https://github.com/chengfeng2025/gemini-mcp-python/issues)

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Ceeon/gemini-mcp/blob/HEAD/LICENSE) file for details.

---

**Note**: using this project requires a valid Gemini API key.

**Official site: ** [https://github.com/Ceeon/gemini-mcp](https://github.com/Ceeon/gemini-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `entertainment and media`, `gemini`, `生图`, `图片`, `google`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `gemini-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/chengfeng2025-nanobananamcp.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
