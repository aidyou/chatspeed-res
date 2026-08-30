---
title: "Excel文件操作工具"
description: "正文语言类型：英语  \n翻译结果：提供对Excel文件的操纵功能，无需安装Microsoft Excel，即可实现工作簿创建、数据操作、格式设置和高级Excel功能。"
---

# Excel文件操作工具

正文语言类型：英语  
翻译结果：提供对Excel文件的操纵功能，无需安装Microsoft Excel，即可实现工作簿创建、数据操作、格式设置和高级Excel功能。

# Excel MCP 服务器
[Smithery](https://smithery.ai/server/@haris-musa/excel-mcp-server)

这是一个 Model Context Protocol (MCP) 服务器实现，提供了无需安装 Microsoft Excel 即可操作 Excel 文件的功能。此服务器支持工作簿创建、数据操作、格式化以及高级的 Excel 功能。

## 要求

- Python 3.10+
- MCP SDK 1.2.0+
- OpenPyXL 3.1.2+

## 组件

### 资源

该服务器通过 OpenPyXL 提供了 Excel 工作簿的操作功能：

- 创建和修改 Excel 工作簿
- 管理工作表和范围
- 处理格式和样式
- 支持图表和数据透视表

### 工具

本服务器提供了一整套 Excel 操作工具。有关所有可用工具、它们的参数及使用示例的详细文档，请参阅 [TOOLS.md](https://github.com/fish0710/excel-mcp/blob/HEAD/TOOLS.md)。

这些工具包括以下功能：

- 工作簿和工作表管理
- 数据读写
- 格式化和样式设置
- 图表和可视化
- 数据透视表和数据分析

详见 [TOOLS.md](https://github.com/fish0710/excel-mcp/blob/HEAD/TOOLS.md) 获取完整文档。

## 特性

- 全面的 Excel 支持：综合性的 Excel 功能
- 数据操作：读取、写入和转换数据
- 高级特性：图表、数据透视表和格式化
- 错误处理：带有清晰消息的全面错误处理

## 使用方法

### 环境配置

可以通过以下环境变量来配置服务器：

- `EXCEL_FILES_PATH`：存储 Excel 文件的目录（默认值：`./excel_files`）

你可以用不同的方式设置它：

Windows CMD:

```cmd
set EXCEL_FILES_PATH=C:\path\to\excel\files
uv run excel-mcp-server
```

Windows PowerShell:

```powershell
$env:EXCEL_FILES_PATH="C:\path\to\excel\files"
uv run excel-mcp-server
```

Linux/MacOS:

```bash
export EXCEL_FILES_PATH=/path/to/excel/files
uv run excel-mcp-server
```

或者在 Claude Desktop 配置中：

```json
{
  "mcpServers": {
    "excel": {
      "command": "uv run excel-mcp-server",
      "transport": "sse",
      "env": {
        "EXCEL_FILES_PATH": "/path/to/excel/files"
      }
    }
  }
}
```

### 启动服务器

启动服务器：

```bash
uv run excel-mcp-server
```

服务器将以 SSE 模式启动，并等待来自 MCP 客户端的连接。

### 在 Cursor IDE 中连接

启动服务器后，在 Cursor IDE 中连接到 SSE 端点：

```
http://localhost:8000/sse
```

Excel MCP 工具将通过代理程序可用。

关于可用工具及其用法，请参阅 [TOOLS.md](https://github.com/fish0710/excel-mcp/blob/HEAD/TOOLS.md)。

## 许可证

该项目根据 MIT 许可证发布 - 详情请见 [LICENSE](https://github.com/fish0710/excel-mcp/blob/HEAD/LICENSE) 文件。

**官方网站：** [https://github.com/fish0710/excel-mcp](https://github.com/fish0710/excel-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`files`, `data`
- 标签：`file systems`, `research and data`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv run excel-mcp-server`
- 参数：无

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/fish0710-excel.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
