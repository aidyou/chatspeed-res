---
title: "油管下载器-MCP"
description: "通过模型上下文协议（Model Context Protocol）将“yt-dlp”与大型语言模型（LLMs）连接起来，使用户能够下载YouTube内容，并将其与Dive以及其他与MCP兼容的大型语言模型进行集成。"
---

# 油管下载器-MCP

通过模型上下文协议（Model Context Protocol）将“yt-dlp”与大型语言模型（LLMs）连接起来，使用户能够下载YouTube内容，并将其与Dive以及其他与MCP兼容的大型语言模型进行集成。

# yt-dlp-mcp

一个与yt-dlp集成的MCP服务器实现，为大型语言模型（LLMs）提供视频和音频内容下载功能（例如YouTube、Facebook、Tiktok等）。

## 功能

* **字幕**：以SRT格式下载字幕供LLMs阅读
* **视频下载**：将视频保存到您的下载文件夹，并可控制分辨率
* **音频下载**：将音频保存到您的下载文件夹
* **注重隐私**：直接下载，无追踪
* **MCP集成**：与Dive及其他兼容MCP的LLMs一起工作

## 安装

### 前提条件

根据您的操作系统安装`yt-dlp`：

```bash
# Windows
winget install yt-dlp

# macOS
brew install yt-dlp

# Linux
pip install yt-dlp
```

### 通过[Dive Desktop](https://github.com/OpenAgentPlatform/Dive)

1. 在Dive Desktop中点击“+ 添加MCP服务器”
2. 复制并粘贴此配置：

```json
{
  "mcpServers": {
    "yt-dlp": {
      "command": "npx",
      "args": [
        "-y",
        "@kevinwatt/yt-dlp-mcp"
      ]
    }
  }
}
```
3. 点击“保存”以安装MCP服务器

## 工具文档

* **list_subtitle_languages**
  * 列出视频的所有可用字幕语言及其格式（包括自动生成的字幕）
  * 输入：
    * `url` (字符串, 必填): 视频的URL

* **download_video_subtitles**
  * 以任何可用格式下载视频字幕。支持常规字幕和自动生成的字幕。
  * 输入：
    * `url` (字符串, 必填): 视频的URL
    * `language` (字符串, 可选): 语言代码（如'en', 'zh-Hant', 'ja'）。默认为'en'

* **download_video**
  * 将视频下载到用户的下载文件夹
  * 输入：
    * `url` (字符串, 必填): 视频的URL
    * `resolution` (字符串, 可选): 视频分辨率('480p', '720p', '1080p', 'best')。默认为'720p'

* **download_audio**
  * 以最佳可用质量（通常是m4a/mp3格式）将音频下载到用户的下载文件夹
  * 输入：
    * `url` (字符串, 必填): 视频的URL

## 使用示例

让您的LLM执行以下命令：
```
"List available subtitles for this video: https://youtube.com/watch?v=..."
"Download a video from facebook: https://facebook.com/..."
"Download Chinese subtitles from this video: https://youtube.com/watch?v=..."
"Download this video in 1080p: https://youtube.com/watch?v=..."
"Download audio from this YouTube video: https://youtube.com/watch?v=..."
```

## 手动启动

如果需要，可以手动启动服务器：
```bash
npx @kevinwatt/yt-dlp-mcp
```

## 要求

* Node.js 20+
* 系统PATH中的`yt-dlp`
* 兼容MCP的LLM服务

## 文档

- [API参考](https://github.com/kevinwatt/yt-dlp-mcp/blob/HEAD/docs/api.md)
- [配置](https://github.com/kevinwatt/yt-dlp-mcp/blob/HEAD/docs/configuration.md)
- [错误处理](https://github.com/kevinwatt/yt-dlp-mcp/blob/HEAD/docs/error-handling.md)
- [贡献指南](https://github.com/kevinwatt/yt-dlp-mcp/blob/HEAD/docs/contributing.md)

## 许可证

MIT

## 作者

Dewei Yen

**官方网站：** [https://github.com/kevinwatt/yt-dlp-mcp](https://github.com/kevinwatt/yt-dlp-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`browser`, `media`
- 标签：`browser automation`, `entertainment and media`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y @kevinwatt/yt-dlp-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/kevinwatt-yt-dlp.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
