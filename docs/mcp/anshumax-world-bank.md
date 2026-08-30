---
title: "世界银行指标服务"
description: "启用AI助手与世界银行开放数据API交互，允许列出并分析可用国家的指标。"
---

# 世界银行指标服务

启用AI助手与世界银行开放数据API交互，允许列出并分析可用国家的指标。

# 世界银行 MCP 服务器
[Smithery](https://smithery.ai/server/@anshumax/world_bank_mcp_server)

这是一个模型上下文协议（MCP）服务器，能够与开放的世界银行数据 API 进行交互。该服务器允许 AI 助手列出指标，并对世界银行中可用国家的这些指标进行分析。

## 功能

- 列出世界银行开放数据 API 中可用的国家
- 列出世界银行开放数据 API 中可用的指标
- 分析各国的指标，如人口细分、贫困人口数量等
- 全面的日志记录

## 使用方法

### 在 Claude Desktop 上使用

将以下内容添加到您的 `claude_desktop_config.json` 文件中：

```json
{
  "mcpServers": {
    "world_bank": {
      "command": "uv",
      "args": [
        "--directory", 
        "path/to/world_bank_mcp_server",
        "run",
        "world_bank_mcp_server"
      ]
    }
  }
}
```

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@anshumax/world_bank_mcp_server) 自动为 Claude Desktop 安装世界银行数据服务器，请执行以下命令：

```bash
npx -y @smithery/cli install @anshumax/world_bank_mcp_server --client claude
```

**官方网站：** [https://github.com/anshumax/world_bank_mcp_server](https://github.com/anshumax/world_bank_mcp_server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`finance`, `data`
- 标签：`research and data`, `finance`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uv`
- 参数：`--directory path/to/world_bank_mcp_server run world_bank_mcp_server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/anshumax-world-bank.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
