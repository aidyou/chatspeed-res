---
title: "arXiv-MCP服务器工具"
description: "一个MCP服务器，允许Claude AI通过自建的本地服务器高效地搜索、浏览和比较arXiv论文。"
---

# arXiv-MCP服务器工具

一个MCP服务器，允许Claude AI通过自建的本地服务器高效地搜索、浏览和比较arXiv论文。

# 🧠 arXiv Research Assistant MCP 服务器

该项目是一个MCP（模型上下文协议）服务器，用于与庞大的arXiv.org论文数据库进行交互。

它允许像**Claude AI**这样的客户端高效地搜索、探索和比较arXiv论文——所有这些都通过一个自定义构建的本地服务器实现。该服务器使用**Python**语言和**FastMCP**框架构建，并采用**uv**进行轻量级包管理。

---

## ✨ 功能特点

- **🔍 基于关键词的论文搜索**  
  通过关键词搜索arXiv论文，并可按相关性或最新发表时间排序。

- **📚 按类别获取最新论文**  
  指定一个arXiv类别代码（例如 `cs.AI`, `math.AP`），以获取该领域内的最新论文。

- **📄 论文详情查询**  
  使用论文的arXiv ID获取详细元数据：标题、作者、摘要、类别、DOI、PDF链接等更多信息。

- **🧑‍🔬 基于作者的论文搜索**  
  获取特定作者发表的所有论文列表。

- **📊 趋势分析（实验性）**  
  根据某一类别下的最近论文概览热门关键词或主题（当前使用模拟数据）。

- **📝 摘要提示生成器**  
  动态生成帮助大型语言模型更有效地总结选定论文的提示。

- **🆚 比较提示生成器**  
  提供两个论文ID以生成结构化的提示来比较它们的内容。

---

## 🛠️ 技术栈

- Python 3.11+
- [FastMCP](https://github.com/modelcontextprotocol/fastmcp)
- uv（用于依赖项及环境管理）
- requests（用于API通信）
- xml.etree.ElementTree（用于解析XML响应）

---

## 🚀 快速开始

### 1. 从PyPI安装
```bash
pip install arxiv-paper-mcp
# or with uv
uv install arxiv-paper-mcp
```

### 🔧 2. 克隆仓库（开发用途）
```bash
git clone https://github.com/daheepk/arxiv-mcp-server.git
cd arxiv-mcp-server
```

### 🔧 3. 安装依赖项（开发用途）

使用`uv`以可编辑模式安装所有依赖项：

```bash
uv pip install -e .
```

## ⚙️ 如何运行

### ▶️ 运行服务器（本地）

```bash
uv run mcp dev arxiv_mcp/server.py
```

## 🔌 与Claude配合使用

若要将此MCP服务器与Claude一起使用，请向Claude的MCP设置中添加以下JSON配置：

```json
{
  "arXivPaper": {
    "command": "uv",
    "args": [
      "run",
      "--with",
      "arxiv-paper-mcp>=0.1.0",
      "arxiv-mcp"
    ]
  }
}
```

## 项目结构
```
arxiv-mcp-server/
├── arxiv_mcp/              # Main package
│   ├── __init__.py
│   ├── app.py              # FastMCP app setup
│   ├── server.py           # Server entry point
│   ├── utils.py            # arXiv API communication logic
│   ├── resources/          # MCP resources (categories, authors, etc.)
│   ├── tools/              # MCP tools (search, detail lookup, trends)
│   └── prompts/            # Prompt templates (summarize, compare)
├── pyproject.toml          # Project config & dependencies
└── README.md               # This file
```

**官方网站：** [https://github.com/daheepk/arxiv-mcp-server](https://github.com/daheepk/arxiv-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`research and data`, `search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`tool run arxiv-paper-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/daheepk-arxiv.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
