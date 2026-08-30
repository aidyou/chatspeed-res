---
title: "Excel文件服务"
description: "一个模型上下文协议服务器，使人工智能助手能够读取和写入Microsoft Excel文件，支持xlsx、xlsm、xltx和xltm等格式。"
---

# Excel文件服务

一个模型上下文协议服务器，使人工智能助手能够读取和写入Microsoft Excel文件，支持xlsx、xlsm、xltx和xltm等格式。

# Excel MCP 服务器

 width="128">

[![NPM 版本](/mcp-assets/2676ce9d04906ee62bf588f55bb53df6.svg)](https://www.npmjs.com/package/@negokaz/excel-mcp-server)
[Smithery](https://smithery.ai/server/@negokaz/excel-mcp-server)

一个读写 MS Excel 数据的 Model Context Protocol (MCP) 服务器。

## 功能

- 从 MS Excel 文件中读取文本值
- 向 MS Excel 文件中写入文本值
- 从 MS Excel 文件中读取公式
- 向 MS Excel 文件中写入公式
- 从 MS Excel 文件中捕获屏幕图像（仅限 Windows）

更多详情，请参见[工具](#tools)部分。

## 要求

- Node.js 20.x 或更高版本

## 支持的文件格式

- xlsx（Excel 工作簿）
- xlsm（启用宏的 Excel 工作簿）
- xltx（Excel 模板）
- xltm（启用宏的 Excel 模板）

## 安装

### 通过 NPM 安装

通过在 MCP 服务器配置中添加以下配置，将自动安装 excel-mcp-server。

对于 Windows：
```json
{
    "mcpServers": {
        "excel": {
            "command": "cmd",
            "args": ["/c", "npx", "--yes", "@negokaz/excel-mcp-server"],
            "env": {
                "EXCEL_MCP_PAGING_CELLS_LIMIT": "4000"
            }
        }
    }
}
```

对于其他平台：
```json
{
    "mcpServers": {
        "excel": {
            "command": "npx",
            "args": ["--yes", "@negokaz/excel-mcp-server"],
            "env": {
                "EXCEL_MCP_PAGING_CELLS_LIMIT": "4000"
            }
        }
    }
}
```

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@negokaz/excel-mcp-server) 自动为 Claude Desktop 安装 Excel MCP 服务器：

```bash
npx -y @smithery/cli install @negokaz/excel-mcp-server --client claude
```

工具

### `read_sheet_names`

列出 Excel 文件中的所有工作表名称。

**参数：**
- `fileAbsolutePath`
    - Excel 文件的绝对路径

### `read_sheet_data`

分页从 Excel 工作表中读取数据。

**参数：**
- `fileAbsolutePath`
    - Excel 文件的绝对路径
- `sheetName`
    - Excel 文件中的工作表名称
- `range`
    - 要在 Excel 工作表中读取的单元格范围（例如："A1:C10"）。[默认：第一个分页范围]
- `knownPagingRanges`
    - 已读取的分页范围列表

### `read_sheet_formula`

分页从 Excel 工作表中读取公式。

**参数：**
- `fileAbsolutePath`
    - Excel 文件的绝对路径
- `sheetName`
    - Excel 文件中的工作表名称
- `range`
    - 要在 Excel 工作表中读取的单元格范围（例如："A1:C10"）。[默认：第一个分页范围]
- `knownPagingRanges`
    - 已读取的分页范围列表

### `read_sheet_image`

**[仅限 Windows]** 分页从 Excel 工作表中以图像形式读取数据。

**参数：**
- `fileAbsolutePath`
    - Excel 文件的绝对路径
- `sheetName`
    - Excel 文件中的工作表名称
- `range`
    - 要在 Excel 工作表中读取的单元格范围（例如："A1:C10"）。[默认：第一个分页范围]
- `knownPagingRanges`
    - 已读取的分页范围列表

### `write_sheet_data`

向 Excel 工作表中写入数据。

**参数：**
- `fileAbsolutePath`
    - Excel 文件的绝对路径
- `sheetName`
    - Excel 文件中的工作表名称
- `range`
    - 要在 Excel 工作表中读取的单元格范围（例如："A1:C10"）。
- `data`
    - 要写入 Excel 工作表的数据

### `write_sheet_formula`

向 Excel 工作表中写入公式。

**参数：**

- `fileAbsolutePath`
    - Excel 文件的绝对路径
- `sheetName`
    - Excel 文件中的工作表名称
- `range`
    - 要在 Excel 工作表中读取的单元格范围（例如，"A1:C10"）
- `formulas`
    - 要写入 Excel 工作表的公式（例如，"=A1+B1"）

配置

您可以通过以下环境变量更改 MCP 服务器的行为：

### `EXCEL_MCP_PAGING_CELLS_LIMIT`

单次分页操作中读取的最大单元格数。  
[默认值：4000]

## 许可证

版权所有 (c) 2025 Kazuki Negoro

excel-mcp-server 在 [MIT License](https://github.com/negokaz/excel-mcp-server/blob/HEAD/LICENSE) 下发布

**官方网站：** [https://github.com/negokaz/excel-mcp-server](https://github.com/negokaz/excel-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`files`
- 标签：`file systems`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`--yes @negokaz/excel-mcp-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/negokaz-excel.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
