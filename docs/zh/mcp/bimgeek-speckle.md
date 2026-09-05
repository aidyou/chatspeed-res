---
title: "Speckle 中间件桥"
description: "一座连接Speckle API和客户端应用程序的桥梁，使用户能够列出/搜索项目、访问模型版本以及从Speckle协作数据中心检索/查询对象及其属性，该数据中心专为AEC工具设计。"
---

# Speckle 中间件桥

一座连接Speckle API和客户端应用程序的桥梁，使用户能够列出/搜索项目、访问模型版本以及从Speckle协作数据中心检索/查询对象及其属性，该数据中心专为AEC工具设计。

# Speckle MCP 服务器

一个用于与Speckle（一种连接到您的AEC工具的协作数据中心）交互的模型上下文协议（MCP）服务器。

## 概览

此MCP服务器充当Speckle API和客户端应用程序之间的桥梁，并提供一组工具，允许用户：

- 列出并搜索Speckle项目
- 获取详细的项目信息
- 访问项目内的模型版本
- 从特定版本中检索和查询对象及其属性

## 安装

### 先决条件

- Python 3.13或更高版本
- 带有个人访问令牌的Speckle帐户
- uv 用于依赖管理和虚拟环境

### 设置

1. 克隆此仓库：
```bash
   git clone https://github.com/bimgeek/speckle-mcp.git
   cd speckle-mcp
```

2. 确保已安装Python 3.13：
```bash
   python --version  # 应显示 Python 3.13.x
```

3. 使用uv安装依赖项：
```bash
   uv pip install -r requirements.txt
```

## 配置

### 环境变量

服务器需要以下环境变量：

- `SPECKLE_TOKEN`：您的Speckle个人访问令牌（必需）
- `SPECKLE_SERVER`：Speckle服务器URL（默认为 https://app.speckle.systems）

### MCP 配置

要将此服务器与Claude一起使用，您需要更新您的MCP配置文件。配置文件通常位于：

- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

在`mcpServers`部分添加或更新"speckle"条目：

```json
{
  "mcpServers": {
    "speckle": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/speckle-mcp",
        "run",
        "speckle_server.py"
      ],
      "env": {
        "SPECKLE_TOKEN": "YOUR_SPECKLE_API_TOKEN_HERE",
        "SPECKLE_SERVER": "https://app.speckle.systems"
      }
    }
  }
}
```

将`/path/to/speckle-mcp`替换为包含`speckle_mcp`包的实际目录路径。

## 可用工具

### 项目

- `list_projects`：列出所有可访问的Speckle项目
  - 参数：
    - `limit`（可选）：要检索的最大项目数量（默认值：20）

- `get_project_details`：检索特定项目的详细信息
  - 参数：
    - `project_id`：要检索的Speckle项目的ID
    - `limit`（可选）：要检索的最大模型数量（默认值：20）

- `search_projects`：按名称或描述搜索项目
  - 参数：
    - `query`：要在项目名称和描述中查找的搜索词

### 模型

- `get_model_versions`：列出特定模型的所有版本
  - 参数：
    - `project_id`：Speckle项目的ID
    - `model_id`：要检索版本的模型ID
    - `limit`（可选）：要检索的最大版本数量（默认值：20）

### 对象

- `get_version_objects`: 从特定版本检索对象
  - 参数：
    - `project_id`: Speckle 项目的 ID
    - `version_id`: 要从中检索对象的版本的 ID
    - `include_children` (可选): 是否在响应中包含子对象（默认：false）

- `query_object_properties`: 从版本中的对象查询特定属性
  - 参数：
    - `project_id`: Speckle 项目的 ID
    - `version_id`: 要从中检索对象的版本的 ID
    - `property_path`: 属性的点表示法路径（例如，"elements.0.name"）

## 故障排除

- 如果遇到身份验证问题，请确保您的 Speckle 令牌有效并且具有必要的权限
- 查看服务器日志以获取详细的错误消息
- 确保在 MCP 配置中正确设置了环境变量

## 许可证

本项目根据 MIT 许可证许可 - 有关详细信息，请参阅 LICENSE 文件。

**官方网站：** [https://github.com/bimgeek/speckle-mcp](https://github.com/bimgeek/speckle-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`art and culture`, `databases`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`--directory /path/to/speckle-mcp run speckle_server.py`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/bimgeek-speckle.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
