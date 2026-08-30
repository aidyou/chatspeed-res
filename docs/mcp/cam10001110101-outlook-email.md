---
title: "MongoDB Outlook邮件处理工具"
description: "处理来自Outlook的电子邮件时，使用日期过滤，将它们存储在SQLite数据库中，同时为MongoDB生成向量嵌入以实现语义搜索功能。"
---

# MongoDB Outlook邮件处理工具

处理来自Outlook的电子邮件时，使用日期过滤，将它们存储在SQLite数据库中，同时为MongoDB生成向量嵌入以实现语义搜索功能。

# 电子邮件处理 MCP 服务器

此 MCP 服务器提供电子邮件处理功能，并集成了 MongoDB 用于语义搜索，以及 SQLite 用于高效存储和检索。

## 功能

- 从 Outlook 处理具有日期范围过滤的电子邮件
- 在 SQLite 数据库中存储电子邮件并进行适当的连接管理
- 使用 Ollama 生成向量嵌入
- 多邮箱支持
- 支持收件箱、已发送邮件文件夹，可选地支持已删除邮件文件夹

## 即将推出的功能

- 具备语义能力的电子邮件搜索
- 使用 LLM 进行电子邮件摘要
- 自动电子邮件分类
- 可定制的电子邮件报告
- 高级过滤选项
- Outlook 草拟电子邮件回复
- Outlook 规则建议
- 扩展数据库选项，集成 Neo4j 和 ChromaDB

## 前提条件

- Python 3.10 或更高版本
- 本地运行 Ollama（用于嵌入）
- 安装 Microsoft Outlook
- Windows 操作系统（用于 Outlook 集成）
- MongoDB 服务器（用于存储嵌入）

## 安装

1. 安装 uv（如果尚未安装）：
```bash
  pip install uv
```

2. 创建虚拟环境：
```bash
  uv venv .venv
```

3. 激活虚拟环境：  
   
   Windows: 

```
    .venv\Scripts\activate
```

   
    macOS/Linux: 

```python
    source .venv/bin/activate
```

4. 安装依赖项：
```bash
uv pip install -e .
```

5. 安装 fastmcp 包：
```bash
uv pip install fastmcp
```

6. 确保 Ollama 本地运行且带有必需的模型：
```bash
ollama pull nomic-embed-text
```

## 配置

将服务器添加到您的 Claude for Desktop 配置文件中：

