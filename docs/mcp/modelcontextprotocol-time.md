---
title: "时间服务"
description: "一个提供时间和时区转换功能的模型上下文协议服务器。该服务器使大型语言模型能够获取当前时间信息，并使用IANA时区名称进行时区转换，同时具备自动检测系统时区的功能。"
---

# 时间服务

一个提供时间和时区转换功能的模型上下文协议服务器。该服务器使大型语言模型能够获取当前时间信息，并使用IANA时区名称进行时区转换，同时具备自动检测系统时区的功能。

# 时间 MCP 服务器

一个提供时间和时区转换功能的模型上下文协议服务器。该服务器使 LLM 能够获取当前时间信息，并使用 IANA 时区名称进行时区转换，同时支持自动检测系统时区。

### 可用工具

- `get_current_time` - 获取特定时区或系统时区的当前时间。
  - 必需参数：
    - `timezone` (字符串): IANA 时区名称（例如 'America/New_York', 'Europe/London'）

- `convert_time` - 在不同时区之间转换时间。
  - 必需参数：
    - `source_timezone` (字符串): 源 IANA 时区名称
    - `time` (字符串): 24小时制的时间格式 (HH:MM)
    - `target_timezone` (字符串): 目标 IANA 时区名称

## 安装

### 使用 uv（推荐）

