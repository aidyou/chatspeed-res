---
title: "MCP地点搜索"
description: "一个用于附近地点搜索的MCP服务器，具有基于IP的位置检测功能。"
---

# MCP地点搜索

一个用于附近地点搜索的MCP服务器，具有基于IP的位置检测功能。

# NearbySearch MCP Server

基于IP位置检测的附近地点搜索MCP服务器。

![GitHub License](/mcp-assets/5816f652aa1f0cc4eedb21a2f733e09e.svg) 
![GitHub Last Commit](/mcp-assets/4e70b12afff6d1394e76925e2c277c74.svg) 
![Python Version](/mcp-assets/405b7b46d001e379991916d79670861b.svg)

## 功能

- **基于IP的位置检测**：使用ipapi.co确定您的当前位置
- **Google Places集成**：根据关键词和可选类型过滤器搜索附近的地点
- **简单界面**：具有可自定义半径的单一工具端点

## 要求

- Python 3.10+
- 启用了Places API的Google Cloud Platform API密钥
- 互联网连接

## 安装

1. 克隆仓库：
```bash
git clone https://github.com/kukapay/nearby-search-mcp.git
cd nearby-search-mcp
```

2. 安装依赖项：
```bash
# Using uv (recommended)
uv add "mcp[cli]" httpx python-dotenv

# Or using pip
pip install mcp httpx python-dotenv
```

3. 客户端配置

```json
{
  "mcpServers": {
    "nearby-search": {
      "command": "uv",
      "args": ["--directory", "path/to/nearby-search-mcp", "run", "main.py"],
      "env": {
        "GOOGLE_API_KEY": "your google api key"
      }
    }
  }
}
```

## 使用方法

### 运行服务器

- **开发模式**（带有MCP Inspector）：
```bash
mcp dev main.py
```

- **在Claude Desktop中安装**：
```bash
mcp install main.py --name "NearbySearch"
```

- **直接执行**：
```bash
python main.py
```

### 可用端点

**工具: `search_nearby`**
 - 搜索您当前位置附近的地点
 - 参数：
   - `keyword` (str): 搜索内容（例如，“咖啡店”）
   - `radius` (int, 可选): 搜索半径（以米为单位，默认值：1500）
   - `type` (str, 可选): 地点类型（例如，“餐厅”，“咖啡馆”）

## 许可证

此项目根据MIT许可证发布 - 详情请参见[LICENSE](https://github.com/kukapay/nearby-search-mcp/blob/HEAD/LICENSE)文件。

**官方网站：** [https://github.com/kukapay/nearby-search-mcp](https://github.com/kukapay/nearby-search-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`location services`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`--directory path/to/nearby-search-mcp run main.py`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/kukapay-nearby-search.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
