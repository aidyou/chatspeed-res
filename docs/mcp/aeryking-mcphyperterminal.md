---
title: "MCP超级终端"
description: "MCP超级终端 MCP超级终端 是一款专为 AI IDE 开发场景设计的终端扩展工具。 它解决了 AI IDE 在调用外部工具时的不足，支持执行命令、Git 操作、自定义命令，几乎可以运行任何终端脚本。 目前支持 macOS 和 Linux 用户。 --- ✨ 特性 - 🔧 命令执行：在 IDE 内部直接运行终端命令 - 🌀 Git 集成：支持常见 Git 操作（提交、拉取、推送等） - ⚙️ 自定义命令：自由配置快捷命令，满足个性化需求 - 📜 脚本执行：可运行任何 Shell / Bash 脚本 - 🖥️ 跨平"
---

# MCP超级终端

MCP超级终端 MCP超级终端 是一款专为 AI IDE 开发场景设计的终端扩展工具。 它解决了 AI IDE 在调用外部工具时的不足，支持执行命令、Git 操作、自定义命令，几乎可以运行任何终端脚本。 目前支持 macOS 和 Linux 用户。 --- ✨ 特性 - 🔧 命令执行：在 IDE 内部直接运行终端命令 - 🌀 Git 集成：支持常见 Git 操作（提交、拉取、推送等） - ⚙️ 自定义命令：自由配置快捷命令，满足个性化需求 - 📜 脚本执行：可运行任何 Shell / Bash 脚本 - 🖥️ 跨平

# MCP超级终端

**MCP超级终端** 是一款专为 AI IDE 开发场景设计的终端扩展工具。  
它解决了 AI IDE 在调用外部工具时的不足，支持执行命令、Git 操作、自定义命令，几乎可以运行任何终端脚本。  
目前支持 **macOS** 和 **Linux** 用户。

---

## ✨ 特性

- 🔧 **命令执行**：在 IDE 内部直接运行终端命令  
- 🌀 **Git 集成**：支持常见 Git 操作（提交、拉取、推送等）  
- ⚙️ **自定义命令**：自由配置快捷命令，满足个性化需求  
- 📜 **脚本执行**：可运行任何 Shell / Bash 脚本  
- 🖥️ **跨平台**：支持 macOS 和 Linux  

---

## 🚀 使用场景

- AI IDE 开发过程中快速调用外部工具  
- 在不离开编辑器的情况下执行 Git 工作流  
- 自动化执行项目脚本（构建、测试、部署）  
- 替代 IDE 内置但受限的终端调用能力  

---

## ⚙️ 配置 MCP 服务

在 IDE 的配置文件中加入以下内容，即可启用 **MCP超级终端**：

```json
{
  "mcpServers": {
    "MCPHyperTerminal": {
      "timeout": 10000,
      "type": "stdio",
      "command": "npx",
      "args": [
        "-y",
        "@mcpshell/command"
      ]
    }
  }
}
```

**官方网站：** [https://www.npmjs.com/package/@mcpshell/command](https://www.npmjs.com/package/@mcpshell/command)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`files`
- 标签：`developer tools`, `file systems`, `超级终端`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @mcpshell/command`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/aeryking-mcphyperterminal.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
