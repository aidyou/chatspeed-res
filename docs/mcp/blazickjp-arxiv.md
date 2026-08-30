---
title: "ArXiv AI搜索服务"
description: "ArXiv MCP服务器通过提供一个 sophisticated interface（ sophisticated接口）来连接arXiv庞大的研究资源库，从而弥合了人工智能模型与学术研究之间的差距。该服务器使人工智能助手能够进行精确的论文搜索并访问完整的论文内容，从而增强了它们与科学文献互动的能力。"
---

# ArXiv AI搜索服务

ArXiv MCP服务器通过提供一个 sophisticated interface（ sophisticated接口）来连接arXiv庞大的研究资源库，从而弥合了人工智能模型与学术研究之间的差距。该服务器使人工智能助手能够进行精确的论文搜索并访问完整的论文内容，从而增强了它们与科学文献互动的能力。

[![Twitter Follow](/mcp-assets/3e82fabdd3d7f3c8bffecf68b940346e.svg)](https://twitter.com/JoeBlazick)
[Smithery](https://smithery.ai/server/arxiv-mcp-server)
[![Python Version](/mcp-assets/4f6146f128339189f0d4b97607879041.svg)](https://www.python.org/downloads/)
[![Tests](/mcp-assets/5bb2427016803e209dad2b0fd1539cd3.svg)](https://github.com/blazickjp/arxiv-mcp-server/actions/workflows/tests.yml)
[![License: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://opensource.org/licenses/MIT)
[![PyPI Downloads](/mcp-assets/b34bb44d64ff71c74ae1877588884af5.svg)](https://pypi.org/project/arxiv-mcp-server/)
[![PyPI Version](/mcp-assets/d8e739c53aee35cbca3756a05279530b.svg)](https://pypi.org/project/arxiv-mcp-server/)

# ArXiv MCP 服务器

> 🔍 通过简单的MCP接口使AI助手能够搜索和访问arXiv论文。

ArXiv MCP 服务器通过消息控制协议（MCP）在AI助手与arXiv研究库之间提供了一个桥梁。它允许AI模型以编程方式搜索论文并访问其内容。

  
🤝 **[贡献](https://github.com/blazickjp/arxiv-mcp-server/blob/main/CONTRIBUTING.md)** • 
📝 **[报告Bug](https://github.com/blazickjp/arxiv-mcp-server/issues)**

## ✨ 核心功能

- 🔎 **论文搜索**：按日期范围和类别筛选查询arXiv论文
- 📄 **论文访问**：下载并阅读论文内容
- 📋 **论文列表**：查看所有已下载的论文
- 🗃️ **本地存储**：论文保存在本地以便更快访问
- 📝 **提示词**：一组研究提示词

## 🚀 快速开始

### 通过Smithery安装

要通过[Smithery](https://smithery.ai/server/arxiv-mcp-server)自动为Claude Desktop安装ArXiv Server：

```bash
npx -y @smithery/cli install arxiv-mcp-server --client claude
```

### 手动安装
使用uv安装：

```bash
uv tool install arxiv-mcp-server
```

开发环境：

```bash
# Clone and set up development environment
git clone https://github.com/blazickjp/arxiv-mcp-server.git
cd arxiv-mcp-server

# Create and activate virtual environment
uv venv
source .venv/bin/activate

# Install with test dependencies
uv pip install -e ".[test]"
```

### 🔌 MCP集成

将此配置添加到您的MCP客户端配置文件中：

```json
{
    "mcpServers": {
        "arxiv-mcp-server": {
            "command": "uv",
            "args": [
                "tool",
                "run",
                "arxiv-mcp-server",
                "--storage-path", "/path/to/paper/storage"
            ]
        }
    }
}
```

开发环境：

```json
{
    "mcpServers": {
        "arxiv-mcp-server": {
            "command": "uv",
            "args": [
                "--directory",
                "path/to/cloned/arxiv-mcp-server",
                "run",
                "arxiv-mcp-server",
                "--storage-path", "/path/to/paper/storage"
            ]
        }
    }
}
```

## 💡 可用工具

服务器提供了四个主要工具：

### 1. 论文搜索
带有可选过滤器的论文搜索：

```python
result = await call_tool("search_papers", {
    "query": "transformer architecture",
    "max_results": 10,
    "date_from": "2023-01-01",
    "categories": ["cs.AI", "cs.LG"]
})
```

### 2. 论文下载
根据arXiv ID下载论文：

```python
result = await call_tool("download_paper", {
    "paper_id": "2401.12345"
})
```

### 3. 列出论文
查看所有已下载的论文：

```python
result = await call_tool("list_papers", {})
```

### 4. 阅读论文
访问已下载论文的内容：

```python
result = await call_tool("read_paper", {
    "paper_id": "2401.12345"
})
```

## 📝 研究提示词

服务器提供专门的提示词来帮助分析学术论文：

### 论文分析提示词
只需一个论文ID即可进行综合的学术论文分析工作流程：

```python
result = await call_prompt("deep-paper-analysis", {
    "paper_id": "2401.12345"
})
```

该提示词包括：
- 使用可用工具(list_papers, download_paper, read_paper, search_papers)的详细说明
- 系统化的论文分析工作流程
- 全面的分析结构，涵盖：
  - 执行摘要
  - 研究背景
  - 方法论分析
  - 结果评估
  - 实践和理论影响
  - 未来研究方向
  - 更广泛的影响

## ⚙️ 配置

通过环境变量配置：

| 变量 | 用途 | 默认值 |
|----------|---------|---------|
| `ARXIV_STORAGE_PATH` | 论文存储位置 | ~/.arxiv-mcp-server/papers |

## 🧪 测试

运行测试套件：

```bash
python -m pytest
```

## 📄 许可证

本项目在 MIT 许可下发布。详情请参阅 LICENSE 文件。

---

由 Pearl Labs 团队用心制作

**官方网站：** [https://github.com/blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`, `data`
- 标签：`research and data`, `search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`tool run arxiv-mcp-server --storage-path /path/to/paper/storage`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/blazickjp-arxiv.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
