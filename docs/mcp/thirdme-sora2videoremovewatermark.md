---
title: "Sora2VideoRemoveWatermark"
description: "Choose your language / 选择语言 / 言語を選択 / Sprache wählen / 언어 선택 / Elige tu idioma / Choisissez votre langue / Escolha seu idioma --- MCP API is a Sora2 video watermark removal service based on Model Cont"
---

# Sora2VideoRemoveWatermark

Choose your language / 选择语言 / 言語を選択 / Sprache wählen / 언어 선택 / Elige tu idioma / Choisissez votre langue / Escolha seu idioma --- MCP API is a Sora2 video watermark removal service based on Model Cont

![English](/mcp-assets/fecd7369c3d0610652a0f2f3830b26f6.svg)
[GitHub](https://github.com/peizhou/mcp-openai-sora/blob/HEAD/README_ZH.md)
[GitHub](https://github.com/peizhou/mcp-openai-sora/blob/HEAD/README_JA.md)
![Deutsch](/mcp-assets/6d6f5ca6af325b769c422c3eb1e9cee8.svg)
[GitHub](https://github.com/peizhou/mcp-openai-sora/blob/HEAD/README_KO.md)
[GitHub](https://github.com/peizhou/mcp-openai-sora/blob/HEAD/README_ES.md)
[GitHub](https://github.com/peizhou/mcp-openai-sora/blob/HEAD/README_FR.md)
[GitHub](https://github.com/peizhou/mcp-openai-sora/blob/HEAD/README_PT.md)

**Choose your language / 选择语言 / 言語を選択 / Sprache wählen / 언어 선택 / Elige tu idioma / Choisissez votre langue / Escolha seu idioma**

---

# MCP API - Sora2 Video Watermark Removal Service

## 🎯 Product Introduction

MCP API is a Sora2 video watermark removal service based on Model Context Protocol (MCP), enabling seamless integration of Sora2 video watermark removal functionality into workflows of mainstream MCP-compatible tools such as Claude Desktop, OpenAI, Cursor, Dify, n8n, and more. Get started in minutes with simple API key authentication.

🌐 **Official Documentation Page**: [https://sora.thirdme.com/mcp](https://sora.thirdme.com/mcp)

## 🚀 Quick Start

### Step 1: Get API Key

1. Visit the [MCP API page](https://sora.thirdme.com/mcp)
2. Enter your email address
3. Click the "Generate API Key" button
4. Copy the generated API key (Keep it secure, it's linked to your subscription and usage quota)

> ⚠️ **Important**: Keep your API key secure. Generating a new key will replace your existing key. If you regenerate, please update your MCP configuration.

### Step 2: Configure Claude Desktop

Add the following configuration to your Claude Desktop config file `mcp.json`:

**Config File Locations:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

**Configuration:**

```json
{
  "mcpServers": {
    "sora-watermark-remover": {
      "url": "https://sora.thirdme.com/api/mcp-sse?key=YOUR_API_KEY"
    }
  }
}
```

> Replace `YOUR_API_KEY` with your actual API key obtained in Step 1.

### Step 3: Use in Claude

After configuration, restart Claude Desktop, then you can directly ask Claude to remove watermarks from Sora2 videos:

**Example Conversation:**

```
Please remove the watermark from this Sora2 video: https://sora.chatgpt.com/share/xxx
```

Claude will automatically call the MCP API to process the video and return a download link to the watermark-free video.

## ✨ Core Features

### 🤖 AI-Powered Watermark Removal
- **Smart Detection**: AI automatically identifies and removes watermarks from Sora2 videos
- **Preserve Quality**: Maintain original video quality while removing watermarks
- **Fast Processing**: Complete processing in 5 seconds, return watermark-free video links

### 🔧 Fast Integration
- **Simple Configuration**: Just add configuration file and API key
- **Wide Compatibility**: Supports all MCP-compatible tools (Claude Desktop, OpenAI, Cursor, Dify, n8n, etc.)
- **Plug and Play**: Ready to use immediately after configuration, no additional development required

### 🔒 Secure & Reliable
- **UUID Authentication**: UUID-based authentication mechanism
- **Rate Limiting**: Prevents abuse and ensures service stability
- **Usage Tracking**: Real-time tracking of API usage and quotas

### 📊 Shared Subscription
- **Unified Quota**: API access and web version share the same subscription quota
- **Flexible Usage**: Use the same subscription service across multiple platforms and tools

## 📖 API Reference

### Endpoint

```
GET/POST https://sora.thirdme.com/api/mcp-sse?key=YOUR_API_KEY
```

### Available Tools

#### remove_watermark

Remove watermark from Sora2 video and get the clean download link. Supports OpenAI Sora video URLs.

**Input Parameters:**
- `videoUrl` (string): The Sora2 video URL to process

**Output:**
Returns a JSON object containing:
- `videoUrl`: Watermark-free video download link
- `thumbnailUrl`: Video thumbnail link
- `videoInfo`: Detailed video information

**Example:**

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

### Error Codes

| Error Code | Description |
|------------|-------------|
| -32001 | User not found |
| -32003 | Subscription required or usage limit reached |
| -32004 | Failed to process video |

## 🛠️ Supported Platforms

- ✅ Claude Desktop
- ✅ OpenAI (MCP Compatible)
- ✅ Cursor
- ✅ Dify
- ✅ n8n
- ✅ Other MCP-Compatible Tools

## 💡 Use Cases

### Use Case 1: Batch Process Sora2 Videos
In Claude Desktop, you can process multiple Sora2 videos at once:

```
Please process and remove watermarks from the following Sora2 videos:
1. https://sora.chatgpt.com/share/video1
2. https://sora.chatgpt.com/share/video2
3. https://sora.chatgpt.com/share/video3
```

### Use Case 2: Integrate into Automation Workflows
In n8n or Dify, you can integrate watermark removal into your automation workflows for batch processing and automated operations.

### Use Case 3: Cursor Development Assistant
When developing projects in Cursor, you can directly ask the AI assistant to handle Sora2 video watermark removal tasks without leaving the development environment.

## 📝 Notes

1. **API Key Security**: Keep your API key secure, do not share it with others or commit it to public repositories
2. **Quota Limits**: API usage is subject to subscription quota limits, please use responsibly
3. **Video Format**: Currently only supports Sora2 video URLs (sora.chatgpt.com/share/xxx format)
4. **Processing Time**: Most videos are processed within 5 seconds
5. **Data Security**: Processed videos are automatically deleted from the server after 24 hours

## ❓ FAQ

### Q: Where can I get an API key?
A: Visit [https://sora.thirdme.com/mcp](https://sora.thirdme.com/mcp), enter your email address to generate an API key.

### Q: How to test if the API key is valid?
A: After generating a key on the MCP API page, you can use the "Test API Key" feature on the page to verify the key's validity.

### Q: Is API usage charged?
A: API usage shares the same subscription quota as the web version. Please refer to the [Pricing page](https://sora.thirdme.com/#pricing) for specific pricing.

### Q: Do you support other video platforms?
A: Currently mainly supports Sora2 videos (sora.chatgpt.com), more platforms may be supported in the future.

### Q: How to handle subscription and quota issues?
A: API access uses the same subscription service as the web version. You can manage subscriptions and view usage on the web version.

## 📧 Support & Feedback

If you encounter any issues during use or have any suggestions, please contact us:

- 📧 Email: support@thirdme.com
- 🌐 Website: [https://sora.thirdme.com](https://sora.thirdme.com)
- 📄 API Documentation: [https://sora.thirdme.com/mcp](https://sora.thirdme.com/mcp)

## 📄 License

This service follows Sora Watermark Remover's Terms of Service and Privacy Policy.

---

**🎉 Start using MCP API and make your AI workflows more powerful!**

**Official site: ** [https://github.com/peizhou/mcp-openai-sora](https://github.com/peizhou/mcp-openai-sora)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `developer tools`, `art and culture`, `browser automation`, `sora`, `openai`, `cursor`, `claude`, `sora2`

## MCP Configuration

- Transport: `http`
- Command: ``
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/thirdme-sora2videoremovewatermark.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
