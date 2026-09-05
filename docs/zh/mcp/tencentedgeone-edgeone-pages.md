---
title: "EdgeOne Pages"
description: "基于 EdgeOne Pages 的 MCP 服务器，支持代码部署为在线页面。"
---

# EdgeOne Pages

基于 EdgeOne Pages 的 MCP 服务器，支持代码部署为在线页面。

# EdgeOne Pages MCP

一个用于将 HTML 内容部署到 EdgeOne Pages 并获取公开可访问 URL 的 MCP 服务。

  

## 演示

![](/mcp-assets/3220ccb45aa40a64f0fd4530fdc7c220.gif)

## 要求

* Node.js 18 或更高版本

## 配置 MCP

```json
{
  "mcpServers": {
    "edgeone-pages-mcp-server": {
      "command": "npx",
      "args": ["edgeone-pages-mcp"]
    }
  }
}
```

## 架构

架构图展示了工作流程：
1. 大型语言模型生成 HTML 内容
2. 内容发送到 EdgeOne Pages MCP 服务器
3. MCP 服务器将内容部署到 EdgeOne Pages 边缘函数
4. 内容存储在 EdgeOne KV Store 以便快速边缘访问
5. MCP 服务器返回一个公共 URL
6. 用户可以通过浏览器访问已部署的内容并享受快速边缘交付

## 功能

* 通过 MCP 协议快速将 HTML 内容部署到 EdgeOne Pages
* 自动生成公开可访问的 URL

## 实现

此 MCP 服务集成了 EdgeOne Pages Functions 以部署静态 HTML 内容。实现方式使用：

1. **EdgeOne Pages Functions** - 一种无服务器计算平台，允许在边缘执行 JavaScript/TypeScript 代码。

2. **关键实现细节**：
   - 使用 EdgeOne Pages KV 存储并提供 HTML 内容
   - 为每次部署自动生成一个公共 URL
   - 使用适当的错误消息处理 API 错误

3. **工作原理**：
   - MCP 服务器通过 `deploy-html` 工具接受 HTML 内容
   - 它连接到 EdgeOne Pages API 以获取基础 URL
   - 使用 EdgeOne Pages KV API 部署 HTML 内容
   - 返回一个可公开访问的已部署内容的 URL

4. **使用示例**：
   - 向 MCP 服务提供 HTML 内容
   - 接收一个可立即访问的公共 URL

有关更多信息，请参阅 [EdgeOne Pages Functions 文档](https://edgeone.ai/document/162227908259442688) 和 [EdgeOne Pages KV 存储指南](https://edgeone.ai/document/162227803822321664)。

## 许可证

MIT

**官方网站：** [https://github.com/TencentEdgeOne/edgeone-pages-mcp/tree/main](https://github.com/TencentEdgeOne/edgeone-pages-mcp/tree/main)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`
- 标签：`developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`edgeone-pages-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/tencentedgeone-edgeone-pages.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
