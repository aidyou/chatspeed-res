---
title: "MCP时钟"
description: "一个轻量级的MCP服务器，可以根据你的IP地址告诉你确切的时间。"
---

# MCP时钟

一个轻量级的MCP服务器，可以根据你的IP地址告诉你确切的时间。

# WhatTimeIsIt MCP 服务器

一个轻量级的MCP服务器，能够准确告诉你当前时间，由[World Time](http://worldtimeapi.org/)提供支持。

![GitHub](/mcp-assets/5816f652aa1f0cc4eedb21a2f733e09e.svg) 
![GitHub 最后一次提交](/mcp-assets/fbff8007b8fe8bc1f07f654c3f3c57ca.svg)

## 安装

1. **克隆仓库**
```bash
   git clone https://github.com/kukapay/whattimeisit-mcp.git
```

2. **客户端配置**
```json
    {
      "mcpServers": {
        "whattimeisit": {
          "command": "uv",
          "args": ["--directory", "path/to/whattimeisit-mcp", "run", "main.py"]
        }
      }
    }
```

## 使用方法

### MCP 工具
该服务器提供了一个工具：
- **工具名称**: `what_time_is_it`
- **描述**: 根据您的当前IP返回当前时间字符串。
- **输出**: 以ISO 8601格式的字符串（例如，`"2025-03-17T03:17:00+11:00"`）。

## 许可证
本项目采用MIT许可证。详情请参阅[LICENSE](https://github.com/kukapay/whattimeisit-mcp/blob/HEAD/LICENSE)文件。

**官方网站：** [https://github.com/kukapay/whattimeisit-mcp](https://github.com/kukapay/whattimeisit-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`location services`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`--directory path/to/whattimeisit-mcp run main.py`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/kukapay-whattimeisit.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
