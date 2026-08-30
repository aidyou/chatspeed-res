---
title: "滴答-MCP"
description: "一个用于TickTick的MCP服务器，可以通过Claude和其他MCP客户端直接与您的TickTick任务管理系统进行交互。"
---

# 滴答-MCP

一个用于TickTick的MCP服务器，可以通过Claude和其他MCP客户端直接与您的TickTick任务管理系统进行交互。

# TickTick MCP 服务器

一个 [模型上下文协议 (MCP)](https://modelcontextprotocol.io/) 服务器，用于通过 Claude 和其他 MCP 客户端直接与您的 TickTick 任务管理系统进行交互。

## 功能

- 📋 查看所有 TickTick 项目和任务
- ✏️ 通过自然语言创建新项目和任务
- 🔄 更新现有任务详情（标题、内容、日期、优先级）
- ✅ 将任务标记为完成
- 🗑️ 删除任务和项目
- 🔄 与 TickTick 的开放 API 全面集成
- 🔌 与 Claude 和其他 MCP 客户端无缝集成

## 前提条件

- Python 3.10 或更高版本
- [uv](https://github.com/astral-sh/uv) - 快速的 Python 包安装器和解析器
- 拥有 API 访问权限的 TickTick 账户
- TickTick API 凭据（客户端 ID、客户端密钥、访问令牌）

## 安装

1. **克隆此仓库**：
```bash
   git clone https://github.com/parkjs814/ticktick-mcp.git
   cd ticktick-mcp
```

2. **使用 uv 安装**：
```bash
   # 如果你还没有安装 uv，先安装它
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # 创建虚拟环境
   uv venv

   # 激活虚拟环境
   # 在 macOS/Linux 上：
   source .venv/bin/activate
   # 在 Windows 上：
   .venv\Scripts\activate

   # 安装包
   uv pip install -e .
```

3. **与 TickTick 进行身份验证**：
```bash
   # 运行身份验证流程
   uv run -m ticktick_mcp.cli auth
```

   此操作将：
   - 请求您的 TickTick 客户端 ID 和客户端密钥
   - 打开浏览器窗口让您登录到 TickTick
   - 自动将您的访问令牌保存到 `.env` 文件中

4. **测试配置**：
```bash
   uv run test_server.py
```
   这将验证您的 TickTick 凭据是否正确工作。

## 与 TickTick 进行身份验证

此服务器使用 OAuth2 对 TickTick 进行身份验证。设置过程非常简单：

1. 在 [TickTick 开发者中心](https://developer.ticktick.com/manage) 注册您的应用程序
   - 设置重定向 URI 为 `http://localhost:8000/callback`
   - 记下您的客户端 ID 和客户端密钥

2. 运行身份验证命令：
```bash
   uv run -m ticktick_mcp.cli auth
```

3. 根据提示输入您的客户端 ID 和客户端密钥

4. 浏览器窗口将打开，以便您使用 TickTick 账户授权该应用程序

5. 授权后，您将被重定向回应用程序，并且您的访问令牌将自动保存到 `.env` 文件中

服务器会自动处理令牌刷新，因此除非您撤销访问权限或删除 `.env` 文件，否则无需重新进行身份验证。

## 与桌面版 Claude 一起使用

1. 安装 [Claude for Desktop](https://claude.ai/download)
2. 编辑你的 Claude for Desktop 配置文件：

   **macOS**:
```bash
   nano ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

   **Windows**:
```bash
   notepad %APPDATA%\Claude\claude_desktop_config.json
```

3. 添加 TickTick MCP 服务器配置，使用绝对路径：
```json
   {
      "mcpServers": {
         "ticktick": {
            "command": "
",
            "args": ["run", "--directory", "
", "-m", "ticktick_mcp.cli", "run"]
         }
      }
   }
```

4. 重启 Claude for Desktop

连接成功后，你将在 Claude 中看到带有 🔨 (工具) 图标的 TickTick MCP 服务器工具。

## 可用的 MCP 工具

| 工具 | 描述 | 参数 |
|------|-------------|------------|
| `get_projects` | 列出所有你的 TickTick 项目 | 无 |
| `get_project` | 获取特定项目的详细信息 | `project_id` |
| `get_project_tasks` | 列出项目中的所有任务 | `project_id` |
| `get_task` | 获取特定任务的详细信息 | `project_id`, `task_id` |
| `create_task` | 创建新任务 | `title`, `project_id`, `content` (可选), `start_date` (可选), `due_date` (可选), `priority` (可选) |
| `update_task` | 更新现有任务 | `task_id`, `project_id`, `title` (可选), `content` (可选), `start_date` (可选), `due_date` (可选), `priority` (可选) |
| `complete_task` | 标记任务为完成 | `project_id`, `task_id` |
| `delete_task` | 删除任务 | `project_id`, `task_id` |
| `create_project` | 创建新项目 | `name`, `color` (可选), `view_mode` (可选) |
| `delete_project` | 删除项目 | `project_id` |

## Claude 示例提示

以下是一些连接 TickTick MCP 服务器后可以使用的示例提示：

- "显示我所有的 TickTick 项目"
- "在我的工作项目中创建一个名为 'Finish MCP server documentation' 的高优先级新任务"
- "列出我的个人项目中的所有任务"
- "将任务 'Buy groceries' 标记为完成"
- "创建一个名为 'Vacation Planning' 的蓝色新项目"
- "我的下一个 TickTick 截止日期是什么时候？"

## 开发

### 项目结构

```
ticktick-mcp/
├── .env.template          # Template for environment variables
├── README.md              # Project documentation
├── requirements.txt       # Project dependencies
├── setup.py               # Package setup file
├── test_server.py         # Test script for server configuration
└── ticktick_mcp/          # Main package
    ├── __init__.py        # Package initialization
    ├── authenticate.py    # OAuth authentication utility
    ├── cli.py             # Command-line interface
    └── src/               # Source code
        ├── __init__.py    # Module initialization
        ├── auth.py        # OAuth authentication implementation
        ├── server.py      # MCP server implementation
        └── ticktick_client.py  # TickTick API client
```

### 认证流程

该项目实现了完整的 TickTick OAuth 2.0 流程：

1. **初始设置**：用户提供他们的 TickTick API 客户端 ID 和密钥
2. **浏览器授权**：用户被重定向到 TickTick 以授予访问权限
3. **令牌接收**：本地服务器接收包含授权码的 OAuth 回调
4. **令牌交换**：使用代码交换访问令牌和刷新令牌
5. **令牌存储**：令牌安全地存储在本地 `.env` 文件中
6. **令牌刷新**：客户端在访问令牌过期时自动刷新

这通过编程方式处理整个 OAuth 流程简化了用户体验。

### 贡献

欢迎贡献！请随时提交 Pull Request。

1. Fork 仓库
2. 创建你的特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交你的更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 打开一个 Pull Request

## 许可证

本项目采用 MIT 许可证 - 详情请参见 LICENSE 文件。

**官方网站：** [https://github.com/jacepark12/ticktick-mcp](https://github.com/jacepark12/ticktick-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`productivity`
- 标签：`note taking`, `calendar management`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`<absolute path to uv>`
- 参数：`run --directory <absolute path to ticktick-mcp directory> -m ticktick_mcp.cli run`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/jacepark12-ticktick.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
