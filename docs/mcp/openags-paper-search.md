---
title: "论文搜索"
description: "# 论文搜索 MCP\n\n一个用于从多个来源（包括 arXiv、PubMed、bioRxiv 和 Sci-Hub（可选））搜索和下载学术论文的模型上下文协议 (MCP) 服务器。设计用于与大型语言模型（如 Claude Desktop）无缝集成。"
---

# 论文搜索

# 论文搜索 MCP

一个用于从多个来源（包括 arXiv、PubMed、bioRxiv 和 Sci-Hub（可选））搜索和下载学术论文的模型上下文协议 (MCP) 服务器。设计用于与大型语言模型（如 Claude Desktop）无缝集成。

# 论文搜索 MCP

一个用于从多个来源（包括 arXiv、PubMed、bioRxiv 和 Sci-Hub（可选））搜索和下载学术论文的模型上下文协议 (MCP) 服务器。设计用于与大型语言模型（如
Claude Desktop）无缝集成。

![PyPI](/mcp-assets/6267836e7841a13fc47a93760874d69a.svg) ![License](/mcp-assets/d177f30277cff66d9af1e3c6409e24dc.svg) ![Python](/mcp-assets/405b7b46d001e379991916d79670861b.svg)
[Smithery](https://smithery.ai/server/@openags/paper-search-mcp)

---

## 目录

- [概述](#概述)
- [功能](#功能)
- [安装](#安装)
    - [快速开始](#快速开始)
        - [安装包](#安装包)
        - [配置 Claude Desktop](#配置-claude-desktop)
    - [开发环境](#开发环境)
        - [设置环境](#设置环境)
        - [安装依赖](#安装依赖)
- [贡献](#贡献)
- [演示](#演示)
- [许可证](#许可证)
- [待办事项](#待办事项)

---

## 概述

`paper-search-mcp` 是一个基于 Python 的 MCP 服务器，使用户能够从各种平台搜索和下载学术论文。它提供了搜索论文（例如
`search_arxiv`）和下载 PDF（例如 `download_arxiv`）的工具，非常适合研究人员和 AI 驱动的工作流程。使用 MCP Python SDK 构建，可以与
LLM 客户端（如 Claude Desktop）无缝集成。

---

## 功能

- **多源支持**：从 arXiv、PubMed、bioRxiv 和 Sci-Hub（可选）搜索和下载论文。
- **标准化输出**：通过 `Paper` 类以一致的字典格式返回论文。
- **异步工具**：使用 `httpx` 高效处理网络请求。
- **MCP 集成**：与 MCP 客户端兼容，增强 LLM 上下文。
- **可扩展设计**：通过扩展 `academic_platforms` 模块轻松添加新的学术平台。

---

## 安装

`paper-search-mcp` 可以使用 `uv` 或 `pip` 进行安装。以下是两种方法：一种是快速开始以便立即使用，另一种是详细的开发环境设置。

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@openags/paper-search-mcp) 自动为 Claude Desktop 安装 paper-search-mcp：

```bash
npx -y @smithery/cli install @openags/paper-search-mcp --client claude
```

### 快速开始

对于希望快速运行服务器的用户：

1. **安装包**：
```bash
   uv add paper-search-mcp
```

2. **配置 Claude Desktop**：
   将以下配置添加到 `~/Library/Application Support/Claude/claude_desktop_config.json`（Mac）或
   `%APPDATA%Claudeclaude_desktop_config.json`（Windows）：
```json
   {
   "mcpServers": {
   "paper_search_server": {
   "command": "uv",
   "args": [
   "run",
   "--directory",
   "/path/to/your/paper-search-mcp",
   "-m",
   "paper_search_mcp.server"
   ]
   }
   }
   }
```
   >    注意：将 `/path/to/your/paper-search-mcp` 替换为实际的安装路径。

### 开发环境

对于希望修改代码或贡献的开发者：

1. **设置环境**：
```bash
   # 如果未安装，则安装 uv
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # 克隆仓库
   git clone https://github.com/openags/paper-search-mcp.git
   cd paper-search-mcp

   # 创建并激活虚拟环境
   uv venv
   source .venv/bin/activate  # 在 Windows 上：.venvScriptsactivate
```

2. **安装依赖**：
```bash
   # 以可编辑模式安装项目
   uv add -e .

   # 添加开发依赖（可选）
   uv add pytest flake8
```

---

## 贡献

我们欢迎贡献！以下是开始的方法：

1. **分叉仓库**：
   在 GitHub 上点击“Fork”。

2. **克隆并设置**：
   bash
   git clone https://github.com/yourusername/paper-search-mcp.git
   cd paper-search-mcp
   pip install -e ".[dev]"  # 安装开发依赖（如果已添加到 pyproject.toml 中）

3. **进行更改**:
    - 在 `academic_platforms/` 目录下添加新的平台。
    - 更新 `tests/` 目录下的测试。

4. **提交 Pull Request**:
   将更改推送到 GitHub 并创建一个 PR。

---

## 演示

 alt="演示" width="800">

## 待办事项

### 计划中的学术平台

- [√] arXiv
- [√] PubMed
- [√] bioRxiv
- [√] medRxiv
- [√] Google Scholar
- [ ] Semantic Scholar
- [ ] PubMed Central (PMC)
- [ ] Science Direct
- [ ] Springer Link
- [ ] IEEE Xplore
- [ ] ACM Digital Library
- [ ] Web of Science
- [ ] Scopus
- [ ] JSTOR
- [ ] ResearchGate
- [ ] CORE
- [ ] Microsoft Academic

---

## 许可证

本项目采用 MIT 许可证。详情请参阅 LICENSE 文件。

---

使用 `paper-search-mcp` 进行愉快的研究！如果您遇到问题，请在 GitHub 上提交一个问题。

**官方网站：** [https://github.com/openags/paper-search-mcp](https://github.com/openags/paper-search-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`
- 标签：`search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`run --directory /path/to/your/paper-search-mcp -m paper_search_mcp.server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/openags-paper-search.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
