---
title: "MCP日期时间"
description: "一个作为 Claude 桌面应用程序的 MCP 服务器实现的日期时间格式化服务。支持生成各种格式的日期时间字符串。"
---

# MCP日期时间

一个作为 Claude 桌面应用程序的 MCP 服务器实现的日期时间格式化服务。支持生成各种格式的日期时间字符串。

# mcp-datetime

[![Python Version](/mcp-assets/e1a2b83f0b6cdff8bd20352d9134afb6.svg)](https://www.python.org/downloads/)
[![MCP Version](/mcp-assets/c055b41030c021cf170741a558fb4dc8.svg)](https://github.com/anaisbetts/mcp)
[![License](/mcp-assets/d177f30277cff66d9af1e3c6409e24dc.svg)](https://github.com/ZeparHyfar/mcp-datetime/blob/HEAD/LICENSE)

English | [日本語](https://github.com/ZeparHyfar/mcp-datetime/blob/HEAD/README_ja.md)

这是一个为 Claude 桌面应用程序实现的 MCP 服务器格式化日期时间的服务。支持生成多种格式的日期时间字符串。

> **注意**：此包仅在 macOS 上进行了测试。尚未验证 Windows 兼容性。

## 前提条件

在使用 mcp-datetime 之前，请确保已安装以下工具：

- Python 3.12 或更高版本
- uv（Python 包安装器）
- uvx（Python 包运行器）

## 功能

- ✨ 支持多种日期时间格式
- 🇯🇵 日语支持
- 📁 优化的文件名生成格式
- 🌏 准确的时区处理
- 🔧 与 Claude 桌面应用程序无缝集成

## MCP 服务器组件

### 工具

该服务器实现了一个工具：

- `get_datetime`：以各种格式获取当前日期和时间
  - 需要一个必需的字符串参数 "format"
  - 根据指定的格式返回格式化的日期时间字符串
  - 支持多种格式类型，包括标准格式、日文格式和 ISO 格式

## 与 Claude 桌面应用程序配合使用

将以下内容添加到您的配置文件中：

配置文件位置 (macOS)：
`~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "mcp-datetime": {
      "command": "uvx",
      "args": ["mcp-datetime"]
    }
  }
}
```

## 关于安装

如果您需要直接安装该包（例如，用于开发或源代码检查），可以使用以下方法之一：

- 从 PyPI 安装

```bash
  pip install mcp-datetime
```

- 从 GitHub 源码安装

```bash
  git clone https://github.com/ZeparHyfar/mcp-datetime.git
  cd mcp-datetime
  pip install -e .
```

- 手动安装示例 `claude_desktop_config.json`

```json
  {
    "mcpServers": {
      "mcp-datetime": {
        "command": "python",
        "args": ["-m", "mcp_datetime"],
        "env": {
          "PYTHON": "/path/to/your/python"
        }
      }
    }
  }
```

  将 "/path/to/your/python" 替换为您实际的 Python 解释器路径
  > 例如，"/usr/local/bin/python3" 或 "/Users/username/.pyenv/versions/3.12.0/bin/python3"

## 基本示例

- 命令格式

```
  # 标准日期时间格式
  call datetime-service.get_datetime {"format": "datetime"}
  # 结果: 2024-12-10 00:54:01

  # 日文格式
  call datetime-service.get_datetime {"format": "datetime_jp"}
  # 结果: 2024年12月10日 00時54分01秒

  # 文件名格式
  call datetime-service.get_datetime {"format": "filename_md"}
  # 结果: 20241210005401.md
```

- Claude 桌面应用程序提示示例

  - 用户

```
    请告诉我当前时间的 date_slash 格式
```

  - Claude

```
    我会获取当前日期的 date_slash 格式。

    当前日期是 2024/12/12
```

## 支持的格式

| 格式名称       | 示例                         | 描述                       |
| ------------ | --------------------------- | -------------------------- |
| date         | 2024-12-10                  | 标准日期格式               |
| date_slash   | 2024/12/10                  | 使用斜杠的日期             |
| date_jp      | 2024年12月10日              | 日语日期格式               |
| datetime     | 2024-12-10 00:54:01         | 标准日期时间               |
| datetime_jp  | 2024年12月10日 00時54分01秒 | 日语日期时间               |
| datetime_t   | 2024-12-10T00:54:01         | 使用 T 分隔符的日期时间    |
| compact      | 20241210005401              | 用于 ID 的紧凑格式         |
| compact_date | 20241210                    | 仅紧凑日期                 |
| compact_time | 005401                      | 仅紧凑时间                 |
| filename_md  | 20241210005401.md           | Markdown 文件名            |
| filename_txt | 20241210005401.txt          | 文本文件名                 |
| filename_log | 20241210005401.log          | 日志文件名                 |
| iso          | 2024-12-10T00:54:01+0900    | ISO 8601 格式              |
| iso_basic    | 20241210T005401+0900        | 基础 ISO 格式              |
| log          | 2024-12-10 00:54:01.123456  | 包含微秒的日志格式         |
| log_compact  | 20241210_005401             | 紧凑的日志格式             |
| time         | 00:54:01                    | 仅时间                     |
| time_jp      | 00時54分01秒                | 日语时间格式               |

## 调试

由于 MCP 服务器运行在 stdio 上，调试可能会比较困难。我们建议使用 [MCP Inspector](https://github.com/modelcontextprotocol/inspector)：

- 使用 PyPI 包

```
  npx @modelcontextprotocol/inspector uvx mcp-datetime
```

- 使用从 GitHub 下载的源代码

```
  git clone https://github.com/ZeparHyfar/mcp-datetime.git
  npx @modelcontextprotocol/inspector uvx --directory ./mcp-datetime run mcp-datetime
```

## 许可证

本项目根据 MIT 许可证发布 - 详情请参阅 [LICENSE](https://github.com/ZeparHyfar/mcp-datetime/blob/HEAD/LICENSE) 文件。

**官方网站：** [https://github.com/ZeparHyfar/mcp-datetime](https://github.com/ZeparHyfar/mcp-datetime)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`productivity`
- 标签：`other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`mcp-datetime`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/zeparhyfar-datetime.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
