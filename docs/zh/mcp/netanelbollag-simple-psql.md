---
title: "PostgreSQL 连接器"
description: "一个用于构建自定义MCP服务器的模板项目，它 enables 直接访问PostgreSQL数据库，通过模型上下文协议允许执行SQL查询和检索模式信息。 （注：原文中的“enables”在翻译中根据语义调整为更符合中文表达的方式。）"
---

# PostgreSQL 连接器

一个用于构建自定义MCP服务器的模板项目，它 enables 直接访问PostgreSQL数据库，通过模型上下文协议允许执行SQL查询和检索模式信息。 （注：原文中的“enables”在翻译中根据语义调整为更符合中文表达的方式。）

# 简单的 PostgreSQL MCP 服务器

这是一个为那些希望构建自己的 MCP 服务器的人准备的模板项目。我设计它的目的是让它非常简单易懂和易于适应——代码非常直接，并附有 MCP 文档，因此你可以快速上手。

## 什么是 MCP？

*TL;DR - 它是一种为 AI 编写插件的方式*

模型上下文协议（MCP）是 LLM 与外部工具和数据交互的标准方式。简而言之：

- **工具** 允许 LLM 执行命令（如运行数据库查询）
- **资源** 是可以附加到对话中的数据（如将文件附加到提示中）
- **提示** 是生成一致的 LLM 指令的模板

## 功能

这个 PostgreSQL MCP 服务器实现了以下功能：

1. **工具**
   - `execute_query` - 对你的数据库运行 SQL 查询
   - `test_connection` - 验证数据库连接是否正常工作

2. **资源**
   - `db://tables` - 架构中的所有表列表
   - `db://tables/{table_name}` - 特定表的架构信息
   - `db://schema` - 数据库中所有表的完整架构信息

3. **提示**
   - 查询生成模板
   - 分析查询构建器
   - 基于此仓库中的模板

## 前提条件

- Python 3.8+
- [uv](https://github.com/astral-sh/uv) - 现代 Python 包管理器和安装程序
- npx（包含在 Node.js 中）
- 你可以连接的 PostgreSQL 数据库

## 快速设置

1. **创建虚拟环境并安装依赖项：**
```bash
   # 使用 uv 创建虚拟环境
   uv venv
   
   # 激活虚拟环境
   source .venv/bin/activate  # 在 Windows 上: .venv\Scripts\activate
   
   # 安装依赖项
   uv pip install -r requirements.txt
```

2. **使用 MCP Inspector 运行服务器：**
```bash
   # 请替换为您的实际数据库凭据
   npx @modelcontextprotocol/inspector uv --directory . run postgres -e DSN=postgresql://username:password@hostname:port/database -e SCHEMA=public
```

   > 注意：如果您是第一次运行 npx，系统会提示您批准安装。输入 'y' 继续。

   运行此命令后，您将在浏览器中看到 MCP Inspector 界面启动。您应该会看到类似以下的消息：
```
   MCP Inspector 正在 http://localhost:5173 运行
```

   如果浏览器没有自动打开，请将 URL 复制粘贴到您的浏览器中。您应该会看到类似这样的界面：
   
3. **使用 Inspector：**
   - 点击界面上的“连接”按钮（除非左下角的控制台中有错误消息）
   - 探索“工具”、“资源”和“提示”选项卡以查看可用功能
   - 尝试点击列出的命令或输入资源名称以检索资源和提示
   - 该界面允许您测试查询并查看 MCP 服务器如何响应

4. **查阅官方文档**

   官方服务器开发者指南：https://modelcontextprotocol.io/quickstart/server

   关于 Inspector 的更多信息：https://modelcontextprotocol.io/docs/tools/inspector

## 将您的 AI 工具连接到服务器

您可以为您的 AI 助手配置 MCP 服务器，方法是创建一个 MCP 配置文件：

```json
{
   "mcpServers": {
      "postgres": {
         "command": "/path/to/uv",
         "args": [
            "--directory",
            "/path/to/simple-psql-mcp",
            "run",
            "postgres"
         ],
         "env": {
            "DSN": "postgresql://username:password@localhost:5432/my-db",
            "SCHEMA": "public"
         }
      }
   }
}
```

或者，您可以使用附带的脚本生成此配置文件：

```bash
# Make the script executable
chmod +x generate_mcp_config.sh

# Run the configuration generator
./generate_mcp_config.sh
```

当被提示时，输入您的 PostgreSQL DSN 和模式名称。

### 如何使用它

现在，您可以用自然语言向 LLM 提问关于您的数据的问题：
- "我的数据库里有哪些表？"
- "按创建日期显示前 5 名用户"
- "按州统计地址数量"

对于测试，Claude Desktop 原生支持 MCP，并且开箱即用地支持所有功能（工具、资源和提示）。

## 示例数据库（可选）

如果您还没有准备好数据库或遇到连接问题，可以使用包含的示例数据库：

```bash
# Make the script executable
chmod +x example-db/create-db.sh

# Run the database setup script
./example-db/create-db.sh
```

此脚本将创建一个预填充了示例用户和地址表的 PostgreSQL 数据库 Docker 容器。运行后，您可以使用以下方式连接：

```bash
npx @modelcontextprotocol/inspector uv --directory . run postgres -e DSN=postgresql://postgres:postgres@localhost:5432/user_database -e SCHEMA=public
```

## 下一步

要扩展此项目并添加您自己的 MCP 服务器：

1. 在 `/src` 目录下创建一个新目录（例如 `/src/my-new-mcp`）
2. 根据 PostgreSQL 示例实现您的 MCP 服务器
3. 将您的新 MCP 添加到 `pyproject.toml` 中：

```toml
[project.scripts]
postgres = "src.postgres:main"
my-new-mcp = "src.my-new-mcp:main"
```

然后，您可以使用以下命令运行您的新 MCP：

```bash
npx @modelcontextprotocol/inspector uv --directory . run my-new-mcp
```

## 文档

- 包含MCP文档以便于LLM开发
- 基于以下方法：https://modelcontextprotocol.io/tutorials/building-mcp-with-llms

## 安全性

这是一个实验性项目，旨在使开发者能够创建自己的MCP服务器。我尽了最小的努力来确保当你尝试使用它时不会立即出现问题，但请小心——使用这个工具很容易进行SQL注入攻击。服务器会检查查询是否以SELECT开头，但除此之外没有任何保证。总之——除非你是创始人且没有付费客户，否则不要在生产环境中运行。

## 许可证

MIT

**官方网站：** [https://github.com/NetanelBollag/simple-psql-mcp](https://github.com/NetanelBollag/simple-psql-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`databases`, `developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`/path/to/uv`
- 参数：`--directory /path/to/simple-psql-mcp run postgres`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/netanelbollag-simple-psql.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
