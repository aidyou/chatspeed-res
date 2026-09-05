---
title: "德国可再生能源数据工具"
description: "为大型语言模型提供德国可再生能源项目相关的新闻和信息访问，并允许按照位置、主题（太阳能、风能、氢能）以及日期范围进行筛选。"
---

# 德国可再生能源数据工具

为大型语言模型提供德国可再生能源项目相关的新闻和信息访问，并允许按照位置、主题（太阳能、风能、氢能）以及日期范围进行筛选。

# Nefino MCP 服务器

Nefino MCP 服务器是一个 [模型上下文协议 (MCP)](https://modelcontextprotocol.io) 服务器，它为大型语言模型（LLMs）提供关于德国可再生能源项目、规划和公告的新闻和信息。它与 Nefino API 集成，以提供对这些数据的结构化访问。

## 功能

- 检索特定地理位置的新闻条目
- 按各种可再生能源主题过滤（太阳能、风能、氢能等）
- 支持按日期范围和最近性查询
- 通过环境变量进行安全认证
- 输入验证和错误处理
- 完全符合 MCP 协议

## 安装

### 前提条件

- Python 3.10 或更高版本
- 访问 Nefino API（需要凭证）

### 安装

```bash
pip install git+https://github.com/nefino/mcp-nefino.git
```

## 配置

服务器需要设置几个环境变量。在运行服务器时应直接传递这些变量。

```bash
NEFINO_USERNAME=your_username
NEFINO_PASSWORD=your_password
NEFINO_JWT_SECRET=your_jwt_secret
NEFINO_BASE_URL=http://api_endpoint
```

## 使用方法

### 与 Claude Desktop 一起使用

1. 安装 [Claude Desktop](https://claude.ai/download)

2. 在您的 Claude Desktop 配置文件中添加以下内容（macOS 上为 `~/Library/Application Support/Claude/claude_desktop_config.json`，Windows 上为 `%APPDATA%\Claude\claude_desktop_config.json`）：

```json
{
  "mcpServers": {
    "nefino": {
      "command": "python",
      "args": ["-m", "mcp_nefino"],
      "env": {
        "NEFINO_USERNAME": "your_username",
        "NEFINO_PASSWORD": "your_password",
        "NEFINO_JWT_SECRET": "your_jwt_secret",
        "NEFINO_BASE_URL": "http://api_endpoint"
      }
    }
  }
}
```

3. 重启 Claude Desktop

### 直接使用

您也可以直接运行服务器：

```bash
python -m mcp_nefino
```

## 可用工具

### retrieve_news_items_for_place

检索具有各种过滤选项的特定位置的新闻条目。

参数：
- `place_id` (字符串)：地点的 ID
- `place_type` (枚举)：地点类型 (PR, CTY, AU, LAU)
- `range_or_recency` (枚举, 可选)：RANGE 或 RECENCY
- `last_n_days` (整数, 可选)：回溯天数（仅在 RECENCY 模式下有效）
- `date_range_begin` (字符串, 可选)：开始日期（格式为 YYYY-MM-DD，仅在 RANGE 模式下有效）
- `date_range_end` (字符串, 可选)：结束日期（格式为 YYYY-MM-DD，仅在 RANGE 模式下有效）
- `news_topics` (枚举列表, 可选)：要过滤的主题 (BATTERY_STORAGE, GRID_EXPANSION, SOLAR, HYDROGEN, WIND)

通过 Claude 的示例查询：
```
Get renewable energy news for administrative unit DE9_AU0213 from January to June 2024, focusing on solar projects.
```

## 开发

要在开发模式下使用 MCP Inspector 运行：

```bash
mcp dev -m mcp_nefino
```

## 错误处理

服务器执行以下验证：
- 日期格式 (YYYY-MM-DD)
- 日期范围的有效性
- RANGE 和 RECENCY 模式的参数组合
- API 凭证和连接性
- 新闻主题的有效性

所有错误都附有描述性消息，有助于诊断问题。

## 许可证

[许可证类型 - 例如，MIT] - 请参阅 LICENSE 文件获取详细信息

**官方网站：** [https://github.com/nefino/mcp-nefino](https://github.com/nefino/mcp-nefino)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`research and data`, `location services`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`python`
- 参数：`-m mcp_nefino`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/nefino-nefino.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
