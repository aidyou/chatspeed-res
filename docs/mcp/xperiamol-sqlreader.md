---
title: "SQLReader"
description: "NaturalSQL MCP Server This is a natural language SQL query server based on the Model Context Protocol (MCP). Features - 🧠 Natural language to SQL query conversion - 🔗 Dynamic database connection confi…"
---

# SQLReader

NaturalSQL MCP Server This is a natural language SQL query server based on the Model Context Protocol (MCP). Features - 🧠 Natural language to SQL query conversion - 🔗 Dynamic database connection confi…

# NaturalSQL MCP Server

This is a natural language SQL query server based on the Model Context Protocol (MCP).

## Features

- 🧠 Natural language to SQL query conversion
- 🔗 Dynamic database connection configuration
- 🛡️ SQL security checks (blocking dangerous operations)
- 📊 Result data table display
- 🌐 Web interface based on Gradio

## Install Dependencies

bash
pip install -r requirements.txt

## Startup Methods

### Method 1: Direct Startup
bash
python app.py

### Method 2: Using Batch File (Windows)
bash
start_mcp_server.bat

## MCP Configuration Files

- `mcp_config.json` - Simple MCP server configuration
- `mcp_server_config.json` - Detailed MCP server configuration, including tool definitions

## Usage Instructions

1. **Configure Database Connection**
   - Enter PostgreSQL connection information in the "Database Configuration" tab
   - Click "Test Connection" to verify the connection
   - Click "Update Configuration" to apply the configuration and load the database schema

2. **Execute Natural Language Query**
   - Switch to the "SQL Query" tab
   - Enter a natural language query, for example: "Show the total order amount for July 2023"
   - Click "Execute Query" to get the results

## Security Features

The system automatically detects and blocks the following dangerous SQL operations:
- DROP
- DELETE  
- TRUNCATE
- UPDATE
- INSERT

## Environment Requirements

- Python 3.8+
- PostgreSQL database
- OpenAI API key (configure in config.py)

## Configure OpenAI API

Set your OpenAI API key in the `config.py` file:

python
openai_api_key = "your-openai-api-key-here"

**Official site: ** [https://www.modelscope.cn/studios/xperiamol/SQLReader](https://www.modelscope.cn/studios/xperiamol/SQLReader)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `memory`, `files`
- Tags: `file systems`, `knowledge and memory`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `mcp-remote https://xperiamol-sqlreader.ms.show/gradio_api/mcp/sse --transport sse-only`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/xperiamol-sqlreader.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
