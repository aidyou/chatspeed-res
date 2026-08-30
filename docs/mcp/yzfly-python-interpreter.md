---
title: "MCP-Py"
description: "一种模型上下文协议服务器，允许大型语言模型与Python环境交互、执行代码以及在指定的工作目录内管理文件。"
---

# MCP-Py

一种模型上下文协议服务器，允许大型语言模型与Python环境交互、执行代码以及在指定的工作目录内管理文件。

# MCP Python 解释器

一个 Model Context Protocol (MCP) 服务器，允许大型语言模型（LLMs）与 Python 环境交互，读写文件，执行 Python 代码，并管理开发工作流。

## 特性

- **环境管理**：列出并使用不同的 Python 环境（系统和 conda）
- **代码执行**：在任何可用环境中运行 Python 代码或脚本
- **包管理**：列出已安装的包并安装新的包
- **文件操作**：
  - 读取任意类型的文件（文本、源代码、二进制）
  - 写入文本和二进制文件
- **Python 提示**：常见 Python 任务模板，如函数创建和调试

## 安装

您可以使用 pip 安装 MCP Python 解释器：

```bash
pip install mcp-python-interpreter
```

或者使用 uv：

```bash
uv install mcp-python-interpreter
```

## 与 Claude Desktop 一起使用

1. 安装 [Claude Desktop](https://claude.ai/download)
2. 打开 Claude Desktop，点击菜单，然后选择设置
3. 转到开发者选项卡并点击“编辑配置”
4. 将以下内容添加到您的 `claude_desktop_config.json` 中：

```json
{
  "mcpServers": {
    "mcp-python-interpreter": {
        "command": "uvx",
        "args": [
            "mcp-python-interpreter",
            "--dir",
            "/path/to/your/work/dir",
            "--python-path",
            "/path/to/your/python"
        ],
        "env": {
            "MCP_ALLOW_SYSTEM_ACCESS": 0
        },
    }
  }
}
```

对于 Windows：

```json
{
  "mcpServers": {
    "python-interpreter": {
      "command": "uvx",
      "args": [
        "mcp-python-interpreter",
        "--dir",
        "C:\\path\\to\\your\\working\\directory",
        "--python-path",
        "/path/to/your/python"
      ],
        "env": {
            "MCP_ALLOW_SYSTEM_ACCESS": 0
        },
    }
  }
}
```

5. 重启 Claude Desktop
6. 您现在应该能在聊天界面中看到 MCP 工具图标

`--dir` 参数是**必需的**，它指定了所有文件将被保存和执行的位置。这有助于通过隔离 MCP 服务器到特定目录来维护安全性。

### 先决条件

- 确保您已经安装了 `uv`。如果没有，请使用以下命令安装：
```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
```
- 对于 Windows：
```powershell
  powershell -ExecutionPolicy Bypass -Command "iwr -useb https://astral.sh/uv/install.ps1 | iex"
```

## 可用工具

Python 解释器提供了以下工具：

### 环境和包管理
- **list_python_environments**：列出所有可用的 Python 环境（系统和 conda）
- **list_installed_packages**：列出特定环境中已安装的包
- **install_package**：在特定环境中安装 Python 包

### 代码执行
- **run_python_code**：在特定环境中执行 Python 代码
- **run_python_file**：在特定环境中执行 Python 文件

### 文件操作
- **read_file**：读取任意类型文件的内容，带有大小和安全限制
  - 支持带语法高亮的文本文件
  - 显示二进制文件的十六进制表示
- **write_file**：创建或覆盖包含文本或二进制内容的文件
- **write_python_file**：特别地创建或覆盖 Python 文件
- **list_directory**：列出目录中的 Python 文件

## 可用资源

- **python://environments**：列出所有可用的 Python 环境
- **python://packages/{env_name}**：列出特定环境中的已安装包
- **python://file/{file_path}**：获取 Python 文件的内容
- **python://directory/{directory_path}**：列出目录中的所有 Python 文件

## 提示

- **python_function_template**: 生成 Python 函数的模板
- **refactor_python_code**: 帮助重构 Python 代码
- **debug_python_error**: 帮助调试 Python 错误

## 示例用法

以下是一些你可以要求 Claude 使用此 MCP 服务器执行的操作示例：

- "显示我系统中所有可用的 Python 环境"
- "在我的 conda-base 环境中运行这段 Python 代码：`print('Hello, world!')`"
- "创建一个名为 'hello.py' 的新 Python 文件，其中包含一个打招呼的函数"
- "读取我的 'data.json' 文件的内容"
- "使用这些设置编写一个新的配置文件..."
- "列出系统 Python 环境中安装的所有包"
- "在我的系统 Python 环境中安装 requests 包"
- "使用这些参数运行 data_analysis.py: --input=data.csv --output=results.csv"

## 文件处理能力

MCP Python 解释器现在支持全面的文件操作：
- 读取最大 1MB 的文本和二进制文件
- 写入文本和二进制文件
- 源代码文件的语法高亮
- 二进制文件的十六进制表示
- 严格的文件路径安全（仅限于工作目录内）

## 安全考虑

此 MCP 服务器可以访问你的 Python 环境和文件系统。关键的安全特性包括：
- 隔离的工作目录
- 文件大小限制
- 防止在工作目录外写入文件
- 显式的覆盖保护

始终要谨慎对待你完全不了解的代码或文件操作。

## 许可证

MIT

**官方网站：** [https://github.com/yzfly/mcp-python-interpreter](https://github.com/yzfly/mcp-python-interpreter)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`files`
- 标签：`developer tools`, `file systems`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`mcp-python-interpreter --dir C:\path\to\your\working\directory --python-path /path/to/your/python`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/yzfly-python-interpreter.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
