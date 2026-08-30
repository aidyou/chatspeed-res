---
title: "DevHub CMS MCP内容管理"
description: "模型上下文协议（MCP）集成，用于在DevHub CMS系统中管理内容（博客文章、内容、位置管理）。"
---

# DevHub CMS MCP内容管理

模型上下文协议（MCP）集成，用于在DevHub CMS系统中管理内容（博客文章、内容、位置管理）。

# DevHub CMS MCP

[Smithery](https://smithery.ai/server/@devhub/devhub-cms-mcp)

一个用于管理 [DevHub CMS 系统](https://www.devhub.com/)内容的 [模型上下文协议 (MCP)](https://modelcontextprotocol.io/) 集成。

## 安装

您需要在本地系统上安装 [uv](https://github.com/astral-sh/uv) 包管理器。

### Claude Desktop 的手动配置

要将此服务器与 [Claude Desktop 应用程序](https://claude.ai/download) 一起使用，请将以下配置添加到 `claude_desktop_config.json` 文件的 "mcpServers" 部分：

```
{
    "mcpServers": {
        "devhub_cms_mcp": {
            "command": "uvx",
            "args": [
                "devhub-cms-mcp"
            ],
            "env": {
                "DEVHUB_API_KEY": "YOUR_KEY_HERE",
                "DEVHUB_API_SECRET": "YOUR_SECRET_HERE",
                "DEVHUB_BASE_URL": "https://yourbrand.cloudfrontend.net"
            }
        }
    }
}
```

更新配置后，重启 Claude Desktop。

### Cursor 的手动配置

此 MCP 也可以通过类似上面的配置添加到您的 [Cursor](https://www.cursor.com/) 全局环境或单个项目中。

示例 [这里](https://docs.cursor.com/context/model-context-protocol#configuring-mcp-servers)

### 通过 Claude Code 安装

Claude Code 的命令行 [支持 MCP 安装](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/tutorials#set-up-model-context-protocol-mcp)。

可以通过更新下面的环境变量来添加 `devhub-cms-mcp`：

```
claude mcp add devhub-cms-mcp \
    -e DEVHUB_API_KEY=YOUR_KEY_HERE \
    -e DEVHUB_API_SECRET=YOUR_SECRET_HERE \
    -e DEVHUB_BASE_URL=https://yourbrand.cloudfrontend.net \
    -- uvx devhub-cms-mcp
```

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@devhub/devhub-cms-mcp) 自动为 Claude Desktop 安装 DevHub CMS MCP：

```bash
npx -y @smithery/cli install @devhub/devhub-cms-mcp --client claude
```

## 本地开发

### 克隆仓库（或您的分支）

```
git clone git@github.com:devhub/devhub-cms-mcp.git
```

### Claude Desktop 的手动配置

为了在本地开发中使用此服务器与 Claude Desktop 应用程序，请将以下配置添加到 `claude_desktop_config.json` 文件的 "mcpServers" 部分：

```
{
    "mcpServers": {
        "devhub_cms_mcp": {
            "command": "uv",
            "args": [
                "--directory",
                "/YOUR/LOCAL/PATH/devhub-cms-mcp/",
                "run",
                "main.py"
            ],
            "env": {
                "DEVHUB_API_KEY": "YOUR_KEY_HERE",
                "DEVHUB_API_SECRET": "YOUR_SECRET_HERE",
                "DEVHUB_BASE_URL": "https://yourbrand.cloudfrontend.net"
            }
        }
    }
}
```

更新配置后，重启 Claude Desktop。

### 使用 `uv` 直接运行的配置

此 MCP 要求设置以下环境变量：

```bash
export DEVHUB_API_KEY="your_api_key"
export DEVHUB_API_SECRET="your_api_secret"
export DEVHUB_BASE_URL="https://yourbrand.cloudfrontend.net"
```

然后运行 MCP

```
uv run main.py
```

## 可用工具

此 MCP 提供了以下工具以与 DevHub CMS 交互：

### 位置管理

- **get_hours_of_operation(location_id)**: 获取特定 DevHub 位置的营业时间。返回每周每天的时间段列表。
- **update_hours(location_id, new_hours, hours_type='primary')**: 更新 DevHub 位置的营业时间。
- **get_nearest_location(business_id, latitude, longitude)**: 根据地理坐标查找最近的 DevHub 位置。

### 内容管理

- **get_blog_post(post_id)**: 按 ID 检索单个博客文章，包括其标题、日期和 HTML 内容。
- **create_blog_post(site_id, title, content)**: 创建新的博客文章。内容应为 HTML 格式，并且不应包含 H1 标签。
- **update_blog_post(post_id, title=None, content=None)**: 更新现有博客文章的标题和/或内容。

### 媒体管理

- **upload_image(base64_image_content, filename)**: 将图像上传到 DevHub 媒体库。支持 webp、jpeg 和 png 格式。图像必须作为 base64 编码的字符串提供。

## 与 LLMs 一起使用

这份MCP设计用于支持模型上下文协议的大型语言模型。它允许LLMs在无需直接集成API访问的情况下管理DevHub CMS中的内容。

## 测试

此包包含一个测试套件，其中包含了对DevHub API请求的模拟，这让你可以在不实际调用API的情况下测试功能。

### 运行测试

要运行测试，请首先安装带有测试依赖项的包：

```bash
uv pip install -e ".[test]"
```

使用pytest运行测试：

```bash
pytest
```

对于更详细的输出和测试覆盖率信息：

```bash
pytest -v --cov=devhub_cms_mcp
```

### 测试结构

- `tests/devhub_cms_mcp/test_mcp_integration.py`: MCP集成端点的测试

**官方网站：** [https://github.com/devhub/devhub-cms-mcp](https://github.com/devhub/devhub-cms-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`file systems`, `location services`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`devhub-cms-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/devhub-devhub-cms.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
