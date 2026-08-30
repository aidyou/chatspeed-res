---
title: "数据集浏览器"
description: "启用与 Hugging Face 数据集查看器 API 的交互，允许用户浏览、搜索、过滤和分析托管在 Hugging Face Hub 上的数据集。"
---

# 数据集浏览器

启用与 Hugging Face 数据集查看器 API 的交互，允许用户浏览、搜索、过滤和分析托管在 Hugging Face Hub 上的数据集。

# Dataset Viewer MCP Server

一个用于与 [Hugging Face Dataset Viewer API](https://huggingface.co/docs/dataset-viewer) 交互的MCP服务器，提供了浏览和分析托管在Hugging Face Hub上的数据集的功能。

## 功能

### 资源

- 使用 `dataset://` URI 方案访问 Hugging Face 数据集
- 支持数据集配置和分割
- 提供分页访问数据集内容
- 处理私有数据集的身份验证
- 支持搜索和过滤数据集内容
- 提供数据集统计和分析

### 工具

服务器提供以下工具：

1. **validate**
   - 检查数据集是否存在且可访问
   - 参数：
     - `dataset`: 数据集标识符（例如 'stanfordnlp/imdb'）
     - `auth_token` (可选): 用于私有数据集

2. **get_info**
   - 获取关于数据集的详细信息
   - 参数：
     - `dataset`: 数据集标识符
     - `auth_token` (可选): 用于私有数据集

3. **get_rows**
   - 获取数据集的分页内容
   - 参数：
     - `dataset`: 数据集标识符
     - `config`: 配置名称
     - `split`: 分割名称
     - `page` (可选): 页码（从0开始）
     - `auth_token` (可选): 用于私有数据集

4. **get_first_rows**
   - 从数据集分割中获取前几行
   - 参数：
     - `dataset`: 数据集标识符
     - `config`: 配置名称
     - `split`: 分割名称
     - `auth_token` (可选): 用于私有数据集

5. **get_statistics**
   - 获取关于数据集分割的统计信息
   - 参数：
     - `dataset`: 数据集标识符
     - `config`: 配置名称
     - `split`: 分割名称
     - `auth_token` (可选): 用于私有数据集

6. **search_dataset**
   - 在数据集中搜索文本
   - 参数：
     - `dataset`: 数据集标识符
     - `config`: 配置名称
     - `split`: 分割名称
     - `query`: 要搜索的文本
     - `auth_token` (可选): 用于私有数据集

7. **filter**
   - 使用类似SQL的条件过滤行
   - 参数：
     - `dataset`: 数据集标识符
     - `config`: 配置名称
     - `split`: 分割名称
     - `where`: SQL WHERE 子句（例如 "score > 0.5"）
     - `orderby` (可选): SQL ORDER BY 子句
     - `page` (可选): 页码（从0开始）
     - `auth_token` (可选): 用于私有数据集

8. **get_parquet**
   - 以Parquet格式下载整个数据集
   - 参数：
     - `dataset`: 数据集标识符
     - `auth_token` (可选): 用于私有数据集

## 安装

### 前提条件

- Python 3.12 或更高版本
- [uv](https://github.com/astral-sh/uv) - 快速的Python包安装器和解析器

### 设置

1. 克隆仓库：
```bash
git clone https://github.com/privetin/dataset-viewer.git
cd dataset-viewer
```

2. 创建虚拟环境并安装：
```bash
# Create virtual environment
uv venv

# Activate virtual environment
# On Unix:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate

# Install in development mode
uv add -e .
```

## 配置

### 环境变量

- `HUGGINGFACE_TOKEN`: 用于访问私有数据集的Hugging Face API令牌

### Claude Desktop集成

将以下内容添加到您的Claude Desktop配置文件中：

在 Windows 上: `%APPDATA%\Claude\claude_desktop_config.json`

在 MacOS 上: `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "dataset-viewer": {
      "command": "uv",
      "args": [
        "run",
        "dataset-viewer"
      ]
    }
  }
}
```

## 使用示例

1. 验证数据集：
```json
{
  "dataset": "stanfordnlp/imdb"
}
```

2. 获取数据集信息：
```json
{
  "dataset": "stanfordnlp/imdb"
}
```

3. 搜索数据集内容：
```json
{
  "dataset": "stanfordnlp/imdb",
  "config": "plain_text",
  "split": "train",
  "query": "great movie"
}
```

4. 筛选并排序行：
```json
{
  "dataset": "stanfordnlp/imdb",
  "config": "plain_text",
  "split": "train",
  "where": "label = 'positive'",
  "orderby": "text DESC",
  "page": 0
}
```

5. 获取数据集统计信息：
```json
{
  "dataset": "stanfordnlp/imdb",
  "config": "plain_text",
  "split": "train"
}
```

## 许可证

MIT 许可证 - 详情请参阅 [LICENSE](https://github.com/privetin/dataset-viewer/blob/HEAD/LICENSE)

**官方网站：** [https://github.com/privetin/dataset-viewer](https://github.com/privetin/dataset-viewer)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`research and data`, `search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`run dataset-viewer`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/privetin-dataset-viewer.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
