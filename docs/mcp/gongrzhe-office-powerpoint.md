---
title: "PowerPoint MCP 服务器"
description: "通过模型上下文协议（Model Context Protocol）实现创建和编辑 PowerPoint 演示文稿的服务器，支持添加幻灯片、图像、文本框、图表和表格等功能。"
---

# PowerPoint MCP 服务器

通过模型上下文协议（Model Context Protocol）实现创建和编辑 PowerPoint 演示文稿的服务器，支持添加幻灯片、图像、文本框、图表和表格等功能。

# Office-PowerPoint-MCP-Server
[Smithery](https://smithery.ai/server/@GongRzhe/Office-PowerPoint-MCP-Server)
![](/mcp-assets/c1486b4e2d8cfd67ed0257afeefda188.svg 'MCP Server')

这是一个使用 `python-pptx` 的 PowerPoint 操控 MCP（Model Context Protocol）服务器。该服务器通过 MCP 协议提供创建、编辑和操控 PowerPoint 演示文稿的工具。

### 示例

#### 提示

#### 输出

#### 演示 GIF -> (./public/demo.mp4)

## 功能

- 往返任何 Open XML 演示文稿（.pptx 文件），包括其所有元素
- 添加幻灯片
- 填充文本占位符，例如创建项目符号幻灯片
- 在任意位置和大小向幻灯片添加图片
- 向幻灯片添加文本框；操控文本字体大小和加粗
- 向幻灯片添加表格
- 向幻灯片添加自定义形状（例如多边形、流程图形状等）
- 添加并操控柱状图、条形图、折线图和饼图
- 访问并更改核心文档属性，如标题和主题

## 安装

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@GongRzhe/Office-PowerPoint-MCP-Server) 自动为 Claude Desktop 安装 PowerPoint 操控服务器：

```bash
npx -y @smithery/cli install @GongRzhe/Office-PowerPoint-MCP-Server --client claude
```

### 先决条件

- Python 3.10 或更高版本
- pip 包管理器

### 安装选项

#### 选项 1：使用设置脚本（推荐）

最简单的方法是使用提供的设置脚本来配置 PowerPoint MCP 服务器，该脚本会自动化安装过程：

```bash
python setup_mcp.py
```

此脚本将：
- 检查先决条件
- 提供安装选项：
  - 从 PyPI 安装（推荐大多数用户使用）
  - 设置本地开发环境
- 安装所需依赖项
- 生成适当的 MCP 配置文件
- 提供与 Claude Desktop 集成的说明

该脚本根据您的环境提供不同的路径：
- 如果您已安装 `uvx`，它将使用 UVX 进行配置（推荐）
- 如果服务器已经安装，它会提供配置选项
- 如果服务器未安装，它会提供安装方法

#### 选项 2：手动安装

1. 克隆仓库：
```bash
   git clone https://github.com/GongRzhe/Office-PowerPoint-MCP-Server.git
   cd Office-PowerPoint-MCP-Server
```

2. 安装依赖项：
```bash
   pip install -r requirements.txt
```

3. 使服务器可执行：
```bash
   chmod +x ppt_mcp_server.py
```

## 使用

### 启动服务器

运行服务器：

```bash
python ppt_mcp_server.py
```

### MCP 配置

#### 选项 1：本地 Python 服务器

将服务器添加到您的 MCP 设置配置文件中：

```json
{
  "mcpServers": {
    "ppt": {
      "command": "python",
      "args": ["/path/to/ppt_mcp_server.py"],
      "env": {}
    }
  }
}
```

#### 选项 2：使用 UVX（无需本地安装）

如果你已经安装了 `uvx`，你可以直接从 PyPI 运行服务器而无需本地安装：

```json
{
  "mcpServers": {
    "ppt": {
      "command": "uvx",
      "args": [
        "--from", "office-powerpoint-mcp-server", "ppt_mcp_server"
      ],
      "env": {}
    }
  }
}
```

## 可用工具

### 演示文稿工具

- **create_presentation**: 创建一个新的 PowerPoint 演示文稿
- **open_presentation**: 从文件中打开一个现有的 PowerPoint 演示文稿
- **save_presentation**: 将当前演示文稿保存到文件
- **get_presentation_info**: 获取关于当前演示文稿的信息
- **set_core_properties**: 设置当前演示文稿的核心文档属性

### 幻灯片工具

- **add_slide**: 向当前演示文稿添加一张新幻灯片
- **get_slide_info**: 获取特定幻灯片的信息
- **populate_placeholder**: 用文本填充占位符
- **add_bullet_points**: 向占位符添加项目符号

### 文本工具

- **add_textbox**: 向幻灯片添加一个文本框

### 图像工具

- **add_image**: 向幻灯片添加一张图片
- **add_image_from_base64**: 从 base64 编码的字符串向幻灯片添加一张图片

### 表格工具

- **add_table**: 向幻灯片添加一个表格
- **format_table_cell**: 格式化表格单元格

### 形状工具

- **add_shape**: 向幻灯片添加一个自动形状

### 图表工具

- **add_chart**: 向幻灯片添加一个图表

## 示例

### 创建一个新的演示文稿

```python
# Create a new presentation
result = use_mcp_tool(
    server_name="ppt",
    tool_name="create_presentation",
    arguments={}
)
presentation_id = result["presentation_id"]

# Add a title slide
result = use_mcp_tool(
    server_name="ppt",
    tool_name="add_slide",
    arguments={
        "layout_index": 0,  # Title slide layout
        "title": "My Presentation",
        "presentation_id": presentation_id
    }
)
slide_index = result["slide_index"]

# Populate subtitle placeholder
result = use_mcp_tool(
    server_name="ppt",
    tool_name="populate_placeholder",
    arguments={
        "slide_index": slide_index,
        "placeholder_idx": 1,  # Subtitle placeholder
        "text": "Created with PowerPoint MCP Server",
        "presentation_id": presentation_id
    }
)

# Save the presentation
result = use_mcp_tool(
    server_name="ppt",
    tool_name="save_presentation",
    arguments={
        "file_path": "my_presentation.pptx",
        "presentation_id": presentation_id
    }
)
```

### 添加一个图表

```python
# Add a chart slide
result = use_mcp_tool(
    server_name="ppt",
    tool_name="add_slide",
    arguments={
        "layout_index": 1,  # Content slide layout
        "title": "Sales Data",
        "presentation_id": presentation_id
    }
)
slide_index = result["slide_index"]

# Add a column chart
result = use_mcp_tool(
    server_name="ppt",
    tool_name="add_chart",
    arguments={
        "slide_index": slide_index,
        "chart_type": "column",
        "left": 1.0,
        "top": 2.0,
        "width": 8.0,
        "height": 4.5,
        "categories": ["Q1", "Q2", "Q3", "Q4"],
        "series_names": ["2023", "2024"],
        "series_values": [
            [100, 120, 140, 160],
            [110, 130, 150, 170]
        ],
        "has_legend": True,
        "legend_position": "bottom",
        "has_data_labels": True,
        "title": "Quarterly Sales",
        "presentation_id": presentation_id
    }
)
```

## 许可证

MIT

**官方网站：** [https://github.com/GongRzhe/Office-PowerPoint-MCP-Server](https://github.com/GongRzhe/Office-PowerPoint-MCP-Server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`files`
- 标签：`file systems`, `developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`--from office-powerpoint-mcp-server ppt_mcp_server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/gongrzhe-office-powerpoint.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
