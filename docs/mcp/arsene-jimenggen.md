---
title: "jimenggen-mcp"
description: "Jimeng AI Full Capability Generation MCP Service Jimeng AI Full Capability Generation MCP Service is an AI image and video generation tool based on the Model Context Protocol (MCP), integrating the po…"
---

# jimenggen-mcp

Jimeng AI Full Capability Generation MCP Service Jimeng AI Full Capability Generation MCP Service is an AI image and video generation tool based on the Model Context Protocol (MCP), integrating the po…

# Jimeng AI Full Capability Generation MCP Service

[![License: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://opensource.org/licenses/MIT)
[![TypeScript](/mcp-assets/6c2f12dd7529236aa9edfab30fbcfcd9.svg)](https://www.typescriptlang.org/)
[![MCP](/mcp-assets/87f72c275fb39706595cd53d5a0896ca.svg)](https://modelcontextprotocol.io/)

Jimeng AI Full Capability Generation MCP Service is an AI image and video generation tool based on the Model Context Protocol (MCP), integrating the powerful generation capabilities of ByteDance's Jimeng AI.

github: https://github.com/ARSENE2630/jimenggen-mcp

## ✨ Core Features

### 🎨 Image Generation
- **Text-to-Image 3.1**: Generate high-quality images based on text descriptions.
- **Image-to-Image 3.0**: Generate new images based on reference images.
- **Image Generation 4.0**: The latest version of the image generation model (planned).

### 🎬 Video Generation
- **Video Generation 3.0 Pro**: Generate high-quality videos based on text descriptions.

### 👗 Image Dressing
- **Image Dressing V2**: Intelligent clothing replacement function.

## 🚀 Quick Start

### Environment Requirements
- Node.js 18+
- TypeScript 5.7.2+

### Install Dependencies
bash
npm install

### Configure Environment Variables
Create a `.env` file and configure the ByteDance API keys:
env
JIMENG_ACCESS_KEY=your_access_key_here
JIMENG_SECRET_KEY=your_secret_key_here

### Build the Project
bash
npm run build

### Run Tests
bash
npm test

### Quick Start (quick start)

#### Client Configuration (IDE)

Add the following configuration to the MCP configuration files in MCP clients such as Claude, Trae, and cursor:

json
{
  "mcpServers": {
    "jimenggen": {
      "command": "npx",
      "args": [
        "jimenggen-mcp@1.0.5"
      ],
      "env": {
        "JIMENG_ACCESS_KEY": "your_access_key_here",
        "JIMENG_SECRET_KEY": "your_secret_key_here=="
      }
    }
  }
}

#### Local Run Configuration

json
{
  "mcpServers": {
    "jimenggen": {
      "command": "node",
      "args": [
        "/path/to/jimenggen-mcp/build/index.js"
      ],
      "env": {
        "JIMENG_ACCESS_KEY": "your_access_key_here",
        "JIMENG_SECRET_KEY": "your_secret_key_here"
      }
    }
  }
}

## 📋 Available Tools

### Text-to-Image
Generate images based on text prompts, supporting custom aspect ratios and multiple artistic styles.

**Parameters:**
- `prompt`: Image generation prompt
- `ratio`: Image aspect ratio, supports customization
- `style`: Image style (realistic, guochao, cyberpunk, etc.)

### Image-to-Image
Generate new images based on reference images, supporting style transfer and content editing.

### Text-to-Video
Generate high-quality video content based on text descriptions.

### Image Dressing
Intelligent clothing replacement function, supporting multiple clothing types and retention options.

## 🔧 Technical Architecture

### Core Technology Stack
- **Runtime**: Node.js + TypeScript
- **Protocol**: Model Context Protocol (MCP)
- **HTTP Client**: node-fetch
- **Image Processing**: sharp
- **Data Validation**: zod

### Project Structure
plaintext
jimenggen-mcp/
├── src/
│   ├── index.ts          # Main entry file
│   └── test.ts           # Test file
├── build/                # Compilation output directory
├── package.json          # Project configuration
├── tsconfig.json         # TypeScript configuration
└── README.md            # Project documentation

## 🔑 API Configuration

### ByteDance Jimeng AI
This project uses the ByteDance Jimeng AI service, which requires the following parameters:
- **Endpoint**: `https://visual.volcengineapi.com`
- **Region**: `cn-north-1`
- **Service**: `cv`

### Supported Models
- `jimeng_t2i_v31` - Text-to-Image 3.1
- `jimeng_i2i_v30` - Image-to-Image 3.0
- `jimeng_ti2v_v30_pro` - Video Generation 3.0 Pro
- `dressing_diffusionV2` - Image Dressing V2
- `jimeng_t2i_v40` - Image Generation 4.0

## 🎯 Usage Examples

### Text-to-Image Example
javascript
// Generate a cyberpunk-style future city image
await textToImage({
  prompt: "Future city night scene, neon lights, cyberpunk style",
  ratio: { width: 1024, height: 768 },
  style: "cyberpunk"
});

### Image-to-Image Example
javascript
// Generate a new style image based on an existing image
await imageToImage({
  prompt: "Convert this photo to oil painting style",
  imageUrl: "https://example.com/original.jpg",
  style: "oil painting"
});## 🔍 Debugging Information

When the service starts, it will display the results of the environment variable check:
 
🔍 MCP Server Startup - Environment Variable Check:
📋 Current Environment Variable Status:
   JIMENG_ACCESS_KEY: ✅ Set (Length:20)
   JIMENG_SECRET_KEY: ✅ Set (Length:40)

## 📝 Development Guide

### Adding New Tools
1. Register new MCP tools in `src/index.ts`
2. Implement the corresponding API call functions
3. Update type definitions and parameter validation
4. Add test cases

### Extending Model Support
1. Add new model mappings in `MODEL_MAPPING`
2. Configure API parameters in `API_CONFIG_MAPPING`
3. Implement the corresponding invocation logic

## 🐛 Troubleshooting

### Common Issues
1. **API Call Failure**: Check if the environment variable configuration is correct
2. **Image Generation Timeout**: Adjust the polling interval and maximum number of attempts
3. **Insufficient Memory**: Optimize image processing logic, use streaming processing

### Debug Mode
Set the `DEBUG=true` environment variable to enable detailed log output.

## 🤝 Contribution Guidelines

Feel free to submit Issues and Pull Requests to improve the project!

### Development Workflow
1. Fork the project
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is open-sourced under the MIT License - see the [LICENSE](https://github.com/ARSENE2630/jimenggen-mcp/blob/HEAD/LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to Volcano Engine for providing the powerful Jimeng AI service
- Thanks to the Model Context Protocol community
- Thanks to all contributors and users

## 📞 Contact

If you have any questions or suggestions, please contact us through the following methods:
- Submit a GitHub Issue
- Send an email to the project maintainers

## Version History

- **v1.0.0**: Initial version, supporting basic text-to-image, image-to-image, video generation, and image transformation features

## Appreciation

If this project has been helpful to you, feel free to show your support with a donation!

---

**Note**: Use of this service requires compliance with the terms of service and usage guidelines of Volcano Engine's Jimeng AI.

**Official site: ** [https://github.com/ARSENE2630/jimenggen-mcp](https://github.com/ARSENE2630/jimenggen-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`, `media`
- Tags: `entertainment and media`, `art and culture`, `developer tools`, `文生图`, `图生图`, `视频生成`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `jimenggen-mcp@1.0.5`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/arsene-jimenggen.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
