---
title: "InsForge"
description: "Insforge MCP 服务器将编码代理转变为全栈构建者，几秒钟内为应用程序添加身份验证、数据库、文件存储、无服务器功能和LLM等后端功能。它是 Insforge 的模型上下文协议服务器。"
---

# InsForge

Insforge MCP 服务器将编码代理转变为全栈构建者，几秒钟内为应用程序添加身份验证、数据库、文件存储、无服务器功能和LLM等后端功能。它是 Insforge 的模型上下文协议服务器。

alt="Insforge Banner">
  

[![MCP Badge](/mcp-assets/ae2b3adc954c277ae2a75d29e41af32b.svg)](https://lobehub.com/mcp/insforge-insforge-mcp)

# Insforge MCP 服务器

InsForge 可以将你的编码代理变成全栈构建者，让它们在几秒钟内为你的应用程序添加后端功能，如身份验证、数据库、文件存储、无服务器函数和大语言模型。

这个仓库是 [Insforge](https://github.com/InsForge/insforge) 的 Model Context Protocol 服务器。

  

## 📖 文档

请访问 [主 Insforge 仓库](https://github.com/InsForge/insforge)获取以下内容：

- 安装和设置说明
- 配置指南
- 可用工具和使用示例
- API 文档
- 贡献指南

## 🚀 快速开始

### 自动安装（推荐）

使用 InsForge 安装程序自动配置客户端的 MCP：

bash
```bash
# Claude Code
npx @insforge/install --client claude-code --env API_KEY=your_api_key --env API_BASE_URL=http://localhost:7130

# Cursor
npx @insforge/install --client cursor --env API_KEY=your_api_key --env API_BASE_URL=http://localhost:7130

# Windsurf
npx @insforge/install --client windsurf --env API_KEY=your_api_key --env API_BASE_URL=http://localhost:7130

# Cline
npx @insforge/install --client cline --env API_KEY=your_api_key --env API_BASE_URL=http://localhost:7130

# Roo Code
npx @insforge/install --client roocode --env API_KEY=your_api_key --env API_BASE_URL=http://localhost:7130
# Trae
npx @insforge/install --client trae --env API_KEY=your_api_key --env API_BASE_URL=http://localhost:7130

# Install dev version for testing
npx @insforge/install --client cursor --env API_KEY=your_api_key --env API_BASE_URL=http://localhost:7130 --dev
```
替换：
- `your_api_key` 为你的 InsForge API 密钥
- `http://localhost:7130` 为你的 InsForge 实例 URL（可选，默认为 localhost:7130）

### 手动安装

如果你更喜欢手动配置 MCP 客户端，请在你的 MCP 设置文件中添加以下内容：

json
```json
{
  "mcpServers": {
    "insforge": {
      "command": "npx",
      "args": [
        "-y",
        "@insforge/mcp@latest"
      ],
      "env": {
        "API_KEY": "your_api_key",
        "API_BASE_URL": "http://localhost:7130"
      }
    }
  }
}
```
详细的设置说明，请参阅 [Insforge 文档](https://docs.insforge.dev)。

## 📄 许可证

Apache License 2.0 - 详情请参见 [LICENSE](https://github.com/InsForge/insforge-mcp/blob/HEAD/LICENSE) 文件。

---

属于 [Insforge](https://github.com/InsForge/insforge) 项目的一部分。

**官方网站：** [https://github.com/InsForge/insforge-mcp](https://github.com/InsForge/insforge-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @insforge/mcp@latest`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/tony430-insforge.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
