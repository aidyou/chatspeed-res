---
title: "个人助手MCP数字生活管理器"
description: "通过与Google日历、Obsidian Vault、Trello的集成以及网页解析功能，实现管理数字生活的统一接口。"
---

# 个人助手MCP数字生活管理器

通过与Google日历、Obsidian Vault、Trello的集成以及网页解析功能，实现管理数字生活的统一接口。

# 个人助理 MCP 服务器

这是一个强大的个人助理服务器，集成了包括 Google 日历、Obsidian Vault、Trello 和网页解析功能在内的多种服务。该服务器基于 FastMCP 构建，为管理您的数字生活提供了统一的接口。

## 功能

- **Google 日历集成**
  - 创建、读取、更新和删除日历事件
  - 列出即将到来的事件

- **Obsidian Vault 管理**
  - 创建、读取、更新和删除笔记
  - 笔记全文搜索
  - 文件夹管理（创建、删除、搜索、列出）

- **Trello 集成**
  - 看板、列表和卡片管理
  - 创建、更新和删除卡片
  - 通过文本查询搜索卡片

- **网页解析**
  - 从任何 URL 中提取并清理 HTML 内容

## 先决条件

- Python 3.10 或更高版本
- Poetry（Python 包管理器）
- Google 日历 API 凭证
- Trello API 凭证（如果使用 Trello 功能）
- Obsidian Vault（如果使用 Obsidian 功能）

## 安装

1. 克隆仓库：
```bash
   git clone https://github.com/yourusername/personal-assistant-mcp.git
   cd personal-assistant-mcp
```

2. 使用 Poetry 安装依赖项：
```bash
   poetry install
```

3. 设置 Google 日历 API：
   - 前往 [Google Cloud Console](https://console.cloud.google.com/)
   - 创建新项目或选择现有项目
   - 启用 Google 日历 API
   - 创建 OAuth 2.0 凭证
   - 下载凭证并将其保存为项目根目录下的 `credentials.json` 文件

4. 设置 Trello API（可选）：
   - 前往 [Trello 开发者门户](https://trello.com/app-key)
   - 获取您的 API 密钥和令牌
   - 将它们添加到环境变量或配置文件中

## 配置

1. 运行初始设置以与 Google 日历进行身份验证：
```bash
   poetry run python main.py
```
   - 这将打开一个浏览器窗口用于 Google 身份验证
   - 按照提示授权应用程序

## 使用

1. 启动服务器：
```bash
   poetry run python main.py
```

2. 服务器将启动并准备好接受兼容 MCP 的客户端连接。

3. 使用任何兼容 MCP 的客户端与服务器交互。服务器提供以下工具：
   - 日历管理
   - Obsidian vault 操作
   - Trello 看板管理
   - 网页解析

## Anthropic Claude Desktop 配置

要将此服务器与 Anthropic Claude Desktop 一起使用，请在您的 Claude Desktop 设置中添加以下配置：

```json
{
   "mcpServers": {
      "personal-assistant": {
         "command": "/path/to/your/venv/bin/python",
         "args": ["/path/to/your/project/main.py"],
         "env": {
                 "GOOGLE_CREDENTIALS_PATH": "/path/to/your/credentials.json",
                 "GOOGLE_TOKEN_PATH": "/path/to/your/token.json",
                 "OBSIDIAN_VAULT_PATH": "/path/to/your/obsidian/vault",
                 "OBSIDIAN_DEFAULT_FOLDER": "your_default_folder",
                 "LOG_PATH": "/path/to/log.txt",
                 "TRELLO_TOKEN": "your_trello_token",
                 "TRELLO_API_KEY": "your_trello_api_key"
         }
      }
   }
}
```

将路径和凭证替换为您实际的值：

- `command`: 指向你的 Python 虚拟环境的 Python 可执行文件的路径
- `args`: 指向你的项目中的 `main.py` 文件的路径
- `GOOGLE_CREDENTIALS_PATH`: 指向你的 Google Calendar 凭据文件的路径
- `GOOGLE_TOKEN_PATH`: 指向你的 Google Calendar 令牌文件的路径
- `OBSIDIAN_VAULT_PATH`: 指向你的 Obsidian 仓库的路径
- `OBSIDIAN_DEFAULT_FOLDER`: 在你的仓库中，新笔记将被创建的默认文件夹的路径
- `TRELLO_TOKEN`: 你的 Trello API 令牌
- `TRELLO_API_KEY`: 你的 Trello API 密钥

## 开发

- 该项目使用 Poetry 进行依赖管理
- 所有工具都在 `main.py` 中注册
- 针对特定服务的实现位于 `services/` 目录下
- 遵循 PEP 8 风格指南编写 Python 代码

## 贡献

1. 分叉仓库
2. 创建你的特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交你的更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到该分支 (`git push origin feature/amazing-feature`)
5. 打开一个 Pull Request

加入我们：

[Telegram](https://t.me/systemlog_ai)
[Blog](https://neuromant.wordpress.com/)

**官方网站：** [https://github.com/lemannrus/personal-assistant-mcp](https://github.com/lemannrus/personal-assistant-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`productivity`
- 标签：`calendar management`, `note taking`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`/path/to/your/venv/bin/python`
- 参数：`/path/to/your/project/main.py`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/lemannrus-personal-assistant.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
