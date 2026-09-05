---
title: "undoom-sketch-mcp"
description: "A sketching server based on MCP (Model Context Protocol) that can convert ordinary images into various styles of sketch effects. It supports single image conversion, batch processing, and multiple cus…"
---

# undoom-sketch-mcp

A sketching server based on MCP (Model Context Protocol) that can convert ordinary images into various styles of sketch effects. It supports single image conversion, batch processing, and multiple cus…

# Undoom Sketch MCP

[![PyPI version](/mcp-assets/60b2ff0fafaa82cb0d264614759d0905.svg)](https://badge.fury.io/py/undoom-sketch-mcp)
[![License: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://opensource.org/licenses/MIT)

An image sketch-ification server based on the MCP (Model Context Protocol) that converts ordinary images into sketch effects in multiple styles. It supports single-image conversion, batch processing, and various custom parameter adjustments.

## Online Demo

The project is published on PyPI and can be used directly:
- **PyPI**: [undoom-sketch-mcp](https://pypi.org/project/undoom-sketch-mcp/)
- **GitHub**: [undoom-sketch-mcp](https://github.com/kk520879/undoom-sketch-mcp)

## Features

- **Multiple sketch styles**: supports three sketch styles - classic, detailed, and soft
- **Batch processing**: supports batch conversion of all images in a folder
- **Multi-format support**: supports common image formats including JPG, PNG, BMP, GIF, TIFF, WEBP
- **Chinese path support**: full support for Chinese file names and paths
- **Adjustable parameters**: custom blur and contrast parameters
- **Image info viewer**: provides basic image information and recommended parameters

## Requirements

- Python >= 3.13
- Dependencies:
  - mcp[cli] >= 1.12.3
  - opencv-python >= 4.8.0
  - numpy >= 1.24.0

## Quick Start

### Method 1: Use uvx directly (recommended)

```bash
# Use a domestic mirror (recommended)
uvx --index-url https://pypi.tuna.tsinghua.edu.cn/simple undoom-sketch-mcp

# Or use the default source
uvx undoom-sketch-mcp
```

### Method 2: Install via PyPI

```bash
# Install the package
pip install undoom-sketch-mcp

# Run the server
python -m undoom_sketch_mcp
```

### Method 3: Install from source

```bash
# Clone the project
git clone https://github.com/kk520879/undoom-sketch-mcp.git
cd undoom-sketch-mcp

# Install with uv (recommended)
uv sync

# Or with pip
pip install -e .
```

## Usage

### As an MCP server

#### 1. Configure the MCP client

Create an `mcp_config.json` config file:

```json
{
  "mcpServers": {
    "undoom-sketch-mcp": {
      "command": "uvx",
      "args": [
        "--index-url",
        "https://pypi.tuna.tsinghua.edu.cn/simple",
        "undoom-sketch-mcp"
      ]
    }
  }
}
```

#### 2. Run the server directly

```bash
# Start the MCP server
python -m undoom_sketch_mcp

# Or use uvx
uvx undoom-sketch-mcp
```

### Available tools

#### 1. convert_image_to_sketch - single image conversion

**MCP call example:**
```json
{
  "tool": "convert_image_to_sketch",
  "arguments": {
    "image_path": "D:\\photos\\portrait.jpg",
    "style": "classic",
    "blur_size": 21,
    "contrast": 256.0
  }
}
```

**Direct Python call:**
```python
from undoom_sketch_mcp.server import convert_image_to_sketch

result = convert_image_to_sketch(
    image_path="D:/photos/portrait.jpg",
    style="classic",
    blur_size=21,
    contrast=256.0
)
print(result)
```

#### 2. batch_convert_images - batch image conversion

```python
from undoom_sketch_mcp.server import batch_convert_images

result = batch_convert_images(
    folder_path="D:/photos/",
    style="detailed",
    blur_size=21,
    contrast=256.0
)
print(result)
```

#### 3. get_image_info - get image info

```python
from undoom_sketch_mcp.server import get_image_info

info = get_image_info("D:/photos/image.jpg")
print(info)
```

### Sketch style description

- **classic**: classic sketch style, balanced lines and contrast
- **detailed**: detailed sketch style, clearer lines and details
- **soft**: soft sketch style, softer effect, good for landscapes

### Parameter description

- `image_path`: full path to the image file (required)
- `blur_size`: Gaussian blur kernel size (3-101, must be odd, default 21)
- `contrast`: contrast parameter (50-500, default 256.0)
- `style`: sketch style (classic/detailed/soft, default classic)

### Parameter suggestions

- **Large images** (>2MP): blur_size=31-51, contrast=200-300
- **Medium images** (0.5MP-2MP): blur_size=21-31, contrast=256
- **Small images** (<0.5MP): blur_size=11-21, contrast=256-300

## Contributing Guide

We welcome all forms of contribution!

### How to contribute

1. Fork this repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Reporting issues

If you find a bug or have a feature suggestion, submit it in [GitHub Issues](https://github.com/kk520879/undoom-sketch-mcp/issues).

### Development environment setup

```bash
# Clone the repository
git clone https://github.com/kk520879/undoom-sketch-mcp.git
cd undoom-sketch-mcp

# Install development dependencies
uv sync --dev

# Run tests
python -m pytest
```

## License

This project is licensed under the [MIT License](https://github.com/kk520879/undoom-sketch-mcp/blob/HEAD/LICENSE).

## Acknowledgments

- [OpenCV](https://opencv.org/) - the powerful computer vision library
- [MCP](https://modelcontextprotocol.io/) - the Model Context Protocol
- [FastMCP](https://github.com/jlowin/fastmcp) - the fast MCP implementation

---

**If this project helps you, please give it a Star!**

**Official site: ** [https://github.com/kk520879/undoom-sketch-mcp](https://github.com/kk520879/undoom-sketch-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `art and culture`, `素描化`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `--index-url https://pypi.tuna.tsinghua.edu.cn/simple undoom-sketch-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/undoom-undoom-sketch.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
