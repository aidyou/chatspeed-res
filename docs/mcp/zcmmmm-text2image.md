---
title: "text2image"
description: "A Model Context Protocol server that provides text-to-image functionality, converting any text into aesthetically pleasing image formats."
---

# text2image

A Model Context Protocol server that provides text-to-image functionality, converting any text into aesthetically pleasing image formats.

# TextImage Service

A Model Context Protocol server that provides text-to-image functionality, converting any text into aesthetically pleasing image formats.

## Features

- Convert text to 1080x1080 sized images
- Automatically calculate text size and center position
- Support custom fonts
- Generated images can be directly saved or displayed

## Installation
```bash
pip install -r requirements.txt
```

## Usage
### As a command line tool
```bash
python src/text2image/text2image.py
```

### In Claude Desktop
Add to your Claude Desktop configuration (claude_desktop_config.json):
```json
{
  "mcpServers": {
    "text2image": {
      "command": "uv",
      "args": [
        "--directory", "/absolute/path/to/text2image",
        "run", "text2image.py"
      ]
    }
  }
}
```

## Available Tools
### text_to_image
Convert text to image

**Parameters**:
- `text` (string, required): Text to be converted
 to image (It can be equipped with a line break character to control the position of line breaks.)
- `text_color` (string, optional): Text color in Hex format, default "#000000"
- `bg_color` (string, optional): Background color in Hex format, default "#FFFFFF"
- `width` (integer, optional): Image width, default 1080
- `height` (integer, optional): Image height, default 1080
- `font_size` (integer, optional): Font size, default 80
- `font_path` (string, optional): Font file path, default 'simhei.ttf'
- `texture` (string, optional): Background texture image path
- `output_path` (string, optional): Output file path, defaults to "output.png" if not specified
- `corner_radius` (integer, optional): Image corner radius, defaults to 0 (sharp corners)

**JSON Request Example**:
```json
{
  "text": "Example text",
  "text_color": "#FF0000",
  "bg_color": "#FFFFFF",
  "width": 800,
  "height": 600,
  "font_size": 60,
  "font_path": "arial.ttf",
  "texture": "background.jpg",
  "output_path": "custom_output.png"
}
```

**Returns**:
- PIL.Image.Image: Generated image object

## Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run service
python src/text2image/text2image.py
```

## License
MIT License

## Contributing
Contributions are welcome! Feel free to submit Pull Requests.

**Official site: ** [https://gitee.com/zcmmmm/text2image-mcp-server](https://gitee.com/zcmmmm/text2image-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `entertainment and media`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uv`
- Args: `--directory /absolute/path/to/text2image run text2image.py`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/zcmmmm-text2image.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
