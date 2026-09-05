---
title: "MCP-PA 智能助手"
description: "一种多功能的模型上下文协议服务器，使人工智能助手能够管理日历、跟踪任务、处理电子邮件、搜索网络以及控制智能家居设备。"
---

# MCP-PA 智能助手

一种多功能的模型上下文协议服务器，使人工智能助手能够管理日历、跟踪任务、处理电子邮件、搜索网络以及控制智能家居设备。

# MCP 个人助理代理

这是一个使用模型上下文协议（MCP）构建的多功能个人助理AI代理，可帮助管理日历、任务、电子邮件等。

## 概述

该项目是一个基于模型上下文协议（MCP）的服务端，为个人助理代理提供了一套工具。它可以与像Claude for Desktop这样的MCP客户端集成，赋予AI助手以下能力：

- 管理日历事件
- 跟踪任务和待办事项
- 阅读和发送电子邮件
- 在网上搜索并检索信息
- 控制智能家居设备

## 要求

⚠️ **重要提示：** MCP SDK需要Python 3.10或更高版本。服务器将不兼容早期版本的Python。
- Python 3.10+
- MCP SDK 1.2.0+
- 必需的Python包（参见requirements.txt）

## 安装

1. 克隆仓库：
```bash
git clone https://github.com/yourusername/mcp-pa-ai-agent.git
cd mcp-pa-ai-agent
```

2. 确保您安装了Python 3.10+：
```bash
python --version
```

3. 如果您的系统Python版本低于3.10，请设置一个兼容环境：
```bash
# Using conda
conda create -n mcp-env python=3.10
conda activate mcp-env

# OR using venv (if Python 3.10+ is installed elsewhere)
python3.10 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

4. 安装依赖项：
```bash
pip install -r requirements.txt
```

5. 通过复制示例文件来配置环境变量：
```bash
cp .env.example .env
```

6. 使用您的API凭证和设置编辑`.env`文件。

## 运行服务器

启动MCP服务器：
```bash
python mcp_server.py
```

服务器将启动并监听来自MCP客户端的连接。

## 连接到Claude for Desktop

1. 安装[Claude for Desktop](https://claude.ai/desktop)

2. 通过编辑配置文件来配置Claude for Desktop以使用此MCP服务器：
   - MacOS/Linux: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`

3. 添加如下配置：
```json
{
  "mcpServers": {
    "personal-assistant": {
      "command": "/path/to/python",
      "args": [
        "/absolute/path/to/mcp-pa-ai-agent/mcp_server.py"
      ]
    }
  }
}
```

如果您正在使用虚拟环境，请确保指向该环境中的Python可执行文件。

4. 重启Claude for Desktop

## 可用工具

### 日历
- `get_events`: 获取即将到来的日历事件
- `create_event`: 创建一个新的日历事件

### 任务
- `list_tasks`: 查看所有任务或按状态筛选
- `add_task`: 创建新任务
- `update_task_status`: 标记任务为待处理、进行中或已完成

### 电子邮件
- `get_emails`: 列出收件箱中的最近邮件
- `read_email`: 查看特定邮件的完整内容
- `send_email`: 编写并发送新邮件

### 知识
- `web_search`: 在网上搜索信息
- `get_weather`: 获取当前天气信息
- `get_news`: 检索最新新闻文章

### 智能家居
- `list_devices`: 查看所有智能家居设备
- `control_device`: 控制智能家居设备（如灯光、恒温器等）
- `get_device_state`: 获取设备当前状态的详细信息

## 配置

服务器需要各种API密钥和服务访问凭据：

- **Google API**: 用于日历和电子邮件功能（OAuth2凭证）
- **Weather API**: 用于获取天气信息
- **News API**: 用于检索新闻
- **Home Assistant**: 用于智能家居控制

请参考`.env.example`文件了解所有可配置选项。

## 故障排除

### Python 版本问题

如果你看到类似以下错误：
```
Error: Python 3.10 or higher is required for the MCP server.
```

你需要升级你的 Python 版本或使用带有 Python 3.10+ 的虚拟环境。

### MCP SDK 安装问题

如果你在安装 MCP SDK 时遇到问题：
```
ERROR: Could not find a version that satisfies the requirement mcp>=1.2.0
```

请确保你使用的是 Python 3.10+ 并且 pip 是最新的：
```bash
pip install --upgrade pip
```

## 开发

要为服务器添加新功能，你可以：

1. 在 `modules/` 目录下创建一个新的模块
2. 使用 `@mcp.tool()` 装饰器实现函数
3. 在 `mcp_server.py` 中导入你的模块

## 许可证

MIT

## 贡献

欢迎贡献！请随时提交 Pull Request。

**官方网站：** [https://github.com/zhangzhongnan928/mcp-pa-ai-agent](https://github.com/zhangzhongnan928/mcp-pa-ai-agent)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`productivity`
- 标签：`calendar management`, `home automation and iot`, `communication`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`/path/to/python`
- 参数：`/absolute/path/to/mcp-pa-ai-agent/mcp_server.py`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/zhangzhongnan928-pa-ai-agent.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
