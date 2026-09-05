---
title: "office办公助手"
description: "Office 文档处理 MCP 服务器 EN CN MCP 服务器 Python 许可证 一个用于 Office 文档处理的 MCP（模型上下文协议）服务器，能够在不离开 AI 助手环境的情况下，在 MCP 客户端中创建和编辑 Word、Excel 和 PowerPoint 文档。 概览 Office-Editor-MCP 实现了 Model Context Protocol 标准，将 Offic…"
---

# office办公助手

Office 文档处理 MCP 服务器 EN CN MCP 服务器 Python 许可证 一个用于 Office 文档处理的 MCP（模型上下文协议）服务器，能够在不离开 AI 助手环境的情况下，在 MCP 客户端中创建和编辑 Word、Excel 和 PowerPoint 文档。 概览 Office-Editor-MCP 实现了 Model Context Protocol 标准，将 Offic…

Office 文档处理 MCP 服务器
EN CN

MCP 服务器 Python 许可证

一个用于 Office 文档处理的 MCP（模型上下文协议）服务器，能够在不离开 AI 助手环境的情况下，在 MCP 客户端中创建和编辑 Word、Excel 和 PowerPoint 文档。

概览
Office-Editor-MCP 实现了 Model Context Protocol 标准，将 Office 文档操作作为工具和资源暴露出来。它充当 AI 助手与 Microsoft Office 文档之间的桥梁，允许您通过 AI 助手创建、编辑、格式化和分析各种 Office 文档。

功能
Word 文档操作
文档管理
使用元数据（标题、作者等）创建新的 Word 文档
提取文本内容并分析文档结构
查看文档属性和统计信息
列出目录中的可用文档
创建文档副本
内容创建
添加不同级别的标题
插入带有可选样式的段落
使用自定义数据创建表格
按比例缩放添加图片
插入分页符
文本格式化
格式化特定文本段落（加粗、斜体、下划线）
更改文本颜色和字体属性
对文本元素应用自定义样式
在整个文档中搜索和替换文本
Excel 操作
工作簿管理
创建新的 Excel 工作簿
打开现有的 Excel 文件
添加/删除/重命名工作表
数据处理
读取和写入单元格内容
插入/删除行和列
排序和筛选数据
应用公式和函数
PowerPoint 操作
演示文稿管理
创建新的 PowerPoint 演示文稿
添加/删除/重新排列幻灯片
设置幻灯片主题和背景
内容编辑
添加文本和图形元素
插入表格和图表
添加动画和过渡效果
高级功能
OCR 识别（从图像中提取文本）
文档比较（比较文档之间的差异）
文档翻译
文档加密和解密
表格数据导入/导出（数据库交互）
安装指南
先决条件
Python 3.7 或更高版本
pip 包管理器
Microsoft Office 或兼容组件（如 python-docx, openpyxl）
基本安装
bash
# 克隆仓库
git clone https://github.com/theWDY/office-editor-mcp.git
cd office-editor-mcp

# 安装依赖
pip install -r requirements.txt

配置
在 Cursor 中配置
方法 1：UI 配置
打开 Cursor
转到 设置 > 功能 > MCP
点击 "+ 添加新的 MCP 服务器"
填写配置信息：
名称：Office 助手（可根据需要修改）
类型：选择 stdio
命令：输入运行服务器的完整路径，例如：
python /path/to/office_server.py
注意：请替换为您的实际文件路径

方法 2：JSON 配置文件（推荐）
在项目目录中创建 .cursor 文件夹（如果不存在）
在该文件夹中创建 mcp.json 文件，并包含以下内容：
json
{
  "mcpServers": {
    "office-assistant": {
      "command": "python",
      "args": ["/path/to/office_server.py"],
      "env": {}
    }
  }
}

在 Claude for Desktop 中配置
编辑 Claude 配置文件：

macOS: ~/Library/Application Support/Claude/claude_desktop_config.json
Windows: %APPDATA%\Claude\claude_desktop_config.json
添加以下配置：
json
{
  "mcpServers": {
    "office-document-server": {
      "command": "python",
      "args": [
        "/path/to/office_server.py"
      ]
    }
  }
}

重启 Claude 以应用配置。
使用示例
配置完成后，您可以向 AI 助手发出如下命令：

