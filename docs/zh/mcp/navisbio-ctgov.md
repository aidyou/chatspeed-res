---
title: "临床试验数据平台"
description: "提供了对ClinicalTrials.gov AACT数据库的访问， enables分析临床试验数据、跟踪发展趋 势以及生成治疗景观洞察。"
---

# 临床试验数据平台

提供了对ClinicalTrials.gov AACT数据库的访问， enables分析临床试验数据、跟踪发展趋 势以及生成治疗景观洞察。

# AACT 临床试验 MCP 服务器

## 概述
这是一个实现了模型上下文协议（MCP）的服务器，提供了对AACT（ClinicalTrials.gov的数据聚合分析）数据库的访问。该服务器能够分析临床试验数据、追踪研发趋势，并自动生成分析备忘录，记录关于治疗领域见解的信息。

## 组件

### 资源
- `memo://insights`: 存储关于临床试验模式的分析发现和见解
- `schema://database`: 数据库模式信息

### 提示词
- `indication-landscape`: 分析给定治疗领域的临床试验模式
  - 必需: `topic` (例如, "多发性硬化症", "乳腺癌")

### 工具
- `read-query`: 在AACT数据库上执行SELECT查询
- `list-tables`: 获取AACT数据库中的可用表
- `describe-table`: 查看特定表的模式信息
- `append-insight`: 添加新的分析发现

## 设置

### 数据库访问
1. 在 https://aact.ctti-clinicaltrials.org/users/sign_up 创建一个免费账户
2. 设置环境变量：
   - `DB_USER`: AACT数据库用户名
   - `DB_PASSWORD`: AACT数据库密码

## 使用Claude桌面版

请注意，目前你需要Claude桌面版以及Claude订阅服务。

将以下配置之一添加到文件claude_desktop_config.json中。（在macOS上，文件位于 /Users/YOUR_USERNAME/Library/Application Support/Claude/claude_desktop_config.json，如果不存在则需要自己创建。）

### 选项1：使用已发布的包
```json
"mcpServers": {
    "CTGOV-MCP": {
      "command": "uvx",
      "args": [
        "mcp-server-aact"
      ],
      "env": {
        "DB_USER": "USERNAME",
        "DB_PASSWORD": "PASSWORD"
      }
    }
}
```

### 选项2：从源代码运行（开发）
```json
"mcpServers": {
    "CTGOV-MCP-DEV": {
      "command": "uv",
      "args": [
        "--directory",
        "PATH_TO_REPOSITORY",
        "run",
        "mcp-server-aact"
      ],
      "env": {
        "DB_USER": "USERNAME",
        "DB_PASSWORD": "PASSWORD"
      }
    }
}
```

## 贡献
我们欢迎贡献！请：
- 在GitHub上开启一个问题
- 发起讨论
- 邮件: jonas.walheim@navis-bio.com

## 许可证
GNU通用公共许可证v3.0 (GPL-3.0)

## 致谢

本项目受到启发并最初基于以下项目的代码：
- [SQLite MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite)
- [DuckDB MCP Server](https://github.com/ktanaka101/mcp-server-duckdb/tree/main)
- [OpenDataMCP](https://github.com/OpenDataMCP/OpenDataMCP)

感谢这些优秀的项目为我们指明方向！🙌

**官方网站：** [https://github.com/navisbio/ctgov_MCP](https://github.com/navisbio/ctgov_MCP)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`research and data`, `databases`, `health and wellness`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`mcp-server-aact`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/navisbio-ctgov.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
