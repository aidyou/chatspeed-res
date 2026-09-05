---
title: "OpenAI Sora2 MCP"
description: "MCP API 是一个基于模型上下文协议（MCP）的 Sora2 视频水印移除服务，能够将 Sora2 视频水印移除功能无缝集成到主流的 MCP 兼容工具的工作流程中，如 Claude Desktop、OpenAI、Cursor、Dify、n8n 等。它支持由 AI 驱动的水印移除、快速集成以及安全可靠的使用。"
---

# OpenAI Sora2 MCP

MCP API 是一个基于模型上下文协议（MCP）的 Sora2 视频水印移除服务，能够将 Sora2 视频水印移除功能无缝集成到主流的 MCP 兼容工具的工作流程中，如 Claude Desktop、OpenAI、Cursor、Dify、n8n 等。它支持由 AI 驱动的水印移除、快速集成以及安全可靠的使用。

![English](/mcp-assets/fecd7369c3d0610652a0f2f3830b26f6.svg)
[GitHub](https://github.com/peizhou/mcp-openai-sora/blob/HEAD/README_ZH.md)
[GitHub](https://github.com/peizhou/mcp-openai-sora/blob/HEAD/README_JA.md)
![Deutsch](/mcp-assets/6d6f5ca6af325b769c422c3eb1e9cee8.svg)
[GitHub](https://github.com/peizhou/mcp-openai-sora/blob/HEAD/README_KO.md)
[GitHub](https://github.com/peizhou/mcp-openai-sora/blob/HEAD/README_ES.md)
[GitHub](https://github.com/peizhou/mcp-openai-sora/blob/HEAD/README_FR.md)
[GitHub](https://github.com/peizhou/mcp-openai-sora/blob/HEAD/README_PT.md)

**选择语言 / Choose your language / 言語を選択 / Sprache wählen / 언어 선택 / Elige tu idioma / Choisissez votre langue / Escolha seu idioma**

---

# MCP API - Sora2 视频水印移除服务

## 🎯 产品介绍

MCP API 是基于 Model Context Protocol (MCP) 的 Sora2 视频水印移除服务，能够将 Sora2 视频水印移除功能无缝集成到主流的 MCP 兼容工具（如 Claude Desktop、OpenAI、Cursor、Dify、n8n 等）的工作流中。只需几分钟即可通过简单的 API 密钥认证开始使用。

🌐 **官方文档页面**: [https://sora.thirdme.com/mcp](https://sora.thirdme.com/mcp)

## 🚀 快速入门

### 第一步：获取 API 密钥

1. 访问 [MCP API 页面](https://sora.thirdme.com/mcp)
2. 输入您的电子邮件地址
3. 点击“生成 API 密钥”按钮
4. 复制生成的 API 密钥（请妥善保管，它与您的订阅和使用配额相关联）

> ⚠️ **重要提示**：请妥善保管您的 API 密钥。生成新的密钥将会替换现有的密钥。如果您重新生成，请更新您的 MCP 配置。

### 第二步：配置 Claude Desktop

在您的 Claude Desktop 配置文件 `mcp.json` 中添加以下配置：

**配置文件位置:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

**配置:**

```json

{

  "mcpServers": {

    "sora-watermark-remover": {

      "url": "https://sora.thirdme.com/api/mcp-sse?key=YOUR_API_KEY"

    }

  }

}

```
> 将 `YOUR_API_KEY` 替换为第一步中获取的实际 API 密钥。

### 第三步：在 Claude 中使用

配置完成后，重启 Claude Desktop，然后您可以直接要求 Claude 移除 Sora2 视频中的水印：

**示例对话:**

```

Please remove the watermark from this Sora2 video: https://sora.chatgpt.com/share/xxx

```
Claude 将自动调用 MCP API 来处理视频，并返回无水印视频的下载链接。

## ✨ 核心功能

### 🤖 基于 AI 的水印移除
- **智能检测**：AI 自动识别并移除 Sora2 视频中的水印
- **保持质量**：在移除水印的同时保持原始视频质量
- **快速处理**：在 5 秒内完成处理，返回无水印视频链接

### 🔧 快速集成
- **简单配置**：只需添加配置文件和 API 密钥
- **广泛兼容性**：支持所有 MCP 兼容工具（如 Claude Desktop、OpenAI、Cursor、Dify、n8n 等）
- **即插即用**：配置后立即可用，无需额外开发

### 🔒 安全可靠
- **UUID 认证**：基于 UUID 的认证机制
- **速率限制**：防止滥用并确保服务稳定性
- **使用跟踪**：实时跟踪 API 使用情况和配额

### 📊 共享订阅
- **统一配额**：API 访问和网页版共享相同的订阅配额
- **灵活使用**：在多个平台和工具上使用同一订阅服务

## 📖 API 参考

### 端点

```

GET/POST https://sora.thirdme.com/api/mcp-sse?key=YOUR_API_KEY

```
### 可用工具

#### remove_watermark

从 Sora2 视频中移除水印并获取干净的下载链接。支持 OpenAI Sora 视频 URL。

**输入参数:**
- `videoUrl` (字符串): 要处理的 Sora2 视频 URL

**输出:**
返回一个 JSON 对象，包含：
- `videoUrl`: 无水印视频下载链接
- `thumbnailUrl`: 视频缩略图链接
- `videoInfo`: 详细的视频信息

**示例:**

```json

{

  "videoUrl": "https://example.com/video.mp4",

  "thumbnailUrl": "https://example.com/thumbnail.jpg",

  "videoInfo": {

    "title": "Video Title",

    "duration": 30,

    "resolution": "1920x1080"

  }

}

```
### 错误代码

| 错误代码 | 描述 |
|------------|-------------|
| -32001 | 用户未找到 |
| -32003 | 需要订阅或已达到使用限制 |
| -32004 | 视频处理失败 |

## 🛠️ 支持的平台- ✅ Claude Desktop
- ✅ OpenAI (MCP Compatible)
- ✅ Cursor
- ✅ Dify
- ✅ n8n
- ✅ 其他兼容MCP的工具

## 💡 使用案例

### 用例1：批量处理Sora2视频
在Claude Desktop中，您可以一次性处理多个Sora2视频：

```

Please process and remove watermarks from the following Sora2 videos:

1. https://sora.chatgpt.com/share/video1

2. https://sora.chatgpt.com/share/video2

3. https://sora.chatgpt.com/share/video3

```
### 用例2：集成到自动化工作流
在n8n或Dify中，您可以将水印移除功能集成到您的自动化工作流中，以进行批量处理和自动化操作。

### 用例3：Cursor开发助手
在Cursor中开发项目时，您可以直接要求AI助手处理Sora2视频的水印移除任务，而无需离开开发环境。

## 📝 注意事项

1. **API密钥安全**：请确保您的API密钥安全，不要与他人共享或将它提交到公共仓库。
2. **配额限制**：API使用受订阅配额限制，请负责任地使用。
3. **视频格式**：目前仅支持Sora2视频URL（sora.chatgpt.com/share/xxx 格式）。
4. **处理时间**：大多数视频在5秒内处理完成。
5. **数据安全**：处理后的视频将在24小时后自动从服务器删除。

## ❓ 常见问题

### Q: 我在哪里可以获得API密钥？
A: 访问[https://sora.thirdme.com/mcp](https://sora.thirdme.com/mcp)，输入您的电子邮件地址生成API密钥。

### Q: 如何测试API密钥是否有效？
A: 在MCP API页面上生成密钥后，您可以使用页面上的“测试API密钥”功能来验证密钥的有效性。

### Q: 使用API收费吗？
A: API使用与网页版共享相同的订阅配额。具体价格请参阅[Pricing page](https://sora.thirdme.com/#pricing)。

### Q: 是否支持其他视频平台？
A: 目前主要支持Sora2视频（sora.chatgpt.com），未来可能会支持更多平台。

### Q: 如何处理订阅和配额问题？
A: API访问使用与网页版相同的订阅服务。您可以在网页版上管理订阅并查看使用情况。

## 📧 支持与反馈

如果您在使用过程中遇到任何问题或有任何建议，请联系我们：

- 📧 电子邮件：support@thirdme.com
- 🌐 网站：[https://sora.thirdme.com](https://sora.thirdme.com)
- 📄 API文档：[https://sora.thirdme.com/mcp](https://sora.thirdme.com/mcp)

## 📄 许可证

本服务遵循Sora Watermark Remover的服务条款和隐私政策。

---

**🎉 开始使用MCP API，让您的AI工作流更强大！**

**官方网站：** [https://github.com/peizhou/mcp-openai-sora](https://github.com/peizhou/mcp-openai-sora)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`developer tools`, `art and culture`, `browser automation`, `sora`, `openai`, `cursor`, `claude`, `sora2`

## MCP 配置

- 传输方式：`http`
- 启动命令：``
- 参数：无

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/thirdme-sora2videoremovewatermark.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
