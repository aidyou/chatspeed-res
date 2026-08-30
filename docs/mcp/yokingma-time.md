---
title: "time-时智"
description: "赋予大型语言模型时间感知能力。\n为您的大型语言模型赋予时间感知能力。访问当前时间、在时区之间转换并轻松获取时间戳。通过精确的时间相关功能增强您的应用程序。"
---

# time-时智

赋予大型语言模型时间感知能力。
为您的大型语言模型赋予时间感知能力。访问当前时间、在时区之间转换并轻松获取时间戳。通过精确的时间相关功能增强您的应用程序。

# 🚀 Time MCP Server: 为LLM赋予时间感知能力

[Smithery](https://smithery.ai/server/@yokingma/time-mcp) 

 

 
 alt="Report a bug">

这是一个模型上下文协议（MCP）服务器实现，它允许大语言模型（LLMs）具备时间感知功能。

 >

## 工具

- `current_time`: 获取当前时间（UTC 和本地时间）
- `relative_time`: 获取相对时间
- `get_timestamp`: 获取指定时间的时间戳
- `days_in_month`: 获取月份中的天数
- `convert_time`: 在不同时区之间转换时间
- `get_week_year`: 获取一年中的周和ISO周

## 安装

### 通过Smithery安装

要通过[Smithery](https://smithery.ai/server/@yokingma/time-mcp)自动为Claude Desktop安装time-mcp：

```bash
npx -y @smithery/cli install @yokingma/time-mcp --client claude
```

### 手动安装（可选）
```shell
npm install -g time-mcp
```

### 使用npx
```shell
npx -y time-mcp
```

## 在Cursor上运行

您的`mcp.json`文件将如下所示：

```json
{
  "mcpServers": {
    "time-mcp": {
      "command": "npx",
      "args": ["-y", "time-mcp"]
    }
  }
}
```

## 在Windsurf上运行

在您的`./codeium/windsurf/model_config.json`文件中添加以下内容：

```json
{
  "mcpServers": {
    "time-mcp": {
      "command": "npx",
      "args": ["-y", "time-mcp"]
    }
  }
}
```

## 许可证

MIT许可证 - 详情请参见[LICENSE](https://github.com/yokingma/time-mcp/blob/HEAD/LICENSE)文件。

**官方网站：** [https://github.com/yokingma/time-mcp](https://github.com/yokingma/time-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`productivity`
- 标签：`other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y time-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/yokingma-time.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
