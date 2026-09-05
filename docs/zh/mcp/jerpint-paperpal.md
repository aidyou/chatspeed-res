---
title: "paperpal：论文伙伴"
description: "MCP扩展程序为大型语言模型（LLMs）提供对arXiv和Hugging Face论文的访问，使用户能够通过自然对话讨论论文、搜索新研究和组织文献综述。"
---

# paperpal：论文伙伴

MCP扩展程序为大型语言模型（LLMs）提供对arXiv和Hugging Face论文的访问，使用户能够通过自然对话讨论论文、搜索新研究和组织文献综述。

# paperpal

MCP 扩展，帮助您搜索和撰写文献综述

> 查看与[Claude的对话](https://claude.ai/share/0572fbd9-3ba2-4143-9f7f-5cae205c6d0d)，了解它可以做什么

## 工作原理

`paperpal` 使您的大型语言模型能够访问 [arxiv](https://www.arxiv.org) 和 [Hugging Face 论文](https://huggingface.co/papers)。
然后，您可以与您喜欢的语言模型（例如 Claude）进行自然对话，并让其指导您。

您可以：

* 讨论论文
* 寻找新论文
* 组织文献综述的想法
* 等等。

当然，这个工具的好坏取决于它的各个组成部分。语言模型仍然可能产生幻觉，且语义搜索永远不会是完美的。

## 快速开始

有许多不同的方式可以与 MCP 服务器交互。

### Claude 桌面应用程序

> 如果这是您第一次使用 MCP 服务器为 Claude 桌面应用程序，请参阅 https://modelcontextprotocol.io/quickstart/user

首先，将此仓库克隆到本地：

    git clone https://github.com/jerpint/paperpal

接下来，将扩展添加到您的应用中。打开配置文件（在 macOS 上应该是 `~/Library/Application Support/Claude/claude_desktop_config.json`），并将以下内容添加到扩展部分：

例如，在 MacOS 上：

```python
{
  "mcpServers": {
    "paperpal": {
      "command": "uv",
      "args": [
        "--directory",
        "/Users//paperpal",
        "run",
        "paperpal.py"
      ]
    }
  }
}
```

重启您的 Claude 桌面应用程序，您应该会看到它出现。

### Cursor

> 如果这是您第一次使用 MCP 服务器为 Cursor，请参阅 https://docs.cursor.com/context/model-context-protocol#remote-development

首先，将此仓库克隆到本地：

    git clone https://github.com/jerpint/paperpal

在项目的根目录下的 `.cursor/mcp.json` 文件中添加以下内容：

```
{
  "mcpServers": {
    "paperpal": {
      "command": "/Users/jeremypinto/.cargo/bin/uv",
      "args": [
        "--directory",
        "/Users/jeremypinto/paperpal",
        "run",
        "paperpal.py"
      ]
    }
  }
}
```

**官方网站：** [https://github.com/jerpint/paperpal](https://github.com/jerpint/paperpal)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`research and data`, `search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`/Users/jeremypinto/.cargo/bin/uv`
- 参数：`--directory /Users/jeremypinto/paperpal run paperpal.py`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/jerpint-paperpal.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
