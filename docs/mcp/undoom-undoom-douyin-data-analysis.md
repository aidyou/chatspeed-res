---
title: "undoom-douyin-data-analysis"
description: "The MCP (Model Context Protocol) server, developed based on the original Douyin data analysis tool, provides functions for collecting, analyzing, and exporting Douyin video and user data. 🎉 It has now…"
---

# undoom-douyin-data-analysis

The MCP (Model Context Protocol) server, developed based on the original Douyin data analysis tool, provides functions for collecting, analyzing, and exporting Douyin video and user data. 🎉 It has now…

# Douyin Data Analysis MCP Server

[![PyPI version](/mcp-assets/dec8b35f184274331a6b0bde60435e1d.svg)](https://badge.fury.io/py/undoom-douyin-data-analysis)
[![Python 3.13+](/mcp-assets/2280fa7946855f272d1788d76d128a9e.svg)](https://www.python.org/downloads/)

An MCP (Model Context Protocol) server developed based on the original Douyin data analysis tool, providing functions for collecting, analyzing, and exporting Douyin video and user data.

**🎉 Now published on PyPI, ready to install and use!**

## Features

### Data Collection
- **Video Search**: Search Douyin videos by keyword, collecting information such as title, author, likes, and comments.
- **User Search**: Search Douyin users by keyword, collecting information such as username, Douyin ID, followers, and likes received.
- **Custom Parameters**: Support setting scroll count and delay time to control the scale and speed of data collection.

### Data Analysis
- **Interaction Data Analysis**: Analyze interaction data such as likes, comments, and shares for videos, providing statistical reports.
- **Content Length Analysis**: Analyze the distribution of video title lengths to understand content characteristics.
- **Keyword Analysis**: Use Chinese word segmentation technology to analyze high-frequency words and discover hot topics.

### Data Export
- **Multiple Formats Supported**: Supports export in JSON, Excel, and CSV formats.
- **Categorized Export**: Can choose to export video data, user data, or all data.
- **Timestamps**: Automatically adds timestamps to avoid file overwriting.

## Installation and Configuration

### Method One: Install from PyPI (Recommended)

1. **Direct Installation**:
   bash
   pip install undoom-douyin-data-analysis
   

2. **Configure MCP Client**:
   Add the following configuration to your MCP client configuration file:
   json
   {
     "mcpServers": {
       "undoom-douyin-data-analysis": {
         "command": "uvx",
         "args": [
           "--index-url",
           "https://pypi.tuna.tsinghua.edu.cn/simple",
           "--from",
           "undoom-douyin-data-analysis",
           "undoom-douyin-mcp"
         ]
       }
     }
   }
   

### Method Two: Local Development Installation

1. **Clone Repository**:
   bash
   git clone https://github.com/kk520879/undoom-douyin-data-analysis.git
   cd undoom_Douyin_data_analysis
   

2. **Install Dependencies**:
   bash
   uv sync
   

3. **Run Locally**:
   bash
   uv run undoom-douyin-mcp
   

### Environment Requirements
- Python 3.13+
- Chrome/Chromium browser
- Internet connection (to access Douyin)

## Available Tools

### 1. search_douyin_videos
Searches for Douyin video data.

**Parameters**:
- `keyword` (required): Search keyword
- `scroll_count` (optional): Number of scrolls, default is 10
- `delay` (optional): Delay time per scroll (seconds), default is 2.0

### 2. search_douyin_users
Searches for Douyin user data.

### 3. analyze_interaction_data
Analyzes video interaction data (likes, comments, etc.).

### 4. analyze_content_length
Analyzes the distribution of video title lengths.

### 5. analyze_keywords
Analyzes high-frequency words in video titles.

### 6. export_data
Exports the collected data.

### 7. get_data_summary
Gets a summary of the currently collected data.

### 8. clear_data
Clears the currently collected data.

## Available Resources

### 1. douyin://data/videos
Currently collected video data (JSON format).

### 2. douyin://data/users
Currently collected user data (JSON format).

### 3. douyin://analysis/summary
Summary of data collection and analysis (text format).

## Usage Examples

### Basic Workflow

1. **Search Video Data**:
   Use the `search_douyin_videos` tool to search by keyword.

2. **Analyze Data**:
   Use `analyze_interaction_data` to analyze interaction data.
   Use `analyze_keywords` to analyze high-frequency words.

3. **Export Results**:
   Use `export_data` to export in the specified format.

## Project Information

- **PyPI Package**: [undoom-douyin-data-analysis](https://pypi.org/project/undoom-douyin-data-analysis/)
- **Version**: 0.1.3
- **License**: MIT License
- **Python Version**: 3.13+

## Notes

1. **Network Environment**: Requires access to the Douyin website.2. **Browser Dependency**: Using DrissionPage requires Chrome/Chromium browser
3. **Crawling Frequency**: It is recommended to set an appropriate delay time to avoid overly frequent requests
4. **Compliance**: Please adhere to the terms of service and relevant laws and regulations of Douyin
5. **Data Usage**: The collected data is for learning and research purposes only, do not use it for commercial purposes

## Technical Architecture

- **MCP Protocol**: Implemented based on Model Context Protocol
- **Asynchronous Processing**: Uses asyncio for asynchronous operations
- **Data Parsing**: Uses BeautifulSoup to parse HTML
- **Chinese Word Segmentation**: Uses jieba for Chinese text analysis
- **Data Handling**: Uses pandas for data manipulation and export

**Official site: ** [https://github.com/kk520879/undoom-douyin-data-analysis](https://github.com/kk520879/undoom-douyin-data-analysis)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `research and data`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `--index-url https://pypi.tuna.tsinghua.edu.cn/simple --from undoom-douyin-data-analysis undoom-douyin-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/undoom-undoom-douyin-data-analysis.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
