---
title: "MCPWeChatOfficialAccounts"
description: "MCP WeChat Official Account Crawler A WeChat official account article crawler system built on the FastMCP framework, enabling AI agents to directly access and analyze WeChat official account content…"
---

# MCPWeChatOfficialAccounts

MCP WeChat Official Account Crawler A WeChat official account article crawler system built on the FastMCP framework, enabling AI agents to directly access and analyze WeChat official account content…

# MCP WeChat Official Account Crawler

[![Python](/mcp-assets/d59218ebaf72462fc74fe3c1ee52295b.svg)](https://python.org)
[![MCP](/mcp-assets/c56f5f4d83b01dc20d77e4e6b62b8d82.svg)](https://github.com/modelcontextprotocol)
[![FastMCP](/mcp-assets/8bb5e1d955292db8ba472ab7db933f7d.svg)](https://github.com/jlowin/fastmcp)
![License](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)

A WeChat official account article crawler system built on the **FastMCP** framework, enabling AI agents to directly access and analyze WeChat official account content. Through the MCP (Model Context Protocol) standard, seamless integration between AI agents and Selenium crawlers is achieved.

## 🎯 Project Background

When using AI platforms or agents, we found that these agents could not directly access the content of WeChat official account articles. To solve this problem, we developed this MCP-protocol-based crawler service, allowing AI agents to fetch and analyze the content of WeChat official accounts.

## ✨ Core Features

- 🤖 **FastMCP Framework** - Advanced encapsulation based on FastMCP, simplifying MCP server development
- 🕷️ **Smart Crawler** - Uses Selenium for browser automation, supporting dynamic content scraping
- 🖼️ **Image Processing** - Automatically downloads article images and converts them into local files
- 📊 **Content Analysis** - Provides article statistics, keyword extraction, and other analytical functions
- 🔌 **Standard Protocol** - Fully compatible with MCP 1.0+ specifications, supporting stdio communication
- 🎯 **AI Integration** - Seamless integration with AI agents like Claude Desktop, ChatGPT, etc.
- 💻 **Multiple Interfaces** - Offers Python API and an interactive command-line interface

## 🏗️ System Architecture

```mermaid

graph TB

    subgraph "AI智能体层"

        A[Claude Desktop]

        B[ChatGPT]

        C[其他AI智能体]

    end

    

    subgraph "MCP协议层"

        D[MCP客户端]

        E[stdio通信]

        F[MCP服务器
FastMCP]

    end

    

    subgraph "爬虫引擎层"

        G[Selenium WebDriver]

        H[Chrome浏览器]

        I[图片下载器]

    end

    

    subgraph "数据存储层"

        J[JSON文件]

        K[TXT文件]

        L[图片文件]

    end

    

    A --> D

    B --> D

    C --> D

    D  E

    E  F

    F --> G

    G --> H

    F --> I

    G --> J

    G --> K

    I --> L

```
### 🔧 Core Components

#### 1. FastMCP Server (`server.py`)
- Advanced encapsulation based on the FastMCP framework
- Provides 3 core tools: article crawling, content analysis, and statistical information
- Singleton pattern management for Selenium crawler instances
- Comprehensive error handling and parameter validation

#### 2. MCP Standard Client (`client.py`)
- Implementation of a standard MCP protocol client
- Asynchronous communication and session management
- Interactive command-line interface
- Python API interface

#### 3. Selenium Crawler Engine (`weixin_spider_simple.py`)
- Automation control of Chrome browsers
- Anti-crawling mechanism handling
- Image downloading and format conversion
- Multi-format file saving

## 🚀 Quick Start

### 📋 Environment Requirements

- **Python**: 3.8+ (recommended 3.10+)
- **Browser**: Chrome/Chromium (automatically manages ChromeDriver)
- **System**: macOS/Windows/Linux

### 📦 Installation Steps

```bash

# 1. 克隆项目

git clone 

cd mcp-weixin

# 2. 安装依赖

pip install -r requirements.txt

```
### 🎮 Launch Methods

#### Modular Launch (Recommended)

```bash

# 启动MCP服务器

python -m mcp_weixin_spider

# 启动客户端演示

python -m mcp_weixin_spider.client

```
## 🛠️ MCP Tool Interface

```yaml

{

  "mcpServers": {

    "weixin_spider": {

      "command": "python",

      "args": [

        "本地路径/server.py"

      ],

      "env": {

        "ARTICLES_DIR": "articles",

        "DOWNLOAD_IMAGES": "true",

        "HEADLESS": "true",

        "WAIT_TIME": "10"

      }

    }

  }

}

```

**Official site: ** [https://github.com/ditingdapeng/MCPWeChatOfficialAccounts](https://github.com/ditingdapeng/MCPWeChatOfficialAccounts)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `communication`
- Tags: `communication`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `python`
- Args: `server.py`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/huojunhong-hjh-mcpwechatofficialaccounts.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
