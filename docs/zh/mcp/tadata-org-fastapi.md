---
title: "FastAPI MCP工具"
description: "一个零配置的工具，可以自动将FastAPI端点暴露为模型上下文协议（MCP）工具，使像Claude这样的大型语言模型系统能够与您的API交互，而无需额外编码。"
---

# FastAPI MCP工具

一个零配置的工具，可以自动将FastAPI端点暴露为模型上下文协议（MCP）工具，使像Claude这样的大型语言模型系统能够与您的API交互，而无需额外编码。

alt="fastapi-to-mcp" height="100"/>

FastAPI-MCP

一个零配置工具，用于自动将 FastAPI 端点作为 Model Context Protocol (MCP) 工具暴露出来。

[![PyPI version](/mcp-assets/3eb159d4ab449e5582c03af5bccbf46e.svg)](https://pypi.org/project/fastapi-mcp/)
[![Python Versions](/mcp-assets/1828c31a371deac816fc5f6b8a6e3bbb.svg)](https://pypi.org/project/fastapi-mcp/)
[![FastAPI](/mcp-assets/d8d3fe385930007a18cb14a71733aa21.svg)](#)
![](/mcp-assets/096e1130aefa8ee21de38bd1147752bc.svg 'MCP Dev')

 alt="fastapi-mcp-usage" height="400"/>

## 特性

- **直接集成** - 直接将 MCP 服务器挂载到你的 FastAPI 应用
- **零配置** - 只需指向你的 FastAPI 应用即可工作
- **自动发现** - 自动发现所有 FastAPI 端点并转换为 MCP 工具
- **保留模式** - 保留请求模型和响应模型的模式
- **保留文档** - 保留所有端点的文档，就像在 Swagger 中一样
- **扩展** - 在自动生成的 MCP 工具旁边添加自定义 MCP 工具

## 安装

我们推荐使用 [uv](https://docs.astral.sh/uv/)，这是一个快速的 Python 包安装器：

```bash
uv add fastapi-mcp
```

或者，你可以使用 pip 安装：

```bash
pip install fastapi-mcp
```

## 基本用法

使用 FastAPI-MCP 的最简单方法是直接将 MCP 服务器添加到你的 FastAPI 应用中：

```python
from fastapi import FastAPI
from fastapi_mcp import add_mcp_server

# Your FastAPI app
app = FastAPI()

# Mount the MCP server to your app
add_mcp_server(
    app,                    # Your FastAPI app
    mount_path="/mcp",      # Where to mount the MCP server
    name="My API MCP",      # Name for the MCP server
)
```

就这样！你的自动生成的 MCP 服务器现在可以在 `https://app.base.url/mcp` 访问了。

## 高级用法

FastAPI-MCP 提供了几种自定义和控制 MCP 服务器创建和配置的方法。以下是一些高级用法模式：

```python
from fastapi import FastAPI
from fastapi_mcp import add_mcp_server

app = FastAPI()

mcp_server = add_mcp_server(
    app,                                    # Your FastAPI app
    mount_path="/mcp",                      # Where to mount the MCP server
    name="My API MCP",                      # Name for the MCP server
    describe_all_responses=True,            # False by default. Include all possible response schemas in tool descriptions, instead of just the successful response.
    describe_full_response_schema=True      # False by default. Include full JSON schema in tool descriptions, instead of just an LLM-friendly response example.
)

# Optionally add custom tools in addition to existing APIs.
@mcp_server.tool()
async def get_server_time() -> str:
    """Get the current server time."""
    from datetime import datetime
    return datetime.now().isoformat()
```

## 示例

请参阅 examples 目录中的完整示例。

## 使用 SSE 连接到 MCP 服务器

一旦你的带有 MCP 集成的 FastAPI 应用程序运行起来，你可以使用任何支持 SSE 的 MCP 客户端（如 Cursor）连接到它：

1. 运行你的应用程序。

2. 在 Cursor -> 设置 -> MCP 中，使用你的 MCP 服务器端点的 URL（例如 `http://localhost:8000/mcp`）作为 sse。

3. Cursor 将自动发现所有可用的工具和资源。

## 使用 [mcp-proxy stdio](https://github.com/sparfenyuk/mcp-proxy?tab=readme-ov-file#1-stdio-to-sse) 连接到 MCP 服务器

如果你的 MCP 客户端不支持 SSE，例如 Claude Desktop： 

1. 运行你的应用程序。

2. 安装 [mcp-proxy](https://github.com/sparfenyuk/mcp-proxy?tab=readme-ov-file#installing-via-pypi)，例如：`uv tool install mcp-proxy`。

3. 在 Claude Desktop MCP 配置文件 (`claude_desktop_config.json`) 中添加：

在 Windows 上：
```json
{
  "mcpServers": {
    "my-api-mcp-proxy": {
        "command": "mcp-proxy",
        "args": ["http://127.0.0.1:8000/mcp"]
    }
  }
}
```
在 MacOS 上： 
```json
{
  "mcpServers": {
    "my-api-mcp-proxy": {
        "command": "/Full/Path/To/Your/Executable/mcp-proxy",
        "args": ["http://127.0.0.1:8000/mcp"]
    }
  }
}
```
通过在终端中运行 `which mcp-proxy` 来找到 mcp-proxy 的路径。

4. Claude Desktop 会自动发现所有可用的工具和资源

## 开发与贡献

感谢您考虑为 FastAPI-MCP 开源项目做出贡献！正是像您这样的人让我们的社区用户能够真正使用这些项目。

在开始之前，请参阅 [CONTRIBUTING.md](https://github.com/tadata-org/fastapi_mcp/blob/HEAD/CONTRIBUTING.md)。

## 社区

加入 [MCParty Slack 社区](https://join.slack.com/t/themcparty/shared_invite/zt-30yxr1zdi-2FG~XjBA0xIgYSYuKe7~Xg)，与其他 MCP 爱好者联系，提问并分享您使用 FastAPI-MCP 的经验。

## 要求

- Python 3.10+
- uv

## 许可证

MIT 许可证。版权所有 (c) 2024 Tadata Inc.

## 关于

由 [Tadata Inc.](https://github.com/tadata-org) 开发和维护

**官方网站：** [https://github.com/tadata-org/fastapi_mcp](https://github.com/tadata-org/fastapi_mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`mcp-proxy`
- 参数：`http://127.0.0.1:8000/mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/tadata-org-fastapi.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
