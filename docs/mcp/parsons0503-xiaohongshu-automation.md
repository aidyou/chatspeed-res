---
title: "xiaohongshu-automation"
description: "xiaohongshu-automation - an automation solution for Xiaohongshu (RED) built on the Model Context Protocol (MCP), providing AI assistants with content publishing, comment management, and system monitor…"
---

# xiaohongshu-automation

xiaohongshu-automation - an automation solution for Xiaohongshu (RED) built on the Model Context Protocol (MCP), providing AI assistants with content publishing, comment management, and system monitor…

# Xiaohongshu Automation Tool

An automation solution for Xiaohongshu (RED) built on the Model Context Protocol (MCP), providing AI assistants with content publishing, comment management, and system monitoring capabilities.

## New Feature: Server-Sent Events (SSE) Support

**SSE real-time data push is now supported!**

The new SSE feature provides:
- **Real-time event push**: real-time updates for tool calls, publishing status, monitoring data, etc.
- **Web client**: a polished web interface for real-time monitoring
- **API endpoints**: RESTful APIs for integration with various clients
- **Multi-topic subscription**: optionally subscribe to the event types you care about

### Quick start of the SSE service

```bash
# Start the SSE server
python mcp_server.py --sse

# Or start directly
python mcp_sse_server.py
```

### Web client experience

Open `sse_web_client.html` in your browser for the real-time monitoring interface, or see SSE_GUIDE.md for the full usage guide.

## Quick Start

### 1. Environment preparation

**We recommend uv for environment management** (a faster, more modern Python package manager)

```bash
# Install uv (if not already installed)
# Windows:
curl -LsSf https://astral.sh/uv/install.ps1 | powershell
# macOS/Linux:
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone the project
git clone
cd xiaohongshu-automation

# Method 1: use uv (recommended)
uv venv                    # create a virtual environment
uv sync                    # install all dependencies

# Method 2: traditional approach
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

### One-click dev environment setup

#### Method 1: convenience script (Windows)

```bash
# Set up the dev environment with one click
scripts\setup_dev.bat
```

#### Method 2: quick test with uvx (recommended)

No need to clone the code; test the latest version directly:

```bash
# Quickly start the FastAPI server (from PyPI)
uvx --from xiaohongshu-automation xhs-server

# Quickly start the MCP server (from PyPI)
uvx --from xiaohongshu-automation xhs-mcp

# Run the latest dev version directly from the Git repo
uvx --from git+https://github.com/A1721/xiaohongshu-automation.git xhs-server

# Test a specific version
uvx --from xiaohongshu-automation==1.0.0 xhs-server
```

#### Method 3: traditional dev environment

```bash
# Clone the project
git clone
cd xiaohongshu-automation

# Use uv (recommended)
uv venv                    # create a virtual environment
uv sync                    # install all dependencies

# Or the traditional way
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

### Building and publishing

```bash
# Build the package
uv build

# Test the locally built package with uvx
uvx --from ./dist/xiaohongshu_automation-1.0.0-py3-none-any.whl xhs-server
uvx --from ./dist/xiaohongshu_automation-1.0.0-py3-none-any.whl xhs-mcp

# Publish to PyPI (using the convenience script)
scripts\publish.bat

# Or publish manually
uv pip install twine
twine upload dist/*

# Test publishing to TestPyPI
twine upload --repository testpypi dist/*

# Test the TestPyPI version with uvx
uvx --index-url https://test.pypi.org/simple/ --from xiaohongshu-automation xhs-server
```

### 2. Start the services

**Important**: both services must be started in order

```bash
# Step 1: start the FastAPI backend service and log in to Xiaohongshu by scanning the QR code
python main.py

# Step 2: start the MCP server
python mcp_server.py
```

### 3. Configure the AI client

Configure the connection to the local MCP server in an MCP-capable AI client.

## Installing a Release Version

### Method 1: traditional install

