---
title: "Windows命令行MCP服务器"
description: "一个安全的模型上下文协议服务器，允许人工智能模型与Windows命令行功能安全交互，实现系统命令的受控执行、项目创建和系统信息获取。"
---

# Windows命令行MCP服务器

一个安全的模型上下文协议服务器，允许人工智能模型与Windows命令行功能安全交互，实现系统命令的受控执行、项目创建和系统信息获取。

# Windows 命令行 MCP 服务器

一个安全的模型上下文协议 (MCP) 服务器，能够使 AI 模型安全高效地与 Windows 命令行功能进行交互。

![Version](/mcp-assets/6eecfe2b7d4bf3580c8fad0645d077dd.svg)
![License: MIT](/mcp-assets/6d39e47e35bcced1bb707dfa0b1c276c.svg)
[Smithery](https://smithery.ai/server/@alxspiker/Windows-Command-Line-MCP-Server)

## 概述

Windows 命令行 MCP 服务器为 AI 模型和 Windows 系统操作之间提供了一个健壮且安全的桥梁。它允许受控执行命令、项目创建和系统信息检索，同时保持严格的安全协议。

## 主要特性

### 🔒 增强安全性
- 全面的命令白名单
- 严格的输入验证
- 防止破坏性系统操作
- 可配置的安全级别

### 🛠 开发工具支持
- 支持 React、Node.js 和 Python 项目的创建
- 安全的开发环境交互
- 扩展对开发工作流的命令支持

### 🖥 系统交互能力
- 执行 Windows CLI 命令
- 运行 PowerShell 脚本
- 检索系统和网络信息
- 管理进程和服务

## 安装

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@alxspiker/Windows-Command-Line-MCP-Server) 自动安装适用于 Claude Desktop 的 Windows 命令行 MCP 服务器：

```bash
npx -y @smithery/cli install @alxspiker/Windows-Command-Line-MCP-Server --client claude
```

### 先决条件
- Node.js 16 或更高版本
- npm 或 yarn
- Windows 操作系统

### 设置
```bash
git clone https://github.com/alxspiker/Windows-Command-Line-MCP-Server.git
cd Windows-Command-Line-MCP-Server
npm install
npm run build
```

## 使用

### 命令行选项
- 默认模式：使用预定义的安全命令
- `--allow-all`：以扩展模式运行（带有额外的预防措施）
- 可以指定自定义命令列表作为参数

### 项目创建
使用内置的项目创建工具安全地创建新项目：
- 支持的项目类型：React、Node.js、Python
- 项目在沙盒化的 `~/AIProjects` 目录中创建

### 可用工具
1. **execute_command**：运行 Windows CLI 命令
2. **execute_powershell**：执行 PowerShell 脚本
3. **create_project**：安全地创建新的开发项目
4. **list_running_processes**：检索活动的系统进程
5. **get_system_info**：收集系统配置详细信息
6. **get_network_info**：检索网络适配器信息
7. **get_scheduled_tasks**：列出并查询系统任务
8. **get_service_info**：管理和查询 Windows 服务
9. **list_allowed_commands**：列出服务器可以执行的所有命令

## 与 Claude for Desktop 一起使用

要将此服务器与 Claude for Desktop 一起使用：

1. 根据上述设置说明构建服务器
2. 将其添加到您的 `claude_desktop_config.json` 文件中：

```json
{
  "mcpServers": {
    "windows-cmd": {
      "command": "node",
      "args": ["/path/to/dist/index.js"]
    }
  }
}
```

将 `/path/to/dist/index.js` 替换为 `dist` 目录中生成的 `index.js` 文件的绝对路径。

3. 重启 Claude for Desktop
4. 您现在可以通过让 Claude 执行 Windows 系统操作来使用这些工具

## 安全考虑

### 允许的命令
默认情况下，只允许安全的命令：

- 系统信息检索
- 网络配置
- 进程管理
- 开发工具交互

### 被阻止的操作
危险命令总是被阻止，包括：
- 磁盘格式化
- 用户管理
- 系统关机
- 关键注册表修改

## 配置

通过指定允许的命令或使用配置标志来自定义服务器的行为。

### 示例
```bash
# Run with default safe commands
node dist/index.js

# Run with specific allowed commands
node dist/index.js dir echo npm git

# Run in extended mode (use with caution)
node dist/index.js --allow-all
```

## 贡献

1. 分叉仓库
2. 创建你的功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交你的更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 打开一个拉取请求

## 许可证

本项目根据 MIT 许可证发布 - 详情请参阅 [LICENSE](https://github.com/alxspiker/Windows-Command-Line-MCP-Server/blob/HEAD/LICENSE) 文件。

## 致谢

- 受 Model Context Protocol 规范启发
- 以安全性和灵活性为设计理念开发

## 版本历史

- **0.3.0**: 实现了 README 中提到的所有工具（系统信息、网络信息、进程管理、服务信息）
- **0.2.0**: 添加了项目创建，扩展了开发工具
- **0.1.0**: 初始版本，具有基本的命令执行能力

## 支持

对于问题、疑问或建议，请在 GitHub 上 [打开一个 issue](https://github.com/alxspiker/Windows-Command-Line-MCP-Server/issues)。

**官方网站：** [https://github.com/alxspiker/Windows-Command-Line-MCP-Server](https://github.com/alxspiker/Windows-Command-Line-MCP-Server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`os automation`, `developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`node`
- 参数：`/path/to/dist/index.js`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/alxspiker-windows-command-line.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
