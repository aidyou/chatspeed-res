---
title: "aigroup-video-mcp"
description: "Aigroup Video MCP Aigroup Video MCP is a video multimodal understanding MCP (Model Context Protocol) server based on Alibaba Cloud DashScope, providing powerful video content analysis capabilities. 🌟…"
---

# aigroup-video-mcp

Aigroup Video MCP Aigroup Video MCP is a video multimodal understanding MCP (Model Context Protocol) server based on Alibaba Cloud DashScope, providing powerful video content analysis capabilities. 🌟…

# Aigroup Video MCP

Aigroup Video MCP is a video multimodal understanding MCP (Model Context Protocol) server based on Alibaba Cloud DashScope, providing powerful video content analysis capabilities.

[![Python](/mcp-assets/d52fa8fd608496fb7cb57d905d36fafc.svg)](https://python.org)
[![License](/mcp-assets/5816f652aa1f0cc4eedb21a2f733e09e.svg)](https://github.com/jackdark425/aigroup-video-mcp/blob/HEAD/LICENSE)
[![MCP](/mcp-assets/5723e6b7b8950ac8c07587ca6cf6e73a.svg)](https://modelcontextprotocol.io)

## 🌟 Features

- **🎥 Video Content Analysis**: Supports analyzing video content via URL or local path
- **🧠 Intelligent Summarization**: Automatically generates video summaries and key information
- **🎬 Scene Recognition**: Identifies major scenes and scene transitions in the video
- **✨ Custom Prompts**: Supports flexible custom analysis requirements
- **🔌 MCP Protocol Support**: Fully compatible with the MCP protocol, supporting stdio and SSE modes
- **⚡ High-Performance Processing**: Based on asynchronous processing, supports concurrent requests
- **📊 Usage Statistics**: Built-in usage statistics and monitoring features
- **🛡️ Security Configuration**: Supports security features such as domain whitelisting and file size limits

## 🎯 Core Functions

### Video Analysis Tools

- **analyze_video**: Basic video content analysis
- **summarize_video**: Video summary generation (supports brief, detailed, and general modes)
- **analyze_video_scenes**: Video scene analysis and transition detection
- **analyze_video_custom**: Custom prompt-based video analysis
- **validate_video_source**: Video source validation and checks

### System Resources

- **config://system**: System configuration information
- **models://available**: Available model information
- **status://system**: System status and health checks
- **stats://usage**: Usage statistics and analysis reports

## 🚀 Quick Start

### Environment Requirements

- Python 3.8+
- DashScope API Key

### Installation

bash
# Clone the project
git clone https://github.com/jackdark425/aigroup-video-mcp.git
cd aigroup-video-mcp

# Install dependencies
pip install -r requirements.txt

# Or install using pip
pip install aigroup-video-mcp

### Configuration

1. Copy the example environment variable file:

bash
cp .env.example .env

2. Edit the `.env` file to set your DashScope API Key:

bash
DASHSCOPE_API_KEY=your_dashscope_api_key_here

3. Or set the environment variable directly:

bash
export DASHSCOPE_API_KEY=your_dashscope_api_key_here

### Running the Server

#### MCP Mode (Default)

bash
# Use stdio transport mode (recommended for MCP clients)
python -m aigroup_video_mcp.main serve

#### SSE Mode

bash
# Use SSE transport mode (for HTTP clients)
python -m aigroup_video_mcp.main serve --transport sse --host 0.0.0.0 --port 3001

## 📖 Usage Examples

### Command Line Tool

#### Analyzing a Video File

bash
# Basic video analysis
python -m aigroup_video_mcp.main analyze video.mp4

# Using a custom prompt
python -m aigroup_video_mcp.main analyze video.mp4 --prompt "Please analyze the characters' actions and expressions in the video"

# Output in JSON format
python -m aigroup_video_mcp.main analyze video.mp4 --format json --save-to result.json

#### Health Check

bash
# Check server health status
python -m aigroup_video_mcp.main health

# View server information
python -m aigroup_video_mcp.main info

# Validate configuration
python -m aigroup_video_mcp.main config

### RooCode MCP Client Integration

If you are developing an MCP client, you can integrate it as follows:
Set `DASHSCOPE_API_KEY` directly in the environment variables.
json
{
  "mcpServers": {
    "aigroup-video-mcp": {
      "command": "python",
      "args": [
        "-m",
        "aigroup_video_mcp.main",
        "serve"
      ],
      "env": {
        "DASHSCOPE_API_KEY": "${env:DASHSCOPE_API_KEY}"
      },
      "alwaysAllow": [
        "analyze_video",
        "summarize_video",
        "analyze_video_scenes",
        "analyze_video_custom",
        "validate_video_source"
      ],
      "disabled": false
    }
  }
}

### Python API

python
import asyncio
from aigroup_video_mcp.core.analyzer import get_analyzer, create_video_source

async def analyze_video():
    # Create an analyzer
    analyzer = get_analyzer(async_mode=True)
    
    # Create a video source
    video_source = create_video_source("path/to/video.mp4")
    
    # Analyze the video
    result = await analyzer.analyze(
        video_source, 
        "Please describe the main content of this video"
    )
    
    if result.success:
        print(result.content)
    else:
        print(f"Analysis failed: {result.error}")

# Run
asyncio.run(analyze_video())## 🛠️ Detailed Tool Description

### analyze_video

A basic tool for video content analysis.

**Parameters:**
- `video_path` (required): Path or URL to the video file
- `prompt` (optional): Custom prompt for analysis
- `model` (optional): Name of the model to use
- `temperature` (optional): Temperature for text generation (0.0-2.0)
- `max_tokens` (optional): Maximum number of tokens in the response

**Example:**
json
{
  "video_path": "https://example.com/video.mp4",
  "prompt": "Please analyze the content of this video, including main scenes, characters, actions, and events.",
  "temperature": 0.7,
  "max_tokens": 2000
}

### summarize_video

A tool for generating video summaries.

**Parameters:**
- `video_path` (required): Path or URL to the video file
- `summary_type` (optional): Type of summary (`general`, `detailed`, `brief`)
- `model` (optional): Name of the model to use
- `temperature` (optional): Temperature for text generation
- `max_tokens` (optional): Maximum number of tokens in the response

### analyze_video_scenes

A tool for analyzing video scenes.

**Parameters:**
- `video_path` (required): Path or URL to the video file
- `scene_detection` (optional): Whether to detect scene transitions
- `detailed_analysis` (optional): Whether to provide a detailed analysis
- `model` (optional): Name of the model to use

### analyze_video_custom

A customizable tool for video analysis.

**Parameters:**
- `video_path` (required): Path or URL to the video file
- `custom_prompt` (required): Custom prompt for analysis
- `analysis_focus` (optional): Focus of the analysis
- `output_format` (optional): Format of the output
- `language` (optional): Language of the output

### validate_video_source

A tool for validating video sources.

**Parameters:**
- `video_path` (required): Path or URL to the video file
- `check_accessibility` (optional): Whether to check accessibility
- `check_format` (optional): Whether to check format compatibility
- `check_size` (optional): Whether to check file size
- `detailed_info` (optional): Whether to return detailed information

## 📊 Supported Video Formats

- MP4
- AVI
- MOV
- MKV
- WebM
- FLV

## ⚙️ Configuration Options

### Environment Variables

| Variable Name | Description | Default Value |
|---------------|-------------|---------------|
| `DASHSCOPE_API_KEY` | DashScope API key | *Required* |
| `VIDEO__MAX_FILE_SIZE` | Maximum file size (bytes) | 104857600 (100MB) |
| `VIDEO__MAX_DURATION` | Maximum video duration (seconds) | 3600 (1 hour) |
| `MCP__MAX_CONCURRENT_REQUESTS` | Maximum number of concurrent requests | 10 |
| `LOG__LEVEL` | Log level | INFO |
| `ENVIRONMENT` | Running environment | production |
| `DEBUG` | Debug mode | false |

### Configuration File

The project supports configuration through a `.env` file. All environment variables can be set in the configuration file.

## 🔒 Security Features

- **File Size Limitation**: Prevents uploading of overly large files
- **Format Validation**: Only supports specified video formats
- **Domain Whitelist/Blacklist**: Controls allowed URL domains
- **Rate Limiting**: Prevents API abuse
- **Input Validation**: Strict parameter validation

## 📈 Monitoring and Statistics

The server includes built-in usage statistics and monitoring features:

- **Usage Statistics**: Frequency of tool and resource usage
- **Performance Monitoring**: Response time and success rate
- **Health Checks**: System status and component health
- **Resource Monitoring**: CPU, memory, and disk usage

Accessing statistics:

bash
# View usage statistics
curl http://localhost:3001/resources/stats://usage

# View system status
curl http://localhost:3001/resources/status://system

## 🐛 Troubleshooting

### Common Issues

1. **API Key Not Set**
   
   Error: DashScope API key is required
   
   Solution: Set the `DASHSCOPE_API_KEY` environment variable

2. **Unsupported Video Format**
   
   Error: Unsupported format: xxx
   
   Solution: Convert the video to a supported format (MP4, AVI, MOV, MKV, WebM, FLV)

3. **File Too Large**
   
   Error: File too large
   
   Solution: Compress the video or adjust the `VIDEO__MAX_FILE_SIZE` configuration

4. **Network Connection Issue**
   
   Error: Failed to connect to DashScope API
   
   Solution: Check your network connection and ensure the API Key is correct### Debug Mode

Enable debug mode to get more detailed logs:

bash
python -m aigroup_video_mcp.main --debug serve

## 🤝 Contribution

Contributions are welcome! Please follow these steps:

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/jackdark425/aigroup-video-mcp/blob/HEAD/LICENSE) file for details.

## 🙏 Acknowledgments

- [Alibaba Cloud DashScope](https://dashscope.aliyun.com/) - Provides powerful multimodal AI capabilities
- [Model Context Protocol](https://modelcontextprotocol.io/) - Provides a standardized model interaction protocol
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Provides the Python implementation of MCP

## 📞 Support

If you encounter any issues or have suggestions, please:

1. Check the [FAQ](https://github.com/jackdark425/aigroup-video-mcp/blob/HEAD/README.md#故障排除) section
2. Submit an [Issue](https://github.com/jackdark425/aigroup-video-mcp/issues)
3. Contact the development team: jackdark425@gmail.com

---

**Made with ❤️ by Aigroup Team**

**Official site: ** [https://github.com/jackdark425/aigroup-video-mcp](https://github.com/jackdark425/aigroup-video-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `entertainment and media`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `python`
- Args: `-m aigroup_video_mcp.main serve`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/jack666-aigroup-video.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
