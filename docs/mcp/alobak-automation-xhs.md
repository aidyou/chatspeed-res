---
title: "automation-xhs"
description: "Xiaohongshu MCP Service, 1. Supports automatic publishing 2. Supports searching for notes 3. Supports analyzing note content 4. Supports multi-account management 5. Supports pre-publishing (publish af…"
---

# automation-xhs

Xiaohongshu MCP Service, 1. Supports automatic publishing 2. Supports searching for notes 3. Supports analyzing note content 4. Supports multi-account management 5. Supports pre-publishing (publish af…

# Xiaohongshu Automation Tool - Simple User Manual

This manual will guide you through the quick setup and usage of the Xiaohongshu automation tool.
Advanced version support (updated to PyPI, ready for use!!!):

1. Multiple accounts (manage multiple accounts, isolated individually, with IP isolation options)
2. Automatic note commenting for traffic generation (supports @mentions)
3. Pre-publishing feature, where AI-generated notes can be added to the pre-publish interface, reviewed manually, and then published directly.

Tested and confirmed working on 2025.8.21

## 1. Download Google Chrome and Browser Driver

### Download Google Chrome
1. Visit [Google Chrome Official Website](https://www.google.com/chrome/)
2. Click "Download Chrome" and install it

### Download Browser Driver
1. Open Chrome browser, enter `chrome://version/` to check the version number
2. Visit [ChromeDriver Download Page](https://chromedriver.chromium.org/downloads)
3. Download the corresponding version of ChromeDriver
4. Extract `chromedriver.exe` to a system PATH directory (e.g., `C:\Windows\System32\`)

> **Tip**: Ensure that the ChromeDriver version matches your Chrome browser version

## 2. Install Python

### Windows System
1. Visit [Python Official Website](https://www.python.org/downloads/)
2. Download Python 3.8 or higher
3. During installation, check "Add Python to PATH"

### Verify Installation
Open Command Prompt (CMD) or PowerShell, and type:
bash
python --version

### Install uv Package Manager
bash
# Windows PowerShell
curl -LsSf https://astral.sh/uv/install.ps1 | powershell

## 3. Run Xiaohongshu Automation Service

### Quick Start (Recommended)
Use uvx to run directly without downloading the source code:

bash
# Start FastAPI server
uvx --from xiaohongshu-automation xhs-server

### Startup Steps
1. After running the above command, the system will automatically download dependencies
2. Once the service starts, it will open a browser window
3. **Important**: You need to scan the QR code to log in to your Xiaohongshu account
4. After successful login, the service will run at `http://localhost:8001`

> **Note**: The first run may take some time to download the dependency packages

## 4. Add MCP Configuration

### Configure AI Client
If you are using an AI client that supports MCP (such as Claude Desktop), add the following configuration:

#### Example Configuration for Claude Desktop
Add the following to the Claude Desktop configuration file:

json
{
  "mcpServers": {
    "xiaohongshu-automation": {
      "command": "uvx",
      "args": ["--from", "xiaohongshu-automation", "xhs-mcp"],
      "env": {
        "FASTAPI_URL": "http://localhost:8001"
      }
    }
  }
}

#### Configuration File Location
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

### Start MCP Service
After configuring the AI client, the MCP service will start automatically. You can also test it manually:

bash
uvx --from xiaohongshu-automation xhs-mcp

## ✅ Verify Installation

### Check Service Status
1. Visit `http://localhost:8001/docs` to view the API documentation
2. Try calling Xiaohongshu-related functions in the AI client

### Common Issues
- **ChromeDriver Error**: Ensure the driver version matches the browser version
- **Python Error**: Ensure Python is correctly installed and added to the PATH
- **Network Error**: Check your network connection and ensure access to PyPI

## 🎉 Get Started

After configuration, you can use the following features in the AI client:
- Post content to Xiaohongshu
- Search and analyze notes
- Retrieve and reply to comments
- System monitoring and diagnostics

---

**Technical Support**: If you encounter any issues, please contact WeChat ID: vasst888
Advanced version support (updated to PyPI, ready for use!!!):

1. Multiple accounts (manage multiple accounts, isolated individually, with IP isolation options)
2. Automatic note commenting for traffic generation (supports @mentions)
3. Pre-publishing feature, where AI-generated notes can be added to the pre-publish interface, reviewed manually, and then published directly.

Tested and confirmed working on 2025.8.21

Demo Video:
96 Vastt. posted a Xiaohongshu note, come and check it out! 😆 6miBi42Dm1f 😆 http://xhslink.com/m/2IS3575CL6b Copy this message and open the 【Xiaohongshu】App to view the exciting content!

This MCP server is for research purposes only and is prohibited from being used for commercial purposes.

**Official site: ** [https://pypi.org/project/xiaohongshu-automation/](https://pypi.org/project/xiaohongshu-automation/)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `browser`, `media`
- Tags: `browser automation`, `entertainment and media`, `小红书`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx --from xiaohongshu-automation`
- Args: `xhs-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/alobak-automation-xhs.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
