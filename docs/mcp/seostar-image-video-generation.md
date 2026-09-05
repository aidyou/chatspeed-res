---
title: "image-video-generation-mcp"
description: "An MCP (Model Context Protocol) server for image and video generation, supporting the CogView and CogVideoX models of the BigModel AI platform."
---

# image-video-generation-mcp

An MCP (Model Context Protocol) server for image and video generation, supporting the CogView and CogVideoX models of the BigModel AI platform.

# MCP Image Video Generation Server

A free MCP (Model Context Protocol) server for generating images and videos, supporting the CogView and CogVideoX models of the BigModel AI platform.

## Features

- 🎨 **Image Generation**: Generate high-quality images using CogView models (cogview-4, cogview-4-250304, cogview-3-flash), with the default being the free cogview-3-flash model
- 🎬 **Video Generation**: Generate videos using CogVideoX models (cogvideox-3, cogvideox-2, cogvideox-flash), with the default being the cogvideox-flash model
- ⚙️ **Configuration Management**: Supports environment variable configuration and dynamic setting updates
- 🔄 **Asynchronous Processing**: Supports video generation task status queries and automatic waiting for completion
- 🛡️ **Error Handling**: Built-in retry mechanism and detailed error messages
- 📝 **TypeScript**: Full type safety support
- 🔧 **Debugging Support**: Built-in MCP Inspector and VS Code debugging configuration
- 🎯 **Watermark-Free**: Default generation without watermarks (watermarks can be removed in the bigmodel.cn security management)

## API Key Application

Before using this server, you need to apply for an API Key on the BigModel.cn platform. The models are available for free.

### Application Steps

