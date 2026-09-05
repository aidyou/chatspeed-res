---
title: "veimagex-mcp"
description: "Volcengine ImageX MCP Volcengine ImageX 的 Model Context Protocol (MCP) Server 实现 项目简介 Volcengine ImageX MCP是一个基于Model Context Protocol的 MCP-server， 它将 Volcengine 服务集成到LLM模型上下文中，使大模型能够直接上传和处理图片资源。 功能特点…"
---

# veimagex-mcp

Volcengine ImageX MCP Volcengine ImageX 的 Model Context Protocol (MCP) Server 实现 项目简介 Volcengine ImageX MCP是一个基于Model Context Protocol的 MCP-server， 它将 Volcengine 服务集成到LLM模型上下文中，使大模型能够直接上传和处理图片资源。 功能特点…

# Volcengine ImageX MCP

[Volcengine ImageX](https://t.zijieimg.com/MIURnXrQfvU/) 的 Model Context Protocol (MCP) Server 实现

## 项目简介

Volcengine ImageX MCP是一个基于[Model Context Protocol](https://github.com/modelcontextprotocol/python-sdk)的 MCP-server，
它将 Volcengine 服务集成到LLM模型上下文中，使大模型能够直接上传和处理图片资源。

## 功能特点

- 提供多种资源访问接口，便于LLM获取veImageX服务信息、图片资源等
- 实现了多个veImageX功能的工具封装，包括图片资源的管理、文生图、AIGC画质修复、画质评估以及常用的用量、质量查询能力
- 提供多种预定义提示模板，帮助LLM更好地理解和使用veImageX功能

## 安装

### 环境要求

- Python 3.11+
- [火山引擎账号及AccessKey/SecretKey](https://console.volcengine.cn/imagex)

## 使用方法

在 mcp client 中配置 mcp 服务， 配置的 MCP JSON：

```json
{
  "mcpServers": {
    "volcengine": {
      "disabled": false,
      "command": "uvx",
      "args": ["veimagex-mcp"],
      "env": {
        "VOLCENGINE_ACCESS_KEY": "Your Volcengine AK",
        "VOLCENGINE_SECRET_KEY": "Your Volcengine SK",
        "SERVICE_ID": "Your Service ID",
        "DOMAIN": "Your Domain"
      },
      "transportType": "stdio"
    }
  }
}
```

**官方网站：** [https://github.com/volcengine/mcp-imagex](https://github.com/volcengine/mcp-imagex)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`art and culture`, `aigc`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`veimagex-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/volcengine-imagex.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
