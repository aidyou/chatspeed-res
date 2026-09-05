---
title: "mcp-davie"
description: "MCP Sample Project A powerful interface for extending AI capabilities through remote control, calculations, email operations, knowledge search, and more. Overview MCP (Model Context Protocol) is a pro…"
---

# mcp-davie

MCP Sample Project A powerful interface for extending AI capabilities through remote control, calculations, email operations, knowledge search, and more. Overview MCP (Model Context Protocol) is a pro…

# MCP Sample Project

A powerful interface for extending AI capabilities through remote control, calculations, email operations, knowledge search, and more.

## Overview

MCP (Model Context Protocol) is a protocol that allows servers to expose tools that can be invoked by language models. Tools enable models to interact with external systems, such as querying databases, calling APIs, or performing computations. Each tool is uniquely identified by a name and includes metadata describing its schema.

## Features

- 🔌 Bidirectional communication between AI and external tools
- 🔄 Automatic reconnection with exponential backoff
- 📊 Real-time data streaming
- 🛠️ Easy-to-use tool creation interface
- 🔒 Secure WebSocket communication

## Quick Start

1. Install dependencies:
bash
pip install -r requirements.txt

2. Set up environment variables:
bash
export MCP_ENDPOINT=

Windows
bash
$env:MCP_ENDPOINT = "wss://api.xiaozhi.me/mcp/?token=eyJhbGciOiJFUzI1N..."

3. Run the calculator example:
bash
python mcp_pipe.py calculator.py

## Project Structure

- `mcp_pipe.py`: Main communication pipe that handles WebSocket connections and process management
- `calculator.py`: Example MCP tool implementation for mathematical calculations
- `requirements.txt`: Project dependencies

## Creating Your Own MCP Tools

Here's a simple example of creating an MCP tool:

python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("YourToolName")

@mcp.tool()
def your_tool(parameter: str) -> dict:
    """Tool description here"""
    # Your implementation
    return {"success": True, "result": result}

if __name__ == "__main__":
    mcp.run(transport="stdio")

## Use Cases

- Mathematical calculations
- Email operations
- Knowledge base search
- Remote device control
- Data processing
- Custom tool integration

## Requirements

- Python 3.7+
- websockets>=11.0.3
- python-dotenv>=1.0.0
- mcp>=1.8.1
- pydantic>=2.11.4

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to all contributors who have helped shape this project
- Inspired by the need for extensible AI capabilities

**Official site: ** [https://www.modelscope.cn/mcp](https://www.modelscope.cn/mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `other`, `file systems`, `art and culture`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `python`
- Args: `E:\mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/daviekong-davie.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
