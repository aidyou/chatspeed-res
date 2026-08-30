---
title: "SQLReader"
description: "NaturalSQL MCP Server 这是一个基于 Model Context Protocol (MCP) 的自然语言 SQL 查询服务器。 功能特性 - 🧠 自然语言转 SQL 查询 - 🔗 动态数据库连接配置 - 🛡️ SQL 安全检查（阻止危险操作） - 📊 结果数据表格展示 - 🌐 基于 Gradio 的 Web 界面 安装依赖 bash pip install -r requirements.txt 启动方式 方式1：直接启动 bash python app.py 方式2：使用批处理文件（Wind"
---

# SQLReader

NaturalSQL MCP Server 这是一个基于 Model Context Protocol (MCP) 的自然语言 SQL 查询服务器。 功能特性 - 🧠 自然语言转 SQL 查询 - 🔗 动态数据库连接配置 - 🛡️ SQL 安全检查（阻止危险操作） - 📊 结果数据表格展示 - 🌐 基于 Gradio 的 Web 界面 安装依赖 bash pip install -r requirements.txt 启动方式 方式1：直接启动 bash python app.py 方式2：使用批处理文件（Wind

# NaturalSQL MCP Server

这是一个基于 Model Context Protocol (MCP) 的自然语言 SQL 查询服务器。

## 功能特性

- 🧠 自然语言转 SQL 查询
- 🔗 动态数据库连接配置
- 🛡️ SQL 安全检查（阻止危险操作）
- 📊 结果数据表格展示
- 🌐 基于 Gradio 的 Web 界面

## 安装依赖

```bash
pip install -r requirements.txt
```

## 启动方式

### 方式1：直接启动
```bash
python app.py
```

### 方式2：使用批处理文件（Windows）
```bash
start_mcp_server.bat
```

## MCP 配置文件

- `mcp_config.json` - 简单的 MCP 服务器配置
- `mcp_server_config.json` - 详细的 MCP 服务器配置，包含工具定义

## 使用说明

1. **配置数据库连接**
   - 在"数据库配置"标签页中输入 PostgreSQL 连接信息
   - 点击"测试连接"验证连接
   - 点击"更新配置"应用配置并加载数据库架构

2. **执行自然语言查询**
   - 切换到"SQL查询"标签页
   - 输入自然语言查询，例如："查看2023年7月的订单总金额"
   - 点击"执行查询"获取结果

## 安全特性

系统会自动检测并阻止以下危险 SQL 操作：
- DROP
- DELETE  
- TRUNCATE
- UPDATE
- INSERT

## 环境要求

- Python 3.8+
- PostgreSQL 数据库
- OpenAI API 密钥（需在 config.py 中配置）

## 配置 OpenAI API

在 `config.py` 文件中设置您的 OpenAI API 密钥：

```python
openai_api_key = "your-openai-api-key-here"
```

**官方网站：** [https://www.modelscope.cn/studios/xperiamol/SQLReader](https://www.modelscope.cn/studios/xperiamol/SQLReader)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`memory`, `files`
- 标签：`file systems`, `knowledge and memory`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`mcp-remote https://xperiamol-sqlreader.ms.show/gradio_api/mcp/sse --transport sse-only`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/xperiamol-sqlreader.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
