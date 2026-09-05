---
title: "FinDataMCP - 财务数据分析服务器"
description: "一个MCP服务器，它通过与雅虎财经的集成，使克劳德桌面能够访问和分析财务数据。"
---

# FinDataMCP - 财务数据分析服务器

一个MCP服务器，它通过与雅虎财经的集成，使克劳德桌面能够访问和分析财务数据。

# FinDataMCP

## To run:
1. Clone repo

2. Install uv (package manager):
```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
```

3. Navigate to folder:
```bash
   cd FinDataMCP
```

3. Install dependencies:
```bash
   # Create virtual env and activate it
   uv venv
   source .venv/bin/activate

   # Install dependencies
   uv add "mcp[cli]" httpx yfinance
```

4. Check that everything s working by running server:
```bash
   uv run findata.py
```

## Connecting to Claude Desktop

1. Install [Claude Desktop](https://claude.ai/desktop) if you haven t already

2. Edit Claude Desktop configuration file (Claude>settings>developer>edit config):

3. Add the following configuration:
```json
   {
       "mcpServers": {
           "findata": {
               "command": "uv",
               "args": [
                   "--directory",
                   "/ABSOLUTE/PATH/TO/PARENT/FOLDER/FinDataMCP",
                   "run",
                   "findata.py"
               ]
           }
       }
   }
```

4. Restart Claude Desktop

For windows cmds: see https://modelcontextprotocol.io/quickstart/server

**官方网站：** [https://github.com/coreyjwang/FinDataMCP](https://github.com/coreyjwang/FinDataMCP)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`finance`
- 标签：`finance`, `rag systems`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`--directory /ABSOLUTE/PATH/TO/PARENT/FOLDER/FinDataMCP run findata.py`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/coreyjwang-findatamcp.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
