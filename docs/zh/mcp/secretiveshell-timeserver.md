---
title: "MCP时区时间服务器"
description: "访问任何时区的时间并获取当前本地时间"
---

# MCP时区时间服务器

访问任何时区的时间并获取当前本地时间

# MCP-timeserver

一个简单的MCP服务器，向代理系统和聊天REPL提供日期时间信息。

## 组件

### 资源

该服务器实现了一个简单的datetime:// URI方案，用于访问给定时区的当前日期/时间，例如：
```
datetime://Africa/Freetown/now
datetime://Europe/London/now
datetime://America/New_York/now
```

### 工具

该服务器公开了一个工具，用于获取系统时区中的当前本地时间：
```python
>>> get_current_time()
"The current time is 2024-12-18 19:59:36"
```

## 快速开始

### 安装

使用以下json

```json
{
  "mcpServers": {
    "MCP-timeserver": {
      "command": "uvx",
      "args": ["MCP-timeserver"]
    }
  }
}
```

**官方网站：** [https://github.com/SecretiveShell/MCP-timeserver](https://github.com/SecretiveShell/MCP-timeserver)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`productivity`
- 标签：`other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`MCP-timeserver`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/secretiveshell-timeserver.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
