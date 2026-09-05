---
title: "MCP-Oracle 数据库交互器"
description: "一种模型上下文协议服务器，使克劳德能够通过自然语言查询访问和交互Oracle数据库。"
---

# MCP-Oracle 数据库交互器

一种模型上下文协议服务器，使克劳德能够通过自然语言查询访问和交互Oracle数据库。

# mcp-server-oracle
Model Context Protocol 服务器，用于访问 Oracle

[![Python 3.12](/mcp-assets/e1a2b83f0b6cdff8bd20352d9134afb6.svg)](https://www.python.org/downloads/release/python-3120/)
[![License: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://opensource.org/licenses/MIT)

## 演示

https://github.com/user-attachments/assets/dc4e377b-4efb-43e6-85fa-93ed852fe21f

## 快速开始

要在 Claude Desktop 应用程序中尝试此功能，请将以下内容添加到您的 claude 配置文件中：

json
{
  "mcpServers": {
    "mcp-server-oracle": {
      "command": "uvx",
      "args": [
        "mcp-server-oracle"
      ],
      "env": {
        "ORACLE_CONNECTION_STRING": "username/password@hostname:password/service_name"
      }
    }
  }
}

### 前提条件

- UV（包管理器）
- Python 3.12+
- Claude Desktop

### 安装

#### Claude Desktop 配置

将服务器配置添加到您的 Claude Desktop 配置文件中：

**MacOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`  
**Windows**: `%APPDATA%/Claude/claude_desktop_config.json`

## 贡献

1. 从 [mcp-server-oracle](https://github.com/hdcola/mcp-server-oracle) 仓库进行 fork
2. 创建你的特性分支
3. 提交你的更改
4. 推送到该分支
5. 打开一个 Pull Request

## 许可证

本项目采用 MIT 许可证 - 详情请参阅 [LICENSE](https://github.com/anpy-j/mcp-oracle/blob/HEAD/LICENSE) 文件。

**官方网站：** [https://github.com/anpy-j/mcp-oracle](https://github.com/anpy-j/mcp-oracle)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`
- 标签：`databases`, `search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`mcp-server-oracle`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/anpy-j-oracle.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
