---
title: "代码思维MCP"
description: "一个模型上下文协议（MCP）服务器，通过自动化流程帮助用户快速理解代码仓库并生成思维导图。它包括管理仓库、拉取请求、问题以及从README.md文件生成思维导图的功能。"
---

# 代码思维MCP

一个模型上下文协议（MCP）服务器，通过自动化流程帮助用户快速理解代码仓库并生成思维导图。它包括管理仓库、拉取请求、问题以及从README.md文件生成思维导图的功能。

# CodeMind MCP

一个 MCP（Model Context Protocol）服务器，通过自动化流程帮助用户快速理解代码仓库并生成思维导图。

## 背景
是不是老是忘记git命令？
- 本MCP 可以用于管理仓库、拉取请求、问题等。

**得到一个项目是不是看不懂项目？**
- **本MCP会作为一个专业的架构师，帮助你快速理解代码仓库并生成思维导图**。

## 核心功能

1.  **`gitcode_request`**: 通用的 GitCode API 调用工具，用于管理仓库、拉取请求、问题等。
2.  **`mindmap`**: 读取当前目录及其子目录中的所有 README.md 文件，生成思维导图：
    *   递归查找并收集所有 README.md 文件
    *   合并文件内容并调用 Coze 工作流生成思维导图
    *   返回思维导图公开访问链接

## 安装与使用

**环境要求**: Node.js >= 18.x

### 全局安装
```bash
npm install -g @lucianaib/codemind-mcp
codemind-mcp
```

### 在 MCP 客户端中配置
```json
{
  "mcpServers": {
    "CodeMind": {
      "command": "npx",
      "args": ["@lucianaib/codemind-mcp"]
    }
  }
}
```


## 工具调用参数

### `gitcode_request`
- **baseUrl**: string (可选)，如 `https://api.gitcode.com`
- **token**: string，鉴权令牌（支持 `Bearer ` 或纯 token）
- **method**: "GET" | "POST" | "PUT" | "PATCH" | "DELETE"
- **path**: string，如 `/v1/repos`
- **query**: Record (可选)
- **body**: Record (可选)
- **headers**: Record (可选)

### `mindmap`
- **prompt**: string (可选)，用于自定义生成思维导图的提示词

## 开发与代码结构

- `src/index.ts`: MCP 服务器入口，使用 `McpServer` 注册工具
- `src/gitcode.ts`: GitCode API 的通用请求封装
- `src/mindmap.ts`: README.md 文件收集及调用 Coze API 的核心逻辑

## 安全提示

**重要**: Coze API 凭证目前硬编码在 `src/mindmap.ts` 中，存在安全风险。生产环境请移至环境变量。

## 许可证

本项目采用 MIT 许可证。详见 [LICENSE](https://github.com/OnePieceLwc/CodeMind-MCP/blob/HEAD/LICENSE) 文件。

**官方网站：** [https://github.com/OnePieceLwc/CodeMind-MCP](https://github.com/OnePieceLwc/CodeMind-MCP)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`, `思维导图`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`@lucianaib/codemind-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/weiaib-codemind.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
