---
title: "MCP-PDF2Markdown-LLM"
description: "一个将PDF文档导出为Markdown格式的MCP服务器，该格式经过优化，适用于LLM处理。"
---

# MCP-PDF2Markdown-LLM

一个将PDF文档导出为Markdown格式的MCP服务器，该格式经过优化，适用于LLM处理。

# pymupdf4llm-mcp

[![Release](/mcp-assets/b95d01c9e536e0b145783f66c5b61a56.svg)](https://img.shields.io/github/v/release/ai-zerolab/pymupdf4llm-mcp)
[![Build status](/mcp-assets/315ded2d2e09548d7e64cb1ec1bd0c55.svg)](https://github.com/ai-zerolab/pymupdf4llm-mcp/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](/mcp-assets/41152979705a66ad9c096b25277fbfe9.svg)](https://codecov.io/gh/ai-zerolab/pymupdf4llm-mcp)
[![Commit activity](/mcp-assets/40f4dbd4ced8845c945315127dbf74d8.svg)](https://img.shields.io/github/commit-activity/m/ai-zerolab/pymupdf4llm-mcp)
[![License](/mcp-assets/3558c36785ba77f4575ce643a3a48f2a.svg)](https://img.shields.io/github/license/ai-zerolab/pymupdf4llm-mcp)

pymupdf4llm 的 MCP 服务器，最适合将 PDF 导出为 Markdown 以供 LLM 使用。

- **Github 仓库**: 
- **文档** 

## 快速开始

运行以下命令来启动 MCP 服务器：

```bash
uvx pymupdf4llm-mcp@latest stdio # stdio mode
# or
uvx pymupdf4llm-mcp@latest sse # sse mode
```

配置你的光标/windsurf/... 和其他 MCP 客户端到此服务器：

```json
{
  "mcpServers": {
    "pymupdf4llm-mcp": {
      "command": "uvx",
      "args": [
        "pymupdf4llm-mcp@latest",
        "stdio"
      ],
      "env": {}
    }
  }
}
```

**官方网站：** [https://github.com/ai-zerolab/pymupdf4llm-mcp](https://github.com/ai-zerolab/pymupdf4llm-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`files`
- 标签：`file systems`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`pymupdf4llm-mcp@latest stdio`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/ai-zerolab-pymupdf4llm.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
