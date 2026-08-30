---
title: "Youtube-Vision-MCP（优兔视觉模型上下文协议服务器）"
description: "MCP（模型上下文协议）服务器利用Google Gemini Vision API与YouTube视频进行交互。它允许用户获取YouTube视频的描述、摘要、问题答案以及提取关键时刻。"
---

# Youtube-Vision-MCP（优兔视觉模型上下文协议服务器）

MCP（模型上下文协议）服务器利用Google Gemini Vision API与YouTube视频进行交互。它允许用户获取YouTube视频的描述、摘要、问题答案以及提取关键时刻。

# YouTube Vision MCP 服务器 (`youtube-vision`)

[![NPM version](/mcp-assets/f4e5d6b7ed21c580934a895ad71ee4a9.svg)](https://www.npmjs.com/package/youtube-vision) 
[![License: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://opensource.org/licenses/MIT)
[Smithery](https://smithery.ai/server/@minbang930/youtube-vision-mcp)

  

这是一个利用 Google Gemini Vision API 与 YouTube 视频进行交互的 MCP（Model Context Protocol）服务器。它允许用户获取视频描述、摘要、回答问题以及从 YouTube 视频中提取关键时刻。

## 功能

*   使用 Gemini Vision API 分析 YouTube 视频。
*   提供多种工具以实现不同的交互方式：
    *   一般描述或问答 (`ask_about_youtube_video`)
    *   摘要生成 (`summarize_youtube_video`)
    *   关键时刻提取 (`extract_key_moments`)
*   列出支持 `generateContent` 的可用 Gemini 模型。
*   可通过环境变量配置 Gemini 模型。
*   通过标准输入/输出 (stdio) 进行通信。

## 前提条件

在使用此服务器之前，请确保您已具备以下条件：

*   **Node.js:** 推荐版本 18 或更高。您可以从 [nodejs.org](https://nodejs.org/) 下载。
*   **Google Gemini API 密钥:** 从 [Google AI Studio](https://aistudio.google.com/app/apikey) 或 Google Cloud Console 获取您的 API 密钥。

## 安装与使用

有两种主要的方式来使用这个服务器：

### 通过 Smithery 安装

要通过 [Smithery](https://smithery.ai/mcp/@minbang930/youtube-vision-mcp) 自动为 Claude Desktop 安装 youtube-vision-mcp：

```bash
npx -y @smithery/cli install @minbang930/youtube-vision-mcp --client claude
```

### 选项 1：使用 npx（推荐用于快速使用）

运行此服务器最简单的方法是使用 `npx`，它可以下载并运行包而无需永久安装。

您可以在 MCP 客户端的设置文件（如 Claude, VSCode 等）中进行配置：

```json
{
  "mcpServers": {
    "youtube-vision": {
      "command": "npx",
      "args": [
        "-y",
        "youtube-vision"
      ],
      "env": {
        "GEMINI_API_KEY": "YOUR_GEMINI_API_KEY",
        "GEMINI_MODEL_NAME": "gemini-2.0-flash"
      }
    }
  }
}
```

将 `"YOUR_GEMINI_API_KEY"` 替换为您实际的 Google Gemini API 密钥。

### 选项 2：手动安装（从源代码）

如果您希望修改代码或直接从源代码运行：

1.  **克隆仓库:**
```bash
    git clone https://github.com/minbang930/Youtube-Vision-MCP.git
    cd youtube-vision
```

2.  **安装依赖:**
```bash
    npm install
```

3.  **构建项目:**
```bash
    npm run build
```

4.  **配置并运行:**
    您可以直接使用 `node dist/index.js` 运行编译后的代码（确保 `GEMINI_API_KEY` 已作为环境变量设置），或者配置您的 MCP 客户端使用 `node` 命令和 `dist/index.js` 的绝对路径来运行它，并通过 `env` 设置传递 API 密钥，如 npx 示例所示。

## 配置

该服务器使用以下环境变量：

*   `GEMINI_API_KEY` (必需): 您的 Google Gemini API 密钥。
*   `GEMINI_MODEL_NAME` (可选): 要使用的特定 Gemini 模型（例如，`gemini-1.5-flash`）。默认为 `gemini-2.0-flash`。**重要提示：** 对于生产或商业用途，请确保选择的模型版本没有被标记为“实验性”或“预览”。

环境变量应在您的 MCP 客户端设置文件（如 `mcp_settings.json`）的 `env` 部分中设置。

## 可用工具

### 1. `ask_about_youtube_video`

回答关于视频的问题或在没有提问时提供一般描述。

*   **输入:**
    *   `youtube_url` (字符串，必需): YouTube 视频的 URL。
    *   `question` (字符串，可选): 关于视频的具体问题。如果省略，则生成一般描述。
*   **输出:** 包含答案或描述的文本。

### 2. `summarize_youtube_video`

生成给定 YouTube 视频的摘要。

*   **输入:**
    *   `youtube_url` (字符串，必需): YouTube 视频的 URL。
    *   `summary_length` (字符串，可选): 所需的摘要长度（'short', 'medium', 'long'）。默认为 'medium'。
*   **输出:** 包含视频摘要的文本。

### 3. `extract_key_moments`

从给定的 YouTube 视频中提取关键时刻（时间戳和描述）。

*   **输入:**
    *   `youtube_url` (字符串，必需): YouTube 视频的 URL。
    *   `number_of_moments` (整数，可选): 要提取的关键时刻数量。默认为 3。
*   **输出:** 描述带有时间戳的关键时刻的文本。

### 4. `list_supported_models`

列出支持 `generateContent` 方法的可用 Gemini 模型（通过 REST API 获取）。

*   **输入:** 无
*   **输出:** 列出支持的模型名称的文本。

## 重要说明

*   **生产环境中的模型选择：** 当将此服务器用于生产或商业用途时，请确保所选的 `GEMINI_MODEL_NAME` 是适合生产使用的稳定版本。根据 [Gemini API 服务条款](https://ai.google.dev/gemini-api/terms)，被标记为“实验性”或“预览”的模型不允许用于生产部署。
*   **API 服务条款：** 使用此服务器依赖于 Google Gemini API。用户有责任审阅并遵守 [Google APIs 服务条款](https://developers.google.com/terms/) 和 [Gemini API 附加服务条款](https://ai.google.dev/gemini-api/terms)。请注意，Gemini API 的免费层和付费层之间可能存在不同的数据使用政策。在使用免费层时不要提交敏感或机密信息。
*   **内容责任：** 通过 Gemini API 生成的内容的准确性和适当性不作保证。在依赖或发布生成的内容之前请谨慎行事。

## 许可证

本项目遵循 MIT 许可证。详情请参见 LICENSE 文件。

**官方网站：** [https://github.com/minbang930/Youtube-Vision-MCP](https://github.com/minbang930/Youtube-Vision-MCP)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`image and video processing`, `entertainment and media`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`-y youtube-vision`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/minbang930-youtube-vision.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
