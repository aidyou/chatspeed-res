---
title: "Exa搜索"
description: "模型上下文协议（MCP）服务器让像克劳德这样的AI助手可以使用Exa AI搜索API进行网络搜索。这种设置使AI模型能够以安全和受控的方式获取实时网络信息。"
---

# Exa搜索

模型上下文协议（MCP）服务器让像克劳德这样的AI助手可以使用Exa AI搜索API进行网络搜索。这种设置使AI模型能够以安全和受控的方式获取实时网络信息。

# Exa MCP 服务器 🔍
[![npm 版本](/mcp-assets/90e07ad32988cad1a586fe228cb593dd.svg)](https://www.npmjs.com/package/exa-mcp-server)
[Smithery](https://smithery.ai/server/exa)

Model Context Protocol (MCP) 服务器允许像 Claude 这样的 AI 助手使用 Exa AI 搜索 API 进行网络搜索。这种设置使 AI 模型能够以安全且受控的方式获取实时网络信息。

演示视频 [https://www.loom.com/share/ac676f29664e4c6cb33a2f0a63772038?sid=0e72619f-5bfc-415d-a705-63d326373f60](https://www.loom.com/share/ac676f29664e4c6cb33a2f0a63772038?sid=0e72619f-5bfc-415d-a705-63d326373f60)

## 什么是 MCP？🤔

Model Context Protocol (MCP) 是一种系统，它允许像 Claude Desktop 这样的 AI 应用程序连接到外部工具和数据源。它为 AI 助手提供了清晰且安全的方式来与本地服务和 API 交互，同时保持用户控制权。

## 这个服务器做什么？🚀

Exa MCP 服务器：
- 使 AI 助手能够使用 Exa 强大的搜索 API 进行网络搜索
- 提供结构化的搜索结果，包括标题、URL 和内容片段
- 缓存最近的搜索作为参考资源
- 优雅地处理速率限制和错误情况
- 支持实时网络爬取以获取最新内容

## 前提条件 📋

在开始之前，请确保您已安装：

- [Node.js](https://nodejs.org/)（版本 18 或更高）
- 已安装 [Claude Desktop](https://claude.ai/download)
- 一个 [Exa API 密钥](https://dashboard.exa.ai/api-keys)
- 安装了 Git

您可以运行以下命令来验证 Node.js 的安装：
```bash
node --version  # Should show v18.0.0 or higher
```

## 安装 🛠️

### NPM 安装

```bash
npm install -g exa-mcp-server
```

### 使用 Smithery

要通过 [Smithery](https://smithery.ai/server/exa) 自动为 Claude Desktop 安装 Exa MCP 服务器：

```bash
npx -y @smithery/cli install exa --client claude
```

### 手动安装

1. 克隆仓库：

```bash
git clone https://github.com/exa-labs/exa-mcp-server.git
cd exa-mcp-server
```

2. 安装依赖项：

```bash
npm install
```

3. 构建项目：

```bash
npm run build
```

4. 创建全局链接（这使得可以从任何地方执行该服务器）：

```bash
npm link
```

## 配置 ⚙️

### 1. 配置 Claude Desktop 以识别 Exa MCP 服务器

您可以在 Claude Desktop 应用程序的设置中找到 claude_desktop_config.json 文件：

打开 Claude Desktop 应用程序并从左上角菜单栏启用开发者模式。

启用后，从左上角菜单栏打开设置，并导航到开发者选项，您将在那里找到编辑配置按钮。点击它将打开 claude_desktop_config.json 文件，允许您进行必要的编辑。

或者（如果您想从终端打开 claude_desktop_config.json）

#### 对于 macOS：

1. 打开您的 Claude Desktop 配置文件：

```bash
code ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

#### 对于 Windows：

1. 打开您的 Claude Desktop 配置文件：

```powershell
code %APPDATA%\Claude\claude_desktop_config.json
```

### 2. 添加 Exa 服务器配置：

```json
{
  "mcpServers": {
    "exa": {
      "command": "npx",
      "args": ["/path/to/exa-mcp-server/build/index.js"],
      "env": {
        "EXA_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

将 `your-api-key-here` 替换为您从 [dashboard.exa.ai/api-keys](https://dashboard.exa.ai/api-keys) 获取的实际 Exa API 密钥。

### 3. 重启 Claude Desktop

为了让更改生效：

1. 完全退出 Claude Desktop（不仅仅是关闭窗口）
2. 再次启动 Claude Desktop
3. 查找 🔌 图标以验证 Exa 服务器是否已连接

## 使用 🎯

配置完成后，您可以要求 Claude 执行网络搜索。以下是一些示例提示：

```
Can you search for recent developments in quantum computing?
```

```
Search for and summarize the latest news about artificial intelligence startups in new york.
```

```
Find and analyze recent research papers about climate change solutions.
```

```
Search for today's breaking news about tech.
```

```
Search for the top 10 AI research papers from 2023, and only use live crawling as a fallback.
```

```
Search for electric vehicles and return 3 results, always using live crawling.
```

服务器将执行以下操作：

1. 处理搜索请求
2. 以最优设置查询 Exa API（包括实时爬取）
3. 将格式化后的结果返回给 Claude
4. 缓存搜索以便将来参考

## 功能 ✨

* **简化网页搜索工具**：仅通过一个查询参数即可让 Claude 搜索网络
* **可自定义的搜索参数**：控制结果数量和实时爬取策略
* **自动实时爬取**：根据指定策略使用实时爬取
* **预设最佳参数**：为结果数量和字符限制使用最佳默认值
* **搜索缓存**：保存最近的搜索作为参考资料
* **错误处理**：优雅地处理 API 错误和速率限制
* **类型安全**：完全使用 TypeScript 实现，并使用 Zod 验证
* **MCP 合规性**：完全实现最新的 MCP 协议规范

## 使用 MCP Inspector 测试 🔍

您可以直接使用 MCP Inspector 测试服务器：

```bash
npx @modelcontextprotocol/inspector node ./build/index.js
```

这将打开一个交互界面，您可以在其中探索服务器的功能、执行搜索查询并查看缓存的搜索结果。

## 故障排除 🔧

### 常见问题

1. **找不到服务器**
   * 确认 npm 链接已正确设置
   * 检查 Claude Desktop 配置语法
   * 确保 Node.js 已正确安装

2. **API 密钥问题**
   * 确认您的 EXA_API_KEY 是有效的
   * 检查 EXA_API_KEY 是否已在 Claude Desktop 配置中正确设置
   * 确认 API 密钥周围没有空格或引号

3. **连接问题**
   * 完全重启 Claude Desktop
   * 检查 Claude Desktop 日志：
   
```bash
   # macOS
   tail -n 20 -f ~/Library/Logs/Claude/mcp*.log
   
   # Windows
   type "%APPDATA%\Claude\logs\mcp*.log"
```

### 获取帮助

如果您遇到问题，请查阅 [MCP 文档](https://modelcontextprotocol.io) 或访问 [GitHub 讨论](https://github.com/orgs/modelcontextprotocol/discussions) 寻求社区支持。

## 致谢 🙏

* [Exa AI](https://exa.ai) 提供了强大的搜索 API
* [Model Context Protocol](https://modelcontextprotocol.io) 提供了 MCP 规范
* [Anthropic](https://anthropic.com) 提供了 Claude Desktop

**官方网站：** [https://github.com/exa-labs/exa-mcp-server](https://github.com/exa-labs/exa-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`
- 标签：`search`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`exa-mcp-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/exa-labs-exa.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
