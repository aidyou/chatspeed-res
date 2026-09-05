---
title: "word文档编辑mcp全面升级版(支持本地和web上传)"
description: "一个功能强大的 Word 文档处理 MCP 服务，提供文档结构提取、内容修改、云存储集成等完整的文档处理解决方案。支持从URL下载文档、批量修改内容、自动上传到阿里云OSS等功能，完全兼容MCP协议，可无缝集成到各种AI助手中。"
---

# word文档编辑mcp全面升级版(支持本地和web上传)

一个功能强大的 Word 文档处理 MCP 服务，提供文档结构提取、内容修改、云存储集成等完整的文档处理解决方案。支持从URL下载文档、批量修改内容、自动上传到阿里云OSS等功能，完全兼容MCP协议，可无缝集成到各种AI助手中。

# 📚 DOCX MCP 完整用户指南

## 🌟 项目简介

**DOCX MCP** 是一个功能强大的 Word 文档处理工具，基于 MCP (Model Context Protocol) 协议，提供 42 个专业的文档处理工具，支持智能表格分析、自动化填充、文档生成等高级功能。

### 核心特性

- 🎯 **42个MCP工具**: 涵盖文档管理、表格处理、图片编辑等全方位功能
- 🤖 **AI友好**: 完美适配 Claude、ChatGPT 等 AI 助手
- 📊 **智能表格**: 自动识别表格结构，智能填充数据
- 🎨 **丰富格式**: 支持文本、图片、表格的精细化格式控制
- 🚀 **高性能**: 基于 FastMCP 框架，快速响应
- 🔧 **易集成**: 标准 MCP 协议，轻松接入各类应用

---

## 📦 快速安装

### 方式1：使用 pip（推荐）

```bash
pip install docx-mcp
```

### 方式2：使用 uv（更快）

```bash
uv pip install docx-mcp
```

### 方式3：使用 uvx（临时运行）

```bash
uvx docx-mcp
```

### 验证安装

```bash
# 检查版本
pip show docx-mcp

# 测试命令
docx-mcp --help
```

---

## 🚀 快速开始

### 1. 作为 MCP 服务器运行

```bash
# 启动 MCP 服务器
docx-mcp

# 或使用 uvx（无需安装）
uvx docx-mcp
```

服务器启动后会显示：
```
启动最终完整MCP服务器...
功能模块:
- 📊 工具分类（42个）
- 📁 文档管理工具 (8个)
- ✍️ 文本内容工具 (5个)
- 📊 表格操作工具 (6个)
- 🔍 表格分析工具 (5个)
- 📝 表格填充工具 (4个)
- 🖼️ 图片处理工具 (3个)
- 📐 页面设置工具 (3个)
- 🧠 智能功能工具 (5个)
- ⚙️ 系统状态工具 (3个)
...
总计: 42个工具
```

### 2. 配置 Claude Desktop

编辑 `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "docx-mcp": {
      "command": "uvx",
      "args": ["docx-mcp"]
    }
  }
}
```

**配置文件位置**:
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

---

## 🛠️ 42个工具完整列表

### 📁 文档管理工具 (8个)

#### 1. `create_document`
创建新的 Word 文档

**参数**:
- `file_path` (必需): 文档保存路径

**示例**:
```python
create_document("report.docx")
```

#### 2. `open_document`
打开现有文档

**参数**:
- `file_path` (必需): 文档路径

#### 3. `save_document`
保存当前文档

#### 4. `save_as_document`
另存为新文档

**参数**:
- `new_file_path` (必需): 新文档路径

#### 5. `close_document`
关闭当前文档

#### 6. `get_document_info`
获取文档信息（段落数、表格数等）

#### 7. `copy_document`
复制文档到新位置

**参数**:
- `source_path` (必需): 源文件路径
- `target_path` (必需): 目标路径

#### 8. `create_work_copy`
创建文档的工作副本

**参数**:
- `file_path` (必需): 原文件路径
- `suffix` (可选): 后缀名，默认"_工作版"

---

### ✍️ 文本内容工具 (5个)

#### 9. `add_paragraph`
添加段落

**参数**:
- `text` (必需): 段落文本
- `bold` (可选): 是否粗体
- `italic` (可选): 是否斜体
- `underline` (可选): 是否下划线
- `font_size` (可选): 字体大小
- `font_name` (可选): 字体名称
- `color` (可选): 颜色（十六进制）
- `alignment` (可选): 对齐方式

