---
title: "YouTube字幕提取器"
description: "一个模型上下文协议服务器，能够从YouTube视频中检索字幕。该服务器通过简单的方式提供对视频字幕和 subtitle 的直接访问。"
---

# YouTube字幕提取器

一个模型上下文协议服务器，能够从YouTube视频中检索字幕。该服务器通过简单的方式提供对视频字幕和 subtitle 的直接访问。

# YouTube 字幕服务器

[Smithery](https://smithery.ai/server/@kimtaeyoon83/mcp-server-youtube-transcript)

一个模型上下文协议服务器，可以检索 YouTube 视频的字幕。该服务器通过简单的接口直接访问视频字幕和字幕。

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/server/@kimtaeyoon83/mcp-server-youtube-transcript) 自动为 Claude Desktop 安装 YouTube 字幕服务器：

```bash
npx -y @smithery/cli install @kimtaeyoon83/mcp-server-youtube-transcript --client claude
```

## 组件

### 工具

- **get_transcript**
  - 从 YouTube 视频中提取字幕
  - 输入：
    - `url` (字符串, 必填): YouTube 视频 URL 或视频 ID
    - `lang` (字符串, 可选, 默认: "en"): 字幕的语言代码（例如 'ko', 'en'）

## 主要功能

- 支持多种视频 URL 格式
- 特定语言的字幕检索
- 响应中的详细元数据

## 配置

要在 Claude Desktop 中使用此服务器，请添加以下配置：

```json
{
  "mcpServers": {
    "youtube-transcript": {
      "command": "npx",
      "args": ["-y", "@kimtaeyoon83/mcp-server-youtube-transcript"]
    }
  }
}
```

## 通过工具安装

[mcp-get](https://github.com/michaellatman/mcp-get) 是一个用于安装和管理 Model Context Protocol (MCP) 服务器的命令行工具。

```shell
npx @michaellatman/mcp-get@latest install @kimtaeyoon83/mcp-server-youtube-transcript
```

## awesome-mcp-servers 
[awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) 是一个精选的 Model Context Protocol (MCP) 服务器列表。

## 开发

### 前提条件

- Node.js 18 或更高版本
- npm 或 yarn

### 设置

安装依赖项：
```bash
npm install
```

构建服务器：
```bash
npm run build
```

进行带有自动重建的开发：
```bash
npm run watch
```

### 测试

```bash
npm test
```

### 调试

由于 MCP 服务器通过 stdio 进行通信，调试可能会比较困难。我们建议在开发过程中使用 MCP Inspector：

```bash
npm run inspector
```

## 错误处理

该服务器实现了针对常见场景的强大错误处理：
- 无效的视频 URL 或 ID
- 不可用的字幕
- 语言可用性问题
- 网络错误

## 使用示例

1. 通过视频 URL 获取字幕：
```typescript
await server.callTool("get_transcript", {
  url: "https://www.youtube.com/watch?v=VIDEO_ID",
  lang: "en"
});
```

2. 通过视频 ID 获取字幕：
```typescript
await server.callTool("get_transcript", {
  url: "VIDEO_ID",
  lang: "ko"
});
```

3. 如何在 Claude Desktop 应用中提取 YouTube 字幕
```
chat: https://youtu.be/ODaHJzOyVCQ?si=aXkJgso96Deri0aB Extract subtitles
```

## 安全注意事项

该服务器：
- 验证所有输入参数
- 优雅地处理 YouTube API 错误
- 实现了字幕检索超时
- 提供详细的错误消息以帮助故障排除

## 许可证

此 MCP 服务器采用 MIT 许可证。有关详细信息，请参阅 LICENSE 文件。

**官方网站：** [https://github.com/kimtaeyoon83/mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`entertainment and media`, `speech processing`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @kimtaeyoon83/mcp-server-youtube-transcript`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/kimtaeyoon83-youtube-transcript.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
