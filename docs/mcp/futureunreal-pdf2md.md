---
title: "PDF2MD PDF转Markdown工具"
description: "PDF转Markdown转换工具"
---

# PDF2MD PDF转Markdown工具

PDF转Markdown转换工具

# MCP-PDF2MD

[Smithery](https://smithery.ai/server/@FutureUnreal/mcp-pdf2md)
[English](#pdf2md-service) | [中文](https://github.com/FutureUnreal/mcp-pdf2md/blob/HEAD/README_CN.md)

# MCP-PDF2MD 服务

基于 MinerU API 的高性能 PDF 转 Markdown 服务，支持本地文件和 URL 链接的批量处理，并提供结构化输出。

## 主要功能

- 格式转换：将 PDF 文件转换为结构化的 Markdown 格式。
- 多源支持：处理本地 PDF 文件和 URL 链接。
- 智能处理：自动选择最佳处理方法。
- 批量处理：支持多文件批量转换，高效处理大量 PDF 文件。
- MCP 集成：无缝集成到 Claude Desktop 等 LLM 客户端。
- 结构保留：保持原始文档结构，包括标题、段落、列表等。
- 智能布局：以人类可读顺序输出文本，适用于单列、多列和复杂布局。
- 公式转换：自动识别并转换文档中的公式为 LaTeX 格式。
- 表格提取：自动识别并转换文档中的表格为结构化格式。
- 清理优化：移除页眉、页脚、脚注、页码等，确保语义连贯。
- 高质量提取：从 PDF 文档中高质量提取文本、图像和布局信息。

## 系统要求

- 软件：Python 3.10+

## 快速开始

1. 克隆仓库并进入目录：
```bash
   git clone https://github.com/FutureUnreal/mcp-pdf2md.git
   cd mcp-pdf2md
```

2. 创建虚拟环境并安装依赖项：
   
   **Linux/macOS**:
```bash
   uv venv
   source .venv/bin/activate
   uv pip install -e .
```
   
   **Windows**:
```bash
   uv venv
   .venv\Scripts\activate
   uv pip install -e .
```

3. 配置环境变量：

   在项目根目录创建一个 `.env` 文件，并设置以下环境变量：
```
   MINERU_API_BASE=https://mineru.net/api/v4/extract/task
   MINERU_BATCH_API=https://mineru.net/api/v4/extract/task/batch
   MINERU_BATCH_RESULTS_API=https://mineru.net/api/v4/extract-results/batch
   MINERU_API_KEY=your_api_key_here
```

4. 启动服务：
```bash
   uv run pdf2md
```

## 命令行参数

服务器支持以下命令行参数：

## Claude Desktop 配置

在 Claude Desktop 中添加以下配置：

**Windows**:
```json
{
    "mcpServers": {
        "pdf2md": {
            "command": "uv",
            "args": [
                "--directory",
                "C:\\path\\to\\mcp-pdf2md",
                "run",
                "pdf2md",
                "--output-dir",
                "C:\\path\\to\\output"
            ],
            "env": {
                "MINERU_API_KEY": "your_api_key_here"
            }
        }
    }
}
```

**Linux/macOS**:
```json
{
    "mcpServers": {
        "pdf2md": {
            "command": "uv",
            "args": [
                "--directory",
                "/path/to/mcp-pdf2md",
                "run",
                "pdf2md",
                "--output-dir",
                "/path/to/output"
            ],
            "env": {
                "MINERU_API_KEY": "your_api_key_here"
            }
        }
    }
}
```

**关于 API 密钥配置的说明：**
您可以使用两种方式设置 API 密钥：
1. 在项目目录内的 `.env` 文件中（推荐用于开发）
2. 如上所示，在 Claude Desktop 配置中（推荐用于常规使用）

如果您在两个地方都设置了 API 密钥，则 Claude Desktop 配置中的密钥优先。

## MCP 工具

服务器提供了以下 MCP 工具：

- **convert_pdf_url**: 将PDF URL转换为Markdown
- **convert_pdf_file**: 将本地PDF文件转换为Markdown

## 获取MinerU API密钥

此项目依赖于MinerU API来提取PDF内容。要获取API密钥：

1. 访问[MinerU官方网站](https://mineru.net/)并注册一个账户
2. 登录后，通过[此链接](https://mineru.net/apiManage/docs?openApplyModal=true)申请API测试资格
3. 一旦您的申请被批准，您可以访问[API管理](https://mineru.net/apiManage/token)页面
4. 按照提供的说明生成您的API密钥
5. 复制生成的API密钥
6. 使用此字符串作为`MINERU_API_KEY`的值

请注意，目前访问MinerU API处于测试阶段，需要获得MinerU团队的批准。审批过程可能需要一些时间，请相应地做好计划。

## 演示

### 输入PDF

### 输出Markdown

## 许可证

MIT许可证 - 详情请参阅LICENSE文件。

## 致谢

本项目基于[MinerU](https://github.com/opendatalab/MinerU/tree/master)的API。

**官方网站：** [https://github.com/FutureUnreal/mcp-pdf2md](https://github.com/FutureUnreal/mcp-pdf2md)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`files`
- 标签：`file systems`, `developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`--directory C:\path\to\mcp-pdf2md run pdf2md --output-dir C:\path\to\output`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/futureunreal-pdf2md.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
