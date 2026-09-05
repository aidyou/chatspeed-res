---
title: "Python MCP 沙盒环境"
description: "一个交互式的Python代码执行环境，允许用户和大型语言模型在隔离的Docker容器中安全地执行Python代码和安装包。"
---

# Python MCP 沙盒环境

一个交互式的Python代码执行环境，允许用户和大型语言模型在隔离的Docker容器中安全地执行Python代码和安装包。

# MCP Sandbox

   alt="MCP Sandbox Logo" width="120" height="120" />

[![Python Version](/mcp-assets/5142151145d2dd1ac338bb460f878742.svg)](https://www.python.org/downloads/release/python-3120/)
[![License](/mcp-assets/fa73b4786cfc281bb30f39f895ada091.svg)](https://opensource.org/licenses/Apache-2.0)
[![UV](/mcp-assets/27d92979939e6529ba512e29790f15c7.svg)](https://github.com/astral-sh/uv)
[![MCP](/mcp-assets/4d2db09f8c33956073a63b9d84264fc0.svg)](https://github.com/estitesc/mission-control-link)

[中文文档](https://github.com/JohanLi233/python-mcp-sandbox/blob/HEAD/README_zh.md) | English

Python MCP Sandbox 是一个交互式的 Python 代码执行工具，允许用户和大语言模型在隔离的 Docker 容器中安全地执行 Python 代码并安装包。

## 功能

- 🐳 **Docker 隔离**：在隔离的 Docker 容器中安全地运行 Python 代码
- 📦 **包管理**：轻松安装和管理 Python 包
- 📊 **文件生成**：支持生成文件并通过网页链接访问

## 安装

```bash
# Clone the repository
git clone https://github.com/JohanLi233/python-mcp-sandbox.git
cd python-mcp-sandbox

uv venv
uv sync

# Start the server
uv run main.py
```

默认的 SSE 端点是 [http://localhost:8000/sse](http://localhost:8000/sse)，你可以通过 MCP Inspector 或任何支持 SSE 连接的客户端与它进行交互。

### 可用工具

1. **create_sandbox**: 创建一个新的 Python Docker 沙箱，并返回其 ID 以供后续代码执行和包安装使用
2. **list_sandboxes**: 列出所有现有的沙箱（Docker 容器）以便重用
3. **execute_python_code**: 在指定的 Docker 沙箱中执行 Python 代码
4. **install_package_in_sandbox**: 在指定的 Docker 沙箱中安装 Python 包
5. **check_package_installation_status**: 检查 Docker 沙箱中某个包是否已安装或其安装状态
6. **execute_terminal_command**: 在指定的 Docker 沙箱中执行终端命令。参数：`sandbox_id` (字符串), `command` (字符串)。返回 `stdout`, `stderr`, `exit_code`。
7. **upload_file_to_sandbox**: 将本地文件上传到指定的 Docker 沙箱。参数：`sandbox_id` (字符串), `local_file_path` (字符串), `dest_path` (字符串, 可选, 默认: `/app/results`)。

## 项目结构

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

## 示例提示
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

## MCP 示例配置

以下是一个示例配置：

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

根据你的环境需要修改 `serverUrl`。

**官方网站：** [https://github.com/JohanLi233/python-mcp-sandbox](https://github.com/JohanLi233/python-mcp-sandbox)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`, `virtualization`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y supergateway --sse http://localhost:8000/sse`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/johanli233-python-sandbox.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
