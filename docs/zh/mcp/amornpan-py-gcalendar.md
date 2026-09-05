---
title: "MCP Google日历服务"
description: "提供对Google日历API的无缝访问的模型上下文协议服务器，支持异步操作，通过标准化接口实现高效的日历管理。"
---

# MCP Google日历服务

提供对Google日历API的无缝访问的模型上下文协议服务器，支持异步操作，通过标准化接口实现高效的日历管理。

# Google Calendar MCP Server - 安装和使用指南

## 📘 概述
Model Context Protocol (MCP) 服务器提供对 Google Calendar API 的无缝访问，并支持异步操作，通过标准接口高效管理日历。

## 🚀 主要特性
- 无缝连接到 Google Calendar API
- 支持异步操作以实现最高效率
- 基于 OAuth 2.0 的认证系统，自动刷新令牌
- 全面的错误处理和日志记录
- 简洁的 MCP 接口，适用于 Claude 和其他 AI

## 🔑 API 工具
| 工具 | 描述 |
|------------|----------|
| **list** | 获取日历中的活动列表（过去两年至未来一年） |
| **create-event** | 在日历中创建新活动 |
| **delete-duplicates** | 删除重复的活动 |
| **delete-event** | 删除指定的活动 |

## 🛠️ 安装

### 先决条件
- Python 3.9 或更高版本
- 互联网连接
- 启用了 Google Calendar API 的 Google Cloud Console 项目

### 安装步骤

1. **克隆项目**
```bash
   git clone https://github.com/yourusername/GCalendar.git
   cd GCalendar
```

2. **创建虚拟环境（推荐方法）**
```bash
   python -m venv gcalendar_venv
   
   # 对于 Windows
   gcalendar_venv\Scripts\activate
   
   # 对于 macOS/Linux
   source gcalendar_venv/bin/activate
```

3. **安装必需的包**
```bash
   pip install -r requirements.txt
```

4. **准备必需的文件夹**
```bash
   mkdir -p credentials logs
```

### 认证设置

1. **创建 Google Cloud Console 项目**
   - 前往 [Google Cloud Console](https://console.cloud.google.com/)
   - 创建新项目
   - 启用 Google Calendar API
   - 创建 OAuth 2.0 客户端 ID
   - 将 credentials.json 下载到 credentials/ 文件夹中

2. **生成令牌**
```bash
   python src/create_token.py
```
   - 按照浏览器中的步骤授权访问
   - 令牌将保存在 credentials/ 文件夹中，命名为 token.json

## ⚙️ 技术配置

### 配置 MCP 服务器
在 `claude_desktop_config.json` 文件中添加：
```json
{
  "mcpServers": {
    "gcalendar": {
      "command": "YOUR_PYTHON_PATH",
      "args": [
        "YOUR_PATH/GCalendar/src/mcp_server.py"
      ]
    }
  }
}
```

替换占位符：
- `YOUR_PYTHON_PATH`: Python 解释器的路径（来自 venv 或 conda）
- `YOUR_PATH`: 克隆项目的完整路径

### 项目结构
```
GCalendar/
├── credentials/
│   ├── credentials.json   # จาก Google Cloud Console
│   └── token.json        # สร้างโดย create_token.py
├── logs/
│   └── calendar_service.log
├── src/
│   ├── calendar_service.py   # การดำเนินการปฏิทินหลัก
│   ├── create_token.py      # การสร้างโทเค็น
│   ├── list_past_events.py  # ยูทิลิตี้การแสดงรายการกิจกรรม
│   ├── mcp_client.py        # การใช้งาน MCP client
│   ├── mcp_server.py        # การใช้งานเซิร์ฟเวอร์หลัก
│   └── renew_token.py       # ยูทิลิตี้การต่ออายุโทเค็น
├── requirements.txt
└── README.md
```

## 📋 使用说明

### 启动服务器

1. **手动启动服务器**
```bash
   python src/mcp_server.py
```

2. **与 Claude Desktop 一起使用**
   - 按照上面技术配置部分中的说明进行配置
   - Claude 会在需要时自动启动服务器

### 示例命令

1. **查看日历中的活动列表**
```
   显示我的日历中的活动
```

2. **创建新活动**
```
   创建名为 "团队会议" 的会议，日期为 2025 年 3 月 25 日，时间为 14:00 至 15:00
```

3. **删除重复的活动**
```
   删除 2025 年 3 月 25 日重复的 "团队会议" 活动
```

## 🔍 故障排除

### 认证问题

1. 检查 credentials.json 和 token.json 文件是否位于 credentials/ 文件夹中。
2. 删除 token.json 并使用 create_token.py 重新创建它。

### 关于时区的问题
1. 确认 timezone 库已安装：
```bash
   pip install pytz tzdata
```

### 检查日志
1. 查看日志文件以获取有关错误的更多信息：
```bash
   cat logs/calendar_service.log
```

## 📚 依赖
- google-auth-oauthlib==1.0.0
- google-auth-httplib2==0.1.0
- google-api-python-client==2.108.0
- aiohttp==3.8.5
- asyncio==3.4.3
- pytz==2023.3
- tzdata==2023.3

## 📄 许可证
此项目根据 MIT License 发布。请参阅 LICENSE 文件以获取详细信息。
"# py-mcp-gcalendar"

**官方网站：** [https://github.com/amornpan/py-mcp-gcalendar](https://github.com/amornpan/py-mcp-gcalendar)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`productivity`
- 标签：`calendar management`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`YOUR_PYTHON_PATH`
- 参数：`YOUR_PATH/GCalendar/src/mcp_server.py`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/amornpan-py-gcalendar.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
