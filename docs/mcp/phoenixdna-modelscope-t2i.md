---
title: "modelscope-t2i-mcp"
description: "Project Overview With the current popularity of text-to-image AIGC, this MCP service has been created to generate images using specified models and save them locally. Currently, it only supports four…"
---

# modelscope-t2i-mcp

Project Overview With the current popularity of text-to-image AIGC, this MCP service has been created to generate images using specified models and save them locally. Currently, it only supports four…

## Project Overview
    With the current popularity of text-to-image AIGC, this MCP service has been created to generate images using specified models and save them locally. Currently, it only supports four models from ModelScope; details are provided later.
    Call the `generate_image` interface to generate an image and record the time taken.
    On success, it returns a tuple containing the path, width, height, and time taken; on failure, it returns None.

## Deployment Guide

### Environment Dependencies:
Node.js 18+ or Python 3.8+ (choose based on your actual runtime environment)

### Configuration Instructions
Refer to the following JSON configuration format (SSE transport as an example):
json
{
  "mcpServers": {
    "your-server-name": {
      "args": [
        "mcp-remote",
        "https://phoenixdna-t2i-modelscope-mcp.ms.show/gradio_api/mcp/sse",
        "--transport",
        "sse-only"
      ],
      "command": "npx"
    }
  }
}

## Usage Examples
### Parameter Explanation:
    Args:
        prompt (str): The prompt for image generation.
        model (str): The name of the model to use, for example:
            - "black-forest-labs/FLUX.1-Krea-dev"
            - "Qwen/Qwen-Image"
            - "MusePublic/489_ckpt_FLUX_1"
            - "MusePublic/flux-high-res"
        width (int): The width of the image in pixels.
        height (int): The height of the image in pixels.

    Returns:
        Optional[Tuple[str, int, int, float]]:
            - fpath (str): The local file path where the generated image is saved.
            - width (int): The width of the generated image.
            - height (int): The height of the generated image.
            - elapsed (float): The time taken to generate the image, in seconds, rounded to 1 decimal place.

            If the generation fails, it returns None.

### Example:
    Example:
        >>> result = generate_gradio(
        ...     prompt="Bamboo forest and mountain peaks, sea of clouds, drone perspective",
        ...     model="Qwen/Qwen-Image",
        ...     width=1024,
        ...     height=1024
        ... )
        >>> print(result)
        ('results/success_20250829-193011.jpg', 1024, 1024, 8.7)
    """

**Official site: ** [https://www.modelscope.cn/studios/phoenixdna/t2i-modelscope-mcp](https://www.modelscope.cn/studios/phoenixdna/t2i-modelscope-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `entertainment and media`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `mcp-remote https://phoenixdna-t2i-modelscope-mcp.ms.show/gradio_api/mcp/sse --transport sse-only`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/phoenixdna-modelscope-t2i.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
