---
title: "jimengpic-mcp"
description: "即梦AI图片生成 MCP 服务 基于火山引擎即梦AI的图片生成MCP（Model Context Protocol）服务。"
---

# jimengpic-mcp

即梦AI图片生成 MCP 服务 基于火山引擎即梦AI的图片生成MCP（Model Context Protocol）服务。

# Jimeng AI Image Generation MCP Service

Based on the Jimeng AI image generation MCP (Model Context Protocol) service from Volcengine.

## Features

- Generate high-quality images using the Volcengine Jimeng AI API
- Supports multiple image ratios: 4:3, 3:4, 16:9, 9:16
- Standardized MCP interface, compatible with various MCP clients
- Environment variable configuration for security and convenience

## Install Dependencies

bash
cd jimengpic-mcp
npm install

## Build the Project

bash
npm run build

## Environment Variable Configuration

Set the following environment variables:

bash
export JIMENG_ACCESS_KEY="Your Volcengine AccessKey"
export JIMENG_SECRET_KEY="Your Volcengine SecretKey"

### Obtain API Keys

1. Visit the [Volcengine Console](https://console.volcengine.com/)
2. After logging in, go to the "Jimeng AI" product page and activate the service (you can choose a free trial)
3. On the "Access Control" page, create an access key to obtain the Access Key and Secret Key
4. Ensure that your account has the necessary permissions and policies for Jimeng AI image generation

**Note:** According to the official documentation, make sure to use the correct `req_key` parameter value `jimeng_high_aes_general_v21_L`.

## Usage

### Run Directly

bash
node build/index.js

### As an MCP Server

Configure this service in an MCP client (such as Claude Desktop, Cursor, etc.):

json
{
  "mcpServers": {
    "jimengpic": {
      "command": "node",
      "args": ["/path/to/jimengpic-mcp/build/index.js"],
      "env": {
        "JIMENG_ACCESS_KEY": "Your AccessKey",
        "JIMENG_SECRET_KEY": "Your SecretKey"
      }
    }
  }
}

## API Endpoints

### generate-image

A tool used when users need to generate images.

**Parameters:**
- `text` (string): The text that the user wants to display on the image
- `illustration` (string): 3-5 keywords for illustration elements that can be used as accessories based on the text to be displayed
- `color` (string): The main background color of the image
- `ratio` (enum): The aspect ratio of the image, supporting the following options:
  - `"4:3"`: 512×384
  - `"3:4"`: 384×512  
  - `"16:9"`: 512×288
  - `"9:16"`: 288×512

**Prompt Generation Rules:**
The tool will automatically combine the input parameters into a prompt in the following format:

Font design: "{text}", black font, italic, with shadow. Clean background, white to {color} gradient. Decorated with light gray, semi-transparent {illustration} and other illustrative elements.

**Returns:**
- On success, returns the image URL and detailed information
- On failure, returns an error message

## Example Usage

typescript
// Call in an MCP client
const result = await mcp.callTool("generate-image", {
  text: "Happy New Year",
  illustration: "fireworks, lanterns, auspicious clouds, stars, fireworks",
  color: "red",
  ratio: "4:3"
});

## Project Structure

jimengpic-mcp/
├── src/
│   └── index.ts          # Main service file
├── build/                # Compiled output directory
├── package.json          # Project configuration
├── tsconfig.json         # TypeScript configuration
└── README.md            # Project description

## Notes

1. Ensure that the network connection is normal and can access the Volcengine API
2. API calls consume credits, so please be mindful of usage
3. The generated image URLs have a time limit, it is recommended to download and save them promptly
4. Please comply with Volcengine's terms of use and Jimeng AI content policies

## Troubleshooting

### Common Errors

1. **Environment variables not set**: Ensure that the correct ACCESS_KEY and SECRET_KEY are set
2. **Network connection issues**: Check the network connection and firewall settings
3. **Insufficient API quota**: Check the Volcengine account balance and API call count
4. **Non-compliant prompts**: Ensure that the prompts comply with content safety guidelines

### Debugging Methods

Add debug information when running:
bash
DEBUG=* node build/index.js

## License

ISC License

**Official site: ** [https://github.com/comeonzhj/jimengpic-mcp](https://github.com/comeonzhj/jimengpic-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `art and culture`

## MCP Configuration

- Transport: `stdio`
- Command: `node`
- Args: `/path/to/jimengpic-mcp/build/index.js`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/comeonzhj-jimengpic.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