**示例**:
```python
add_paragraph(
    text="这是重要内容",
    bold=True,
    font_size=14,
    color="#FF0000",
    alignment="center"
)
```

#### 10. `add_heading`
添加标题

**参数**:
- `text` (必需): 标题文本
- `level` (可选): 标题级别（1-9）

#### 11. `add_text_with_formatting`
添加精确格式化的文本

#### 12. `search_and_replace`
搜索并替换文本

**参数**:
- `search_text` (必需): 搜索文本
- `replace_text` (必需): 替换文本
- `case_sensitive` (可选): 是否区分大小写

#### 13. `smart_add_content`
智能添加内容（自动识别类型）

**参数**:
- `content` (必需): 内容
- `content_type` (可选): 类型（paragraph/heading/list）
- `style` (可选): 样式（normal/emphasis/quote）
- `auto_format` (可选): 自动格式化

---

### 📊 表格操作工具 (6个)

#### 14. `add_table`
添加表格

**参数**:
- `rows` (必需): 行数
- `cols` (必需): 列数
- `data` (可选): 表格数据（二维数组）
- `has_header` (可选): 是否有表头

**示例**:
```python
add_table(
    rows=3,
    cols=3,
    data=[
        ["姓名", "年龄", "职业"],
        ["张三", "25", "工程师"],
        ["李四", "30", "设计师"]
    ],
    has_header=True
)
```

#### 15. `add_table_row`
添加表格行

**参数**:
- `table_index` (必需): 表格索引
- `row_data` (必需): 行数据数组

#### 16. `add_table_column`
添加表格列

**参数**:
- `table_index` (必需): 表格索引
- `column_index` (可选): 插入位置
- `data` (可选): 列数据

#### 17. `format_table`
格式化表格

**参数**:
- `table_index` (必需): 表格索引
- `style` (可选): 表格样式

#### 18. `merge_table_cells`
合并表格单元格

**参数**:
- `table_index` (必需): 表格索引
- `row_start` (必需): 起始行
- `col_start` (必需): 起始列
- `row_end` (必需): 结束行
- `col_end` (必需): 结束列

#### 19. `intelligent_create_table`
智能创建表格（自动样式）

**参数**:
- `data` (必需): 表格数据（二维数组）
- `auto_style` (可选): 自动应用样式

---

### 🔍 表格分析工具 (5个)

#### 20. `extract_table_structure`
提取表格结构（完整分析）

**参数**:
- `file_path` (必需): 文档路径
- `table_index` (必需): 表格索引

**返回**: JSON格式的详细表格结构

**示例**:
```python
structure = extract_table_structure("report.docx", 0)
# 返回：表格行列数、单元格内容、合并信息等
```

#### 21. `extract_all_tables_structure`
提取所有表格结构

**参数**:
- `file_path` (必需): 文档路径

#### 22. `extract_document_structure`
提取完整文档结构

**参数**:
- `file_path` (必需): 文档路径
- `include_cell_details` (可选): 是否包含单元格详情

#### 23. `get_table_structure_cache_info`
获取表格结构缓存信息

#### 24. `clear_table_structure_cache`
清空表格结构缓存

---

### 📝 表格填充工具 (4个)

#### 25. `extract_fillable_fields`
提取可填充字段（坐标专用）

**参数**:
- `file_path` (必需): 文档路径

**返回**: 字段坐标映射、空位信息、填充建议

**示例**:
```python
fields = extract_fillable_fields("template.docx")
# 返回：{"field_coordinates": {"姓名": [0, 1, 2]}, ...}
```

#### 26. `fill_with_coordinates`
使用坐标填充（主要功能）

**参数**:
- `file_path` (必需): 文档路径
- `coordinate_data` (必需): 坐标数据字典

**示例**:
```python
fill_with_coordinates(
    "template.docx",
    {
        "张三": [0, 1, 2],  # [表格索引, 行, 列]
        "2023001": [0, 2, 2],
        "计算机学院": [0, 3, 2]
    }
)
```

#### 27. `basic_table_fill`
基础表格填充（智能匹配）

**参数**:
- `file_path` (必需): 文档路径
- `fill_data` (必需): 填充数据字典

**示例**:
```python
basic_table_fill(
    "template.docx",
    {
        "姓名": "张三",
        "学号": "2023001",
        "学院": "计算机学院",
        "专业": "计算机科学与技术"
    }
)
```

#### 28. `intelligent_table_fill`
智能表格填充（辅助功能）

---

### 🖼️ 图片处理工具 (3个)

#### 29. `add_image`
添加图片

