---
title: "BeautifulSoup4 网页浏览器"
description: "使用BeautifulSoup4启用网页浏览功能"
---

# BeautifulSoup4 网页浏览器

使用BeautifulSoup4启用网页浏览功能

[![Twitter Follow](/mcp-assets/3e82fabdd3d7f3c8bffecf68b940346e.svg)](https://twitter.com/JoeBlazick)
[Smithery](https://smithery.ai/server/web-browser-mcp-server)
[![Python Version](/mcp-assets/4f6146f128339189f0d4b97607879041.svg)](https://www.python.org/downloads/)
[![License: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://opensource.org/licenses/MIT)
[![PyPI Downloads](/mcp-assets/f8c1de5b3c366a7630260f8a746beba5.svg)](https://pypi.org/project/web-browser-mcp-server/)
[![PyPI Version](/mcp-assets/0002d1bc4f92679c760e34714252a2a1.svg)](https://pypi.org/project/web-browser-mcp-server/)

## ✨ 特性

> 🌐 通过简单的MCP接口，使AI助手能够浏览和从网页中提取内容。

Web Browser MCP Server通过消息控制协议（MCP）为AI模型提供了浏览网站、提取内容以及理解网页的能力。它支持使用CSS选择器进行智能内容提取，并具备强大的错误处理功能。

  
🤝 **[贡献](https://github.com/blazickjp/web-browser-mcp-server/blob/main/CONTRIBUTING.md)** • 
📝 **[报告Bug](https://github.com/blazickjp/web-browser-mcp-server/issues)**

## ✨ 核心特性

- 🎯 **智能内容提取**：使用CSS选择器精确获取所需内容
- ⚡ **闪电般快速**：采用异步处理以实现最佳性能
- 📊 **丰富的元数据**：捕获标题、链接和结构化内容
- 🛡️ **稳健且可靠**：内置错误处理和超时管理
- 🌍 **跨平台**：在任何运行Python的地方都可工作

## 🚀 快速开始

### 通过Smithery安装

要通过[Smithery](https://smithery.ai/server/web-browser-mcp-server)自动为Claude Desktop安装Web Browser Server：

```bash
npx -y @smithery/cli install web-browser-mcp-server --client claude
```

### 手动安装
使用uv安装：

```bash
uv tool install web-browser-mcp-server
```

开发环境：

```bash
# Clone and set up development environment
git clone https://github.com/blazickjp/web-browser-mcp-server.git
cd web-browser-mcp-server

# Create and activate virtual environment
uv venv
source .venv/bin/activate

# Install with test dependencies
uv pip install -e ".[test]"
```

### 🔌 MCP集成

将此配置添加到您的MCP客户端配置文件中：

```json
{
    "mcpServers": {
        "web-browser-mcp-server": {
            "command": "uv",
            "args": [
                "tool",
                "run",
                "web-browser-mcp-server"
            ],
            "env": {
                "REQUEST_TIMEOUT": "30"
            }
        }
    }
}
```

开发环境：

```json
{
    "mcpServers": {
        "web-browser-mcp-server": {
            "command": "uv",
            "args": [
                "--directory",
                "path/to/cloned/web-browser-mcp-server",
                "run",
                "web-browser-mcp-server"
            ],
            "env": {
                "REQUEST_TIMEOUT": "30"
            }
        }
    }
}
```

## 💡 可用工具

服务器提供了一个强大的网页浏览工具：

### browse_webpage
使用可选的CSS选择器浏览并从网页中提取内容：

```python
# Basic webpage fetch
result = await call_tool("browse_webpage", {
    "url": "https://example.com"
})

# Target specific content with CSS selectors
result = await call_tool("browse_webpage", {
    "url": "https://example.com",
    "selectors": {
        "headlines": "h1, h2",
        "main_content": "article.content",
        "navigation": "nav a"
    }
})
```

## ⚙️ 配置

通过环境变量进行配置：

| 变量 | 目的 | 默认值 |
|----------|---------|---------|
| `REQUEST_TIMEOUT` | 网页请求超时时间（秒） | 30 |

## 🧪 测试

运行测试套件：

```bash
python -m pytest
```

## 📄 许可证

本项目依据MIT许可证发布。详情请参见LICENSE文件。

---

由Pear Labs团队用心制作

**官方网站：** [https://github.com/blazickjp/web-browser-mcp-server](https://github.com/blazickjp/web-browser-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`browser`
- 标签：`browser automation`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`tool run web-browser-mcp-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/blazickjp-web-browser.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
