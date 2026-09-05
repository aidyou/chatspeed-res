---
title: "CSV表格读取"
description: "\"该getdata工具提供了用于访问 CSV 文件的自然语言界面,并使用语言模型来分析和响应查询.\""
---

# CSV表格读取

"该getdata工具提供了用于访问 CSV 文件的自然语言界面,并使用语言模型来分析和响应查询."

# Xiyan Table MCP Server

这是一个基于 MCP (Model Control Protocol) 的表格数据查询服务器。它允许用户配置本地表格数据，并通过自然语言进行查询。

## 功能特点
- 🌐 使用自然语言分析和查询表格信息
- 🤖 支持通用大语言模型（GPT、Qwen-Max）和 [XiYanTable]
- 🔧 支持从 CSV 文件读取表格内容

## 工具预览
- "get_data 工具提供了一个自然语言接口来访问 CSV 文件，并使用语言模型来分析和响应查询。"

## 快速开始

需要 Python 3.10+ 环境。
你可以通过 pip 安装服务器，它将安装最新版本：

```bash
pip install xiyan-table-mcp-server
```

安装完成后，你可以直接通过以下命令运行服务器：
```bash
python -m xiyan_mcp_server
```
但在完成以下配置之前，它不会提供任何功能。
你将获得一个 yml 文件。之后你可以通过以下命令运行服务器：
```yaml
env YML=path/to/yml python -m xiyan_mcp_server
```

## 配置

你需要一个 YAML 配置文件来配置服务器。
在 config_demo.yml 中提供了一个默认配置文件，内容如下：

```yaml
table:
  path: "" 
  encoding: "utf-8"     
  preview_rows: 20       

model:
  model_name: "qwen-max-0125"
  api_key: ""
  api_base: "https://dashscope.aliyuncs.com/compatible-mode/v1"
  temperature: 0.1

server:
  name: "xiyan-table"    
  version: "0.1.0"   
```

## 启动
```json
{
    "mcpServers": {
        "xiyan-table-mcp-server": {
            "command": "python",
            "args": [
                "-m",
                "xiyan_table_mcp_server"
            ],
            "env": {
                "YML": "PATH/TO/YML"
            }
        }
    }
}
```

**官方网站：** [https://github.com/zyy07/xiyan_table_mcp_server](https://github.com/zyy07/xiyan_table_mcp_server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`files`
- 标签：`file systems`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`python`
- 参数：`-m xiyan_table_mcp_server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/zyy07-xiyan-table.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
