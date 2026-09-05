---
title: "Git MCP协议服务器"
description: "一种模型上下文协议服务器，使大型语言模型能够通过强大的API与Git仓库进行交互，支持仓库初始化、克隆、文件暂存、提交和分支管理等操作。"
---

# Git MCP协议服务器

一种模型上下文协议服务器，使大型语言模型能够通过强大的API与Git仓库进行交互，支持仓库初始化、克隆、文件暂存、提交和分支管理等操作。

# GIT MCP 服务器

[![TypeScript](/mcp-assets/7c898618a7d157909abc6db18bdcc682.svg)](https://www.typescriptlang.org/)
[![模型上下文协议](/mcp-assets/31793c78ad966d98b7d3c0c31f29c13a.svg)](https://modelcontextprotocol.io/)
[![版本](/mcp-assets/34eb066f8612fa3d28e2f417de70ab01.svg)]()
[![许可证](/mcp-assets/fa73b4786cfc281bb30f39f895ada091.svg)](https://opensource.org/licenses/Apache-2.0)
[![状态](/mcp-assets/bb344818c4ef265bcc66e763f085f8e0.svg)]()
[![GitHub](/mcp-assets/97f0b3c39c1612d1f7c230ae94ac44a3.svg)](https://github.com/cyanheads/git-mcp-server)

一个模型上下文协议 (MCP) 服务器，提供了与 Git 仓库交互的工具。该服务器允许 AI 助手和 LLM 代理通过标准化接口管理仓库、分支、提交和文件，而无需直接访问文件系统或命令行。它将 Git 操作暴露为 MCP 资源和工具，利用 `simple-git` 库实现核心功能，同时保持适当的安全边界。

## 目录

- [概述](#概述)
  - [架构与组件](#架构--组件)
- [特性](#特性)
  - [资源访问](#资源访问)
  - [Git 操作](#git-操作)
- [安装](#安装)
  - [先决条件](#先决条件)
  - [从 NPM 安装](#从-npm-安装)
  - [从源码安装](#从源码安装)
- [使用](#使用)
  - [运行服务器](#运行服务器)
  - [与 Claude 集成](#与-claude-集成)
  - [与其他 MCP 客户端集成](#与其他-mcp-客户端集成)
- [项目结构](#项目结构)
- [工具](#工具)
  - [仓库操作](#仓库操作)
  - [分支操作](#分支操作)
  - [工作目录操作](#工作目录操作)
  - [远程操作](#远程操作)
  - [高级操作](#高级操作)
- [资源](#资源)
  - [仓库资源](#仓库资源)
- [开发](#开发)
  - [构建和测试](#构建和测试)
- [许可证](#许可证)

## 概述

主要功能：

- **仓库管理**：初始化、克隆和检查仓库状态
- **分支操作**：创建、列出、切换、删除和合并分支
- **工作目录**：暂存文件、提交更改、创建差异
- **远程操作**：添加远程、获取、拉取、推送
- **高级 Git 命令**：管理标签、存储更改、挑选提交、变基

### 架构与组件

核心系统架构：

点击展开 Mermaid 图表

```mermaid
flowchart TB
    subgraph API["API Layer"]
        direction LR
        MCP["MCP Protocol"]
        Val["Validation (Zod)"]

        MCP --> Val
    end

    subgraph Core["Core Services"]
        direction LR
        GitService["Git Service (simple-git)"]
        ErrorService["Error Service"]

        GitService  ErrorService
    end

    subgraph Resources["Resource Layer"]
        direction LR
        Repo["Repository Resources"]
        Diff["Diff Resources"]
        File["File Resources"]
        History["History Resources"]

        Repo  Diff
        Repo  File
        Repo  History
    end

    subgraph Tools["Tool Layer"]
        direction LR
        RepoTools["Repository Tools"]
        BranchTools["Branch Tools"]
        WorkdirTools["Working Directory Tools"]
        RemoteTools["Remote Tools"]
        AdvancedTools["Advanced Tools"]

        RepoTools  BranchTools
        BranchTools  WorkdirTools
        WorkdirTools  RemoteTools
        RemoteTools  AdvancedTools
    end

    Val --> GitService
    GitService --> Resources
    GitService --> Tools

    classDef layer fill:#2d3748,stroke:#4299e1,stroke-width:3px,rx:5,color:#fff
    classDef component fill:#1a202c,stroke:#a0aec0,stroke-width:2px,rx:3,color:#fff
    classDef api fill:#3182ce,stroke:#90cdf4,stroke-width:2px,rx:3,color:#fff
    classDef core fill:#319795,stroke:#81e6d9,stroke-width:2px,rx:3,color:#fff
    classDef resource fill:#2f855a,stroke:#9ae6b4,stroke-width:2px,rx:3,color:#fff
    classDef tool fill:#805ad5,stroke:#d6bcfa,stroke-width:2px,rx:3,color:#fff

    class API,Core,Resources,Tools layer
    class MCP,Val api
    class GitService,ErrorService core
    class Repo,Diff,File,History resource
    class RepoTools,BranchTools,WorkdirTools,RemoteTools,AdvancedTools tool
```

核心组件：

- **MCP 服务器 (`server.ts`)**: 使用 `@modelcontextprotocol/sdk` 创建一个暴露资源和工具的服务器。
- **Git 服务 (`services/git-service.ts`)**: 在 `simple-git` 库之上提供了一个抽象层，为 Git 操作提供了清晰的接口。
- **资源 (`resources/`)**: 通过 MCP 资源以一致的 URI 模板形式暴露 Git 数据（如状态、日志、文件内容）。
- **工具 (`tools/`)**: 通过定义良好的输入模式（使用 Zod 进行验证）的 MCP 工具暴露 Git 操作（如提交、推送、拉取）。
- **错误处理 (`services/error-service.ts`)**: 为 Git 和 MCP 操作提供标准化的错误处理和报告。
- **入口点 (`index.ts`)**: 初始化并启动服务器，将其连接到标准 I/O 传输。

## 功能

### 资源访问

通过 MCP 资源暴露 Git 仓库信息：

- **仓库信息**：访问基本的 Git 仓库信息，包括当前分支、状态和引用详情
- **仓库分支**：列出仓库中的所有分支，并标明当前分支
- **仓库远程**：列出所有配置的远程仓库及其 URL
- **仓库标签**：列出仓库中的所有标签及其引用
- **文件内容**：在给定的 Git 引用下访问特定文件的内容
- **目录列表**：查看特定路径和引用下的文件和目录列表
- **差异**：获取不同引用之间、未暂存更改或已暂存更改之间的差异
- **提交历史**：查看包含作者、日期和消息信息的详细提交日志
- **文件归责**：查看逐行归属，显示最后一次修改每行的提交
- **提交详情**：访问特定提交的详细信息，包括差异更改

### Git 操作

通过 MCP 工具执行 Git 命令：

- **仓库操作**：初始化仓库、从远程克隆、检查仓库状态
- **分支操作**：创建分支、列出分支、切换分支、删除分支、合并
- **工作目录操作**：暂存文件、取消暂存文件、提交更改、创建差异
- **远程操作**：添加远程、列出远程、抓取、拉取、推送
- **高级操作**：管理标签、存储更改、挑选提交、变基分支、重置、清理

## 安装

### 先决条件

- Node.js 16 或更高版本
- 已安装并可在 PATH 中使用的 Git

### 从 NPM 安装

```bash
npm install -g @cyanheads/git-mcp-server
```

### 从源代码安装

```bash
git clone https://github.com/cyanheads/git-mcp-server.git
cd git-mcp-server
npm install
npm run build
```

## 使用

### 运行服务器

如果通过 NPM 全局安装：

```bash
git-mcp-server
```

如果从源代码运行：

```bash
node build/index.js
```

该服务器通过标准输入/输出使用模型上下文协议进行通信，使其与任何 MCP 客户端兼容。

### 与 Claude 集成

将以下内容添加到您的 Claude 配置文件中（例如，`cline_mcp_settings.json` 或 `claude_desktop_config.json`）：

```json
{
  "mcpServers": {
    "git": {
      "command": "git-mcp-server", // Or the full path to build/index.js if not installed globally
      "args": [],
      "env": {},
      "disabled": false,
      "autoApprove": [] // Configure auto-approval rules if desired
    }
  }
}
```

### 与其他 MCP 客户端集成

使用 MCP 检查器测试服务器：

```bash
# If installed globally
npx @modelcontextprotocol/inspector git-mcp-server

# If running from source
npx @modelcontextprotocol/inspector build/index.js
```

## 项目结构

代码库遵循模块化结构：

```
git-mcp-server/
├── src/
│   ├── index.ts           # Entry point: Initializes and starts the server
│   ├── server.ts          # Core MCP server implementation and setup
│   ├── resources/         # MCP Resource implementations
│   │   ├── descriptors.ts # Resource URI templates and descriptions
│   │   ├── diff.ts        # Diff-related resources (staged, unstaged, commit)
│   │   ├── file.ts        # File content and directory listing resources
│   │   ├── history.ts     # Commit history and blame resources
│   │   ├── index.ts       # Aggregates and registers all resources
│   │   └── repository.ts  # Repository info, branches, remotes, tags resources
│   ├── services/          # Core logic and external integrations
│   │   ├── error-service.ts # Centralized error handling utilities
│   │   └── git-service.ts   # Abstraction layer for simple-git operations
│   ├── tools/             # MCP Tool implementations
│   │   ├── advanced.ts    # Advanced Git tools (tag, stash, cherry-pick, rebase, log, show)
│   │   ├── branch.ts      # Branch management tools (list, create, checkout, delete, merge)
│   │   ├── index.ts       # Aggregates and registers all tools
│   │   ├── remote.ts      # Remote interaction tools (add, list, fetch, pull, push)
│   │   ├── repository.ts  # Repository level tools (init, clone, status)
│   │   └── workdir.ts     # Working directory tools (add, reset, commit, diff, reset-commit, clean)
│   ├── types/             # TypeScript type definitions
│   │   └── git.ts         # Custom types related to Git operations
│   └── utils/             # Shared utility functions
│       ├── global-settings.ts # Manages global working directory setting
│       └── validation.ts  # Input validation schemas (Zod) and helpers
├── build/                 # Compiled JavaScript output
├── docs/                  # Documentation files
├── logs/                  # Log files (if any)
├── scripts/               # Helper scripts for development (e.g., clean, tree)
├── .env.example           # Example environment variables
├── .gitignore             # Git ignore rules
├── LICENSE                # Project license file
├── package.json           # Project metadata and dependencies
├── package-lock.json      # Lockfile for dependencies
├── README.md              # This file
└── tsconfig.json          # TypeScript compiler configuration
```

## 工具

Git MCP 服务器提供了一整套用于 Git 操作的工具：

### 仓库操作

| 工具         | 描述                                                                                      |
| ------------ | ----------------------------------------------------------------------------------------- |
| `git_init`   | 在指定路径初始化一个新的 Git 仓库，支持创建裸仓库选项。                                 |
| `git_clone`  | 从远程 URL 克隆一个 Git 仓库到本地路径，支持分支和深度选项。                             |
| `git_status` | 获取 Git 仓库当前状态，包括工作目录和暂存区的更改。                                      |

### 分支操作

| 工具                | 描述                                                                                    |
| ------------------- | --------------------------------------------------------------------------------------- |
| `git_branch_list`   | 列出仓库中的所有分支，支持包含远程分支的选项。                                          |
| `git_branch_create` | 创建新分支，支持指定起始点和自动切换选项。                                               |
| `git_checkout`      | 切换分支、标签或提交，并支持在切换时创建新分支的选项。                                  |
| `git_branch_delete` | 删除分支，支持强制删除未合并的分支选项。                                                |
| `git_merge`         | 将一个分支合并到当前分支，支持自定义提交信息和合并策略。                                |

### 工作目录操作

| 工具                | 描述                                                                                     |
| ------------------- | ---------------------------------------------------------------------------------------- |
| `git_add`           | 将文件添加到暂存区，支持单独文件或整个目录。                                             |
| `git_reset`         | 从暂存区取消暂存文件，支持特定文件或所有暂存更改的选项。                                  |
| `git_commit`        | 提交暂存更改，支持自定义提交信息、作者信息和修改选项。                                    |
| `git_diff_unstaged` | 获取工作目录中所有未暂存更改的差异，支持特定文件的选项。                                   |
| `git_diff_staged`   | 获取索引中所有已暂存更改的差异，支持特定文件的选项。                                       |
| `git_reset_commit`  | 将仓库重置到特定引用，支持硬重置、软重置或混合模式选项。                                 |
| `git_clean`         | 从工作树中移除未跟踪的文件，支持目录和强制清理选项。                                     |

### 远程操作

| 工具              | 描述                                                                                  |
| ----------------- | -------------------------------------------------------------------------------------------- |
| `git_remote_add`  | 使用名称和 URL 添加一个新的远程仓库。                                             |
| `git_remote_list` | 列出所有配置的远程仓库及其 URL。                                      |
| `git_fetch`       | 从远程仓库获取更新，可指定特定分支。                   |
| `git_pull`        | 从远程仓库拉取更改，可以选择变基策略。                      |
| `git_push`        | 将本地更改推送到远程仓库，可选择强制推送和上游跟踪选项。 |

### 高级操作

| 工具               | 描述                                                                               |
| ------------------ | ----------------------------------------------------------------------------------------- |
| `git_tag_create`   | 创建新标签，支持带有消息的注释标签。                           |
| `git_tag_list`     | 列出仓库中的所有标签及其引用。                                    |
| `git_stash_create` | 暂存工作目录中的更改，可选择暂存未跟踪文件并添加描述。 |
| `git_stash_list`   | 列出仓库中所有的暂存项及其描述。                               |
| `git_stash_apply`  | 应用一个暂存更改而不从暂存列表中移除它。                           |
| `git_stash_pop`    | 应用一个暂存更改并从暂存列表中移除它。                                 |
| `git_cherry_pick`  | 将特定提交的更改应用到当前分支。                                |
| `git_rebase`       | 将当前分支变基到另一个分支，支持交互模式选项。              |
| `git_log`          | 获取提交历史记录，输出格式和深度可自定义。                             |
| `git_show`         | 显示特定提交的详细信息，包括差异变更。                 |

## 资源

Git MCP 服务器通过标准的 MCP 资源公开 Git 数据：

### 仓库资源

请注意，原文档末尾部分关于“Repository Resources”的具体内容没有提供，因此这部分保持原样。如果有更多具体信息需要翻译，请补充提供。

| 资源                                                    | 描述                                                                              |
| ----------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `git://repo/{repoPath}/info`                                | 包括当前分支、状态和引用详情的基本 Git 仓库信息 |
| `git://repo/{repoPath}/branches`                            | 仓库中所有分支的列表，带当前分支指示器                     |
| `git://repo/{repoPath}/remotes`                             | 所有配置的远程仓库及其 URL 的列表                               |
| `git://repo/{repoPath}/tags`                                | 仓库中所有标签及其引用的列表                                 |
| `git://repo/{repoPath}/file/{filePath}?ref={ref}`           | 返回给定 Git 引用处特定文件的内容                          |
| `git://repo/{repoPath}/ls/{dirPath}?ref={ref}`              | 返回特定路径和引用下的文件和目录列表                 |
| `git://repo/{repoPath}/diff/{fromRef}/{toRef}?path={path}`  | 返回两个 Git 引用（提交、分支、标签）之间的差异                      |
| `git://repo/{repoPath}/diff-unstaged?path={path}`           | 返回工作目录中所有未暂存更改的差异                          |
| `git://repo/{repoPath}/diff-staged?path={path}`             | 返回索引中所有已暂存更改的差异                                        |
| `git://repo/{repoPath}/log?maxCount={maxCount}&file={file}` | 返回包含作者、日期和消息详情的提交历史日志                    |
| `git://repo/{repoPath}/blame/{filePath}`                    | 返回逐行归属，显示最后一次修改每行的提交                        |
| `git://repo/{repoPath}/commit/{commitHash}`                 | 返回关于特定提交的详细信息，包括差异更改              |

## 开发

### 构建与测试

```bash
# Build the project
npm run build

# Watch for changes and rebuild automatically
npm run watch

# Test the server locally using the MCP inspector tool
npm run inspector

# Clean build artifacts
npm run clean

# Generate a file tree representation for documentation
npm run tree

# Clean and rebuild the project completely
npm run rebuild
```

## 许可证

Apache License 2.0 - 详见 [LICENSE](https://github.com/cyanheads/git-mcp-server/blob/HEAD/LICENSE) 获取详细信息。

---

使用 Model Context Protocol 构建

**官方网站：** [https://github.com/cyanheads/git-mcp-server](https://github.com/cyanheads/git-mcp-server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`version control`, `developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`@cyanheads/git-mcp-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/cyanheads-git.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
