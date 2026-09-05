---
title: "DoubaoMCPServer-MCP_Agent_Challenge"
description: "Doubao MCP Server 项目简介"
---

# DoubaoMCPServer-MCP_Agent_Challenge

Doubao MCP Server 项目简介

# Doubao MCP Server

## Project Overview

Doubao MCP Server is an MCP (Model Context Protocol) server based on the Volcano Engine Doubao API, providing powerful multimodal generation capabilities for AI clients. The project was developed with the aim of integrating the advanced AI generation capabilities of Volcano Engine Doubao into various AI clients that support the MCP protocol, allowing users to directly use features such as text-to-image, text-to-video, and image-to-video in their familiar development environments.

**Core Functional Features:**

- **Text-to-Image**: Generate high-quality images based on textual descriptions
- **Text-to-Video**: Generate video content based on textual descriptions
- **Image-to-Video**: Generate dynamic videos based on images and textual descriptions
- **Image Encoding**: Support conversion of local image files to base64 encoding
- **Model Configuration**: Support selection from multiple Doubao AI models

**Supported AI Models:**

- Text-to-Image Model: `doubao-seedream-3-0-t2i-250415`
- Image-to-Video Model: `doubao-seedance-1-0-lite-i2v-250428`
- Text-to-Video Model: `doubao-seedance-1-0-lite-t2v-250428`

## Deployment Guide

### **Environment Dependencies**

- Python >= 3.13
- Volcano Engine Doubao API Key

### **Installation Methods**

**Method One: Install using pip**

bash
pip install doubao-mcp-server

**Method Two: Install using uvx (Recommended)**

bash
uvx doubao-mcp-server

### **Client Configuration**

#### **Cursor Configuration**

Add the following configuration to the `~/.cursor/mcp.json` file:

json
{
  "mcpServers": {
    "doubao-mcp-server": {
      "command": "uvx",
      "args": [
        "doubao-mcp-server"
      ],
      "env": {
        "DOUBAO_API_KEY": "your-api-key-here"
      }
    }
  }
}

#### **Cherry Studio Configuration**

1. Open Cherry Studio

2. Go to **Settings → MCP Servers → Add Server**

3. Configure the parameters:
   - **Name**: `doubao-mcp-server`
   - **Description**: `Doubao AI Generation Service`
   - **Type**: `STDIO`
   - **Command**: `uvx`
   - **Arguments**: `doubao-mcp-server`
   - **Environment Variables**: `DOUBAO_API_KEY=your-api-key-here`
   
4. Click Save and Enable

   Detailed Diagrams

   ![image-20250615165107667](/mcp-assets/e99fa0dc242f4458043f32eab6f491c7.png)

![image-20250615165205135](/mcp-assets/bc21e97a249a4dc5eabc56c2bee8b6bd.png)

After configuration, you can check which tools are available

![image-20250615165249803](/mcp-assets/7be6db8636e04a55c5b7c0405a430ab9.png)

#### **Claude Desktop Configuration**

Add the following to the `claude_desktop_config.json` file:

json
{
  "mcpServers": {
    "doubao-mcp-server": {
      "command": "uvx",
      "args": ["doubao-mcp-server"],
      "env": {
        "DOUBAO_API_KEY": "your-api-key-here"
      }
    }
  }
}

#### **Continue.dev Configuration**

Add the following to the `config.json` file:

json
{
  "mcpServers": [
    {
      "name": "doubao-mcp-server",
      "command": "uvx",
      "args": ["doubao-mcp-server"],
      "env": {
        "DOUBAO_API_KEY": "your-api-key-here"
      }
    }
  ]
}

### **API Key Acquisition**

1. Visit the [Volcano Engine Console](https://console.volcengine.com/)

2. Register and log in to your account

3. Activate the Doubao large model service (you need to authorize each model separately)

   For Volcano Engine models, you need to authorize each one separately. Click on the management link to activate.

   ![image-20250614201840722](/mcp-assets/614d57a29c6e627aa0e2f4bd29ac1cf6.png)

4. Create an API key in the API Management section

   API Management

   ![image-20250614201758573](/mcp-assets/b93179c87ed7356f066ab2da6c3a447c.png)

## Available Tools

### **1. set_api_key**

Set the Doubao API key

- `api_key` (string): Doubao API key

### **2. text_to_image**

Generate an image based on a textual description

- `prompt` (string): Description prompt for the image
- `size` (string, optional): Image size, default is "1024x1024"
- `model` (string, optional): Model name

**Supported Image Sizes**: 512x512, 768x768, 1024x1024, 1024x1792, 1792x1024

### **3. text_to_video**

Generate a video based on a textual description

- `prompt` (string): Description prompt for the video- `duration` (string, optional): Video duration in seconds, default "5"
- `ratio` (string, optional): Video aspect ratio, default "16:9"
- `model` (string, optional): Model name

**Supported video ratios**: 16:9, 9:16, 1:1

### **4. image_to_video**

Generates a video based on an image and a text description.

- `prompt` (string): Prompt for the video description
- `image_base64` (string): Base64 encoded string of the image
- `duration` (string, optional): Video duration in seconds, default "5"
- `ratio` (string, optional): Video aspect ratio, default "16:9"
- `model` (string, optional): Model name

### **5. encode_image_to_base64**

Encodes a local image file into a base64 string.

- `image_path` (string): Path to the image file

## Usage Examples

### **Text-to-Image Example**

Use the text_to_image tool to generate an image of "sunset by the seaside".

### **Text-to-Video Example**

Use the text_to_video tool to generate a 5-second video of "a cat playing in the garden".

### **Image-to-Video Example**

First, use encode_image_to_base64 to encode the image, then use image_to_video to generate the video.

  Illustrative case (text-to-image)

  ![image-20250615165711353](/mcp-assets/cea13a747b0ab53f739e9ef3863cfaee.png)

Text-to-video

![image-20250615165906609](/mcp-assets/c26cb67a405392321c30401d037ce070.png)

Generated video

![image-20250615170034340](/mcp-assets/1018befe1bbf7c254299dfa65df85f7b.png)

## Notes

- Video generation tasks may take a long time to complete, please be patient.
- Ensure that your API key has sufficient quota.
- The URLs of generated content are time-limited, please save them promptly.

## Troubleshooting

### **Common Issues**

1. **API Key Error**: Make sure the API key is correct and valid.
2. **Network Connection Issue**: Check your network connection and firewall settings.
3. **Model Unavailable**: Confirm that the model name is correct.

### **Debug Mode**

Enable detailed log output:

bash
uvx doubao-mcp-server --verbose

## Project Information

**License**: MIT License

**Author**: wwzhouhui - [75271002@qq.com](mailto:75271002@qq.com)

**Version**: v0.1.0

- Initial version release
- Supports text-to-image, text-to-video, and image-to-video functionalities
- Integrated with Volcano Engine Doubao API

**Contributions**: Feel free to submit Issues and Pull Requests to improve this project.

**Official site: ** [https://github.com/wwwzhouhui/doubao_mcp_server](https://github.com/wwwzhouhui/doubao_mcp_server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `developer tools`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `doubao-mcp-server`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/wwwzhouhui-doubaomcpserver-agent-challenge.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
