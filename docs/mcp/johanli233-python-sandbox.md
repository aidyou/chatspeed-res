---
title: "python-mcp-sandbox"
description: "An interactive Python code execution environment that allows users and LLMs to safely execute Python code and install packages in isolated Docker containers."
---

# python-mcp-sandbox

An interactive Python code execution environment that allows users and LLMs to safely execute Python code and install packages in isolated Docker containers.

# MCP Sandbox

   alt="MCP Sandbox Logo" width="120" height="120" />

[![Python Version](/mcp-assets/5142151145d2dd1ac338bb460f878742.svg)](https://www.python.org/downloads/release/python-3120/)
[![License](/mcp-assets/fa73b4786cfc281bb30f39f895ada091.svg)](https://opensource.org/licenses/Apache-2.0)
[![UV](/mcp-assets/27d92979939e6529ba512e29790f15c7.svg)](https://github.com/astral-sh/uv)
[![MCP](/mcp-assets/4d2db09f8c33956073a63b9d84264fc0.svg)](https://github.com/estitesc/mission-control-link)

[中文文档](https://github.com/JohanLi233/python-mcp-sandbox/blob/HEAD/README_zh.md) | English

Python MCP Sandbox is an interactive Python code execution tool that allows users and LLMs to safely execute Python code and install packages in isolated Docker containers.

## Features

- 🐳 **Docker Isolation**: Securely run Python code in isolated Docker containers
- 📦 **Package Management**: Easily install and manage Python packages
- 📊 **File Generation**: Support for generating files and accessing them via web links

## Installation

```bash
# Clone the repository
git clone https://github.com/JohanLi233/python-mcp-sandbox.git
cd python-mcp-sandbox

uv venv
uv sync

# Start the server
uv run main.py
```

The default SSE endpoint is http://localhost:8000/sse, and you can interact with it via the MCP Inspector through SSE or any other client that supports SSE connections.

### Available Tools

1. **create_sandbox**: Creates a new Python Docker sandbox and returns its ID for subsequent code execution and package installation
2. **list_sandboxes**: Lists all existing sandboxes (Docker containers) for reuse
3. **execute_python_code**: Executes Python code in a specified Docker sandbox
4. **install_package_in_sandbox**: Installs Python packages in a specified Docker sandbox
5. **check_package_installation_status**: Checks if a package is installed or installation status in a Docker sandbox
6. **execute_terminal_command**: Executes a terminal command in the specified Docker sandbox. Parameters: `sandbox_id` (string), `command` (string). Returns `stdout`, `stderr`, `exit_code`.
7. **upload_file_to_sandbox**: Uploads a local file to the specified Docker sandbox. Parameters: `sandbox_id` (string), `local_file_path` (string), `dest_path` (string, optional, default: `/app/results`).

## Project Structure

```
python-mcp-sandbox/
├── main.py                    # Application entry point
├── requirements.txt           # Project dependencies
├── Dockerfile                 # Docker configuration for Python containers
├── results/                   # Directory for generated files
├── mcp_sandbox/               # Main package directory
│   ├── __init__.py
│   ├── models.py              # Pydantic models
│   ├── api/                   # API related components
│   │   ├── __init__.py
│   │   └── routes.py          # API route definitions
│   ├── core/                  # Core functionality
│   │   ├── __init__.py
│   │   ├── docker_manager.py  # Docker container management
│   │   └── mcp_tools.py       # MCP tools
│   └── utils/                 # Utilities
│       ├── __init__.py
│       ├── config.py          # Configuration constants
│       ├── file_manager.py    # File management
│       └── task_manager.py    # Periodic task management
└── README.md                  # Project documentation
```

## Example Prompt
```
I've configured a Python code execution sandbox for you. You can run Python code using the following steps:

1. First, use the "list_sandboxes" tool to view all existing sandboxes (Docker containers).
   - You can reuse an existing sandbox_id if a sandbox exists, do not create a new one.
   - If you need a new sandbox, use the "create_sandbox" tool.
   - Each sandbox is an isolated Python environment, and the sandbox_id is required for all subsequent operations.

2. If you need to install packages, use the "install_package_in_sandbox" tool
   - Parameters: sandbox_id and package_name (e.g., numpy, pandas)
   - This starts asynchronous installation and returns immediately with status

3. After installing packages, you can check their installation status using the "check_package_installation_status" tool
   - Parameters: sandbox_id and package_name (name of the package to check)
   - If the package is still installing, you need to check again using this tool

4. Use the "execute_python_code" tool to run your code
   - Parameters: sandbox_id and code (Python code)
   - Returns output, errors and links to any generated files
   - All generated files are stored inside the sandbox, and file_links are direct HTTP links for inline viewing

Example workflow:
- Use list_sandboxes to check for available sandboxes, if no available sandboxes, use create_sandbox to create a new one → Get sandbox_id
- Use install_package_in_sandbox to install necessary packages (like pandas, matplotlib), with the sandbox_id parameter
- Use check_package_installation_status to verify package installation, with the same sandbox_id parameter
- Use execute_python_code to run your code, with the sandbox_id parameter

Code execution happens in a secure sandbox. Generated files (images, CSVs, etc.) will be provided as direct HTTP links, which can viewed inline in the browser.

Remember not to use plt.show() in your Python code. For visualizations:
- Save figures to files using plt.savefig() instead of plt.show()
- For data, use methods like df.to_csv() or df.to_excel() to save as files
- All saved files will automatically appear as HTTP links in the results, which you can open or embed directly.
```

## MCP Example Config

Below is an example config:

```json
{
  "mcpServers": {
    "mcp-sandbox": {
      "type": "sse",
      "serverUrl": "http://localhost:8000/sse"
    }
  }
}
```

Modify the `serverUrl` as needed for your environment.

**Official site: ** [https://github.com/JohanLi233/python-mcp-sandbox](https://github.com/JohanLi233/python-mcp-sandbox)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `developer tools`, `virtualization`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y supergateway --sse http://localhost:8000/sse`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/johanli233-python-sandbox.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
