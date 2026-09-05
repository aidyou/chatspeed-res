---
title: "Excel分块读取器"
description: "通过自动分块和分页高效处理大型Excel文件，使用MCP实现无缝的文件读取和管理功能，例如工作表选择和错误处理。"
---

# Excel分块读取器

通过自动分块和分页高效处理大型Excel文件，使用MCP实现无缝的文件读取和管理功能，例如工作表选择和错误处理。

# MCP Excel 读取器

[Smithery](https://smithery.ai/server/@ArchimedesCrypto/excel-reader-mcp-chunked)
这是一个用于读取 Excel 文件的 Model Context Protocol (MCP) 服务器，支持自动分块和分页。使用 SheetJS 和 TypeScript 构建，该工具通过将大文件自动拆分为可管理的小块来帮助您高效处理大型 Excel 文件。

## 功能

- 📊 自动大小限制读取 Excel 文件 (.xlsx, .xls)
- 🔄 大数据集的自动分块
- 📑 表格选择与行分页
- 📅 正确的日期处理
- ⚡ 针对大文件优化
- 🛡️ 错误处理与验证

## 安装

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@ArchimedesCrypto/excel-reader-mcp-chunked) 自动为 Claude Desktop 安装 Excel 读取器：

```bash
npx -y @smithery/cli install @ArchimedesCrypto/excel-reader-mcp-chunked --client claude
```

### 作为 MCP 服务器安装

1. 全局安装：
```bash
npm install -g @archimdescrypto/excel-reader
```

2. 添加到您的 MCP 设置文件中（通常位于 `~/.config/claude/settings.json` 或等效位置）：
```json
{
  "mcpServers": {
    "excel-reader": {
      "command": "excel-reader",
      "env": {}
    }
  }
}
```

### 开发环境

1. 克隆仓库：
```bash
git clone https://github.com/ArchimdesCrypto/mcp-excel-reader.git
cd mcp-excel-reader
```

2. 安装依赖项：
```bash
npm install
```

3. 构建项目：
```bash
npm run build
```

## 使用

Excel 读取器提供了一个名为 `read_excel` 的工具，具有以下参数：

```typescript
interface ReadExcelArgs {
  filePath: string;      // Path to Excel file
  sheetName?: string;    // Optional sheet name (defaults to first sheet)
  startRow?: number;     // Optional starting row for pagination
  maxRows?: number;      // Optional maximum rows to read
}

// Response format
interface ExcelResponse {
  fileName: string;
  totalSheets: number;
  currentSheet: {
    name: string;
    totalRows: number;
    totalColumns: number;
    chunk: {
      rowStart: number;
      rowEnd: number;
      columns: string[];
      data: Record[];
    };
    hasMore: boolean;
    nextChunk?: {
      rowStart: number;
      columns: string[];
    };
  };
}
```

### 基本用法

当与 Claude 或其他 MCP 兼容的 AI 一起使用时：

```
Read the Excel file at path/to/file.xlsx
```

AI 将使用该工具读取文件，并自动处理大文件的分块。

### 功能

1. **自动分块**
   - 自动将大文件分割成可管理的小块
   - 默认块大小为 100KB
   - 提供分页所需的元数据

2. **表格选择**
   - 按名称读取特定表格
   - 如果未指定，默认读取第一个表格

3. **行分页**
   - 通过 startRow 和 maxRows 控制要读取的行
   - 获取下一个块的信息以进行连续读取

4. **错误处理**
   - 验证文件存在性和格式
   - 提供清晰的错误消息
   - 优雅地处理格式不正确的 Excel 文件

## 通过 SheetJS 功能扩展

Excel 读取器基于 SheetJS 构建，可以利用其强大的功能进行扩展：

### 可用扩展

1. **公式处理**
```typescript
   // 启用公式解析
   const wb = XLSX.read(data, {
     cellFormula: true,
     cellNF: true
   });
```

2. **单元格格式化**
```typescript
   // 访问单元格样式和格式
   const styles = Object.keys(worksheet)
     .filter(key => key[0] !== '!')
     .map(key => ({
       cell: key,
       style: worksheet[key].s
     }));
```

3. **数据验证**
```typescript
   // 访问数据验证规则
   const validation = worksheet['!dataValidation'];
```

4. **表格功能**
   - 合并单元格：`worksheet['!merges']`
   - 隐藏行/列：`worksheet['!rows']`, `worksheet['!cols']`
   - 表格保护：`worksheet['!protect']`

更多功能和详细文档，请访问 [SheetJS 文档](https://docs.sheetjs.com/)。

## 贡献

1. 叉分仓库
2. 创建你的特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交你的更改 (`git commit -m '添加了一些惊人的功能'`)
4. 推送到该分支 (`git push origin feature/amazing-feature`)
5. 打开一个拉取请求

## 许可证

本项目根据 MIT 许可证发布 - 详情请参阅 [LICENSE](https://github.com/ArchimedesCrypto/excel-reader-mcp/blob/HEAD/LICENSE) 文件。

## 致谢

- 使用 [SheetJS](https://sheetjs.com/) 构建
- 属于 [Model Context Protocol](https://github.com/modelcontextprotocol/mcp) 生态系统的一部分

**官方网站：** [https://github.com/ArchimedesCrypto/excel-reader-mcp](https://github.com/ArchimedesCrypto/excel-reader-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`files`
- 标签：`file systems`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`excel-reader`
- 参数：无

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/archimedescrypto-excel-reader.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