**参数**:
- `image_path` (必需): 图片路径
- `width` (可选): 宽度（英寸）
- `height` (可选): 高度（英寸）

**示例**:
```python
add_image("logo.png", width=3, height=2)
```

#### 30. `extract_images`
提取文档中的所有图片

**参数**:
- `output_dir` (可选): 输出目录

#### 31. `resize_image`
调整图片大小

**参数**:
- `image_index` (必需): 图片索引
- `width` (必需): 新宽度
- `height` (必需): 新高度

---

### 📐 页面设置工具 (3个)

#### 32. `set_page_margins`
设置页边距

**参数**:
- `top` (可选): 上边距（英寸）
- `bottom` (可选): 下边距
- `left` (可选): 左边距
- `right` (可选): 右边距

**示例**:
```python
set_page_margins(top=1, bottom=1, left=1.5, right=1.5)
```

#### 33. `set_page_orientation`
设置页面方向

**参数**:
- `orientation` (可选): portrait（纵向）或 landscape（横向）

#### 34. `set_page_size`
设置页面大小

**参数**:
- `width` (可选): 宽度（英寸）
- `height` (可选): 高度（英寸）

---

### 🧠 智能功能工具 (5个)

#### 35. `intelligent_create_document`
智能创建文档（含模板）

**参数**:
- `file_path` (必需): 文档路径
- `template_type` (可选): 模板类型
  - `basic`: 基础文档
  - `business`: 商务文档
  - `academic`: 学术论文
- `auto_optimize` (可选): 自动优化页面

**示例**:
```python
intelligent_create_document(
    "report.docx",
    template_type="business",
    auto_optimize=True
)
```

#### 36. `get_smart_suggestions`
获取智能建议

**参数**:
- `context` (可选): 上下文类型
  - `document_editing`: 文档编辑
  - `table_creation`: 表格创建
  - `content_formatting`: 内容格式化
  - `structure_optimization`: 结构优化
  - `professional_polish`: 专业润色

#### 37. `get_intelligent_planning_guide`
获取智能规划指导

**返回**: AI使用MCP工具的完整指南

#### 38. `create_intelligent_workflow_plan`
创建智能工作流规划

**参数**:
- `user_request` (必需): 用户请求描述

**返回**: 详细的工具调用计划

#### 39. `get_tool_detailed_guidance`
获取工具详细指导

**参数**:
- `tool_name` (必需): 工具名称

---

### ⚙️ 系统状态工具 (3个)

#### 40. `get_system_status`
获取系统状态

**返回**: 当前文档状态、可用工具列表等

#### 41. `test_connection`
测试连接

**返回**: 连接状态确认

#### 42. `get_server_info`
获取服务器信息

**返回**: 服务器版本、功能列表等

---

## 💡 使用场景示例

### 场景1：批量生成报告

```python
from final_complete_server import *

# 1. 创建文档
intelligent_create_document("report.docx", "business", True)

# 2. 添加标题
add_heading("月度工作报告", level=1)

# 3. 添加表格
intelligent_create_table([
    ["项目名称", "完成度", "备注"],
    ["项目A", "100%", "已完成"],
    ["项目B", "80%", "进行中"]
])

# 4. 保存
save_document()
```

### 场景2：智能填充表单

```python
from core.universal_table_filler import UniversalTableFiller

filler = UniversalTableFiller()

# 1. 分析表格结构
coordinates = filler.analyze_and_get_coordinates("template.docx")

# 2. 准备数据
data = {
    "姓名": "张三",
    "学号": "2023001",
    "学院": "计算机学院",
    "专业": "计算机科学与技术",
    "联系方式": "13800138000"
}

# 3. 智能填充
fill_with_coordinates("template.docx", {
    "张三": [0, 1, 2],
    "2023001": [0, 2, 2],
    "计算机学院": [0, 3, 2],
    "计算机科学与技术": [0, 4, 2],
    "13800138000": [0, 5, 2]
})
```

### 场景3：文档批量处理

```python
import os
from pathlib import Path

# 批量处理文件夹中的所有文档
folder = Path("documents")
for doc in folder.glob("*.docx"):
    # 打开文档
    open_document(str(doc))
    
    # 添加页码
    add_paragraph(f"第 {{PAGE}} 页", alignment="center")
    
    # 统一页边距
    set_page_margins(1, 1, 1, 1)
    
    # 保存
    save_document()
    close_document()
```

---

## 🎯 高级功能

### 1. 表格结构分析

