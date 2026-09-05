---
title: "Unsplash图片搜索服务端"
description: "一个轻量级服务器，可实现与Unsplash图像库的无缝集成，使开发人员能够直接从Cursor编辑器中使用各种过滤器搜索高质量照片。"
---

# Unsplash图片搜索服务端

一个轻量级服务器，可实现与Unsplash图像库的无缝集成，使开发人员能够直接从Cursor编辑器中使用各种过滤器搜索高质量照片。

# Unsplash MCP Server

English | [简体中文](https://github.com/hellokaton/unsplash-mcp-server/blob/HEAD/README_zh.md)

> 一个简单的MCP服务器，用于无缝集成Unsplash图片和搜索功能。

[![Python 3.9+](/mcp-assets/fc6c1779d629c51ff66ed00bf03ad061.svg)](https://www.python.org/downloads/)
[![License: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://opensource.org/licenses/MIT)
[Smithery](https://smithery.ai/server/@hellokaton/unsplash-mcp-server)

## 📋 概述

Unsplash MCP Server 用于搜索丰富且高质量的图片。非常适合希望将Unsplash功能集成到自己应用程序中的开发者使用。

## ✨ 特性

- **高级图片搜索**：通过以下过滤条件搜索Unsplash庞大的照片库：
  - 关键词相关性
  - 色彩方案
  - 方向选项
  - 自定义排序和分页

## 🔑 获取Unsplash访问密钥

在安装此服务器之前，您需要获取Unsplash API访问密钥：

1. 在[Unsplash](https://unsplash.com/developers)创建一个开发者账户
2. 注册一个新的应用
3. 从应用详情页面获取您的访问密钥
4. 在下面的配置步骤中使用此密钥

更多细节，请参考[官方Unsplash API文档](https://unsplash.com/documentation)。

## 🚀 安装

要通过[Smithery](https://smithery.ai/server/@hellokaton/unsplash-mcp-server)自动为Claude Desktop安装Unsplash图像集成服务器：

### IDE 设置

**Cursor IDE**

```bash
npx -y @smithery/cli@latest install @hellokaton/unsplash-mcp-server --client cursor --key 7558c683-****-****
```

**Windsurf**

```bash
npx -y @smithery/cli@latest install @hellokaton/unsplash-mcp-server --client windsurf --key 7558c683-****-****
```

**Cline**

```bash
npx -y @smithery/cli@latest install @hellokaton/unsplash-mcp-server --client cline --key 7558c683-****-****
```

### 手动安装

```bash
# Clone the repository
git clone https://github.com/hellokaton/unsplash-mcp-server.git

# Navigate to project directory
cd unsplash-mcp-server

# Create virtual environment
uv venv

# Install dependencies
uv pip install .
```

**Cursor 编辑器集成**

将以下配置添加到您的Cursor编辑器的`settings.json`中：

⚠️ **注意：** 请根据您的实际安装情况调整以下配置：

- 如果`uv`不在您的系统PATH中，请使用绝对路径（例如`/path/to/uv`）
- `./server.py`应修改为您服务器脚本的实际位置（可以使用绝对路径或相对于工作区的路径）

 alt="Cursor 配置截图" />

```json
{
  "mcpServers": {
    "unsplash": {
      "command": "uv",
      "args": ["run", "--with", "fastmcp", "fastmcp", "run", "./server.py"],
      "env": {
        "UNSPLASH_ACCESS_KEY": "${YOUR_ACCESS_KEY}"
      }
    }
  }
}
```

### 在Cursor中使用

 alt="Cursor 中的Unsplash MCP" />

## 🛠️ 可用工具

### 搜索图片

```json
{
  "tool": "search_photos",
  "query": "mountain",
  "per_page": 5,
  "orientation": "landscape"
}
```

## 🔄 其他实现

- Golang: [unsplash-mcp-server](https://github.com/douglarek/unsplash-mcp-server)
- Java: [unsplash-mcp-server](https://github.com/JavaProgrammerLB/unsplash-mcp-server)

## 📄 许可证

[MIT许可证](https://github.com/hellokaton/unsplash-mcp-server/blob/HEAD/LICENSE)

## 📬 联系方式

- [Twitter/X](https://x.com/hellokaton)
- [GitHub Issues](https://github.com/hellokaton/unsplash-mcp-server/issues)

**官方网站：** [https://github.com/hellokaton/unsplash-mcp-server](https://github.com/hellokaton/unsplash-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`art and culture`, `search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`run --with fastmcp fastmcp run ./server.py`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/hellokaton-unsplash.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
