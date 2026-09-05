---
title: "MasterGo设计协作工具"
description: "MasterGo Magic MCP 是一个独立的 MCP（模型上下文协议）服务，旨在将 MasterGo 设计工具与 AI 模型连接起来。它使 AI 模型能够直接从 MasterGo 设计文件中检索 DSL 数据。"
---

# MasterGo设计协作工具

MasterGo Magic MCP 是一个独立的 MCP（模型上下文协议）服务，旨在将 MasterGo 设计工具与 AI 模型连接起来。它使 AI 模型能够直接从 MasterGo 设计文件中检索 DSL 数据。

# MasterGo Magic MCP

MasterGo Magic MCP 是一项独立的 MCP（模型上下文协议）服务，旨在将 MasterGo 设计工具与 AI 模型连接起来。它使 AI 模型能够直接从 MasterGo 设计文件中检索 DSL 数据。

## 核心功能

- 从 MasterGo 设计文件中检索 DSL 数据
- 可通过 npx 直接运行
- 不需要外部依赖，只需 Node.js 环境

## 教程

- https://mastergo.com/file/155675508499265?page_id=158:0002

## 使用方法

### 获取 MG_MCP_TOKEN

1. 访问 https://mastergo.com
2. 进入个人设置
3. 点击安全设置选项卡
4. 找到个人访问令牌
5. 点击生成令牌

### 命令行选项

```
npx @mastergo/magic-mcp --token=YOUR_TOKEN [--url=API_URL] [--rule=RULE_NAME] [--debug]
```

#### 参数：

- `--token=YOUR_TOKEN` （必需）：用于身份验证的 MasterGo API 令牌
- `--url=API_URL` （可选）：API 基础 URL，默认为 http://localhost:3000
- `--rule=RULE_NAME` （可选）：添加要应用的设计规则，可以多次使用
- `--debug` （可选）：启用调试模式以获取详细错误信息

您还可以使用空格分隔格式来指定参数：

```
npx @mastergo/magic-mcp --token YOUR_TOKEN --url API_URL --rule RULE_NAME --debug
```

### cursor 使用方法

Cursor Mcp 使用指南参考：https://docs.cursor.com/context/model-context-protocol#using-mcp-tools-in-agent

```json
{
  "mcpServers": {
    "mastergo-magic-mcp": {
      "command": "npx",
      "args": [
        "-y",
        "@mastergo/magic-mcp",
        "--token=",
        "--url=https://mastergo.com"
      ],
      "env": {}
    }
  }
}
```

### cline 使用方法

```json
{
  "mcpServers": {
    "@master/mastergo-magic-mcp": {
      "command": "npx",
      "args": [
        "-y",
        "@mastergo/magic-mcp",
        "--token=",
        "--url=https://mastergo.com"
      ],
      "env": {}
    }
  }
}
```

## 许可证

ISC

**官方网站：** [https://github.com/mastergo-design/mastergo-magic-mcp](https://github.com/mastergo-design/mastergo-magic-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @mastergo/magic-mcp --token=MG_MCP_TOKEN --url=https://mastergo.com`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/mastergo-design-mastergo-magic.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
