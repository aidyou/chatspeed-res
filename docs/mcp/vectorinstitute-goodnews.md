---
title: "MCP积极新闻"
description: "一种模型上下文协议服务器，它通过Cohere语言模型的情感分析功能从NewsAPI获取并排名正面新闻文章，使用户能够通过Claude Desktop等界面访问鼓舞人心的新闻故事。"
---

# MCP积极新闻

一种模型上下文协议服务器，它通过Cohere语言模型的情感分析功能从NewsAPI获取并排名正面新闻文章，使用户能够通过Claude Desktop等界面访问鼓舞人心的新闻故事。

# MCP 好消息

---

[![CodeQL](/mcp-assets/7cb6a07622c89f1868d26563ea3805aa.svg)](https://github.com/VectorInstitute/mcp-goodnews/actions/workflows/github-code-scanning/codeql)
[![Linting](/mcp-assets/265aa86a63acfcc94b0810633c43edd8.svg)](https://github.com/VectorInstitute/mcp-goodnews/actions/workflows/lint.yml)
[![单元测试和上传覆盖率](/mcp-assets/330ad3cad933784a3af4ce0d96f20edb.svg)](https://github.com/VectorInstitute/mcp-goodnews/actions/workflows/unit_test.yml)
[![codecov](/mcp-assets/1a234f4d2d89ec3ce218d06c6d518c8b.svg)](https://codecov.io/github/VectorInstitute/mcp-goodnews)
[![发布](/mcp-assets/d5ccd5c5c7571857b94be33d0359c687.svg)](https://github.com/VectorInstitute/mcp-goodnews/actions/workflows/release.yml)
![GitHub 许可证](/mcp-assets/443190a98194af50f87289b7ed6cab6a.svg)

  

MCP 好消息是一个简单的模型上下文协议（MCP）应用程序，它包含一个用于获取积极、正面和鼓舞人心的新闻的服务器。此工具从 [NewsAPI](https://newsapi.org/) 获取新闻文章，并使用 Cohere LLM 根据正面情绪对新闻进行排名并返回顶级新闻文章。

## 动机

在一个负面新闻常常占据头条的世界里，好消息 MCP 旨在突出更多积极和鼓舞人心的新闻故事。这个项目受到了早期名为 GoodnewsFirst 的倡议的启发，该倡议每天向电子邮件订阅者提供积极的新闻——这是一个非常棒的项目！虽然 GoodnewsFirst 出现在最近大型语言模型（LLMs）突破之前，并依赖于传统的感情排名方法，但好消息 MCP 利用现代 LLMs 在零样本设置下执行情感分析。

## 示例用法：Claude 桌面版上的 MCP 好消息

### 要求

- [Cohere API 密钥](https://dashboard.cohere.com/)
- [NewsAPI 密钥](https://newsapi.org/)
- [Claude 桌面应用程序](https://claude.ai/download)
- [uv Python 项目和包管理器](https://docs.astral.sh/uv/getting-started/installation/)

### 克隆 `mcp-goodnews`

```bash
# Clone the repository
git clone https://github.com/VectorInstitute/mcp-goodnews.git
```

在下一步中，我们需要提供克隆仓库位置的绝对路径。

### 更新 Claude 桌面配置以找到 mcp-goodnews

#### 对于 Mac/Linux

```bash
# Navigate to the configuration directory
cd ~/Library/Application\ Support/Claude/config

# Edit the claude_desktop_config.json file
nano claude_desktop_config.json
```

#### 对于 Windows

```bash
# Navigate to the configuration directory
cd %APPDATA%\Claude\config

# Edit the claude_desktop_config.json file
notepad claude_desktop_config.json
```

并且你需要在 `mcpServers` 下为 `Goodnews` 添加一个条目：

```json
{
  "mcpServers": {
    "Goodnews": {
      "command": "
/uv",
      "args": [
        "--directory",
        "
/mcp-goodnews/src/mcp_goodnews",
        "run",
        "server.py"
      ],
      "env": {
        "NEWS_API_KEY": "",
        "COHERE_API_KEY": ""
      }
    }
  }
}
```

### 启动或重启 Claude 桌面

Claude 桌面将使用更新后的配置来构建并运行 mcp-goodnews 服务器。
如果成功，你将在聊天对话窗口的右下角看到锤子工具图标。

点击锤子工具图标将弹出一个模态框，其中列出了可用的MCP工具。
你应该能在列表中看到`fetch_list_of_goodnews`。

### 向Claude询问好消息！

示例提示：

- "给我看一些今天的正面新闻。"
- "这周世界上发生了哪些积极的事情？"
- "给我一些关于科学的鼓舞人心的新闻报道。"

## 工作原理

1. 当您请求好消息时，应用程序会向NewsAPI查询最近的文章
2. Cohere LLM分析每篇文章的情绪
3. 文章根据正面情绪得分进行排名
4. 通过Claude返回给您排名最高的好消息故事

## 许可证

[Apache 2.0](https://github.com/VectorInstitute/mcp-goodnews/blob/HEAD/LICENSE)

---

_通过Goodnews MCP保持乐观！_

**官方网站：** [https://github.com/VectorInstitute/mcp-goodnews](https://github.com/VectorInstitute/mcp-goodnews)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`search`, `research and data`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`<absolute-path-to-bin>/uv`
- 参数：`--directory <absolute-path-to-cloned-repo>/mcp-goodnews/src/mcp_goodnews run server.py`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/vectorinstitute-goodnews.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
