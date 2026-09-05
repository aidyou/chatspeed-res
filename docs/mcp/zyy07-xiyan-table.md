---
title: "xiyan_table_mcp_server"
description: "\"The getdata tool offers a natural language interface for accessing CSV files and uses language model to analyze and respond to queries.\""
---

# xiyan_table_mcp_server

"The getdata tool offers a natural language interface for accessing CSV files and uses language model to analyze and respond to queries."

## Features
- 🌐 Analyze and query table information using natural language.
- 🤖 Support general LLMs (GPT,Qwen-Max), and [XiYanTable]
- 🔧 Read table contents from CSV files

## Tools Preview
 - "The ``get_data`` tool offers a natural language interface for accessing CSV files and uses language model to analyze and respond to queries."

## QuickStart

Python 3.10+ is required. 
You can install the server through pip, and it will install the latest version:

```bash
pip install xiyan-table-mcp-server
```

After that you can directly run the server by:
```bash
python -m xiyan_table_mcp_server
```
But it does not provide any functions until you complete following config.
You will get a yml file. After that you can run the server by:
```yaml
env YML=path/to/yml python -m xiyan_table_mcp_server
```

## Configuration

You need a YAML config file to configure the server.
A default config file is provided in config_demo.yml which looks like this:

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

## Launch
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

**Official site: ** [https://github.com/zyy07/xiyan_table_mcp_server](https://github.com/zyy07/xiyan_table_mcp_server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `files`
- Tags: `file systems`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `python`
- Args: `-m xiyan_table_mcp_server`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/zyy07-xiyan-table.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
