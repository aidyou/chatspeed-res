---
title: "文档智能工具"
description: "通过自然语言使人工智能能够读取、创建和修改Word文档。"
---

# 文档智能工具

通过自然语言使人工智能能够读取、创建和修改Word文档。

# Word Tools MCP 服务器

一个提供基于 AI 的 Word 文档操作功能的模型上下文协议 (MCP) 服务器。此服务器实现了 MCP 协议，使 AI 应用程序能够通过自然语言交互来创建、编辑和管理 Word 文档。

[Smithery](https://smithery.ai/server/@puchunjie/doc-tools)

  

## 功能

- 完整的 MCP 协议实现
- Word 文档的创建和管理
- 丰富的文本内容操作
- 表格的创建和格式化
- 文档布局控制
- 文档元数据管理
- 实时文档状态监控

## 先决条件

- Node.js 14 或更高版本
- Microsoft Word（可选，用于高级功能）

## 安装

```bash
npx @puchunjie/doc-tools-mcp
```

或者全局安装：

```bash
npm install -g @puchunjie/doc-tools-mcp
```

作为项目依赖使用：

```bash
npm install @puchunjie/doc-tools-mcp
```

## 使用方法

1. 启动 MCP 服务器：

```bash
npx @puchunjie/doc-tools-mcp
```

2. 服务器默认将在 8765 端口启动

3. 配置您的 AI 应用程序（例如 Cursor, VSCode）以使用 MCP 服务器：
```
   http://localhost:8765
```

## MCP 工具

服务器提供了以下 MCP 功能：

- `create_document` - 创建一个新的 Word 文档
  - 参数：filePath（必需），title, author

- `open_document` - 打开一个现有的 Word 文档
  - 参数：filePath（必需）

- `add_paragraph` - 向文档中添加段落
  - 参数：filePath（必需），text（必需），style, alignment

- `add_table` - 向文档中添加表格
  - 参数：filePath（必需），rows（必需），cols（必需），headers, data

- `search_and_replace` - 在文档中查找并替换文本
  - 参数：filePath（必需），searchText（必需），replaceText（必需），matchCase

- `set_page_margins` - 设置文档页面边距
  - 参数：filePath（必需），top, right, bottom, left

- `get_document_info` - 获取文档元数据
  - 参数：filePath（必需）

## 与 AI 应用程序集成

### Cursor

1. 打开 Cursor 配置文件 `~/.cursor/mcp.json`
2. 添加以下配置：
```json
{
  "mcpServers": {
    "doc-tools-mcp": {
      "command": "npx",
      "args": [
        "@puchunjie/doc-tools-mcp"
      ]
    }
  }
}

```

对于本地开发版本：
```json
{
  "mcpServers": {
    "doc-tools-mcp": {
      "command": "node",
      "args": [
        "/path/to/your/doc-tools-mcp/dist/mcp-server.js"
      ]
    }
  }
}
```

配置完成后，您可以使用自然语言来操作 Word 文档：
```
"Create a new document named report.docx"
"Add a heading 'Monthly Report' to report.docx"
"Insert a 4x3 table with sales data"
```

### VSCode 和其他兼容 MCP 的工具

对于支持 MCP 协议的其他工具，类似的集成步骤适用。请查阅您工具的文档以获取特定的 MCP 服务器配置步骤。

## 开发

要扩展或修改此 MCP 服务器：

1. 克隆仓库：
```bash
git clone 
cd doc-tools-mcp
```

2. 安装依赖项：
```bash
npm install
```

3. 以开发模式启动：
```bash
npm run start
```

4. 构建生产版本：
```bash
npm run build
```

### 添加新的 MCP 函数

1. 在 `src/services/DocumentService.ts` 中添加新方法
2. 在 `src/mcp-server.ts` 中注册新函数
3. 根据需要更新类型定义

## 配置

- 默认端口：8765（可配置）
- 支持的文件类型：.docx
- 所有文件路径应为绝对路径或相对于当前工作目录的路径

## 许可证

MIT

## 支持

如果您遇到任何问题或有任何改进建议，请在我们的 GitHub 仓库中提交问题。

**官方网站：** [https://github.com/puchunjie/doc-tools-mcp](https://github.com/puchunjie/doc-tools-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`files`
- 标签：`file systems`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`@puchunjie/doc-tools-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/puchunjie-doc-tools.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
