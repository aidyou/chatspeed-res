---
title: "Strava健康数据分析服务器"
description: "一个模型上下文协议服务器，为语言模型提供对Strava API数据的访问，使它们能够查询和分析Strava上的运动员活动。"
---

# Strava健康数据分析服务器

一个模型上下文协议服务器，为语言模型提供对Strava API数据的访问，使它们能够查询和分析Strava上的运动员活动。

# Strava MCP 服务器

![Python Package](/mcp-assets/b34dd1f9c1c9445c7bad4f893b73a785.svg)
[![License: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10](/mcp-assets/9a5462509af74d8a0229903fa0c244e1.svg)](https://www.python.org/downloads/release/python-3100/)

这是一个 [Model Context Protocol](https://modelcontextprotocol.io/introduction) (MCP) 服务器，提供对 Strava API 的访问。它允许语言模型从 Strava API 查询运动员活动数据。

## 可用工具

该服务器提供了以下工具：

### 活动查询

- `get_activities(limit: int = 10)`: 获取已认证运动员的最近活动
- `get_activities_by_date_range(start_date: str, end_date: str, limit: int = 30)`: 获取特定日期范围内的活动
- `get_activity_by_id(activity_id: int)`: 获取特定活动的详细信息
- `get_recent_activities(days: int = 7, limit: int = 10)`: 获取过去 X 天内的活动

日期应以 ISO 格式 (`YYYY-MM-DD`) 提供。

## 活动数据格式

服务器返回的活动数据具有统一的字段名称和单位：

| 字段 | 描述 | 单位 |
|-------|-------------|------|
| `name` | 活动名称 | - |
| `sport_type` | 运动类型 | - |
| `start_date` | 开始日期和时间 | ISO 8601 |
| `distance_metres` | 距离 | 米 |
| `elapsed_time_seconds` | 总经过时间 | 秒 |
| `moving_time_seconds` | 移动时间 | 秒 |
| `average_speed_mps` | 平均速度 | 米/秒 |
| `max_speed_mps` | 最大速度 | 米/秒 |
| `total_elevation_gain_metres` | 总海拔升高 | 米 |
| `elev_high_metres` | 最高海拔 | 米 |
| `elev_low_metres` | 最低海拔 | 米 |
| `calories` | 燃烧的卡路里 | 千卡 |
| `start_latlng` | 起点坐标 | [纬度, 经度] |
| `end_latlng` | 终点坐标 | [纬度, 经度] |

## 认证

要使用此服务器，您需要与 Strava API 进行认证。请按照以下步骤操作：

1. 创建一个 Strava API 应用程序：
   - 前往 [Strava API 设置](https://www.strava.com/settings/api)
   - 创建一个应用程序以获取您的 Client ID 和 Client Secret
   - 将授权回调域设置为 `localhost`

2. 获取您的刷新令牌：
   - 使用随附的 `get_strava_token.py` 脚本：
```bash
   python get_strava_token.py
```
   - 按照提示授权您的应用程序
   - 脚本会将您的令牌保存到 `.env` 文件中

3. 设置环境变量：
   服务器需要以下环境变量：
   - `STRAVA_CLIENT_ID`: 您的 Strava API Client ID
   - `STRAVA_CLIENT_SECRET`: 您的 Strava API Client Secret
   - `STRAVA_REFRESH_TOKEN`: 您的 Strava API 刷新令牌

## 使用方法

### Claude for Desktop

更新您的 `claude_desktop_config.json`（在 macOS 上位于 `~/Library/Application\ Support/Claude/claude_desktop_config.json`，在 Windows 上位于 `%APPDATA%/Claude/claude_desktop_config.json`），以包含以下内容：

```json
{
    "mcpServers": {
        "strava": {
            "command": "uvx",
            "args": [
                "strava-mcp-server"
            ],
            "env": {
                "STRAVA_CLIENT_ID": "YOUR_CLIENT_ID",
                "STRAVA_CLIENT_SECRET": "YOUR_CLIENT_SECRET",
                "STRAVA_REFRESH_TOKEN": "YOUR_REFRESH_TOKEN"
            }
        }
    }
}
```

### Claude Web

对于 Claude Web，你可以本地运行服务器并通过 MCP 扩展连接它。

## 示例查询

连接后，你可以向 Claude 提问，例如：

- "我最近的活动有哪些？"
- "显示我上周的活动"
- "过去一个月里我最长的一次跑步是多久？"
- "获取关于我最新骑行活动的详细信息"

## 错误处理

服务器为常见的问题提供了易于理解的错误消息：

- 无效的日期格式
- API 认证错误
- 网络连接问题

## 许可证

本项目采用 MIT 许可证发布 - 详情请参阅 LICENSE 文件。

**官方网站：** [https://github.com/tomekkorbak/strava-mcp-server](https://github.com/tomekkorbak/strava-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`health and wellness`, `research and data`, `search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`strava-mcp-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/tomekkorbak-strava.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