Word 文档操作
"创建一个名为 'quarterly_report.docx' 的新文档，并添加封面页"
"向文档中添加一个标题和三个段落"
"插入一个 4x4 的销售数据表格"
"将第 2 段中的 'important' 一词加粗并设为红色"
"搜索并替换所有 'old term' 为 'new term'"

Excel 操作
"创建一个名为 'financial_analysis.xlsx' 的新 Excel 工作簿"
"在 A1 单元格中插入 '季度销售' 作为标题"
"创建一个包含部门销售数据的表格并计算总和"创建销售数据的条形图
按降序对B列中的数据进行排序
PowerPoint 操作
创建名为 'project_presentation.pptx' 的演示文稿
添加标题为 'Project Overview' 的新幻灯片
在第2张幻灯片中插入公司徽标
为标题添加飞入动画
API 参考
Word 文档操作
# 文档创建和属性
create_document(filename, title=None, author=None)
get_document_info(filename)
get_document_text(filename)
get_document_outline(filename)
list_available_documents(directory=".")
copy_document(source_filename, destination_filename=None)

# 内容添加
add_heading(filename, text, level=1)
add_paragraph(filename, text, style=None)
add_table(filename, rows, cols, data=None)
add_picture(filename, image_path, width=None)
add_page_break(filename)

# 文本格式化
format_text(filename, paragraph_index, start_pos, end_pos, bold=None, 
            italic=None, underline=None, color=None, font_size=None, font_name=None)
search_and_replace(filename, find_text, replace_text)
delete_paragraph(filename, paragraph_index)
create_custom_style(filename, style_name, bold=None, italic=None, 
                    font_size=None, font_name=None, color=None, base_style=None)
Excel 操作
# 工作簿操作
create_workbook(filename)
open_workbook(filename)
save_workbook(filename, new_filename=None)
add_worksheet(filename, sheet_name=None)
list_worksheets(filename)

# 单元格操作
read_cell(filename, sheet_name, cell_reference)
write_cell(filename, sheet_name, cell_reference, value)
format_cell(filename, sheet_name, cell_reference, **format_args)
PowerPoint 操作
# 演示文稿操作
create_presentation(filename)
open_presentation(filename)
save_presentation(filename, new_filename=None)
add_slide(filename, layout=None)
故障排除
常见问题
缺少样式

某些文档可能缺少用于标题和表格操作所需的样式
服务器将尝试创建缺失的样式或使用直接格式化
为了获得最佳效果，请使用带有标准 Office 样式的模板
权限问题

确保服务器具有读取/写入文档路径的权限
使用 copy_document 函数为锁定的文档创建可编辑副本
如果操作失败，请检查文件所有权和权限
图像插入问题

使用绝对路径指定图像文件
验证图像格式兼容性（推荐使用 JPEG、PNG）
检查图像文件大小和权限
调试
通过设置环境变量启用详细日志记录：

export MCP_DEBUG=1  # Linux/macOS
set MCP_DEBUG=1     # Windows
实现进度
✅ 构建 MCP 服务器基本框架
✅ 成功与 AI 助手集成
✅ 基本 Word 文档操作
✅ 基本 Excel 工作簿操作
✅ 基本 PowerPoint 演示文稿操作
✅ 高级功能增强
✅ 性能优化
✅ 跨平台兼容性测试
贡献
欢迎贡献！请随时提交 Pull Request。

分叉仓库
创建你的特性分支 (git checkout -b feature/amazing-feature)
提交更改 (git commit -m 'Add some amazing feature')
推送到分支 (git push origin feature/amazing-feature)
打开 Pull Request
许可证
此项目根据 MIT 许可证发布 - 详情请参阅 LICENSE 文件。

致谢
Model Context Protocol 用于协议规范
python-docx 用于 Word 文档处理
openpyxl 用于 Excel 处理
python-pptx 用于 PowerPoint 处理
注意：此服务器会与系统上的文档文件交互。在 AI 助手或其他 MCP 客户端中确认请求的操作之前，请始终验证这些操作是否适当。

**官方网站：** [https://pypi.org/project/office-editor-mcp/](https://pypi.org/project/office-editor-mcp/)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`memory`
- 标签：`knowledge and memory`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`--from office-editor-mcp==0.2.1 pptserver`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/lesyeuxderr-office-editor.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
