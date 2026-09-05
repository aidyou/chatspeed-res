---
title: "Tavily智搜"
description: "该服务器使AI系统能够与Tavily的搜索和数据提取工具集成，提供实时的网络信息访问和领域特定的搜索。"
---

# Tavily智搜

该服务器使AI系统能够与Tavily的搜索和数据提取工具集成，提供实时的网络信息访问和领域特定的搜索。

# Tavily MCP 服务器 

![GitHub Repo stars](/mcp-assets/2c43d86a5c7e70011ed1d24ae527b2d6.svg)
![npm](/mcp-assets/aafae7ed7f5b12a9b3239f7ddfe732e5.svg)

>  **兼容 [Cline](https://github.com/cline/cline), [Cursor](https://cursor.sh), [Claude Desktop](https://claude.ai/desktop) 以及其他任何 MCP 客户端！**
>
> Tavily MCP 也与任何 MCP 客户端兼容
>
>   结合 Tavily MCP 与 Neo4j MCP 服务器的 [教程](https://medium.com/@dustin_36183/building-a-knowledge-graph-assistant-combining-tavily-and-neo4j-mcp-servers-with-claude-db92de075df9)!
> 
>   在 VS Code 中将 Tavily MCP 与 Cline 集成的 [教程](https://medium.com/@dustin_36183/connect-your-coding-assistant-to-the-web-integrating-tavily-mcp-with-cline-in-vs-code-5f923a4983d1) (演示 + 示例用例)
>

模型上下文协议（MCP）是一个开放标准，它使 AI 系统能够无缝地与各种数据源和工具进行交互，促进安全的双向连接。

由 Anthropic 开发的模型上下文协议（MCP）使像 Claude 这样的 AI 助手能够无缝集成 Tavily 的高级搜索和数据提取功能。这种集成提供了对网络信息的实时访问，具备复杂的过滤选项和特定领域的搜索功能。

Tavily MCP 服务器提供：
- 与 tavily-search 和 tavily-extract 工具的无缝交互
- 通过 tavily-search 工具实现实时网络搜索能力
- 通过 tavily-extract 工具从网页中智能提取数据

## 前提条件 

在开始之前，请确保您已具备以下条件：

- [Tavily API 密钥](https://app.tavily.com/home)
  - 如果您还没有 Tavily API 密钥，可以在此处注册一个免费帐户 [这里](https://app.tavily.com/home)
- [Claude Desktop](https://claude.ai/download) 或 [Cursor](https://cursor.sh)
- [Node.js](https://nodejs.org/) (v20 或更高版本)
  - 您可以通过运行以下命令来验证 Node.js 安装：
    - `node --version`
- [Git](https://git-scm.com/downloads) 安装（仅在使用 Git 安装方法时需要）
  - 在 macOS 上：`brew install git`
  - 在 Linux 上：
    - Debian/Ubuntu: `sudo apt install git`
    - RedHat/CentOS: `sudo yum install git`
  - 在 Windows 上：下载 [Git for Windows](https://git-scm.com/download/win)

## Tavily MCP 服务器安装 

### 使用 NPX 运行

```bash
npx -y tavily-mcp@0.1.4  
```

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@tavily-ai/tavily-mcp) 自动为 Claude Desktop 安装 Tavily MCP 服务器：

```bash
npx -y @smithery/cli install @tavily-ai/tavily-mcp --client claude
```

虽然您可以单独启动服务器，但这在孤立状态下并不是特别有用。相反，您应该将其集成到 MCP 客户端中。下面是如何配置 Claude Desktop 应用程序以与 tavily-mcp 服务器一起工作的示例。

## 配置 MCP 客户端 

此仓库将解释如何配置 [Cursor](https://cursor.sh) 和 [Claude Desktop](https://claude.ai/desktop) 以与 tavily-mcp 服务器一起工作。

### 配置 Cline 

在 Cline 中设置 Tavily MCP 服务器最简单的方法是通过市场一键安装：

1. 在 VS Code 中打开 Cline
2. 点击侧边栏中的 Cline 图标
3. 导航到 "MCP Servers" 标签（4个方块图标）
4. 搜索 "Tavily" 并点击 "安装"
5. 当提示时，输入你的 Tavily API 密钥

或者，你可以手动在 Cline 中设置 Tavily MCP 服务器：

1. 打开 Cline MCP 设置文件：

   ### 对于 macOS：
```bash
   # 使用 Visual Studio Code
   code ~/Library/Application\ Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json
   
   # 或者使用 TextEdit
   open -e ~/Library/Application\ Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json
```

   ### 对于 Windows：
```bash
   code %APPDATA%\Code\User\globalStorage\saoudrizwan.claude-dev\settings\cline_mcp_settings.json
```

2. 将 Tavily 服务器配置添加到文件中：

   将 `your-api-key-here` 替换为你的实际 [Tavily API 密钥](https://tavily.com/api-keys)。

```json
   {
     "mcpServers": {
       "tavily-mcp": {
         "command": "npx",
         "args": ["-y", "tavily-mcp@0.1.4"],
         "env": {
           "TAVILY_API_KEY": "your-api-key-here"
         },
         "disabled": false,
         "autoApprove": []
       }
     }
   }
```

3. 保存文件。如果 Cline 已经运行，请重启它。

4. 使用 Cline 时，你现在可以访问 Tavily MCP 工具了。你可以在对话中直接要求 Cline 使用 tavily-search 和 tavily-extract 工具。

### 配置 Cursor 

> **注意**：需要 Cursor 版本 0.45.6 或更高版本

要在 Cursor 中设置 Tavily MCP 服务器：

1. 打开 Cursor 设置
2. 导航到 Features > MCP Servers
3. 点击 "+ Add New MCP Server" 按钮
4. 填写以下信息：
   - **名称**：输入服务器的昵称（例如："tavily-mcp"）
   - **类型**：选择 "command" 作为类型
   - **命令**：输入运行服务器的命令：
```bash
     env TAVILY_API_KEY=your-api-key npx -y tavily-mcp@0.1.4
```
     > **重要**：将 `your-api-key` 替换为你的 Tavily API 密钥。你可以在 [app.tavily.com/home](https://app.tavily.com/home) 获取一个。

添加服务器后，它应该会出现在 MCP 服务器列表中。可能需要手动点击 MCP 服务器右上角的刷新按钮来填充工具列表。

Composer Agent 会根据您的查询自动使用 Tavily MCP 工具。最好通过描述您想做的事情来明确请求使用这些工具（例如，“使用 tavily-search 搜索有关 AI 的最新新闻”）。在 Mac 上，按 command + L 打开聊天界面，在屏幕顶部选择 composer 选项，然后在提交按钮旁边选择 agent，并在准备就绪时提交查询。

### 配置 Claude 桌面应用程序 
### 对于 macOS：

```bash
# Create the config file if it doesn't exist
touch "$HOME/Library/Application Support/Claude/claude_desktop_config.json"

# Opens the config file in TextEdit 
open -e "$HOME/Library/Application Support/Claude/claude_desktop_config.json"

# Alternative method using Visual Studio Code (requires VS Code to be installed)
code "$HOME/Library/Application Support/Claude/claude_desktop_config.json"
```

### 对于 Windows：
```bash
code %APPDATA%\Claude\claude_desktop_config.json
```

### 添加 Tavily 服务器配置：

将 `your-api-key-here` 替换为您实际的 [Tavily API 密钥](https://tavily.com/api-keys)。

```json
{
  "mcpServers": {
    "tavily-mcp": {
      "command": "npx",
      "args": ["-y", "tavily-mcp@0.1.2"],
      "env": {
        "TAVILY_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

### 2. Git 安装

1. 克隆仓库：
```bash
git clone https://github.com/tavily-ai/tavily-mcp.git
cd tavily-mcp
```

2. 安装依赖项：
```bash
npm install
```

3. 构建项目：
```bash
npm run build
```

### 配置 Claude 桌面应用程序 
按照上述[配置 Claude 桌面应用程序](#configuring-the-claude-desktop-app-)部分中概述的配置步骤操作，使用下面的 JSON 配置。

将 `your-api-key-here` 替换为您实际的 [Tavily API 密钥](https://tavily.com/api-keys)，并将 `/path/to/tavily-mcp` 替换为您系统上克隆仓库的实际路径。

```json
{
  "mcpServers": {
    "tavily": {
      "command": "npx",
      "args": ["/path/to/tavily-mcp/build/index.js"],
      "env": {
        "TAVILY_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

## 在 Claude 桌面应用程序中的使用 

安装完成后并配置好 Claude 桌面应用程序后，您必须完全关闭并重新打开 Claude 桌面应用程序才能看到 tavily-mcp 服务器。您应该会在应用程序左下角看到一个锤子图标，表示可用的 MCP 工具，您可以点击锤子图标以查看更多关于 tavily-search 和 tavily-extract 工具的信息。

现在 Claude 将能够完全访问 tavily-mcp 服务器，包括 tavily-search 和 tavily-extract 工具。如果您将以下示例插入 Claude 桌面应用程序中，您应该能看到 tavily-mcp 服务器工具的效果。

### Tavily 搜索示例

1. **通用网页搜索**：
```
Can you search for recent developments in quantum computing?
```

2. **新闻搜索**：
```
Search for news articles about AI startups from the last 7 days.
```

3. **特定领域搜索**：
```
Search for climate change research on nature.com and sciencedirect.com
```

### Tavily 提取示例 

1. **提取文章内容**：
```
Extract the main content from this article: https://example.com/article
```

###  结合搜索和提取功能 

您还可以结合使用 tavily-search 和 tavily-extract 工具来执行更复杂的任务。

```
Search for news articles about AI startups from the last 7 days and extract the main content from each article to generate a detailed report.
```

## 故障排除 

### 常见问题

1. **找不到服务器**
   - 通过运行 `npm --verison` 来验证 npm 安装。
   - 通过运行 `code ~/Library/Application\ Support/Claude/claude_desktop_config.json` 检查 Claude 桌面配置语法。
   - 通过运行 `node --version` 确保正确安装了 Node.js。
   
2. **NPX 相关问题**
  - 如果遇到与 `npx` 相关的错误，可能需要使用 npx 可执行文件的完整路径。
  - 您可以通过在终端中运行 `which npx` 查找此路径，然后在配置中将 `"command": "npx"` 这一行替换为 `"command": "/full/path/to/npx"`。

3. **API 密钥问题**
   - 确认您的 Tavily API 密钥有效
   - 检查配置中是否正确设置了 API 密钥
   - 确认 API 密钥周围没有空格或引号

## 致谢 

- [Model Context Protocol](https://modelcontextprotocol.io) 提供了 MCP 规范
- [Anthropic](https://anthropic.com) 提供了 Claude Desktop

**官方网站：** [https://github.com/tavily-ai/tavily-mcp](https://github.com/tavily-ai/tavily-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`, `browser`
- 标签：`search`, `browser automation`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y tavily-mcp@0.1.4`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/tavily-ai-tavily.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
