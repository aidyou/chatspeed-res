---
title: "douyin-mcp-server"
description: "Douyin operations assistant: extracts watermark-free Douyin video links, video copywriting, IP copywriting, material copywriting, and copywriting benchmarking/revision. Official site: https://github.c…"
---

# douyin-mcp-server

Douyin operations assistant: extracts watermark-free Douyin video links, video copywriting, IP copywriting, material copywriting, and copywriting benchmarking/revision. Official site: https://github.c…

# Douyin Watermark-Free Video Text Extraction MCP Server

[![PyPI version](/mcp-assets/aa79358ec60ce76091d985d146c82353.svg)](https://badge.fury.io/py/douyin-mcp-server)
[![Python version](/mcp-assets/1828c31a371deac816fc5f6b8a6e3bbb.svg)](https://pypi.org/project/douyin-mcp-server/)
[![License](/mcp-assets/fa73b4786cfc281bb30f39f895ada091.svg)](https://opensource.org/licenses/Apache-2.0)

An MCP (Model Context Protocol) server that downloads watermark-free videos from Douyin share links, extracts the audio, and converts it to text.

## Project Statement

**Official documentation:** https://github.com/yzfly/douyin-mcp-server

Refer to this project's [README.md](https://github.com/yzfly/douyin-mcp-server/blob/main/README.md) for detailed feature descriptions, usage, and API configuration.

**Important:** If a third-party platform cannot use the server due to its own MCP Server feature limitations, please contact the platform provider. This project provides no technical support or guarantees of any kind. Users bear all losses or damages that may arise from using this project.

**Legal statement:**
1. This project is released under the Apache 2.0 license
2. This project is for learning and research only; it must not be used for any illegal or non-compliant purpose
3. Usage of this project must comply with all applicable laws and regulations
4. The authors and contributors of this project accept no legal liability for any part of the project

## Features

- **Watermark-free video download** - get high-quality watermark-free videos from Douyin share links
- **Smart audio extraction** - automatically extract the audio from videos
- **AI text recognition** - extract text using state-of-the-art speech recognition
- **Automatic cleanup** - intelligently removes temporary files created during processing
- **Flexible configuration** - supports custom API configuration; defaults to the [Alibaba Cloud Bailian API](https://help.aliyun.com/zh/model-studio/get-api-key?)

## Quick Start

### Step 1: Get an API key

Visit the [Alibaba Cloud Bailian API](https://help.aliyun.com/zh/model-studio/get-api-key?) page to get your `DASHSCOPE_API_KEY`:

![Get Alibaba Cloud Bailian API](/mcp-assets/ff29f237674467956ae8c440d6fdcdd4.png)

### Step 2: Configure the environment variable

Add the following config to MCP Server-capable apps such as Claude Desktop or Cherry Studio:

```json
{
  "mcpServers": {
    "douyin-mcp": {
      "command": "uvx",
      "args": ["douyin-mcp-server"],
      "env": {
        "DASHSCOPE_API_KEY": "sk-xxxx"
      }
    }
  }
}
```

### Step 3: Start using it

Once configured, you can call the MCP tools normally in supported applications.

## API Configuration

### Current version (>= 1.2.0)

The latest version defaults to the Alibaba Cloud Bailian API, which offers:
- Better recognition results
- Faster processing
- Lower local resource usage

**Setup:**
1. Go to [Alibaba Cloud Bailian](https://help.aliyun.com/zh/model-studio/get-api-key?) and enable the API service
2. Get the API key and set it as the environment variable `DASHSCOPE_API_KEY`

### Legacy compatibility (<= 1.1.0)

To use an older version, use this configuration:

```json
{
  "mcpServers": {
    "douyin-mcp": {
      "command": "uvx",
      "args": ["douyin-mcp-server@1.1.0"],
      "env": {
        "DOUYIN_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

**Note:** The old version uses the SiliconFlow API; register an account at [SiliconFlow](https://cloud.siliconflow.cn/i/TxUlXG3u) and get an API key.

[1.1.0 documentation](https://pypi.org/project/douyin-mcp-server/1.1.0/)

## Tools

### `get_douyin_download_link`

Gets a watermark-free download link for a Douyin video.

**Parameters:**
- `share_link` (string): a Douyin share link or text containing a link

**Returns:**
- Download link and video info in JSON format

**Note:** works without an API key.

### `extract_douyin_text`

A full text-extraction tool that handles video-to-text conversion in one step.

**Pipeline:**
1. Parse the Douyin share link
2. Run speech recognition directly on the video URL
3. Return the extracted text

**Parameters:**
- `share_link` (string): a Douyin share link or text containing a link
- `model` (string, optional): speech recognition model; defaults to `paraformer-v2`

**Environment variable requirements:**
- `DASHSCOPE_API_KEY`: Alibaba Cloud Bailian API key (required)

### `parse_douyin_video_info`

A lightweight video info parsing tool.

**Parameters:**
- `share_link` (string): a Douyin share link

**Note:** only parses basic video info; does not download the video file.

### Resource access

- `douyin://video/{video_id}`: get details for a video by ID

## System Requirements

### Runtime
- **Python**: 3.10 or later

### Dependencies
- `requests` - HTTP requests
- `ffmpeg-python` - audio/video processing
- `tqdm` - progress bars
- `mcp` - Model Context Protocol support
- `dashscope` - Alibaba Cloud Bailian API client

## Notes

- **API key required**: text extraction needs a valid Alibaba Cloud Bailian API key
- **Some features are free**: getting download links requires no API key
- **Format support**: most Douyin video formats are supported
- **Performance**: the Alibaba Cloud Bailian API provides faster and more accurate recognition

## Development Guide

### Local development setup

```bash
# Clone the project
git clone https://github.com/yzfly/douyin-mcp-server.git
cd douyin-mcp-server

# Install dependencies (development mode)
pip install -e .
```

### Running tests

```bash
# Start the server for testing
python -m douyin_mcp_server.server
```

### Claude Desktop local development config

Add the local development config to your Claude Desktop config file:

```json
{
  "mcpServers": {
    "douyin-mcp": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/path/to/your/douyin-mcp-server",
        "python",
        "-m",
        "douyin_mcp_server"
      ],
      "env": {
        "DASHSCOPE_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

## Disclaimer

### Usage risk
- Users decide entirely on their own whether to use this project and assume all risk
- The authors accept no responsibility for any loss, liability, or risk arising from use of the project

### Code quality
- This project is developed from existing knowledge and technology; the authors strive to ensure correctness and safety
- However, no guarantee is made that the code is completely free of errors or defects; users must evaluate and test it themselves

### Third-party dependencies
- Third-party libraries, plugins, and services used by this project are subject to their own open-source or commercial licenses
- Users must review and comply with the corresponding agreements
- The authors accept no responsibility for the stability, security, or compliance of third-party components

### Legal compliance
- Users must research applicable laws and regulations themselves and ensure their usage is lawful and compliant
- Legal liability and risk from any violation of law is borne entirely by the user
- Using this tool for any activity that infringes intellectual property rights is prohibited
- The developers do not participate in, endorse, or condone the acquisition or distribution of any illegal content

### Data handling
- This project accepts no responsibility for the compliance of users' data collection, storage, or transmission activities
- Users should comply with applicable laws and regulations and ensure lawful, legitimate data handling

### Limitation of liability
- Users may not associate the project authors, contributors, or related parties with their usage
- Users may not hold the authors liable for any loss or damage arising from use of the project
- Derivative development, modification, or compilation based on this project is unrelated to the original authors

### Intellectual property
- This project grants users no patent license
- If use of this project leads to patent disputes or infringement, users bear all risk and liability
- Without written authorization, the project may not be used for commercial promotion, marketing, or sub-licensing

### Service termination
- The authors reserve the right to stop providing service to users who violate this statement at any time
- Violating users may be required to destroy code and derivative works already obtained
- The authors reserve the right to update this statement without notice

**Important: Please read and fully understand this disclaimer before using this project. If you have questions or do not agree with any term, do not use the project. Continuing to use it means you fully accept the statement and voluntarily assume all risks and consequences.**

## License

Apache License 2.0

## Author

- **yzfly** - [yz.liu.me@gmail.com](mailto:yz.liu.me@gmail.com)
- GitHub: [https://github.com/yzfly](https://github.com/yzfly)

## Contributing

Issues and Pull Requests are welcome! We look forward to your participation and contributions.

## Changelog

### v1.2.0 (latest)
- **Performance**: faster, more accurate video copy extraction
- **API upgrade**: switched to the Alibaba Cloud Bailian API, significantly improving recognition accuracy
- **Config update**: environment variable changed from `DOUYIN_API_KEY` to `DASHSCOPE_API_KEY`

### v1.1.0
- **Bug fix**: fixed an error caused by overly long file names when extracting videos

### v1.0.0
- **First release**: initial version
- **Core features**: Douyin video text extraction
- **Link retrieval**: watermark-free video download links
- **Environment config**: reads the API key from an environment variable
- **Automatic cleanup**: removes temporary files automatically
- **Flexible configuration**: supports custom API configuration

**Official site: ** [https://github.com/yzfly/douyin-mcp-server](https://github.com/yzfly/douyin-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `entertainment and media`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `douyin-mcp-server`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/zephyr-douyin.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