当使用 [`uv`](https://docs.astral.sh/uv/) 时不需要特别安装。我们将使用 [`uvx`](https://docs.astral.sh/uv/guides/tools/) 直接运行 *mcp-server-time*。

### 使用 PIP

或者，您可以通过 pip 安装 `mcp-server-time`：

```bash

pip install mcp-server-time

```
安装后，您可以使用以下命令作为脚本运行：

```bash

python -m mcp_server_time

```
## 配置

### 为 Claude.app 配置

在您的 Claude 设置中添加：

使用 uvx

```json

{

  "mcpServers": {

    "time": {

      "command": "uvx",

      "args": ["mcp-server-time"]

    }

  }

}

```

使用 Docker

```json

{

  "mcpServers": {

    "time": {

      "command": "docker",

      "args": ["run", "-i", "--rm", "-e", "LOCAL_TIMEZONE", "mcp/time"]

    }

  }

}

```

使用 pip 安装

```json

{

  "mcpServers": {

    "time": {

      "command": "python",

      "args": ["-m", "mcp_server_time"]

    }

  }

}

```

### 为 Zed 配置

在您的 Zed settings.json 中添加：

使用 uvx

```json

"context_servers": [

  "mcp-server-time": {

    "command": "uvx",

    "args": ["mcp-server-time"]

  }

],

```

使用 pip 安装

```json

"context_servers": {

  "mcp-server-time": {

    "command": "python",

    "args": ["-m", "mcp_server_time"]

  }

},

```

### 为 VS Code 配置

为了快速安装，请使用下面的一键安装按钮之一...

[![使用 UV 在 VS Code 中安装](/mcp-assets/ff0c64ea4d3a42e6aeccd71c5a5b6a57.svg)](https://insiders.vscode.dev/redirect/mcp/install?name=time&config=%7B%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22mcp-server-time%22%5D%7D) [![使用 UV 在 VS Code Insiders 中安装](/mcp-assets/805d41193c5fff3f82290b52ad64e24d.svg)](https://insiders.vscode.dev/redirect/mcp/install?name=time&config=%7B%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22mcp-server-time%22%5D%7D&quality=insiders)

[![使用 Docker 在 VS Code 中安装](/mcp-assets/615447f368859665ebd2f40a2de6e777.svg)](https://insiders.vscode.dev/redirect/mcp/install?name=time&config=%7B%22command%22%3A%22docker%22%2C%22args%22%3A%5B%22run%22%2C%22-i%22%2C%22--rm%22%2C%22mcp%2Ftime%22%5D%7D) [![使用 Docker 在 VS Code Insiders 中安装](/mcp-assets/49320713ff1e41ecebdc5836428df687.svg)](https://insiders.vscode.dev/redirect/mcp/install?name=time&config=%7B%22command%22%3A%22docker%22%2C%22args%22%3A%5B%22run%22%2C%22-i%22%2C%22--rm%22%2C%22mcp%2Ftime%22%5D%7D&quality=insiders)

对于手动安装，请将以下 JSON 块添加到 VS Code 的用户设置（JSON）文件中。您可以通过按 `Ctrl + Shift + P` 并输入 `Preferences: Open User Settings (JSON)` 来完成此操作。

可选地，您可以将其添加到工作区中的 `.vscode/mcp.json` 文件中。这将允许您与他人共享配置。

> 注意：当使用 `mcp.json` 文件时，需要 `mcp` 键。

使用 uvx

```json

{

  "mcp": {

    "servers": {

      "time": {

        "command": "uvx",

        "args": ["mcp-server-time"]

      }

    }

  }

}

```

使用 Docker

```json

{

  "mcp": {

    "servers": {

      "time": {

        "command": "docker",

        "args": ["run", "-i", "--rm", "mcp/time"]

      }

    }

  }

}

```

### 为 Zencoder 配置

1. 转到 Zencoder 菜单 (...)
2. 从下拉菜单中选择 `Agent Tools`
3. 点击 `Add Custom MCP`
4. 添加下方的名称和服务器配置，并确保点击 `Install` 按钮

使用 uvx

```json

{

    "command": "uvx",

    "args": ["mcp-server-time"]

  }

```

### 自定义 - 系统时区

默认情况下，服务器会自动检测您的系统时区。您可以通过在配置的 `args` 列表中添加 `--local-timezone` 参数来覆盖这一点。

示例：
```json
{
  "command": "python",
  "args": ["-m", "mcp_server_time", "--local-timezone=America/New_York"]
}
```
## 示例交互

1. 获取当前时间：
```json
{
  "name": "get_current_time",
  "arguments": {
    "timezone": "Europe/Warsaw"
  }
}
```
响应：
```json
{
  "timezone": "Europe/Warsaw",
  "datetime": "2024-01-01T13:00:00+01:00",
  "is_dst": false
}
```
2. 在不同时区之间转换时间：
```json
{
  "name": "convert_time",
  "arguments": {
    "source_timezone": "America/New_York",
    "time": "16:30",
    "target_timezone": "Asia/Tokyo"
  }
}
```
响应：
```json
{
  "source": {
    "timezone": "America/New_York",
    "datetime": "2024-01-01T12:30:00-05:00",
    "is_dst": false
  },
  "target": {
    "timezone": "Asia/Tokyo",
    "datetime": "2024-01-01T12:30:00+09:00",
    "is_dst": false
  },
  "time_difference": "+13.0h",
}
```
## 调试您可以使用MCP检查器来调试服务器。对于uvx安装：

```bash

npx @modelcontextprotocol/inspector uvx mcp-server-time

```
或者，如果您在特定目录中安装了该包或正在对其进行开发：

```bash

cd path/to/servers/src/time

npx @modelcontextprotocol/inspector uv run mcp-server-time

```
## 问题示例（针对Claude）

1. "现在几点了？"（将使用系统时区）
2. "东京现在几点了？"
3. "当纽约时间下午4点时，伦敦是几点？"
4. "将东京时间上午9:30转换为纽约时间"

## 构建

Docker构建：

```bash

cd src/time

docker build -t mcp/time .

```
## 贡献

我们鼓励贡献以帮助扩展和改进mcp-server-time。无论您想添加新的时间相关工具、增强现有功能还是改进文档，您的输入都是宝贵的。

有关其他MCP服务器和其他实现模式的示例，请参阅：
https://github.com/modelcontextprotocol/servers

欢迎提交拉取请求！请随时贡献新想法、错误修复或增强功能，使mcp-server-time更加强大和有用。

## 许可证

mcp-server-time根据MIT许可证授权。这意味着您可以自由使用、修改和分发软件，但需遵守MIT许可证的条款和条件。更多详细信息，请参见项目存储库中的LICENSE文件。

**官方网站：** [https://github.com/modelcontextprotocol/servers/tree/main/src/time](https://github.com/modelcontextprotocol/servers/tree/main/src/time)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`productivity`
- 标签：`calendar management`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`mcp-server-time`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/modelcontextprotocol-time.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
