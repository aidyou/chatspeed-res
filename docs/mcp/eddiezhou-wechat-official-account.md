---
title: "Wechat_Official_Account"
description: "WeChat Official Account content creation assistant - a multimodal-AI-powered tool for automated generation and publishing of WeChat Official Account content. A Python and MCP-based automation tool for…"
---

# Wechat_Official_Account

WeChat Official Account content creation assistant - a multimodal-AI-powered tool for automated generation and publishing of WeChat Official Account content. A Python and MCP-based automation tool for…

---
name: WeChat Official Account Content Creation Assistant
version: 1.0
description: A multimodal-AI-based tool for automated generation and publishing of WeChat Official Account content
author: AI Assistant
---

# WeChat Official Account Content Automation Assistant

A Python and MCP-based tool for automating WeChat Official Account content, covering the complete flow from material generation to draft creation.

# Tutorial video (reference)
Bilibili: https://www.bilibili.com/video/BV1iEhzzaEKr/
Douyin: https://www.douyin.com/user/self?modal_id=7544390677770112291

## Core Features

- **Access Token retrieval**: automatically obtains the WeChat Official Account API credential
- **AI cover generation and upload**: uses multimodal AI to generate article cover images and uploads them to the WeChat permanent material library automatically
- **AI article generation**: generates WeChat Official Account article content with AI
- **Automatic draft creation**: assembles the AI-generated cover and content and submits them to the WeChat draft box automatically

## Official Account Backend Configuration (Important)

**IP whitelist configuration (Important!!!):**
  [Settings & Development] -> [Development Interface Management] -> [Basic Configuration] -> IP whitelist
  Add the following IP: 47.92.200.108

**Developer ID retrieval (Important!!!):**
  [Settings & Development] -> [Development Interface Management] -> [Basic Configuration] -> Developer ID

**Developer password retrieval (Important!!!):**
  [Settings & Development] -> [Development Interface Management] -> [Basic Configuration] -> Developer password

**System prompt (Important!!!):**
  Provide the system prompt with the APP_ID and APP_SECRET obtained above. Example (replace with your own):
    APP_ID=wxcef12345678901c1
    APP_SECRET=d1234567890abcdefghijkl123456789

## Environment Requirements

- WeChat Official Account developer account
- MCP service support

## MCP Service Description

This tool calls and manages AI capabilities through the MCP service, mainly integrating the following AI capabilities:

- **Multimodal image generation**: creates cover images that meet WeChat Official Account requirements (2.35:1 ratio)
- **Text generation**: automatically writes WeChat Official Account article content
- **Content optimization**: adjusts the format of generated text to meet WeChat publishing requirements

## Workflow

### 1. Access Token Retrieval

The system first calls the official WeChat API with the AppID and AppSecret to obtain an Access Token, which serves as the base credential for all subsequent API calls.

```python
# Get the WeChat Official Account API credential
def get_wechat_access_token(appid, secret):
    url = "https://api.weixin.qq.com/cgi-bin/token"
    params = {
        "grant_type": "client_credential",
        "appid": appid,
        "secret": secret
    }
    # Send the request and handle the response...
```

### 2. AI Cover Generation and Upload

Uses the multimodal AI integrated through the MCP service to generate a compliant cover image, automatically uploads it to the WeChat permanent material library, and obtains a media_id for later draft creation.

**Generation and upload flow:**
1. Call the multimodal AI model via the MCP service to generate a cover image based on the article topic
2. Adjust the generated image to meet WeChat requirements for size and ratio (2.35:1)
3. Call the WeChat permanent material upload endpoint to upload the adjusted image
4. Parse the returned result, extract, and save the media_id

```python
# Upload permanent material (image)
def upload_wechat_permanent_media(access_token, media_file):
    url = f"https://api.weixin.qq.com/cgi-bin/material/add_material?access_token={access_token}&type=image"
    # Process the file and upload...
```

### 3. AI Article Generation and Draft Creation

Calls the text-generation AI model through the MCP service to create article content, and creates a WeChat draft using the previously obtained media_id.

**Article generation and draft creation flow:**
1. Call the text-generation AI model via the MCP service to generate article content based on the topic
2. Optimize the generated content's format to comply with WeChat publishing standards
3. Call the WeChat draft creation endpoint to create a draft using the generated content and cover material ID

```python
# Add a draft to the draft box
def add_wechat_draft(access_token, title, content, thumb_media_id):
    url = f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={access_token}"
    # Build the request data and send...
```

## Notes

- Make sure your WeChat Official Account has developer mode enabled and that you have the correct AppID and AppSecret
- The Access Token is valid for 2 hours; you need to re-fetch it after it expires
- Uploaded materials count against your WeChat material library quota; manage materials reasonably
- Generated content and cover images may require manual review before publishing
- Follow the WeChat Official Account platform's content policies and terms of use

## Configuration

Before using, make sure the following required parameters are configured:

- WeChat Official Account AppID
- WeChat Official Account AppSecret
- MCP service configuration (if needed)

## FAQ

### Q: Why does Access Token retrieval fail?
**A:** Check that the AppID and AppSecret are correct and that the network connection is working.

### Q: "invalid media_id" error when uploading material?
**A:** Make sure you are using a valid permanent material media_id; temporary material IDs cannot be used to create drafts.

### Q: What if the generated content quality is not satisfactory?
**A:** Try adjusting the AI model's prompt with a more detailed topic description.

## Tech Stack

- Python
- MCP service
- WeChat Official Account API
- Multimodal AI model (image generation)
- Text generation AI model

## License

Apache 2.0

**Official site: ** [https://modelscope.cn/studios/EddieZhou/Wechat_Official_Account](https://modelscope.cn/studios/EddieZhou/Wechat_Official_Account)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `communication`
- Tags: `communication`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `mcp-remote https://eddiezhou-wechat-official-account.ms.show/gradio_api/mcp/sse --transport sse-only`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/eddiezhou-wechat-official-account.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
