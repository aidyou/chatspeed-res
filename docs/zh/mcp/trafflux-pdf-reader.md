---
title: "PDF阅读器"
description: "提供用于读取和提取PDF文件中文本的工具，支持本地文件和URL。"
---

# PDF阅读器

提供用于读取和提取PDF文件中文本的工具，支持本地文件和URL。

# PDF Reader MCP 服务器

这是一个 Model Context Protocol (MCP) 服务器，提供了从 PDF 文件中读取和提取文本的工具，支持本地文件和 URL。

## 作者

Philip Van de Walker  
邮箱: philip.vandewalker@gmail.com  
GitHub: [https://github.com/trafflux](https://github.com/trafflux)

## 功能

- 从本地 PDF 文件中读取文本内容
- 从 PDF URL 中读取文本内容
- 对损坏或无效 PDF 的错误处理
- 挂载卷以访问本地 PDF
- 自动检测 PDF 编码
- 标准化的 JSON 输出格式

## 安装

1. 克隆仓库：

```bash
git clone https://github.com/trafflux/pdf-reader-mcp.git
cd pdf-reader-mcp
```

2. 构建 Docker 镜像：

```bash
docker build -t mcp/pdf-reader .
```

## 使用

### 运行服务器

要运行服务器并访问本地 PDF 文件：

```bash
docker run -i --rm -v /path/to/pdfs:/pdfs mcp/pdf-reader
```

将 `/path/to/pdfs` 替换为您的 PDF 文件目录的实际路径。

如果不使用本地 PDF 文件：

```bash
docker run -i --rm mcp/pdf-reader
```

### MCP 配置

将以下配置添加到您的 MCP 设置中：

```json
{
  "mcpServers": {
    "pdf-reader": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-v",
        "/path/to/pdfs:/pdfs",
        "mcp/pdf-reader"
      ],
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

不使用本地文件 PDF 文件时：

```json
{
  "mcpServers": {
    "pdf-reader": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "mcp/pdf-reader"],
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

### 可用工具

1. `read_local_pdf`

   - 目的：从本地 PDF 文件中读取文本内容
   - 输入：
```json
     {
       "path": "/pdfs/document.pdf"
     }
```
   - 输出：
```json
     {
       "success": true,
       "data": {
         "text": "提取的内容..."
       }
     }
```

2. `read_pdf_url`
   - 目的：从 PDF URL 中读取文本内容
   - 输入：
```json
     {
       "url": "https://example.com/document.pdf"
     }
```
   - 输出：
```json
     {
       "success": true,
       "data": {
         "text": "提取的内容..."
       }
     }
```

## 错误处理

服务器处理各种错误情况，并提供清晰的错误消息：

- 无效或损坏的 PDF 文件
- 缺失的文件
- URL 请求失败
- 权限问题
- 网络连接问题

错误响应遵循以下格式：

```json
{
  "success": false,
  "error": "Detailed error message"
}
```

## 依赖项

- Python 3.11+
- PyPDF2: PDF 解析和文本提取
- requests: 用于从 URL 获取 PDF 的 HTTP 客户端
- MCP SDK: Model Context Protocol 实现

## 项目结构

```
.
├── Dockerfile          # Container configuration
├── README.md          # This documentation
├── requirements.txt   # Python dependencies
└── src/
    ├── __init__.py    # Package initialization
    └── server.py      # Main server implementation
```

## 许可证

版权所有 2025 Philip Van de Walker

根据 Apache License, Version 2.0（“许可证”）获得许可；除非符合许可证的要求，否则不得使用此文件。您可以在以下地址获取许可证副本：

    http://www.apache.org/licenses/LICENSE-2.0

除非适用法律要求或书面同意，否则根据许可证分发的软件是按“原样”提供的，没有任何明示或暗示的保证或条件。有关特定语言的权限和限制，请参阅许可证。

## 贡献

欢迎贡献！请随时提交 Pull Request。

## 联系方式

对于问题、意见或贡献，请联系 Philip Van de Walker：

- 邮箱: philip.vandewalker@gmail.com
- GitHub: https://github.com/trafflux

**官方网站：** [https://github.com/trafflux/pdf-reader-mcp](https://github.com/trafflux/pdf-reader-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`browser`, `files`
- 标签：`file systems`, `browser automation`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`docker`
- 参数：`run -i --rm -v /path/to/pdfs:/pdfs mcp/pdf-reader`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/trafflux-pdf-reader.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