- Windows: `%APPDATA%\Claude\claude_desktop_config.json`
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "outlook-email": {
      "command": "C:/Users/username/path/to/mcp-server-outlook-email/.venv/Scripts/python",
      "args": [
        "C:/Users/username/path/to/mcp-server-outlook-email/src/mcp_server.py"
      ],
      "env": {
        "MONGODB_URI": "mongodb://localhost:27017/MCP?authSource=admin",
        "SQLITE_DB_PATH": "C:\\Users\\username\\path\\to\\mcp-server-outlook-email\\data\\emails.db",
        "EMBEDDING_BASE_URL": "http://localhost:11434",
        "EMBEDDING_MODEL": "nomic-embed-text",
        "COLLECTION_NAME": "outlook-emails",
        "PROCESS_DELETED_ITEMS": "false"
      }
    }
  }
}
```

### 跟踪与监控

该服务器设计支持外部跟踪和监控解决方案。MCP 日志实现已被有意移除，以支持一个更强大的独立实施的跟踪方法。

注意：不要尝试重新实现之前的日志系统。未来将提供一个新的跟踪解决方案。

配置字段说明：
- `command`: 您虚拟环境中 Python 可执行文件的完整路径
- `args`: 包含 MCP 服务器脚本完整路径的数组
- `env`: 用于配置的环境变量
  - `MONGODB_URI`: MongoDB 连接字符串
  - `SQLITE_DB_PATH`: SQLite 数据库文件的绝对路径
  - `EMBEDDING_BASE_URL`: Ollama 服务器 URL
  - `EMBEDDING_MODEL`: 用于嵌入的模型
  - `LLM_MODEL`: 用于 LLM 操作的模型
  - `COLLECTION_NAME`: 要使用的 MongoDB 集合名称（必需）
  - `PROCESS_DELETED_ITEMS`: 是否处理来自已删除邮件文件夹的邮件（可选，默认为 "false"）
- `disabled`: 服务器是否被禁用（应设置为 false）
- `alwaysAllow`: 不需要用户确认的工具数组
- `autoApprove`: 可自动批准的工具数组

将路径替换为您系统中的实际路径。请注意，`env` 部分中的 Windows 路径应使用双反斜杠。

## 可用工具

### 1. process_emails
处理指定日期范围内的电子邮件：
```python
{
  "start_date": "2024-01-01",    # ISO format date (YYYY-MM-DD)
  "end_date": "2024-02-15",      # ISO format date (YYYY-MM-DD)
  "mailboxes": ["All"]           # List of mailbox names or ["All"] for all mailboxes
}
```

该工具将执行以下操作：
1. 连接到指定的 Outlook 邮箱
2. 从收件箱和已发送项目文件夹（如果启用，则还包括已删除项目）中检索电子邮件
3. 将电子邮件存储在 SQLite 数据库中
4. 使用 Ollama 生成嵌入
5. 将嵌入存储在 MongoDB 中以进行语义搜索

## Claude 中的示例用法

```
"Process emails from February 1st to February 17th from all mailboxes"
```

## 架构

服务器使用混合搜索方法：
1. SQLite 数据库用于：
   - 主要电子邮件存储
   - 全文搜索功能
   - 处理状态跟踪
   - 高效过滤
   - 如果目录不存在则自动创建
   - 正确关闭连接以防止数据库锁定

2. MongoDB 用于：
   - 向量嵌入存储
   - 语义相似性搜索
   - 元数据过滤
   - 高效检索
   - 使用后正确关闭连接

## 错误处理

服务器为常见问题提供了详细的错误消息：
- 无效的日期格式
- 与 Outlook 的连接问题
- MongoDB 错误
- 带有重试逻辑的嵌入生成失败
- SQLite 存储错误
- 自动重试的 Ollama 服务器连接问题

## 资源管理

服务器实施了适当的资源管理以防止问题：
- 在服务器运行期间保持数据库连接（SQLite 和 MongoDB）打开，以防止“无法对已关闭的数据库进行操作”错误
- 仅在服务器关闭时通过 atexit 处理程序关闭连接
- 使用析构函数和上下文管理器作为后备，确保对象被垃圾回收时关闭连接
- 连接管理旨在平衡资源使用与操作可靠性
- 对外部服务（如 Ollama）的强大重试逻辑以处理临时连接问题

## 安全注意事项

- 服务器仅处理指定邮箱中的电子邮件
- 所有数据都存储在本地（SQLite）和 MongoDB 中
- 除了调用本地 Ollama 服务器外，没有其他外部 API 调用
- 需要用户明确批准才能处理电子邮件
- 通过 MCP 接口不暴露敏感电子邮件数据

## 调试

如果您遇到问题：
1. 验证电子邮件是否成功处理（检查 process_emails 响应）
2. 确保 Ollama 服务器正在运行以生成嵌入
3. 检查 SQLite 数据库是否可访问
4. 确认 MongoDB 连接正常工作

**官方网站：** [https://github.com/Cam10001110101/mcp-server-outlook-email](https://github.com/Cam10001110101/mcp-server-outlook-email)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`communication`
- 标签：`databases`, `communication`, `knowledge and memory`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`C:/Users/username/path/to/mcp-server-outlook-email/.venv/Scripts/python`
- 参数：`C:/Users/username/path/to/mcp-server-outlook-email/src/mcp_server.py`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/cam10001110101-outlook-email.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