If the project is published on PyPI, users can install it directly:

```bash
pip install xiaohongshu-automation
```

### Method 2: use uvx (recommended)

**uvx** is a powerful feature of uv that runs Python packages directly without installing them into the current environment - great for CLI tools and one-off tasks.

#### Advantages
- **No install needed**: run packages directly without polluting the current environment
- **Automatic management**: automatically creates temporary environments and manages dependencies
- **Isolated execution**: each run happens in its own environment
- **Cache optimization**: environments are cached automatically, so subsequent runs are faster

#### Usage

```bash
# Run the FastAPI server directly
uvx --from xiaohongshu-automation xhs-server

# Run the MCP server directly
uvx --from xiaohongshu-automation xhs-mcp

# Run a specific script (if provided by the package)
uvx --from xiaohongshu-automation --help

# Run a specific version
uvx --from xiaohongshu-automation==1.0.0 xhs-server

# Run from TestPyPI (test version)
uvx --index-url https://test.pypi.org/simple/ --from xiaohongshu-automation xhs-server
```

#### For developers using uvx

```bash
# Run from a locally built package
uvx --from ./dist/xiaohongshu_automation-1.0.0-py3-none-any.whl xhs-server

# Run directly from a Git repo
uvx --from git+https://github.com/A1721/xiaohongshu-automation.git xhs-server
```

### Method 3: install from source

```bash
# Clone the project
git clone
cd xiaohongshu-automation

# Install with uv
uv pip install -e .

# Or install with pip
pip install -e .
```

## Troubleshooting

### Common issue: MCP call succeeds but AI reports failure

**Symptom**: the MCP service call succeeds, but the AI execution result shows failure
**Cause**: the FastAPI backend service is not running
**Fix**: run `python main.py` to start the backend service

See TIMEOUT_TROUBLESHOOTING.md for the detailed troubleshooting guide.

### Quick diagnosis

```bash
# Run the diagnostic tool
python test_timeout_improvements.py

# Or call it through MCP
xiaohongshu_timeout_diagnostic
```

## Features

### Core Tools

1. **xiaohongshu_publish** - publish content to Xiaohongshu
   - Supports multiple images (1-18)
   - Content quality analysis and optimization suggestions
   - Smart topic tags and @user detection

2. **xiaohongshu_get_comments** - get comment analysis
   - Sentiment analysis and keyword extraction
   - Comment statistics and engagement analysis

3. **xiaohongshu_reply_comments** - batch reply to comments
   - Smart reply suggestions and content optimization
   - Batch processing and tone adjustment

4. **xiaohongshu_monitor** - system monitoring
   - Health score
   - Service status checks
   - History analysis

5. **xiaohongshu_timeout_diagnostic** - timeout diagnosis (new)
   - Network connectivity tests
   - Performance analysis
   - Configuration suggestions

### Resources

- **xiaohongshu://monitor/status** - real-time monitoring status
- **xiaohongshu://posts/history** - publishing history
- **xiaohongshu://tools/info** - tool info overview

### Prompt Templates

- **xiaohongshu_content_template** - content creation template
- **xiaohongshu_reply_template** - comment reply template
- **xiaohongshu_optimization_tips** - optimization suggestion template

## API Endpoints

### Publish content
```http
POST /publish
Content-Type: application/json

{
  "pic_urls": ["https://example.com/image1.jpg"],
  "title": "Title",
  "content": "Content text"
}
```

### Get comments (not yet complete)
```http
GET /get_comments?url=https://www.xiaohongshu.com/explore/xxxxx
```

### Reply to comments (not yet complete)
```http
POST /post_comments?url=https://www.xiaohongshu.com/explore/xxxxx
Content-Type: application/json

{
  "comment_id_1": ["reply content 1", "reply content 2"],
  "comment_id_2": ["reply content 3"]
}
```

## Configuration Options

### Timeout configuration

