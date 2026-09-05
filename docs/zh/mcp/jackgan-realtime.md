---
title: "全球实时时间查询（MCP&Agent挑战赛）"
description: "全球时区时间查询器 项目介绍 全球时区时间查询器是一个基于Python和Gradio开发的Web应用工具，能够实时获取全球任意时区的详细时间信息。该工具具有以下特点： - 支持标准时区格式（如\"Asia/Shanghai\"、\"America/NewYork\"等）的时间查询 - 默认显示中国标准时间(UTC+8) - 提供详尽的时间信息，包括当前时间、日期、星期、年份、月份、小时、分钟、秒钟等 -…"
---

# 全球实时时间查询（MCP&Agent挑战赛）

全球时区时间查询器 项目介绍 全球时区时间查询器是一个基于Python和Gradio开发的Web应用工具，能够实时获取全球任意时区的详细时间信息。该工具具有以下特点： - 支持标准时区格式（如"Asia/Shanghai"、"America/NewYork"等）的时间查询 - 默认显示中国标准时间(UTC+8) - 提供详尽的时间信息，包括当前时间、日期、星期、年份、月份、小时、分钟、秒钟等 -…

# 全球时区时间查询器

## 项目介绍

全球时区时间查询器是一个基于Python和Gradio开发的Web应用工具，能够实时获取全球任意时区的详细时间信息。该工具具有以下特点：

- 支持标准时区格式（如"Asia/Shanghai"、"America/New_York"等）的时间查询
- 默认显示中国标准时间(UTC+8)
- 提供详尽的时间信息，包括当前时间、日期、星期、年份、月份、小时、分钟、秒钟等
- 计算并显示与UTC的偏移量，支持中文友好的时差描述
- 显示一年中的第几天和第几周
- 具备夏令时检测功能
- 提供直观的Web界面，支持示例查询

该工具不仅可以作为独立的时间查询应用使用，还可以在大模型遇到时间指令不明确（如"最近"、"近期"等）时，帮助大模型获取当前时间，提升时间相关问答的准确性。

## 部署指南

### 环境要求

- Python 3.9+（推荐Python 3.10或更高版本）
- pip包管理工具

### 安装依赖

项目依赖以下Python库：
- gradio：用于创建Web界面
- zoneinfo：用于时区处理（Python 3.9+内置）
- datetime：用于日期时间处理（Python标准库）

使用pip安装所需依赖：

```bash
pip install gradio
```

### 运行项目

1. 确保已安装所有依赖
2. 在项目目录下运行以下命令：

```bash
python time2.py
```

3. 应用启动后，会在控制台显示本地访问URL（通常为http://127.0.0.1:7863）和公共访问URL
4. 在浏览器中打开本地访问URL即可使用应用

## 使用案例

### 基础使用

1. 打开全球时区时间查询器Web界面
2. 默认显示中国标准时间(UTC+8)的详细信息
3. 在输入框中输入其他时区名称（如"America/New_York"），点击提交按钮获取对应时区的时间信息

### 示例查询

应用提供了几个常用时区的示例查询，点击示例按钮即可快速查看：

- UTC：协调世界时
- Asia/Shanghai：中国标准时间
- America/New_York：纽约时间
- Europe/London：伦敦时间
- Asia/Tokyo：东京时间

### 输出信息解读

查询结果包含以下信息：

- 时区名称
- 时区缩写
- 当前时间（年月日时分秒格式）
- 星期几（中文显示）
- 详细日期信息
- 详细时间信息
- 一年中的第几天
- 一年中的第几周
- 是否为夏令时
- 与UTC的偏移量（格式为±HH:MM）
- 中文友好的时差描述（如"比UTC时间快8.0小时"）

### mcp服务配置
studio
```
{
  "mcpServers": {
    "gradio": {
      "args": [
        "mcp-remote",
        "https://jackgan-realtime.ms.show/gradio_api/mcp/sse",
        "--transport",
        "sse-only"
      ],
      "command": "npx"
    }
  }
}
```

**官方网站：** [https://modelscope.cn/studios/JackGan/realtime/summary](https://modelscope.cn/studios/JackGan/realtime/summary)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`productivity`
- 标签：`search`, `developer tools`, `calendar management`, `时间,地区`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`mcp-remote https://jackgan-realtime.ms.show/gradio_api/mcp/sse --transport sse-only`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/jackgan-realtime.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
