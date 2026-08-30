---
title: "MCP-MIRO连接器"
description: "用于连接MIRO白板应用的模型上下文协议服务器。允许进行白板操作、便签创建、批量操作等更多功能。"
---

# MCP-MIRO连接器

用于连接MIRO白板应用的模型上下文协议服务器。允许进行白板操作、便签创建、批量操作等更多功能。

# mcp-miro MCP 服务器
[Smithery](https://smithery.ai/server/@llmindset/mcp-miro)

一个用于连接 MIRO 白板应用程序的 Model Context Protocol 服务器。

- 允许板面操作、便签创建、批量操作等。
- 可以通过环境变量传递您的 OAuth 密钥，或者使用“--token”参数。
- 拍摄便签照片并让 Claude 创建 MIRO 等效作品效果非常好。

## 安装

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@llmindset/mcp-miro) 自动安装适用于 Claude Desktop 的 MIRO 白板连接器：

```bash
npx -y @smithery/cli install @llmindset/mcp-miro --client claude
```

### 使用 mcp-get

您可以使用 mcp-get 安装此包：

```bash
npx @michaellatman/mcp-get@latest install @llmindset/mcp-miro
```

_注意 - 如果您使用的是旧版本的 Windows PowerShell，可能需要先运行_ `Set-ExecutionPolicy Bypass -Scope Process` _再执行此命令。_

## 功能

### 资源
- 获取板面内容

### 工具
- 创建便签、形状
- 读取板面、框架、内容
- 批量创建

### 提示
- 关于板面坐标等指导

## 开发

安装依赖项：
```bash
npm install
```

构建服务器：
```bash
npm run build
```

对于带有自动重建的开发：
```bash
npm run watch
```

## 安装

要与 Claude Desktop 一起使用，请添加服务器配置：

在 MacOS 上：`~/Library/Application Support/Claude/claude_desktop_config.json`
在 Windows 上：`%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "mcp-miro": {
      "command": "/path/to/node-or-npx",
      "arguments": [
        "/path/to/mcp-miro/build/index.js",
        "--token","MIRO-OAUTH-KEY"
      ]
    }
  }
}
```

### 调试

由于 MCP 服务器通过 stdio 进行通信，调试可能会有挑战。我们建议使用 [MCP Inspector](https://github.com/modelcontextprotocol/inspector)，它作为一个包脚本提供：

```bash
npm run inspector
```

Inspector 将提供一个 URL 以便在浏览器中访问调试工具。

在开发环境中推荐添加 [https://github.com/miroapp/api-clients/blob/041de24ebf7955432b447d887ede066ad4c7e2c7/packages/generator/spec.json](https://github.com/miroapp/api-clients/blob/041de24ebf7955432b447d887ede066ad4c7e2c7/packages/generator/spec.json) 作为参考。

**官方网站：** [https://github.com/evalstate/mcp-miro](https://github.com/evalstate/mcp-miro)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`, `other`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`/path/to/node-or-npx`
- 参数：无

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/evalstate-miro.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
