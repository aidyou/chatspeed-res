---
title: "AI Word文档助手"
description: "一个模型上下文协议服务器，它使人工智能助手能够通过标准化的工具和资源创建、读取、编辑和格式化Microsoft Word文档。"
---

# AI Word文档助手

一个模型上下文协议服务器，它使人工智能助手能够通过标准化的工具和资源创建、读取、编辑和格式化Microsoft Word文档。

# Office-Word-MCP-Server

一个用于创建、读取和操作 Microsoft Word 文档的 Model Context Protocol (MCP) 服务器。该服务器通过标准化接口使 AI 助手能够处理 Word 文档，提供丰富的文档编辑功能。

  

![](/mcp-assets/c1486b4e2d8cfd67ed0257afeefda188.svg 'MCP Server')

## 概述

Office-Word-MCP-Server 实现了 [Model Context Protocol](https://modelcontextprotocol.io/)，将 Word 文档操作作为工具和资源暴露出来。它充当 AI 助手与 Microsoft Word 文档之间的桥梁，允许进行文档创建、内容添加、格式化和分析。

### 示例

#### 提示

![image](/mcp-assets/395a6377f12fe93d389157130a292b11.png)

#### 输出

![image](/mcp-assets/a79683de81cad01ede15b3c05c60f894.png)

## 功能

### 文档管理
- 创建带有元数据的新 Word 文档
- 提取文本并分析文档结构
- 查看文档属性和统计信息
- 列出目录中的可用文档
- 创建现有文档的副本

### 内容创建
- 添加不同级别的标题
- 插入段落（可选样式）
- 使用自定义数据创建表格
- 按比例缩放添加图片
- 插入分页符

### 富文本格式
- 格式化特定文本段落（加粗、斜体、下划线）
- 更改文本颜色和字体属性
- 应用自定义样式到文本元素
- 在整个文档中搜索和替换文本

### 表格格式
- 使用边框和样式格式化表格
- 创建具有独特格式的表头行
- 应用单元格阴影和自定义边框
- 结构化表格以提高可读性

### 高级文档操作
- 删除段落
- 创建自定义文档样式
- 在整个文档中应用一致的格式
- 详细控制特定范围的文本格式

## 安装

### 前提条件
- Python 3.8 或更高版本
- pip 包管理器

### 基本安装

```bash
# Clone the repository
git clone https://github.com/GongRzhe/Office-Word-MCP-Server.git
cd Office-Word-MCP-Server

# Install dependencies
pip install -r requirements.txt
```

### 使用设置脚本

或者，您可以使用提供的设置脚本，该脚本处理：
- 检查前提条件
- 设置虚拟环境
- 安装依赖项
- 生成 MCP 配置

```bash
python setup_mcp.py
```

## 与 Claude for Desktop 一起使用

### 配置

#### 方法 1：本地安装后

1. 安装完成后，将服务器添加到您的 Claude for Desktop 配置文件中：

```json
{
  "mcpServers": {
    "word-document-server": {
      "command": "python",
      "args": [
        "/path/to/word_server.py"
      ]
    }
  }
}
```

#### 方法 2：无需安装（使用 uvx）

1. 您还可以通过使用 uvx 包管理器配置 Claude for Desktop 来使用服务器，而无需本地安装：

```json
{
  "mcpServers": {
    "word-document-server": {
      "command": "uvx",
      "args": [
        "--from", "office-word-mcp-server", "word_mcp_server"
      ]
    }
  }
}
```

2. 配置文件位置：
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`

3. 重启 Claude for Desktop 以加载配置。

### 示例操作

配置完成后，您可以要求 Claude 执行以下操作：

- "创建一个名为 'report.docx' 的新文档，并添加封面页"
- "在我的文档中添加一个标题和三个段落"
- "插入一个包含销售数据的4x4表格"
- "将第2段中的单词 'important' 设置为加粗并显示为红色"
- "查找并替换所有 'old term' 实例为 'new term'"
- "为节标题创建自定义样式"
- "对我的文档中的表格应用格式"

## API 参考

### 文档创建与属性

```python
create_document(filename, title=None, author=None)
get_document_info(filename)
get_document_text(filename)
get_document_outline(filename)
list_available_documents(directory=".")
copy_document(source_filename, destination_filename=None)
```

### 内容添加

```python
add_heading(filename, text, level=1)
add_paragraph(filename, text, style=None)
add_table(filename, rows, cols, data=None)
add_picture(filename, image_path, width=None)
add_page_break(filename)
```

### 文本格式化

```python
format_text(filename, paragraph_index, start_pos, end_pos, bold=None, 
            italic=None, underline=None, color=None, font_size=None, font_name=None)
search_and_replace(filename, find_text, replace_text)
delete_paragraph(filename, paragraph_index)
create_custom_style(filename, style_name, bold=None, italic=None, 
                    font_size=None, font_name=None, color=None, base_style=None)
```

### 表格格式化

```python
format_table(filename, table_index, has_header_row=None, 
             border_style=None, shading=None)
```

## 故障排除

### 常见问题

1. **缺少样式**
   - 某些文档可能缺乏执行标题和表格操作所需的样式
   - 服务器将尝试创建缺失的样式或使用直接格式化
   - 为了获得最佳结果，请使用具有标准 Word 样式的模板

2. **权限问题**
   - 确保服务器有权读写文档路径
   - 使用 `copy_document` 函数来创建锁定文档的可编辑副本
   - 如果操作失败，请检查文件所有权和权限

3. **图片插入问题**
   - 使用绝对路径指定图像文件
   - 确认图像格式兼容性（推荐使用 JPEG、PNG）
   - 检查图像文件大小和权限

### 调试

通过设置环境变量启用详细日志记录：

```bash
export MCP_DEBUG=1  # Linux/macOS
set MCP_DEBUG=1     # Windows
```

## 贡献

欢迎贡献！请随时提交 Pull Request。

1. 分叉仓库
2. 创建你的功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交你的更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到该分支 (`git push origin feature/amazing-feature`)
5. 打开 Pull Request

## 许可证

此项目根据 MIT 许可证发布 - 详情请参阅 LICENSE 文件。

## 致谢

- [模型上下文协议](https://modelcontextprotocol.io/) 提供了协议规范
- [python-docx](https://python-docx.readthedocs.io/) 用于处理 Word 文档
- [FastMCP](https://github.com/modelcontextprotocol/python-sdk) 提供 Python MCP 实现

---

*注意：此服务器会与您系统上的文档文件交互。在 Claude for Desktop 或其他 MCP 客户端中确认任何请求的操作之前，请始终验证这些操作是否适当。*

**官方网站：** [https://github.com/gongrzhe/office-word-mcp-server](https://github.com/gongrzhe/office-word-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`files`
- 标签：`file systems`, `note taking`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`--from office-word-mcp-server word_mcp_server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/gongrzhe-office-word.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
