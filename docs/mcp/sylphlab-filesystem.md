---
title: "Filesystem-MCP 服务器（文件系统 MCP）"
description: "一个基于 TypeScript 的 MCP 服务器，实现了简单的笔记系统，允许用户通过 URI 和工具创建、访问文本笔记并生成摘要。"
---

# Filesystem-MCP 服务器（文件系统 MCP）

一个基于 TypeScript 的 MCP 服务器，实现了简单的笔记系统，允许用户通过 URI 和工具创建、访问文本笔记并生成摘要。

# 文件系统 MCP 服务器 (@sylphlab/filesystem-mcp)

[![npm 版本](/mcp-assets/0d89c2ac0364202e96bf81ee71923631.svg)](https://badge.fury.io/js/%40sylphlab%2Ffilesystem-mcp)
[![Docker 拉取次数](/mcp-assets/dfdae949fb9b905b5571a7a6d41a6870.svg)](https://hub.docker.com/r/sylphlab/filesystem-mcp)

  

**为您的 AI 代理（如 Cline/Claude）提供安全、高效且节省令牌的项目文件访问权限。** 这个 Node.js 服务器实现了 [模型上下文协议 (MCP)](https://docs.modelcontextprotocol.com/)，提供了一组强大的文件系统工具，并在定义的项目根目录内安全运行。

## 安装

有几种方法可以使用文件系统 MCP 服务器：

**1. 推荐：通过 MCP 主机配置使用 `npx`（或 `bunx`）**

最简单的方法是通过 `npx` 或 `bunx`，直接在您的 MCP 主机环境（例如 Roo/Cline 的 `mcp_settings.json`）中进行配置。这确保您始终使用 npm 上的最新版本，而无需本地安装或 Docker。

_示例 (`npx`)：_

```json
{
  "mcpServers": {
    "filesystem-mcp": {
      "command": "npx",
      "args": ["@sylphlab/filesystem-mcp"],
      "name": "Filesystem (npx)"
    }
  }
}
```

_示例 (`bunx`)：_

```json
{
  "mcpServers": {
    "filesystem-mcp": {
      "command": "bunx",
      "args": ["@sylphlab/filesystem-mcp"],
      "name": "Filesystem (bunx)"
    }
  }
}
```

**重要提示：** 服务器使用其自己的当前工作目录 (`cwd`) 作为项目根目录。请确保您的 MCP 主机（例如 Cline/VSCode）配置为以您的活动项目的根目录作为 `cwd` 启动命令。

**2. Docker**

对于容器化环境，请使用官方 Docker 镜像。

_MCP 主机配置示例：_

```json
{
  "mcpServers": {
    "filesystem-mcp": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-v",
        "/path/to/your/project:/app", // Mount your project to /app
        "sylphlab/filesystem-mcp:latest"
      ],
      "name": "Filesystem (Docker)"
    }
  }
}
```

**请记得将 `/path/to/your/project` 替换为正确的绝对路径。**

**3. 本地构建（用于开发）**

1. 克隆：`git clone https://github.com/sylphlab/filesystem-mcp.git`
2. 安装：`cd filesystem-mcp && pnpm install` （现在使用 pnpm）
3. 构建：`pnpm run build`
4. 配置 MCP 主机：
```json
    {
      "mcpServers": {
        "filesystem-mcp": {
          "command": "node",
          "args": ["/path/to/cloned/repo/filesystem-mcp/dist/index.js"], // 更新后的构建目录
          "name": "Filesystem (本地构建)"
        }
      }
    }
```
    **注意：** 从您希望作为项目根目录的目录启动 `node` 命令。

## 快速开始

一旦在您的 MCP 主机中配置了服务器（参见安装部分），您的 AI 代理就可以立即开始使用文件系统工具。

_示例代理交互（概念性）：_

```
Agent: 
         filesystem-mcp
         read_content
         
{"paths": ["src/index.ts"]}

       

Server Response: (Content of src/index.ts)
```

## 为什么选择这个项目？

- **🛡️ 安全且便捷的项目根目录聚焦:** 操作仅限于项目根目录（启动时的 `cwd`）。
- **⚡ 优化与整合的工具:** 批量操作减少了AI服务器往返次数，节省了令牌和延迟。每个批次中的每个项目都有可靠的结果。
- **🚀 易于集成:** 通过 `npx`/`bunx` 快速设置。
- **🐳 容器化选项:** 可作为Docker镜像使用。
- **🔧 全面的功能:** 涵盖广泛的文件系统任务。
- **✅ 强大的验证:** 使用Zod模式进行参数验证。

## 性能优势

_(占位符：在此处添加基准测试结果和比较，展示相对于其他方法如单个shell命令的优势。)_

- **批量操作:** 与单一操作相比显著减少了开销。
- **直接API使用:** 比为每个命令生成shell进程更高效。
- _(在有具体基准数据时添加)_

## 功能

该服务器为您的AI代理配备了强大而高效的文件系统工具包：

- 📁 **浏览与检查 (`list_files`, `stat_items`):** 列出文件/目录（递归、统计），获取多个项目的详细状态。
- 📄 **读取与写入内容 (`read_content`, `write_content`):** 读取/写入/追加多个文件，创建父目录。
- ✏️ **精确编辑与搜索 (`edit_file`, `search_files`, `replace_content`):** 在多个文件中执行外科手术式的编辑（插入、替换、删除），保留缩进并输出差异；带上下文的正则表达式搜索；多文件搜索/替换。
- 🏗️ **管理目录 (`create_directories`):** 创建多个目录包括中间的父目录。
- 🗑️ **安全删除 (`delete_items`):** 递归删除多个文件/目录。
- ↔️ **移动与复制 (`move_items`, `copy_items`):** 移动/重命名/复制多个文件/目录。
- 🔒 **控制权限 (`chmod_items`, `chown_items`):** 更改多个项目的POSIX权限和所有权。

**主要优势:** 所有接受多个路径/操作的工具都单独处理每个项目，并返回详细的状况报告。

## 设计理念

_(占位符：解释核心设计原则。)_

- **安全第一:** 优先防止访问项目根目录之外的内容。
- **效率:** 最小化AI交互的通信开销和令牌使用。
- **健壮性:** 为批量操作提供详细的成果和错误报告。
- **简洁性:** 通过MCP提供清晰一致的API。
- **标准合规性:** 严格遵守模型上下文协议。

## 与其他解决方案的比较

_(占位符：客观地与其他替代方案进行比较。)_

| 特性/方面          | 文件系统 MCP 服务器 | 单个 Shell 命令（通过代理） | 其他自定义脚本 |
| :---------------------- | :-------------------- | :------------------------------------ | :------------------- |
| **安全性**            | 高（限制为 Root）  | 低（代理需要 shell 访问权限）        | 可变             |
| **效率（令牌）** | 高（批量处理）       | 低（每个操作一条命令）              | 可变             |
| **延迟**             | 低（直接 API）      | 高（Shell 启动开销）           | 可变             |
| **批处理操作**    | 是（大多数工具）      | 否                                    | 可能                |
| **错误报告**     | 详细（每项）   | 基本（stdout/stderr 解析）         | 可变             |
| **设置**               | 简单（npx/Docker）     | 需要安全的 shell 设置           | 自定义               |

## 未来计划

_(占位符：列出即将推出的功能或改进。)_

- 探索文件监控功能。
- 研究对非常大文件的流支持。
- 提高特定操作的性能。
- 为 `list_files` 添加更多高级过滤选项。

## 文档

_(占位符：在文档网站可用时添加链接。)_

完整文档，包括详细的 API 参考和示例，将在以下位置提供：[Link to Docs Site]

## 贡献

欢迎贡献！请在 [GitHub repository](https://github.com/sylphlab/filesystem-mcp) 上打开一个 issue 或提交一个 pull request。

## 许可证

此项目根据 [MIT License](https://github.com/shtse8/filesystem-mcp/blob/HEAD/LICENSE) 发布。

---

## 开发

1. 克隆: `git clone https://github.com/sylphlab/filesystem-mcp.git`
2. 安装: `cd filesystem-mcp && pnpm install`
3. 构建: `pnpm run build` (将 TypeScript 编译到 `dist/`)
4. 监视: `pnpm run dev` (可选，在保存时重新编译)

## 发布（通过 GitHub Actions）

此仓库使用 GitHub Actions (`.github/workflows/publish.yml`) 在向 `main` 分支推送版本标签 (`v*.*.*`) 时自动发布包到 [npm](https://www.npmjs.com/package/@sylphlab/filesystem-mcp) 并构建/推送 Docker 镜像到 [Docker Hub](https://hub.docker.com/r/sylphlab/filesystem-mcp)。需要在 GitHub 仓库设置中配置 `NPM_TOKEN`、`DOCKERHUB_USERNAME` 和 `DOCKERHUB_TOKEN` 密钥。

**官方网站：** [https://github.com/shtse8/filesystem-mcp](https://github.com/shtse8/filesystem-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`files`
- 标签：`note taking`, `file systems`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`@sylphlab/filesystem-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/sylphlab-filesystem.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
