---
title: "Excel服务器"
description: "提供对Excel文件的操纵功能。此服务器启用工作簿创建、数据操纵、格式设置和高级Excel功能。"
---

# Excel服务器

提供对Excel文件的操纵功能。此服务器启用工作簿创建、数据操纵、格式设置和高级Excel功能。

# Excel MCP 服务器

这是一个模型上下文协议（MCP）服务器，允许你在不安装 Microsoft Excel 的情况下操作 Excel 文件。使用你的 AI 代理创建、读取和修改 Excel 工作簿。

## 功能

- 📊 创建和修改 Excel 工作簿
- 📝 读写数据
- 🎨 应用格式和样式
- 📈 创建图表和可视化
- 📊 生成数据透视表
- 🔄 管理工作表和范围

## 快速开始

### 前提条件

- Python 3.10 或更高版本

### 安装

1. 克隆仓库：
```bash
git clone https://github.com/haris-musa/excel-mcp-server.git
cd excel-mcp-server
```

2. 使用 uv 安装：
```bash
uv pip install -e .
```

### 运行服务器

启动服务器（默认端口 8000）：
```bash
uv run excel-mcp-server
```

自定义端口（例如 8080）：

```bash
# Bash/Linux/macOS
export FASTMCP_PORT=8080 && uv run excel-mcp-server

# Windows PowerShell
$env:FASTMCP_PORT = "8080"; uv run excel-mcp-server
```

## 与 AI 工具一起使用

### Cursor IDE

1. 在 Cursor 中添加此配置：
```json
{
  "mcpServers": {
    "excel": {
      "url": "http://localhost:8000/sse",
      "env": {
        "EXCEL_FILES_PATH": "/path/to/excel/files"
      }
    }
  }
}
```

2. Excel 工具将通过你的 AI 助手可用。

### 远程托管与传输协议

该服务器使用服务器发送事件（SSE）传输协议。对于不同的使用场景：

1. **与 Claude Desktop 一起使用（需要 stdio）:**
   - 使用 [Supergateway](https://github.com/supercorp-ai/supergateway) 将 SSE 转换为 stdio:

2. **托管您的 MCP 服务器：**
   - [远程 MCP 服务器指南](https://developers.cloudflare.com/agents/guides/remote-mcp-server/)

## 环境变量

- `FASTMCP_PORT`: 服务器端口（默认：8000）
- `EXCEL_FILES_PATH`: Excel 文件目录（默认：`./excel_files`）

## 可用工具

服务器提供了一整套的 Excel 操作工具。请参阅 [TOOLS.md](https://github.com/haris-musa/excel-mcp-server/blob/HEAD/TOOLS.md) 获取所有可用工具的完整文档。

## 许可证

MIT 许可证 - 详情见 [LICENSE](https://github.com/haris-musa/excel-mcp-server/blob/HEAD/LICENSE)。

**官方网站：** [https://github.com/haris-musa/excel-mcp-server](https://github.com/haris-musa/excel-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`, `databases`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`excel-mcp-server stdio`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/haris-musa-excel.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
