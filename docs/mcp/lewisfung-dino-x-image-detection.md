---
title: "DINO-X-Image-Detection-MCP"
description: "DINO-X MCP enables large language models to perform fine-grained object detection and image understanding through the DINO-X and Grounding DINO 1.6 APIs. It allows precise localization of visual conte…"
---

# DINO-X-Image-Detection-MCP

DINO-X MCP enables large language models to perform fine-grained object detection and image understanding through the DINO-X and Grounding DINO 1.6 APIs. It allows precise localization of visual conte…

# DINO-X MCP

[English](https://github.com/IDEA-Research/DINO-X-MCP/blob/HEAD/README.md) | **Chinese**

The official DINO-X MCP server, based on the world-leading visual detection models DINO-X and Grounding DINO 1.6 APIs, providing fine-grained object detection and image understanding capabilities to large models.

## Why DINO-X MCP?

Although multimodal models can understand and describe images, they often lack precise localization of visual content and high-quality structured output.

With DINO-X MCP, you can:

- Achieve fine-grained image understanding: supports whole-image recognition and targeted detection.
- Precisely obtain object count, location, and attributes, and use them as a basis for image Q&A and other tasks.
- Combine with other MCP Servers to build multi-step visual workflows.
- Build natural-language-driven visual agents for automation tasks in real scenarios.

## Application Examples

| Scenario | Input | Output |
|---------|---------|---------|
| **Detection & localization** | Prompt: "Help me select the fire-affected area in the forest and visualize it with Canvas" + Input image | Result |
| **Object counting** | Prompt: "Please analyze this warehouse image, detect all the cardboard boxes in it, and count the total" + Input image | Result |
| **Feature detection** | Prompt: "Find all the red cars in the image and visualize them with Canvas" + Input image | Result |
| **Attribute reasoning** | Prompt: "Find the tallest person in the image, describe their clothing, and visualize with Canvas" + Input image | Result |
| **Whole-image detection** | Prompt: "Find the fruit with the highest vitamin C content in the image" + Input image | Answer: kiwi (93mg/100g) |
| **Pose analysis** | Prompt: "Please analyze what yoga pose this is and display the key points with Canvas" + Input image | Result |

## Quick Start

### 1. Environment preparation

You can install Node.js using any of the following methods:

#### Method 1: Use the install script

```bash
# MacOS or Linux
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
source ~/.bashrc  # if using zsh, run: source ~/.zshrc
nvm install --lts

# Windows
winget install OpenJS.NodeJS.LTS
# or use PowerShell (as administrator)
iwr -useb https://raw.githubusercontent.com/chocolatey/chocolatey/master/chocolateyInstall/InstallChocolatey.ps1 | iex
choco install nodejs-lts -y
```

#### Method 2: Manual download and install

Download the installer from the [Node.js official website](https://nodejs.org/)

Also, choose an MCP-protocol-supporting AI assistant or client, including but not limited to:

- [Cursor](https://www.cursor.com/)
- [WindSurf](https://windsurf.com/)
- [Trae](https://www.trae.ai/)
- [Cherry Studio](https://www.cherry-ai.com/)

### 2. Configure the MCP server

#### Method 1: Use the NPM package

Add the configuration to your MCP client's config file:

```json
{
  "mcpServers": {
    "dinox-mcp": {
      "command": "npx",
      "args": ["-y", "@deepdataspace/dinox-mcp"],
      "env": {
        "DINOX_API_KEY": "you-api-key-here"
      }
    }
  }
}
```

#### Method 2: Use a local project

First, clone this project locally and build it:

```bash
# Download the source code
git clone https://github.com/IDEA-Research/DINO-X-MCP.git
cd DINO-X-MCP

# Install dependencies
pnpm install

# Build
pnpm run build
```

Then configure it in the MCP client:

```json
{
  "mcpServers": {
    "dinox-mcp": {
      "command": "node",
      "args": ["/path/to/DINO-X-MCP/build/index.js"],
      "env": {
        "DINOX_API_KEY": "you-api-key-here"
      }
    }
  }
}
```

### 3. Get an API key

Register an account at the [DINO-X official website](https://cloud.deepdataspace.com/request_api); new users get free API quota.

After getting the API key, replace `you-api-key-here` in the configuration above with the real key.

### 4. Supported tools

After refreshing the MCP configuration, you can use the following features in large-model conversations:

| Feature | Function | Input | Output |
| ----------------------------- | ---------------------------------------------------------------------------- | ------------------- | ------------------------------- |
| Whole-image detection | Detect and localize all recognizable objects in the image | image link | name of each object + 2D box + detailed description |
| Targeted object detection | Specify one or more targets and detect their positions and detailed descriptions | image link + target names | 2D boxes of all specified targets + detailed description |
| Human pose detection | Detect 17 key points of each person in the image for pose/action analysis | image link | key point coordinates + description |

## Usage Guide

### Which image formats are supported?

- We recommend image links starting with `https://`
- Or full paths starting with `file://`
- Common formats: `jpg`, `jpeg`, `png`, `webp`

### API usage

See the [DINO-X API documentation](https://cloud.deepdataspace.com/docs).

## Developer Guide

If you want to modify this MCP service, you can enable watch mode; code changes will be recompiled automatically:

```bash
pnpm run watch
```

When you run into problems, use the official debug tool:

```bash
pnpm run inspector
```

## License

Apache License 2.0

**Official site: ** [https://github.com/IDEA-Research/DINO-X-MCP](https://github.com/IDEA-Research/DINO-X-MCP)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `developer tools`, `research and data`, `entertainment and media`, `目标检测`, `图像理解`, `图像识别`, `姿态估计`, `mcp`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @deepdataspace/dinox-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/lewisfung-dino-x-image-detection.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
