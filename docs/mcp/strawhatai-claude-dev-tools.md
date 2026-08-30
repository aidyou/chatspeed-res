---
title: "Claude开发者工具"
description: "允许克劳德在您的计算机上执行终端命令并进行文件系统操作，包括基于差异替换的精确代码编辑。"
---

# Claude开发者工具

允许克劳德在您的计算机上执行终端命令并进行文件系统操作，包括基于差异替换的精确代码编辑。

# Claude Desktop Commander MCP

[![npm downloads](/mcp-assets/999dd87726404fdf9913938b754b945e.svg)](https://www.npmjs.com/package/@wonderwhy-er/desktop-commander)
[Smithery](https://smithery.ai/server/@wonderwhy-er/desktop-commander)

简短版本。两个关键点：终端命令和基于差异的文件编辑。

  

这是一个允许 Claude 桌面应用程序在您的计算机上执行长时间运行的终端命令并通过模型上下文协议 (MCP) 管理进程的服务器 + 基于 [MCP 文件系统服务器](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) 构建，以提供额外的搜索和替换文件编辑功能。

## 功能

- 执行带有输出流的终端命令
- 命令超时和后台执行支持
- 进程管理（列出和终止进程）
- 长时间运行命令的会话管理
- 完整的文件系统操作：
  - 读/写文件
  - 创建/列出目录
  - 移动文件/目录
  - 搜索文件
  - 获取文件元数据
  - 代码编辑功能：
    - 对小改动进行手术式的文本替换
    - 对大改动进行全面文件重写
    - 多文件支持
    - 基于模式的替换

## 安装
首先，请确保您已下载并安装了 [Claude 桌面应用程序](https://claude.ai/download)，并且已经安装了 [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)。

### 选项 1：通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@wonderwhy-er/desktop-commander) 自动为 Claude 桌面应用安装 Desktop Commander：

```bash
npx -y @smithery/cli install @wonderwhy-er/desktop-commander --client claude
```

### 选项 2：通过 npx 安装
只需在终端中运行以下命令：
```
npx @wonderwhy-er/desktop-commander setup
```
如果 Claude 正在运行，请重启它

### 选项 3：手动添加到 claude_desktop_config
将此条目添加到您的 `claude_desktop_config.json` 中（在 Mac 上，路径为 ~/Library/Application\ Support/Claude/claude_desktop_config.json）：
```json
{
  "mcpServers": {
    "desktop-commander": {
      "command": "npx",
      "args": [
        "-y",
        "@wonderwhy-er/desktop-commander"
      ]
    }
  }
}
```
如果 Claude 正在运行，请重启它

### 选项 4：本地检出
1. 克隆并构建：
```bash
git clone https://github.com/wonderwhy-er/ClaudeComputerCommander.git
cd ClaudeComputerCommander
npm run setup
```
如果 Claude 正在运行，请重启它

设置命令将：
- 安装依赖项
- 构建服务器
- 配置 Claude 的桌面应用程序
- 如果需要，向 Claude 的配置中添加 MCP 服务器

## 使用方法

服务器提供了这些工具类别：

### 终端工具
- `execute_command`：运行具有可配置超时时间的命令
- `read_output`：从长时间运行的命令获取输出
- `force_terminate`：停止正在运行的命令会话
- `list_sessions`：查看活动的命令会话
- `list_processes`：查看系统进程
- `kill_process`：按 PID 终止进程
- `block_command`/`unblock_command`：管理命令黑名单

### 文件系统工具
- `read_file`/`write_file`：文件操作
- `create_directory`/`list_directory`：目录管理  
- `move_file`：移动/重命名文件
- `search_files`：基于模式的文件搜索
- `get_file_info`：文件元数据

### 编辑工具

- `edit_block`: 应用手术式文本替换（最适合文件大小变化小于20%的情况）
- `write_file`: 完整文件重写（最适合大改动大于20%或`edit_block`失败时使用）

搜索/替换块格式：
```
filepath.ext
>>>>>> REPLACE
```

示例：
```
src/main.js
>>>>>> REPLACE
```

## 处理长时间运行的命令

对于可能需要一段时间才能完成的命令：

1. `execute_command` 在超时后返回初始输出
2. 命令继续在后台运行
3. 使用带有PID的`read_output`获取新的输出
4. 如果需要，使用`force_terminate`来停止命令

## 模型上下文协议集成

此项目扩展了MCP文件系统服务器以实现以下功能：
- Claude Desktop中的本地服务器支持
- 完整的系统命令执行
- 进程管理
- 文件操作
- 通过搜索/替换块进行代码编辑

作为探索Claude MCPs的一部分创建：[https://youtube.com/live/TlbjFDbl5Us](https://youtube.com/live/TlbjFDbl5Us)

## 贡献

如果您觉得这个项目有用，请考虑在GitHub上给它一个⭐星！这有助于其他人发现该项目并鼓励进一步开发。

我们欢迎社区贡献！无论您发现了错误、有功能请求还是想贡献代码，都可以通过以下方式帮助我们：

- **发现了错误？** 在[github.com/wonderwhy-er/ClaudeComputerCommander/issues](https://github.com/wonderwhy-er/ClaudeComputerCommander/issues)中打开一个问题
- **有功能想法？** 在问题部分提交一个功能请求
- **想要贡献代码？** 叉分仓库，创建一个分支，并提交一个拉取请求
- **有问题或讨论？** 在GitHub的讨论标签下开始一个讨论

所有的贡献，无论大小，都非常感谢！

## 许可证

MIT

**官方网站：** [https://github.com/strawhatai/claude-dev-tools](https://github.com/strawhatai/claude-dev-tools)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`files`
- 标签：`os automation`, `file systems`, `developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @wonderwhy-er/desktop-commander`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/strawhatai-claude-dev-tools.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
