---
title: "GitHub MCP 转换服务"
description: "一项免费、开源的服务，可将 GitHub 项目转换为 MCP 端点，使人工智能助手能够在无需任何设置的情况下访问和理解项目文档。"
---

# GitHub MCP 转换服务

一项免费、开源的服务，可将 GitHub 项目转换为 MCP 端点，使人工智能助手能够在无需任何设置的情况下访问和理解项目文档。

# GitMCP

 />

  
GitMCP是什么
 •
  
功能
 •
  
快速开始
 •
  
工作原理
 •
  
示例
 •
  
常见问题解答
 •
  
隐私
 •
  
贡献指南
 •
  
许可证

[![Twitter Follow](/mcp-assets/cf3bd9486561f3b7327e31cbbf2fffc1.svg)](https://twitter.com/idosal1)
[![Twitter Follow](/mcp-assets/8494e03e35786995266c756ccc470a3b.svg)](https://twitter.com/liadyosef)

  

## 🤔 GitMCP是什么？
**停止幻想，开始实际编码！**

[GitMCP](https://gitmcp.io) 是一个免费、开源的远程 [Model Context Protocol (MCP)](https://docs.anthropic.com/en/docs/agents-and-tools/mcp) 服务器，它可以将**任何** GitHub 项目（仓库或 GitHub 页面）转换成文档中心。它允许像 Cursor 这样的 AI 工具访问最新的文档和代码，从而无缝结束代码幻觉。

## ✨ 功能

- 😎 **任意 GitHub 项目的最新文档**：让您的 AI 助手无缝访问 GitHub 项目的文档和代码。内置的智能搜索功能帮助找到 AI 需要的确切内容，而不会使用过多的令牌！
- 🧠 **不再有幻觉**：有了 GitMCP，您的 AI 助手可以为您提供准确且相关的答案。
- ☁️ **零配置**：GitMCP 在云端运行。只需将选择的 GitMCP URL 添加为 IDE 中的 MCP 服务器即可——无需下载、安装、注册或更改。
- ✅ **免费且私密**：GitMCP 是开源的，完全免费使用。它不收集个人信息或存储查询。您甚至可以自行托管！

## 🚀 快速开始

使用 GitMCP 很简单！请按照以下步骤操作：

### 第一步：选择您想要的服务器类型

根据您想连接的内容选择以下 URL 格式之一：

- 对于 GitHub 仓库：`gitmcp.io/{owner}/{repo}` 
- 对于 GitHub Pages 站点：`{owner}.gitmcp.io/{repo}`
- 对于支持任何仓库的通用工具（动态）：`gitmcp.io/docs`

将 `{owner}` 替换为 GitHub 用户名或组织名称，并将 `{repo}` 替换为仓库名称。

为了方便起见，您还可以使用着陆页上的转换工具将 GitHub URL 转换成 MCP URL！

### 第二步：连接您的 AI 助手

从下面的选项中选择您的 AI 助手并按照配置说明进行操作：

#### 连接 Cursor

更新您的 Cursor 配置文件 `~/.cursor/mcp.json`:
```json
{
  "servers": [
    {
      "name": "My GitHub Project",
      "url": "gitmcp.io/{owner}/{repo}"
    }
  ]
}
```

将 `{owner}` 和 `{repo}` 替换为您实际的 GitHub 用户名和仓库名称。

```json
   {
     "mcpServers": {
       "gitmcp": {
         "url": "https://gitmcp.io/{owner}/{repo}"
       }
     }
   }
```

#### 连接 Claude 桌面版

1. 在 Claude 桌面版中，进入设置 > 开发者 > 编辑配置
2. 将配置替换为：
```json
   {
     "mcpServers": {
       "gitmcp": {
         "command": "npx",
         "args": [
           "mcp-remote",
           "https://gitmcp.io/{owner}/{repo}"
         ]
       }
     }
   }
```

#### 连接 Windsurf

更新你的 Windsurf 配置文件 `~/.codeium/windsurf/mcp_config.json`:
```json
   {
     "mcpServers": {
       "gitmcp": {
         "serverUrl": "https://gitmcp.io/{owner}/{repo}"
       }
     }
   }
```

#### 连接 VSCode

更新你的 VSCode 配置文件 `.vscode/mcp.json`:
```json
   {
     "servers": {
       "gitmcp": {
         "type": "sse",
         "url": "https://gitmcp.io/{owner}/{repo}"
       }
     }
   }
```

#### 连接 Cline

更新你的 Cline 配置文件 `~/Library/Application Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`:
```json
   {
     "mcpServers": {
       "gitmcp": {
         "url": "https://gitmcp.io/{owner}/{repo}",
         "disabled": false,
         "autoApprove": []
       }
     }
   }
```

#### 连接 Highlight AI

1. 打开 Highlight AI 并点击侧边栏中的插件图标（@ 符号）
2. 点击侧边栏顶部的 **已安装插件**
3. 选择 **自定义插件**
4. 点击 **使用自定义 SSE URL 添加插件**

插件名称: `gitmcp`
SSE URL: `https://gitmcp.io/{owner}/{repo}`

有关向 HighlightAI 添加自定义 MCP 服务器的更多详细信息，请参阅[文档](https://docs.highlightai.com/learn/developers/plugins/custom-plugins-setup)。

> **注意:** 请记得将 `{owner}` 和 `{repo}` 替换为实际的 GitHub 用户名/组织和仓库名称。你也可以使用动态端点 `https://gitmcp.io/docs` 来允许你的 AI 助手按需访问任何仓库。

## ⚙️ 工作原理

GitMCP 使用模型上下文协议 (MCP) 将你的 AI 助手连接到 GitHub 仓库，这是一种标准，可以让 AI 工具从外部源请求额外的信息。

当你使用 GitMCP 时会发生什么：

1. **你向 AI 助手提供 GitMCP URL**（例如 `gitmcp.io/microsoft/typescript`）。GitMCP 提供诸如文档获取、智能搜索、代码搜索等工具。
2. **提示 AI 助手** 关于文档或代码相关的问题。
3. **你的 AI 发送请求** 到 GitMCP 以使用其工具（需要你的批准）。
4. **GitMCP 执行 AI 的请求** 并返回请求的数据。
5. **你的 AI 接收到信息** 并生成更准确、有根据的响应，而不会出现幻觉。

### 支持的文档

GitMCP 目前支持以下文档（按优先级顺序）：
1. [llms.txt](https://llmstxt.org)
2. 项目的 AI 优化版本文档
3. `README.md`/根目录

## 💡 示例

这里有一些示例，展示了如何使用不同的 AI 助手和仓库与 GitMCP 一起工作：

### 示例 1：使用 Windsurf 与特定仓库

对于 GitHub 仓库 `https://github.com/microsoft/playwright-mcp`，将 `https://gitmcp.io/microsoft/playwright-mcp` 作为 MCP 服务器添加到 Windsurf 中。

**提示给 Claude：**
> "我该如何使用 Playwright MCP"

Windsurf 将从 GitMCP 拉取相关文档以正确实现记忆功能。

### 示例 2：使用 Cursor 与 GitHub Pages 站点

```

对于 GitHub Pages 站点 `langchain-ai.github.io/langgraph`，将 `https://langchain-ai.gitmcp.io/langgraph` 作为 MCP 服务器添加到 Cursor 中。

**给 Cursor 的提示：**
> "为我的 LangGraph 代理添加记忆功能"

Cursor 将从 GitMCP 拉取相关的文档和代码以正确实现记忆功能。

### 示例 3：使用动态端点的 Claude Desktop

您不必选择特定的仓库。通用的 `gitmcp.io/docs` 端点允许 AI 实时选择 GitHub 项目！

**给任何 AI 助手的提示：**
> "我想了解 OpenAI Whisper 语音识别模型。解释一下它是如何工作的。"

Claude 将从 GitMCP 拉取数据并回答问题。

## 🛠️ 工具

GitMCP 为 AI 助手提供了几个有价值的工具，帮助它们访问、理解和查询 GitHub 仓库。

### `fetch__documentation`

此工具从 GitHub 仓库获取主要文档。它通过检索相关文档（例如 `llms.txt`）来工作。这使 AI 能够对项目的概要有一个很好的了解。

**何时有用：** 对于关于项目目的、特性或如何开始的一般问题

### `search__documentation`

此工具允许 AI 通过提供特定的搜索查询来搜索仓库中的文档。而不是加载所有文档（这可能非常庞大），它使用智能搜索来找到仅相关的部分。

**何时有用：** 对于有关项目内特定功能、函数或概念的具体问题

### `fetch_url_content`

此工具帮助 AI 从文档中提到的链接获取信息。它从这些链接中检索内容，并将其转换为 AI 可以轻松阅读的格式。

**何时有用：** 当文档引用了有助于回答您的问题的外部信息时

### `search__code`

此工具使用 GitHub 的代码搜索在仓库的实际代码中进行搜索。它帮助 AI 找到具体的代码示例或实现细节。

**何时有用：** 当您想要某些实现示例或需要文档中未涵盖的技术细节时

> **注意：** 使用动态端点 (`gitmcp.io/docs`) 时，这些工具的命名略有不同（如 `fetch_generic_documentation`、`search_generic_code` 和 `search_generic_documentation`），并且需要额外的信息来指定要访问哪个仓库。

## ❓ 常见问题

### 什么是 Model Context Protocol？

[Model Context Protocol](https://link.5) 是一个标准，允许 AI 助手以结构化的方式请求和接收来自外部源的额外上下文，从而增强其理解和性能。

### GitMCP 是否与任何 AI 助手兼容？

是的，GitMCP 与支持 Model Context Protocol 的任何 AI 助手兼容，包括像 Cursor、VSCode、Claude 等工具。

### GitMCP 是否与所有 GitHub 项目兼容？

当然！GitMCP 可以与任何公共 GitHub 仓库一起使用，而无需进行任何修改。它优先考虑 `llms.txt` 文件，如果该文件不可用，则会回退到 `README.md` 或其他页面。未来的更新计划支持更多的文档方法，甚至动态生成内容。

### GitMCP 是否收费？

不，GitMCP 是一个免费的服务，对社区没有任何费用。

## 🔒 隐私

GitMCP 深度致力于保护用户的隐私。该服务不需要认证，因此不会访问或存储任何个人身份信息。此外，它不会存储代理发送的任何查询。而且，由于 GitMCP 是一个开源项目，你可以在自己的环境中独立部署。

GitMCP 只访问已经公开的内容，并且只有在用户查询时才会这样做。GitMCP 不会自动抓取仓库。在访问任何 GitHub Pages 站点之前，代码会检查 `robots.txt` 规则并遵循站点所有者设定的指令，允许他们选择退出。请注意，GitMCP 不会永久存储关于 GitHub 项目及其内容的数据。

## 👥 贡献

我们欢迎贡献、反馈和想法！请查阅我们的 [贡献指南](https://link.6)。

### 本地开发环境设置

1. **克隆仓库**
```bash
   git clone https://github.com/idosal/git-mcp.git
   cd git-mcp
```

2. **安装依赖**
```bash
   pnpm install
```

3. **本地运行以进行开发**
```bash
   npm run dev
   # 或者
   pnpm dev
```

#### 使用 MCP Inspector 进行测试

1. 安装 MCP Inspector 工具：
```bash
   npx @modelcontextprotocol/inspector
```

2. 在检查器界面中：
   - 将传输类型设置为 `SSE`
   - 输入你的 GitMCP URL（例如：`http://localhost:5173/docs`）
   - 点击“连接”

## 📄 许可证

本项目采用 [Apache License 2.0](https://github.com/idosal/git-mcp/blob/HEAD/LICENSE) 许可。

## 免责声明

GitMCP 按“原样”提供，不附带任何形式的保证。虽然我们努力确保服务的可靠性和安全性，但我们不对使用过程中可能出现的任何损害或问题负责。通过 GitMCP 访问的 GitHub 项目受其各自所有者的条款和条件约束。GitMCP 与 GitHub 或上述任何 AI 工具无关。

## Star 历史

[![Star History Chart](/mcp-assets/7ff5ea12648cd650854ef8cf69c6f49e.svg)](https://www.star-history.com/#idosal/git-mcp&Timeline)
```

**官方网站：** [https://github.com/idosal/git-mcp](https://github.com/idosal/git-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`, `version control`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`mcp-remote https://gitmcp.io/{owner}/{repo}`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/idosal-git.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