1. **Visit the BigModel Open Platform**

   - Open your browser and visit: [https://www.bigmodel.cn/claude-code?ic=QHPPFCALMK](https://www.bigmodel.cn/claude-code?ic=QHPPFCALMK)
   - Click "Login" or "Register" in the upper right corner

2. **Register/Login Account**

   - Register an account using a phone number or email
   - Complete real-name verification (as required by the platform)
   - Log in to the developer console

3. **Get API Key**
   - Click on the profile icon in the upper right corner, find the API Key, and click to enter
   - Add a new API Key (keep it confidential)

### Cost Explanation

- **Free Quota**: New users typically receive a certain amount of free call quota
- **Billing Method**: Billed based on actual call count and resource usage
- **Balance Inquiry**: You can check the balance and usage in the console
- **Recharge Methods**: Supports multiple online recharge methods

### Model Pricing

| Model Type | Model Name        | Cost Type    | Recommended Scenarios             |
| ---------- | ----------------- | ------------ | --------------------------------- |
| Image Generation | cogview-3-flash | Free/Low Cost | Rapid prototyping, daily use      |
| Image Generation | cogview-4       | Paid         | High-quality images, professional use |
| Video Generation | cogvideox-flash | Free         | Rapid video generation            |
| Video Generation | cogvideox-3     | Paid         | Standard quality videos           |

> 💡 **Recommendation**: It is recommended to use the free model (cogview-3-flash) during development and testing phases, and choose paid models for production environments based on needs.

### API Key Usage Precautions

- 🔒 **Confidentiality**: Treat the API Key as a password; do not expose it in code repositories
- ✅ **Permissions**: Ensure that the API Key has permission to access the required model services
- 🔄 **Rotation**: Regularly rotate the API Key to enhance security
- 📊 **Monitoring**: Regularly check API usage and cost

## Usage

### MCP Configuration

Add the following to your MCP client configuration:

plaintext
```json
{
  "mcpServers": {
    "image-video-generation": {
      "command": "npx",
      "args": ["-y", "image-video-generation-mcp@latest"],
      "env": {
        "IMAGE_VIDEO_GENERATION_API_KEY": "your_api_key"
      },
      "type": "stdio"
    }
  }
}
```
## Default Models

- **Image Generation**: `cogview-3-flash` (free model, fast generation)
- **Video Generation**: `cogvideox-flash` (fast video generation)

### Environment Variable Description

| Environment Variable                                     | Required | Default Value            | Description             |
| -------------------------------------------------------- | -------- | ------------------------ | ----------------------- |
| `IMAGE_VIDEO_GENERATION_API_KEY`                         | ✅       | -                        | API Key                 |
| `IMAGE_VIDEO_GENERATION_DEFAULT_IMAGE_MODEL`             | ❌       | `cogview-3-flash`        | Default image generation model |
| `IMAGE_VIDEO_GENERATION_DEFAULT_VIDEO_MODEL`             | ❌       | `cogvideox-flash`        | Default video generation model |

### Supported Tools

#### 1. generate_image

Generates an image, supporting the following parameters:

- `prompt` (required): Text description of the image
- `model`: Model selection (`cogview-4`, `cogview-4-250304`, `cogview-3-flash`)
- `quality`: Image quality (`standard`, `hd`)
- `size`: Image size (e.g., `1024x1024`)
- `watermark_enabled`: Whether to add a watermark
- `user_id`: User tracking ID

#### 2. generate_video

Generates a video, supporting the following parameters:- `prompt` (required): Video description text (maximum 512 characters)
- `model`: Model selection (`cogvideox-3`, `cogvideox-2`, `cogvideox-flash`)
- `quality`: Output quality mode (`speed`, `quality`)
- `size`: Video resolution (e.g., `1920x1080`)
- `fps`: Frame rate (30, 60)
- `duration`: Video length (5, 10 seconds)
- `with_audio`: Whether to enable AI-generated audio
- `watermark_enabled`: Whether to control watermark

#### 3. query_video_result

Query the result of an asynchronous video generation task:

- `task_id` (required): The ID returned by the video generation task

#### 4. wait_for_video

Wait for the video generation to complete and return the result:

- `task_id` (required): Task ID
- `max_wait_time`: Maximum waiting time (default 300000 milliseconds)
- `poll_interval`: Polling interval (default 5000 milliseconds)

#### 5. configure_models

Configure default models and settings:

- `default_image_model`: Default image generation model
- `default_video_model`: Default video generation model
- `timeout`: Request timeout
- `max_retries`: Maximum number of retries

## Troubleshooting

### MCP Connection Issues

If you encounter issues connecting to MCP, please check the following:

1. **API Key Configuration**: Ensure that the `IMAGE_VIDEO_GENERATION_API_KEY` environment variable is correctly set.

2. **Network Connection**: Ensure that you can access `https://open.bigmodel.cn/api`.

3. **Version Issues**: Use the latest version
```bash
   # Clear the npm cache and use the latest version
   npm cache clean --force
   npx -y image-video-generation-mcp@latest
```
4. **Configuration File Format**: Ensure that the MCP configuration file format is correct.
```json
   {
     "mcpServers": {
       "image-video-generation": {
         "command": "npx",
         "args": ["-y", "image-video-generation-mcp@latest"],
         "env": {
           "IMAGE_VIDEO_GENERATION_API_KEY": "your_bigmodel_api_key"
         },
         "type": "stdio"
       }
     }
   }
```
### Common Errors

- **"API Key is required"**: You need to set the `IMAGE_VIDEO_GENERATION_API_KEY` environment variable.
- **"command not found"**: npm cache issue, try clearing the cache or wait a few minutes.
- **Connection Timeout**: Check your network connection and firewall settings.

## Support

If you have any issues, please submit [GitHub Issues](https://github.com/156554395/image-video-generation-mcp/issues).

## Related Links

- [BigModel API Documentation](https://docs.bigmodel.cn/)
- [MCP Protocol](https://modelcontextprotocol.io/)

**Official site: ** [https://github.com/156554395/image-video-generation-mcp](https://github.com/156554395/image-video-generation-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `entertainment and media`, `developer tools`, `文生图`, `文生视频`, `图片和视频`, `生成图片`, `生成视频`, `视频生成`, `图片生成`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y image-video-generation-mcp@latest`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/seostar-image-video-generation.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