```bash
# Basic timeout settings
export FASTAPI_TIMEOUT=30          # default timeout
export PUBLISH_TIMEOUT=60          # publish operation timeout
export COMMENTS_TIMEOUT=30         # comment operation timeout
export MONITOR_TIMEOUT=15          # monitor operation timeout
export HEALTH_CHECK_TIMEOUT=5      # health check timeout

# Retry mechanism
export ENABLE_AUTO_RETRY=true      # enable automatic retry
export MAX_RETRIES=3               # max retry count
export RETRY_DELAY=2               # retry interval (seconds)

# Logging config
export LOG_LEVEL=INFO              # log level
export DETAILED_ERROR_MSG=true     # detailed error messages
```

### Example environment configurations

#### Local development
```bash
export FASTAPI_TIMEOUT=30
export PUBLISH_TIMEOUT=60
export ENABLE_AUTO_RETRY=true
export MAX_RETRIES=3
```

#### Production
```bash
export FASTAPI_TIMEOUT=60
export PUBLISH_TIMEOUT=120
export ENABLE_AUTO_RETRY=true
export MAX_RETRIES=5
export RETRY_DELAY=3
```

## Testing

### Running the test suites

```bash
# Basic functionality tests
python test_mcp_server.py

# Timeout and diagnostic tests
python test_timeout_improvements.py

# Publish-specific tests
python test_publish_fix.py
```

### Performance monitoring

```bash
# Enable verbose logging
export LOG_LEVEL=DEBUG
python mcp_server.py

# Monitor system status
xiaohongshu_monitor
```

## Project Structure

```
xiaohongshu-automation/
├── main.py                     # FastAPI main service
├── mcp_server.py              # MCP server
├── config.py                  # Configuration management
├── adapters/
│   └── xiaohongshu_adapter.py # Service adapter
├── tools/                     # MCP tools
│   ├── base_tool.py          # Base tool class
│   ├── publish_tool.py       # Publish tool
│   ├── comments_tool.py      # Comments tool
│   ├── monitor_tool.py       # Monitor tool
│   ├── timeout_diagnostic_tool.py # Diagnostic tool (new)
│   └── tool_manager.py       # Tool manager
├── xiaohongshu_tools.py       # Core functionality module
├── unti.py                    # Utility functions
├── requirements.txt           # Python dependencies
├── TIMEOUT_TROUBLESHOOTING.md # Troubleshooting guide (new)
└── README.md                  # Project documentation
```

## Dependencies

- Python 3.8+
- FastAPI - web framework
- MCP (Model Context Protocol) - AI integration protocol
- httpx - HTTP client
- pydantic - data validation
- selenium - browser automation
- requests - HTTP requests

## Version History

### v1.0.0 (2025-06-01)
- Basic MCP server implementation
- Core tool set (publish, comments, monitor)
- Smart retry and timeout configuration
- Timeout diagnostic tool
- Detailed troubleshooting guide

## Contributing

Issues and Pull Requests are welcome to improve the project.

## License

MIT License

---

## Getting Help

If you run into problems:

1. **Check the troubleshooting guide**: TIMEOUT_TROUBLESHOOTING.md
2. **Run the diagnostic tool**: `python test_timeout_improvements.py`
3. **Check the service status**: make sure `python main.py` is running
4. **Check the logs**: enable `LOG_LEVEL=DEBUG` for details

**Quick checklist**:
- [ ] FastAPI service started (`python main.py`)
- [ ] MCP server started (`python mcp_server.py`)
- [ ] http://localhost:8000/docs is accessible
- [ ] AI client is configured with the MCP connection

---

*Last updated: 2025-06-01*

**Official site: ** [https://pypi.org/project/xiaohongshu-automation/](https://pypi.org/project/xiaohongshu-automation/)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `browser`, `media`
- Tags: `art and culture`, `browser automation`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx --from xiaohongshu-automation`
- Args: `xhs-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/parsons0503-xiaohongshu-automation.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
