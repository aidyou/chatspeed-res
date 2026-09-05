---
title: "MCP PDF工具"
description: "使用PyPDF2的MCP可以实现以下功能： • 合并PDF（merge-pdfs） • 提取页面（extract-pages） • 搜索PDF（search-pdfs） • 按顺序合并PDF（merge-pdfs-ordered，按照用户指定的顺序合并） • 查找相关PDF（find-related-pdfs，通过正则表达式提取文本以查找相关的PDF文件）"
---

# MCP PDF工具

使用PyPDF2的MCP可以实现以下功能： • 合并PDF（merge-pdfs） • 提取页面（extract-pages） • 搜索PDF（search-pdfs） • 按顺序合并PDF（merge-pdfs-ordered，按照用户指定的顺序合并） • 查找相关PDF（find-related-pdfs，通过正则表达式提取文本以查找相关的PDF文件）

# WORK IN PROGRESS - USE WITH CAUTION - Windows:

# MCP PDF 工具服务器

一个提供 PDF 操作工具的 MCP（模型上下文协议）服务器。此服务器允许 LLM 通过模型上下文协议执行诸如合并 PDF 和提取页面等操作。

## 功能

- 将多个 PDF 文件合并为一个 PDF
- 按用户指定顺序将多个 PDF 文件合并为一个 PDF
- 从 PDF 文件中提取特定页面
- 搜索 PDF *文件系统搜索或 Everything 搜索比这更有效*
- 根据目标输入 PDF 的文本提取和正则表达式模式匹配查找（并合并）相关 PDF

## 安装

1. 克隆此仓库
2. 
```bash
cd mcp-pdf-tools

# Create and activate virtual environment
uv venv
.venv\Scripts\activate

# Install the package
uv pip install -e .
```

## 与 Claude Desktop 一起使用

将以下内容添加到您的 Claude Desktop 配置文件 (claude_desktop_config.json) 中：

```json
{
    "mcpServers": {
        "pdf-tools": {
            "command": "uv",
            "args": [
                "--directory",
                "PATH_TO\\mcp-pdf-tools",
                "run",
                "pdf-tools"
            ]
        }
    }
}
```

**官方网站：** [https://github.com/hanweg/mcp-pdf-tools](https://github.com/hanweg/mcp-pdf-tools)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`productivity`
- 标签：`other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`--directory PATH_TO\mcp-pdf-tools run pdf-tools`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/hanweg-pdf-tools.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