```python
from core.table_structure_extractor import table_extractor

# 提取表格结构
structure = table_extractor.extract_table_structure("document.docx", 0)

# 获取表格信息
print(f"行数: {structure.rows}")
print(f"列数: {structure.columns}")
print(f"表格类型: {structure.table_type}")
print(f"页面格式: {structure.page_format}")

# 遍历单元格
for row in structure.cells:
    for cell in row:
        print(f"({cell.row_index}, {cell.col_index}): {cell.text}")
```

### 2. 智能工作流规划

```python
from core.intelligent_tool_planner import intelligent_planner

# 获取工具规划
plan = intelligent_planner.create_intelligent_plan(
    "创建一个学生信息表，包含姓名、学号、班级，并填充示例数据"
)

# 按计划执行
for step in plan.workflow_steps:
    print(f"步骤 {step.step_id}: {step.description}")
    print(f"工具: {step.tool_name}")
    print(f"参数: {step.parameters}")
```

### 3. 自定义模板

```python
# 创建自定义业务模板
intelligent_create_document("template.docx", "business")

# 添加公司信息
add_paragraph("ABC公司", bold=True, font_size=16, alignment="center")
add_paragraph("地址：XX市XX路XX号")
add_paragraph("电话：021-12345678")

# 添加表格框架
add_table(10, 3, has_header=True)

# 保存为模板
save_as_document("custom_template.docx")
```

---

## 🔧 配置与优化

### 环境变量配置

```bash
# 设置缓存目录
export UV_CACHE_DIR=/path/to/cache

# 禁用进度条
export UV_NO_PROGRESS=1

# 使用国内镜像
export UV_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple
```

### 性能优化建议

1. **使用缓存**: 表格结构会自动缓存，提高重复操作速度
2. **批量操作**: 尽量打开文档后一次性完成多个操作
3. **合理使用工具**: 根据需求选择合适的工具（如基础vs智能）

---

## 🐛 常见问题

### Q1: 安装失败怎么办？

```bash
# 方式1：使用国内镜像
pip install docx-mcp -i https://pypi.tuna.tsinghua.edu.cn/simple

# 方式2：升级pip
python -m pip install --upgrade pip
pip install docx-mcp

# 方式3：使用uv（更快）
curl -LsSf https://astral.sh/uv/install.sh | sh
uv pip install docx-mcp
```

### Q2: 导入模块失败？

```python
# 确保使用正确的导入方式
from final_complete_server import mcp  # ✅ 正确
# from docx_mcp import mcp  # ❌ 错误
```

### Q3: 表格填充不准确？

```python
# 推荐使用坐标填充方式
# 1. 先分析结构
fields = extract_fillable_fields("template.docx")

# 2. 根据返回的坐标信息填充
fill_with_coordinates("template.docx", coordinate_data)
```

### Q4: 如何调试？

```python
# 启用详细日志
import logging
logging.basicConfig(level=logging.DEBUG)

# 查看工具列表
status = get_system_status()
print(status)
```

---

## 📝 API 参考

### Python API

```python
# 导入方式
from final_complete_server import mcp
from core.universal_table_filler import UniversalTableFiller
from core.intelligent_table_analyzer import IntelligentTableAnalyzer
from core.table_structure_extractor import table_extractor
```

### MCP Protocol API

作为 MCP 服务器运行时，通过标准 MCP 协议调用工具：

```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": {
    "name": "create_document",
    "arguments": {
      "file_path": "example.docx"
    }
  }
}
```

---

## 🔗 相关链接

- **PyPI**: https://pypi.org/project/docx-mcp/
- **GitHub**: https://github.com/rockcj/Docx_MCP_cj
- **问题反馈**: https://github.com/rockcj/Docx_MCP_cj/issues
- **MCP协议**: https://modelcontextprotocol.io/
- **FastMCP**: https://gofastmcp.com

---

## 📄 许可证

MIT License

---

## 🙏 致谢

感谢所有贡献者和用户的支持！

---

**版本**: 0.1.6  
**更新时间**: 2025-10-02  
**作者**: DOCX MCP Team

---

## 📞 获取帮助

如果遇到问题或需要帮助：

1. 查看本文档的常见问题部分
2. 访问 GitHub Issues
3. 查看示例代码
4. 联系维护团队

Happy Documenting! 📝✨

**官方网站：** [https://github.com/rockcj/Docx_MCP_cj.git](https://github.com/rockcj/Docx_MCP_cj.git)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`files`
- 标签：`file systems`, `ai智能化处理docx文档助手`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`docx-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/rockcj-docx.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
